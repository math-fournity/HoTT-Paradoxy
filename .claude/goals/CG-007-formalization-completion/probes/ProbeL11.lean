import GodelQ.ZFC.SeqTranslateFormula

/-! 探针 L11：conjunct 公式性（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.Translate GodelQ.ZFCArith

namespace ProbeL11

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- `shiftVec b n = [^#b, …, ^#(b+n-1)]` 是合法的 n 元项向量，层数 b+n
lemma isSemitermVec_shiftVec (b : V) : ∀ (n : ℕ),
    IsSemitermVec ℒₛₑₜ (n : V) (b + (n : V)) (shiftVec b (n : V))
  | 0 => by simp
  | n + 1 => by
    push_cast
    rw [shiftVec_succ, IsSemitermVec.cons_iff]
    refine ⟨?_, ?_⟩
    · rw [IsSemiterm.bvar]
      calc b < (n : V) + b + 1 := lt_add_self_add_one b (n : V)
        _ = b + ((n : V) + 1) := by ring
    · have ih := isSemitermVec_shiftVec b n
      have h := IsSemitermVec.termBShiftVec (L := ℒₛₑₜ) ih
      simpa only [add_assoc] using h

-- 单元素向量 `?[^#i]`
lemma isSemitermVec_single_bvar {i n : V} (hi : i < n) :
    IsSemitermVec ℒₛₑₜ 1 n ?[^#i] :=
  IsSemitermVec.singleton.mpr (IsSemiterm.bvar.mpr hi)

end ProbeL11
