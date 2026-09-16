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
- 方案演化账本：`git log --grep=plan-revise`

## 执行 SOP

`.codex/skills/hott-paradox-search-sop/SKILL.md`（七段执行循环 + 反思清单 + git 纪律）

## 当前步骤（指针，权威是 STATE）

- STATE active 队首：`A-PREMISE-001`；revision 156；执行状态 `PREMISE_001_P2_COMPLETE_AWAITING_USER_P3P4`
- 第 1 步（已完成，commit `187033c`）：冻结 `PREMISE_DENOMINATOR_V1`（A–G 共 35 条；反思补入 A+B/0/1/2/W 后由 `plan-revise(008)` bc0a899 扩到 35 条；分母分片 sha256 `5cd1b44f`，remainder=0；每条含 P1 前提陈述 + 出处锚到 Theory Schema）
- 第 2 步（已完成，commit `f21da7d`）：35/35 条逐条 P2，输出到 `PREMISE-001/002`（A 11 + B 4）与 `PREMISE-001/003`（C 4 + D 5 + E 4 + F 2 + G 5）；每条含 `reality_skeleton`（非空、未默认只填计算域：D-01 转动域、D-04 制造工装域、E-04 量仪精度域、G-03 运动域）、`divergence_point`、`evidence_level`、≥1 `OMISSION_SHAPE`、`corpus_pressure`；reflection=no-plan-change（三点澄清已登记）
- 第 3 步（当前，停机点）：整单交用户 P3/P4 判定。`divergence_point` 是唯一可判定对象；AI 不得自证非现实性（SOP 判词 `USER_ADJUDICATION_REQUIRED`）。建议优先看 `PREMISE-G-03`（高阶相等无限迭代，运动域，与圆环悖论同形）。用户判为非现实者才进 SUPPLY_REGISTRATION + GEN-001 链
- 权威来源：`.codex/research/hott/STATE.json` 的 `active` 与 `execution_control.next_minimal_verification`

## 认识论锚点（不可漂移）

`核心认知.md` generation-7：KC-000044（理论是现实的骨架式模仿，假想中的现实也是现实）、
KC-000045（数学与 HoTT 必然可映射现实；现实标准在对齐过程中被构造）、
KC-000046（AI 缺的是用现实理解理论的动作，不是思考现实的能力）。

## 边界

- 不预设 HoTT 不一致，也不预设一致。
- 非现实性判定（P3/P4）永远由用户作出，AI 不得自证。
- 未完成机器证明的内容不交付为数学结论。
- 未 push、未 tag。
