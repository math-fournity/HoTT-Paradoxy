import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ExsBlockerQ 归约到一条内部可证性（2026-10-13）

路线：`replace_of_imp` + `Derivable.ex_m`。

1. `hmem`：`^∃ (domZero ⋏ iT 1 p) ∈ translateSeq s`（`iT_exs` + `mem_translateSeq_iff`，已证）；
2. `ih` 给出 `Derivable (insert (iT 0 (substs1 t p)) (translateSeq s))`；
3. `replace_of_imp` 把 sequent 里的 `iT 0 (substs1 t p)` 换成实例公式；
4. `ex_m` 消掉 `^∃`。

**剩余恰好一条**：内部可证性 `Provable 𝗭𝗙𝗖 (neg A ⋎ B)`。
本探针验证：除该条外，路线全部 typecheck。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

namespace ProbeExsReduce

theorem exsB_reduced (s p t dd T' : V)
    (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hps : ^∃ p ∈ (s : V))
    (hp : IsUFormula ℒₒᵣ p)
    (ht : IsTerm ℒₒᵣ t)
    (hT' : IsTerm ℒₛₑₜ T')
    (hfd : fstIdx dd = insert (substs1 ℒₒᵣ t p) s)
    (ih : Q (V := V) dd)
    (hprov : Provable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (neg ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p))
        ^⋎ substs1 ℒₛₑₜ T' (domZero (V := V) ^⋏ iT (0+1:V) p))) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s) := by
  unfold Q at ih
  rw [hfd, translateSeq_insert] at ih
  have hmem : ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V) ∈ translateSeq s :=
    mem_translateSeq_iff.mpr ⟨(^∃ p : V), hps,
      (iT_exs (V := V) (n := (0:V)) hp).symm⟩
  have hAB : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (neg ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p))
        ^⋎ substs1 ℒₛₑₜ T' (domZero (V := V) ^⋏ iT (0+1:V) p)) ∅) :=
    internal_provable_iff_internal_derivable.mp hprov
  have hS : IsFormulaSet (L := ℒₛₑₜ) (translateSeq s) :=
    ShCraigElimBranches.isFormulaSet_translateSeq hs
  have hpex : IsSemiformula ℒₒᵣ (1:V) p := by
    have h0 : IsFormula ℒₒᵣ (^∃ p) := hs (^∃ p) hps
    simpa using (IsSemiformula.exs (L := ℒₒᵣ) (n := (0:V)) (p := p)).mp h0
  have hA : IsFormula ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p)) :=
    isSemiformula_iT (n := (0:V)) (substs1 ℒₒᵣ t p)
      (IsSemiformula.substs1 (L := ℒₒᵣ) (n := (0:V)) ht hpex)
  have hB : IsFormula ℒₛₑₜ (substs1 ℒₛₑₜ T' (domZero (V := V) ^⋏ iT (0+1:V) p)) :=
    IsSemiformula.substs1 (L := ℒₛₑₜ) (n := (0:V)) hT'
      (IsSemiformula.and.mpr ⟨by simpa using isSemiformula_domZero (V := V) (n := (0:V)),
        by simpa using isSemiformula_iT (n := (1:V)) p hpex⟩)
  exact Derivable.ex_m hmem hT' (ShCraigElimSetupQ.replace_of_imp hAB hA hB hS ih)

end ProbeExsReduce

#print axioms ProbeExsReduce.exsB_reduced
