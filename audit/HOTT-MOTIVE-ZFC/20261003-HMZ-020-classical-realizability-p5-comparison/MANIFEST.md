# HMZ-020：classical realizability 与 user-P P5 的冻结比较

> **身份：** `SUCCESSOR_SOURCE_RUN / FROZEN_DENOMINATOR / DENOMINATOR_COMPLETE_WITH_SCOPE / CLASSICAL_ZF_PROGRAM_SEMANTIC_CONTROL / P_REQUALIFICATION_REQUIRED / NO_ZFC_Q_OR_MATH_CLAIM`。

## 研究问题

Palmgren 的 constructive delivery contract 与 Krivine 的 classical realizability/ZF program correspondence 是否已经给出 user-P P5 的全部内容？如果它们只是在不同逻辑与模型语义下明确支付程序/控制/realizer条件，那么还需要什么来源才能支持“同一 ZFC consumer 预支使用未支付对象”的 P5？

## 冻结分母

| ID | 类 | 来源 | 角色 |
|---|---|---|---|
| `HMZ-S-032` | C/D/E | Krivine 2013 classical realizability / `ZFε`. | ZF-related program correspondence under explicit realizability-model semantics. |
| `HMZ-S-031` | E/B/D | Palmgren 2004 constructive logic/type theory. | Constructive proof/program/termination/correctness contract. |
| `HMZ-S-011` | C/D | Paulson 2021 Isabelle/ZF. | Ordinary ZF proof-formalization interface, without a claimed universal delivery contract. |
| `HMZ-S-018` | B/D | HoTT Library 2017. | Type-theoretic axiom/computation countercontrol. |
| `HMZ-S-029` | C/D/E | Koepke–Koerwien 2006. | Explicit program/limit/reflection model control. |

## Result summary

```text
constructive proof/program delivery: SOURCE-SUPPORTED
classical ZF-related proof/program realizability: SOURCE-SUPPORTED
both contracts have explicit logical/model/operational payment: SOURCE-SUPPORTED
ordinary bare-ZFC consumer promises same delivery: NOT FOUND
NeedBuild → OperatorUse → BuildDone same-card transition: NOT FOUND
P5 preemptive-use surplus: NOT FOUND
P-qualified ZFC Q: NO
```

The source result is stronger than a simple “ZFC has no programs” claim: specialized classical realizability can attach program semantics to ZF. The required conclusion remains narrow: this does not identify a bare-ZFC consumer that preemptively uses an unpaid construction.
