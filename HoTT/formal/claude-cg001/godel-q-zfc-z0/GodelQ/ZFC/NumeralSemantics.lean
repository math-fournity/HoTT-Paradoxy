import GodelQ.ZFC.NumeralCode
import GodelQ.ZFC.OmegaArith

/-!
# CG-006 · S4（一）：Rayo 数字公式在 𝗭 的模型中恰好定义 `ofNat n`

`V ⊧ Num_n(z) ↔ z = ofNat n`，对每个 `V ⊧ 𝗭`（元层对 n 归纳；用到外延性与 `succ x = x ∪ {x}`）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory

namespace GodelQ.ZFCNum

variable {V : Type*} [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭]

omit [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭] in
lemma comp_castLE_two (y z : V) :
    (![y, z] ∘ Fin.castLE (by omega : 1 ≤ 2) : Fin 1 → V) = ![y] := by
  funext i
  match i with
  | ⟨0, _⟩ => rfl

lemma eval_numeralF_zero (z : V) : V ⊧/![z] (numeralF 0) ↔ z = ofNat 0 := by
  simp [numeralF, ofNat, mem_ext_iff (x := z)]

lemma eval_numeralF_succ (n : ℕ) (z : V) :
    V ⊧/![z] (numeralF (n + 1)) ↔ ∃ y, V ⊧/![y] (numeralF n) ∧ ∀ w, w ∈ z ↔ w ∈ y ∨ w = y := by
  simp [numeralF, numStep, Matrix.constant_eq_singleton]

lemma eval_numeralF_iff (n : ℕ) (z : V) : V ⊧/![z] (numeralF n) ↔ z = ofNat n := by
  induction n generalizing z with
  | zero => exact eval_numeralF_zero z
  | succ n ih =>
    rw [eval_numeralF_succ]
    simp only [ih, exists_eq_left]
    show (∀ w, w ∈ z ↔ w ∈ (ofNat n : V) ∨ w = ofNat n) ↔ z = SetTheory.succ (ofNat n)
    rw [mem_ext_iff]
    simp only [mem_succ_iff]
    exact forall_congr' fun w ↦ by rw [or_comm]

#print axioms eval_numeralF_iff

end GodelQ.ZFCNum
