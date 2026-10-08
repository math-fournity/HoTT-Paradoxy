import GodelQ.ZFC.Z0Shadow

/-!
# CG-006 · S6 负控制：去掉 `𝗜𝚺₁ ⪯ Sh`

条件定理 `zfc_z0_conditional` 用到两条前提。只给 `Sh.RE`、不给 `𝗜𝚺₁ ⪯ Sh` 时，同一结论的证明
应当在缺少 `𝗜𝚺₁ ⪯ Sh` 实例处被拒：这条前提是承重的，不能被 `𝗥₀ ⪯ Sh` 之类已证的事实替代。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic

namespace GodelQ.ZFCZ0

open GodelQ.ZFCArith

theorem wrong_z0_without_ISigma1 [Sh.RE] :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val) :=
  zfc_z0_conditional

end GodelQ.ZFCZ0
