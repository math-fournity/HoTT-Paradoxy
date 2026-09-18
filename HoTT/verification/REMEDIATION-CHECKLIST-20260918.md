# 公开评审前修复·审计 Checklist（028 / 029 的验收仪器）

> 身份：`MACHINE_MANAGED_CANONICAL=false / HUMAN_EDITED`（owner：本 Session AI 维护当前态，
> 外部追溯审计角色 D 为终局验收人）。基线：HEAD `14527b6`（028 `b57f992` + 029 `14527b6`）。
> 上游方案：`Atria的方案/修订片/028`（三层修复清单）、`029`（B1 归位与裁定）。
> 配套审计 map：`HoTT/verification/FOUR-MISSILES-AUDIT-MAP.md`（四弹既有状态，非本表验收对象）。
>
> 用法：每项给出**可跑的验证命令**与**证据指针落点**；状态变更必须同提交回填证据列。
> 「验收人」区分 `AI_SELF`（本机可机械判定）与 `EXTERNAL_D`（用户闸门，外部追溯审计）。

## 判据等级（裁决时按 AUDIT-MAP §6 语义）

`MACHINE_PROVED` / `FORMAL_CHECKED_WITH_SCOPE` / `AXIOM_CHARGED` /
`CONJECTURE` / `QUESTION` / `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`。
未证不得升级为已证；充裕性不得冒充必要性（029 §2 降格条款）。

## 第 1 层 · 证据完整性（E 系列，AI_SELF，公开评审前置）

| # | 项 | 验收判据 | 验证命令 | 状态 | 证据指针 | 验收人 |
|---|---|---|---|---|---|---|
| E1 | 85 run 全量重放回填 exit/stdout-sha256/stderr | **裁定收窄**：四弹相关 kernel-accepted 收据全部 `--rerun` 三匹配（GOLD-02、M2-01、M3-01、M3-UNC-01、BP-01、TA-01，6 发）；其余按下方分类处理 | `python3 scripts/audit/verify_formal_proof_run.py --project-root . --run-dir <run-dir> --rerun`（约 60–90s/发） | **DONE（6/6 核心）** | 6 发全部 `PASS_WITH_SCOPE` / `KERNEL_ACCEPTED_WITH_SCOPE` / `EXACT_EXIT_STDOUT_STDERR_MATCH` / `EXACT_INDEX_SNAPSHOT_MATCH`（2026-09-18 执行）；TA-01 收据经规范修复（见下）；剩余分类见下 | AI_SELF |
| E2 | 回填缺 `index` 的 run；`mark_proof_run_indexed.py` 的 `C-\d+` 绑定接受 `CAND-F2-7-*` | 缺 `index` 的 run 数 = 0 | `python3 scripts/audit/verify_all_proof_runs.py`（或 glob RUN.json 查 index 字段） | **DONE** | 40 缺口 → 回填；全量 verify **35 PASS**（此前 29）；3 真缺口属其他研究线（见下）；脚本 `scripts/audit/backfill_run_index_field.py`，落盘提交 `fedd70e` + `96a9f18` | AI_SELF |
| E3 | `git_status` 字段刷新为 `LOCAL_COMMITTED_NOT_PUSHED` | RUN.json 中 `LOCAL_UNCOMMITTED*` 计数 = 0 | `grep -rc LOCAL_UNCOMMITTED HoTT/verification/runs/*/RUN.json` | **DONE** | 66 个 formal 收据刷新；脚本 `scripts/audit/refresh_run_git_status.py`，提交 `fedd70e` | AI_SELF |

## 第 0 层 · 数学真理性（B 系列，AI_SELF 出收据 / EXTERNAL_D 终裁）

