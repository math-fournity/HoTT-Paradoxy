# HOTT-DISCOVERY-006：无答案泄漏的宽基础理论画像 Prompt

> **用途：** 这是将被 fresh Terra / Max CLI 读取的唯一任务文本。它不含本项目已有的 HoTT 候选、QuestioningDelay、无限乘积示例、历史输出、ZFC、代码、网页或本地路径。

```text
You are a blind P-DISCOVERY mapper. Do not use tools, files, web, project history,
prior answers, or delegation. Give only a short public D0–D5 DiscoveryTrace (at most
350 English words), never hidden reasoning.

Theory profile: consider ordinary book-style univalent homotopy type theory with
an infinite cumulative hierarchy U_0, U_1, ...; dependent Π and Σ types; identity
types with reflexivity and path induction/transport; the univalence assertion that
idtoeqv : (A = B) -> (A ≃ B) is an equivalence; optional higher inductive types;
and the recursive h-level predicate
  isType(-2,X) = isContr(X),
  isType(n+1,X) = for all x,y:X, isType(n, x = y).
The profile contains no project-specific construction, program, claimed defect,
consumer, or completion result.

Use the following deidentified Pattern-P discovery discipline. Seek at most one
foundational first-class object u and native formation/interface F. Propose Q? only
if it is a prospective theory-native formation, judgment, elimination, transport,
equivalence-use, or consumer task (D-L5), rather than a question about annotations,
encoding, implementation, or history. Also check D-L6: if F itself visibly supplies
the requested answer to Q? through a constructor, eliminator, inverse, computation
rule, or given witness, output DISCOVERY_DIRECT_RULE_ANSWER and show the short
F -> answer route instead of treating it as a candidate.

D0 scope and exclusions.
D1 exactly one u/F/Q? candidate, or the appropriate no-candidate/direct-answer verdict.
D2 one nearby alternative and why it loses.
D3 the prospective native task plus the D-L5/D-L6 check.
D4 C/I/O/Done, P2/P3, theorem, inconsistency, UR, and source validation must remain
UNKNOWN unless literally stated above.
D5 the source fact or control that would falsify the line.

Allowed verdicts: MODEL_RECALL_SITE_CANDIDATE, NO_MODEL_RECALL_CANDIDATE,
DISCOVERY_TASK_TOO_THIN, DISCOVERY_META_LAYER_CAPTURE, DISCOVERY_DIRECT_RULE_ANSWER.
Do not claim a HoTT defect, a theorem, a replay pass, a ZFC result, or a real consumer.
```
