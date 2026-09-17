# goal-1：用现实对齐找出 HoTT 的非现实前提，并验证它

> 本文件**只是索引和指向**，不是正文。执行时加载 SOP Skill
> `.codex/skills/hott-paradox-search-sop/SKILL.md`，按其执行循环走每一步；
> 每一步的反思与方案演化在 git log 中追踪。**冲突时以方案正文与 STATE 为准，本文件不是权威。**

## 方案正文

- 总索引：`Atria的方案/修订片.md`
- 核心修订片：
  - `修订片/003` — GEN-001 有界生成器验收单元（链贯通的验收标准）
  - `修订片/006` — S1–S6 供给策略 + SUPPLY_REGISTRATION 规程（新任务族从哪来）
  - `修订片/007` — 供给层加严（corpus_pressure / reality_anchor_holder）
  - `修订片/008` — PREMISE-001：A–G 分母、P1–P4 分工、必填字段
  - `修订片/009` — P3/P4 由 AI 执行 + 强制审计层 + 外部 AI 追溯审计
  - `修订片/010` — GEN-001 首链经验回写（CE-MAP 归属澄清 + 引擎能力事实 + 合并决策角色归属）
  - `修订片/014` — delay 片段 map 空间与现象饱和的强制披露纪律（O-5）
  - `修订片/015` — V2 片段设计与 delay→V2 门槛判定规程（G-a/G-b/G-c + 两阶段验收 + 忠实性警戒）
  - `修订片/016` — V2 阶段1 片段扩展验收完成与声明分母单一来源纪律
  - `修订片/017` — 全面自动化推进纪律（整条执行链自动化 + 关键判定可审计清单；
    外部 AI 追溯审计为终局复核，不再前瞻性邀请用户介入）
  - `修订片/018` — GEN-001-V2-1 首族链验收完成与两个已登记缺口（区间 I oracle 缺口 = 下一单元首选）
- 方案演化账本：`git log --grep=plan-revise`

## 执行 SOP

`.codex/skills/hott-paradox-search-sop/SKILL.md`（七段执行循环 + 反思清单 + git 纪律）

## 当前步骤（指针，权威是 STATE）

- STATE active 队首：`A-PREMISE-001`；revision 167；执行状态见 STATE 的 `execution_control`
- 第 1 步（已完成 `187033c`）：冻结 `PREMISE_DENOMINATOR_V1`（A–G 共 35 条，remainder=0）
- 第 2 步（已完成 `f21da7d`）：35/35 条逐条 P2
- 第 3 步（已完成 `92ee268`/`3a6aa9f`，修订片 009 角色重分工后由 AI 执行）：35/35 条 P3/P4，
  全部带完整 `P3P4_AUDIT_TRAIL`（steelman / falsifier / corpus_self_audit / depends_on），
  全部 `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`；非现实候选 9 条
  （A-03/A-11/B-01/D-01/D-04/E-02/E-04/G-03/G-05）
- 第 4 步（已完成 `03087c4`）：9 条非现实候选完成 SUPPLY_REGISTRATION（三道闸齐备）+
  5 个建议任务族冻结
