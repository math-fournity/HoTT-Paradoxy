# A1 自查控制：依赖族出路、残留的状态认同、作为数据的时间

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 6fd0312a。起因：外部审计（GPT-5.6 Terra）对 CG001-C-01–C-24 的审查，以及用户要求“首先检查你自己的工作到底是否存在它指出的问题”。
> proof id：`MP-CG001-FAMILY-CONTROL-001`（主包）、`MP-CG001-FAMILY-CONTROL-NEG-001`（负控制）；claims：`CG001-C-25`–`CG001-C-27`。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设，不加公理。
> 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §7（GOAL_LOCAL_INDEX_ONLY）；总入口 `.claude/总索引.md`；逐条自查见 `.claude/思考与发现/CN-020 - Terra 审计的逐条自查与回应.md`。

## 这个包为什么存在

它把审计里指向 Claude 的两点做成机器可查的让步，并把让步之后剩下的东西单独写出来：

1. **依赖族出路是合法的，并且能完成有限读数任务。** 审计指出：C-06 已经展示了用类型族保存变化，“变化是预先写进模型的”不构成反驳，因为物理的温度场同样要作为模型结构给出。这一点与 Claude 自己在 CN-016 中的论证（“终点读数由场决定，对应决定论”）一致。C-25 证明：在实现后的四位置环上，一个按 +1、+1、−1、−1 粘合的类型族带有一个截面，它在四个具名位置的原始读数正是高度 0,1,2,1。所以 C-19、C-20 的“价格”只针对非依赖的集合值读数。
2. **让步之后仍然剩下的**：在这个族的总空间里，走一步之前的状态 (r0, 0) 与之后的状态 (r1, 1) 被认同，整体状态的任何观察量在两处相等（C-26）。变化只以按位置读出的原始数据存活，不是状态的改变。
3. **C-24 的单调性是假设，不是由方向推出的。** C-27 证明：时间作为数据时，信号 0,1,0 存在，只是它不顺 (ℕ, ≤) 的箭头。

数学内容都是标准事实，**不主张原创**。

## 命题全文

| claim | 命题（量词与假设照实写） | 源码符号 |
|---|---|---|
| **CG001-C-25**（依赖族完成有限读数任务） | 对 HIT `Ring`（点 `r0`–`r3`，路径 `e0 : r0 ≡ r1`、`e1`、`e2`、`e3 : r3 ≡ r0`）与类型族 `Gauge`（四点处为 `ℤ`；沿 `e0`、`e1` 为 `sucPathℤ`，沿 `e2`、`e3` 为 `predPathℤ :≡ ua (predℤ , …)`）：存在截面 `heights : (x : Ring) → Gauge x`，满足 `heights r0 ≡ pos 0`、`heights r1 ≡ pos 1`、`heights r2 ≡ pos 2`、`heights r3 ≡ pos 1`（均由 `refl`）；`¬ (heights r0 ≡ heights r1)`。负控制：在一步粘合为 `sucPathℤ` 的族上，把终点原始读数声明为 `pos 5` 被内核拒绝（`1 != 5`）。 | `Ring`、`predPathℤ`、`Gauge`、`heights`、`rawProfile`、`rawReadingsDiffer`；负控制 `WrongGaugeSection.agda` |
| **CG001-C-26**（残留：状态被认同） | `Path (Σ Ring Gauge) (r0 , pos 0) (r1 , pos 1)`；对任意 `P` 与 `g : Σ Ring Gauge → P`，`g (r0 , pos 0) ≡ g (r1 , pos 1)`。 | `stepIdentifiesStates`、`stateObservablesFrozen` |
| **CG001-C-27**（作为数据的时间） | 对 `signal : ℕ → ℕ`（0 ↦ 0，1 ↦ 1，其余 ↦ 0）：`signal 0 ≡ 0`、`signal 1 ≡ 1`、`signal 2 ≡ 0`；`¬ (∀ m n → m ≤ n → signal m ≤ signal n)`；`¬ (1 ≤ 0)`。 | `signal`、`signalUpThenDown`、`signalRespectsNoOrder`、`one≰zero` |

## 禁止外推

- C-25 只在具名的有限位置上给出原始读数；区间内部的读数落在 Glue 类型里，不在固定的 ℤ 中。按用户的量子化现实观，状态是有限个可命名的，因此有限读数任务可以完成；本包不断言连续轨迹上任意时刻的读数都可以这样取得。
- C-26 不说“HoTT 不能表示变化”：原始读数确实不同（C-25）。它说的是：在把运动读作恒等的表示里，变化不是整体状态的改变。这是否构成用户意义上的非现实性，取决于现实任务是否要求“状态改变”，属于用户的裁定（见 CN-020）。
- C-27 不说有向类型论能或不能表达先升后降；它只说，这样的信号在“时间作为数据”时存在，并且不顺序的箭头。
