import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeHAll
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `hAll` 支：`^∀ p ∈ s`，子推导在 `insert (free p) (setShift s)` 上。

**归约**：
* `iT 0 (^∀ p) = ^∀ (imp domZero (iT 1 p))`（`iT_all`），故 `translateSeq s` 含该全称；
* `Derivable.all` 需要 `Derivable (insert (free q) (setShift (translateSeq s)))`，`q := imp domZero (iT 1 p)`；
* `free q = D → iT 0 (free p)`（`free_imp_domZero` + `iT_free`），
  `ih` 给 `Derivable (insert (iT 0 (free p)) (setShift (translateSeq s')))`，
  经 `weaken_imp` 得目标。 -/
lemma hAll {s p d : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hp : (^∀ p) ∈ s)
    (hd : fstIdx d = insert (free ℒₒᵣ p) (setShift ℒₒᵣ s))
    (ih : Q (V := V) d) :
    Q (V := V) (allIntro s p d) := by
  simp only [Q, fstIdx_allIntro]
  -- `q := imp domZero (iT 1 p)`
  set q : V := imp ℒₛₑₜ (domZero (V := V)) (iT (1 : V) p) with hq
  -- `^∀ q ∈ translateSeq s`
  have hpa : IsSemiformula ℒₒᵣ (0 + 1) p := by
    have := (hs (^∀ p) hp)
    exact IsSemiformula.all.mp this
  have hfs : IsFormulaSet (L := ℒₒᵣ) (setShift ℒₒᵣ s) :=
    (IsFormulaSet.setShift_iff).mpr hs
  have hfp : IsFormula ℒₒᵣ (free ℒₒᵣ p) := hpa.free
  have hfs' : IsFormulaSet (L := ℒₒᵣ) (insert (free ℒₒᵣ p) (setShift ℒₒᵣ s)) :=
    IsFormulaSet.insert_iff.mpr ⟨hfp, hfs⟩
  have hfs'' : IsFormulaSet (L := ℒₛₑₜ) (setShift ℒₛₑₜ (translateSeq s)) :=
    (IsFormulaSet.setShift_iff).mpr (isFormulaSet_translateSeq hs)
  -- `ih` 展开
  have ih' : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (iT (0 : V) (free ℒₒᵣ p)) (setShift ℒₛₑₜ (translateSeq s))) := by
    have h := ih
    rw [Q, hd] at h
    rw [show translateSeq (insert (free ℒₒᵣ p) (setShift ℒₒᵣ s))
        = insert (iT (0 : V) (free ℒₒᵣ p)) (translateSeq (setShift ℒₒᵣ s)) from
      translateSeq_insert] at h
    rw [translateSeq_setShift hfs] at h
    exact h
  -- `Derivable.all`
  refine Derivable.all (T := 𝗭𝗙𝗖) ?_ ?_
  · -- `IsSemiformula ℒₛₑₜ 1 q`
    rw [hq]
    exact IsSemiformula.imp.mpr
      ⟨isSemiformula_domZero' (V := V),
       isSemiformula_iT (V := V) (n := (1 : V)) p hpa⟩
  · -- `Derivable (insert (free q) (setShift (translateSeq s)))`
    rw [hq]
    sorry

end GodelQ.ProbeHAll
