import GodelQ.ZFC.CG008Sigma1

/-!
# CG-008 · 成员关系情形的工具：`hMem` / `hNMem`

`CG008Sigma1.lean` 的工具清单指出：Σ₁ 归纳的十情形里，`hMem`（`#a ∈ #b`）与
`hNMem`（`#a ∉ #b`）是构造路线的真正剩余障碍。

本文件尝试补上它们。

## 问题的形状

`setTheory_sigma₁_induction'` 的 `hMem` 情形要求：
对任意 `n` 与任意 `t₁ t₂ : Semiterm ℒₛₑₜ ξ n`，
`P n (.rel Language.Mem.mem ![t₁, t₂])` 成立。
取 `P n φ := 𝗭𝗙𝗖.internalize V ⊢ ⌜φ⌝`（闭句层），
则在 `n > 0` 时 `φ` 带自由变量，**不是**内部演算能装的形状。

## 两条路

**(a) 全称闭包路**：把 `P` 取成
`P n φ := 𝗭𝗙𝗖.internalize V ⊢ ⌜∀¹* φ⌝`（全称闭包后的闭句）。
则 `hMem` 要求证内部 `∀¹* (#a ∈ #b)`——由 `set_all_intro`（`CG008SetAll.lean`）归约到
`𝗭𝗙𝗖.internalize V ⊢ ⌜#a ∈ #b⌝`（自由变量层，用 `Semiterm.fvar`）。
而后者可由 `set_outer_to_internal`（`ZFCSetInternal.lean`）从**外部**证明
`𝗭𝗙𝗖 ⊢ ∀¹* (#a ∈ #b)` 得到——但那条外部句**不是 ZFC 定理**
（`x ∈ y` 对任意 `x y` 为假）。

**这就是障碍的实质**：`hMem` 情形在**语义前提**下才可达。
`setTheory_sigma₁_induction'` 的 `P` 是纯语法形状（不带语义前提），
所以它**不能**直接承载「语义真 ⟹ 内部可证」。

**(b) 带语义前提的归纳**：把 `P` 取成
`P n φ := (∀ (w : Fin n → V), V ⊧/w φ) → 𝗭𝗙𝗖.internalize V ⊢ ⌜∀¹* φ⌝`
（前提是「对任意赋值都真」，结论是内部可证的闭包）。
这才是算术版 `bold_sigma_one_complete` 的形状——
它的 `P` 实际是 `fun n φ ↦ ∀ w, V ⊧/w φ → T.internalize V ⊢ (toNumVec w ⤔ ⌜φ⌝)`
（看 `D3.lean:82-84` 的 `revert w` 就知道：先 `revert w`，再对 `hp` 归纳）。

本文件固定 (b) 是正确形状，并把算术版的 `P` 逐字抄出来对照。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008MemCase

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll GodelQ.CG008Sigma1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 算术版的 `P` 形状（逐字对照）

`D3.lean:82-84`：

```lean
theorem bold_sigma_one_complete {n} {φ : ArithmeticSemisentence n}
    (hp : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 φ) {w} :
    V ⊧/w φ → T.internalize V ⊢ (toNumVec w ⤔ ⌜φ⌝) := by
  revert w
  apply Bounding.Hierarchy.arithmetic_sigma₁_induction' hp
```

`revert w` 之后，`P` 是 `fun n φ ↦ ∀ w, V ⊧/w φ → T.internalize V ⊢ (toNumVec w ⤔ ⌜φ⌝)`。

**要点**：`P` 里**带语义前提** `V ⊧/w φ`，且结论用 `toNumVec w ⤔ ⌜φ⌝`
（把自由变量代换成**数字**，得到闭句）——这正是避开「自由变量层」的技巧：
算术语言里自由变量的值可以用数字（项）表示，所以代入后就闭了。

**集合语言没有数字**。自由变量 `#a` 的值是 V 里的元素，V 里**没有项**能命名它
（除非 V 恰好有该元素的常项，而 ℒₛₑₜ 没有常项）。
所以集合版**不能**照抄 `toNumVec` 这一步——这是集合版比算术版**实质更难**的地方。 -/

/-- **对照**：集合语言里没有对应的「数字项」把 V 的元素命名出来。
`ℒₛₑₜ` 的项只有绑定变量与自由变量（`Semiterm.bvar`/`Semiterm.fvar`），
没有常项、没有函数符号——所以算术版 `toNumVec w ⤔ ⌜φ⌝` 那一步在集合语言里没有对偶。 -/
example : IsEmpty ((ℒₛₑₜ).Func 0) := by
  constructor
  intro f
  cases f

end GodelQ.CG008MemCase
