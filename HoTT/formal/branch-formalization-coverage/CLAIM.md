# CG001-C-123 至 C-126：八个 git worktree 的形式化资产在 `dev` 上全部有可重放收据

> **证明包**：`MP-CG001-BRANCH-FORMALIZATION-COVERAGE-001`；负控制 `MP-CG001-BRANCH-FORMALIZATION-COVERAGE-NEG-001`。
>
> **目标包**：CG-007（`.claude/goals/CG-007-formalization-completion/`），单元 W9；本机 Codex 会话，2026-10-09。授权原话（2026-10-08）：“按照你的想法进行优先级安排，完成后续所有‘形式化和机器证明’工作。”
>
> **理论变体**：Lean 4 core（v4.34.1，二进制与版本行在 `LEAN_TOOLCHAIN.json` 中按字节与 SHA-256 固定），无 Mathlib、无项目库；驱动在禁网沙盒内按绝对路径调用 pinned 二进制，不经过 elan 代理。
>
> **身份**：本机重放与来源固定（不是新数学）。研究发起人要求“必须 Cover 所有值得保留的 8 个当初的 git worktree 留下的工作方向”。本包把八条线留下的 Lean-core 形式源在 `dev` 上重新执行一遍，使每一条都能从 `dev` 指向一份 receipts、源哈希与二进制哈希都固定的运行证据。

## 0. 这个包做了什么、没做什么

**做了什么**：八条 GPT 线（`origin/dev-01` 至 `origin/dev-09`，无 dev-05）留下的形式化资产分三类——已经并入 `dev` 的、留在分支上的、以及没有形式包的。第二类此前只在各自分支上有收据，`dev` 上没有任何一份可指向它们收据的索引。本包把这一类中**能用本机 Lean core 直接执行**的全部源文件（16 个正源 + 2 个负控制）逐字节复制到 `HoTT/formal/branch-formalization-coverage/GodelQ/`，用 pinned Lean 4.34.1 在禁网沙盒里编译，并为它们生成 `dev` 上的正式收据。

**没做什么**：没有证明任何新命题。所有定理在各自分支上已经被证明；本包只重执行它们，并把源码、二进制、输出固定下来。因此本包的 claim 是“**这条线的形式资产在本机可重放、来源可逐字节核对**”，不是“这条线完成了什么数学”。

## 1. 八个方向的覆盖判定

下表按 `git-worktree对话录/README.md` 的八条线逐条给出：这条线留下了什么形式资产、它现在的证据状态、以及本包是否覆盖了它。“覆盖”只指**在 `dev` 上有可重放收据**这一件事。

| 线 | 留下的形式资产 | 并入 `dev` 前状态 | 本包覆盖 |
|---|---|---|---|
| dev-01 | `zfc-dense-quantized-motion`、`zfc-dense-quantized-contract`、`zfc-meta-subtheory-adequacy`（D01-C-369–C-371） | 已并入（`4a3535d9`），13 个 Lean 运行已本机重放 | 不需要：已有 `dev` 收据 |
| dev-02 | `zfc-actual-q-policy` 分支版 5 个 Lean 源（D02-C-359–C-365 中 `ActualQPolicy`、`ZFCObservationLanguage`、`ZFCCompletionPolicyUniformity`、`ZFCUnpaidCompletionPromotion`、`ZFCMembershipLanguageBoundary`） | 留在分支（与 `dev` 同路径不同内容） | ✅ 本包收据 |
| dev-03 | `zfc-observation-boundary` 6 个 Lean 源（`ObservationBoundary`、`MetaObservationConsistency`、`ActualPolicyWitness`、`ActualPolicyEvidenceFrontier`、`SepCompletionPromotion`、`SequentialCompletionContracts`、`UouCompletionPromotion`） | 留在分支 | ✅ 本包收据 |
| dev-04 | `zfc-observation-boundary` 5 个正源 + 2 个负控制（`CompletionPromotionTension`、`MetaSubtheoryAudit`、`CompletionSubstitutionProfile`、`CommunityObservationPolicy` 及两个 `Wrong*`） | 留在分支 | ✅ 本包收据（含负控制） |
| dev-06 | 无新形式包；`audit/20261004-H0-Z0-PATTERN-FIRST-PF-B2-过程锚点再审.md`（H0 过程锚七字段，方法资产） | 留在分支 | 不适用：无 Lean/Agda 源 |
| dev-07 | 无新形式包；Pattern-First 集成与受控卡 | 留在分支 | 不适用：无 Lean/Agda 源 |
| dev-08 | 无新形式包（GUI 标签，主检出 `dev`）；来源卡与 C0R9–C0R11 审计 | 已在 `dev` | 不适用：无形式包 |
| dev-09 | `cubical-godel-fragment`（D09-C-370–C-386）已并入（`4a3535d9`）；`external-foundation-incompleteness`（D09-C-369）留在分支 | 前者已重放；后者运行依赖已不存在的 `/tmp` 检出 | 不适用：Foundation 检出不在本机 toolchain cache 中，无法重执行；其作用已由 CG001-C-102 与 C-95–C-101 取代 |

