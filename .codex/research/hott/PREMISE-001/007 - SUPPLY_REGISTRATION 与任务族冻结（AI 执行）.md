<!-- governance-shard:v2
logical_id: PREMISE-001
shard_id: 007
index: ../PREMISE-001.md
-->

# SUPPLY_REGISTRATION 与任务族冻结（AI 执行）

> step-4。角色 A 执行，依据修订片 008 §5（三道闸）+ 修订片 009 §2/§3
> （reality_anchor_holder 扩展第三取值）+ 修订片 003（GEN-001 任务规格九字段）。
> **全部注册项带 pending-audit 标记，外部审计推翻时按 depends_on 回滚。**
> 本分片**不产生数学结论**：注册的是"把候选交给机器"的交接，不是候选成立。

## 1. 注册总则

- 只注册 005/006 分片中 ai_verdict=非现实 的 9 条。现实/暂不判定者不注册。
- 每条必填 SUPPLY_REGISTRATION 全部字段（008 §5），其中：
  - `reality_anchor_holder` = `AI(带审计层, pending)`——修订片 009 §2 的第三合法取值；
  - `human_supply` = AI 冻结的任务定义（修订片 009 §4 的 3a 步），
    **显式标注是 AI 供给而非用户供给**，防止冒充（修订片 003 §5 的角色纪律）；
  - `audit_status` = `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`；
  - `rollback_token` = 本条的 depends_on 链（外部审计推翻时回滚的下游清单）。
- **三道闸**：S1–S6 锚定 ✓（每条标 strategy）；corpus_pressure 声明 ✓（每条标依据）；
  reality_anchor_holder ✓（第三取值）。

## 2. 逐条注册

### SUPPLY-001 · PREMISE-A-03（Nat：计数过程当作已完成）

- **strategy**：S3（理论经济/稠密族）+ S5（表达保真）——"良基性内置"使"可能不终止"无对象承担
- **kc_anchor**：KC-000014/022（方向 B：现实无法完成而理论当作已完成）
- **premise_id**：PREMISE-A-03
- **omission_shape**：completion, sequencing
- **human_supply**：AI 冻结任务族 `TASK-FAMILY-COMPLETION-PROCESS`：
  任务定义"一个其正确性依赖计数过程是否终止的验证任务"；构造子清单 =
  {计数器、终止边界、非终止延续、结果消费者}；分母大小 = 有限（构造子笛卡尔积，界=3）；
  观察层 = 计数步；完成属性 = 到达终止边界；oracle = 终止性判定。
  **标注：AI 供给，非用户供给。**
- **program_role**：引擎在冻结文法上枚举"计数器 × 边界 × 延续 × 消费者"组合，
  grammar-preserving 归约到"消费者是否在无终止边界时得到结果"
- **kernel_role**：原生核校验归约后的命题（需支持 Nat/递归的系统：Agda/Coq 均可，
  但结论若涉及 HoTT 特有结构须用 cubical 原生系统，F-011）
- **premise_step**：P1–P4 全部（AI 执行）
- **corpus_pressure**：省略结构撑得起（判定理由是"被移除者在系统内无对象承担"，
  不依赖语料频率）；但 A-03 自评 corpus 风险中偏高，**注册时保留该自评**
- **reality_anchor_holder**：AI(带审计层, pending)
- **evidence_anchors**：005 分片 A-03；002 分片 A-03；CORE_RULES.md（Nat 规则 C09）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**（推翻时回滚）：SUPPLY-001 → TASK-FAMILY-COMPLETION-PROCESS 冻结
  → GEN-001 run（若已开）→ CE-MAP 行（若已建）

### SUPPLY-002 · PREMISE-A-11（W：生长过程当作已完成的树）

