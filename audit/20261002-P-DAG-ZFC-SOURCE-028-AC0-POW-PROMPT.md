# P-DAG-ZFC-SOURCE-028：AC0 choice-function / Power Set P1 prompt

```text
You are a P-VALIDATION source mapper. Use only the frozen primary-source card. Do not
use tools, files, web, project history, prior results, or delegation. Do not provide
hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace.

For P1, identify theory scope/layer, subject, formation, consumer, input/output/Done,
and Q if the source actually supplies one. Test L6/L7: distinguish a positive same-task
obligation from a normal false-branch query, and separately test whether any
packet-visible axiom, definition, theorem, or supplied witness already directly pays it.
Do not collapse the Power Set formation rule, an Axiom-of-Choice formulation, and a
well-order conditional theorem into one rule. State a nearby reading, shortest
source-rule chain, counterfactual, and bounded status.

BEGIN FROZEN SOURCE CARD
Source identity: isabelle-prover/mirror-isabelle,
src/ZF/AC/AC_Equiv.thy at commit 5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8,
SHA-256 3953f40986a937b25d3f04072155e05c7e0f4e8fdae6182878b07a3110ad5c6c.

The file imports ZF and says "begin (*obviously not ZFC*)". It records that AC0
comes from Suppes and AC1--AC19 are choice equivalents. It defines:
  AC0 == forall A. exists f. f ∈ (Π X ∈ Pow(A)-{0}. X)
  AC1 == forall A. 0 ∉ A --> exists f. f ∈ (Π X ∈ A. X)

Later it proves the conditional lemma:
  well_ord(A,R) ==> exists f. f ∈ (Π X ∈ Pow(A)-{0}. X)
named ex_choice_fun_Pow.

Treat the prospective candidate as:
T = Isabelle ZF plus the displayed AC0 formulation;
u = Pow(A)-{0};
F = Pow(A) together with removing 0;
C = the dependent product Π X∈u. X;
Q = exists f in C;
Done = f ∈ C.

This source supplies no runtime lifecycle, no claim that bare ZF proves AC0, and
no theorem that AC0 is a computational construction. The task is only to classify
whether Q is a positive obligation and whether the displayed AC0 assertion or the
separate well-order conditional rule directly pays it.
END FROZEN SOURCE CARD
```