dev-01 与 dev-09 的两个已并入包的完整重放证据在 `dev` 的 `HoTT/verification/runs/` 与 `.claude/goals/CG-006-zfc-complete-formalization/verification/20261008-S7C-IMPORT-REPLAY.json`，本包不重复。

**未覆盖的如实登记**：dev-09 的 `external-foundation-incompleteness`（D09-C-369）本机不能重执行——它的运行依赖一个已不存在的 Foundation 检出路径。这不是“没有试”，是试了之后确认依赖缺失；结论保持 `SOURCE_REPORTED_NOT_REPLAYED`，其作用由 CG-006 在 `1fb01b72` 上的交叉核对（CG001-C-102）与真实 𝗭𝗙𝗖 上的 C-95–C-101 承担。dev-02/03/04 的 `GeometricCompletion.lean`（dev-03/dev-04 各一份）依赖 Mathlib，本机 toolchain pin 未含 Mathlib 构建树，因此不在本包内；它在分支上的 `20261003-MP-ZFC-GEOMETRIC-COMPLETION-001-0{1..5}` 收据保持原样。

## 2. 精确命题

| 编号 | 内容 |
|---|---|
| CG001-C-123 | 表 §1 中标 “✅ 本包收据” 的 16 个 Lean-core 正源，在 pinned Lean 4.34.1、禁网沙盒下**全部编译通过**（exit 0），且每个文件的 SHA-256 与其分支原件逐字节相同 |
| CG001-C-124 | 同一环境下，2 个负控制源**都在预定点被内核拒绝**（`assumption` 失败 / 模块解析失败），说明被控定理确实用到了它所假设的桥 |
| CG001-C-125 | 16 个正源中 165 条 `#print axioms` 报告全部为 “does not depend on any axioms”；stdout/stderr 与 exit code 被 `source-manifest.json` 与二进制哈希一起固定 |
| CG001-C-126 | 八个工作树方向的形式化覆盖是完整的：两条已并入线沿用既有 `dev` 收据，三条有形式包的线由本包补齐，三条无形式包的线判为不适用，一条（dev-09 的外部 Foundation 包）判为本机不可重放并保持 `SOURCE_REPORTED_NOT_REPLAYED` |

## 3. 运行

| run | proof | 预期 | 退出 | 结果 |
|---|---|---|---|---|
| `20261009-CG001-BRANCH-FORMALIZATION-COVERAGE-06` | `MP-CG001-BRANCH-FORMALIZATION-COVERAGE-001` | ACCEPT | 0（16 个正源，165 条无公理报告） | `KERNEL_ACCEPTED_WITH_SCOPE` |
| `20261009-CG001-BRANCH-FORMALIZATION-COVERAGE-NEG-02` | `MP-CG001-BRANCH-FORMALIZATION-COVERAGE-NEG-001` | REJECT | 1 | `KERNEL_REJECTED`（细化阶段，预期内） |

驱动：`.claude/goals/CG-007-formalization-completion/tools/capture_branch_run.py`（本包新增，处理了分支源里根级 `import MetaSubtheoryAudit` 的解析）。

