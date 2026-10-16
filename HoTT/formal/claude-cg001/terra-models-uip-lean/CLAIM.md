# Terra 正控制模型在 UIP 内核中的消融（C-61）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325。
>
> **起因**：用户要求 Claude 理解 Terra 从 015 起的新尝试、判断其路子是否对，并问能否接手。Terra 在 017、018 用两组 Cubical Agda 正控制（C-351–C-356）关闭了 T1（审计回滚）与 T2（一次性授权码），理由是“HoTT 内存在完成同一任务的表示”。本包检验这些正控制究竟用到了 HoTT 的哪一部分。
>
> - proof id：`MP-CG001-TERRA-MODELS-UIP-LEAN-001`（主包）；负控制 `MP-CG001-TERRA-MODELS-UIP-LEAN-NEG-001`。
> - claim：`CG001-C-61`。
> - 工具链：Lean 4.34.0 核心，不用 Mathlib（`../pedometer-ablation-lean/LEAN_TOOLCHAIN.json`）；捕获 `.claude/goals/CG-001-targeted-overview/tools/capture_lean_proof_run.py`，驱动 `tools/lean_check.py`，主包另以 `leanchecker --fresh` 重放。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §15（GOAL_LOCAL_INDEX_ONLY）。

## 被转写的来源（只读，未改动）

| 文件 | Terra 命题 | SHA-256 | 字节 |
|---|---|---|---|
| `HoTT/formal/terra-t2-one-shot/OneShotCapability.agda` | C-354–C-356 | `8d23db569bd847ac3a88841f21784afb4a7a08a7c62b2d8fb94ef79a1a9ec189` | 3,561 |
| `HoTT/formal/terra-t1-h0-generic/H0AuditGeneric.agda` | C-351–C-353 | `18844a3dd21f09be06fe46e915daf2aea3b699164988f4b7b6eae7da459e505c` | 3,504 |

逐构造子转写：同名归纳类型、同样的模式匹配分支、同样的命题。唯一的形式差别是 Terra 的参数化模块在这里写成显式参数，`undo-law` 写成 `undo_law`。

## 命题全文（`TerraModelsUIP.lean`，命名空间 `CG001.TerraModelsUIP`）

- **(a) 本内核满足 UIP**：`uip : ∀ (p q : a = b), p = q`，由 `rfl` 成立（Lean 的 `Prop` 证明无关）。
- **(b) T2 模型**：`duplicateIsTwoCopies`、`pureCopiesBothGrant`、`firstCopyGrants`、`secondCopyIsDenied`、`serverHasConsumedCode`、`bothAttemptsRecorded`，与 Terra C-354–C-356 逐条同陈述，均由 `rfl` 成立。
- **(c) T1（H₀ 泛型）模型**：`contentUndo`（C-351）、`auditAppend`（C-352，另证 `appendAssoc`）、`fullStateNotReturn`（C-353）。
- 11 条定理的 `#print axioms` 全部为“不依赖任何公理”。

**结论（有范围的机器证明）**：Terra 用来关闭 T1、T2 的正控制，原样成立于一个满足 UIP 的内核之中。

## 这件事说明什么（解释，非机器证明）

- 【来源】UIP 与单价性不相容：若宇宙含 Bool，单价性给出 Bool 与自身的两种不同认同（HoTT Book 例 3.1.9）；Cubical 一侧的机器证明见 C-63 (a)。
- 【解释】所以这些正控制的成功不依赖 HoTT 特有的任何原则：不依赖把转移写成路径、单价性、高阶归纳类型或运输。它们展示的是任何依赖类型论都有的普通数据与状态传递的能力。
- 【解释】对 T1、T2 的结案因此是中性的：它们推翻了“HoTT 做不了审计／一次性兑换”这类强句，却没有检验 HoTT 自己的抽象（相同即结构）。完成任务的那一半，恰好是 HoTT 与反单价的理论共有的那一半。

## 禁止外推

- 不说明 Terra 的 Cubical 证明有错：它们在 Cubical Agda 中精确重放通过（本会话在临时副本中独立重放四个运行，stdout/stderr 按路径归一后逐字节一致）。
- 不说明 HoTT 做不了 T1、T2 的任务，也不说明 T1、T2 是现实相对悖论。
- 不陈述任何关于 HoTT 路径的事：Lean 的相等满足 UIP，本包只关于这两个集合层模型。
- 不把“HoTT 与 UIP 理论共有的部分完成了任务”推广为“HoTT 特有的部分必然造成失败”；后者需要另外的论证。

## 负控制

`WrongSecondGrant.lean`：断言同一授权码的第二次兑换也被批准（`secondAttempt.1 = granted accessToken`，`rfl`）。预期被拒：内核算出 `denied`。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-TERRA-MODELS-UIP-LEAN-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-TERRA-MODELS-UIP-LEAN-NEG-01`。
- 重放：`python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir <运行目录> --rerun`（负控制加 `--expect-rejected`）。
