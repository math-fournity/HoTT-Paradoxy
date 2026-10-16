# P-DAG-HOTT-VALIDATION-017：具体宇宙卡的 P3 冻结 source-match prompt

```text
You are a P-VALIDATION source mapper. Use only the frozen source card and P3 method.
Do not use tools, files, web, project history, prior results, or delegation. Do not
provide hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace.

P3 asks whether the same source-backed object u has a construction/admission order:
Draft(u), NeedBuild(u), NeedEval(R(u,u)), Admitted(u), OperatorUse(R,u), BuildDone(u),
with a rule-supported dependency cycle or unpaid ordering obligation. Do not invent a
scheduler. A completed/never delayed process is not automatically an admission cycle.
Every state/edge must cite the card. Compare a nearby completion-only reading. State
the shortest actual transition chain or missing edge. Give a verdict-changing
counterfactual. Choose exactly one of P3_ADMISSION_CYCLE_WITH_SCOPE,
COMPLETION_PROCESS_NOT_ADMISSION_CYCLE, CONSTRUCTION_SEMANTICS_NOT_SUPPLIED,
INSUFFICIENT_ALIGNMENT in E7.

BEGIN FROZEN SOURCE CARD
File identity: QuestioningDelay.agda, SHA-256 c7b5ddf389bb1501a6f420651c229f4dee84c78f6901ab4080c2faea242f69db.
96 Judge : Type ell -> Type ell
97 Judge C = (k : Nat) -> Dec (isOfHLevel (suc k) C)
99 module Questioning (C : Type ell) (judge : Judge C) where
102 askFrom : Nat -> Delay Nat
103 askFrom k .force = answer k (judge k)
105 answer : (k : Nat) -> Dec (isOfHLevel (suc k) C) -> Delay' Nat
106 answer k (yes _) = now k
107 answer k (no _) = later (askFrom (suc k))
109 Q : Delay Nat
110 Q = askFrom 1
115 runYes ... -> evalFor n (answer k (yes h)) = just k
121 runNoSuc ... -> evalFor (suc n) (answer k (no nh)) = runFor n (askFrom (suc k))
127 settledAt ... -> runFor n (askFrom k) = just k
141 notSettledAt ... -> runFor (suc n) (askFrom k) = runFor n (askFrom (suc k))
165 Halts : Type
166 Halts = Sigma n:Nat. Sigma j:Nat. runFor n Q = just j
190 module NoLevel (...) where
193 askFromIsNever : (k : Nat) -> askFrom k = never
196 answerIsNever : ... -> answer k d = later never
200 QIsNever : Q = never
203 QRunsNothing : (n : Nat) -> runFor n Q = nothing
275 judgeU : Judge (Type l-zero)
276 judgeU k = no (universeHasNoLevel (suc k))
284 universeQuestioningIsNever : (judge : Judge (Type l-zero)) -> question (Type l-zero) judge = never
292 universeQuestioningNeverAnswers : (judge : Judge (Type l-zero)) -> not Questioning.Halts (Type l-zero) judge
END FROZEN SOURCE CARD
```

