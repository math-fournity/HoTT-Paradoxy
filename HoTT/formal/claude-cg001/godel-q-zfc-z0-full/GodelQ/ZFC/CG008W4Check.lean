import GodelQ.ZFC.CG008RightHalf

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008W4Check

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.ZFCSetInternal GodelQ.CG008RightHalf

/-! # W4 的「查存量」——**结论：没有隐藏难点**

## W4 问的是什么

「从 `V └§ t₁ = t₂` 造一条 ZFC 推导」是否已有存量。

## 查到的（算术侧的样板，`EquationalTheory.lean`）

```lean
variable (T : ArithmeticTheory) [Theory.Δ₁ T] [EQ _ └┤ T]

@[simp] lemma eq_refl (t : Term V ℒₒᵣ) : T.internalize V ⊢ t ≐ t
@[simp] lemma eq_symm (t u : Term V ℒₒᵣ) : T.internalize V ⊢ (t ≐ u) ─┤ (u ≐ t)
@[simp] lemma eq_uniform_trans (t₁ t₂ t₃ : Term V ℒₒᵣ) :
    T.internalize V ⊢ (t₁ ≐ t₂) ─┤ (t₂ ≐ t₃) ─┤ (t₁ ≐ t₃)
```

## 关键观察：**这一族引理不用 numerals**

三条引理的证明套路**完全一致**：

1. `complete.{0} T _ fun M _ _ ↦ by simp [models_iff]`——元层证 `T ⊢ “╬║ x, x = x”`；
2. `internal_provable_of_outer_provable` 搬进 V；
3. `TProof.specialize!/specialize₂!/specialize₃!` 代入 **Term V ℒₒᵣ**（闭项）。

**第 1 步是纯语义（`simp`），第 3 步是纯语法代入——全程没有 `toNumVec`，没有 `numeral`。**

## 对 W4 的判定

**W4 不需要新数学。** 集合侧的对应物（`set_eq_refl`/`set_eq_symm`/`set_eq_trans`）
**本包 `ZFCSetInternal.lean:90/99/138` 已经证了**，用的正是这三步。

**所以右半没有隐藏难点**——它的真实工作量全在 W2（`term_complete` 对偶的逐支展开），
而 W2 的唯一新零件是 `toOmegaVec`，定义一行。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件只记查实，**不含未证标记**。 -/

/-- 查实：本包的 `set_eq_refl` 存在（`ZFCSetInternal.lean:90`），证明套路正是三步。 -/
noncomputable example (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (t : Term V ℒₛₑₜ) :
    𝗭𝗙𝗖.internalize V ⊢ setEq t t := set_eq_refl t

/-- 查实：`set_eq_symm` 也在（`:99`）。 -/
noncomputable example (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (t u : Term V ℒₛₑₜ) :
    𝗭𝗙𝗖.internalize V ⊢ setEq t u 🡒 setEq u t := set_eq_symm t u

end GodelQ.CG008W4Check