- 第 5 步（GEN-001 链，进行中）：
  - **首链已完成**（`GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE`，revision 161 / `f62ec04`）：
    `TASK-FAMILY-WITNESS-RECOVERABILITY`（E-02）。9 atoms × 598 contexts，remainder=0；
    2,736 原始分离 → 52 规范归约见证；3 个越界见证经 Cubical Agda 原生核四路校验
    （verify / controls / negative-control 被拒 / verify-replay 精确匹配）。
  - **第二族已完成**（revision 162 / `9e23c9e`）：`TASK-FAMILY-COMPLETION-PROCESS`（A-03）。
    3 新声明 continuation 对 15 既有文法 map 唯一性 PASS；7 atoms × 460 contexts = 5,520 checks、
    remainder=0；46 个越界见证对 l1-v0/v1/v2 拒绝理由全部唯一 `BIND_CONTINUATION`；4 个见证
    （WV-053/0070/0021/0014，覆盖 3 构造子 × 2 机制）经原生核四路校验 + 主 repo 副本独立复现。
  - **第三族已完成**（revision 163 / `c36c2e4`）：`TASK-FAMILY-IDENTITY-OBSERVATION-LAYER`（B-01）。
    3 新声明 verdict continuation 对全部既有文法 map 唯一性 PASS；7 atoms × 440 contexts =
    5,280 checks、remainder=0；956→70 规范归约；44 越界见证对 5 个 delay 既有文法拒绝理由
    220/220 唯一 `BIND_CONTINUATION`；4 见证（WV-0014/0023/0044/0067，覆盖 3 构造子 × 3 机制）
    经原生核四路校验 + 主 repo 副本独立复现；现象新颖性 PARTIAL（层依赖现象一半旧文法已可表达）
    按修订片 012 披露交外部审计。
  - **第四族已完成**（GEN-001-4）：`TASK-FAMILY-DIVISIBILITY-CONDITION-OR-CAPABILITY`
    （D-01 / E-04 / G-03 continuity 三联）。3 新声明 verdict continuation 对 17 既有文法
    map 唯一性 PASS；7 atoms × 440 contexts = 5,280 checks、remainder=0；916→58 规范归约；
    32 越界见证对 6 个 delay 既有文法拒绝理由 192/192 全部唯一 `BIND_CONTINUATION`；
    4 见证（WV-0025/0026/0027/0051，覆盖 3 构造子 × 3 机制）经原生核四路校验 + 主 repo
    独立复现 exit 0。**同族坍缩判定：三成员共享同一机制 pattern**（delay 片段内无区间/
    截断塔/高阶迭代构造可区分），登记 `PATTERN_REDUCED_NOT_CERTIFIED_AS_FULL_TASK_EQUIVALENCE`，
    只报一个验收单元；现象新颖性 PARTIAL。详见 `GEN-001-DIVISIBILITY-REPORT.md`。
  - **第五族已完成（V1 最后一族，commit `389bea0`，revision 165）**：
    `TASK-FAMILY-EXISTENCE-VERSUS-AVAILABILITY`（D-04 / G-05，本批置信度最低一对）。
    3 新声明 verdict continuation 对 **19 个既有文法**（含 L1-DIVISIBILITY-v1）map 唯一性
    PASS 且互相 map-distinct；7 atoms × 440 contexts = 5,280 checks、remainder=0；
    916→58 规范归约（三机制全覆盖）；**32 越界见证 × 7 个 delay 既有文法 = 224/224
    拒绝理由全部唯一 `BIND_CONTINUATION`**；4 见证经原生核四路校验 + **主 repo 副本独立复现
    4/4 exit 0**。同族坍缩 Q4：两成员共享同一机制 pattern → `PATTERN_REDUCED`
    （多成员族坍缩率 2/2）；现象新颖性 PARTIAL；前提置信度最低一对显式披露，
    保持 `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`。
  - **step-6 五族 omission audit 已完成**（commit `f8eaa53` + 修订片 014，commit `310f7a9`）：
    **O-5 新发现**——delay 片段 continuation map 空间 49/18/31（剩余 29 个非 const map
    29/29 可产见证），但 `separation_kind` 3 值自第一族起 3/3 覆盖：**文法层未耗尽、
    现象层已饱和**。登记 `DELAY_FRAGMENT_PHENOMENON_SATURATED`；修订片 014 把它变成
    后续 delay 族的强制披露与事前门槛（再加 delay 族前必须先答 §2.3）。
  - **V1 的 5 个冻结任务族已用尽。** 下一单元 = **V2 片段（修订片 015）**：
    - 门槛规程 G-a（序/稠密）/ G-b（存在≠可用的双坐标）/ G-c（层级塔）；
    - `L2-cofibration` 片段最小设计：计算轴 + 面/层级结构轴 + 可用性态；
      `separation_kind` 获 `availability_observation / level_observation /
      density_observation` 三个新取值（现象新颖性的唯一出口）；
    - **阶段 1（片段扩展验收，已完成）**：Python ground 语义 + selftest 142/142 +
      Cubical Agda mirror 逐项一致（289 ground × 11 op-list = 3179 条 applyOps，
      原生核 KERNEL_ACCEPTED / refl 消解双等式）→ 判词
      `FRAGMENT_EXTENDED_WITH_SCOPE`（revision 166；引擎 `4428c48` + `9729d9f`；
      修订片 016 / commit `e36bdd4`）。工程验收，`registers_new_claim:false`，
      非数学结论，不进 CLAIM_EVIDENCE_MATRIX；新增 `DENOMINATOR_SINGLE_SOURCE` 纪律。
    - **阶段 2（`GEN-001-V2-1` 首族链，已完成，revision 167 / 修订片 018 `51247fd`）**：
      SUPPLY-009（S6+S3，D-04/G-05，命中 G-b），判词
      **`GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE`**。3,059 contexts × 1,104 等价对 =
      **3,377,136 checks、remainder=0**、order_independent；**212,864 → 51,904** 规范归约；
      **50,624/50,624** 作用域内见证被 7 个既有 delay 文法全拒且理由唯一（1,280 条纯
      race/deadline 见证登记为 `L1_SHARED_INGRESS`）；**4 见证 × 四路原生核收据**
      （WV-0001 availability / WV-23233 level×新 continuation / WV-0785 / WV-0786 density；
      verify exit 0 / 双正控制 / negative-control **exit 42** / verify-replay 精确匹配）；
      **51,904/51,904 归约见证输入对 `delayEquiv=true`（L1 输入层不可见）**；6 个分离
      种类全部出现（文法内现象层饱和）。强制披露：现象新颖性 **PARTIAL**（实质新颖性 =
      availability/level/density 三新观察层）；Q4 同族坍缩 **`PATTERN_REDUCED`**（D-04/G-05
      不可机械区分，只报一个验收单元）。引擎 `3a6ccd0`；主 repo 交付物 `38dcbc5`。
      **V2 专属强制披露已执行**：4 kernel 见证全部
      `POINT_SET_MIRROR_MODEL_KERNEL_CONFIRMED` / `interval_i_confirmed=false`。
  - 交付物：`HoTT/generators/GEN-001/`（V2-1 四件 + `GEN-001-INDEX.md`）；收据：
    引擎 `runs/SEARCH-GEN001-V2-1-001/` + `runs/VERIFY-GEN-001-V2-1-WV-*/`（分支
    `feat/machine-overview-m1`，commit `3a6ccd0`）
