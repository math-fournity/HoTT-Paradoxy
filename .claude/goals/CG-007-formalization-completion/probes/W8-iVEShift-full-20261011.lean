import GodelQ.ZFC.ProbeI

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate
open GodelQ.ProbeE GodelQ.ProbeH GodelQ.ProbeI GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeJ

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iVE` 与 `termShift` 的跨语言相容律**（一般项 `t`，层数 `n`）。

`termShift` 改 `ℒₒᵣ` 侧的 fvar（加一），`iVE` 送 fvar 到 `eqAtom ^&x` 不动；
`shift ℒₛₑₜ` 在 `ℒₛₑₜ` 侧对 fvar 也加一。bvar 两侧都不动。
故两条路一致——这是 `iT_shift` 的项层地基。 -/
theorem iVE_shift (n : V) : ∀ t, IsSemiterm ℒₒᵣ n t →
    iVE n (termShift ℒₒᵣ t) = shift ℒₛₑₜ (iVE n t) := by
  apply IsSemiterm.sigma1_induction (L := ℒₒᵣ) (n := n)
    (P := fun t ↦ iVE n (termShift ℒₒᵣ t) = shift ℒₛₑₜ (iVE n t))
  · definability
  · intro z hz
    exact iVE_shift_bvar n z
  · intro x
    exact iVE_shift_fvar n x
  · intro k f v hkf hv ih
    exact iVE_shift_func hkf hv ih

end GodelQ.ProbeJ
