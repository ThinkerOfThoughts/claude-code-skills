#!/usr/bin/env python3
"""ere-probe.py <tree-root> '<ERE>' — print the MEASURED file set (and hit lines) for a SITE_PATTERN.

Exists so a criteria row's SITE_PATTERN can be TUNED AGAINST THE MEASUREMENT instead of guessed and
then contradicted by the measurement file it cites. Reviewer F/1's blocker in pass 2 was exactly
"the measured site sets are not the measurement".
"""
import re,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from checklib import corpus,SHORT
root=sys.argv[1]; pat=re.compile(sys.argv[2],re.I)
files=corpus(root); nf=0; nh=0
for f in files:
    hits=[(i+1,l.rstrip()) for i,l in enumerate(open(f,encoding="utf-8",errors="replace"))
          if pat.search(l)]
    if not hits: continue
    nf+=1; nh+=len(hits)
    print(f'{SHORT(os.path.relpath(f,root)):12s} {os.path.relpath(f,root)}')
    for ln,l in hits: print(f'      :{ln}  {l[:110]}')
print(f'MEASURED: {nh} hits in {nf} files')
