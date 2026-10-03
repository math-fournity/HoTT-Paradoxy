# P-DAG-SOURCE-072：HF diagonal / Pf source-match payload

```text
You are a P-VALIDATION source mapper. Use only the frozen primary-source card below. Do not use tools, files, web, project history, prior results, or delegation. Do not provide hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace of at most 900 words.

BEGIN FROZEN SOURCE CARD
Source: Lawrence C. Paulson, “A Mechanised Proof of Gödel's Incompleteness Theorems using Nominal Isabelle,” arXiv:2104.13792, PDF SHA-256 4475747a8b3434372e90e2cf3b5164c6cefbec35c0dede4d867b52068b16379c.

Frozen source facts:
1. The paper describes mechanised proofs of incompleteness theorems in Isabelle/HOL, including a formal proof of the second theorem, for a hereditarily finite set (HF) calculus.
2. It distinguishes the proof calculus, coding the calculus within itself, and later work on quotations/pseudo-coding and the second theorem.
3. The paper refers to the proof predicate Pf and to syntactic coding/substitution/quotation machinery formalised in the HF calculus.
4. The final steps of the second theorem use a diagonal formula delta obtained via the first incompleteness theorem.
5. The source describes a formalisation/proof development; it gives no runtime lifecycle or real-world task.
END FROZEN SOURCE CARD

## Frozen parent TaskCard — echo these exact fields in E3

T = HF formal calculus as represented in an Isabelle/HOL formalisation
u = source diagonal formula delta
F = coding of syntax, quotation/pseudo-coding and Pf proof predicate
C = HF calculus proof predicate / external Isabelle/HOL proof development
I = coded formulas, quotes, substitutions and proof-calculus derivations
O = source-reported diagonal/second-incompleteness proof relations
Done = theorem/proof-development result at the stated layer only
Q? = whether source supports a same-object proof/certification reentry that is an active unpaid task at this layer, rather than a known metatheorem or external proof result

## Required analysis

E0 scope; E1 source identity; E2 source-bearing facts; E3 exact parent TaskCard; E4 direct correspondence; E5 P1/P2/P3 layer and bridge ledger; E6 nearest control/guard and verdict; E7 what changed fact would alter the result.

At E5 state separately:
1. P1: whether the formal source actually presents Q? as a current active task or only proves/describes a theorem;
2. P2: which parts of Bind/Form/Bridge/Reenter are source-supported for delta/Pf and which are not; distinguish syntactic self-reference from same-object logical feedback;
3. P3: whether Draft/NeedBuild/NeedEval/Admitted/OperatorUse/BuildDone transitions are source-provided.

At E6 identify any layer/quotation/derivability guard and whether it supplies a control. Do not assert a ZFC result, an internal inconsistency, a general incompleteness theorem, a runtime process, a real task, or a new knife.
```
