import GodelQ.TwoChoices.Core
import GodelQ.TwoChoices.Rational
import GodelQ.TwoChoices.Machines

/-!
# 命题对照与公理审计：CG001-C-418 至 C-421

* C-418：两次选择是同一条原则。在不预设排中律的底座上，A 的两种形态（单调开关的终值；有界单调
  自然数序列的终值）都与 LPO 互推；去掉“有界”，A 的单调形态不成立。
* C-419：对照。芝诺过程在每个精度上的整数读数，落定的步由公式给出（第 `k` 步），落定后比“1”
  恰少一格，每一步都还没到；不用 LPO。桥（经典）：整数读数就是有理数位置 `1 - (1/2)ⁿ` 的读数；
  有理数列的柯西步由公式给出，极限是 1，每一步都小于 1。
* C-420：A 断言其存在的结果，机器交不出。每个停机搜索在经典逻辑里都有落定的一步，却没有机器
  统一交出这一步，也没有机器交出终值。
* C-421：经典逻辑（Lean，与 ZFC 一样）对“会停”与“永不停”一视同仁，集合的存在不过问可计算性；
  同一个理论又证得出二者可计算性的差别；LPO 在经典逻辑里是定理。

**公理审计**（文件末尾的 `run_cmd`，机器断言，违反则编译失败）：
1. C-418、C-419 的整数部分及其组成定理不依赖 `Classical.choice`。在经典逻辑里 LPO 与 A 本来都是
   定理，互推没有内容；内容只在这一条上。
2. 对照：C-420、C-421、`lpo_classical` 与 C-419 的有理数桥确实依赖 `Classical.choice`，说明审计
   不是空的；Mathlib 的 `Rat.le_total` 也依赖它，这是有理数一侧只作桥的原因。
-/

namespace GodelQ.TwoChoices

open GodelQ

/-- CG001-C-418：两次选择是同一条原则（不预设排中律）。 -/
theorem qual_C418 :
    (LimBit ↔ LPO) ∧ (NatBMC ↔ LPO) ∧
    ¬ (∀ x : Nat → Nat, MonoNat x → ∃ N, SettlesAt x N) :=
  ⟨limBit_iff_lpo, natBMC_iff_lpo, unbounded_settling_false⟩

/-- CG001-C-419：芝诺的极限用不着 A（整数读数，构造性）。 -/
theorem qual_C419 :
    (∀ k, SettlesAt (zenoReading k) k) ∧
    (∀ k, zenoReading k k + 1 = 2 ^ k) ∧
    (∀ k n, zenoReading k n < 2 ^ k) ∧
    (∀ k, MonoNat (zenoReading k)) :=
  ⟨zenoReading_settles, zenoReading_final, zenoReading_lt, zenoReading_mono⟩

/-- CG001-C-419 的桥（经典）：整数读数就是有理数位置的读数；有理数列的收敛步由公式给出。 -/
theorem qual_C419_bridge :
    (∀ k n, ((zenoReading k n : ℕ) : ℤ) = ⌊(2 : ℚ) ^ k * zenoQ n⌋) ∧
    Monotone zenoQ ∧
    (∀ n, zenoQ n < 1) ∧
    (∀ k m, k ≤ m → 1 - zenoQ m ≤ (1 / 2) ^ k) ∧
    CauchyQ zenoQ :=
  ⟨zenoReading_eq_floor, zenoQ_mono, zenoQ_lt_one, zenoQ_close, zenoQ_cauchy⟩

/-- CG001-C-420：A 断言其存在的结果，机器交不出。 -/
theorem qual_C420 :
    (∀ e : Process, MonoBits (haltBits e)) ∧
    (∀ e : Process, ∃ N, SettlesAt (haltBits e) N) ∧
    (¬ ∃ F : Process → ℕ, Computable F ∧ ∀ e, SettlesAt (haltBits e) (F e)) ∧
    (¬ ∃ f : Process → Bool, Computable f ∧
      ∀ e, ∃ N, SettlesAt (haltBits e) N ∧ haltBits e N = f e) :=
  ⟨haltBits_mono, haltBits_settles_classically, no_computable_settling_point,
    no_computable_final_value⟩

/-- CG001-C-421：经典逻辑不区分“停”与“不停”，又证得出二者的差别；LPO 在经典逻辑里是定理。 -/
theorem qual_C421 :
    LPO ∧
    (∀ e : Process, Done e ∨ ¬ Done e) ∧
    ((∃ S : Set Process, ∀ e, e ∈ S ↔ Done e) ∧ (∃ S : Set ℕ, ∀ n, n ∈ S ↔ n % 2 = 0)) ∧
    (ComputablePred (fun n : ℕ => n % 2 = 0) ∧ ¬ ComputablePred Done) :=
  ⟨lpo_classical, bivalence_halting, sets_exist_alike, computability_differs⟩

end GodelQ.TwoChoices

open Lean in
run_cmd do
  let constructive : List Name :=
    [``GodelQ.TwoChoices.qual_C418, ``GodelQ.TwoChoices.qual_C419,
     ``GodelQ.TwoChoices.lpo_of_limBit, ``GodelQ.TwoChoices.limBit_of_lpo,
     ``GodelQ.TwoChoices.settles_of_lpo_gap, ``GodelQ.TwoChoices.natBMC_of_lpo,
     ``GodelQ.TwoChoices.limBit_of_natBMC, ``GodelQ.TwoChoices.unbounded_settling_false,
     ``GodelQ.TwoChoices.zenoReading_settles, ``GodelQ.TwoChoices.zenoReading_final,
     ``GodelQ.TwoChoices.zenoReading_lt, ``GodelQ.TwoChoices.zenoReading_mono]
  for n in constructive do
    let axs ← collectAxioms n
    if axs.contains ``Classical.choice then
      throwError m!"公理审计失败：{n} 依赖 Classical.choice（{axs}）"
    logInfo m!"公理审计通过：{n} 不依赖 Classical.choice；实际公理 {axs}"
  let classical : List Name :=
    [``GodelQ.TwoChoices.qual_C420, ``GodelQ.TwoChoices.qual_C421,
     ``GodelQ.TwoChoices.lpo_classical, ``GodelQ.TwoChoices.qual_C419_bridge, ``Rat.le_total]
  for n in classical do
    let axs ← collectAxioms n
    unless axs.contains ``Classical.choice do
      throwError m!"对照失败：{n} 本应依赖 Classical.choice（{axs}）"
    logInfo m!"对照：{n} 依赖 Classical.choice；实际公理 {axs}"

#print axioms GodelQ.TwoChoices.qual_C418
#print axioms GodelQ.TwoChoices.qual_C419
#print axioms GodelQ.TwoChoices.qual_C419_bridge
#print axioms GodelQ.TwoChoices.qual_C420
#print axioms GodelQ.TwoChoices.qual_C421
