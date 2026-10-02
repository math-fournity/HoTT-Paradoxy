# P-DAG-HOTT-VALIDATION-012：P3 的冻结 source-match prompt

```text
You are a P-VALIDATION source mapper. You receive only the frozen source card below and the P3 method. Do not use tools, files, web, commands, Git, delegation, prior project results, or knowledge of any earlier experiment. Do not provide hidden chain-of-thought. Produce a concise public MatchTrace with headings E0, E1, E2, E3, E4, E5, E6, E7.

P3 asks a narrower question than “does the program have delay?” It requires source-backed states or transitions for the same object u: Draft(u), NeedBuild(u), NeedEval(R(u,u)), Admitted(u), OperatorUse(R,u), BuildDone(u), and a rule-backed dependency in which admission/use/formation creates a cycle or an unpaid ordering obligation. Do not invent a scheduler or treat `later` alone as admission. A normal completion process is a valid negative control. Every claimed state or edge must cite a line from the frozen card. Compare at least one nearby static or completion-only reading. E5 must give the smallest transition chain or name the missing edge. E6 must name one changed source fact that would change the verdict. E7 must choose exactly one bounded status from P3_ADMISSION_CYCLE_WITH_SCOPE, COMPLETION_PROCESS_NOT_ADMISSION_CYCLE, CONSTRUCTION_SEMANTICS_NOT_SUPPLIED, INSUFFICIENT_ALIGNMENT.

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
127 settledAt ... -> runFor n (askFrom k) = just k
134 notSettledAtZero ... -> runFor zero (askFrom k) = nothing
141 notSettledAt ... -> runFor (suc n) (askFrom k) = runFor n (askFrom (suc k))

163 -- halting is exactly settled at some finite h-level
165 Halts : Type
166 Halts = Sigma n:Nat. Sigma j:Nat. runFor n Q = just j
168 HasLevel : Type ell
169 HasLevel = Sigma m:Nat. isOfHLevel m C
183 haltsToLevel : Halts -> HasLevel
186 levelToHalts : HasLevel -> Halts
190 module NoLevel (noLevel : (m : Nat) -> not isOfHLevel m C) where
193 askFromIsNever : (k : Nat) -> askFrom k = never
196 answerIsNever : ... -> answer k d = later never
200 QIsNever : Q = never
203 QRunsNothing : (n : Nat) -> runFor n Q = nothing
END FROZEN SOURCE CARD
```

