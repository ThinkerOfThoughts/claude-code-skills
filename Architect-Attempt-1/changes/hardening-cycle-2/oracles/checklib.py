#!/usr/bin/env python3
"""Positive per-site assertion runner. Corpus PINNED (see lib-corpus.sh); `changes/` cannot enter.

Three guards pass 2 lacked:
  * SITE SETS ARE MEASURED, NEVER TYPED — each row carries an ERE over the OLD text; the site set is
    whatever files match it in the tree under test. A typo cannot become a false claim.
  * POLARITY GUARD — a pinned string preceded (within 160 normalized chars) by a negation/foil marker
    does NOT count as an assertion. Pass 2's checker would have accepted
    "What pass 1 wrongly said: <pinned string>".
  * KIND — NEW rows must FAIL on the baseline tree, PRESERVE rows must PASS there. That is the
    can-fail self-test, run by baseline-replay.sh.
  * VACUOUS-SITE GUARD (added pass 3, item 10) — a NEW row whose SITE_PATTERN measures ZERO sites
    asserts nothing and FAILS. This is the S-CTX-VAC insight ("path-validation over an absent key
    checks zero paths and passes trivially") applied to the checker itself, and it is what lets a
    CO-OCCURRENCE row be honest: such a row's SITE_PATTERN matches the NEW claim's own phrase, so at
    baseline it measures 0 sites and FAILS there rather than passing vacuously.
"""
import re,sys,os,subprocess
NEG = re.compile(r'(?:wrongly said|was wrong|is wrong|do not state|never state|must not say|superseded|foil|strike|~~|instead of|rather than saying|pass 1 said|previously claimed|no longer)',re.I)
def corpus(root):
    out=[]
    for f in ("SKILL.md","METHODOLOGY.md","README.md"):
        p=os.path.join(root,f)
        if os.path.isfile(p): out.append(p)
    for d in ("stages","templates","examples"):
        dd=os.path.join(root,d)
        for r,_,fs in os.walk(dd):
            for f in sorted(fs):
                if f.endswith(".md"): out.append(os.path.join(r,f))
    return sorted(out)
def norm(s):
    s=s.replace("**","").replace("`","")
    s=re.sub(r'(?<![\w*])\*(?![\s*])','',s); s=re.sub(r'(?<![\s*])\*(?![\w*])','',s)
    return re.sub(r'\s+',' ',s)
SHORTMAP=[("stages/stage-1-frame-template-match.md","s1"),("stages/stage-2-draft-node.md","s2"),
    ("stages/stage-3-completeness-critic.md","s3"),("stages/stage-4-adversarial-redteam.md","s4"),
    ("stages/stage-5-gate.md","s5"),("stages/stage-6-granularity-decompose.md","s6"),
    ("stages/stage-7-assemble.md","s7"),("stages/stage-8-restart-resume.md","s8"),
    ("stages/charter.md","ch"),("templates/seed/README.md","tp/README"),
    ("templates/seed/generic-node.md","tp/generic"),("templates/seed/decomposition-node.md","tp/decomp"),
    ("templates/seed/leaf-task-spec.md","tp/leaf"),
    ("examples/authoring-a-skill/planning.md","ex/planning"),
    ("examples/authoring-a-skill/README.md","ex/README"),
    ("METHODOLOGY.md","M"),("SKILL.md","S"),("README.md","R")]
def SHORT(p):
    for long,short in SHORTMAP:
        if p==long: return short
    return p
def rows(tsv):
    for ln in open(tsv):
        if ln.startswith("#") or not ln.strip(): continue
        p=ln.rstrip("\n").split("\t")
        while len(p)<5: p.append("")
        yield {"id":p[0],"kind":p[1],"pat":p[2],"pin":p[3],"absent":p[4]}
def main():
    args=[a for a in sys.argv[1:] if a!="--sites"]
    list_sites = "--sites" in sys.argv
    root=args[0]; tsv=args[1]; only=args[2] if len(args)>2 else None
    mins={}; mp=os.path.join(os.path.dirname(os.path.abspath(tsv)),"preserve-counts.txt")
    if os.path.exists(mp):
        for ln in open(mp):
            if ln.startswith("#") or not ln.strip(): continue
            k,v=ln.split(); mins[k]=int(v)
    files=corpus(root); texts={f:norm(open(f,encoding="utf-8",errors="replace").read()) for f in files}
    raw  ={f:open(f,encoding="utf-8",errors="replace").read() for f in files}
    fails=0; total=0; results=[]
    for r in rows(tsv):
        if only and r["id"]!=only: continue
        total+=1
        try: pat=re.compile(r["pat"],re.I)
        except re.error as e: print(f"FATAL {r['id']}: bad SITE_PATTERN: {e}"); return 2
        sites=[f for f in files if pat.search(raw[f])]
        pin=norm(r["pin"]).lower(); miss=[]; foil=[]
        for f in sites:
            t=texts[f]; i=t.lower().find(pin)
            if i<0: miss.append(os.path.relpath(f,root)); continue
            if NEG.search(t[max(0,i-160):i]): foil.append(os.path.relpath(f,root))
        bad_abs=[]
        for a in [x for x in r["absent"].split("|") if x.strip()]:
            for f in files:
                if norm(a) in texts[f]: bad_abs.append(f"{os.path.relpath(f,root)}~{a[:40]}")
        erosion=None
        if r["kind"]=="PRESERVE" and r["id"] in mins and len(sites)<mins[r["id"]]:
            erosion=f'{len(sites)} sites, baseline had {mins[r["id"]]}'
        if list_sites:
            sl=" ".join(SHORT(os.path.relpath(f,root)) for f in sites) or "-"
            print(f'{r["id"]}\t{r["kind"]}\t{len(sites)}\t{sl}')
            continue
        vacuous = (r["kind"] in ("NEW","COOC") and not sites)
        ok = not miss and not foil and not bad_abs and erosion is None and not vacuous
        results.append((r["id"],r["kind"],len(sites),ok,miss,foil,bad_abs,erosion,vacuous))
        if not ok: fails+=1
    for rid,kind,n,ok,miss,foil,ba,er,vac in results:
        st="PASS" if ok else "FAIL"
        print(f"{st} {rid:16s} kind={kind:8s} measured_sites={n}")
        for m in miss: print(f"       MISSING-AT   {m}")
        for m in foil: print(f"       FOIL-ONLY    {m}  (pinned string present but negated — polarity guard)")
        for m in ba:   print(f"       ABSENCE-VIOL {m}")
        if er:         print(f"       SITE-EROSION {er}  (PRESERVE non-erosion: config item (6) second half)")
        if vac:        print(f"       VACUOUS      0 measured sites — a NEW row that asserts nothing cannot pass")
    if list_sites: return 0
    print(f"CHECK: {total-fails}/{total} rows PASS  ({fails} FAIL)")
    return 1 if fails else 0
if __name__=="__main__": sys.exit(main())
