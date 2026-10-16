import GodelQ.ZFC.SeqTranslateFormula

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

open GodelQ.Translate GodelQ.ZFCArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 负控制（应与正式规则 iVE_bvar 冲突）：把 iVE 的 bvar 规则错写成"层数不加一"。
-- 内核应拒绝：iVE 0 ^#0 = eqAtom ^#1，而 eqAtom ^#0 ≠ eqAtom ^#1。
example : iVE (0 : V) (^#0) = eqAtom (^#0) := by
  rw [iVE_bvar]

end GodelQ.SeqTranslate
