# P-DAG-ZFC-SOURCE-029：axiomatized AC / Power Set proof-layer payment prompt

```text
You are a P-VALIDATION source mapper. Use only the frozen primary-source card. Do not
use tools, files, web, project history, prior results, or delegation. Do not provide
hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace.

This is a proof-system-layer regression control. Identify the exact theory/layer,
object, formation, consumer, input/output/Done, and Q. Test L2c, L5b, L6, L7 and
L7b. Distinguish an explicit axiomatization from a definition, a completed theorem
from an open consumer demand, and a proof-system conclusion from an object-level or
runtime witness. Enumerate the shortest packet-visible proof/payment chain. Do not
turn a source theorem into a ZFC inconsistency, executable selector, or real-world
task. State a nearby reading, counterfactual, and bounded status.

BEGIN FROZEN SOURCE CARD
Source identity: isabelle-prover/mirror-isabelle, src/ZF/AC.thy at commit
5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8, SHA-256
8f02e7ec0a2396972a1693572bc046d9906cc430b67b45a072eb1ffbd1e2e126.

The file is an Isabelle/ZF theory importing ZF. It explicitly declares:
  axiomatization where
    AC: [a ∈ A; for every x ∈ A, exists y ∈ B(x)]
        ==> exists z. z ∈ Pi(A,B)

It then proves these source-local steps:
  AC_Pi: if every x ∈ A has a y ∈ B(x), then exists z ∈ Pi(A,B).
  AC_func: if every x ∈ A has a y ∈ x, then exists f ∈ A -> Union(A)
           with f`x ∈ x for every x ∈ A.
  AC_func0: if 0 ∉ A, then the same choice-function conclusion holds.
  AC_func_Pow: exists f ∈ (Pow(C)-{0}) -> C such that for every
               x ∈ Pow(C)-{0}, f`x ∈ x.

The source proves AC_func_Pow from AC_func0, which is proved through AC_func,
AC_Pi, and the axiomatized AC. Treat the card as exactly:
  T = Isabelle/ZF proof system plus its displayed AC axiom;
  u = Pow(C)-{0}; F = Pow plus removing 0;
  consumer = proof-system derivation of AC_func_Pow;
  input = C and the source proof environment containing AC;
  output = an accepted proof of the existential choice-function statement;
  Done = theorem acceptance in that proof system;
  Q = the existential conclusion of AC_func_Pow.

The source does not supply an object-level/runtimes consumer or a named executable f.
It is not a claim that bare ZF proves Choice and it is not a standard-ZFC Q result.
END FROZEN SOURCE CARD
```
