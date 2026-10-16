# P-DAG-TOOL-BIRTH-056：Metamath extensionality／Power Set source-match prompt

```text
You are a P-VALIDATION source mapper.
Use only the frozen primary-source card. Do not use tools, files, web, project history,
prior results, or delegation. Do not provide hidden chain-of-thought. Return E0 through
E7 as a concise public MatchTrace.

Assess whether the source supplies the ingredients for a history-sensitive identity task:
trace/provenance representation, a projection to current membership snapshot, a consumer
that treats extensional equality as sufficient for diachronic identity, or a runtime
replacement/admission process. Distinguish P1 object/task, P2 equality/representation
bridge, P3 stages/Done, and proof-system theorem acceptance. Do not invent any missing
consumer or history field. Do not claim a theory defect, ZFC Q, new tool, UR, or theorem.

BEGIN FROZEN SOURCE CARD
Primary URLs read 2026-10-03:
  https://us.metamath.org/mpeuni/ax-ext.html
  https://us.metamath.org/mpeuni/pwex.html

The ax-ext page calls extensionality an axiom of Zermelo-Fraenkel set theory and says
two sets are identical if they contain the same elements. Its displayed assertion is:
  (for all z, z in x iff z in y) implies x = y.
It also describes an equality-free formulation by membership agreement.

The pwex page calls pwex the power set axiom expressed in class notation. It has
hypothesis A in V and assertion power-set(A) in V, obtained by a displayed proof
using a conditional theorem and modus ponens. The page lists ax-ext among dependencies.

Neither page states a replacement-history datatype, a lineage observer, a projection
from traces to snapshots, a consumer task asking diachronic identity, a runtime scheduler,
or a construction/admission lifecycle.
END FROZEN SOURCE CARD

At E5 output exactly this containment ledger:
  P1 object/task: [source fact] => [verdict] — [reason]
  P2 equality/representation: [source fact] => [verdict] — [reason]
  P3 trace/admission: [source fact] => [verdict] — [reason]
  consumer/Done: [source fact] => [verdict] — [reason]
  tool-birth disposition: [source fact] => [verdict] — [reason]
```
