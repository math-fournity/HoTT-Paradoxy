# P-DAG-ZFC-SOURCE-031：AC / Power Set P3 atomic-formation control prompt

```text
You are a P-VALIDATION source mapper for P3. Use only the frozen primary-source
card. Do not use tools, files, web, project history, prior results, or delegation.
Do not provide hidden chain-of-thought. Return E0 through E7 as a concise public
MatchTrace.

For P3, map only source-supported transitions into Draft, NeedBuild, NeedEval,
Admitted, OperatorUse, and BuildDone. For every claimed state or edge give the source
fact, prerequisite and effect. An existential axiom, completed theorem, or proof-rule
existential elimination does not itself establish a construction lifecycle. Distinguish
a proof-context local witness from object-level construction and real/task realization.
If no actual P3 transition exists, return CONSTRUCTION_SEMANTICS_NOT_SUPPLIED or a more
precise atomic/proof-context control. Do not call any result a ZFC B-direction finding.

BEGIN FROZEN SOURCE CARD
Source identity: isabelle-prover/mirror-isabelle, src/ZF/AC.thy at commit
5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8, SHA-256
8f02e7ec0a2396972a1693572bc046d9906cc430b67b45a072eb1ffbd1e2e126.

The file is an Isabelle/ZF theory importing ZF. It explicitly declares:
  axiomatization where
    AC: [a ∈ A; for every x ∈ A, exists y ∈ B(x)]
        ==> exists z. z ∈ Pi(A,B)

It proves:
  AC_Pi_Pow: exists f. f ∈ product over X in Pow(C)-{0} of X,
              using AC_Pi [THEN exE].
  AC_func: a choice-function existence theorem, using AC_Pi [THEN exE].
  AC_func0: derives the same conclusion under 0 ∉ A.
  AC_func_Pow: exists f ∈ (Pow(C)-{0}) -> C such that every x in the
               nonempty-subset family is mapped into x; its proof applies
               AC_func0 [THEN bexE] and then introduces a bounded witness.

Treat the prospective object as the existentially quantified f and the
prospective operator as proof-level existential elimination/local proof use.
The source gives no runtime scheduler, no construction state for f before the
axiom, no real-world task, and no claim that bare ZF proves AC.
END FROZEN SOURCE CARD
```
