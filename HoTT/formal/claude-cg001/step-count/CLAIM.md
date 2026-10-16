# 数步数：一步是路径时，去而复返与不动分不开

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。起因：用户要求按建议顺序主动推进；“伪交换”种子的文献核查中，在同伦补丁理论期刊版 §3.2 读到作者明写“数补丁个数的函数不可定义”。候选卡与讨论见 `.claude/思考与发现/CN-023 - 数步数：一步是路径时，去而复返与不动分不开.md`。
> proof id：`MP-CG001-STEP-COUNT-001`（主包）、`MP-CG001-STEP-COUNT-NEG-001`（负控制）；claims：`CG001-C-39`–`CG001-C-41`。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设，不加公理；零警告。
> 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §9（GOAL_LOCAL_INDEX_ONLY）；总入口 `.claude/总索引.md`。

## 这个包为什么存在

把一步（或一次编辑）写成路径，撤销就是把路倒着走。这样恒等、复合、撤销以及它们的全部规律都白送。代价是“做了又撤销”（`p ∙ sym p`）与“什么都没做”（`refl`）成了同一条路径。于是“一共走了几步、改了几次”这件现实中最简单的事，在理论里没有办法回答：
- 任何以路径为输入的函数，都把去而复返看成不动（C-39）；
- 任何类型族沿路径运输的“随身计数器”，也数不出去而复返的两步（C-39 的 `noCarriedPedometer`）——这一点与 A1 不同：A1 有依赖族出路（C-25），这里没有；
- 可加的计数只能是净位移，也就是圈数（C-40）；
- 把旅程当作数据（步子的列表）时，步数与净位移都能算；实现成路径以后，净位移保留，步数丢失（C-41）。

同伦补丁理论的作者在期刊版 §3.2 写到了同一件事：数补丁里有几个基本补丁的函数不可定义，因为一个补丁接着它的逆等于恒等补丁。本包在本项目工具链中原生证明其一般形式与两个实例。

数学内容都是标准事实（群胚律加函数尊重路径），**不主张原创**。

## 命题全文

记号：`ΩS¹ = base ≡ base`；`winding`、`winding-hom` 取自 `Cubical.HITs.S1.Base`；`rCancel`、`lCancel`、`rUnit` 取自 `Cubical.Foundations.GroupoidLaws`；ℕ 的 `_+_` 按第一个参数递归。

| claim | 命题（量词与假设照实写） | 源码符号 |
|---|---|---|
| **CG001-C-39**（去而复返对一切读数不可见） | 对任意类型 `A`、`x y : A`、`p : x ≡ y`：对任意 `P` 与 `c : x ≡ x → P`，`c (p ∙ sym p) ≡ c refl`；对任意 `c : y ≡ y → P`，`c (sym p ∙ p) ≡ c refl`；对任意类型族 `B` 与 `b : B x`，`subst B (p ∙ sym p) b ≡ b`；`¬ (Σ[ c ∈ (x ≡ x → ℕ) ] (c refl ≡ 0) × (c (p ∙ sym p) ≡ 2))`；对任意 `B`，`¬ (Σ[ r ∈ (B x → ℕ) ] Σ[ b ∈ B x ] r (subst B (p ∙ sym p) b) ≡ suc (suc (r b)))`。 | `roundTripInvisible`、`undoRedoInvisible`、`roundTripTransportTrivial`、`noPedometer`、`noCarriedPedometer` |
| **CG001-C-40**（圆上的可加计数只能是净位移） | `¬ (Σ[ c ∈ (ΩS¹ → ℕ) ] ((p q : ΩS¹) → c (p ∙ q) ≡ c p + c q) × (c loop ≡ 1))`；`winding (loop ∙ sym loop) ≡ pos 0`（由 `refl`）。 | `noAdditiveStepCounter`、`netRoundTrip` |
| **CG001-C-41**（作为数据的旅程有步数，实现成路径后只剩净位移） | `Step = {fwd, back}`，`Journey = List Step`，`steps = length`，`realize [] = refl`、`realize (s ∷ j) = stepLoop s ∙ realize j`（`fwd ↦ loop`、`back ↦ sym loop`），`net` 按 `fwd ↦ +1`、`back ↦ −1` 求和。则：对一切 `j`，`winding (realize j) ≡ net j`；`steps (fwd ∷ back ∷ []) ≡ 2` 与 `steps [] ≡ 0`（由 `refl`）；`net (fwd ∷ back ∷ []) ≡ net []`（由 `refl`）；`realize (fwd ∷ back ∷ []) ≡ realize []`；`¬ (Σ[ c ∈ (ΩS¹ → ℕ) ] ((j : Journey) → c (realize j) ≡ steps j))`。负控制：以 `refl` 断言两段旅程（作为数据）的步数相等，内核拒绝（`2 != 0 of type ℕ`）。 | `Step`、`Journey`、`steps`、`stepLoop`、`realize`、`stepNet`、`net`、`windingStep`、`realizeKeepsNet`、`thereAndBack`、`stepsDiffer`、`netAgrees`、`realizedAgree`、`stepCountLost`；负控制 `WrongStepCount.agda` |

## 来源定位（转述，不是引文）

Angiuli、Morehouse、Licata、Harper，*Homotopical patch theory*，Journal of Functional Programming 26（2016），DOI `10.1017/S0956796816000198`。本轮经 sciverse 全文库读取（MinerU 解析的期刊版正文），未入库。页码按期刊版页眉。

| 本包 | 对应的原文陈述 | 位置 |
|---|---|---|
| C-39、C-40 | 并非所有看似合理的解释都是函子性的：数一个复合补丁里基本补丁个数的函数，会给“补丁接着它的逆”2、给恒等补丁 0，而二者相等，所以这个函数不可定义；作者预告函子性会使补丁历史的定义变复杂 | §3.2 末段，p.11 |
| C-39 | 逆补丁是两侧逆：先做后撤等于不变，先撤后做也等于不变 | §3.1 末段，p.10 |
| C-41 | 模型化为群胚迫使一切补丁有完全的逆；补丁通常有“事后撤销”，却没有“事前撤销”（不能在文件创建之前删除它）；补救办法是在 HoTT 内使用范畴库（HoTT Book 第 9 章），或使用有向同伦类型论 | §10 讨论以群胚建模之劣势的几段，p.41 |
| 两层（与 C-33 同） | 命题相等的项可以有不同的计算，而 HoTT 内部没有任何谓词能区分它们 | §10 末段，p.41–42 |

扩展版（2014）对照：§3.1 第 3 段（要求逆而不只是收缩）；§8（对称路径是限制；未能表述伪交换）。期刊版的结论已改写，未再出现“未能表述伪交换”一句（本轮在期刊版全文中检索未见；不等于作者后来表述了它）。

## 禁止外推

- 不说 HoTT 不能表示“步数”或“日志”：C-41 就在 HoTT 里用列表表示了它们。它说的是：一旦把一步写成路径，步数就不再是这一步的函数，也不能由任何类型族沿路径携带。
- 不说补丁理论失败：作者知道这一点，并用历史索引与限制合并来处理。
- C-40 只涉及圆上的环路与取值于 ℕ 的可加计数；C-39 对一切类型成立。
- 负控制只说明作为数据的两段旅程步数不同（内核分得开）；它不是理论内部关于路径的定理。
- “步”“撤销”“计步器”“补丁”是解释标签；不说任何物理或版本控制系统的事实。
