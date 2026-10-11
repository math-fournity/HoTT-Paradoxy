import GodelQ.ZFC.SeqTranslate

/-! 探针 L8：三条新引理（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.Translate GodelQ.ZFCArith

namespace ProbeL8

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma isSemiformula_cRel (R : V) : IsSemiformula ℒₛₑₜ 2 (cRel R) := by
  unfold cRel cRelN
  split <;> split <;>
    first
      | rw [Sentence.coe_quote_eq_quote]
        exact Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (arithTrln.rel Language.ORing.Rel.eq)
      | rw [Sentence.coe_quote_eq_quote]
        exact Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (arithTrln.rel Language.ORing.Rel.lt)

lemma isSemiformula_cDomN : IsSemiformula ℒₛₑₜ 1 (↑cDomN : V) := by
  unfold cDomN
  rw [Sentence.coe_quote_eq_quote]
  simpa using
    Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (arithTrln.domain)

-- 0 元函数定义公式
lemma isSemiformula_cFunc_zero : IsSemiformula ℒₛₑₜ 1 (cFunc 0 0) := by
  simp only [cFunc, cFuncN, reduceIte]
  rw [Sentence.coe_quote_eq_quote]
  simpa using
    Sentence.quote_isSemiformula (L := ℒₛₑₜ) (arithTrln.func Language.ORing.Func.zero)

end ProbeL8