- **strategy**：S3 + S5；与 SUPPLY-001 同形
- **kc_anchor**：KC-000014/022
- **premise_id**：PREMISE-A-11
- **omission_shape**：completion, sequencing
- **human_supply**：AI 冻结任务族 `TASK-FAMILY-WELLFOUNDED-BRANCHING`：
  任务定义"一个其结论依赖分支展开是否终止的任务"；构造子清单 =
  {分支节点、展开深度界、非终止分支、叶消费者}；分母 = 有限（界=3）；
  观察层 = 展开步；完成属性 = 到达叶；oracle = 良基性判定。
  **标注：AI 供给。**
- **program_role**：枚举"节点 × 深度界 × 非终止分支 × 消费者"，归约到
  "消费者是否在无深度界时得到叶结果"
- **kernel_role**：原生核校验（系统要求同 SUPPLY-001）
- **premise_step**：P1–P4 全部（AI 执行）
- **corpus_pressure**：省略结构撑得起（同 SUPPLY-001 的结构论证）
- **reality_anchor_holder**：AI(带审计层, pending)
- **evidence_anchors**：005 分片 A-11；002 分片 A-11；CORE_RULES.md（W 规则）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：SUPPLY-002 → TASK-FAMILY-WELLFOUNDED-BRANCHING → GEN-001 → CE-MAP
- **合并建议**：与 SUPPLY-001 合并为单一 GEN-001 任务族"过程性 vs 已完成性"
  （共同分母）；**合并与否由外部审计决定，AI 只建议**——若合并，
  两条的 depends_on 链合并为一。

### SUPPLY-003 · PREMISE-B-01（定义相等可判定，语义同一推出界外）

- **strategy**：S5（表达保真）——"同一性判据依赖观察层"在系统内无对象承担
- **kc_anchor**：KC-000031/035（极简理论覆盖/表达保真）
- **premise_id**：PREMISE-B-01
- **omission_shape**：observability, self-evidence
- **human_supply**：AI 冻结任务族 `TASK-FAMILY-IDENTITY-OBSERVATION-LAYER`：
  任务定义"一个其'两件东西是否同一'的结论依赖指定观察层/用途的任务"；
  构造子清单 = {待判对象对、观察层（语法/命题/用途）、同一性判据、结论消费者}；
  分母 = 有限（界=3）；oracle = 同一性在给定观察层下的判定。
  **标注：AI 供给。**
- **program_role**：枚举"对象对 × 观察层 × 判据 × 消费者"，归约到
  "同一性结论是否随观察层改变"
- **kernel_role**：原生核校验（须能表达 definitional vs propositional equality 的分离：
  Agda/Coq 原生支持；若涉及 univalence 须 cubical 原生系统）
- **premise_step**：P1–P4 全部（AI 执行）
- **corpus_pressure**：省略结构撑得起（判定理由是"被移除者在系统内无归宿"，
  不依赖语料频率）
- **reality_anchor_holder**：AI(带审计层, pending)
- **evidence_anchors**：005 分片 B-01；002 分片 B-01；CORE_RULES.md（C03/C04）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：SUPPLY-003 → TASK-FAMILY-IDENTITY-OBSERVATION-LAYER → GEN-001 → CE-MAP
- **合并建议**：与 G-01/G-02 构成"同一性层深与锚定"主题簇；**注意 G-01/G-02 判为
  暂不判定，因此不进入本注册**——若外部审计将 G-01/G-02 翻转为非现实，
  需新建 SUPPLY 并加入本簇。

### SUPPLY-004 · PREMISE-D-01（区间：稠密可分性当作给定能力）

- **strategy**：S3（稠密族）——"可分性是条件还是能力"
- **kc_anchor**：KC-000003（稠密 vs 量子化）、KC-000044（骨架式模仿）
- **premise_id**：PREMISE-D-01
- **omission_shape**：continuity（依前提本性选定）
- **human_supply**：AI 冻结任务族 `TASK-FAMILY-DIVISIBILITY-CONDITION-OR-CAPABILITY`：
  任务定义"一个其正确性依赖转动/连续运动在给定测量条件下是否可再分的任务"；
  构造子清单 = {区间位置、测量条件（分辨率等级）、可分性判定、运动消费者}；
  分母 = 有限（界=3）；观察层 = 分辨率等级；oracle = 可分性在条件下的判定。
  **标注：AI 供给。**
