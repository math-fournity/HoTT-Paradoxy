import GodelQ.ZFC.ShRE

/-! 负控制：`Sh.RE` 归结为翻译的可计算性之后，那条可计算性本身没有证明。不给它、只想用 `simp` 搪塞过去，
Lean 必须拒绝。这表明剩下的这条纯语法引理确实被用到，本包没有偷偷证明它。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory GodelQ.ZFCZ0 GodelQ.ZFCArith in
theorem wrong_sh_re_without_computability : Sh.RE :=
  Sh_RE_of_translate_computable (by simp)
