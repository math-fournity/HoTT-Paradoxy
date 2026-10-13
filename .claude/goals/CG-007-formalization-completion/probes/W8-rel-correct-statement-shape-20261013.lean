import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`rel` 支（正确陈述形状：`p` 在 `→` 左边）**。

⚠ 不能写成 `iT 1 (^rel 2 R v) = …`（`v` 符号时**陈述层**就 `whnf` 超时）。
必须写成 `∀ p, IsSemiformula … p → …`，照 `iT_shift` 的先例。 -/
example : ∀ p, IsSemiformula ℒₒᵣ (2:V) p →
    iT (1:V) (subst ℒₒᵣ (?[^#0, ^&0] : V) p) = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) p) := by
  intro p hp
  -- `p` 是符号，但只在 `hp` 里出现；下面按构造子分情况
  obtain ⟨k, R, v, hR, hv, rfl⟩ := IsSemiformula.rel.mp hp
  have hw : IsSemitermVec ℒₒᵣ (2:V) (1:V) (?[^#0, ^&0] : V) :=
    IsSemitermVec.doubleton.mpr
      ⟨IsSemiterm.bvar.mpr (by norm_num),
       IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0⟩
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv.isUTerm]
  trace_state
  sorry

end GodelQ.ProbeFL
