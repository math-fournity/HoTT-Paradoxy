import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ExsBlockerQ ⟸ 一条**具名**残余义务（2026-10-13）

把上一条探针的归约打包成：一个具名 `def`（残余义务）+
`ExsBlockerQ` 由它推出的**完整证明**。

`hExsBridge` 的自由参数 `T'` 是桥接项——残余内容正是「`iT` 与 `substs1` 的相容」，
与 `AllBlocker` 的 `iT_substs1` 同源（§2.7 判死的等式路线是**等式**形态，
这里是**蕴含**形态：`replace_of_imp` 只需要 `¬A ⋎ B` 可证，不需要 A = B）。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

namespace ProbeExsNamed

/-- **`hExs` 的具名残余义务**：`ex_m` 的桥接。

`ih` 手里是 `iT 0 (substs1 ℒᵣ t p)`，而 `ex_m` 要 `substs1 ℒₛₑₜ T' (domZero ⋏ iT 1 p)`。
两者由 `replace_of_imp` 桥接，条件是这条内部蕴含在 𝗭𝗙𝗖 中可证。
`T'` 是桥接项（`IsTerm ℒₛₑₜ T'`）。 -/
def ExsBridge (V : Type*) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] : Prop :=
  ∀ {p t T' : V}, IsUFormula ℒₒᵣ p → IsTerm ℒₒᵣ t → IsTerm ℒₛₑₜ T' →
    Provable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (neg ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p))
        ^⋎ substs1 ℒₛₑₜ T' (domZero (V := V) ^⋏ iT (0+1:V) p))

/-- **`ExsBlockerQ` 由 `ExsBridge` 推出**（证明完整，无未证标记）。 -/
theorem exsBlockerQ_of_bridge (hBr : ExsBridge V) :
    ShCraigElimSetupQ.ExsBlockerQ (V := V) := by
  intro s p t dd hs hps ht hfd hder ih
  unfold Q at ih ⊢
  rw [fstIdx_exsIntro]
  rw [hfd, translateSeq_insert] at ih
  -- `ex_m` 要的成员关系
  have hpex : IsSemiformula ℒₒᵣ (1:V) p := by
    have h0 : IsFormula ℒₒᵣ (^∃ p) := hs (^∃ p) hps
    simpa using (IsSemiformula.exs (L := ℒₒᵣ) (n := (0:V)) (p := p)).mp h0
  have hp : IsUFormula ℒₒᵣ p := hpex.isUFormula
  have hmem : ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V) ∈ translateSeq s :=
    mem_translateSeq_iff.mpr ⟨(^∃ p : V), hps,
      (iT_exs (V := V) (n := (0:V)) hp).symm⟩
  -- 桥接项取 `^&0`（`ℒₛₑₜ` 无函数符号，项只能是变量）
  have hT' : IsTerm ℒₛₑₜ (^&(0:V) : V) :=
    IsSemiterm.fvar (L := ℒₛₑₜ) (V := V) (n := (0:V)) 0
  -- `replace_of_imp` 的三条良构性前提
  have hS : IsFormulaSet (L := ℒₛₑₜ) (translateSeq s) :=
    ShCraigElimBranches.isFormulaSet_translateSeq hs
  have hA : IsFormula ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p)) :=
    isSemiformula_iT (n := (0:V)) (substs1 ℒₒᵣ t p)
      (IsSemiformula.substs1 (L := ℒₒᵣ) (n := (0:V)) ht hpex)
  have hB : IsFormula ℒₛₑₜ (substs1 ℒₛₑₜ (^&(0:V)) (domZero (V := V) ^⋏ iT (0+1:V) p)) :=
    IsSemiformula.substs1 (L := ℒₛₑₜ) (n := (0:V)) hT'
      (IsSemiformula.and.mpr ⟨by simpa using isSemiformula_domZero (V := V) (n := (0:V)),
        by simpa using isSemiformula_iT (n := (1:V)) p hpex⟩)
  -- 桥接：`¬A ⋎ B` 内部可证
  have hAB : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (neg ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p))
        ^⋎ substs1 ℒₛₑₜ (^&(0:V)) (domZero (V := V) ^⋏ iT (0+1:V) p)) ∅) :=
    internal_provable_iff_internal_derivable.mp (hBr hp ht hT')
  exact Derivable.ex_m hmem hT' (ShCraigElimSetupQ.replace_of_imp hAB hA hB hS ih)

end ProbeExsNamed

#print axioms ProbeExsNamed.exsBlockerQ_of_bridge