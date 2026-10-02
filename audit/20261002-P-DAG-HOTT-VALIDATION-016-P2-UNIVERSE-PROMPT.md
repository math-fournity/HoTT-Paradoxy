# P-DAG-HOTT-VALIDATION-016：具体宇宙卡的 P2 冻结 source-match prompt

```text
You are a P-VALIDATION source mapper. Use only the frozen source card and P2 method.
Do not use tools, files, web, project history, prior results, or delegation. Do not
provide hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace.

P2 needs a source-grounded chain Bind(phi) -> Form(phi)=u -> Bridge R(x,u) <-> phi(x)
-> Reenter x:=u -> normalize phi(u) to same-query feedback H(q), with polarity/guard.
An iterated stage search, a local Dec branch, or a theorem Q=never is not itself
formula binding, a bridge, substitution, or same-query feedback. Compare a nearby
reading, state the shortest actual chain or missing field, give a verdict-changing
counterfactual, and choose exactly one of P2_MATCHED_WITH_SCOPE, P2_NOT_APPLICABLE,
P2_GUARD_BLOCKED, INSUFFICIENT_ALIGNMENT in E7.

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
165 Halts : Type
166 Halts = Sigma n:Nat. Sigma j:Nat. runFor n Q = just j
168 HasLevel : Type ell
169 HasLevel = Sigma m:Nat. isOfHLevel m C
183 haltsToLevel : Halts -> HasLevel
186 levelToHalts : HasLevel -> Halts
275 judgeU : Judge (Type l-zero)
276 judgeU k = no (universeHasNoLevel (suc k))
284 universeQuestioningIsNever : (judge : Judge (Type l-zero)) -> question (Type l-zero) judge = never
287 universeQuestioningRunsNothing : (judge : Judge (Type l-zero)) (n : Nat) -> runFor n (question (Type l-zero) judge) = nothing
292 universeQuestioningNeverAnswers : (judge : Judge (Type l-zero)) -> not Questioning.Halts (Type l-zero) judge
END FROZEN SOURCE CARD
```