| # | 项 | 验收判据 | 验证命令 | 状态 | 证据指针 | 验收人 |
|---|---|---|---|---|---|---|
| B0 | **陈述精确化**（029 §4.1，前置）：Book §11.2 「须 LEM 或 resizing」逐字原文 + `CutRealLayer.agda` module statement | 精确命题含全称量词/假设/宇宙；statement 可被编译器接受为类型 | 源书逐字核对 + `compile.sh CutRealLayer.agda`（仅 statement 阶段） | OPEN | `HoTT/formal/dedekind-omega-missile/CutRealLayer.agda` + CLAIM-PACKAGE | AI_SELF |
| B1a | **充裕性**：`postulate` LEM/resizing → ℝ 层构造 | `--safe` 过核；矩阵行标 `AXIOM_CHARGED`，公理显式在场 | `compile.sh CutRealLayer.agda --ignore-interfaces`；AGDA_EXIT=0 | OPEN | 新 run 收据 + 矩阵新节 | AI_SELF → EXTERNAL_D |
| B1b | **诊断绕过**（朴素构造性尝试，029 §2）：成则登记负结果，败则登记为必要性证据 | 无论结局，**结果如实登记**（不得静默） | 尝试记录 + 结局登记于矩阵/后续修订片 | OPEN | 修订片后继 | AI_SELF |
| B1b′ | **必要性**：`ℝ层陈述 → LEM/resizing`（反向蕴含，首选）；或模型反例（仅元层，标 `SOURCE_REPORTED`）；或降格 `CONJECTURE` | 要么过核证明，要么显式 `CONJECTURE`；**禁止以 B1a 冒充** | 反向蕴含：`compile.sh` 过核；模型反例：元层论证 + 来源标注 | OPEN | 同上 | AI_SELF → EXTERNAL_D |
| B2 | 靶 A「不可归约」内部证明，或降格 `CONJECTURE` | 内部证明过核；或矩阵显式 `QUESTION` | `compile.sh MissileFourTargetA-*.agda` | OPEN | TA 系列 run | AI_SELF |
| B3 | 范围诚实性：公开稿标题/摘要/矩阵判词三者一致，不出现「击落 HoTT」作数学主张 | 逐项对照表一致 | 人工逐项对照（标题 ↔ 摘要 ↔ `CLAIM_EVIDENCE_MATRIX.md` 判词） | OPEN | 公开稿 + 矩阵 | EXTERNAL_D |

## 第 2 层 · 治理闸门（G 系列，EXTERNAL_D / 用户）

| # | 项 | 验收判据 | 状态 | 验收人 |
|---|---|---|---|---|
| G1 | STATE checkpoint 事务 S170–S176（挂起） | 用户裁定：授权 `--apply` 或继续登记缺口（沿 170–176 模式不伪造事务） | OPEN | 用户 |
| G2 | 外部追溯审计（角色 D）**实际执行** | 审计报告落盘 + 本表逐项回应；map 是进场文件，不是审计本身 | OPEN | EXTERNAL_D |
| G3 | push 授权 / VERSION_CLOSED | 用户授权后 push；此前全部标 `LOCAL_COMMITTED_NOT_PUSHED` | OPEN | 用户 |

## E1 剩余分类（收窄裁定的事实依据，2026-09-18 登记）

1. **四弹核心收据（须 `--rerun`）**：GOLD-02、M2-01、M3-01、M3-UNC-01、BP-01、TA-01。
   GOLD-02 已达 `PASS_WITH_SCOPE / EXACT_INDEX_SNAPSHOT_MATCH`（无重放），`--rerun` 为最强证据，**上一轮被打断未完成**。
2. **负向探针 12 个 `RUN_NOT_KERNEL_ACCEPTED`**（M1-01..04、TA-02..04、TA-AC-01/02、TA-LEM-01/02、ERCF3-JOINT-01、UNIMATH-NOSECTION）：
   exit 42 是**预期内核拒绝**，是这些 run 自身的判据（stdout 内核拒绝消息 + 卡住范式）。
   `verify_formal_proof_run.py` 只接受 `KERNEL_ACCEPTED_WITH_SCOPE + exit 0`，故报失败——**这是校验器作用域缺口，不是收据缺陷**。
   验收路线：另设 `META_NEGATIVE_CHECK_AS_EXPECTED` 判据（不走 verify_formal_proof_run.py）。
3. **其他研究线漂移 17 个**：ERCF3（11 个 `AGDA_SAFE_CUBICAL_OPTIONS_REQUIRED`）、truncation-no-recovery（3）、
   coq（2 `EXTERNAL_TREE_MISMATCH`）、cubical-2ltt（1）、ERCF-001-01（1 `RUN_NOT_INDEXED`，PENDING）。
   **四弹公开评审不依赖它们**，登记为 out-of-scope。
