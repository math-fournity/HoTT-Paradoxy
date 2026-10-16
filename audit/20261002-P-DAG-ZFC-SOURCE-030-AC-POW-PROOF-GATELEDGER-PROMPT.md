# P-DAG-ZFC-SOURCE-030：AC / Power Set proof-layer Gate Ledger regression prompt

```text
You are a P-VALIDATION source mapper. Use only the frozen primary-source card. Do not
use tools, files, web, project history, prior results, or delegation. Do not provide
hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace.

This is a proof-system-layer regression control. Use the same exact theory card only.
At the end of E5, output exactly this five-line public Gate Ledger, in this order:
  L2c layer: [source fact] => [verdict] — [reason]
  L5b active-demand status: [source fact] => [verdict] — [reason]
  L6 F-only payment: [source fact] => [verdict] — [reason]
  L7 positive-obligation mode: [source fact] => [verdict] — [reason]
  L7b packet payment: [source fact] => [verdict] — [reason]

Use each label only for its named question. L2c is the declared layer. L5b says whether
Q is a definition, axiom/assumption, current proof goal, completed theorem, conditional
theorem, or supplied witness, and whether it remains active in this card. L6 asks only
whether the powerset formation itself answers Q. L7 asks only whether a consumer's Done
requires Q true. L7b lists whether visible axioms, proved lemmas with supplied premises,
or supplied witnesses directly pay Q. Do not use a claim that no executable witness is
named as an answer to L7b. Do not use formation of u as an answer to L5b.

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

The source does not supply an object-level/runtime consumer or a named executable f.
It is not a claim that bare ZF proves Choice and it is not a standard-ZFC Q result.
END FROZEN SOURCE CARD
```
