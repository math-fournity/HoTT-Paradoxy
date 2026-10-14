-- CG-009: **ExsBridge2 反例搜索**（001-Step 派活，分水岭定音）
--
-- 要证伪/证成：`ExsBridge2` 对含 fvar 的 t 是否为假。
--   ExsBridge2 := ∀ {p t}, IsUFormula ℒₒᵣ p → IsTerm ℒₒᵣ t →
--       Provable 𝗭𝗙𝗖 (imp ℒₛₑₜ (iT 0 (substs1 ℒₒᵣ t p)) (^∃ (domZero ^⋏ iT 1 p)))
--
-- LK 全称化：`Provable (imp A B)` ≡ `⊢ ∀x (A → B)`。
-- 故需找 `x ∉ ω` 使 `A(x)` 真、`B` 假（B 不含 x）。
--
-- **记录在案的失败候选**（别重跑）：
--   `t = ^&0`、`p = ⌜#0 = #0⌝`：004-Step 机核验——两边都真，**不构成反例**。
--
-- 本文件尝试一个新候选：让 B 假。B = ∃z∈ω, (iT 1 p)(z)。
-- 取 p 使 `iT 1 p` 在 ω 上恒假 ⟹ B 假。同时要让 `iT 0 (subst ?[t] p)` 在某个 x 上真。
import GodelQ.ZFC.ExsBridge2

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ExsCounterHunt

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 事实层（已经机器固化的，可直接引）

1. `IsTerm ℒₒᵣ ^&x` 成立（`IsSemiterm.fvar` 无条件）。
2. `iVE 0 ^&x = eqAtom ^&x`（`iVE_fvar`）——A 侧含 `^&x`。
3. `domZero = subst ℒₛₑₜ ?[^#0] cDomN`（`InternalTranslate.lean:215`），
   即"bvar 0 ∈ ω"；B 侧的 ∃ 绑定的是**新**变量，不含 `^&x`。
-/

example (x : V) : IsTerm ℒₒᵣ (^&x : V) := IsSemiterm.fvar 0 x
example (x : V) : iVE (0 : V) (^&x : V) = eqAtom (^&x : V) := iVE_fvar 0 x

/-! ## 候选：p 使 B 假

B = `∃z (z ∈ω ∧ (iT 1 p) z)`。要使 B 恒假，需 `iT 1 p` 在 ω 上恒假。

最直接的想法：`p = ^nrel 2 cLess ?[^#0, #1]`（"#0 ≥ 1"）——在 ω 上恒假？
不对：ω 里有 1,2,3,... 都 ≥ 1。
要"恒假"需要在 ω 上无满足者——比如 `#0 = #1 ∧ #0 = #2 ∧ #0 ≠ #1` 型矛盾。
**最简单**：`p = ^nrel 2 cEq ?[^#0, ^#0]`（"#0 ≠ #0"）——自相矛盾，恒假！

则：
* B = `∃z∈ω, z ≠ z` → 恒假 ✔
* A = `iT 0 (subst ?[^&x] (#0 ≠ #0))` → 也恒假（同一个矛盾，只是 bvar 0 换成 ^&x）
  ⟹ A 也假，**不构成反例**（要 A 真 B 假）。

**症结**：`substs1 t p` 只换 p 的 bvar 0，p 的"恒假性"被保留下来——
**如果 p 恒假，A 和 B 一起假**。这就是为什么 `p = ⊤` 那条（004-Step 做的）
是唯一容易的情形：⊤ 恒真，两边一起真。

**结论（结构性）**：A 与 B 的差别**只在** bvar 0 被换成 t 值、
以及外层那个 ∃z∈ω 上。**B 比 A 多要求"见证在 ω 里"**。
所以反例必须是：**存在 x ∉ ω，使 `(iT 1 p)` 在 x 处成立**。
即：`p` 在 ω 外有一个满足点、在 ω 内没有。

这恰好是"**非标准模型里 ω 不初等**"的一个实例——可以说
`ExsBridge2` 的一般形状 ⟺ "iT 1 p 的满足集若含 ω 外元素则也含 ω 内元素"，
即 p 的翻译在 ω 上的**下推封闭性**。**这不是平凡的。**
-/

end GodelQ.ExsCounterHunt
