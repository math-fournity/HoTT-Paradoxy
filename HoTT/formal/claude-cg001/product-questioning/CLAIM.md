# 不是宇宙的类型上，同一个追问也不停：HoTT Book 例 8.8.6 的邻近对照（C-81、C-82）

> HUMAN_EDITED；2026-09-30；Claude，本机 Claude Code 会话 `eadb3381`（macOS）。
>
> 起因：CN-048 第 3、4 节建议做 HoTT Book 例 8.8.6 的邻近对照，并问“要我现在开始做例 8.8.6 的对照吗？”；用户【原话】“开始”。对齐检查（《最高指示-Claude版》§6 五项）与过程记录：`.claude/explore/20260930-例8.8.6邻近对照-工作台.md`。
>
> - proof id：
>   - 主包：`MP-CG001-PRODUCT-QUESTIONING-001`（`ProductQuestioning.agda`）；
>   - 负控制：`MP-CG001-PRODUCT-QUESTIONING-NEG-001` 至 `-NEG-004`（下文“负控制”一节）。
> - claim：`CG001-C-81`、`CG001-C-82`（Cubical Agda）。
> - 工具链：Agda 2.8.0 + cubical 0.9，本机 macOS 记录 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；`--safe --cubical --guardedness`，不用任何公设。
> - 依赖（全部导入，不重抄）：
>   - `../pedometer-semantics/PedometerSemantics.agda`（C-55：`Delay`、`never`、`runFor`）；
>   - `../pedometer-semantics/DelayMonad.agda`（C-59，经 C-77 间接导入）；
>   - `../universe-questioning/UniverseHasNoLevel.agda`（C-75：`K`、`ΩⁿK`、`sec`、`trivSec`、`Πpt`、`Ω^Πpt`、`hLevelΩ^`）；
>   - `../questioning-delay/QuestioningDelay.agda`（C-77：`Judge`、`Questioning`、`question`、`judgesAreEqual`、`whetherSettled`、`levelUp`）。
> - 来源：HoTT Book §8.8 例 8.8.6（2013 版，经 sciverse 全文核对，书页 292）。
> - 标签：`FORMAL_QUESTIONING_NEVER_HALTS_ON_A_NON_UNIVERSE_PRODUCT_WITH_BOUNDED_CONTROL`。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §21（GOAL_LOCAL_INDEX_ONLY）。

## 任务

- **追问程序 Q 不变**：沿用 C-77 的 `question C judge`。第 k 问问“C 的相同在第 k+1 层落定了吗？”（`isOfHLevel (k+1) C`），判定器每一问交出“是”或“否”的证明；得“是”即停并交出 k，得“否”即走一步问下一问；从第 1 问开始。计数约定同 C-77：从第 1 问开始时，“第 k 问停”就是燃料 k−1 时返回 k。
- **换掉被追问的对象**：C-78 追问的是宇宙 `Type ℓ-zero`。本包追问一个普通的小类型
  - `Prod = (n : ℕ) → K n`，其中 `K n = EM ℤ (1+n)`（C-75 包的 Eilenberg–MacLane 空间）。
  这是 HoTT Book 例 8.8.6 的构造：一族类型，第 n 个在 n 维（这里是 1+n 维）有不平凡的环，取它们的乘积。
- **对照**：同一个乘积、同一种成员，只把成员高度设上限：
  - `Bounded b = (n : ℕ) → K b`（每个分量都是同一个 `K b`）。
- **完成标准**：程序返回 `now k`，即交出落定的一层。运行语义沿用 C-55、C-59。

## 命题全文

### C-81：成员高度无上限的乘积（`ProductQuestioning.agda`）

- **(a) 基点上的环不平凡**：`secAtBase≢triv : (n : ℕ) → ¬ (sec n (x₀ n) ≡ trivSec n (x₀ n))`，其中 `x₀ n = 0ₖ (suc n)` 是 `K n` 的基点。C-75 的 `secNontrivial` 陈述的是整条截面；它的证明只在基点取值，本命题把同一论证写成基点上的形式，这正是例 8.8.6 需要的“在一点处不平凡的环”。
- **(b) 乘积没有任何有限层**：`productHasNoLevel : (m : ℕ) → ¬ isOfHLevel m Prod`。证明按例 8.8.6：
  - 乘积的 (1+m) 维环路空间等于各分量 (1+m) 维环路空间的乘积（`Ω^Πpt`）；
  - 取元素 `bump m`：第 m 个分量放 `sec m (x₀ m)`，其余分量放平凡环（`discreteℕ` 判别分量号）；
  - 若乘积在 h-层 2+m 落定，这个环路空间可缩（`hLevelΩ^`），于是 `bump m` 平凡，取第 m 个分量得 `sec m (x₀ m)` 平凡，与 (a) 矛盾（`productNot2+`）。
