/-!
# 两次选择：放弃 ASK 与选择 A，在不预设排中律的底座上是同一条原则（CG001-C-418、C-419）

研究发起人（2026-10-14，原话节选）：“ZFC放弃了这种观察力，得到了A型数学便利，并同时异化为了
ZFC-1=ZFC+A。放弃是一次选择，而A是第二次选择。A是什么？A就是一个无限的步骤才能到达，从而存在的
结果，当作已经存在的结果，参与运算。”

本文件只用 Lean 内核，不导入 Mathlib。全部证明不用 `Classical.choice`：在经典逻辑里，下面几条
原则本来都是定理，它们之间的等价没有内容；内容只在“不用排中律也推得出”这一点上。
`QualificationTC.lean` 的公理审计会机器断言这一点，违反则编译失败。

* `LPO`：每个 ω 追问要么永远答“否”，要么某一步答“是”。读法：每个无限搜索停不停，已经定了；
  不问判定它的过程停不停，就当它有现成的答案。这是“放弃 ASK”落在真假值上的形态。
* `LimBit`：每个单调开关序列都有现成可用的终值，即存在一步，此后不再改变。
  读法：无限步之后才见分晓的结果，被当作已经存在、可以拿来用的结果。这是 A 落在对象上的最简形态。
* `NatBMC`：每个有界单调的自然数序列都有现成的终值。这是 A 的“单调有界必有极限”形态（整数刻度）。
  有理数、实数刻度的形态由它在每个精度上取地板函数得到；本包没有对那一形态做构造性的机器证明
  （Mathlib 的 ℚ 依赖 `Classical.choice`，见 `Rational.lean` 与 `CLAIM.md` §5）。

主定理：`limBit_iff_lpo`、`natBMC_iff_lpo`（C-418 的前两项）。
对照（C-419）：芝诺过程在每个精度上的读数，落定的那一步由公式直接给出（第 `k` 步），不需要任何
搜索，所以“极限是 1”用不着 A（`zenoReading_settles`）。
-/

namespace GodelQ.TwoChoices

/-- 一个 ω 追问：第 `k` 步回答“落定了吗”。与 `same-q-univalent` 的 `OmegaQ = ℕ → Bool` 同型。 -/
abbrev OmegaQ := Nat → Bool

/-- LPO（有限全知原理）：每个 ω 追问，要么永远答“否”，要么在某一步答“是”。 -/
def LPO : Prop := ∀ q : OmegaQ, (∀ k, q k = false) ∨ (∃ k, q k = true)

/-- 单调开关序列：一旦为真，此后都为真。 -/
def MonoBits (s : Nat → Bool) : Prop := ∀ m n, m ≤ n → s m = true → s n = true

/-- 序列在第 `N` 步落定：此后各步的值都等于第 `N` 步的值。 -/
def SettlesAt {α : Type} (s : Nat → α) (N : Nat) : Prop := ∀ m, N ≤ m → s m = s N

/-- A（开关形态）：每个单调开关序列都有一个落定的步，它的终值现成可用。 -/
def LimBit : Prop := ∀ s : Nat → Bool, MonoBits s → ∃ N, SettlesAt s N

/-- 单调的自然数序列。 -/
def MonoNat (x : Nat → Nat) : Prop := ∀ m n, m ≤ n → x m ≤ x n

/-- A（有界单调形态，整数刻度）：每个有界单调的自然数序列都有一个落定的步。 -/
def NatBMC : Prop := ∀ x : Nat → Nat, MonoNat x → ∀ B, (∀ n, x n ≤ B) → ∃ N, SettlesAt x N

/-! ## “到这一问为止，见过‘是’吗” -/

/-- `seen q n`：前 `n + 1` 问里是否出现过“是”。 -/
def seen (q : OmegaQ) : Nat → Bool
  | 0 => q 0
  | n + 1 => seen q n || q (n + 1)

theorem seen_of_le {q : OmegaQ} {k n : Nat} (h : k ≤ n) (hk : q k = true) :
    seen q n = true := by
  induction n with
  | zero =>
    have hk0 : k = 0 := Nat.le_zero.mp h
    subst hk0
    simpa [seen] using hk
  | succ n ih =>
    rcases Nat.lt_or_eq_of_le h with hlt | heq
    · have hs := ih (Nat.le_of_lt_succ hlt)
      simp [seen, hs]
    · subst heq
      simp [seen, hk]

