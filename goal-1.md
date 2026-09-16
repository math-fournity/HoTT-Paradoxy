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
- 方案演化账本：`git log --grep=plan-revise`

## 执行 SOP

`.codex/skills/hott-paradox-search-sop/SKILL.md`（七段执行循环 + 反思清单 + git 纪律）

## 当前步骤（指针，权威是 STATE）

- STATE active 队首：`A-PREMISE-001`；revision 163；执行状态见 STATE 的 `execution_control`
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
  - **待续**：EXISTENCE-VS-AVAILABILITY（D-04/G-05，置信度最低）；
    状态见 `HoTT/generators/GEN-001/GEN-001-INDEX.md`
  - 交付物：`HoTT/generators/GEN-001/`；收据：`HoTT/verification/runs/20260916-VERIFY-GEN001-*`
- 第 6 步：每个 bounded pass 后的 omission audit（信封外 unknown ingress）；已登记首个输入：
  A-03 族与 E-02 首链族在 delay 片段共享 race-截断分离机制（ingress，非结论）
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