- **(c) 追问永不停**（对任意判定器）：
  - `productQuestioningIsNever : (judge : Judge Prod) → question Prod judge ≡ never`；
  - `productQuestioningRunsNothing : (judge : Judge Prod) (n : ℕ) → runFor n (question Prod judge) ≡ nothing`；
  - `productQuestioningNeverAnswers : (judge : Judge Prod) → ¬ Questioning.Halts Prod judge`；
  - 判定器存在：`judgeProd k = no (productHasNoLevel (suc k))`；且唯一：`everyJudgeIsJudgeProd : (judge : Judge Prod) → judge ≡ judgeProd`；
  - 内核实跑：`productKernelRuns1000 : runFor 1000 (question Prod judgeProd) ≡ nothing`（`refl`）。
- **(d) 对照另一个问题**：`productWhetherAnswersNo : (d : Dec (Σ[ m ∈ ℕ ] isOfHLevel m Prod)) → runFor 0 (whetherSettled Prod d) ≡ just false`。问“有没有一层落定？”的程序一步不走就答“没有”，对该问题的任何判定方式都如此。

### C-82：同一个乘积，成员高度有上限（`ProductQuestioning.agda`）

- **(a) 恰好高一层**：对每个 b，
  - `boundedLevel : (b : ℕ) → isOfHLevel (3 + b) (Bounded b)`（`isOfHLevelΠ` 加 `hLevelEM`）；
  - `boundedNot2+ : (b : ℕ) → ¬ isOfHLevel (2 + b) (Bounded b)`（常值元素“每个分量都放 `sec b (x₀ b)`”，取第 0 个分量）。
- **(b) 恰好第 2+b 问停**（对任意判定器）：
  - `boundedStopsAt : (b : ℕ) (judge : Judge (Bounded b)) → runFor (suc b) (question (Bounded b) judge) ≡ just (suc (suc b))`；
  - `boundedSilentBefore : (b : ℕ) (judge : Judge (Bounded b)) (i : ℕ) → i < suc b → runFor i (question (Bounded b) judge) ≡ nothing`；
  - 判定器存在：`judgeBounded : (b : ℕ) → Judge (Bounded b)`；
  - 实例 b = 0：`boundedZeroStopsAtTwo`：`(n : ℕ) → K 0` 的追问燃料 0 沉默、燃料 1 返回 2，即第 2 问停。

## 负控制

| proof id | 文件 | 断言 | 预期 |
|---|---|---|---|
| `MP-CG001-PRODUCT-QUESTIONING-NEG-001` | `WrongProductAnswersEarly.agda` | 乘积的追问用 `judgeProd`、燃料 1 就返回 1（`refl`） | 被拒：内核实跑，得 `nothing != just 1` |
| `MP-CG001-PRODUCT-QUESTIONING-NEG-002` | `WrongProductNeverByRefl.agda` | 乘积的追问等于 `never`，用 `refl` 证 | 被拒：`askFrom Prod judgeProd 1 != never`。计算本身看不出程序不停，C-81 (c) 必须用 C-77 的余归纳证明 |
| `MP-CG001-PRODUCT-QUESTIONING-NEG-003` | `WrongBoundedSilent.agda` | 有界乘积 `Bounded 0` 用 `judgeBounded 0`、燃料 1 仍沉默（`refl`） | 被拒：内核算出第 1 问答“否”、第 2 问答“是”，得 `just 2 != nothing` |
| `MP-CG001-PRODUCT-QUESTIONING-NEG-004` | `WrongBoundedStopsEarly.agda` | 有界乘积 `Bounded 0` 第 1 问就停（燃料 0 返回 1，`refl`） | 被拒：`nothing != just 1`（它不是集合） |

## 这件事改变了什么（解释，非机器证明）

