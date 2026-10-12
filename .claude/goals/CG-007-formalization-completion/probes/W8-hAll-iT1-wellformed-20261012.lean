import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeBV
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 决定性探针：`iT 1 ^#0` 的 `bv` 到底是多少？

`iT 1 ^#0 = eqAtom ^#1 = ^rel 2 cEqN ?[^#0, ^#1]`。
表面看它用了 bvar `#1`，似乎需要层数 2。但 `isSemiformula_iT` 说
`IsSemiformula ℒₒᵣ 1 p → IsSemiformula ℒₛₑₜ 1 (iT 1 p)`。

**两者若冲突，说明我对 `bv` 的理解有误。** 直接测。 -/

-- `^#0` 是**项**不是公式，`iT` 作用不上。改用最小的公式 `^rel 2 R ?[^#0,^#0]`。
-- 关键：`IsSemiformula ℒₛₑₜ 1 (iT 1 (^rel 2 R ?[^#0,^#0]))` 是否成立？
example {R : V} (hR : (ℒₒᵣ).IsRel 2 R) :
    IsSemiformula ℒₛₑₜ 1 (iT (1 : V) (^rel 2 R (?[^#0, ^#0] : V))) :=
  isSemiformula_iT (V := V) (n := (1 : V)) (^rel 2 R (?[^#0, ^#0] : V))
    (IsSemiformula.rel.mpr ⟨hR, IsSemitermVec.doubleton.mpr
      ⟨IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1),
       IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1)⟩⟩)

end GodelQ.ProbeBV
