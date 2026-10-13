import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`TermBShift.construction` 的 `func` 字段与 `L` 无关**（定义即得）。

这是绕开 `IsFunc` 的关键：`termBShift_func` 要 `L.IsFunc k f`，
但 `construction.func` 的定义里**没有它**。 -/
lemma tbs_func_lang (k f v' : V) :
    TermBShift.construction.func ℒₒᵣ ![] k f v' v'
      = TermBShift.construction.func ℒₛₑₜ ![] k f v' v' := rfl

/-- **`termBShift` 的语言无关性**（全称版，用 `construction` 绕开 `IsFunc`）。 -/
lemma termBShift_lang_indep : ∀ t, IsUTerm ℒₒᵣ t →
    termBShift ℒₒᵣ t = termBShift ℒₛₑₜ t := by
  apply IsUTerm.induction (L := ℒₒᵣ) 𝚺
    (P := fun t ↦ termBShift ℒₒᵣ t = termBShift ℒₛₑₜ t) (by definability)
  case hbvar =>
    intro z; rw [termBShift_bvar, termBShift_bvar]
  case hfvar =>
    intro x; rw [termBShift_fvar, termBShift_fvar]
  case hfunc =>
    intro k f v hkf hv ih
    show TermBShift.construction.result ℒₒᵣ ![] (^func k f v)
        = TermBShift.construction.result ℒₛₑₜ ![] (^func k f v)
    rw [show TermBShift.construction.result ℒₒᵣ ![] (^func k f v)
          = TermBShift.construction.func ℒₒᵣ ![] k f v
            (TermBShift.construction.resultVec ℒₒᵣ ![] k v) from
      TermBShift.construction.result_func' (L := ℒₒᵣ) hkf hv]
    rw [show TermBShift.construction.result ℒₛₑₜ ![] (^func k f v)
          = TermBShift.construction.func ℒₛₑₜ ![] k f v
            (TermBShift.construction.resultVec ℒₛₑₜ ![] k v) from
      TermBShift.construction.result_func' (L := ℒₛₑₜ) hkf hv]
    simp only [TermBShift.construction]
    congr 1
    apply nth_ext' k ?_ ?_ ?_
    · rw [TermBShift.construction.resultVec_lh ℒₒᵣ ![] hv]
    · rw [TermBShift.construction.resultVec_lh ℒₛₑₜ ![] hv]
    · intro i hi
      rw [TermBShift.construction.nth_resultVec ℒₒᵣ ![] hv hi,
        TermBShift.construction.nth_resultVec ℒₛₑₜ ![] hv hi]
      exact ih i hi

end GodelQ.ProbeFL
