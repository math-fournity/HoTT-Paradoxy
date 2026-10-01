# 教科书消解做成对照：同一个追问，对集合截断第 1 问就停，代价是截断把“相同”宣布成事实（C-83）

> HUMAN_EDITED；2026-09-30；Claude，本机 Claude Code 会话 `eadb3381`（macOS）。
>
> 起因：CN-050 第 2 节的对照表里，“教科书消解：对集合截断 ∥X∥₀ 发问，第 1 问就停”一行只是按定义说的，没有单独跑内核；第 7 节建议补一个机器检查。用户【原话】“做。”
>
> - proof id：
>   - 主包：`MP-CG001-TRUNCATION-QUESTIONING-001`（`TruncationQuestioning.agda`）；
>   - 负控制：`MP-CG001-TRUNCATION-QUESTIONING-NEG-001`、`-NEG-002`（下文“负控制”一节）。
> - claim：`CG001-C-83`（Cubical Agda）。
> - 工具链：Agda 2.8.0 + cubical 0.9，本机 macOS 记录 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；`--safe --cubical --guardedness`，不用任何公设。
> - 依赖（全部导入，不重抄）：
>   - `../pedometer-semantics/PedometerSemantics.agda`（C-55：`Delay`、`never`、`runFor`）；
>   - `../pedometer-semantics/DelayMonad.agda`（C-59，经 C-77 间接导入）；
>   - `../universe-questioning/UniverseHasNoLevel.agda`（C-75，经 C-77、C-81 间接导入）；
>   - `../questioning-delay/QuestioningDelay.agda`（C-77、C-78：`Judge`、`Questioning`、`question`、`judgesAreEqual`、`universeQuestioningIsNever`）；
>   - `../product-questioning/ProductQuestioning.agda`（C-81：`Prod`、`productQuestioningIsNever`）。
> - 标签：`FORMAL_TRUNCATION_CONTROL_STOPS_AT_STAGE_ONE_WITH_COST`。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §22（GOAL_LOCAL_INDEX_ONLY）。

## 任务

- **追问程序不变**：沿用 C-77 的 `question C judge`，从第 1 问开始；计数约定同 C-77（从第 1 问开始时，“第 k 问停”就是燃料 k−1 时返回 k）。
- **被追问的对象换成集合截断**：C-78 追问宇宙 `Type ℓ-zero`，C-81 追问乘积 `Prod`，两者都永不停。教科书式的回应是：去问它们的集合截断 `∥ X ∥₂`，那里“相同”在第 1 问就落定。本包把这个回应做成内核对照，并同时陈述它的代价。
- **完成标准**：程序返回 `now k`。运行语义沿用 C-55、C-59。

## 命题全文

### C-83（`TruncationQuestioning.agda`）

- **(a) 集合截断第 1 问就停**：`truncStopsAtOne : (X : Type ℓ) (judge : Judge ∥ X ∥₂) → runFor 0 (question ∥ X ∥₂ judge) ≡ just 1`。对任意类型、任意判定器都如此，与 ℕ、Bool 相同（C-79）。
- **(b) 宇宙**（`TU = ∥ Type ℓ-zero ∥₂`）：
  - `TUNotProp : ¬ isProp TU`：`Unit` 与空类型所在的分支不同（把分支读成“有没有居民”这一命题，经 `isSetHProp`）；
  - 判定器存在：`judgeTU`，第 0 问答“否”，从第 1 问起答“是”；且唯一：`everyJudgeIsJudgeTU : (judge : Judge TU) → judge ≡ judgeTU`；
  - `truncUniverseStopsAtOne : (judge : Judge TU) → runFor 0 (question TU judge) ≡ just 1`；
  - 内核实跑：`truncUniverseKernel : runFor 0 (question TU judgeTU) ≡ just 1`（`refl`）；
  - 并列：`universeSideBySide : (judge : Judge (Type ℓ-zero)) (tjudge : Judge TU) → (question (Type ℓ-zero) judge ≡ never) × (runFor 0 (question TU tjudge) ≡ just 1)`。
