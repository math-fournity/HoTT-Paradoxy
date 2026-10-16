# P-DAG-TOOL-BIRTH-058：Mathlib NFA 幂集状态消费者 source-match prompt

```text
You are a P-VALIDATION source mapper.
Use only the frozen local source card. Do not use tools, files, web, project history,
prior results, or delegation. Do not provide hidden chain-of-thought. Return E0 through
E7 as a concise public MatchTrace.

Assess a potential trace/snapshot/identity pattern. Distinguish: concrete paths, the
set-of-possible-endpoints representation, language-acceptance consumer, its I/O/Done,
and a diachronic identity task. Map P1/P2/P3 honestly. Decide whether loss of individual
path identity is an error for this source's stated acceptance task, and whether it
supports a Tool-Birth candidate. Do not claim a theory defect, Power Set/ZFC Q, new tool,
UR, or theorem beyond the source card.

BEGIN FROZEN SOURCE CARD
Source: Mathlib/Computability/NFA.lean, SHA-256
42d15719f191c3125a1ec01be3f655471469df419420fdb76ad87ac1b342ab02.

The source describes an NFA as a state machine deciding language membership by possible
paths. Its transition has type `step : σ → α → Set σ`; start and accept are `Set σ`.
`stepSet S a` is the union of transitions from states in S. `evalFrom S x` is a fold of
stepSet and returns `Set σ`, described as all possible ending states for word x from S.

`acceptsFrom S` is the language whose words have an accepting state in `evalFrom S x`;
the source defines acceptance by existence of an accepting endpoint in that result set.

Separately, `Path` is an inductive type representing a concrete path for a particular
word. The source proves membership in `evalFrom {s} x` iff there is a nonempty concrete
Path from s to that endpoint. Thus it has both a path representation and an endpoint-set
representation. No source text says language acceptance asks whether two paths are the
same continuing artifact, or that path provenance is a Done condition for acceptance.
END FROZEN SOURCE CARD

At E5 output exactly this containment ledger:
  P1 consumer/task: [source fact] => [verdict] — [reason]
  P2 trace/snapshot bridge: [source fact] => [verdict] — [reason]
  P3 stages/Done: [source fact] => [verdict] — [reason]
  history-sensitive identity: [source fact] => [verdict] — [reason]
  tool-birth disposition: [source fact] => [verdict] — [reason]
```