- **program_role**：枚举"位置 × 条件 × 可分性 × 消费者"，归约到
  "运动结论是否在条件不允许更细时仍依赖更细"
- **kernel_role**：原生核校验（须支持区间/连接的 cubical 原生系统：cubicaltt/redtt/cooltt/cctt
  之一，F-011 硬约束）
- **premise_step**：P1–P4 全部（AI 执行）
- **corpus_pressure**：**语料频率为主风险条目**——稠密性是 KC-000043 阻力最强处。
  按修订片 009 §3，corpus_self_audit 高，置信度已降一档；
  **注册保留该风险标注，外部审计必须优先复核本条。**
- **reality_anchor_holder**：AI(带审计层, pending)
- **evidence_anchors**：006 分片 D-01；003 分片 D-01；EXTENSIONS_AND_METATHEORY.md（区间）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：SUPPLY-004 → TASK-FAMILY-DIVISIBILITY → GEN-001 → CE-MAP
- **合并建议**：与 SUPPLY-006（E-04）/SUPPLY-008（G-03）构成 continuity 三联；
  **建议合并为单一 GEN-001 任务族"可分性是条件还是能力"**（共同分母可统一为
  "可分性 × 测量条件 × 消费者"）；合并与否由外部审计决定。

### SUPPLY-005 · PREMISE-D-04（Kan 填充：存在当作已就位）

- **strategy**：S4（自反/资源族）+ S3——"存在性 ≠ 可用性"
- **kc_anchor**：KC-000029（理论经济：存在性顶替被省略者）
- **premise_id**：PREMISE-D-04
- **omission_shape**：completion, self-evidence
- **human_supply**：AI 冻结任务族 `TASK-FAMILY-EXISTENCE-VERSUS-AVAILABILITY`：
  任务定义"一个其结论依赖填充物/产能是否在需要时可用（而非仅存在）的任务"；
  构造子清单 = {填充物存在性、就位状态、调用时刻、任务消费者}；
  分母 = 有限（界=3）；oracle = 可用性判定（存在 ∧ 就位 ∧ 及时）。
  **标注：AI 供给。**
- **program_role**：枚举"存在性 × 就位 × 时刻 × 消费者"，归约到
  "任务结论是否在'存在但未就位'时出错"
- **kernel_role**：原生核校验（须支持 Kan 填充的 cubical 原生系统，F-011）
- **premise_step**：P1–P4 全部（AI 执行）
- **corpus_pressure**：省略结构撑得起，**但本条置信度低（自评最可能被推翻）**——
  判定理由在纯形式层较弱（形式层项的供给确实是无限的）。
  注册保留低置信度标注。
- **reality_anchor_holder**：AI(带审计层, pending)
- **evidence_anchors**：006 分片 D-04；003 分片 D-04；EXTENSIONS_AND_METATHEORY.md（Kan）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：SUPPLY-005 → TASK-FAMILY-EXISTENCE-VERSUS-AVAILABILITY → GEN-001 → CE-MAP
- **合并建议**：与 SUPPLY-009（G-05）合并为"存在性 vs 可用性"单族；**低置信度条目，
  外部审计优先复核。**

### SUPPLY-006 · PREMISE-E-04（截断塔稠密性：细分当作已提供能力）

- **strategy**：S3（稠密族）；与 SUPPLY-004 同形
- **kc_anchor**：KC-000003、KC-000044
- **premise_id**：PREMISE-E-04
- **omission_shape**：continuity（依前提本性选定）
- **human_supply**：AI 冻结任务族——**建议并入 SUPPLY-004 的
  TASK-FAMILY-DIVISIBILITY**（量仪精度域与转动域是同一"可分性 × 测量条件"分母的
  两个现实入口）。若外部审计决定不合并，另立
  `TASK-FAMILY-TRUNCATION-TOWER-RESOLUTION`，构造子清单同形。
  **标注：AI 供给。**
