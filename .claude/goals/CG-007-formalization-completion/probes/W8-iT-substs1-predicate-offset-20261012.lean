import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iT_substs1` 的归纳设置（谓词被接受，九支待填）**。

护罩必须是 **`param + 1 = n`**（不是 `param = n`）：因为 `iT` 的 `all`/`exs` 支
把参数推一格（`param ↦ param+1`），而 `subst` 推过 `qqAlls` 时向量用 `qVec`
（首分量 `^#0`）。两者**同步**，故归纳不变量里 `param` 与 `n` 差 1。

本机确认：谓词被 `semiformula_result_induction` 接受，
九支的归纳假设形状正确（`rel` 支已能展开到 `iTR` 层）。 -/
theorem iT_substs1_setup : ∀ p, IsSemiformula ℒₒᵣ (1:V) p →
    iT (0:V) (subst ℒₒᵣ (?[^&0] : V) p) = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p → param + 1 = n →
      iT param (subst ℒₒᵣ (?[^&0] : V) p)
        = subst ℒₛₑₜ (?[^&0] : V) (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param + 1 = n →
        iT param (subst ℒₒᵣ (?[^&0] : V) p) = subst ℒₛₑₜ (?[^&0] : V) q)
      (by definability)
      (by intro n param k R v hR hv h; sorry)
      (by intro n param k R v hR hv h; sorry)
      (by intro n param h; sorry)
      (by intro n param h; sorry)
      (by intro n param p q hp hq ihp ihq h; sorry)
      (by intro n param p q hp hq ihp ihq h; sorry)
      (by intro n param p hp ih h; sorry)
      (by intro n param p hp ih h; sorry)
  · intro p hp
    have h := key (param := (0:V)) (n := (1:V)) hp (by norm_num)
    rw [show iT.construction.result ℒₒᵣ (0:V) p = iT (0:V) p from rfl] at h
    rw [show iT.construction.result ℒₒᵣ (1:V) p = iT (1:V) p from rfl] at h
    exact h

end GodelQ.ProbeFL