theorem exists_of_seen {q : OmegaQ} : ∀ {n : Nat}, seen q n = true → ∃ k, k ≤ n ∧ q k = true
  | 0, h => ⟨0, Nat.le_refl 0, by simpa [seen] using h⟩
  | n + 1, h => by
    simp only [seen, Bool.or_eq_true] at h
    rcases h with h | h
    · obtain ⟨k, hk, hq⟩ := exists_of_seen h
      exact ⟨k, Nat.le_succ_of_le hk, hq⟩
    · exact ⟨n + 1, Nat.le_refl _, h⟩

theorem seen_mono (q : OmegaQ) : MonoBits (seen q) := by
  intro m n hmn hm
  obtain ⟨k, hk, hq⟩ := exists_of_seen hm
  exact seen_of_le (Nat.le_trans hk hmn) hq

/-! ## A（开关形态）⟹ LPO：承认终值现成，就判定了每个无限搜索 -/

theorem lpo_of_limBit (h : LimBit) : LPO := by
  intro q
  obtain ⟨N, hN⟩ := h (seen q) (seen_mono q)
  cases hs : seen q N with
  | true =>
    obtain ⟨k, _, hk⟩ := exists_of_seen hs
    exact Or.inr ⟨k, hk⟩
  | false =>
    refine Or.inl (fun k => ?_)
    cases hk : q k with
    | false => rfl
    | true =>
      have h1 : seen q (N + k) = true := seen_of_le (Nat.le_add_left k N) hk
      have h2 : seen q (N + k) = seen q N := hN (N + k) (Nat.le_add_right N k)
      rw [h2, hs] at h1
      cases h1

/-! ## LPO ⟹ A（开关形态） -/

theorem limBit_of_lpo (h : LPO) : LimBit := by
  intro s hs
  rcases h s with hall | ⟨k, hk⟩
  · exact ⟨0, fun m _ => by rw [hall m, hall 0]⟩
  · exact ⟨k, fun m hm => by rw [hs k m hm hk, hk]⟩

theorem limBit_iff_lpo : LimBit ↔ LPO := ⟨lpo_of_limBit, limBit_of_lpo⟩

/-! ## LPO ⟹ A（有界单调形态）：对“还能再升几格”归纳，每一格问一次 LPO -/

theorem settles_of_lpo_gap (h : LPO) :
    ∀ G : Nat, ∀ x : Nat → Nat, MonoNat x → (∀ n, x n ≤ x 0 + G) → ∃ N, SettlesAt x N := by
  intro G
  induction G with
  | zero =>
    intro x hx hb
    exact ⟨0, fun m _ => Nat.le_antisymm (by simpa using hb m) (hx 0 m (Nat.zero_le m))⟩
  | succ G ih =>
    intro x hx hb
    rcases h (fun n => decide (x 0 < x n)) with hall | ⟨n0, hn0⟩
    · refine ⟨0, fun m _ => Nat.le_antisymm ?_ (hx 0 m (Nat.zero_le m))⟩
      exact Nat.le_of_not_lt (of_decide_eq_false (hall m))
    · have hlt : x 0 < x n0 := of_decide_eq_true hn0
      have hy : MonoNat (fun n => x (n0 + n)) :=
        fun a b hab => hx _ _ (Nat.add_le_add_left hab n0)
      have hyb : ∀ n, (fun n => x (n0 + n)) n ≤ (fun n => x (n0 + n)) 0 + G := by
        intro n
        have hbn := hb (n0 + n)
        dsimp only
        rw [Nat.add_zero]
        omega
      obtain ⟨N', hN'⟩ := ih (fun n => x (n0 + n)) hy hyb
      refine ⟨n0 + N', fun m hm => ?_⟩
      have e : n0 + (m - n0) = m := by omega
      have hm' := hN' (m - n0) (by omega)
      dsimp only at hm'
      rw [e] at hm'
      exact hm'

theorem natBMC_of_lpo (h : LPO) : NatBMC := by
  intro x hx B hB
  exact settles_of_lpo_gap h B x hx (fun n => Nat.le_trans (hB n) (Nat.le_add_left B (x 0)))

/-! ## A（有界单调形态）⟹ A（开关形态） -/

theorem monoNat_toNat {s : Nat → Bool} (hs : MonoBits s) : MonoNat (fun n => (s n).toNat) := by
  intro m n hmn
  dsimp only
  cases hm : s m with
  | false => exact Nat.zero_le _
  | true =>
    rw [hs m n hmn hm]
    exact Nat.le_refl _

