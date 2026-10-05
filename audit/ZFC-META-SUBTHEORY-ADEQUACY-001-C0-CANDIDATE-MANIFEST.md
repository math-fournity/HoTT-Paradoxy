# ZFC-META-SUBTHEORY-ADEQUACY-001：C0 核心候选宇宙冻结

> **身份：** `CORE_ADEQUACY_CANDIDATE_MANIFEST / C0_STARTUP_OWNER / NOT_A_MATHEMATICAL_RESULT`。
>
> **parent SOP：** `ZFC-META-SUBTHEORY-ADEQUACY-SOP`。
>
> **当前状态：** `C0_UNIVERSE_FROZEN / NO_C1_C6_LEAF_STARTED / CORE_VERDICT_NOT_PROVED`。

## C0 的问题

冻结能够真正改变 core verdict 的候选宇宙，防止研究又把可重放的 proof checker、abstract fixture 或外部书籍当成 bare ZFC 对连续统子理论负责的 actual interface。

每一个 `LIVE` 候选最终必须支付：

```text
M / S / Q / FormalDone / OriginDone / P / Bridge / Adequacy
```

## 候选族与当前分母

| family | 初始候选／控制 | 当前身份 | 目前已知 | C0 后的最小判别动作 | 不能推出 |
|---|---|---|---|---|---|
| `F-A` 标准连续统 application | IEP + Norton 的 Zeno Standard Solution | `LIVE / C1A_PARTIAL_FOUNDATION_AND_THEOREM_IDENTITY_UNPAID` | IEP 固定 ZFC-with-Choice → standard real analysis → Standard Solution / finite-time arrival；Norton fixed task switch。没有版本固定 exact S theorem 被 IEP 的 P 消费。 | `C1A-2`：找 exact-ZFC／exact-S theorem identity 与 IEP P 的同链 payment；若没有，保留 F-A live 并转 F-B source candidate。 | bare ZFC 已有或没有 defect；任一极限 theorem 就是芝诺解答。 |
| `F-B` ZFC 内实分析 formalization | ZF/ZFC/Mizar/Isabelle/ZF 等可执行实数、序列、极限、连续性 formalization | `LIVE / MIZAR_FOTG_C1_WITNESS / SOURCE_DISCOVERY_CONTINUES` | frozen Mizar FOTG source + `NUMPOLY1:Th87` 形成 Mizar real-sequence limit witness；它是 ZFC 的非保守 extension，且没有 Q/P。IsarMathLib/Isabelle-ZF real construction 是下一入口。 | `C0B / C1A-2`：只收录同时能冻结 M→S、theorem identity，并能与 actual Q/P 对齐或明确排除的版本固定候选。 | “找到实数库”即 core contract，或 Mizar theorem 自动是 IEP Zeno theorem。 |
| `F-C` foundation adequacy 来源 | 说明集合论作为数学基础如何解释、保真或审查子理论结果的来源 | `LIVE / ADEQUACY_SOURCE_REQUIRED` | 既有 SEP 只支付语言／表示能力，不能支付 adequacy。 | `C0C`：寻找明确的 foundation-to-subtheory semantic/interpretation/adequacy statement，并记录其是否涉及 Q/P。 | M 必须为每个物理任务承担 bridge 的既定公理。 |
| `F-D` H0 comparison | main H0、KLV/CCHM/cubical models、H0→Z0 资产 | `LIVE_CONTROL / SAMEQ_H0_UNPAID` | H0 fixed、部分 trace和source boundary已有；SameQ 尚无。 | `C0D`：只寻找能逐字段支付 `SameQ_H0` 的 source/formalization；否则维持 control。 | H0 与芝诺自动同 Q。 |
| `F-E` defense / task-switch | 明确支付 bridge、明确拒绝 P 或明确声明换题的来源 | `LIVE_CONTROL` | Norton 是 explicit task-switch 的已知控制。 | `C0E`：每个 live candidate 必须配一个同层 defense/control。 | 任何 task switch 自动证明 ZFC failure。 |

## 明确排除为核心候选的控制

| item | 排除理由 | 仍可用作 |
|---|---|---|
| `set.mm` proof acceptance + C-369 Appendix-C vocabulary extension | 支付 proof/database Done，以及 actual `$v/$f` vocabulary 的 M-level infinite-variable-extension 子义务；仍未支付 S/Q/P 的连续统 completion、internal `mFS` witness或`Prv`。 | Code/Accept 与“有限词表不是唯一阻断”的反控制。 |
| Foundation generic Gödel | 支付一般技术机制，未实例化 actual M/S/Q/P。 | T-DIAG 条件核。 |
| ACL2 Iris/Zeno | 不是 ZFC；固定 Lisp theorem未给 physical bridge。 | 跨理论 source-payment 反控制。 |
| C-364/C-367/C-368 | abstract 或 source-bound fixture。 | formal proof skeleton 与反控制。 |
| C-365/C-366 | 集合论可表示过程。 | 排除“不能表示过程”的过强主张。 |

## 分母与完成纪律

```text
candidate_families_total = 5
families_live            = 5
families_exhausted       = 0
actual_core_contracts    = 0
core_kernel_verdicts     = 0
remainder                = 5
```

### C1A 叶的状态与 successor scan（2026-10-05）

- 已检查的 actual / version-fixed source candidates：`F-A=1`（IEP standard application）；`F-B=2`（Mizar FOTG/MML limit witness；IsarMathLib Isabelle/ZF real-construction ingress）。
- C1A 产物：[foundation–theorem identity card](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C1A-FOUNDATION-THEOREM-CARD.md) 与对应 source snapshots。
- leaf verdict：`C1A_PARTIAL_FOUNDATION_AND_THEOREM_WITNESSES / FOUNDATION_VARIANT_AND_THEOREM_IDENTITY_UNPAID / NOT_CORE_MACHINE_PROVED`。
- successor scan：`F-A` 仍缺 exact theorem identity + P consumption；`F-B` 仍缺 Q/P。下一项为 `C1A-2/C0B`，不得返回 proof checker、generic Gödel 或 C-369 control。

所以 C0／C1 仍未完成，任何 `CURRENT_*_CLOSED_WITH_SCOPE` 旧标签都不能结束本 SOP。每处理一个候选，必须更新上述计数、保留 source identity、写出 `successor_scan`，并从仍 live 的候选中选下一项。只有所有 family remainder 为零且 C6 总门满足，才有整体完成资格。