- **(c) 乘积**：`productSideBySide : (judge : Judge Prod) (tjudge : Judge ∥ Prod ∥₂) → (question Prod judge ≡ never) × (runFor 0 (question ∥ Prod ∥₂ tjudge) ≡ just 1)`。本包不构造 `∥ Prod ∥₂` 的判定器：第 0 问要判定 `∥ Prod ∥₂` 是不是命题，这牵涉可数选择；本条对判定器是全称的。
- **(d) 截断的代价**：
  - `notEqActs : transport notEq true ≡ false`（`refl`）与 `notEqNotRefl : ¬ notEq ≡ refl`：宇宙里 Bool 与自己相同的两种方式（`notEq` 与 `refl`）不同；
  - `truncCollapses : cong ∣_∣₂ notEq ≡ refl`：截断之后二者相等，由构造子 `squash₂`（任意两条平行路径相等）直接给出；
  - `noDecoding : ¬ (Σ[ g ∈ (TU → Type ℓ-zero) ] ((A : Type ℓ-zero) → g ∣ A ∣₂ ≡ A))`：没有函数能把截断解码回宇宙；否则宇宙是集合的收缩，因而是集合（`isOfHLevelRetract 2`），与 `notEqNotRefl` 矛盾。

## 负控制

| proof id | 文件 | 断言 | 预期 |
|---|---|---|---|
| `MP-CG001-TRUNCATION-QUESTIONING-NEG-001` | `WrongTruncSilent.agda` | 截断宇宙的追问用 `judgeTU`、燃料 0 仍沉默（`refl`） | 被拒：内核实跑，第 1 问答“是”，得 `just 1 != nothing` |
| `MP-CG001-TRUNCATION-QUESTIONING-NEG-002` | `WrongNotEqTrivial.agda` | 截断之前，沿 `notEq` 搬运 `true` 仍得 `true`（`refl`） | 被拒：内核把搬运算成 `false`，得 `false != true` |

## 这件事改变了什么（解释，非机器证明）

- 【判断】**教科书消解是成立的，而且是在内核里成立的**：对截断发问，第 1 问就停（(a)–(c)）。这不能拿来否认 C-78、C-81，它说的是另一个对象。
- 【判断】**它成立的方式，是把“相同”宣布成事实**：截断的构造子 `squash₂` 规定任意两条平行路径相等；于是宇宙里 Bool 与自己相同的两种方式，在截断里成了一种（(d)）。而且这一步回不去：没有函数能把截断解码回宇宙（`noDecoding`）。换句话说，问题变简单，是因为被问的对象已经不是宇宙本身。
- 【解释】这与 CN-050 第 2 节的对位一致：极限用一条定义把“走到了”宣布回来，截断用一个构造子把“相同是事实”宣布回来；两者都不恢复被改掉的现实条件本身（离散的空间、事实式的相同），也都是理论内部的正当构造。这是解释，不是定理。
- 【解释】与 CN-035、CN-037 的观察“每一种修复都加回事实式的相同”同形；按 CN-038，“凭构造宣布完成”是 B 向读法所在。

## 元层还剩什么

- 与 C-77、C-78、C-81 相同：把内部定理读成“现实中照这个程序去跑”的陈述，需要所用理论一致；对任意闭判定器，还需要典范性。本包对 `judgeTU` 的停机由内核实跑检查（(b) 的 `refl`）。

## 禁止外推

- 不证明 HoTT 不一致，也不证明截断“错了”。截断是 HoTT 的正当构造；本包只陈述它让追问停下的方式与代价。
- 不证明“对截断发问与对宇宙发问是同一个任务”，也不证明它们不是；任务忠实性由研究发起人裁定（CN-049 第 4 节第 1 问、CN-050）。
- (c) 不构造 `∥ Prod ∥₂` 的判定器；该判定器第 0 问涉及可数选择，本包对此不作断言。
- 用到高阶归纳类型（集合截断、命题截断；经 C-81 另有 Eilenberg–MacLane 空间）与单价性（`notEq` 由对合构造，经 C-75 的环路计算）。
- `≡ never` 只经有限燃料的运行来读（C-59 (c)）；不是墙钟时间、真实设备或证明助手运行时间的陈述。
- 数学内容标准：集合截断是集合、截断不能解码回非集合，都是 HoTT 的常识（HoTT Book §6.9、§7.3），**不主张原创**。本仓库新增的是：把它放在追问程序旁边，作为 C-78、C-81 的“教科书消解”对照。
- 运行只在本机 macOS 上捕获与重放，没有在第二个平台重放。

## 运行

- 主包：`HoTT/verification/runs/20260930-CG001-TRUNCATION-QUESTIONING-01`。
- 负控制：`20260930-CG001-TRUNCATION-QUESTIONING-NEG-01`、`-NEG-02`（与上表 NEG-001、NEG-002 依次对应）。
- 捕获工具：`.claude/goals/CG-001-targeted-overview/tools/capture_cg001_agda_macos_run.py`；核对：`verify_cg001_run.py --rerun`。