- **下一单元（AI 全自动，修订片 017；不由已完成的任何 checkpoint 授权，须另起单元）**：
  **缺口 A（区间 I oracle，首选）**——构造 DM3 或真实区间（min/max/neg）上的 V2 值解释，
  使结构性分离（availability / level / boolean payload）可由原生核在 De Morgan 代数上确认；
  这是把模型层分离升级为结论证据的**唯一**路径（修订片 015 §5 / F-011 / 018 §3A）。
  或 V2 第二族（G-a 稠密 / G-c 层级独立供给，优先级以「是否需点集专属律」为第一排序键——
  结构性 > 模型层，修订片 018 §4），或 SUPPLY-010 新任务族。
- 第 6 步：每个 bounded pass 后的 omission audit（信封外 unknown ingress）——五族后已完成
  （commit `f8eaa53`，裁决 revised → 修订片 014/015）：登记 `DELAY_FRAGMENT_PHENOMENON_SATURATED`
  （文法层 49/18/31 未耗尽但现象层 3 值饱和）、同族坍缩 2/2、五族 157 个越界见证 100%
  delay-equivalent（族间独立性未证，登记为信封外 ingress 而非结论）
- 权威来源：`.codex/research/hott/STATE.json` 的 `active` 与 `execution_control.next_minimal_verification`

## 认识论锚点（不可漂移）

`核心认知.md` generation-7：KC-000044（理论是现实的骨架式模仿，假想中的现实也是现实）、
KC-000045（数学与 HoTT 必然可映射现实；现实标准在对齐过程中被构造）、
KC-000046（AI 缺的是用现实理解理论的动作，不是思考现实的能力）。

## 边界

- 不预设 HoTT 不一致，也不预设一致。
- 非现实性判定（P3/P4）由 AI 执行并带强制审计层，外部 AI 追溯审计为终局复核；AI 不得把 pending-audit 候选判定自证为结论（修订片 009）。
- 未完成机器证明的内容不交付为数学结论。
- 未 push、未 tag。
- **两个已登记缺口（修订片 018 §3，随 GEN-001-V2-1 判词传播）**：(A) 区间 I 的 oracle
  不存在——mirror `Face = Point → Bool` 为点集模型，其 §10 DM3 三元链反模型自证对
  De Morgan 代数**可靠但不完备**，故全部 V2 见证**一律不得作为关于区间 I 的结论证据**；
  (B) 越界机械检查作用域 = 7 个 delay 文法，12 个 symbolic-horn 文法为 schema 级
  `BACKEND_MISMATCH` 未跑机械检查（作用域边界，非已证不相交）。
- V2 片段的点集 16 面模型**可靠但不完备**（验证布尔等式而区间 I 是 De Morgan 代数）：
  Python 模型只当枚举器，oracle verdict 必须由 Agda 真实区间 I 给出（修订片 015 §3.4）。
