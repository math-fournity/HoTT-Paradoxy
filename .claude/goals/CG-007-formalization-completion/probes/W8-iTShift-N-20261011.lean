import GodelQ.ZFC.ProbeM

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate
open GodelQ.TranslateShiftCompat GodelQ.ProbeK GodelQ.ProbeL GodelQ.ProbeM

set_option maxHeartbeats 800000

namespace GodelQ.ProbeN

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iT` 与 `shift` 的跨语言相容律**（一般公式码 `p`，层数 `n`）。

`iT` 是 `UformulaRec1` 的构造，用 `semiformula_result_induction` 在 V 内部归纳；
九支分别由 `ProbeM` 的引理给出。与 `iT_neg` 同法，谓词带 `param = n` 护罩
（`iT` 的 `all`/`exs` 支改层数 `param + 1`）。 -/
theorem iT_shift {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT n p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p → param = n →
      iT param (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n → iT param (shift ℒₒᵣ p) = shift ℒₛₑₜ q)
      (by definability)
      -- rel
      (by
        intro n param k R v hR hv h
        subst h
        rw [show iT.construction.rel param k R v = iT param (^rel k R v) from
          (UformulaRec1.Construction.result_rel (c := iT.construction) (L := ℒₒᵣ)
            hR hv.isUTerm).symm]
        exact iT_shift_rel hR hv)
      -- nrel
      (by
        intro n param k R v hR hv h
        subst h
        rw [show iT.construction.nrel param k R v = iT param (^nrel k R v) from
          (UformulaRec1.Construction.result_nrel (c := iT.construction) (L := ℒₒᵣ)
            hR hv.isUTerm).symm]
        exact iT_shift_nrel hR hv)
      -- verum
      (by
        intro n param h
        subst h
        simpa [iT] using iT_shift_verum param)
      -- falsum
      (by
        intro n param h
        subst h
        simpa [iT] using iT_shift_falsum param)
      -- and
      (by
        intro n param p q hp hq ihp ihq h
        subst h
        rw [show iT.construction.and param p q
              (UformulaRec1.Construction.result ℒₒᵣ iT.construction param p)
              (UformulaRec1.Construction.result ℒₒᵣ iT.construction param q)
              = iT param (p ^⋏ q) from
          (UformulaRec1.Construction.result_and (c := iT.construction) (L := ℒₒᵣ)
            hp.isUFormula hq.isUFormula).symm]
        exact iT_shift_and hp hq (ihp rfl) (ihq rfl))
      -- or
      (by
        intro n param p q hp hq ihp ihq h
        subst h
        rw [show iT.construction.or param p q
              (UformulaRec1.Construction.result ℒₒᵣ iT.construction param p)
              (UformulaRec1.Construction.result ℒₒᵣ iT.construction param q)
              = iT param (p ^⋎ q) from
          (UformulaRec1.Construction.result_or (c := iT.construction) (L := ℒₒᵣ)
            hp.isUFormula hq.isUFormula).symm]
        exact iT_shift_or hp hq (ihp rfl) (ihq rfl))
      -- all
      (by
        intro n param p hp ih h
        subst h
        simpa [iT] using iT_shift_all hp (ih 0 (by simp [iT.construction]) (by simp [iT.construction])))
      -- exs
      (by
        intro n param p hp ih h
        subst h
        simpa [iT] using iT_shift_exs hp (ih 0 (by simp [iT.construction]) (by simp [iT.construction])))
  · intro p hp
    have h := key hp (rfl : n = n)
    simpa [iT] using h

end GodelQ.ProbeN
