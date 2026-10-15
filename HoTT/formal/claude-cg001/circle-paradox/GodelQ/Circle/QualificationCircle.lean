import GodelQ.Circle.CircleParadox

/-!
# 命题对照：CG001-C-424（圆环悖论本身）
-/

namespace GodelQ.Circle

open Filter Topology GodelQ.Zeno

/-- CG001-C-424。 -/
theorem qual_C424 :
    -- 从 M 到 N 一步；我们当初确实得到了 M
    Nonempty (M ≃ₜ N) ∧ M.Nonempty ∧
    -- 从 N 复原到 M：两端越来越近，却在任何有限阶段都没合上
    ArrivesAt farEnd (0 : Ring) ∧ ¬ AttainsAt farEnd (0 : Ring) ∧
    (∀ n, θ n = zenoSeq 1 (n + 1)) ∧
    -- 每个有限阶段的形态都不是 M；只在极限那一刻是 M
    (∀ n, Set.range (bend (θ n)) ≠ M) ∧ Set.range (bend 1) = M ∧
    -- 点没有大小：缺口永远含无穷多个点，长度永远大于 0
    (∀ n, (gap n).Infinite) ∧ (∀ n, 0 < 1 - θ n) ∧
    -- 归因：拿走的那一点在圆上不是孤立点
    ¬ Isolated (0 : Ring) ∧
    -- 离散环对照：逼近在有限阶段到达；缺口在有限步内只剩一点
    (∀ (m : ℕ) (s : ℕ → Fin m) (x : Fin m), ArrivesAt s x → AttainsAt s x) ∧
    (∀ g₀ k, g₀ - 1 ≤ k → discreteGap g₀ k = 1) :=
  ⟨one_step, M_nonempty, farEnd_arrives, closing_never_attains, θ_eq_zenoSeq, range_bend_ne,
    range_bend_one, gap_infinite, gap_length_pos, zero_not_isolated,
    fun _ _ _ h => discrete_closing_attains h, discreteGap_reaches_one⟩

end GodelQ.Circle

#print axioms GodelQ.Circle.qual_C424
