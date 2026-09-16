<!-- governance-shard:v2
logical_id: ATRIA-MACHINE-OVERVIEW-PLAN-REVISION
shard_id: 010
index: ../修订片.md
-->

# GEN-001 首链执行的经验回写（CE-MAP 归属与引擎能力事实）

> 修订对象：本方案 003 片 §4 action 7（CE-MAP 索引行）+ 003 片 §3（有界新组合的可实现性）+
> 007 分片 SUPPLY 表的"合并与否由外部审计决定"条款。
> 依据：GEN-001 首链（2026-09-16）的实际执行收据（`HoTT/generators/GEN-001/`）。
> 修订性质：**执行层澄清 + 能力事实登记**，不改变 003 片的验收判据，不产生数学结论。

## 1. 触发来源

`source=reflection`（GEN-001 step-5 的 S-4 反思，第 6/7 条：漂移累积与被后续修正推翻）。
执行 003 片 action 7 时发现它与引擎自身的证据政策及 F-011 直接冲突，必须回写否则后续单元会重复踩点。

## 2. CE-MAP 归属的澄清（003 片 action 7）

**原条款**：GEN-001 产出"在 CE-MAP 建立索引行（claim ID / proof ID / 源码 / run receipt /
证据等级 / 禁止外推）"。

**冲突**：机器统观引擎的 `registry.json.evidence_policy` 明文规定"Exploration and calibration
receipts stay under machine-overview/runs/ and never enter HoTT/CLAIM_EVIDENCE_MATRIX.md by
themselves"；F-011 / `MATH_PROOF_BEFORE_DELIVERY_V1` 同样规定只有源码 + 原生核 run + 冻结矩阵行
齐备的**精确数学命题**才能进入 CE-MAP。GEN-001 验收的是**链的贯通**，其 `claim_relation` 为
`exploration_candidate_not_registered / registers_new_claim: false`。

**修订（执行层）**：GEN-001 单元的索引化改由 `HoTT/generators/GEN-001/GEN-001-INDEX.md` 承担，
显式标注"能力验收 / 非数学结论 / 不进入 CLAIM_EVIDENCE_MATRIX.md"。`CLAIM_EVIDENCE_MATRIX.md`
的进入门槛不变。**003 片 action 7 的意图（索引化、可追溯、禁止外推）被完整保留**，
只是索引落点改变。

若某一天 GEN-001 链产出的候选被升级为真正的数学命题（需 F-011 全部门禁），
届时才在 CE-MAP 建行，并使用 `MP-GEN-001-*` 前缀。

## 3. 引擎能力事实（对 003 片 §3"有界新组合"的补充）

首链实测登记如下，供后续四个任务族排期使用（observed，非推断）：

| 事实 | 内容 | 对后续族的影响 |
|---|---|---|
| L1 片段（delay/race/bind/deadline）支持**任意新声明延续 map**，无需改引擎代码 | 新延续在 `render_target` / `render_proof` 中按一般 ground term 渲染，原生核接受 | COMPLETION-PROCESS、WITNESS-RECOVERABILITY 型族**成本低** |
| symbolic-horn 后端的 renderer 集合是**封闭的 12 项**（`SYMBOLIC_NATIVE_RENDERERS`） | 新 symbolic 族需改 `case.py` + `verify.py` 并写新 Agda target 才能进原生核 | DIVISIBILITY（区间/连续）型族若要走 symbolic 路线，**成本高**；可先尝试 L1 建模对应 |
| 越界证明可机械化的层级是**声明构造子集合** | `within_grammar_witness` 对旧文法返回 `BIND_CONTINUATION` 即证明越界 | 后续族必须显式声明"新构造子"，否则越界不可证 |
| 归约比 | 首链 2,736 原始分离 → 52 规范见证（约 52:1） | 预算估算参考：每族送核点不宜超过个位数 |
| 中断恢复 | verify 进程被外部杀死后，引擎 roll-over 并在重跑时把同 run-id 的 target_freeze 记为 `REUSED`，而校验器在 `first_verify_run == run_id` 时期望 `FROZEN` | **已知缝隙**：处置=用新 run-id 重跑同见证 + 原收据不修改地归档披露；不得手改 RUN.json |

## 4. SUPPLY 合并决策的角色归属（007 分片）

007 分片写"合并与否由外部审计决定"。用户 2026-09-16 裁定（修订片 009 的同一裁定）：
P3/P4 及其下游执行由 AI 全权负责，外部 AI 追溯审计。**因此合并决策也归于 AI 执行 +
强制审计层**，与 009 的角色重分工一致。

**首链的实际决策与理由（AI 执行，pending external audit）**：
不合并，先单独跑 `TASK-FAMILY-WITNESS-RECOVERABILITY`。理由：
(1) corpus 风险低、置信度中——007 表自评如此，适合作为首链；
(2) 它在引擎 L1 片段上有最自然的建模对应，无需改引擎代码（§3）；
(3) DIVISIBILITY 三联（D-01/E-04/G-03）是 corpus 风险最高处，已显式记账为"外部审计优先复核"，
    留待 V1 审计意见后再跑，可以避免在高风险条目上先投入机器预算；
(4) EXISTENCE-VS-AVAILABILITY（D-04/G-05）置信度最低、最易被推翻，同样留待审计。

**该决策的可推翻性**：外部审计若认为应先跑高风险族以尽早暴露问题，本决策立即回滚，
按 `depends_on` 链（007 分片）重排。该决策**不是**"AI 淘汰了低置信度条目"——
D-04/G-05 与 D-01/E-04/G-03 仍在队列内，只是排在后面。

## 5. 不改变的条款

- 003 片 §4 的九字段任务规格、§5 的三角色分工、§6 的完成判词与禁止外推——全部不变。
- 003 片 §3 的"有界，不是无界"安全设计——不变（首链 remainder=0 且无截断，安全性质成立）。
- 006–009 片的供给策略、语料压力字段、P3/P4 角色重分工——不变。
- 本修订**不产生数学结论**（F-011）。

## 6. 本修订的自我限定

- §3 的能力事实基于**一台机器、一个引擎版本（coordinator 0.5.0 工作树态）**的实测；
  引擎版本变化后须重测，不得外推到其他版本。
- §4 的排序决策是**优先级判断**，不是"该族无候选"的结论。
- 首链的建模对应（E-02 → Delay Bool）是**有界对应物**，不是 HoTT 命题截断本身
  （见 `GEN-001-REPORT.md` §4）。外部审计若否决该对应，链贯通结论不变，但任何
  "E-02 已被机器检验"的推论必须撤回。
