import GodelQ.ZFC.ArrivalZFC

/-! 负控制（C-118）：把到达句与**旧的**永不停机句 `neverS ΦH`（Foundation 的不透明 Σ1 公式 `codeOfREPred`）
配对，照搬 `zfc_arr_iff_never` 的语义论证。那一步要的是“在每个模型里，到达句与 `haltsS ΦH` 一真一假”，
手里只有对 `ΦS` 的结论；旧公式在非标准模型里的行为无从推理，Lean 必须拒绝。等价是对 `ΦS` 证的，
到达句与停机公式来自同一个 `stopF`，这一点被用到了。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory GodelQ.ZFCNum GodelQ.ZFCEff GodelQ.ArrivalZFC in
theorem wrong_arrival_old_phi (a : ℕ) : 𝗭𝗙𝗖 ⊢ arrS a 🡘 neverS ΦH a := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  rw [Semantics.models_iff, neverS, Semantics.Not.models_not]
  exact models_arr_iff_not_halts (M := M) a
