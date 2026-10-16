import GodelQ.ZFC.SeqTranslateFormula

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

open GodelQ.Translate GodelQ.ZFCArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- [1a] iVE bvar 计算规则
example (n z : V) : iVE n (^#z) = eqAtom (^#(z + 1)) := by
  simp [iVE, iVE.construction]

-- [1b] iVE fvar 计算规则
example (n x : V) : iVE n (^&x) = eqAtom (^&x) := by
  simp [iVE, iVE.construction]

-- [1c] iVE func 计算规则（保持 resultVec 形式）
example {n k f v : V} (hkf : (ℒₒᵣ).IsFunc k f) (hv : IsUTermVec ℒₒᵣ k v) :
    iVE n (^func k f v) =
      (if k = 0 then ve0 k f else ve2 n k f (iVE.construction.resultVec ℒₒᵣ ![n] k v)) := by
  rw [iVE, iVE.construction.result_func' hkf hv]
  rfl

-- [1d] resultVec 的第 i 项是递归结果
example {n k v : V} (hv : IsUTermVec ℒₒᵣ k v) {i : V} (hi : i < k) :
    (iVE.construction.resultVec ℒₒᵣ ![n] k v).[i] = iVE n v.[i] := by
  rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv hi]
  simp [iVE]

end GodelQ.SeqTranslate