- **program_role**：同 SUPPLY-004（统一分母下枚举）
- **kernel_role**：原生核校验（须支持截断层级的系统；h-level 可在 Agda/Coq 表达，
  但截断塔的 cubical 定理形式须原生系统，F-011）
- **premise_step**：P1–P4 全部（AI 执行）
- **corpus_pressure**：**语料频率为主风险条目**（与 SUPPLY-004 同列三联）；
  置信度已降一档
- **reality_anchor_holder**：AI(带审计层, pending)
- **evidence_anchors**：006 分片 E-04；003 分片 E-04；EXTENSIONS_AND_METATHEORY.md（截断塔）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：SUPPLY-006 →（并入 SUPPLY-004 链 or 独立链）→ GEN-001 → CE-MAP

### SUPPLY-007 · PREMISE-E-02（命题截断：见证信息不可恢复）

- **strategy**：S5（表达保真）——"信息销毁的不可逆性"
- **kc_anchor**：KC-000031/035
- **premise_id**：PREMISE-E-02
- **omission_shape**：observability, completion
- **human_supply**：AI 冻结任务族 `TASK-FAMILY-WITNESS-RECOVERABILITY`：
  任务定义"一个在施加截断后、后续工序需要见证才能完成的任务"；
  构造子清单 = {见证、截断施加、后续工序、完成判定}；
  分母 = 有限（界=3）；oracle = 后续工序在截断后是否可完成。
  **标注：AI 供给。**
- **program_role**：枚举"见证 × 截断 × 工序 × 判定"，归约到
  "完成是否需要被截断丢弃的信息"
- **kernel_role**：原生核校验（须支持命题截断的系统：Agda/Coq 的 squash/Prop，
  或 cubical 的 IsOne 截断；F-011）
- **premise_step**：P1–P4 全部（AI 执行）
- **corpus_pressure**：省略结构撑得起（判定理由依赖形式层事实：截断丢弃见证信息）
- **reality_anchor_holder**：AI(带审计层, pending)
- **evidence_anchors**：006 分片 E-02；003 分片 E-02；CORE_RULES.md（命题截断）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：SUPPLY-007 → TASK-FAMILY-WITNESS-RECOVERABILITY → GEN-001 → CE-MAP

### SUPPLY-008 · PREMISE-G-03（高阶相等无限迭代：终止/锚定条件被移出）

- **strategy**：S3（稠密族）——"迭代的终止条件被完全移出"
- **kc_anchor**：KC-000003、KC-000044
- **premise_id**：PREMISE-G-03
- **omission_shape**：continuity, self-evidence
- **human_supply**：AI 冻结任务族——**建议并入 SUPPLY-004 的
  TASK-FAMILY-DIVISIBILITY**（运动域与转动域/量仪域同属"可分性 × 测量条件"分母）。
  若不合并，另立 `TASK-FAMILY-HIGHER-PATH-ANCHORING`：
  任务定义"一个其结论依赖高阶相等的迭代深度是否需要锚定的任务"；
  构造子清单 = {路径对、迭代深度、锚定条件、结论消费者}；分母 = 有限（界=3）。
  **标注：AI 供给。**
- **program_role**：枚举"路径对 × 深度 × 锚定 × 消费者"，归约到
  "结论是否在无锚定时出错"
- **kernel_role**：原生核校验（须支持 identity type 高阶结构的 cubical 原生系统，F-011）
- **premise_step**：P1–P4 全部（AI 执行）
- **corpus_pressure**：**语料频率为主风险最高条目**（三重诱导：语料流利 +
  004 表导航 + 用户路径同形）；置信度已降一档，且**明确不把"与圆环悖论同形"
  当作证据**。外部审计必须优先复核本条。
- **reality_anchor_holder**：AI(带审计层, pending)
- **evidence_anchors**：006 分片 G-03；003 分片 G-03；CORE_RULES.md（identity 规则）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：SUPPLY-008 →（并入 SUPPLY-004 链 or 独立链）→ GEN-001 → CE-MAP

