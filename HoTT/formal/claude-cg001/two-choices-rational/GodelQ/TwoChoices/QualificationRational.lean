import Lean.Elab.Command
import GodelQ.TwoChoices.RationalConstructive

/-!
# 命题对照与公理审计：CG001-C-425

* C-425 (1)–(2)：两次选择的有理数形态。在不预设排中律的底座上，“每个有界单调的有理数列都收敛”
  （`BMCQ`，柯西形态）与 LPO 互推，也与 A 的开关形态 `LimBit` 互推。
* C-425 (3)–(9)：对照，C-419 的有理数形态。芝诺位置 1 − 2⁻ⁿ 分母为正，单调，有界，每一步都小于 1；
  柯西步与“离 1 小于 1/(k+1)”的步都由公式 k + 1 给出；步数不能一律取第 0 步。

**公理审计**（文件末尾的 `run_cmd`，机器断言，违反则编译失败）：
1. C-425 及其组成定理不依赖 `Classical.choice`。在经典逻辑里 `BMCQ` 与 LPO 本来都是定理，互推没有
   内容；内容只在这一条上。
2. 对照：借排中律证出的 `bmcQ_classical` 与 `Classical.em` 确实依赖 `Classical.choice`，说明审计不是空的。
-/

namespace GodelQ.TwoChoices

/-- CG001-C-425：两次选择的有理数形态（不预设排中律），以及芝诺的有理数对照。 -/
theorem qual_C425 :
    (BMCQ ↔ LPO) ∧
    (BMCQ ↔ LimBit) ∧
    (∀ n, 0 < (zenoQp n).2) ∧
    MonoQ zenoQp ∧
    BoundedQ zenoQp ∧
    (∀ n, QLt (zenoQp n) (1, 1)) ∧
    (∀ k m n : Nat, k + 1 ≤ m → k + 1 ≤ n → CloseQ ((k : Int) + 1) (zenoQp m) (zenoQp n)) ∧
    (∀ k n : Nat, k + 1 ≤ n → CloseQ ((k : Int) + 1) (zenoQp n) (1, 1)) ∧
    ¬ (∀ k m n : Nat, CloseQ ((k : Int) + 1) (zenoQp m) (zenoQp n)) :=
  ⟨bmcQ_iff_lpo, bmcQ_iff_limBit, zenoQp_pos, zenoQp_mono, zenoQp_bounded, zenoQp_lt_one,
    zenoQp_cauchy, zenoQp_to_one, zeno_modulus_zero_false⟩

/-- 对照（经典）：借排中律，`BMCQ` 是定理。审计要求它依赖 `Classical.choice`。 -/
theorem bmcQ_classical : BMCQ := by
  apply bmcQ_of_lpo
  intro q
  rcases Classical.em (∃ k, q k = true) with h | h
  · exact Or.inr h
  · refine Or.inl (fun k => ?_)
    cases hk : q k with
    | false => rfl
    | true => exact absurd ⟨k, hk⟩ h

end GodelQ.TwoChoices

open Lean in
run_cmd do
  let constructive : List Name :=
    [``GodelQ.TwoChoices.qual_C425,
     ``GodelQ.TwoChoices.bmcQ_iff_lpo, ``GodelQ.TwoChoices.bmcQ_iff_limBit,
     ``GodelQ.TwoChoices.bmcQ_of_lpo, ``GodelQ.TwoChoices.limBit_of_bmcQ,
     ``GodelQ.TwoChoices.lpo_of_bmcQ,
     ``GodelQ.TwoChoices.flr_mono, ``GodelQ.TwoChoices.close_of_flr_eq,
     ``GodelQ.TwoChoices.zenoQp_mono, ``GodelQ.TwoChoices.zenoQp_bounded,
     ``GodelQ.TwoChoices.zenoQp_lt_one, ``GodelQ.TwoChoices.zenoQp_cauchy,
     ``GodelQ.TwoChoices.zenoQp_cauchyQ, ``GodelQ.TwoChoices.zenoQp_to_one,
     ``GodelQ.TwoChoices.zeno_modulus_zero_false]
  for n in constructive do
    let axs ← collectAxioms n
    if axs.contains ``Classical.choice then
      throwError m!"公理审计失败：{n} 依赖 Classical.choice（{axs}）"
    logInfo m!"公理审计通过：{n} 不依赖 Classical.choice；实际公理 {axs}"
  let classical : List Name :=
    [``GodelQ.TwoChoices.bmcQ_classical, ``Classical.em]
  for n in classical do
    let axs ← collectAxioms n
    unless axs.contains ``Classical.choice do
      throwError m!"对照失败：{n} 本应依赖 Classical.choice（{axs}）"
    logInfo m!"对照：{n} 依赖 Classical.choice；实际公理 {axs}"

#print axioms GodelQ.TwoChoices.qual_C425
#print axioms GodelQ.TwoChoices.bmcQ_iff_lpo
#print axioms GodelQ.TwoChoices.zenoQp_cauchyQ
#print axioms GodelQ.TwoChoices.bmcQ_classical
