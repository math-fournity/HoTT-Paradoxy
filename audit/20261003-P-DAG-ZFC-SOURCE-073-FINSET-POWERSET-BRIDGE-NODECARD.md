# P-DAG-ZFC-SOURCE-073：有限 powerset 的 P3 ConstructionBridge control NodeCard

> **身份：** `PRELAUNCH_NODECARD / CROSS_FRAMEWORK_FINITE_CONTROL / P3_B_COMPLETION_CONTROL / NOT_A_ZFC_P3_OR_THEORY_RESULT`。

```text
node_id: P-DAG-ZFC-SOURCE-073-FINSET-POWERSET-BRIDGE
parent: H069 source formation guard; H069–H072 P3 construction-interpretation gap
purpose: establish a controlled construction bridge only where the input is
         explicitly finite. Compare Isabelle/ZF Pow membership with Mathlib
         Finset.powerset's finite output contract. Determine whether this is a
         same-task finite completion control or an impermissible bridge to
         arbitrary/infinite ZF Power Set.
actor: gpt-5.6-terra / max; fallback=false
runner: scripts/pattern_p_appserver_blind_discovery.py @ d1b73ff4
private root: /Users/aurolafly/.codex-experiments/pattern-p-h073
access profile: PINNED_PRIMARY_SOURCE / source-match
permission/approval: governance-regression-fresh / never; no tools, files,
                     web, Git, or delegation
source A: Isabelle's Logics: FOL and ZF PDF, SHA-256
          4ce0ae256cb7506832fdc5d3605ff752c932c3c5721e3140c4658d84e56b0fcb
          (Pow membership as subset)
source B: mathlib4 Mathlib/Data/Finset/Powerset.lean
          @ 300d0e535721bc098547106fc297d8ba2a63f6bb
          SHA-256 cff2d246934cd2c1eb4d264985c863d6d5f1e364a65b62eceb695dadd0098be3
source scope: a cross-framework finite construction control, not an equivalence
              between arbitrary ZF sets and Finset values and not a runtime run.
frozen TaskCard:
  T      = ZF Pow membership plus Mathlib finite-powerset implementation control
  u      = subset collection of explicitly finite input s
  F      = Pow(B) / Finset.powerset(s)
  C      = Finset powerset output/membership/cardinality interface
  I      = s : Finset alpha, and candidate t : Finset alpha
  O      = t in s.powerset iff t subseteq s; card(s.powerset)=2^card(s)
  Done   = finite output value satisfies membership/cardinality contract; no
           wall-clock or arbitrary-ZF completion asserted
  Q?     = whether this finite control supplies a valid same-task construction
           bridge for arbitrary ZF Pow, or only proves finite completion scope
PowerSetDefenseLedger target:
  PS0 ZF Pow vs Finset powerset; PS1 finite all-subsets; PS2 finite type/input;
  PS3 cross-framework scope; PS4 retained arbitrary surplus; PS5 finite/infinite
  task switch; PS6 finite-control verdict.
nonnegotiable:
  - do not call Finset.powerset a construction of Pow(A) for arbitrary/infinite A;
  - no runtime timing/lifecycle from a source definition alone;
  - source must distinguish representation and mathematical set equality;
  - no ZFC Q/UR/construction tension conclusion.
success: preflight/prompt-input PASS; E0–E7, exact E3, P1/P2/P3 and PS0–PS6
         with explicit same-task verdict, zero tool/file/approval.
observation cadence: 60 seconds; automatic wall-clock interruption: absent
```