`20261009-CG001-BRANCH-FORMALIZATION-COVERAGE-01/02/03/04/05` 与 `-NEG-01` 是本次为修正驱动而留下的失败或不完整尝试。它们不是任何结论的证据，保留只为记录驱动的修正过程：`-01` 源于源路径基准错误；`-02/03` 源于负控制被放进同一次编译以及依赖模块的搜索路径位置错误；`-04` 的输出路径与根级 `import` 不匹配；`-05` 的 `source-manifest.json` 把依赖模块列了两次；`-06` 补齐 `command_argv` 后即为正式收据。`-NEG-01` 缺 `command_argv`，`-NEG-02` 补齐后即为正式收据。**判据一律以 `-06` 与 `-NEG-02` 为准。**

## 4. 禁止外推

1. 不把“本机可重放”读成“这条线的结论被独立复核”。这些命题在分支上由 GPT 线自己证明，本包只重执行；数学内容、范围与禁止外推仍以各分支自己的 `CLAIM.md` 为准。
2. 不把本包的覆盖读成八条线的**研究**被完成。dev-02/03/04 的 closure 明说它们不是 bare ZFC 的形式化、不是 `ZFC ⊢ False`。
3. 不把 dev-09 的外部 Foundation 包的缺失重放读成“它错了”。判词是 `SOURCE_REPORTED_NOT_REPLAYED`，即本机不能执行。
4. 不把 `GeometricCompletion.lean` 的缺席读成它不可信。它依赖 Mathlib，缺的是本包的 toolchain pin，不是它的收据。

## 5. 文件与来源

18 个 `.lean` 源逐个与三份分支原件比对 SHA-256 后逐一复制：

| 分支 | 文件 |
|---|---|
| `origin/dev-02` | `ActualQPolicy.lean`、`ZFCCompletionPolicyUniformity.lean`、`ZFCMembershipLanguageBoundary.lean`、`ZFCObservationLanguage.lean`、`ZFCUnpaidCompletionPromotion.lean` |
| `origin/dev-03` | `ActualPolicyEvidenceFrontier.lean`、`ActualPolicyWitness.lean`、`MetaObservationConsistency.lean`、`ObservationBoundary.lean`、`SepCompletionPromotion.lean`、`SequentialCompletionContracts.lean`、`UouCompletionPromotion.lean` |
| `origin/dev-04` | `CommunityObservationPolicy.lean`、`CompletionPromotionTension.lean`、`CompletionSubstitutionProfile.lean`、`MetaSubtheoryAudit.lean`、`WrongCompletionPromotionTension.lean`、`WrongMetaSubtheoryAudit.lean` |

逐文件字节数与 SHA-256 见两个 run 的 `source-manifest.json`（`-05` 覆盖 16 个正源，`NEG-01` 覆盖 2 个负控制）。

## 6. 索引路线：为什么这个包不进 `PROOF_VERSION_CLOSURE`

`scripts/audit/verify_formal_proof_run.py` 在 `index_status` 上要求 `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`，
而置该状态的 `scripts/audit/mark_proof_run_indexed.py` 又要求 proof 已登记进
`HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 `packages`/`later_packages`。该 registry 的
claim id 模式只接受 `C-NNN`（见 `scripts/audit/proof_claim_ids.py` 的 `CLAIM_ID`），不接受本包使用的
`CG001-C-NNN`；后者属于 Claude 线编号空间，由 `.claude/goals/CG-001-targeted-overview/证据索引.md`
承载索引。

因此本包沿用 CG-007 全线一致的路线：索引写在 CG-001 证据索引 §36 与共享矩阵末节，`RUN.json` 的
`index_status` 保持 `PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE`（与 `20261009-CG001-GODEL-Q-ZFC-Z0-FULL-01`
等 CG-007 收据相同）。曾尝试把本包登记进 `later_packages` 以走 registry 线，被
`CLAIM_IDS_UNPARSEABLE:CG001-C-123..C-126` 拒绝；那次尝试已把 registry 还原到 HEAD 原样
（`git diff` 为空），未留下格式或内容改动。这不是遗漏，是两条索引线各自的适用范围。

## 7. 工具

`LEAN_TOOLCHAIN.json`：pinned Lean 二进制与版本行。
`capture_branch_run.py`：禁网沙盒驱动器，生成 `formal-proof-run/v1` 收据。
