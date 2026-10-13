import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`subst` 的层数收缩**：`subst ?[^#0,^&0] p = subst ?[^#0] p`（`p` 层 1）。

用语言多态版 `subst_congr_prefix'`（本轮新入生产包）。 -/
lemma subst_two_eq_subst_one {p : V} (hp : IsSemiformula ℒₒᵣ (1:V) p) :
    subst ℒₒᵣ (?[^#0, ^&0] : V) p = subst ℒₒᵣ (?[^#0] : V) p := by
  have hv2 : IsSemitermVec ℒₒᵣ (2:V) (1:V) (?[^#0, ^&0] : V) := by
    refine IsSemitermVec.iff (L := ℒₒᵣ) (k := (2:V)) (n := (1:V))
      (v := (?[^#0, ^&0] : V)) |>.mpr ⟨?_, ?_⟩
    · rw [show (?[^#0, ^&0] : V) = (^#0 : V) ∷ ((^&0 : V) ∷ (0:V)) from rfl]
      simp only [len_adjoin, len_nil]; norm_num
    · intro j hj
      show IsSemiterm ℒₒᵣ (1:V) ((^#0 : V) ∷ ((^&0 : V) ∷ (0:V))).[j]
      rcases lt_two_cases hj with rfl | rfl
      · rw [nth_adjoin_zero]; exact IsSemiterm.bvar.mpr (by norm_num)
      · rw [nth_adjoin_one, nth_adjoin_zero]
        exact IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0
  have hv1 : IsSemitermVec ℒₒᵣ (1:V) (1:V) (?[^#0] : V) :=
    IsSemitermVec.singleton.mpr (IsSemiterm.bvar.mpr (by norm_num))
  exact subst_congr_prefix' (L := ℒₒᵣ) (n := (1:V)) (m := (1:V))
    (k₁ := (2:V)) (k₂ := (1:V)) (w := (?[^#0, ^&0] : V)) (w' := (?[^#0] : V)) p hp
    (by norm_num) (by norm_num) hv2 hv1 (fun j hj ↦ by
      have hj0 : j = 0 := lt_one_iff_eq_zero.mp hj
      subst hj0
      rw [show (?[^#0, ^&0] : V) = (^#0 : V) ∷ ((^&0 : V) ∷ (0:V)) from rfl,
        show (?[^#0] : V) = ((^#0 : V) ∷ (0:V)) from rfl]
      rw [nth_adjoin_zero, nth_adjoin_zero])

/-- **`iT_substs1` 的「同层」形状**（候选 1 的目标，归纳谓词已被 Lean 接受）。

```
iT 1 (subst ?[^#0,^&0] σ) = subst ?[^&0] (iT 1 σ)      （σ 层 1）
```

**`rel` 支的精确剩余**（本机实测）：
`iT` 侧已展开到 `iTR param k R (termSubstVec ℒₒᵣ k ?[^#0,^&0] v)`，
`subst` 侧在 `subst ?[^&0] (^rel k R ?[iVE param v.[0], …])`。
两边要接上，需要 **`iTR` 与 `termSubstVec` 的交换律**
（`iTR` 内含 `iVE` 的 `conjunct` 链，逐分量换名）——即 `conjunct_rename_second_gen` 的
一般 `t` 版（本轮已证 `bvar`/`fvar` 两支）。 -/
theorem iT_substs1_samelevel : ∀ p, IsSemiformula ℒₒᵣ (1:V) p →
    iT (1:V) (subst ℒₒᵣ (?[^#0, ^&0] : V) p)
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p → param = n → 0 < param →
      iT param (subst ℒₒᵣ (?[^#0, ^&0] : V) p)
        = subst ℒₛₑₜ (?[^&0] : V) (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n → 0 < param →
        iT param (subst ℒₒᵣ (?[^#0, ^&0] : V) p) = subst ℒₛₑₜ (?[^&0] : V) q)
      (by definability)
      -- rel：**已展开到 iTR 层**，剩余见上
      (by
        intro n param k R v hR hv h hpos
        subst h
        rw [show iT.construction.rel param k R v = iT param (^rel k R v) from
          (UformulaRec1.Construction.result_rel (c := iT.construction) (L := ℒₒᵣ)
            hR hv.isUTerm).symm]
        rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv.isUTerm]
        sorry)
      (by intro n param k R v hR hv h hpos; sorry)
      (by intro n param h hpos; sorry)
      (by intro n param h hpos; sorry)
      (by intro n param p q hp hq ihp ihq h hpos; sorry)
      (by intro n param p q hp hq ihp ihq h hpos; sorry)
      (by intro n param p hp ih h hpos; sorry)
      (by intro n param p hp ih h hpos; sorry)
  · intro p hp
    have h := key (param := (1:V)) (n := (1:V)) hp rfl (by norm_num)
    rw [show iT.construction.result ℒₒᵣ (1:V) p = iT (1:V) p from rfl] at h
    exact h

end GodelQ.ProbeFL