### SUPPLY-009 · PREMISE-G-05（所有 cofibration 可填充设为构造可用）

- **strategy**：S4 + S3；与 SUPPLY-005 同形
- **kc_anchor**：KC-000029
- **premise_id**：PREMISE-G-05
- **omission_shape**：completion, self-evidence
- **human_supply**：AI 冻结任务族——**建议并入 SUPPLY-005 的
  TASK-FAMILY-EXISTENCE-VERSUS-AVAILABILITY**（同一"存在 ≠ 可用"分母）。
  若不合并，另立 `TASK-FAMILY-FILLABILITY-AS-CONSTRUCTIVE`。
  **标注：AI 供给。**
- **program_role**：同 SUPPLY-005
- **kernel_role**：原生核校验（cubical 原生系统，F-011）
- **premise_step**：P1–P4 全部（AI 执行）
- **corpus_pressure**：省略结构撑得起，**但置信度低（自评最可能被推翻，与 SUPPLY-005 同列）**
- **reality_anchor_holder**：AI(带审计层, pending)
- **evidence_anchors**：006 分片 G-05；003 分片 G-05；EXTENSIONS_AND_METATHEORY.md
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：SUPPLY-009 →（并入 SUPPLY-005 链 or 独立链）→ GEN-001 → CE-MAP

## 3. 任务族汇总（供外部审计决定合并）

| 建议任务族 | 成员 | 共同分母 | corpus 风险 | 置信度 |
|---|---|---|---|---|
| `TASK-FAMILY-DIVISIBILITY-CONDITION-OR-CAPABILITY` | D-01, E-04, G-03 | 可分性 × 测量条件 × 消费者 | **高（三联，KC-000043 阻力最强处）** | 中（已降档） |
| `TASK-FAMILY-EXISTENCE-VERSUS-AVAILABILITY` | D-04, G-05 | 存在性 × 就位 × 时刻 × 消费者 | 低 | **低（最可能被推翻）** |
| `TASK-FAMILY-COMPLETION-PROCESS` | A-03, A-11 | 计数/展开 × 终止界 × 消费者 | 中 | 中 |
| `TASK-FAMILY-IDENTITY-OBSERVATION-LAYER` | B-01 | 对象对 × 观察层 × 判据 × 消费者 | 低 | 中 |
| `TASK-FAMILY-WITNESS-RECOVERABILITY` | E-02 | 见证 × 截断 × 工序 × 判定 | 低 | 中 |

**硬纪律**（修订片 003 §5）：AI 供给了任务族，GEN-001 验收的是**引擎的枚举/归约/核验
能力在新族上的贯通**，不是"引擎自主发现新研究方向"。这一区分在每条的 human_supply
字段中以"标注：AI 供给"显式写出，不得抹除。

## 4. 下一步（step-5）

对每个（合并或独立的）任务族执行 GEN-001 链：
冻结文法 → 引擎枚举 → grammar-preserving 归约 → 原生核校验 → run 收据 → CE-MAP 索引。
**若原生核不可用**，判词 `GENERATOR_LINK_BLOCKED_KERNEL_UNAVAILABLE`，
登记 kernel/环境缺口，**不降级为 Python/启发式校验**（F-011 硬约束）。

## 5. 自我限定

- **本注册不是候选成立的证明**：注册的是"把候选交给机器"的交接。
  任何"该前提非现实"的交付措辞仍需 GEN-001 链 + 原生核。
- **合并建议是建议**：合并与否由外部审计决定；AI 只提供共同分母的分析。
- **低置信度条目未被过滤**：D-04/G-05（置信度低）仍注册，
  因为"最可能被推翻"是外部审计的输入，不是 AI 自行淘汰的理由。
  若外部审计希望 AI 自行淘汰低置信度条目，需修订 009 §3 的字段语义。
- **corpus 高风险条目未被过滤**：D-01/E-04/G-03（语料流利度风险最高）
  仍注册，理由同上——风险被显式记账，不由 AI 隐式处置。
