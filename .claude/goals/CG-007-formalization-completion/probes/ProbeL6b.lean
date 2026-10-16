import GodelQ.ZFC.SeqTranslate

/-! 探针 L6b：三条新引理（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.Translate GodelQ.ZFCArith

namespace ProbeL6b

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 第 3 条：cRel 的公式性（层级 = 元数 2）
lemma isSemiformula_cRel (R : V) : IsSemiformula ℒₛₑₜ 2 (cRel R) := by
  unfold cRel cRelN
  split <;> split <;>
    first
      | exact Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (arithTrln.rel Language.ORing.Rel.eq)
      | exact Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (arithTrln.rel Language.ORing.Rel.lt)

-- 定义域公式的编码
lemma isSemiformula_cDomN : IsSemiformula ℒₛₑₜ 1 (↑cDomN : V) := by
  unfold cDomN
  exact Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (arithTrln.domain)

end ProbeL6b
