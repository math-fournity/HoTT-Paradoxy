# 补丁理论的附录：上下文空间可缩、编辑前后的整体状态被认同、理论内相等而运行可分

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。起因：Terra 复审 003 的 O-007（HPT 证据范围）、O-008（A1′ 的同一任务合同）、O-009（C-26 与可观察性）。回应正文：`Terra对Opus的审计/Opus给GPT的回应/004 - Opus 对 Terra 003 的回复：CG-001.md`；思考笔记：`.claude/思考与发现/CN-022 - Terra 复审 003 的自查与对辩：补丁理论的附录与有向读数.md`。
> proof id：`MP-CG001-PATCH-CONTRACTIBLE-001`（主包）、`MP-CG001-PATCH-CONTRACTIBLE-NEG-001`（负控制，C-32）、`MP-CG001-PATCH-CONTRACTIBLE-NEG-002`（负控制，C-33）；claims：`CG001-C-30`–`CG001-C-33`。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设，不加公理；零警告。
> 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §8（GOAL_LOCAL_INDEX_ONLY）；总入口 `.claude/总索引.md`。

## 这个包为什么存在

上一轮（C-28、C-29）只重建了《同伦补丁理论》正文第 6 节报告的两处困难。本轮通读其扩展版全文，发现附录 A（作者注明是正式发表版因篇幅删去的部分）把事情说得更彻底：作者自己证明，行数上下文（A.2）和历史索引上下文（A.3、A.5）的上下文空间都是**可缩的**，从空上下文出发的路径完全由终点的历史决定，“路径不提供额外信息”；他们正是用这一点得到合并律。另外，正文 5.3 节说：由路径连接的两个元素，在理论内部不能被区分，运行时却可以。

本包在本项目工具链中原生重建这些陈述的数学核心，用来回答 Terra 的三个问题：
1. 作者的“历史索引”修复并没有把状态从认同中解放出来，而是让整个上下文空间可缩，状态的区别只留在索引数据里（C-30–C-32）；
2. C-26 那类“整体状态被认同”，说的是理论内部的全部非依赖观察，而不是任意一层观察；区分只在理论之外的两层出现：认同之前的索引数据，以及运行（定义性计算）（C-32、C-33 及两个负控制）；
3. 补丁理论 2014 年缺少的操作语义，今天的 Cubical Agda 已能提供：第 4 节的解释器真的能算（C-33）。

数学内容都是标准事实，**不主张原创**；本包不是对原论文的复现，只重建其中几条陈述的核心。

## 命题全文

记号：`singl a = Σ[ x ∈ A ] (a ≡ x)`（cubical 0.9 Prelude）；`ΩS¹ = base ≡ base`；`winding`、`intLoop`、`decodeEncode` 取自 `Cubical.HITs.S1.Base`。

| claim | 命题（量词与假设照实写） | 源码符号 |
|---|---|---|
| **CG001-C-30**（行数上下文可缩） | 对 HIT `LineCtx`（`doc : ℕ → LineCtx`；`add : (n : ℕ) → doc n ≡ doc (suc n)`，与 C-28、C-29 的 `R` 同一个 HIT）：`isContr LineCtx`，中心 `doc 0`；对任意 `F : LineCtx → Type ℓ` 与 `n : ℕ`，`F (doc 0) ≡ F (doc n)`。C-28、C-29 由此可得。 | `LineCtx`、`lineToPath`、`lineContraction`、`isContrLineCtx`、`allFibresEqual` |
| **CG001-C-31**（历史索引上下文可缩） | 对 HIT `HistCtx`（`hdoc : List Bool → HistCtx`；`hadd : (b : Bool) (h : List Bool) → hdoc h ≡ hdoc (b ∷ h)`）：`isContr HistCtx`，中心 `hdoc []`；`(Σ[ h ∈ List Bool ] hdoc [] ≡ hdoc h) ≃ List Bool`；对任意 `x y` 与 `p q : x ≡ y`，`p ≡ q`。 | `HistCtx`、`histToPath`、`histContraction`、`isContrHistCtx`、`logEquiv`、`parallelPatchesEqual` |
| **CG001-C-32**（单点模型：编辑前后的整体状态被认同） | `Model (hdoc h) = singl h`，`Model (hadd b h i) = ua (isContr→Equiv (isContrSingl h) (isContrSingl (b ∷ h))) i`；`State = Σ HistCtx Model`。则 `isContr State`；记 `before = (hdoc [] , ([] , refl))`、`after = (hdoc (true ∷ []) , (true ∷ [] , refl))`：`before ≡ after`；对任意 `P` 与 `g : State → P`，`g before ≡ g after`；`¬ (Σ[ d ∈ (HistCtx → Bool) ] ¬ (d (hdoc []) ≡ d (hdoc (true ∷ []))))`；`¬ ([] ≡ true ∷ [])`；`readAt [] (snd before) ≡ []` 与 `readAt (true ∷ []) (snd after) ≡ true ∷ []`（均由 `refl`）。负控制 NEG-001：以 `refl` 证明 `Path HistCtx (hdoc []) (hdoc (true ∷ []))`，内核拒绝（`[] != true ∷ []`）。 | `Model`、`isContrModel`、`State`、`isContrState`、`before`、`after`、`editIdentifiesStates`、`observablesAgree`、`noChangeDetector`、`historiesDiffer`、`readAt`、`readBefore`、`readAfter`；负控制 `WrongStateRefl.agda` |
| **CG001-C-33**（两层：理论内相等，运行可分） | `optimizeKeep p = (p , refl)`、`optimizeNormal p = (intLoop (winding p) , sym (decodeEncode base p))`，类型都是 `(p : ΩS¹) → singl p`。则 `optimizeKeep ≡ optimizeNormal`；`fst (optimizeNormal (loop ∙ sym loop)) ≡ refl` 由 `refl`（定义性计算）成立；`winding (loop ∙ loop) ≡ pos 2` 由 `refl` 成立。负控制 NEG-002：以 `refl` 证明 `Path (base ≡ base) (loop ∙ sym loop) refl`，内核拒绝（`hcomp (doubleComp-faces (λ _ → base) (sym loop) i) (loop i) != base`）。 | `optimizeKeep`、`optimizeNormal`、`optimizersEqual`、`normalRemovesDetour`、`interpreterRuns`；负控制 `WrongDetourRefl.agda` |

