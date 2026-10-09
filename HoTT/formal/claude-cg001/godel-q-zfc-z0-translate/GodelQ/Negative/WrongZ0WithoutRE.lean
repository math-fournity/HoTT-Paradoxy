import GodelQ.ZFC.Z0PA

/-! 负控制：不导入内部翻译（因而没有 `Sh.RE` 实例），直接要不带前提的 Z0 影子形式。
Lean 必须在实例 `Sh.RE` 处拒绝。这表明 C-120 的无条件形式正是靠 W4b 新证的实例得到的，
`𝗜𝚺₁ ⪯ Sh`（C-110）一条不够。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory GodelQ.ZFCZ0 GodelQ.ZFCArith in
theorem wrong_zfc_z0_without_re : 𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val) :=
  zfc_z0_of_RE
