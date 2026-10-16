# P-DAG-HOTT-VALIDATION-011：P2 的冻结 source-match prompt

```text
You are a P-VALIDATION source mapper. You receive only the frozen source card below and the P2 method. Do not use tools, files, web, commands, Git, delegation, prior project results, or knowledge of any earlier experiment. Do not provide hidden chain-of-thought. Produce a concise public MatchTrace with headings E0, E1, E2, E3, E4, E5, E6, E7.

P2 asks whether this source supports the exact chain:
Bind(phi) -> Form(phi)=u -> Bridge R(x,u) <-> phi(x) -> Reenter x:=u -> normalize phi(u) to a same-query feedback H(q), with a source-grounded polarity or guard.
Every claimed field must cite a line from the frozen card. A recursive program, a stage increment, or a Dec branch is not by itself Bind, Bridge, Reenter, or feedback. Compare at least one nearby alternative reading. E5 must show the shortest source rule chain or explicitly state which field is absent. E6 must name one changed source fact that changes the verdict. E7 must choose exactly one bounded status from P2_MATCHED_WITH_SCOPE, P2_NOT_APPLICABLE, P2_GUARD_BLOCKED, INSUFFICIENT_ALIGNMENT.

BEGIN FROZEN SOURCE CARD
File identity: QuestioningDelay.agda, SHA-256 c7b5ddf389bb1501a6f420651c229f4dee84c78f6901ab4080c2faea242f69db.

94 -- A judge answers, at every stage k, whether C is settled at h-level k+1.
96 Judge : Type ell -> Type ell
97 Judge C = (k : Nat) -> Dec (isOfHLevel (suc k) C)
99 module Questioning (C : Type ell) (judge : Judge C) where
101 mutual
102   askFrom : Nat -> Delay Nat
103   askFrom k .force = answer k (judge k)
105   answer : (k : Nat) -> Dec (isOfHLevel (suc k) C) -> Delay' Nat
106   answer k (yes _) = now k
107   answer k (no _) = later (askFrom (suc k))
109 Q : Delay Nat
110 Q = askFrom 1

115 runYes ... -> evalFor n (answer k (yes h)) = just k
118 runNoZero ... -> evalFor zero (answer k (no nh)) = nothing
121 runNoSuc ... -> evalFor (suc n) (answer k (no nh)) = runFor n (askFrom (suc k))

163 -- halting is exactly settled at some finite h-level
165 Halts : Type
166 Halts = Sigma n:Nat. Sigma j:Nat. runFor n Q = just j
168 HasLevel : Type ell
169 HasLevel = Sigma m:Nat. isOfHLevel m C
183 haltsToLevel : Halts -> HasLevel
186 levelToHalts : HasLevel -> Halts
END FROZEN SOURCE CARD
```

