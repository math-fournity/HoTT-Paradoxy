import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `termBShiftVec` 三元组的展开。用 `nth_ext'` 逐分量，避开 cons 引理的 numeral 匹配。 -/
lemma tBV_three {a b c : V} (ha : IsUTerm ℒₛₑₜ a) (hb : IsUTerm ℒₛₑₜ b)
    (hc : IsUTerm ℒₛₑₜ c) :
    termBShiftVec ℒₛₑₜ (3:V) (?[a, b, c] : V)
      = (?[termBShift ℒₛₑₜ a, termBShift ℒₛₑₜ b, termBShift ℒₛₑₜ c] : V) := by
  have hv : IsUTermVec ℒₛₑₜ (3:V) (?[a, b, c] : V) := by
    rw [show (?[a, b, c] : V) = a ∷ (b ∷ (c ∷ (0:V))) from rfl]
    exact IsUTermVec.adjoin (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty hc) hb) ha
  refine nth_ext' (3:V) ?_ ?_ ?_
  · rw [len_termBShiftVec hv]
  · rw [show (?[termBShift ℒₛₑₜ a, termBShift ℒₛₑₜ b, termBShift ℒₛₑₜ c] : V)
          = termBShift ℒₛₑₜ a ∷ (termBShift ℒₛₑₜ b ∷ (termBShift ℒₛₑₜ c ∷ (0:V))) from rfl]
    simp only [len_adjoin, len_nil]; norm_num
  · intro j hj
    have h3 : j = 0 ∨ j = 1 ∨ j = 2 := by
      have hle : j ≤ (2:V) := by
        have := hj
        rw [show (3:V) = 2 + 1 by norm_num] at this
        exact lt_succ_iff_le.mp this
      rcases le_two_iff_eq_zero_or_one_or_two.mp hle with h | h | h
      · exact Or.inl h
      · exact Or.inr (Or.inl h)
      · exact Or.inr (Or.inr h)
    rcases h3 with rfl | rfl | rfl
    · rw [nth_termBShiftVec hv (by norm_num)]
      simp only [nth_adjoin_zero]
    · rw [nth_termBShiftVec hv (by norm_num)]
      simp only [nth_adjoin_one, nth_adjoin_zero]
    · rw [nth_termBShiftVec hv (by norm_num)]
      simp only [nth_adjoin_two, nth_adjoin_one, nth_adjoin_zero]

/-- `termBShiftVec` 二元组的展开。 -/
lemma tBV_two {a b : V} (ha : IsUTerm ℒₛₑₜ a) (hb : IsUTerm ℒₛₑₜ b) :
    termBShiftVec ℒₛₑₜ (2:V) (?[a, b] : V)
      = (?[termBShift ℒₛₑₜ a, termBShift ℒₛₑₜ b] : V) := by
  rw [show (?[a, b] : V) = a ∷ (b ∷ (0:V)) from rfl]
  rw [show (2:V) = (0 + 1) + 1 by norm_num]
  rw [termBShiftVec_cons ha (IsUTermVec.adjoin IsUTermVec.empty hb)]
  rw [show (0 + 1 : V) = 0 + 1 from rfl, termBShiftVec_cons hb IsUTermVec.empty,
    termBShiftVec_nil]

/-- **向量账（正确版）**：`(qVec)^[2] ?[^#i,^#2] = ?[^#0, ^#1, ^#(i+2), ^#4]`。

**⚠ 我先前的写法 `?[^#0,^#1,^#i,^#2]` 是错的**：`termBShift` 把 bvar **加一**
（它用于「进入一层绑定」），所以 `qVec` 的每一次迭代都让**尾部分量整体 +1**，
而不是原样保留。

```
qVec ?[^#i,^#2]      = ?[^#0, ^#(i+1), ^#3]
qVec ?[^#0,^#(i+1),^#3] = ?[^#0, ^#1, ^#(i+2), ^#4]
```

这正是「保护语义」的具体形态：`subst` 推过 `∀` 时，
向量首格被 `^#0` 占据，其余分量**整体右移一格**。 -/
lemma hqL {i : V} :
    (qVec ℒₛₑₜ)^[2] (?[^#i, ^#2] : V) = (?[^#0, ^#1, ^#(i + 2), ^#4] : V) := by
  rw [Function.iterate_succ_apply', Function.iterate_one]
  rw [show qVec ℒₛₑₜ (?[^#i, ^#2] : V) = (?[^#0, ^#(i + 1), ^#3] : V) from by
    rw [Bootstrapping.qVec,
      show len (?[^#i, ^#2] : V) = (2:V) from by simp [len_adjoin, len_nil]; norm_num]
    rw [tBV_two (IsUTerm.bvar (z := i)) (IsUTerm.bvar (z := (2:V)))]
    rw [termBShift_bvar, termBShift_bvar]
    rw [show ((2:V) + 1) = (3:V) by norm_num]]
  rw [Bootstrapping.qVec,
    show len (?[^#0, ^#(i + 1), ^#3] : V) = (3:V) from by
      simp [len_adjoin, len_nil]; norm_num]
  rw [tBV_three (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (i + 1)))
    (IsUTerm.bvar (z := (3:V)))]
  rw [termBShift_bvar, termBShift_bvar, termBShift_bvar]
  rw [show ((0:V) + 1) = (1:V) by norm_num]
  rw [show (^#((i + 1) + 1) : V) = (^#(i + 2) : V) from by
    rw [show ((i + 1) + 1 : V) = i + 2 by ring]]
  rw [show ((3:V) + 1) = (4:V) by norm_num]

end GodelQ.ProbeFL
