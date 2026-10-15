import GodelQ.ZFC.ArrivalRational

/-!
# 命题对照：CG001-C-428（极限的有理数 ε–N 写法落到 𝗭𝗙𝗖）

* (1) 每一个 𝗜𝚺₁ 模型里，有理精度的到达恰是 2⁻ᴷ 精度的到达；
* (2)(3) 𝗭𝗙𝗖 逐个证明有理精度的到达句与 C-118 的到达句等价，因而与永不停机句等价；
* (4) 有理精度的到达句在 `Universe` 里的意思恰是跑者到达；
* (5) 它在 ℕ 里逐字是剩余距离趋于 0 的 ε–N 写法，ε 取遍正有理数；
* (6) 有一个跑者确实到达，𝗭𝗙𝗖 每一刻都确认它尚未停，却证明不了它的有理精度到达句；
* (7) 𝗭𝗙𝗖 证明经典芝诺的有理精度极限句；(8) 那句话在 ℕ 里逐字是 2⁻ⁿ → 0 的 ε–N 写法，ε 取遍正有理数。
-/

namespace GodelQ.ArrivalRat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic
open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.ZFCEff GodelQ.ZFCSound GodelQ.Arrival GodelQ.ArrivalZFC

/-- CG001-C-428：极限的有理数 ε–N 写法落到 𝗭𝗙𝗖。 -/
theorem qual_C428 :
    (∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (e : V),
      arrRatF.Evalb ![e] ↔ arrF.Evalb ![e]) ∧
    (∀ a : ℕ, 𝗭𝗙𝗖 ⊢ arrRatS a 🡘 arrS a) ∧
    (∀ a : ℕ, 𝗭𝗙𝗖 ⊢ arrRatS a 🡘 neverS ΦS a) ∧
    (∀ d : Process, Universe.{0}↓[ℒₛₑₜ] ⊧ arrRatS (Encodable.encode d) ↔ Arrives d) ∧
    (∀ d : Process, arrRatF.Evalb ![Encodable.encode d] ↔
      ∀ p q : ℕ, 0 < p → 0 < q → ∃ N, ∀ n, N ≤ n → remaining d n < (p : ℝ) / q) ∧
    (∃ d : Process, Arrives d ∧ (∀ k : ℕ, 𝗭𝗙𝗖 ⊢ haltsS ΨN (Encodable.encode (d, k))) ∧
      𝗭𝗙𝗖 ⊬ arrRatS (Encodable.encode d)) ∧
    (𝗭𝗙𝗖 ⊢ arithTrln.translate arriveRatC) ∧
    (ℕ↓[ℒₒᵣ] ⊧ arriveRatC ↔
      ∀ p q : ℕ, 0 < p → 0 < q → ∃ N, ∀ n, N ≤ n → (1 / 2 : ℝ) ^ n < (p : ℝ) / q) :=
  ⟨fun _ _ _ e => arrRat_iff_arr e, zfc_arrRat_iff_arr, zfc_arrRat_iff_never, universe_arrRatS_iff,
    arrRat_encode_rat, zfc_runner_rat, zfc_arriveRatC, arriveRatC_nat⟩

end GodelQ.ArrivalRat

#print axioms GodelQ.ArrivalRat.qual_C428
#print axioms GodelQ.ArrivalRat.arrRat_iff_arr
#print axioms GodelQ.ArrivalRat.zfc_arrRat_iff_never
#print axioms GodelQ.ArrivalRat.zfc_runner_rat
#print axioms GodelQ.ArrivalRat.zfc_arriveRatC
#print axioms GodelQ.ArrivalRat.arrRat_encode_rat
#print axioms GodelQ.ArrivalRat.arriveRatC_nat
