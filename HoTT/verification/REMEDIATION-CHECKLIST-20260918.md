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
| E1 | 85 run 全量重放回填 exit/stdout-sha256/stderr | 任意 run 第三方重放三匹配 100%；`exit_code` 字段不再为 `None`，负向探针为实测值（当前机 UnequalTerms=42） | `sh HoTT/formal/dedekind-omega-missile/compile.sh <Mod>.agda --ignore-interfaces`（仓库根执行）逐 run 比对；新增 `scripts/audit/sweep_receipt_replay.py` | OPEN | 待回填（RUN.json × 85） | AI_SELF |
| E2 | 回填 40 个缺 `index` 的 run；`mark_proof_run_indexed.py` 的 `C-\d+` 绑定接受 `CAND-F2-7-*` | 缺 `index` 的 run 数 = 0 | `python3 -c "…glob RUN.json 查 index 字段…"`；`python3 scripts/audit/verify_formal_proof_run.py --run-dir <run>` 逐 run PASS | OPEN | 待回填 | AI_SELF |
| E3 | `git_status` 字段刷新为 `LOCAL_COMMITTED_NOT_PUSHED` | RUN.json 中 `LOCAL_UNCOMMITTED*` 计数 = 0 | `grep -rc LOCAL_UNCOMMITTED HoTT/verification/runs/*/RUN.json` | OPEN | 待回填 | AI_SELF |

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

## 公开评审门（硬条件）

**E1 ∧ E2 ∧ E3 ∧ B0 ∧ B1a ∧ (B1b′ 解决：证明或降格) ∧ B2 ∧ B3 ∧ G2 全部非 OPEN，
方可公开。** 任一 OPEN 项必须在外部审计进场前如实标注，不得标注为已完成。

## 当前阻断顺序（029 §4）

B0（陈述精确化）→ B1a → B1b → B1b′（或降格）；E1–E3 与 B 路线互不阻塞，建议并行先清 E 系列。
