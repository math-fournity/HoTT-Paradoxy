# 分支上的形式包

> GPT 各线在各自分支上写成的形式包，以及它们的去向。权威记录是 `HoTT/CLAIM_NAMESPACE_LEDGER.md` §3；分支命题用前缀 D01、D02、D09 区分。

**2026-10-09 更新**：凡是能用本机 Lean core 重新执行的分支 Lean 源，现在都在 `dev` 上有一份可重放收据
（`HoTT/formal/branch-formalization-coverage/`，CG001-C-123 至 C-126，运行
`20261009-CG001-BRANCH-FORMALIZATION-COVERAGE-05` 与 `-NEG-01`）。下表“去向”列随之更新。
八个 worktree 方向的逐条覆盖判定见该包 `CLAIM.md` §1。

| 分支（提交） | 包 | 编号 | 去向 | 说明 |
|---|---|---|---|---|
| dev-01（`f10899cb`） | `zfc-dense-quantized-motion`、`zfc-dense-quantized-contract`、`zfc-meta-subtheory-adequacy` | D01-C-369–C-371 | 已并入 `dev`（`4a3535d9`，逐字节相同），13 个 Lean 运行本机重放 | 稠密性与运动的机器控制。归入无哥德尔路线的组件，见第 02 章 |
| dev-09（`ac6391b6`） | `cubical-godel-fragment` | D09-C-370–C-386 | 已并入 `dev`（`4a3535d9`），8 个 Agda 运行重放 | Cubical Agda 中的哥德尔编码片段，只到语法形状，没有对象层的可表示性定理 |
| dev-09 | `external-foundation-incompleteness` | D09-C-369 | 留在分支；**本机不可重放** | 运行依赖已不存在的 `/tmp` Foundation 检出。判词 `SOURCE_REPORTED_NOT_REPLAYED`；作用已由 CG001-C-102 与 C-95–C-101 取代 |
| dev-02（`4005fa80`） | `zfc-actual-q-policy`（分支版）5 个 Lean 源 | D02-C-359–C-365 | 留在分支（与 `dev` 同路径不同内容）；**已有 `dev` 收据** | `ActualQPolicy`、`ZFCObservationLanguage`、`ZFCCompletionPolicyUniformity`、`ZFCUnpaidCompletionPromotion`、`ZFCMembershipLanguageBoundary`；见 `branch-formalization-coverage/` |
| dev-03（`854a6aba`） | `zfc-observation-boundary` 7 个 Lean 源 | 无 C 编号（`MP-ZFC-ACTUAL-POLICY-WITNESS-001` 等） | 留在分支；**已有 `dev` 收据** | `ObservationBoundary`、`MetaObservationConsistency`、`ActualPolicyWitness`、`ActualPolicyEvidenceFrontier`、`SepCompletionPromotion`、`SequentialCompletionContracts`、`UouCompletionPromotion` |
| dev-04（`f97bbcb4`） | `zfc-observation-boundary` 5 个正源 + 2 个负控制 | 无 C 编号（`MP-ZFC-COMPLETION-PROMOTION-TENSION-001` 等） | 留在分支；**已有 `dev` 收据** | `CompletionPromotionTension`、`MetaSubtheoryAudit`、`CompletionSubstitutionProfile`、`CommunityObservationPolicy`；负控制在 `-NEG-01` 运行中被内核拒绝 |
| dev-06、dev-07 | 无新的形式包 | — | 留在分支 | Pattern-First 的方案、卡片与审计；H0 过程锚七字段已由 CG-005 吸收 |
| dev-03、dev-04 | `GeometricCompletion.lean`（两版） | `MP-ZFC-GEOMETRIC-COMPLETION-001` | 留在分支 | 依赖 Mathlib，本机 toolchain pin 未含 Mathlib 构建树，故不在 `branch-formalization-coverage/` 内；分支上的 `20261003-MP-ZFC-GEOMETRIC-COMPLETION-001-0{1..5}` 收据保持原样 |

## 取用

- 用 `git show <分支>@<提交>:<路径>` 读，不要切换检出。
- 要本机重放，直接看 `HoTT/formal/branch-formalization-coverage/` 的对应文件与运行收据；那份收据的 `source-manifest.json` 记着每个文件与分支原件的 SHA-256 相同。
- 并入前先看映射表 §3 的理由，并按 `HoTT/CLAIM_NAMESPACE_LEDGER.md` 的规则编号：`dev` 的下一个共享编号是 C-387。

## 下一步

- 没有进行中的工作。`external-foundation-incompleteness`（D09-C-369）需要一份本机可用的 Foundation 检出才能重执行；在拿到之前它保持 `SOURCE_REPORTED_NOT_REPLAYED`，不并入也不删除。
