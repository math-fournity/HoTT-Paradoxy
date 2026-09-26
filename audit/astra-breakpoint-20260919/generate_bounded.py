#!/usr/bin/env python3
"""Generate a declared finite Boolean consumer family; its scope excludes arbitrary HoTT terms."""
import hashlib
import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "HoTT/formal/astra-breakpoint-check/BoundedConsumers.agda"
EVIDENCE = ROOT / "audit/astra-breakpoint-20260919/bounded-envelope.json"

def main():
    if OUT.exists() or EVIDENCE.exists():
        if sys.argv[1:] not in (["--repair-missing-import"], ["--repair-id"]):
            raise SystemExit("OUTPUT_EXISTS")
        old = json.loads(EVIDENCE.read_text())
        assert hashlib.sha256(OUT.read_bytes()).hexdigest() == old["source_sha256"]
        assert "id : Bool → Bool" not in OUT.read_text()
        seq = "02" if sys.argv[1:] == ["--repair-id"] else "01"
        backup = ROOT / ("audit/astra-breakpoint-20260919/attempt-sources/20260919-MP-ASTRA-BOUNDED-" + seq)
        backup.mkdir(exist_ok=False)
        (backup / OUT.name).write_bytes(OUT.read_bytes())
        (backup / EVIDENCE.name).write_bytes(EVIDENCE.read_bytes())
    text = ["{-# OPTIONS --safe --cubical --guardedness #-}",
            "module BoundedConsumers where", "open import Cubical.Foundations.Prelude",
            "open import Cubical.Data.Bool", "open import Cubical.Data.Empty",
            "id : Bool → Bool", "id x = x", ""]
    rows = []
    # Bits index [false, true]; the grammar has syntactically different words.
    for depth in range(4):
        for word in itertools.product(("id", "not"), repeat=depth):
            for outputs in itertools.product((False, True), repeat=2):
                ident = "c" + str(len(rows)).zfill(3)
                lit = lambda b: "true" if b else "false"
                text += [f"{ident}f : Bool → Bool",
                         f"{ident}f false = {lit(outputs[0])}",
                         f"{ident}f true = {lit(outputs[1])}"]
                expr = "x"
                for symbol in word:
                    expr = "(" + symbol + " " + expr + ")"
                text += [f"{ident} : Bool → Bool", f"{ident} x = {ident}f {expr}"]
                vals = []
                for b in (False, True):
                    for symbol in word:
                        b = not b if symbol == "not" else b
                    vals.append(outputs[int(b)])
                constant = vals[0] == vals[1]
                if constant:
                    text += [f"{ident}compatible : (a b : Bool) → {ident} a ≡ {ident} b"]
                    for a,b in itertools.product((False,True),repeat=2):
                        text += [f"{ident}compatible {lit(a)} {lit(b)} = refl"]
                else:
                    lemma = "true≢false" if vals[1] else "false≢true"
                    text += [f"{ident}incompatible : ((a b : Bool) → {ident} a ≡ {ident} b) → ⊥",
                             f"{ident}incompatible p = {lemma} (p true false)"]
                text += [""]
                rows.append({"id": ident, "word": list(word), "function_false_true": outputs,
                             "consumer_false_true": vals, "compatible": constant})
    data = ("\n".join(text) + "\n").encode()
    manifest = {"schema": "astra-bounded-consumers/v1", "calculus": "safe Cubical Agda",
                "grammar": "Words of id/not of length 0..3 followed by one of four Bool→Bool truth tables",
                "observation": "Boolean value", "completion": "total evaluation of these closed finite consumers",
                "oracle": "universal relation compatibility, not physical restoration or arbitrary search",
                "denominator": len(rows), "members": rows,
                "source_sha256": hashlib.sha256(data).hexdigest(),
                "independent_count": "4*(1+2+4+8)=60; 2 constant and 2 nonconstant functions per permutation word",
                "no_claim": "No enumeration of arbitrary dependent terms, proof search, or all HoTT consumers"}
    OUT.write_bytes(data)
    EVIDENCE.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"members": len(rows), "compatible": sum(r["compatible"] for r in rows),
                      "independent_formula": 4 * sum(2**n for n in range(4)),
                      "source": str(OUT.relative_to(ROOT))}))

if __name__ == "__main__":
    main()
