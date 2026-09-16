---
name: hott-paradox-search-sop
description: 执行"用现实对齐寻找 HoTT 非现实前提"这条方案的 SOP。按步骤驱动 PREMISE-001 / GEN-001 链；每完成一个流程、以及每次穿越上下文压缩边界之后，系统调查前一个阶段或 Session 的工作是否应当调整和优化方案；每次方案优化必须立即 git 提交，使方案演化在 git log 中可追踪。
metadata:
  version: "1.1.0"
  role: "execution"
  language: "zh-CN"
  plan_index: "Atria的方案/修订片.md"
  goal_file: "goal-1.md"
  state_index: ".codex/research/hott/STATE.json"
  governance_skill: "hott-local-session-governance"
  business_skill: "hott-paradox-research"
  plan_core_shards: "修订片 003 / 006 / 007 / 008 / 009"
---

# 方案执行与方案演化 SOP

本 Skill 是"用现实对齐找出 HoTT 非现实前提"这条方案的**执行驱动器与方案演化纪律**。
它不产生数学结论，也不替代业务研究 Skill；它规定**每一步怎么走、走完怎么反思、
反思改了方案怎么留痕**。

用户通过 `goal-1.md`（一个只含指引的索引文件）配合 `/goal` 驱动本 Skill；本 Skill
也可以在用户授权下自设 goal 推进。

## 1. 何时触发本 Skill

以下任一条件成立即加载并遵守本 Skill：

1. 用户要求"执行方案 / 走下一步 / 继续 PREMISE-001 / 跑 GEN-001"；
2. 用户用 `/goal` 指向 `goal-1.md`，或要求按 SOP 完成 goal；
3. 一个流程步骤刚完成，需要决定是否调整方案；
4. 上下文刚被压缩，或跨 Session / 跨目录接手本方案；
5. 用户要求审视"方案是否需要优化"。

触发本 Skill **之前**必须先完成本地治理 Skill 的启动闭包（四件套全文 + STATE）。
本 Skill 不重复四件套加载，只消费其结果。

## 2. 方案地图（只指路，不复制正文）

| 职责 | 位置 |
|---|---|
| 方案总索引（分片表） | `Atria的方案/修订片.md` |
| GEN-001 有界生成器验收单元 | `Atria的方案/修订片/003` |
| S1–S6 供给策略与 SUPPLY_REGISTRATION 规程 | `Atria的方案/修订片/006` |
| 供给层加严（corpus_pressure / reality_anchor_holder） | `Atria的方案/修订片/007` |
| PREMISE-001：A–G 分母、P1–P4 分工、必填字段 | `Atria的方案/修订片/008` |
| P3/P4 自动化执行与外部审计层 | `Atria的方案/修订片/009` |
| 当前任务队列与下一动作 | `.codex/research/hott/STATE.json`（`active` / `execution_control.next_minimal_verification`） |
| goal 索引 | `goal-1.md` |
| 方案演化轨迹 | `git log --grep=plan-revise` |

**权威顺序**：方案的当前真值是修订片正文 + STATE；`goal-1.md` 只是指针，冲突时以
修订片与 STATE 为准。四件套（核心认知/方向追踪/全景视野/扩展认知）是用户原文与
投影权威，本 Skill 不改写它们。

## 3. 执行循环：一个步骤的七段

每一步都走完 S-1 到 S-7，不得跳段。

**S-1 闭包恢复**：沿用治理 Skill，确认四件套已全文加载、STATE 已读、本 Skill 已加载。
压缩后或跨 Session 接手时，按 §4 补齐。

**S-2 定位当前步骤**：读 STATE 的 `active` 队首与 `next_minimal_verification`，
对照 `goal-1.md` 的"当前步骤"。三者冲突时以 STATE 为准，并把 `goal-1.md` 指针同步过去。

**S-3 执行该步骤**：按修订片 008 的字段规格产出（P1 逐字前提 + 出处；P2 结构分析：
`reality_skeleton` / `divergence_point` / `evidence_level` / 至少一个 `OMISSION_SHAPE`）。
角色分工不越界：AI 执行 P1/P2 与 P3/P4（P3/P4 必须带修订片 009 §3 的
P3P4_AUDIT_TRAIL 全部必填字段，含 steelman 与 falsifier，全部标
AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT，不得自证为结论）；生效复核由外部 AI
审计（角色 D，用户安排，追溯性）；引擎在冻结文法上枚举/归约；原生核做校验，
不得由 Python 枚举或普通 Lean Eq 替代（F-011）。

**S-4 反思**：逐条回答 §5 的清单。不允许"总体良好"这种合并答复。

**S-5 裁决并分流**：
- 若需调整方案 → 修订对应修订片/规程 → **立即 git 提交（见 §6）** → 若改动涉及投影或
  STATE，走 canonical checkpoint（`.codex/tools/cognition_runtime.py`），不得直接编辑 STATE。
- 若不需调整 → 在本轮 dev-notes 明确登记"已审，无需调整"及理由，**避免后续重复审计**。

**S-6 收尾**：dev-notes 归档 + 逐 KC 回评（沿用治理 Skill §5）。

**S-7 推进步骤指针**：更新 STATE（经 checkpoint）与 `goal-1.md` 的"当前步骤"段。

## 4. 穿越压缩边界后的恢复

上下文压缩后，方案的"做到哪一步、上一步是否已反思"必须**从持久载体重建**，不得凭记忆：

