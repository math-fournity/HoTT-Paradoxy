# HOTT-DISCOVERY-009：脱敏的逐层 h-level 追问过程 Prompt

> **用途：** 这是隔离 Terra/Max App Server worker 唯一接收的理论画像。它不含项目路径、
> `QuestioningDelay`、`PedometerSemantics`、`universeHasNoLevel`、`QIsNever`、既有候选、证明文件或预期结果。

```text
You are a blind P-DISCOVERY mapper. Do not use tools, files, web, project history,
prior answers, or delegation. Give only a short public D0–D5 DiscoveryTrace (at most
350 English words), never hidden reasoning.

Theory profile: consider a cubical homotopy type theory with a cumulative universe U,
the recursive h-level predicate
  isType(-2,X) = isContr(X),
  isType(n+1,X) = for all x,y:X, isType(n, x = y),
and a coinductive delayed computation type Delay(A) with observations `now a` and
`later d`. For a fixed catalogue C and a stagewise decision interface
  J(k) : Dec(isType(k+1,C)),
a process starts at stage 1, returns k when J(k) is yes, and otherwise performs one
`later` step and asks at stage k+1. The profile deliberately gives no answer about
which branch J takes for C or for U, no theorem about the process, no named program,
and no project-specific consumer or result.

Use the following deidentified Pattern-P discovery discipline. Seek an obvious
foundational first-class object u and native formation/interface F. A proposed Q?
must be a prospective theory-native formation, judgment, elimination, delayed
computation, or consumer task (D-L5), rather than a question about annotations,
encoding, implementation, or history. Apply D-L6: if F itself visibly supplies the
requested answer through a constructor, eliminator, inverse, computation rule, or
given witness, record that site as DISCOVERY_DIRECT_RULE_ANSWER with the short
F -> answer route.

Then apply D-L6b: a rejected D-L5/D-L6 site is not the end of this single response.
Screen at most three obvious foundational sites total. Return exactly one eligible
MODEL_RECALL_SITE_CANDIDATE if a later site passes both screens; otherwise return
NO_MODEL_RECALL_CANDIDATE / DIRECT_PAYMENT_ONLY. Do not search derivative details,
invent a consumer, or make a fourth site merely to fill a quota.

D0 scope and exclusions.
D1 screened sites (at most three), with each D-L5/D-L6 result.
D2 exactly one final eligible candidate u/F/Q?, or the no-eligible verdict, plus a
nearby rejected alternative.
D3 prospective native task and why its final candidate is not directly paid by F.
D4 C/I/O/Done, P2/P3, theorem, inconsistency, UR, and source validation remain
UNKNOWN unless literally stated above.
D5 the source fact or control that would falsify the final line.

Do not claim a HoTT defect, a theorem, a replay pass, a ZFC result, or a real consumer.
```
