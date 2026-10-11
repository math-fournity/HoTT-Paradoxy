import GodelQ.ZFC.ZFCSetInternal

/-!
# CG-008 · 把 D3 缺口化成内部演算形状（可执行的归约）

`Z0Blocked.lean:zfcTr_D3_internalize` 的两端都是 `Provable 𝗭𝗙𝗖 (⌜·⌝ : V)`——
「V 内部有一个编码为 V 元素的 𝗭𝗙𝗖 推导」。本文件用 Foundation 的通用
`tprovable_iff_provable`（`Typed.lean:168`，只要求 `[T.Δ₁]`，载体多态）
把两端**同时**化成内部演算形状：

```
Provable 𝗭𝗙𝗖 (⌜σ⌝ : V)   ⟺   𝗭𝗙𝗖.internalize V ⊢ ⌜σ⌝
```

这个归约的价值：化过去之后，`ZFCSetInternal.lean` 的 13 条集合语言内部演算引理
（`set_eq_refl`、`set_eq_symm`、`set_subst_eq`、`set_subst_mem`、`set_K_intro`、
`set_A_intro_left`、`set_exs_intro` 等）就成了可直接使用的工具，
而原形里的 `Provable`/见证 `d : V` 是被封装起来的、不可操作的。

**注意**：这是**归约**，不是 D3 的证明。归约后的目标仍然是
「V 内部从 `⌜translate τ⌝` 的推导造出 `⌜translate (zfcTr τ)⌝` 的推导」，
这需要 ZFC 的**内部化 Σ₁ 完全性**（见 CLAIM §9.3），尚未形式化。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Reduce

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **归约（前提一侧）**：V 内部的 `Provable` 等价于内部演算。

由 `tprovable_iff_provable`（`Typed.lean:168`）直接给出；它对 `𝗭𝗙𝗖` 可用
因为 `[𝗭𝗙𝗖.Δ₁]` 已由 `ZFCDelta1.lean` 证得，且该引理载体多态——
两端都是同一个 `V`，不经过 `: ℕ`。 -/
theorem provable_iff_internal {σ : SetTheorySentence} :
    Provable 𝗭𝗙𝗖 (⌜σ⌝ : V) ↔ 𝗭𝗙𝗖.internalize V ⊢ ⌜σ⌝ :=
  (tprovable_iff_provable (T := 𝗭𝗙𝗖) (V := V)).symm

/-- **归约（缺口整体）**：`zfcTr_D3_internalize` 等价于内部演算形状的命题。

这**不是**新证明，只是把同一条缺口搬到一个可操作的形状里：
左端是原形（`Provable`，见证被封在 `∃ d : V` 里，无法直接构造），
右端是内部演算（有 `ZFCSetInternal.lean` 的 13 条引理可用）。

两端的等价由 `provable_iff_internal` 在**同一个 `V`** 上做两次改写得到——
这正是避开载体墙的关键：不做 `: V` ↔ `: ℕ` 的重接。 -/
theorem zfcTr_D3_internalize_iff_internal :
    (∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (τ : ArithmeticSentence),
        Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V) →
        Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V))
      ↔
    (∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (τ : ArithmeticSentence),
        𝗭𝗙𝗖.internalize V ⊢ ⌜arithTrln.translate τ⌝ →
        𝗭𝗙𝗖.internalize V ⊢ ⌜arithTrln.translate (zfcTr τ)⌝) := by
  constructor
  · intro h V _ _ τ hτ
    exact (provable_iff_internal (V := V)).mp (h V τ ((provable_iff_internal (V := V)).mpr hτ))
  · intro h V _ _ τ hτ
    exact (provable_iff_internal (V := V)).mpr (h V τ ((provable_iff_internal (V := V)).mp hτ))

/-- **推论**：只要内部演算形状成立，`Z0Blocked.lean` 的 `zfcTr_D3_internalize` 立即成立，
从而 `Z0Full.zfc_z0_full_of_D3_internalize` 给出完整 Z0。 -/
theorem zfcTr_D3_internalize_of_internal
    (h : ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (τ : ArithmeticSentence),
        𝗭𝗙𝗖.internalize V ⊢ ⌜arithTrln.translate τ⌝ →
        𝗭𝗙𝗖.internalize V ⊢ ⌜arithTrln.translate (zfcTr τ)⌝) :
    ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (τ : ArithmeticSentence),
        Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V) →
        Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) :=
  zfcTr_D3_internalize_iff_internal.mpr h

/-- **完整形式的条件定理**：内部演算形状一旦成立，Z0 立即成立。 -/
theorem zfc_z0_full_of_internal
    (h : ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (τ : ArithmeticSentence),
        𝗭𝗙𝗖.internalize V ⊢ ⌜arithTrln.translate τ⌝ →
        𝗭𝗙𝗖.internalize V ⊢ ⌜arithTrln.translate (zfcTr τ)⌝) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  zfc_z0_full_of_D3_internalize (zfcTr_D3_internalize_of_internal h)

end GodelQ.CG008Reduce

#print axioms GodelQ.CG008Reduce.provable_iff_internal
#print axioms GodelQ.CG008Reduce.zfcTr_D3_internalize_iff_internal
#print axioms GodelQ.CG008Reduce.zfcTr_D3_internalize_of_internal
#print axioms GodelQ.CG008Reduce.zfc_z0_full_of_internal