1. 读 STATE（`active` / `execution_control` / `latest_session`）；
2. 读最近 1–2 条 dev-notes 条目（本 Session 的用户问题与最终回复）；
3. 跑 `git log --grep=plan-revise` 与 `git log` 最近若干条，区分**方案修订**与**步骤产出**；
4. 对照 `goal-1.md` 的"当前步骤"；
5. 若最近一次步骤产出**没有**附带 `reflection:` 痕迹（无论 no-plan-change 还是 revised），
   则该步骤的 S-4 未完成，**先补反思再继续**。

恢复后第一件事是补齐未完成的反思，不是赶进度。

## 5. 反思清单（每步必答，逐条）

1. **分母一致性**：当前分母的每一条，其 P2 是否仍与用户当前认识论一致？尤其
   `reality_skeleton` 有没有被写成"无法构造"（那是被用户否证的旧前提的残余）？
2. **策略锚定**：本步产出是否由 S1–S6 之一驱动并完成 `SUPPLY_REGISTRATION`？
   有没有绕过策略锚定、退化成自由联想？
3. **角色越界**：AI 执行 P3/P4 时，每条是否带全 P3P4_AUDIT_TRAIL 必填字段
   （尤其 steelman 与 falsifier）？有没有把 pending-audit 的候选判定当作已成立
   结论交付？有没有用模式匹配判断候选成立（该层只走原生核）？有没有用 Python
   枚举或普通 Lean Eq 冒充原生核？
4. **负结论误用**：scoped negative 是否被当成"该族无候选"或"发现能力缺失"？
   （三者是三回事，见修订片 003 §6。）
5. **信封外候选**：有没有来自新论文/版本/实现/consumer、跨框架差分、反例、
   新现实任务的候选落在当前分母之外？若有，登记 unknown ingress，不得静默丢弃。
6. **被后续修正推翻**：前一阶段/Session 的方案前提，有没有被核心认知的新 generation
   （如 KC-000044–046 的认识论修正）推翻？若有，对应修订片必须原位改写并提交。
7. **漂移累积**：距上一次 `plan-revise` 之间，是否累积了本应一起处理的方案漂移？

每条给出**证据**（文件/行、commit、运行收据）或明确标"无证据、仅判断"。

## 6. 方案演化与 git 纪律

方案是可演化的，但演化必须可追踪。以下为硬纪律：

- **方案修订必须立即提交**，提交信息格式：
  `plan-revise(<owner 或修订片号>): <一句话变更>; source=<reflection|compaudit|user>`
- **步骤产出必须立即提交**，提交信息格式：
  `<任务号>(step-N): <产出摘要>; reflection=<no-plan-change|revised-in <commit-hash>>`
  即：每一步的提交**必须携带反思结论**，没有反思结论的步骤提交是不合规的。
- 方案修订与步骤产出**不得混在同一个 commit**，除非它们属于同一次原子 checkpoint 事务。
- 提交前跑校验器：`scripts/audit/verify_governance_shards.py` 与（若涉及核心认知）
  `scripts/audit/verify_core_cognition.py`；涉及 STATE/投影走 canonical checkpoint。
- 不自动 push、不打 tag（沿用项目 AGENTS）。
- **禁止不提交就继续下一步**：否则方案漂移在 git log 中不可追踪，本 SOP 的存在失去意义。

git log 是本方案的演化账本。`git log --grep=plan-revise` 应能完整复述方案如何从
v1 走到当前版本，以及每一次修订的触发来源。

## 7. 停止条件与失败判词

```text
PLAN_STEP_EXHAUSTED_WITH_SCOPE
  / 当前任务的全部步骤完成，每步带 reflection 痕迹
  / 方案演化账本（plan-revise 序列）完整
  / 不声称找到悖论；不声称分母穷尽开放候选空间

P3P4_AI_EXECUTED_PENDING_AUDIT  ← 修订片 009 生效后替代 USER_ADJUDICATION_REQUIRED
  / AI 已对每条完成 P3/P4 判定，全部带 P3P4_AUDIT_TRAIL 必填字段
  / 全部条目 audit_status = AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
  / 不阻塞推进：判为非现实者带 pending-audit 标记进 SUPPLY_REGISTRATION
  / 用户保留非介入式推翻权；外部 AI 审计（角色 D）为终局复核层
  / 不构成"该前提非现实"的结论；结论仍需 GEN-001 链 + 原生核（MATH_PROOF_BEFORE_DELIVERY_V1）

PLAN_REVISION_DIVERGENCE
  / 反思连续 3 轮产生互相矛盾或来回反转的方案修订
  / 停止修订，把冲突摆给用户裁决，不得继续堆叠修订
```

## 8. 与另外两个 Skill 的分工（不重叠）

- `hott-local-session-governance`（治理）：Session 启动闭包、四件套加载、逐 KC 回评、
  checkpoint 纪律。**本 Skill 消费其结果，不重复。**
- `hott-paradox-research`（业务）：候选的生成、构造、形式化、机器核验本身。
  **本 Skill 不做研究，只驱动"下一步是哪一步、走完要不要改方案"。**
- 本 Skill（执行）：步骤驱动 + 反思循环 + 方案演化 git 纪律。

三者可同一次执行中按需加载；本 Skill 不是它们的替代，是它们之间的**调度层**。

## 9. 本 Skill 不声称的

- 本 SOP 提升的是**可追踪性与分工确定性**，不提升找到悖论的概率，也不预设悖论存在。
- 反思清单的第 1–7 条是**检查项**，不是通过即正确；未发现问题不等于没有问题。
- 本 Skill 不产出任何数学结论（F-011）；非现实性判定永不由 AI 自证。
- 若用户的新指令与本 Skill 冲突，用户指令优先；冲突本身记入 dev-notes。
