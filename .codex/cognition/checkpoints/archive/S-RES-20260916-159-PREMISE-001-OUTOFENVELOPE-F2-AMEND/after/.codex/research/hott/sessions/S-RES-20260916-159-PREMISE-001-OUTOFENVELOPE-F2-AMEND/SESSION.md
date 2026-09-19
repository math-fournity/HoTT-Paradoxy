# S-RES-20260916-159-PREMISE-001-OUTOFENVELOPE-F2-AMEND

- 工作单元：`/goal 按照Skill完成goal-1.md` 驱动。**停机点不变**（`AWAITING_USER_P3P4`，revision 158 已登记）。本单元只做一件事：把上一单元（S-RES-20260916-158）登记的 **F2 ingress 补全到可行动**——初版 F2 只据 `CORE_RULES.md:101` 一个非承诺行，说"univalence 入、resizing 未入"；第二次查证发现这个登记**被低估**。
- 方法：把分母 35 条的 **P1 出处范围**（§1.1–1.13、§2.1–2.2、§2.9–2.10、§3.1、§3.3、§3.6、§6.9、§A.2、第 6 章）与仓库来源快照 `HoTT/theory-schema/SOURCES_AND_COVERAGE.md` 的 section 清单逐项对照。该快照已 21/21 本地来源 SHA 比对（:242），是独立于分母构建视角的第二来源。
- 发现（commit `19a1efb`）：缺口的形状不是"一个公理未入"，而是**整层"逻辑原则/可选公理"来源在手、分母零条**：
  - §3.2 `Propositions as types?`（PAT 原则本身，`logic.tex:159`）——属设计决策层，但 G-01..G-05 未含；
  - §3.4 `Classical vs. intuitionistic logic`（LEM，`logic.tex:353`）；
  - §3.5 `Subsets and propositional resizing`（`logic.tex:451`）——这是初版 F2 唯一指出的那一条；
  - §3.8 `The axiom of choice`（`logic.tex:701`）；
  - §3.9 `The principle of unique choice`（`logic.tex:801`）；
  - §3.10 `When are propositions truncated?`（`logic.tex:852`）——E-02/E-03 只登记截断**构造**，未登记"何时该截断"的判据；
  - §11.2 Dedekind cut 与 Ω 选择（`reals.tex`）。
  - `SOURCES_AND_COVERAGE.md:200` 自述"logic.tex §3.4–3.5、§3.7–3.8：LEM、resizing、截断与 AC"已定点展开——即来源在仓库内、可立即引用，却未被枚举进分母。
- 修正后的归类：**仍不是缺陷**。univalence 是 HoTT 的定义性公理，上述是可选/经典原则层，V1 把它整层置于范围外是合理范围选择。但作为 **V2 取舍项**它比初版大，V2 需决定四项：(i) LEM/AC/unique choice 是否作为"可选前提"单列类别（它们在现实对齐下的省略形状与 A–G 不同——是**显式假设的额外能力**，不是被压平的现实条件）；(ii) §3.2 PAT 是否补进 G 类；(iii) §3.10 截断时机判据是否补进 E 类；(iv) §11.2 实数完备性/Ω 选择是否单立。
- 角色纪律：**本次只登记不判定**（判定权在用户，且属 V2 范围）；不改 V1 分母、不改 004 判定表、不做 P3/P4 判定。
- S-4 反思：①分母一致——V1 未动；②策略锚定——这是已完成 ingress 的补全，不是新审计（pass 的遗漏审计要求在 158 已满足，用了一个独立来源）；③角色越界——无；④负结论误用——F2 是"范围边界"不是"该族无候选"；⑤信封外候选——补全的是已登记项，未新增；⑥无被推翻；⑦漂移累积——无。裁决 `no-plan-change`。
- S-6 收尾：goal 驱动自动续跑，无新用户文本消息需归档；逐 KC 回评见本目录 `CORE_COGNITION_AUDIT.md`（generation-7 全量 46 条）。
- S-7 推进：STATE revision 158→159（本 checkpoint 事务）；**停机点不变**；投影 marker 刷到 159；FRONTIER 的 V2 ingress 槽位更新为"可选公理/逻辑原则整层"。
- 数学状态：不变。无数学命题交付（`MATH_PROOF_BEFORE_DELIVERY_V1` 不适用）。
- Git：审计修正 `19a1efb`（带 reflection）；本 checkpoint 事务单独提交；不 push、不 tag。
