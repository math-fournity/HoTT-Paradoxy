import Mathlib.Tactic.Ring
import GodelQ.TwoChoices.Core

/-!
# CG-010 R3：两次选择的实数形态——有界单调的有理数列都收敛 ⟺ LPO（构造性，CG001-C-425）

C-418 在整数刻度上证明了：A（单调序列的终值现成可用）与 LPO 在不预设排中律的底座上互推。它同时
写明，有理数、实数一侧没有做构造性的机器证明，因为 Mathlib 的 ℚ 本身依赖 `Classical.choice`。
本文件自己写一套最小的有理数，补上这一形态。

* 有理数取整数对 `(a, b)`，b 是正的自然数，表示 a/b；比较用交叉相乘（`QLe`、`QLt`）。
* `CloseQ c p q`：|p − q| < 1/c，交叉相乘写出。
* 收敛取柯西形态（`CauchyQ`）：对每个精度 1/(k+1)，有一步 N，此后两两之差小于 1/(k+1)。这里的
  “有一步”是命题层的存在，不给出模的函数。
* `BMCQ`：每个有界单调、分母为正的有理数列都收敛。这是 A 的“单调有界必有极限”形态（有理数刻度）。

主定理 `bmcQ_iff_lpo : BMCQ ↔ LPO`：
* LPO ⟹ BMCQ：在精度 1/(k+1) 上取整数读数 ⌊(k+1)·xₙ⌋（分母为正时，`Int` 的带余除法就是取整）。
  读数单调有界，由 `Core` 的整数刻度定理 `natBMC_of_lpo` 得到落定的一步；读数相同的两项相差小于
  1/(k+1)。
* BMCQ ⟹ LPO：把单调开关序列看成 0/1 的有理数列（分母为 1），在精度 1 上落定，用 C-418 的
  `lpo_of_limBit`。

对照（C-419 的有理数形态，构造性）：芝诺位置 1 − 2⁻ⁿ 单调，有界，每一步都小于 1；柯西步与“离 1
小于 1/(k+1)”的步都由公式 k + 1 直接给出，不用 LPO。

只用 Lean 内核的整数引理、`omega` 与 `ring`（`ring` 在 ℤ 上只用 `propext`）；不用 `linarith`、
`nlinarith`，它们在 ℤ 上依赖 `Classical.choice`。`QualificationRational.lean` 的公理审计机器断言：
这里的定理都不依赖 `Classical.choice`。
-/

namespace GodelQ.TwoChoices

/-- 有理数：整数对 (a, b)，表示 a/b；用到时要求 b > 0。 -/
abbrev Qp := Int × Nat

/-- a/b ≤ a'/b'（交叉相乘）。 -/
def QLe (p q : Qp) : Prop := p.1 * (q.2 : Int) ≤ q.1 * (p.2 : Int)

/-- a/b < a'/b'（交叉相乘）。 -/
def QLt (p q : Qp) : Prop := p.1 * (q.2 : Int) < q.1 * (p.2 : Int)

/-- |p − q| < 1/c（交叉相乘）。 -/
def CloseQ (c : Int) (p q : Qp) : Prop :=
  c * (p.1 * (q.2 : Int) - q.1 * (p.2 : Int)) < (p.2 : Int) * (q.2 : Int) ∧
  c * (q.1 * (p.2 : Int) - p.1 * (q.2 : Int)) < (p.2 : Int) * (q.2 : Int)

/-- 有理数列单调。 -/
def MonoQ (x : Nat → Qp) : Prop := ∀ m n, m ≤ n → QLe (x m) (x n)

/-- 有理数列有上界。 -/
def BoundedQ (x : Nat → Qp) : Prop := ∃ B : Qp, 0 < B.2 ∧ ∀ n, QLe (x n) B

/-- 柯西：对每个精度 1/(k+1)，有一步 N，此后两两之差小于 1/(k+1)。 -/
def CauchyQ (x : Nat → Qp) : Prop :=
  ∀ k : Nat, ∃ N, ∀ m n, N ≤ m → N ≤ n → CloseQ ((k : Int) + 1) (x m) (x n)

/-- A（有理数形态）：每个有界单调、分母都为正的有理数列都收敛。 -/
def BMCQ : Prop :=
  ∀ x : Nat → Qp, (∀ n, 0 < (x n).2) → MonoQ x → BoundedQ x → CauchyQ x

