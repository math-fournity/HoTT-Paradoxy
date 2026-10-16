#!/usr/bin/env python3
"""Finite illustration of a halting-coded monotone rational approximation.

This script uses a deliberately finite catalogue of toy machines.  It is not a
construction of the true halting set and not a proof of noncomputability.
"""
from fractions import Fraction
import json, pathlib

# None means no halt observed in our toy semantics; integers are halt stages.
halts = {0: 1, 1: None, 2: 4, 3: 2, 4: None, 5: 7}
values=[]
for s in range(10):
    q=Fraction(0,1)
    for e,h in halts.items():
        if e <= s and h is not None and h <= s:
            q += Fraction(1, 4 ** (e+1))
    values.append({"stage":s,"numerator":q.numerator,"denominator":q.denominator,"float":float(q)})
assert all(values[i]["float"] <= values[i+1]["float"] for i in range(len(values)-1))
out={
  "warning":"Finite toy illustration only; it does not decide the halting problem or prove the Specker theorem.",
  "toy_halting_schedule":halts,
  "values":values,
  "monotone":True
}
p=pathlib.Path(__file__).with_name('specker_limit_demo.json')
p.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
