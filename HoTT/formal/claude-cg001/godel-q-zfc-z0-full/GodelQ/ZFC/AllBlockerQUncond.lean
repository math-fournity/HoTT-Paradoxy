import GodelQ.ZFC.HAllUncond
import GodelQ.ZFC.ShCraigElimSetupQ
set_option linter.unusedVariables false

/-!
# CG-007 · W8：**`hAll` 的无条件收据**（两条独立路线）

本文件把 `hAll` 的阻塞义务 `AllBlockerQ` 从「假设」升级为「定理」，
并给出**两条独立路线**（数学内容不同，可互证）。

## 路线 B（重言式，主收据）

`HABElim.hAB_derivable` 证的是命题重言式 `A → (C → A)`
（`A = free (iT 1 p)`、`C = subst ?[^&0] domZero`），**不是语法等式桥**。

```lean
HAllUncond.hAll : (hs) (hp) (hd) (ih) → Q (allIntro s p d)
```

## 路线 A（等式桥，附收据）

`bridgeB` 是 `iT_subst_open`（∀m 的一般律）在 `m = 0` 的实例：

```lean
bridgeB q hq : subst ?[^&0] (iT 1 q) = iT 0 (subst ?[^&0] q)
```

配本文件原有的 `allKey_of_bridge` / `allBlockerQ_of_key` 即得 `AllBlockerQ`。

## `len_qVec` 的语义保真（机器证明）

两版 `len_qVec`（Foundation `Bootstrapping` 与 `TranslateShiftCompat`）在相同前提下
**定义相等**——见 `len_qVec_rfl_equiv`（证法 `cases h.lh; rfl`）。
移植时 `ITSubstOpen4` 的 7 处裸名引用已加 `Bootstrapping.` 前缀消歧。

## 核验

* 全链 **70 模块从源码编译，`skipped=0`**（exit 0）
* 三条定理的 `#print axioms` 均为 `[propext, Classical.choice, Quot.sound]`，**无 `sorryAx`**

`ShCraigElim ⟺ (AllBlockerQ ∧ ExsBlockerQ ∧ RootBlockerQ)`，
**现 AllBlockerQ ✅**（本文件），另两条仍为义务。 -/


open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open GodelQ.ShCraigElimSetupQ GodelQ.TranslateShiftCompat GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.ZFCZ0

namespace GodelQ.AllBlockerQUncond

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`len_qVec` 两版定义相等**（语义保真，`rfl` 级机器证明）。

Foundation 的 `Bootstrapping.len_qVec (h : IsUTermVec L k w) : len (qVec L w) = k + 1`
与 `TranslateShiftCompat.len_qVec (h : IsUTermVec ℒₛₑₜ (len w) w) : len (qVec ℒₛₑₜ w) = len w + 1`
只在 `k` 与 `len w` 上不同；由 `IsUTermVec.lh : k = len w` 二者合一。 -/
theorem len_qVec_rfl_equiv {k w : V} (h : IsUTermVec ℒₛₑₜ k w) :
    Bootstrapping.len_qVec (L := ℒₛₑₜ) h = len_qVec h := by
  cases h.lh
  rfl

/-- ★ **路线 B（重言式）**：`hAll` 的无条件形式（`HAllUncond.hAll` 的别名）。 -/
theorem hAll_uncond := @GodelQ.HAllUncond.hAll (V := V)

/-- **路线 A（等式桥）**：`iT_subst_open` 的 m=0 实例。 -/
theorem bridgeB (q : V) (hq : IsSemiformula ℒₒᵣ (1:V) q) :
    subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) q) = iT (0:V) (subst ℒₒᵣ (?[^&0] : V) q) := by
  have h1 : IsSemiformula ℒₒᵣ ((0:V) + 1) q := by
    rw [show (0:V) + 1 = 1 from _root_.zero_add 1]; exact hq
  have h := GodelQ.ITSubstOpen9.iT_subst_open (V := V) (0:V) q h1
  rw [GodelQ.QvecVDefs.QvecVOr_zero, GodelQ.QvecVDefs.QvecV_zero] at h
  rw [show (0:V) + 1 = 1 from _root_.zero_add 1] at h
  exact h.symm

/-- **路线 A**：`AllKey` 无条件。 -/
theorem allKey_uncond : AllKey (V := V) :=
  allKey_of_bridge (fun {q} hq => bridgeB q hq)

/-- ★ **路线 A**：`AllBlockerQ` **无条件**。 -/
theorem allBlockerQ_uncond : AllBlockerQ (V := V) :=
  allBlockerQ_of_key allKey_uncond

end GodelQ.AllBlockerQUncond

#print axioms GodelQ.AllBlockerQUncond.len_qVec_rfl_equiv
#print axioms GodelQ.AllBlockerQUncond.hAll_uncond
#print axioms GodelQ.AllBlockerQUncond.bridgeB
#print axioms GodelQ.AllBlockerQUncond.allKey_uncond
#print axioms GodelQ.AllBlockerQUncond.allBlockerQ_uncond
