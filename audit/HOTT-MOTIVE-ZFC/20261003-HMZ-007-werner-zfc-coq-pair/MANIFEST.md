# HMZ-007：WoLLIC 机器动机与 Werner ZFC-in-Coq 配对来源分母

> **身份：** `SUCCESSOR_SOURCE_RUN / FROZEN_DENOMINATOR / DENOMINATOR_COMPLETE_WITH_SCOPE / SOURCE_PAYMENT_AND_ANTI_ANALOGY_CONTROLS / NO_ZFC_Q_CLAIM`。

## 1. 研究问题

Voevodsky 2011 WoLLIC 的 `HMZ-R-014` 明说 ZFC-based proof-assistant formalization 曾产生“不自然构造”，但没有名字或任务。Werner 1997 的 CIC↔ZFC 互编码与可取得的 Coq/ZF 源码，是否提供一个可审的配对：在同一 formalization task 中，ZFC 的对象、formation、consumer 和 Done 是否有未支付的 P-shaped 张力？

**历史关联边界：** WoLLIC 没有点名 Werner；本 run 只把 Werner 作为与 R-014 同类的、可核查的 ZFC-in-CIC consumer，标为 `CANDIDATE_PAIRING_NOT_ATTRIBUTED`。它不是“Voevodsky 所指尝试已被证实”的历史结论。

## 2. 冻结来源分母

| ID | 类 | 来源 | 状态 | 本轮作用 |
|---|---|---|---|---|
| `HMZ-S-021` | A | Voevodsky 2011 WoLLIC 九页讲演。 | `READ_FROM_HMZ-006` | R-014：ZFC-based proof-assistant formalization 的作者级动机。 |
| `HMZ-S-022` | B, C, E | Benjamin Werner, *Sets in Types, Types in Sets*, TACS 1997；作者 PDF draft。 | `READ_RELEVANT_LOCATORS` | CIC/ZFC 双向编码、`Power`、Replacement／Choice 的来源论述。 |
| `HMZ-S-023` | C, D | `rocq-archive/zfc` 的 backward-compatible archive snapshot，commit `ede7126560844c381c2b021003a8dbcb0668ecad`。 | `SOURCE_INSPECTED_WITH_SCOPE` | `Ens`、`IN`、`EQ`、`Power`、Replacement／choice、Russell guard 的可见实现。 |
| `HMZ-S-011` | C, D, E | Paulson 2021 Isabelle/ZF（HMZ-001 冻结复用）。 | `REUSED_CONTROL` | 防止把任何 proof-assistant encoding 当作 bare ZFC 本身。 |
| `HMZ-S-016` | A, B, E | Grayson 2018（HMZ-003 冻结复用）。 | `REUSED_CONTROL` | 计算归约、axiom与有效交付的层级控制。 |

### 纳入与排除

- **纳入：** 以 `R-014` 到 `ZFC-in-CIC` 的明确 consumer 为范围；源码与论文相互校正。
- **不纳入：** “所有 ZFC-in-Coq 项目”、Werner 全部元理论、Coq 当前版本的可编译性、Voevodsky 与 Werner 的历史因果关系、Power Set 的全部 P-FORGE 站位。
- **停止条件：** 每个来源已有 R/Z/Q disposition、payment／guard、同一任务控制和 coverage remainder；不因源码中出现 `Russell` 或 `Power` 一词自动扩展成全理论审计。

## 3. 快速结果

```text
R-014 → Z pairing: SOURCE-SUPPORTED AS A CANDIDATE PAIR, NOT HISTORICAL ATTRIBUTION
exact Z-side: CIC model/encoding of ZFC, not bare ZFC itself
explicit payments: EM plus TTDA/TTCA non-computational choice principles for Replacement and set AC
Russell guard: only bounded comprehension from an existing Ens; “all Ens are members of U” is assumed and refuted
Power-set path: source-defined Power construction, but host CIC/impredicative Prop changes the target theory and no self-reentry is shown
P-qualified Q: NO
H0→Z0: ANTI_ANALOGY_CONTROL
```

详见 [SOURCE-CATALOG](SOURCE-CATALOG.md)、[R-CARDS](R-CARDS.md)、[Z-CARDS](Z-CARDS.md)、[Q-CARDS](Q-CARDS.md)、[CONSUMER-CONTROLS](CONSUMER-CONTROLS.md)、[COVERAGE](COVERAGE.md) 与 [FINDINGS](FINDINGS.md)。
