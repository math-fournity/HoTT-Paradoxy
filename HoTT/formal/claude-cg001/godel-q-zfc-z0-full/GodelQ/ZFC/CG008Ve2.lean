import GodelQ.ZFC.CG008VeLevel

/-!
# CG-008 · `ve2` 的零件
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Ve2
open GodelQ.ZFCArith GodelQ.Translate GodelQ.CG008VeParts
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `cFunc k f` 在 `k ≠ 0` 时是层 3 的公式（add/mul）。 -/
lemma cFunc_isSemiformula_three {k f : V} (hk : k ≠ 0) :
    Bootstrapping.IsSemiformula ℒₛₑₜ 3 (Translate.cFunc k f) := by
  rw [Translate.cFunc]
  by_cases hf : f = 0 <;>
    simp only [hk, hf, ↓reduceIte, Translate.cFuncN, ite_true, ite_false]
  all_goals try norm_num
  · rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote (V := V) (L := ℒₛₑₜ) (n := 3)
      (arithTrln.func Language.ORing.Func.add)]
    simpa [Nat.cast_ofNat] using
      FFL.FirstOrder.Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (n := 3) _
  · rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote (V := V) (L := ℒₛₑₜ) (n := 3)
      (arithTrln.func Language.ORing.Func.mul)]
    simpa [Nat.cast_ofNat] using
      FFL.FirstOrder.Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (n := 3) _

/-- 三元替换向量 `^#2 ∷ ?[^#0, ^#1]` 在层 3 是项向量。

用 `IsSemitermVec.cons_iff` + `doubleton` 拆，避免直接处理 `V` 上的界。 -/
lemma isSemitermVec_ve2vec : Bootstrapping.IsSemitermVec ℒₛₑₜ 3 3 (^#2 ∷ (?[^#0, ^#1] : V)) := by
  rw [show (3 : V) = 2 + 1 by norm_num]
  rw [Bootstrapping.IsSemitermVec.cons_iff]
  refine ⟨?_, ?_⟩
  · simp [Bootstrapping.IsSemiterm.bvar]
  · rw [Bootstrapping.IsSemitermVec.doubleton]
    exact ⟨by simp [Bootstrapping.IsSemiterm.bvar], by simp [Bootstrapping.IsSemiterm.bvar]⟩

-- `conjunct` 的公式性未证：两个 `subst` 分支的层数要与 `cDomN`（层 1）和 `y` 对齐，
-- 本轮两次尝试未过。见包内记录。

end GodelQ.CG008Ve2

#print axioms GodelQ.CG008Ve2.cFunc_isSemiformula_three
#print axioms GodelQ.CG008Ve2.isSemitermVec_ve2vec