theorem toNat_le_one (b : Bool) : b.toNat ≤ 1 := by
  cases b <;> decide

theorem bool_eq_of_toNat_eq {a b : Bool} (h : a.toNat = b.toNat) : a = b := by
  cases a <;> cases b <;> first | rfl | (cases h)

theorem limBit_of_natBMC (h : NatBMC) : LimBit := by
  intro s hs
  obtain ⟨N, hN⟩ := h (fun n => (s n).toNat) (monoNat_toNat hs) 1 (fun n => toNat_le_one (s n))
  exact ⟨N, fun m hm => bool_eq_of_toNat_eq (hN m hm)⟩

theorem natBMC_iff_lpo : NatBMC ↔ LPO :=
  ⟨fun h => lpo_of_limBit (limBit_of_natBMC h), natBMC_of_lpo⟩

/-- 去掉“有界”，A 的单调形态就不成立：`x n = n` 永不落定。负控制 NEG-002 的正面对应。 -/
theorem unbounded_settling_false :
    ¬ (∀ x : Nat → Nat, MonoNat x → ∃ N, SettlesAt x N) := by
  intro h
  obtain ⟨N, hN⟩ := h (fun n => n) (fun _ _ hmn => hmn)
  have hN1 := hN (N + 1) (Nat.le_succ N)
  dsimp only at hN1
  omega

/-! ## 对照（C-419）：芝诺过程的每个精度上的读数，落定的步由公式给出

芝诺跑者第 `n` 步后的位置是 `1 - 2⁻ⁿ`。在精度 `2⁻ᵏ` 上读它，读数是
`⌊2ᵏ · (1 - 2⁻ⁿ)⌋ = 2ᵏ - 2^(k-n)`（`n ≥ k` 时 `k - n = 0`，读数是 `2ᵏ - 1`；与有理数的对应见
`Rational.lean` 的 `zenoReading_eq_floor`）。下面三条都不用 LPO：
落定的步是 `k` 本身（公式，不是搜索出来的）；落定后的读数比 `2ᵏ`（即“1”）恰少一格；
每一步的读数都小于 `2ᵏ`（每一步都还没到）。 -/

/-- 芝诺过程在精度 `2⁻ᵏ` 上第 `n` 步的读数。 -/
def zenoReading (k n : Nat) : Nat := 2 ^ k - 2 ^ (k - n)

theorem zenoReading_mono (k : Nat) : MonoNat (zenoReading k) := by
  intro m n hmn
  unfold zenoReading
  have hp : 2 ^ (k - n) ≤ 2 ^ (k - m) := Nat.pow_le_pow_right (by decide) (by omega)
  omega

theorem zenoReading_lt (k n : Nat) : zenoReading k n < 2 ^ k := by
  unfold zenoReading
  have h1 : 0 < 2 ^ (k - n) := Nat.two_pow_pos (k - n)
  have h2 : 2 ^ (k - n) ≤ 2 ^ k := Nat.pow_le_pow_right (by decide) (Nat.sub_le k n)
  omega

theorem zenoReading_settles (k : Nat) : SettlesAt (zenoReading k) k := by
  intro m hm
  unfold zenoReading
  have hkm : k - m = 0 := by omega
  rw [hkm, Nat.sub_self]

theorem zenoReading_final (k : Nat) : zenoReading k k + 1 = 2 ^ k := by
  unfold zenoReading
  rw [Nat.sub_self, Nat.pow_zero]
  have hk := Nat.two_pow_pos k
  omega

end GodelQ.TwoChoices

#print axioms GodelQ.TwoChoices.lpo_of_limBit
#print axioms GodelQ.TwoChoices.limBit_of_lpo
#print axioms GodelQ.TwoChoices.limBit_iff_lpo
#print axioms GodelQ.TwoChoices.settles_of_lpo_gap
#print axioms GodelQ.TwoChoices.natBMC_of_lpo
#print axioms GodelQ.TwoChoices.limBit_of_natBMC
#print axioms GodelQ.TwoChoices.natBMC_iff_lpo
#print axioms GodelQ.TwoChoices.unbounded_settling_false
#print axioms GodelQ.TwoChoices.zenoReading_mono
#print axioms GodelQ.TwoChoices.zenoReading_lt
#print axioms GodelQ.TwoChoices.zenoReading_settles
#print axioms GodelQ.TwoChoices.zenoReading_final
