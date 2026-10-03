# P-DAG-ZFC-SOURCE-073：finite powerset construction-bridge source-match payload

```text
You are a P-VALIDATION source mapper. Use only the frozen primary-source card below. Do not use tools, files, web, project history, prior results, or delegation. Do not provide hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace of at most 900 words.

BEGIN FROZEN SOURCE CARD
Source A: Isabelle's Logics: FOL and ZF, official PDF, SHA-256 4ce0ae256cb7506832fdc5d3605ff752c932c3c5721e3140c4658d84e56b0fcb. It states Pow membership as A in Pow(B) iff A is a subset of B.

Source B: mathlib4 Mathlib/Data/Finset/Powerset.lean at commit 300d0e535721bc098547106fc297d8ba2a63f6bb, SHA-256 cff2d246934cd2c1eb4d264985c863d6d5f1e364a65b62eceb695dadd0098be3.
It defines powerset (s : Finset alpha) : Finset (Finset alpha) and documents it as the finset of all subsets of s seen as finsets. It proves t in powerset s iff t subseteq s, powerset_empty, powerset_insert, and card(powerset s) = 2 ^ card s.

This card concerns only an explicit finite input s : Finset alpha. It supplies no identification of arbitrary ZF set A with a Finset, no infinite input, no execution trace, no wall-clock result, and no real-world task.
END FROZEN SOURCE CARD

## Frozen parent TaskCard — echo these exact fields in E3

T = ZF Pow membership plus Mathlib finite-powerset implementation control
u = subset collection of explicitly finite input s
F = Pow(B) / Finset.powerset(s)
C = Finset powerset output/membership/cardinality interface
I = s : Finset alpha, and candidate t : Finset alpha
O = t in s.powerset iff t subseteq s; card(s.powerset)=2^card(s)
Done = finite output value satisfies membership/cardinality contract; no wall-clock or arbitrary-ZF completion asserted
Q? = whether this finite control supplies a valid same-task construction bridge for arbitrary ZF Pow, or only proves finite completion scope

## Required analysis

E0 scope; E1 source identity; E2 source facts; E3 exact parent TaskCard; E4 direct correspondence; E5 P1/P2/P3 finite-control ledger; E6 PowerSetDefenseLedger; E7 bounded verdict and altered fact.

At E5, state whether the finite representation/output contract supplies a P3 lifecycle or only a finite completion control; do not invent runtime transitions. At E6 use exact semantic fields:

| field | question |
| PS0 source/variant | Which ZF Pow and Finset powerset variants/layers are examined? |
| PS1 defended Russell feature | What finite/bounded feature is present and what is not established? |
| PS2 actual guard | Which finite input/type/output facts restrict the control? |
| PS3 guard scope | What exact task/framework scope is covered? |
| PS4 candidate surplus | With guard retained, what arbitrary-ZF same-task Q/reentry/lifecycle remains source-supported? |
| PS5 same-task control | Does changing finite input to arbitrary/infinite ZF set preserve the task? |
| PS6 verdict | Give a bounded verdict from DEFENSE_IDENTIFIED, CANDIDATE_GUARD_BLOCKED, BEYOND_DEFENSE_CANDIDATE, SOURCE_GUARD_SCOPE_UNSET or NOT_ENOUGH_EVIDENCE. |

Do not assert an equivalence of ZF and Lean, a ZFC construction process, a runtime result, UR, or a theory defect.
```
