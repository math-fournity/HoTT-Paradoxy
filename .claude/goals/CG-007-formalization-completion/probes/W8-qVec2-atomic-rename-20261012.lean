import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeH
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
/-! ## 决定性实验：`qVec²` 形状的原子情形（2026-10-12，exit 0）

按更正后的猜想：`iT 0 (subst w p) = subst (qVec² w) (iT 2 p)`（`w = ?[^&0]`，`p` 层数 1）。
`qVec² ?[^&0] = ?[^#0, ^#1, ^&0]`。

**注意层数**：左边 `iT 0`，右边 `iT 2`——差 2，因为 `eqAtom` 自带一层绑定变量。 -/

example : subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V) (^rel (0 + 1 + 1) (↑cEqN) (?[^#0, ^#2] : V))
    = (^rel (0 + 1 + 1) (↑cEqN) (?[^#0, ^&0] : V) : V) := by
  have hv : IsUTermVec ℒₛₑₜ (0 + 1 + 1) ((^#0 : V) ∷ ((^#2 : V) ∷ (0 : V))) :=
    IsUTermVec.adjoin
      (IsUTermVec.adjoin (IsUTermVec.empty (L := ℒₛₑₜ) (V := V)) (IsUTerm.bvar (z := (2:V))))
      (IsUTerm.bvar (z := (0:V)))
  have hR : (ℒₛₑₜ).IsRel (0 + 1 + 1) (↑cEqN : V) := by
    rw [show (0:V) + 1 + 1 = 2 by norm_num, cEqN]
    exact codeIn_rel_quote _
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) hR (by simpa using hv)]
  congr 1
  rw [show (?[^#0, ^#2] : V) = (^#0 : V) ∷ ((^#2 : V) ∷ (0 : V)) from rfl,
    show (0 : V) + 1 + 1 = 2 by norm_num,
    termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (2:V))),
    termSubst_bvar, termSubst_bvar]
  simp

end GodelQ.ProbeH
