import GodelQ.ZFC.CG008Bv3

/-!
# CG-008 · `bv (iVE n t) ≤ n + 1`——主定理

## 形状

`iVE n t` 按 `t` 的结构递归：
`bvar z ↦ eqAtom (^#(z+1))`、`fvar x ↦ eqAtom (^&x)`、
`func k f v ↦ if k = 0 then ve0 k f else ve2 n k f (iVE-结果向量)`。

## 关键

用 `IsSemiterm.induction`（`Term/Basic.lean:912`），其 `bvar` 分支给 **`z < n`**——
正是所需的界（`IsUTerm.induction` 的 `bvar` 分支不给界，见 `CG008Bv2.lean`）。

## 已备零件

- `bv_iVE_gate`（`CG008Bv3.lean`）：Σ₁ 闸门已过；
- `eqAtom_isUFormula`（`CG008RelCase2.lean`）；
- `ve0_isUFormula`、`ve2_isUFormula`（`CG008VeLevel`/`CG008ShiftProof`）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008BvBound
open GodelQ.ZFCArith GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`eqAtom` 的 `bv` 界**：`bv (eqAtom t) ≤ termBV t + 1`。

用 `bv_rel` 化到 `listMax (termBVVec 2 ?[^#0, t])`，
再用 `listMax_adjoin` 两次化到 `max 1 (max (termBV t) 0)`，
最后 `max_le` 拆成 `1 ≤ termBV t + 1` 与 `termBV t ≤ termBV t + 1`。
**全程用 `≤` 不用 `=`**（`V` 无 `OrderedRing`，`max_eq_left` 要的 `0 ≤ x` 没有现成引理）。 -/
theorem bv_eqAtom_le (t : V) (ht : Bootstrapping.IsUTerm ℒₛₑₜ t) :
    Bootstrapping.bv ℒₛₑₜ (Translate.eqAtom t)
      ≤ Max.max (Bootstrapping.termBV ℒₛₑₜ t) 1 := by
  have hv : Bootstrapping.IsUTermVec ℒₛₑₜ 2 (?[^#0, t] : V) :=
    Bootstrapping.IsUTermVec.mkSeq₂_iff.mpr
      ⟨Bootstrapping.IsUTerm.bvar (L := ℒₛₑₜ) (z := 0), ht⟩
  have hR : (ℒₛₑₜ).IsRel 2 (Translate.cEqN : V) := by
    rw [Translate.cEqN]
    exact (Bootstrapping.isRel_quote_quote (V := V) (L := ℒₛₑₜ) (k := 2)
      (x := Encodable.encode (Language.Eq.eq : (ℒₛₑₜ).Rel 2))).mpr
      ⟨Language.Eq.eq, rfl⟩
  rw [Translate.eqAtom, Bootstrapping.bv_rel hR hv]
  -- `listMax (termBVVec 2 ?[^#0, t]) ≤ termBV t + 1`
  -- 走 `listMaxss_le_iff` 逐分量，避免任何 `listMax` 的 `max` 律
  rw [Arithmetic.listMaxss_le_iff]
  intro i hi
  rw [Bootstrapping.len_termBVVec hv] at hi
  rw [Bootstrapping.nth_termBVVec hv hi]
  -- `i < 2` 拆成 `i = 0 ∨ i = 1`
  have h2 : (2 : V) = 1 + 1 := by norm_num
  rw [h2, lt_succ_iff_le] at hi
  rcases le_iff_lt_or_eq.mp hi with hi0 | hi1
  · -- `i < 1` ⇒ `i = 0`
    have : i = 0 := by
      rw [lt_one_iff_eq_zero] at hi0; exact hi0
    subst this
    rw [GodelQ.CG008Bv2.nth_vec₂_zero]
    rw [Bootstrapping.termBV_bvar]
    -- `1 ≤ max (termBV t) 1`
    simpa using le_max_right (Bootstrapping.termBV ℒₛₑₜ t) (1 : V)
  · -- `i = 1`
    subst hi1
    rw [GodelQ.CG008Bv2.nth_vec₂_one]
    -- `termBV t ≤ max (termBV t) 1`
    exact le_max_left (Bootstrapping.termBV ℒₛₑₜ t) (1 : V)

end GodelQ.CG008BvBound

#print axioms GodelQ.CG008BvBound.bv_eqAtom_le
