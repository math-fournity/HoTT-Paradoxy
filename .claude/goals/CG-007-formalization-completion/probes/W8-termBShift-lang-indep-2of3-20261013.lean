import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`termBShift` 的语言无关性**（用计算引理，不用 `rfl`）。

`TermBShift.blueprint` **没有 `L` 参数**（`Term/Functions.lean:320`），
故其 graph 与 `L` 无关；但 `result` 是 `Classical.choose!`，
故 `rfl` 不成立——需按构造子逐条用计算引理。 -/
lemma termBShift_lang_indep_bvar (z : V) :
    termBShift ℒₒᵣ (^#z : V) = termBShift ℒₛₑₜ (^#z : V) := by
  rw [termBShift_bvar, termBShift_bvar]

lemma termBShift_lang_indep_fvar (x : V) :
    termBShift ℒₒᵣ (^&x : V) = termBShift ℒₛₑₜ (^&x : V) := by
  rw [termBShift_fvar, termBShift_fvar]

/-- **`termBShift` 的语言无关性（全称版）**。

`TermBShift.blueprint` **无 `L` 参数**，故其 graph 与语言无关；
`result` 是 `Classical.choose!`，故需按构造子用计算引理逐条证。 -/
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
    -- `termBShift_func` 要 `IsFunc`：`ℒₒᵣ` 侧用 `hkf`，`ℒₛₑₜ` 侧要另证
    rw [termBShift_func (L := ℒₒᵣ) hkf hv]
    sorry

end GodelQ.ProbeFL
