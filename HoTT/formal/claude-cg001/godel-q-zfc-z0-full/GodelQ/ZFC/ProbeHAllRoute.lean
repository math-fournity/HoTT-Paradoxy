import GodelQ.ZFC.TranslateSeqShift
import GodelQ.ZFC.ShCraigElimBranches

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

set_option maxHeartbeats 4000000

namespace GodelQ.ProbeHAllRoute
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 检查 imp 的展开是否 rfl
example (a b : V) : imp ℒₛₑₜ a b = neg ℒₛₑₜ a ^⋎ b := rfl

-- 检查 ¬ 的层
#check @IsSemiformula.neg
#check @IsSemiformula.verum
#check @isSemiformula_iT
#check @IsSemiformula.free
#check @mem_bitInsert_iff
#check @IsSemiformula.all
#check @isSemiformula_domZero
#check @substs_neg
#check @neg_neg

-- 路线验证：hAll 归约到一条公式恒等式 hkey
example {s p : V} (hs : IsFormulaSet ℒₒᵣ s) (hp : (^∀ p : V) ∈ s)
    (ih : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (translateSeq (insert (free ℒₒᵣ p) (setShift ℒₒᵣ s))))
    (hkey : free ℒₛₑₜ (imp ℒₛₑₜ domZero (iT (1 : V) p))
      = imp ℒₛₑₜ (subst ℒₛₑₜ (?[^&0] : V) (cDomN : V))
          (iT (0 : V) (free ℒₒᵣ p))) :
    Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq s) := by
  have hp1 : IsSemiformula ℒₒᵣ 1 p := by
    have h := IsSemiformula.all.mp (hs _ hp)
    simpa using h
  have hpu : IsUFormula ℒₒᵣ p := hp1.isUFormula
  have hS : IsFormulaSet (L := ℒₛₑₜ) (setShift ℒₛₑₜ (translateSeq s)) :=
    IsFormulaSet.setShift (GodelQ.ShCraigElimBranches.isFormulaSet_translateSeq hs)
  have hA : IsSemiformula ℒₛₑₜ 0 (iT (0 : V) (free ℒₒᵣ p)) :=
    isSemiformula_iT (free ℒₒᵣ p) (IsSemiformula.free hp1)
  have hZ : IsSemiformula ℒₛₑₜ 0 (subst ℒₛₑₜ (?[^&0] : V) (cDomN : V)) :=
    IsSemiformula.subst isSemiformula_cDomN
      (IsSemitermVec.singleton.mpr (IsSemiterm.fvar 0 0))
  have hih : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (iT (0 : V) (free ℒₒᵣ p)) (setShift ℒₛₑₜ (translateSeq s))) := by
    rw [translateSeq_insert, GodelQ.TranslateSeqShift.translateSeq_setShift hs] at ih
    exact ih
  have hmem : (^∀ (imp ℒₛₑₜ domZero (iT (1 : V) p)) : V) ∈ translateSeq s :=
    mem_translateSeq_iff.mpr ⟨^∀ p, hp, (iT_all hpu).symm⟩
  refine Derivable.all_m (s := translateSeq s) hmem ?_
  rw [hkey]
  refine Derivable.cut (L := ℒₛₑₜ) (T := 𝗭𝗙𝗖) (iT (0 : V) (free ℒₒᵣ p)) ?_ ?_
  · -- 第一义务：从 IH 弱化
    refine Derivable.wk ?_ ?_ hih
    · intro q hq
      rcases mem_bitInsert_iff.mp hq with rfl | hq
      · exact hA
      · rcases mem_bitInsert_iff.mp hq with rfl | hq
        · exact hZ.imp hA
        · exact hS q hq
    · intro x hx
      simp only [mem_bitInsert_iff] at hx ⊢
      tauto
  · -- 第二义务：{¬A, dZ→A} 可证
    rw [show imp ℒₛₑₜ (subst ℒₛₑₜ (?[^&0] : V) (cDomN : V))
          (iT (0 : V) (free ℒₒᵣ p))
        = neg ℒₛₑₜ (subst ℒₛₑₜ (?[^&0] : V) (cDomN : V))
          ^⋎ iT (0 : V) (free ℒₒᵣ p) from rfl]
    refine Derivable.or_m ?_ ?_
    · simp only [mem_bitInsert_iff]; tauto
    · refine Derivable.em ?_ _ ?_ ?_
      · intro q hq
        rcases mem_bitInsert_iff.mp hq with rfl | hq
        · exact hZ.neg
        · rcases mem_bitInsert_iff.mp hq with rfl | hq
          · exact hA
          · rcases mem_bitInsert_iff.mp hq with rfl | hq
            · exact hA.neg
            · rcases mem_bitInsert_iff.mp hq with rfl | hq
              · exact hZ.imp hA
              · exact hS q hq
      · simp only [mem_bitInsert_iff]; tauto
      · simp only [mem_bitInsert_iff]; tauto

end GodelQ.ProbeHAllRoute
