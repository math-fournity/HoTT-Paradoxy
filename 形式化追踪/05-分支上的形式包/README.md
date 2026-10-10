# 分支上的形式包

> GPT 各线在各自分支上写成的形式包，以及它们的去向。权威记录是 `HoTT/CLAIM_NAMESPACE_LEDGER.md` §3；分支命题用前缀 D01、D02、D09 区分。

**2026-10-09 更新**：凡是能用本机 Lean core 重新执行的分支 Lean 源，现在都在 `dev` 上有一份可重放收据
（`HoTT/formal/branch-formalization-coverage/`，CG001-C-123 至 C-126；判据运行是
`20261009-CG001-BRANCH-FORMALIZATION-COVERAGE-06` 与 `-NEG-02`，`-01..-05` 与 `-NEG-01` 是驱动修正期的失败尝试）。
唯一原本被排除在外的 `GeometricCompletion.lean`（dev-03/dev-04）也已在本机 Mathlib 上重放（CG001-C-127）。
八个 worktree 方向的逐条覆盖判定见该包 `CLAIM.md` §1。

**2026-10-10 更新**：最后一条缺口（dev-09 的 `external-foundation-incompleteness`，D09-C-369）已在本机
Foundation `1fb01b72` 构建树上重放（CG001-C-387，运行 `20261010-CG001-FFL-INCOMPLETENESS-R3-REPLAY-01`
与 `-NEG-01`）；八个 worktree 方向的覆盖至此闭合。

| 分支（提交） | 包 | 编号 | 去向 | 说明 |
|---|---|---|---|---|
| dev-01（`f10899cb`） | `zfc-dense-quantized-motion`、`zfc-dense-quantized-contract`、`zfc-meta-subtheory-adequacy` | D01-C-369–C-371 | 已并入 `dev`（`4a3535d9`，逐字节相同），13 个 Lean 运行本机重放 | 稠密性与运动的机器控制。归入无哥德尔路线的组件，见第 02 章 |
| dev-09（`ac6391b6`） | `cubical-godel-fragment` | D09-C-370–C-386 | 已并入 `dev`（`4a3535d9`），8 个 Agda 运行重放 | Cubical Agda 中的哥德尔编码片段，只到语法形状，没有对象层的可表示性定理 |
| dev-09 | `external-foundation-incompleteness` | D09-C-369 | 留在分支；**已在本机重放**（2026-10-10） | 原件两个文件逐字节复制到 `HoTT/formal/claude-cg001/external-foundation-incompleteness/GodelQ/`，在本机 Foundation `1fb01b72` 构建树上过核；运行 `20261010-CG001-FFL-INCOMPLETENESS-R3-REPLAY-01` 与 `-NEG-01`。注意 Foundations pin 差异（`f3972f42` → `1fb01b72`），见包 `CLAIM.md` §4 |
| dev-02（`4005fa80`） | `zfc-actual-q-policy`（分支版）5 个 Lean 源 | D02-C-359–C-365 | 留在分支（与 `dev` 同路径不同内容）；**已有 `dev` 收据** | `ActualQPolicy`、`ZFCObservationLanguage`、`ZFCCompletionPolicyUniformity`、`ZFCUnpaidCompletionPromotion`、`ZFCMembershipLanguageBoundary`；见 `branch-formalization-coverage/` |
| dev-03（`854a6aba`） | `zfc-observation-boundary` 7 个 Lean 源 | 无 C 编号（`MP-ZFC-ACTUAL-POLICY-WITNESS-001` 等） | 留在分支；**已有 `dev` 收据** | `ObservationBoundary`、`MetaObservationConsistency`、`ActualPolicyWitness`、`ActualPolicyEvidenceFrontier`、`SepCompletionPromotion`、`SequentialCompletionContracts`、`UouCompletionPromotion` |
| dev-04（`f97bbcb4`） | `zfc-observation-boundary` 5 个正源 + 2 个负控制 | 无 C 编号（`MP-ZFC-COMPLETION-PROMOTION-TENSION-001` 等） | 留在分支；**已有 `dev` 收据** | `CompletionPromotionTension`、`MetaSubtheoryAudit`、`CompletionSubstitutionProfile`、`CommunityObservationPolicy`；负控制在 `-NEG-01` 运行中被内核拒绝 |
| dev-06、dev-07 | 无新的形式包 | — | 留在分支 | Pattern-First 的方案、卡片与审计；H0 过程锚七字段已由 CG-005 吸收 |
| dev-03、dev-04 | `GeometricCompletion.lean`（两版逐字节相同） | CG001-C-127 | ✅ **已有 `dev` 收据** | `claude-cg001/godel-q-geometric-completion/`；17 s、exit 0、8 条公理报告全为三条标准公理。上一轮记为“缺 Mathlib 构建树”的理由不成立：本机有完整 Mathlib `5ed29652`，缺的只是 pin 未列本体根（新工具 `make_mathlib_pins.py` 补上） |

### 缺口清单（诚实登记）

| 缺口 | 现在状态 | 为什么 |
|---|---|---|
| （空） | — | 2026-10-10 前唯一剩下的 dev-09 `external-foundation-incompleteness`（D09-C-369）已在本机 Foundation `1fb01b72` 构建树上重放（CG001-C-387），见上一表与 `HoTT/formal/claude-cg001/external-foundation-incompleteness/`。此前的判词 `SOURCE_REPORTED_NOT_REPLAYED` 随之撤销，但**不**改读成原 `/tmp` 检出的逐字节重执行：pin 由 `f3972f42` 变为 `1fb01b72`（仅新增一个模块），是源码层等价的重放 |

## 取用

- 用 `git show <分支>@<提交>:<路径>` 读，不要切换检出。
- 要本机重放，直接看 `HoTT/formal/branch-formalization-coverage/` 的对应文件与运行收据；那份收据的 `source-manifest.json` 记着每个文件与分支原件的 SHA-256 相同。
- 并入前先看映射表 §3 的理由，并按 `HoTT/CLAIM_NAMESPACE_LEDGER.md` 的规则编号：`dev` 的下一个共享编号是 C-387。

## 下一步

- 没有进行中的工作。`external-foundation-incompleteness`（D09-C-369）已于 2026-10-10 在本机 Foundation 构建树上重放（`20261010-CG001-FFL-INCOMPLETENESS-R3-REPLAY-01`，正运行 `--rerun` `PASS_WITH_SCOPE`；负控制在 soundness 前提缺失处被拒）；原件仍留在 dev-09 分支不并入，重放包在 `HoTT/formal/claude-cg001/external-foundation-incompleteness/`。
- 上一轮认定为缺 Mathlib 的那一条已在本轮补齐（CG001-C-127）。
