import GodelQ.ZFC.SeqTranslateFormula

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

open GodelQ.Translate GodelQ.ZFCArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `cFunc 0 f`（0 元函数符号的定义公式码）层级 1，对任意 `f`。 -/
lemma isSemiformula_cFunc_arity0 (f : V) : IsSemiformula ℒₛₑₜ 1 (cFunc 0 f) := by
  simp only [cFunc, cFuncN, reduceIte]
  split
  · rw [Sentence.coe_quote_eq_quote]
    simpa using Sentence.quote_isSemiformula (L := ℒₛₑₜ) (arithTrln.func Language.ORing.Func.zero)
  · split
    · rename_i h
      exact absurd h (by decide)
    · rw [Sentence.coe_quote_eq_quote]
      simpa using Sentence.quote_isSemiformula (L := ℒₛₑₜ) (arithTrln.func Language.ORing.Func.one)

/-- `cFunc k f`（2 元函数符号的定义公式码）层级 3，对 `k ≠ 0`。 -/
lemma isSemiformula_cFunc_arity2 {k : V} (hk : k ≠ 0) (f : V) :
    IsSemiformula ℒₛₑₜ 3 (cFunc k f) := by
  simp only [cFunc, cFuncN, reduceIte]
  split
  · rename_i h
    exact absurd h hk
  · split
    · split
      · rename_i h
        exact absurd h (by decide)
      · rw [Sentence.coe_quote_eq_quote]
        simpa using
          Sentence.quote_isSemiformula (L := ℒₛₑₜ) (arithTrln.func Language.ORing.Func.add)
    · split
      · rename_i h
        exact absurd h (by decide)
      · split
        · rename_i h
          exact absurd h (by decide)
        · rw [Sentence.coe_quote_eq_quote]
          simpa using
            Sentence.quote_isSemiformula (L := ℒₛₑₜ) (arithTrln.func Language.ORing.Func.mul)

end GodelQ.SeqTranslate
