import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ExsBlockerQ 走 Derivable.ex_m：让 Lean 打印精确残差（2026-10-13）

此前我报的「and_m 拆解」是纸笔推测（and_m 要 p ⋏ q ∈ s，
而 domZero ⋏ iT 1 p 在 ^∃ 里面，不在 s 里——形状不匹配）。
按纪律：让机器打印残差，不写推测。

本探针只做一件事：把 ex_m 路线的两个洞留空，
让 Lean 报出 unsolved goals——那就是机器产出的精确义务。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

namespace GodelQ.ProbeExsResidual

/-- 走 Derivable.ex_m：hmem 可证（iT_exs + mem_translateSeq_iff）；两个洞留空看残差。 -/
theorem exsB_ex_m_residual (s p t dd : V)
    (hps : ^∃ p ∈ (s : V))
    (hp : IsUFormula ℒₒᵣ p)
    (hfd : fstIdx dd = insert (substs1 ℒₒᵣ t p) s)
    (ih : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) (fstIdx dd))) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s) := by
  rw [hfd, translateSeq_insert] at ih
  have hmem : ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V) ∈ translateSeq s :=
    mem_translateSeq_iff.mpr ⟨(^∃ p : V), hps,
      (iT_exs (V := V) (n := (0:V)) hp).symm⟩
  -- 洞 1 可关：^&0 是项（层 0，无绑定变量）。
  refine Derivable.ex_m (t := (^&(0:V) : V)) hmem
    (IsSemiterm.fvar (L := ℒₛₑₜ) (V := V) (n := (0:V)) 0) ?_

end GodelQ.ProbeExsResidual