## 来源定位（转述，不是引文）

来源：Angiuli、Morehouse、Licata、Harper，*Homotopical Patch Theory (Expanded Version)*，[作者主页 PDF](https://carloangiuli.com/papers/hpt-expanded.pdf)，18 页，pdfTeX 2014-07-30，本地核对副本 SHA-256 `1de2daa4ad25075c88b8b957362b6014b23e767e21b15341593cae233fc5eeb2`（副本在会话临时目录，未入库）。页码指该 PDF 的物理页。

| 本包 | 对应的原文陈述 | 位置 |
|---|---|---|
| C-30 | 开区间 I*（`doc : Nat → I*`、`add1 : doc n = doc n+1`）可缩，拓扑上是半直线；从 `doc 0` 到 `doc n` 的路径唯一，终点上下文决定发生过的补丁序列 | 附录 A.2，p.15 |
| C-28、C-29（上一轮） | 按行数分类的上下文容纳不了“n 行文件的类型”这一自然解释；若所有上下文可从空仓库到达，所有上下文都只能解释为可缩类型 | §6 第 2、3 段，p.10 |
| C-31 | 以布尔列表为历史的上下文 HIT 可缩；从 `doc []` 出发的路径与历史一一对应（`log`）；合并律由可缩性得到（所有方块交换） | 附录 A.3，p.15–16；A.5（第 6 节完整版本的可缩性，作者称有机器检查的证明），p.17 |
| C-32 | 每个上下文解释为它的历史所决定的那个文件的单点类型 `S(replay h)` | §6 第 4 段与 §6.2，p.10–11 |
| C-33 | 映到可缩类型的函数在理论内部彼此相等，运行时仍可作出理论内部被遮蔽的区分；优化器例子；与函数外延性的经验相比 | §5.3 “Singleton Types and Computation” 段，p.10 |
| C-33 | 第 4 节的仓库是单个整数，补丁理论“就是圆”；解释器用万有覆叠，算的是圈数 | §4、§4.1，p.5–6 |
| C-33 | 作者当时没有可以运行这些程序的形式操作语义，只能推测程序如何运行 | §1 倒数第 2 段，p.2 |

## 禁止外推

- 不说补丁理论失败或不一致：可缩性正是作者用来得到合并律的性质（A.3、A.5）。
- C-31、C-32 用布尔列表作历史（对应附录 A.3 的二叉树版本），不重建第 6 节带 ADD、RM 与交换律的完整 `History` HIT；作者对该完整版本的可缩性另有机器检查证明（A.5 脚注），本包未复现。
- C-32 取“内容 = 历史本身”（replay 为恒等），对应 A.3；第 6.2 节 replay 为一般函数时，总空间同样由单点类型组成，本包未形式化该一般形态。
- “状态”“编辑”“认同”“运行”是解释标签。C-32 的形式内容只是：总空间可缩，任何非依赖观察在两点相等，上下文上没有区分前后的布尔测试，历史本身不同，内容可以从具名上下文上的纤维读出。它**不说**现实仓库没有变化，也**不说**运行时不能区分（C-33 正好说明运行可以区分）。
- C-33 的“运行”指 Cubical Agda 内核的定义性计算（归一化），不是任何版本控制系统的执行。两个负控制只说明相关两项不是定义性相等；“不是定义性相等”是内核的元层判断，不是理论内部的定理（理论内部无法陈述它，也正因如此才叫“被遮蔽”）。
- 不说任何版本控制系统的事实。
