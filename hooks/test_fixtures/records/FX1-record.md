# fixture record FX1

ANSWER T1 BEGIN
T1 (where the recall-block wiring test lives): the new tests go in tests/unit/brain/chat/test_stage3_defect3_defect4.py, beside the existing Fix-3 full-open block, not in a new module. They assert: each full-tier memory is reported once per open; snippet-tier memories are not reported; the persona_dir=None legacy path is not reported. [RULE: P7 (reuse the existing test block), P17, P15 | M]
ANSWER T1 END