/-! ## 精度 1/c 上的整数读数 ⌊c · a/b⌋ -/

/-- ⌊c · a / b⌋（b > 0 时，`Int` 的带余除法就是取整）。 -/
def flr (c : Int) (p : Qp) : Int := (c * p.1) / (p.2 : Int)

theorem flr_le {c : Int} {p : Qp} (hb : 0 < p.2) : (p.2 : Int) * flr c p ≤ c * p.1 :=
  Int.mul_ediv_self_le (by omega)

theorem lt_flr {c : Int} {p : Qp} (hb : 0 < p.2) :
    c * p.1 < (p.2 : Int) * flr c p + (p.2 : Int) :=
  Int.lt_mul_ediv_self_add (by omega)

/-- 读数单调：a/b ≤ a'/b'，c ≥ 0 ⟹ ⌊c·a/b⌋ ≤ ⌊c·a'/b'⌋。 -/
theorem flr_mono {c : Int} (hc : 0 ≤ c) {p q : Qp} (hp : 0 < p.2) (hq : 0 < q.2) (h : QLe p q) :
    flr c p ≤ flr c q := by
  have hq' : (0 : Int) < (q.2 : Int) := by omega
  have hp' : (0 : Int) < (p.2 : Int) := by omega
  show flr c p ≤ (c * q.1) / (q.2 : Int)
  rw [Int.le_ediv_iff_mul_le hq']
  -- 要证 ⌊c·a/b⌋ · b' ≤ c · a'
  have h1 : (p.2 : Int) * flr c p ≤ c * p.1 := flr_le hp
  have h2 : (p.2 : Int) * flr c p * (q.2 : Int) ≤ c * p.1 * (q.2 : Int) :=
    Int.mul_le_mul_of_nonneg_right h1 (Int.le_of_lt hq')
  have h3 : c * (p.1 * (q.2 : Int)) ≤ c * (q.1 * (p.2 : Int)) :=
    Int.mul_le_mul_of_nonneg_left h hc
  have e1 : (p.2 : Int) * flr c p * (q.2 : Int) = (p.2 : Int) * (flr c p * (q.2 : Int)) := by ring
  have e2 : c * p.1 * (q.2 : Int) = c * (p.1 * (q.2 : Int)) := by ring
  have e3 : c * (q.1 * (p.2 : Int)) = (p.2 : Int) * (c * q.1) := by ring
  rw [e1, e2] at h2
  rw [e3] at h3
  exact Int.le_of_mul_le_mul_left (Int.le_trans h2 h3) hp'

/-- 读数相同的两个有理数，相差小于 1/c。 -/
theorem close_of_flr_eq {c : Int} {p q : Qp} (hp : 0 < p.2) (hq : 0 < q.2)
    (h : flr c p = flr c q) : CloseQ c p q := by
  have hp' : (0 : Int) < (p.2 : Int) := by omega
  have hq' : (0 : Int) < (q.2 : Int) := by omega
  have hp1 : (p.2 : Int) * flr c q ≤ c * p.1 := h ▸ flr_le hp
  have hp2 : c * p.1 < (p.2 : Int) * flr c q + (p.2 : Int) := h ▸ lt_flr hp
  have hq1 : (q.2 : Int) * flr c q ≤ c * q.1 := flr_le hq
  have hq2 : c * q.1 < (q.2 : Int) * flr c q + (q.2 : Int) := lt_flr hq
  -- 乘上另一个分母
  have a1 : (p.2 : Int) * flr c q * (q.2 : Int) ≤ c * p.1 * (q.2 : Int) :=
    Int.mul_le_mul_of_nonneg_right hp1 (Int.le_of_lt hq')
  have a2 : c * p.1 * (q.2 : Int) < ((p.2 : Int) * flr c q + (p.2 : Int)) * (q.2 : Int) :=
    Int.mul_lt_mul_of_pos_right hp2 hq'
  have b1 : (q.2 : Int) * flr c q * (p.2 : Int) ≤ c * q.1 * (p.2 : Int) :=
    Int.mul_le_mul_of_nonneg_right hq1 (Int.le_of_lt hp')
  have b2 : c * q.1 * (p.2 : Int) < ((q.2 : Int) * flr c q + (q.2 : Int)) * (p.2 : Int) :=
    Int.mul_lt_mul_of_pos_right hq2 hp'
  -- 统一成同样的单项式，再用 omega
  have e1 : (p.2 : Int) * flr c q * (q.2 : Int) = flr c q * ((p.2 : Int) * (q.2 : Int)) := by ring
  have e2 : ((p.2 : Int) * flr c q + (p.2 : Int)) * (q.2 : Int)
      = flr c q * ((p.2 : Int) * (q.2 : Int)) + (p.2 : Int) * (q.2 : Int) := by ring
  have e3 : (q.2 : Int) * flr c q * (p.2 : Int) = flr c q * ((p.2 : Int) * (q.2 : Int)) := by ring
  have e4 : ((q.2 : Int) * flr c q + (q.2 : Int)) * (p.2 : Int)
      = flr c q * ((p.2 : Int) * (q.2 : Int)) + (p.2 : Int) * (q.2 : Int) := by ring
  have e5 : c * (p.1 * (q.2 : Int) - q.1 * (p.2 : Int))
      = c * p.1 * (q.2 : Int) - c * q.1 * (p.2 : Int) := by ring
  have e6 : c * (q.1 * (p.2 : Int) - p.1 * (q.2 : Int))
      = c * q.1 * (p.2 : Int) - c * p.1 * (q.2 : Int) := by ring
  rw [e1] at a1
  rw [e2] at a2
  rw [e3] at b1
  rw [e4] at b2
  show c * (p.1 * (q.2 : Int) - q.1 * (p.2 : Int)) < (p.2 : Int) * (q.2 : Int) ∧
    c * (q.1 * (p.2 : Int) - p.1 * (q.2 : Int)) < (p.2 : Int) * (q.2 : Int)
  rw [e5, e6]
  constructor <;> omega

/-! ## LPO ⟹ BMCQ -/

/-- 精度 1/c 上第 n 项的读数减去第 0 项的读数，落到自然数。 -/
def readNat (c : Int) (x : Nat → Qp) (n : Nat) : Nat := (flr c (x n) - flr c (x 0)).toNat

theorem bmcQ_of_lpo (h : LPO) : BMCQ := by
  intro x hpos hmono hbound k
  obtain ⟨B, hB, hxB⟩ := hbound
  have hc : (0 : Int) ≤ (k : Int) + 1 := by omega
  have hy : MonoNat (readNat ((k : Int) + 1) x) := by
    intro m n hmn
    show (flr ((k : Int) + 1) (x m) - flr ((k : Int) + 1) (x 0)).toNat
      ≤ (flr ((k : Int) + 1) (x n) - flr ((k : Int) + 1) (x 0)).toNat
    apply Int.toNat_le_toNat
    have := flr_mono hc (hpos m) (hpos n) (hmono m n hmn)
    omega
  have hyB : ∀ n, readNat ((k : Int) + 1) x n
      ≤ (flr ((k : Int) + 1) B - flr ((k : Int) + 1) (x 0)).toNat := by
    intro n
    show (flr ((k : Int) + 1) (x n) - flr ((k : Int) + 1) (x 0)).toNat
      ≤ (flr ((k : Int) + 1) B - flr ((k : Int) + 1) (x 0)).toNat
    apply Int.toNat_le_toNat
    have := flr_mono hc (hpos n) hB (hxB n)
    omega
  obtain ⟨N, hN⟩ := natBMC_of_lpo h _ hy _ hyB
  refine ⟨N, fun m n hm hn => ?_⟩
  have h0m := flr_mono hc (hpos 0) (hpos m) (hmono 0 m (Nat.zero_le m))
  have h0n := flr_mono hc (hpos 0) (hpos n) (hmono 0 n (Nat.zero_le n))
  have hmn : readNat ((k : Int) + 1) x m = readNat ((k : Int) + 1) x n :=
    (hN m hm).trans (hN n hn).symm
  have em := Int.toNat_of_nonneg
    (show (0 : Int) ≤ flr ((k : Int) + 1) (x m) - flr ((k : Int) + 1) (x 0) by omega)
  have en := Int.toNat_of_nonneg
    (show (0 : Int) ≤ flr ((k : Int) + 1) (x n) - flr ((k : Int) + 1) (x 0) by omega)
  have hmn' : (((flr ((k : Int) + 1) (x m) - flr ((k : Int) + 1) (x 0)).toNat : Nat) : Int)
      = (((flr ((k : Int) + 1) (x n) - flr ((k : Int) + 1) (x 0)).toNat : Nat) : Int) :=
    congrArg (fun t : Nat => (t : Int)) hmn
  have hfl : flr ((k : Int) + 1) (x m) = flr ((k : Int) + 1) (x n) := by omega
  exact close_of_flr_eq (hpos m) (hpos n) hfl

/-! ## BMCQ ⟹ LPO：用 0/1 的有理数列 -/

/-- 开关序列看成 0/1 的有理数列，分母为 1。 -/
def bitQ (s : Nat → Bool) (n : Nat) : Qp := ((((s n).toNat : Nat) : Int), 1)

theorem limBit_of_bmcQ (h : BMCQ) : LimBit := by
  intro s hs
  have hmono : MonoQ (bitQ s) := by
    intro m n hmn
    have := monoNat_toNat hs m n hmn
    dsimp only at this
    show (((s m).toNat : Nat) : Int) * ((1 : Nat) : Int)
      ≤ (((s n).toNat : Nat) : Int) * ((1 : Nat) : Int)
    omega
  have hbound : BoundedQ (bitQ s) := by
    refine ⟨(1, 1), Nat.one_pos, fun n => ?_⟩
    have := toNat_le_one (s n)
    show (((s n).toNat : Nat) : Int) * ((1 : Nat) : Int) ≤ (1 : Int) * ((1 : Nat) : Int)
    omega
  obtain ⟨N, hN⟩ := h (bitQ s) (fun _ => Nat.one_pos) hmono hbound 0
  refine ⟨N, fun m hm => ?_⟩
  obtain ⟨h1, h2⟩ := hN m N hm (Nat.le_refl N)
  dsimp only [bitQ] at h1 h2
  apply bool_eq_of_toNat_eq
  omega

theorem lpo_of_bmcQ (h : BMCQ) : LPO := lpo_of_limBit (limBit_of_bmcQ h)

/-- C-425 的主定理：A 的有理数形态与 LPO 互推（不预设排中律）。 -/
theorem bmcQ_iff_lpo : BMCQ ↔ LPO := ⟨lpo_of_bmcQ, bmcQ_of_lpo⟩

theorem bmcQ_iff_limBit : BMCQ ↔ LimBit :=
  ⟨limBit_of_bmcQ, fun h => bmcQ_of_lpo (lpo_of_limBit h)⟩

/-! ## 对照：芝诺位置 1 − 2⁻ⁿ，柯西步由公式给出，不用 LPO -/

/-- 芝诺跑者第 n 步后的位置 1 − 2⁻ⁿ = (2ⁿ − 1)/2ⁿ。 -/
def zenoQp (n : Nat) : Qp := (((2 ^ n : Nat) : Int) - 1, 2 ^ n)

theorem zenoQp_pos (n : Nat) : 0 < (zenoQp n).2 := Nat.two_pow_pos n

theorem mono_aux {a b : Int} (hab : a ≤ b) : (a - 1) * b ≤ (b - 1) * a := by
  have e1 : (a - 1) * b = a * b - b := by ring
  have e2 : (b - 1) * a = a * b - a := by ring
  rw [e1, e2]
  omega

theorem zenoQp_mono : MonoQ zenoQp := by
  intro m n hmn
  have hp : 2 ^ m ≤ 2 ^ n := Nat.pow_le_pow_right (by decide) hmn
  show (((2 ^ m : Nat) : Int) - 1) * ((2 ^ n : Nat) : Int)
    ≤ (((2 ^ n : Nat) : Int) - 1) * ((2 ^ m : Nat) : Int)
  exact mono_aux (Int.ofNat_le.mpr hp)

theorem zenoQp_bounded : BoundedQ zenoQp :=
  ⟨(1, 1), Nat.one_pos, fun n => by
    show (((2 ^ n : Nat) : Int) - 1) * ((1 : Nat) : Int) ≤ (1 : Int) * ((2 ^ n : Nat) : Int)
    omega⟩

/-- 每一步都还没到 1。 -/
theorem zenoQp_lt_one (n : Nat) : QLt (zenoQp n) (1, 1) := by
  show (((2 ^ n : Nat) : Int) - 1) * ((1 : Nat) : Int) < (1 : Int) * ((2 ^ n : Nat) : Int)
  omega

/-- n ≥ k + 1 时 2ⁿ > k + 1。 -/
theorem two_pow_gt {k n : Nat} (h : k + 1 ≤ n) : ((k : Int) + 1) < ((2 ^ n : Nat) : Int) := by
  have h1 : k + 1 < 2 ^ (k + 1) := Nat.lt_two_pow_self
  have h2 : 2 ^ (k + 1) ≤ 2 ^ n := Nat.pow_le_pow_right (by decide) h
  omega

theorem cauchy_aux {c a b : Int} (hc : 0 ≤ c) (ha : 0 < a) (hb : c < b) :
    c * ((a - 1) * b - (b - 1) * a) < a * b := by
  have e : c * ((a - 1) * b - (b - 1) * a) = c * a - c * b := by ring
  have h1 : c * a < b * a := Int.mul_lt_mul_of_pos_right hb ha
  have h2 : 0 ≤ c * b := Int.mul_nonneg hc (by omega)
  have e2 : b * a = a * b := Int.mul_comm b a
  rw [e]
  rw [e2] at h1
  omega

/-- 柯西步由公式 k + 1 给出。 -/
theorem zenoQp_cauchy (k : Nat) :
    ∀ m n, k + 1 ≤ m → k + 1 ≤ n → CloseQ ((k : Int) + 1) (zenoQp m) (zenoQp n) := by
  intro m n hm hn
  have hc : (0 : Int) ≤ (k : Int) + 1 := by omega
  have hbm := two_pow_gt hm
  have hbn := two_pow_gt hn
  have ham : (0 : Int) < ((2 ^ m : Nat) : Int) := by omega
  have han : (0 : Int) < ((2 ^ n : Nat) : Int) := by omega
  show ((k : Int) + 1) * ((((2 ^ m : Nat) : Int) - 1) * ((2 ^ n : Nat) : Int)
        - (((2 ^ n : Nat) : Int) - 1) * ((2 ^ m : Nat) : Int))
        < ((2 ^ m : Nat) : Int) * ((2 ^ n : Nat) : Int) ∧
      ((k : Int) + 1) * ((((2 ^ n : Nat) : Int) - 1) * ((2 ^ m : Nat) : Int)
        - (((2 ^ m : Nat) : Int) - 1) * ((2 ^ n : Nat) : Int))
        < ((2 ^ m : Nat) : Int) * ((2 ^ n : Nat) : Int)
  refine ⟨cauchy_aux hc ham hbn, ?_⟩
  have h2 := cauchy_aux hc han hbm
  rw [Int.mul_comm ((2 ^ n : Nat) : Int) ((2 ^ m : Nat) : Int)] at h2
  exact h2

theorem zenoQp_cauchyQ : CauchyQ zenoQp := fun k => ⟨k + 1, zenoQp_cauchy k⟩

/-- 从第 k + 1 步起，离 1 小于 1/(k+1)：极限是 1，步数由公式给出。 -/
theorem zenoQp_to_one (k : Nat) :
    ∀ n, k + 1 ≤ n → CloseQ ((k : Int) + 1) (zenoQp n) (1, 1) := by
  intro n hn
  have hb := two_pow_gt hn
  show ((k : Int) + 1) * ((((2 ^ n : Nat) : Int) - 1) * ((1 : Nat) : Int)
        - (1 : Int) * ((2 ^ n : Nat) : Int)) < ((2 ^ n : Nat) : Int) * ((1 : Nat) : Int) ∧
      ((k : Int) + 1) * ((1 : Int) * ((2 ^ n : Nat) : Int)
        - (((2 ^ n : Nat) : Int) - 1) * ((1 : Nat) : Int)) < ((2 ^ n : Nat) : Int) * ((1 : Nat) : Int)
  constructor <;> omega

/-- 柯西步不能一律取第 0 步：精度 1/2 时，第 0 步（位置 0）与第 2 步（位置 3/4）相差 3/4。
负控制 NEG-002 的正面对应。 -/
theorem zeno_modulus_zero_false :
    ¬ ∀ k m n : Nat, CloseQ ((k : Int) + 1) (zenoQp m) (zenoQp n) := by
  intro h
  obtain ⟨_, h2⟩ := h 1 0 2
  revert h2
  decide

end GodelQ.TwoChoices
