import GodelQ.ZFC.ProbeL

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate
open GodelQ.TranslateShiftCompat GodelQ.ProbeK GodelQ.ProbeL

set_option maxHeartbeats 800000

namespace GodelQ.ProbeM

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `rel` 支：`iT n (^rel k R v) = iTR n k R v`，`shift` 走 `shift_iTR`。 -/
lemma iT_shift_rel {n k R v : V} (hR : (ℒₒᵣ).IsRel k R) (hv : IsSemitermVec ℒₒᵣ k n v) :
    iT n (shift ℒₒᵣ (^rel k R v)) = shift ℒₛₑₜ (iT n (^rel k R v)) := by
  rw [Bootstrapping.shift_rel hR hv.isUTerm,
      iT_rel hR (hv.termShiftVec.isUTerm),
      iT_rel hR hv.isUTerm, shift_iTR hR hv]

/-- `nrel` 支：`iT n (^nrel k R v) = neg (iTR n k R v)`；两边都要 `shift_neg`。 -/
lemma iT_shift_nrel {n k R v : V} (hR : (ℒₒᵣ).IsRel k R) (hv : IsSemitermVec ℒₒᵣ k n v) :
    iT n (shift ℒₒᵣ (^nrel k R v)) = shift ℒₛₑₜ (iT n (^nrel k R v)) := by
  rw [Bootstrapping.shift_nrel hR hv.isUTerm,
      iT_nrel hR (hv.termShiftVec.isUTerm),
      iT_nrel hR hv.isUTerm]
  rw [show neg ℒₛₑₜ (iTR n k R (termShiftVec ℒₒᵣ k v))
        = shift ℒₛₑₜ (neg ℒₛₑₜ (iTR n k R v)) from by
      rw [shift_neg (n := n) (isSemiformula_iTR hR hv), shift_iTR hR hv]]

/-- `verum` 支。 -/
lemma iT_shift_verum (n : V) :
    iT n (shift ℒₒᵣ (^⊤ : V)) = shift ℒₛₑₜ (iT n (^⊤ : V)) := by
  rw [shift_verum, iT_verum]
  exact (shift_verum (L := ℒₛₑₜ) (V := V)).symm

/-- `falsum` 支。 -/
lemma iT_shift_falsum (n : V) :
    iT n (shift ℒₒᵣ (^⊥ : V)) = shift ℒₛₑₜ (iT n (^⊥ : V)) := by
  rw [shift_falsum, iT_falsum]
  exact (shift_falsum (L := ℒₛₑₜ) (V := V)).symm

/-- `and` 支：`iT_and` 两侧 + `shift_and`。 -/
lemma iT_shift_and {n p q : V} (hp : IsSemiformula ℒₒᵣ n p) (hq : IsSemiformula ℒₒᵣ n q)
    (ihp : iT n (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT n p))
    (ihq : iT n (shift ℒₒᵣ q) = shift ℒₛₑₜ (iT n q)) :
    iT n (shift ℒₒᵣ (p ^⋏ q)) = shift ℒₛₑₜ (iT n (p ^⋏ q)) := by
  have hsp : IsSemiformula ℒₛₑₜ n (iT n p) := isSemiformula_iT (n := n) p hp
  have hsq : IsSemiformula ℒₛₑₜ n (iT n q) := isSemiformula_iT (n := n) q hq
  rw [shift_and hp.isUFormula hq.isUFormula,
      iT_and hp.isUFormula.shift hq.isUFormula.shift,
      iT_and hp.isUFormula hq.isUFormula,
      shift_and hsp.isUFormula hsq.isUFormula, ihp, ihq]

/-- `or` 支。 -/
lemma iT_shift_or {n p q : V} (hp : IsSemiformula ℒₒᵣ n p) (hq : IsSemiformula ℒₒᵣ n q)
    (ihp : iT n (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT n p))
    (ihq : iT n (shift ℒₒᵣ q) = shift ℒₛₑₜ (iT n q)) :
    iT n (shift ℒₒᵣ (p ^⋎ q)) = shift ℒₛₑₜ (iT n (p ^⋎ q)) := by
  have hsp : IsSemiformula ℒₛₑₜ n (iT n p) := isSemiformula_iT (n := n) p hp
  have hsq : IsSemiformula ℒₛₑₜ n (iT n q) := isSemiformula_iT (n := n) q hq
  rw [shift_or hp.isUFormula hq.isUFormula,
      iT_or hp.isUFormula.shift hq.isUFormula.shift,
      iT_or hp.isUFormula hq.isUFormula,
      shift_or hsp.isUFormula hsq.isUFormula, ihp, ihq]

/-- `all` 支：`iT n (^∀ p) = ^∀ imp domZero (iT (n+1) p)`。
`shift` 走 `shift_all` + `shift_imp_domZero`。 -/
lemma iT_shift_all {n p : V} (hp : IsSemiformula ℒₒᵣ (n + 1) p)
    (ih : iT (n + 1) (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT (n + 1) p)) :
    iT n (shift ℒₒᵣ (^∀ p)) = shift ℒₛₑₜ (iT n (^∀ p)) := by
  have hpu : IsUFormula ℒₒᵣ p := hp.isUFormula
  have hsp : IsSemiformula ℒₛₑₜ (n + 1) (iT (n + 1) p) := isSemiformula_iT (n := n + 1) p hp
  rw [Bootstrapping.shift_all hpu, iT_all hpu.shift, iT_all hpu,
      Bootstrapping.shift_all (IsUFormula.imp.mpr ⟨isUFormula_domZero2, hsp.isUFormula⟩)]
  congr 1
  rw [show (imp ℒₛₑₜ (domZero (V := V)) (iT (n + 1) (shift ℒₒᵣ p)))
        = imp ℒₛₑₜ (domZero (V := V)) (iT (n + 1) (shift ℒₒᵣ p)) from rfl]
  rw [shift_imp_domZero hsp.isUFormula, ih]

/-- `exs` 支：`iT n (^∃ p) = ^∃ domZero ^⋏ iT (n+1) p`。
`shift` 走 `shift_exs` + `shift_conj_domZero`。 -/
lemma iT_shift_exs {n p : V} (hp : IsSemiformula ℒₒᵣ (n + 1) p)
    (ih : iT (n + 1) (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT (n + 1) p)) :
    iT n (shift ℒₒᵣ (^∃ p)) = shift ℒₛₑₜ (iT n (^∃ p)) := by
  have hpu : IsUFormula ℒₒᵣ p := hp.isUFormula
  have hsp : IsSemiformula ℒₛₑₜ (n + 1) (iT (n + 1) p) := isSemiformula_iT (n := n + 1) p hp
  rw [Bootstrapping.shift_exs hpu, iT_exs hpu.shift, iT_exs hpu,
      Bootstrapping.shift_exs (IsUFormula.and.mpr ⟨isUFormula_domZero2, hsp.isUFormula⟩)]
  congr 1
  rw [shift_conj_domZero hsp.isUFormula, ih]

end GodelQ.ProbeM