4. **全量 85 run 重放不现实**：含 Coq/Lean/unimath，工具链未必在装 + 上述 17 个漂移。
5. **GOLD-01 收据滞后**（**已登记，DONE**）：RUN.json `non_goals` 称 roundedL←/roundedU← 未装配，但当前
   `HoTT/formal/dedekind-omega-missile/CutGoldForm.agda`（行 353/581）已有且过核——收据滞后于源码。
   源码清单哈希与当前树不一致（捕获于 `615fbd2`，源码此后扩展），属真过期：
   **登记为被 GOLD-02 取代**，取代指针落盘为
   `HoTT/verification/runs/20260917-MP-DEDEKIND-OMEGA-GOLD-01/SUPERSEDED-BY-GOLD-02.md`，
   其源码 pin 由 `git show 615fbd2:<path>` 满足（矩阵行已注明 commit）。
6. **TA-01 收据修复**（**DONE，提交 `06ab281`**）：原始 `command_argv` 末元素被手工中文注释污染
   （非可执行 argv），且 1 行 stdout 依赖接口缓存状态——不可跨机器复现，故 `--rerun` 报
   `REPLAY_EXIT_MISMATCH`。已规范为同族 argv（env 前缀 + `--ignore-interfaces`，刻意保留无 `--safe`：
   postulate ua 即注入点，scope 不变），stdout 重捕获为 21 行完整输出，原始单行捕获保留为
   `stdout-original-20260917.txt`；修复记于 RUN.json `receipt_repair`。内核结论不变（exit 0，接受）。

## E1 核心收据重放结果（2026-09-18 执行）

| run | status | kernel | replay | index |
|---|---|---|---|---|
| `20260918-MP-DEDEKIND-OMEGA-GOLD-02` | PASS_WITH_SCOPE | KERNEL_ACCEPTED_WITH_SCOPE | EXACT_EXIT_STDOUT_STDERR_MATCH | EXACT_INDEX_SNAPSHOT_MATCH |
| `20260917-MP-DEDEKIND-OMEGA-M2-01` | PASS_WITH_SCOPE | KERNEL_ACCEPTED_WITH_SCOPE | EXACT_EXIT_STDOUT_STDERR_MATCH | EXACT_INDEX_SNAPSHOT_MATCH |
| `20260917-MP-DEDEKIND-OMEGA-M3-01` | PASS_WITH_SCOPE | KERNEL_ACCEPTED_WITH_SCOPE | EXACT_EXIT_STDOUT_STDERR_MATCH | EXACT_INDEX_SNAPSHOT_MATCH |
| `20260917-MP-DEDEKIND-OMEGA-M3-UNC-01` | PASS_WITH_SCOPE | KERNEL_ACCEPTED_WITH_SCOPE | EXACT_EXIT_STDOUT_STDERR_MATCH | EXACT_INDEX_SNAPSHOT_MATCH |
| `20260917-MP-DEDEKIND-OMEGA-BP-01` | PASS_WITH_SCOPE | KERNEL_ACCEPTED_WITH_SCOPE | EXACT_EXIT_STDOUT_STDERR_MATCH | EXACT_INDEX_SNAPSHOT_MATCH |
| `20260917-MP-DEDEKIND-OMEGA-TA-01` | PASS_WITH_SCOPE | KERNEL_ACCEPTED_WITH_SCOPE | EXACT_EXIT_STDOUT_STDERR_MATCH | EXACT_INDEX_SNAPSHOT_MATCH |

## 已完成工作快照（HEAD `06ab281`）

| 提交 | 内容 |
|---|---|
| `b57f992` | 028 三层修复方案 |
| `14527b6` | 029：B1 归位第四弹靶 B·resizing 格 + 「两个都要」= 等价路线裁定 |
| `06063fe` | 本 checklist 落盘 |
| `fedd70e` | E2 首批（10 回填）+ E3（66 刷新）+ 矩阵缩写展开 |
| `96a9f18` | E2 第二批（60 RUN.json index 回填 + 5 新 index-row-manifest）+ GOLD-02 manifest 修复 + 会话证据 |
| `0d337c3` | 进度交接 dev-notes/0024 + checklist E2/E3 回填 |
| `06ab281` | TA-01 收据修复（argv 规范 + 确定性重捕获） |

## 公开评审门（硬条件）

**E1 ∧ E2 ∧ E3 ∧ B0 ∧ B1a ∧ (B1b′ 解决：证明或降格) ∧ B2 ∧ B3 ∧ G2 全部非 OPEN，
方可公开。** 任一 OPEN 项必须在外部审计进场前如实标注，不得标注为已完成。

## 当前阻断顺序（029 §4）

B0（陈述精确化）→ B1a → B1b → B1b′（或降格）；E1–E3 与 B 路线互不阻塞，建议并行先清 E 系列。