- 【判断】**追问停不下来，不需要被追问的对象是宇宙。** C-78 的对象是宇宙；C-81 的对象是一个普通的小类型 `Prod : Type ℓ-zero`，同一个程序同样等于 `never`。两者证明路线不同：C-78 经局部—整体环路原理（单价性）把成员的环抬到宇宙上；C-81 直接用“乘积的环路空间是环路空间的乘积”。
- 【判断】**同一个乘积，成员高度设上限就停，而且停在上限决定的那一问。** C-82 与 C-81 只差一件事：分量是同一个 `K b`，还是维数随 n 增长的 `K n`。前者恰好第 2+b 问停，后者永不停。在本包的范围内，让追问停不下来的是“成员高度没有上限”；Π 的“一次交出整体”本身不导致不停（C-82 也是一次交出的乘积）。
- 【判断】**对罗素线主张的影响**（CN-048 第 3 节的预测，现有机器证据支持）：
  - “追问永不停”不是宇宙独有的现象；
  - 宇宙在罗素线上的特殊之处要另说：它是理论不能拒绝的论域元素（KC-000050），单价性是关于它的陈述；而本包的乘积是可以不去构造的。本包的构造还用到类型族 `K : ℕ → Type ℓ-zero`，宇宙在这里是把“无界高度”装进一个对象的工具。
- 【判断】**对归因讨论的影响**（CN-047 补注）：在 B 方向的读法下，“一次交出一个相同永远落不定的整体”的不只是宇宙的形成规则，Π 的形成同样交出了 `Prod`。能区分的证据现在多了一行：
  - 保留高阶归纳类型与单价性，把被追问的对象从宇宙换成乘积：永不停（C-81）；
  - 同一个乘积，成员高度设上限：第 2+b 问停（C-82）；
  - 旧有的两行：相同换成事实（Lean）第 1 问停（C-80）；保留单价性、目录成员高度以 1+n 为上限，第 1+n 问停（C-79）。
  哪一条前提是非现实的抽象，仍由研究发起人按其现实观裁定（CN-047 第 4 节的问法）；本包只提供区分证据，不代替裁定。
- 【解释】与用户原意的关系：KC-000018 说罗素的 S“无法构建出来——无法停机，所以S不存在”。若把这条规则用到 HoTT，本包表明它碰到的不只是宇宙，也包括一切一次交出的、成员高度没有上限的整体。这是否合研究发起人的原意，由研究发起人判断。

## 元层还剩什么

- 与 C-77、C-78 相同：把内部定理读成“现实中照这个程序去跑，永远拿不到答案”，需要所用理论一致；对任意闭判定器，还需要典范性。立方类型论（含高阶归纳类型）有立方集合模型【来源转述：Cohen–Coquand–Huber–Mörtberg 2018；Coquand–Huber–Mörtberg 2018】；Agda 全部特性合在一起的一致性，本包不作断言。
- 对本包的判定器 `judgeProd`，照程序执行不停是语法事实：每一问都答“否”，内核实跑检查了 1000 步（C-81 (c)）。需要一致性的，是“这些‘否’都对”。

## 禁止外推

- 不证明 HoTT 不一致，也不证明“`Prod` 不存在”。本包证明的是：追问 `Prod` 落定于哪一层的程序等于 `never`。
- 解释桥（“存在性追问 = 这个过程”）与现实侧前提（“存在要求落定”）待研究发起人裁定，也交社区判断；本包不改变它们的身份。
- 用到高阶归纳类型（Eilenberg–MacLane 空间）与单价性（经 C-75 的环路计算）。不用高阶归纳类型时的情形，本包没有构造。
- 本包的构造用到类型族 `K : ℕ → Type ℓ-zero`。本包**不**证明“没有宇宙就造不出没有有限层的类型”，也不证明任何关于“没有宇宙的类型论”的命题。
- 判定器立即作答；不停机来自问的层数没有顶，不来自某一问难答。
- `≡ never` 只经有限燃料的运行来读（C-59 (c)）；不是墙钟时间、真实设备或证明助手运行时间的陈述。
- 数学内容标准：乘积没有有限层是 HoTT Book 例 8.8.6（成员取 `K n` 而非 Sⁿ），**不主张原创**。本仓库新增的是：在它上面跑 C-77 的追问程序，并给出同一构造、成员高度有上限的对照（C-82），把它作为 C-78 的邻近对照。
- 运行只在本机 macOS 上捕获与重放，没有在第二个平台重放。

## 运行

- 主包：`HoTT/verification/runs/20260930-CG001-PRODUCT-QUESTIONING-01`。
- 负控制：`20260930-CG001-PRODUCT-QUESTIONING-NEG-01` 至 `-NEG-04`（与上表 NEG-001 至 NEG-004 依次对应）。
- 捕获工具：`.claude/goals/CG-001-targeted-overview/tools/capture_cg001_agda_macos_run.py`（由云端会话的 Linux 版派生，差异写在文件头）；核对：`verify_cg001_run.py --rerun`。
