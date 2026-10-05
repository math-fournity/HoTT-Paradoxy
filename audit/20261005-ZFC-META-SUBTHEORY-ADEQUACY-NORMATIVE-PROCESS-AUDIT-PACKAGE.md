# `ZFC+Q_norm` 过程完成审计：专用 Lean package 的来源、规格与运行审计

> **身份：** `NORMATIVE_EXTENSION_MACHINE_PROOF_AUDIT / NOT_A_CORE_C6_VERDICT`。
>
> **Package：** `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001`，claims `C-370`–`C-374`。
>
> **primary run：** [`20261005-MP-ZFC-NORMATIVE-PROCESS-AUDIT-001-03`](../HoTT/verification/runs/20261005-MP-ZFC-NORMATIVE-PROCESS-AUDIT-001-03/RUN.json)。

## 1. 这个 package 回答的精确问题

研究发起人提出的 `Q_norm` 不是“ZFC 已经有的一个公理”，而是给基础性元理论的规范责任：当它支持的子理论以某种 `FormalDone` 宣布原过程任务已经完成时，必须检查 `FormalDone → OriginDone` 是否获得支付；若任务已被明示改写，则结论只能是修订任务完成。

本 package 因此只形式化以下三分审计接口：

```text
paid certificate FormalDone → OriginDone  => originalResolved
explicit task switch                       => revisedResolved
missing bridge                             => bridgeRequired
```

这将“需要有过程完成观察力”的用户规范变成可复用的逻辑 contract；它不把规范倒写为 bare ZFC 的既有职责。

## 2. source-to-spec 对照

| 规范／来源层输入 | 形式字段 | 资格边界 |
|---|---|---|
| 用户的 MetaTheory→SubTheory bridge 审查要求 | `CompletionContract`、`BridgeStatus`、`audit` | 用户的规范性 premise，不是 ZFC object-language 事实。 |
| C5E 的 foundation/application responsibility split | `paid`、`explicitTaskSwitch`、`missing` 三种来源状态 | 把来源卡已区分的责任形状写成审计分类；不让 Lean 替代来源解释。 |
| C5C/Norton 的 strict/revised completion card | `nortonContract` | frozen source-bound control：revised formal completion、strict original completion、explicit switch。 |
| C5F hybrid-Zeno 正控制 | `bridgeRequired` 是可被正式理论承担的合法判词 | 不把 hybrid execution 与连续 runner 或 HoTT Q 同一化。 |

## 3. kernel 实际检查的内容

源码 [`ProcessCompletionAudit.lean`](../HoTT/formal/zfc-normative-process-audit/ProcessCompletionAudit.lean) 在 Lean 4.34.1 core 中检查通过。保存的 primary run 固定：

- 精确 source、README、claim scope、toolchain、用户 primary source和 C5E/C5F/C0R3 source cards；
- `/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.1/bin/lean` 的 bytes 与 SHA-256；
- 12 个 selected theorem 的 `#print axioms` 输出，全部为“does not depend on any axioms”；
- `stderr` 为 0 bytes；
- 矩阵中 proof row + C-370–C-374 五条 claim row 的冻结行哈希；
- exact command replay，结果为 `EXACT_EXIT_STDOUT_STDERR_MATCH`。

由 kernel 接受的内容是：

1. `originalResolved` verdict 蕴含 `OriginDone`；
2. 显式改题只能得到 `revisedResolved`，且不等于 `originalResolved`；
3. bridge 缺失得到 `bridgeRequired`，且不等于 `originalResolved`；
4. paid bridge 的正控制可得到 original verdict 和 origin conclusion；
5. missing bridge 的负控制即使有 `FormalDone` 也不能得到 original verdict。

## 4. 这项证明不交付什么

```text
not: bare ZFC 已经具有或违反 Q_norm
not: 任何现有数学共同体实践已经采纳 Q_norm
not: IEP/Norton 的历史主张由 Lean 证明
not: 现实运动已经被充分形式化
not: Zeno 与 HoTT 构成 SameFullQ
not: ZFC 的对象语言不一致，或核心 C6 已完成
```

`C-359` 所需要的 actual `SameFullQ`、实际 P 适用和 HoTT B 的跨核映射仍未由来源支付；新 package 也没有触及这些前提。因此它强化的是研究发起人要求的**规范接口**，不是把 bare-ZFC core target 提前结案。

## 5. 捕获器缺口与修复

第一次 run `…-01` 已被 Lean core 接受，但 generic capture path 没有在 source manifest 中 pin Lean binary。proof-version verifier 因而报告 `LATER_LEAN_BINARY_NOT_PINNED`。该 run 被保留为历史 pipeline receipt，不能作为版本闭合的主证据。

`scripts/audit/capture_lean_proof_run.py` 随后修复：每次 generic Lean capture 都将 resolved Lean executable 以 `lean-core-binary` 写入 `external_dependencies`。`…-02` 由此通过 selected evidence closure；但本报告和 extension-admission 随后补入专用 package 链接，故 `…-02` 的 frozen source-manifest 按设计失效，而没有被修改。最终 `…-03` 在所有 source-to-spec 文档稳定后重新捕获、索引、冻结和重放，是 registry 的 primary run。修复提高的是证据环境和来源绑定的完整性，没有改变 theorem、toolchain版本或来源分类。

## 6. 对主线的后果

```text
Q_norm extension: machine proved with explicit scope
bare-ZFC C6:     still not released
next core action: C0-SUCCESSOR-RESELECTION-003
```

这正是两条线可以并存的正确关系：规范性 extension 让未来研究能明确地说“若采纳这项责任，应如何审计”；核心 evidence line 仍必须找到一个 actual `M/S/Q/P/Bridge/Adequacy` contract，才能评价 bare ZFC 的实际理论精度。
