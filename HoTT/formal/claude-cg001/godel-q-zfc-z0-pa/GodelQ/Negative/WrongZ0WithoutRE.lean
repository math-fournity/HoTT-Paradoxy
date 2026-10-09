import GodelQ.ZFC.Z0PA

/-! 负控制：`𝗜𝚺₁ ⪯ Sh` 已经是定理（C-110），但 `Sh.RE` 仍没有证明。不给 `Sh.RE`，Z0 的结论推不出来，
Lean 必须拒绝（实例 `Sh.RE` 找不到）。这表明剩下的这条前提确实被用到，本包没有偷偷证明它。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory GodelQ.ZFCZ0 GodelQ.ZFCArith in
theorem wrong_z0_without_RE : 𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val) :=
  zfc_z0_of_RE
