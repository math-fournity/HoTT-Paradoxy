import Mathlib.Data.Rat.Floor
import GodelQ.TwoChoices.Core

/-!
# 芝诺序列的有理数一侧：显式的收敛步，以及与整数读数的对应（CG001-C-419 的桥）

`Core.lean` 在整数刻度上证明了：芝诺过程在精度 `2⁻ᵏ` 上的读数 `zenoReading k n` 从第 `k` 步起落定，
落定的步由公式给出，不需要 LPO。本文件把它接回有理数：

* `zenoQ n = 1 - (1/2)ⁿ` 是芝诺跑者第 `n` 步后的位置；
* `zenoReading_eq_floor`：`zenoReading k n = ⌊2ᵏ · zenoQ n⌋`，整数读数确实是有理数位置的读数；
* `zenoQ_close`：从第 `k` 步起离 1 不超过 `(1/2)ᵏ`；`zenoQ_cauchy`：柯西步由公式 `N(k) = k + 1`
  给出；`zenoQ_lt_one`：每一步都小于 1。

**身份**：本文件是经典的。Mathlib 的 ℚ 本身的序与域结构依赖 `Classical.choice`（例如
`Rat.le_total`、`Rat.instField`；`QualificationTC.lean` 的审计机器核对了这一点），所以这里的
定理不能作构造性的证据，只作“整数读数忠实于有理数位置”的桥。“极限是 1 不需要 A”的内容在于
收敛步是公式（`k`、`k + 1`），不是搜索出来的；这一点从命题的形状就看得见，与证明用不用经典公理
无关。构造性的部分（整数读数）在 `Core.lean`，由审计断言不依赖 `Classical.choice`。

“有界单调的有理数列都收敛 ⟺ LPO”这一实数形态，本包没有做构造性的机器证明：它要一套不依赖
`Classical.choice` 的有理数。它由整数刻度形态（C-418 的 `NatBMC`）在每个精度上取地板函数得到，
这一步是初等的；文献中的陈述见 `CLAIM.md` §5。
-/

namespace GodelQ.TwoChoices

/-- 芝诺跑者第 `n` 步后的位置。 -/
def zenoQ (n : ℕ) : ℚ := 1 - (1 / 2) ^ n

/-- 有理数列的柯西性：每个精度 `1/(k+1)` 都有一步，此后两两相差小于它。 -/
def CauchyQ (x : ℕ → ℚ) : Prop :=
  ∀ k : ℕ, ∃ N, ∀ m n, N ≤ m → N ≤ n → |x m - x n| < 1 / ((k : ℚ) + 1)

theorem abs_lt_of_both {a c : ℚ} (h1 : a < c) (h2 : -a < c) : |a| < c :=
  abs_lt.mpr ⟨by linarith, h1⟩

theorem half_pow_pos (n : ℕ) : (0 : ℚ) < (1 / 2) ^ n := pow_pos (by norm_num) n

theorem half_pow_anti {m n : ℕ} (h : m ≤ n) : ((1 : ℚ) / 2) ^ n ≤ (1 / 2) ^ m :=
  pow_le_pow_of_le_one (by norm_num) (by norm_num) h

theorem zenoQ_lt_one (n : ℕ) : zenoQ n < 1 := by
  unfold zenoQ
  have := half_pow_pos n
  linarith

theorem zenoQ_mono : Monotone zenoQ := by
  intro m n hmn
  unfold zenoQ
  have := half_pow_anti hmn
  linarith

/-- 显式的收敛步：从第 `k` 步起，离 1 不超过 `(1/2)ᵏ`。 -/
theorem zenoQ_close (k m : ℕ) (h : k ≤ m) : 1 - zenoQ m ≤ (1 / 2) ^ k := by
  unfold zenoQ
  have := half_pow_anti h
  linarith

theorem half_pow_le_inv_succ (k : ℕ) : ((1 : ℚ) / 2) ^ k ≤ 1 / ((k : ℚ) + 1) := by
  induction k with
  | zero => norm_num
  | succ k ih =>
    have hk : (0 : ℚ) ≤ (k : ℚ) := Nat.cast_nonneg k
    rw [pow_succ]
    calc ((1 : ℚ) / 2) ^ k * (1 / 2) ≤ 1 / ((k : ℚ) + 1) * (1 / 2) := by
          apply mul_le_mul_of_nonneg_right ih (by norm_num)
      _ ≤ 1 / (((k + 1 : ℕ) : ℚ) + 1) := by
          rw [div_mul_div_comm, one_mul, div_le_div_iff₀ (by linarith) (by push_cast; linarith)]
          push_cast
          linarith

/-- 芝诺序列是柯西列，收敛步由公式 `N(k) = k + 1` 给出。 -/
theorem zenoQ_cauchy : CauchyQ zenoQ := by
  intro k
  refine ⟨k + 1, fun m n hm hn => ?_⟩
  have hm1 := zenoQ_close (k + 1) m hm
  have hn1 := zenoQ_close (k + 1) n hn
  have hm2 := zenoQ_lt_one m
  have hn2 := zenoQ_lt_one n
  have hb := half_pow_le_inv_succ (k + 1)
  have hstep : (1 : ℚ) / (((k + 1 : ℕ) : ℚ) + 1) < 1 / ((k : ℚ) + 1) := by
    have hk : (0 : ℚ) ≤ (k : ℚ) := Nat.cast_nonneg k
    rw [div_lt_div_iff₀ (by push_cast; linarith) (by linarith)]
    push_cast
    linarith
  apply abs_lt_of_both <;> linarith

theorem two_pow_mul_half_pow (a b : ℕ) : (2 : ℚ) ^ (a + b) * (1 / 2) ^ a = 2 ^ b := by
  rw [pow_add, mul_comm ((2 : ℚ) ^ a) _, mul_assoc, ← mul_pow]
  norm_num

theorem two_pow_mul_half_pow' (a b : ℕ) : (2 : ℚ) ^ a * (1 / 2) ^ (a + b) = (1 / 2) ^ b := by
  rw [pow_add, ← mul_assoc, ← mul_pow]
  norm_num

/-- 读数对应：`zenoReading k n = ⌊2ᵏ · zenoQ n⌋`。 -/
theorem zenoReading_eq_floor (k n : ℕ) :
    ((zenoReading k n : ℕ) : ℤ) = ⌊(2 : ℚ) ^ k * zenoQ n⌋ := by
  unfold zenoReading zenoQ
  rcases Nat.le_total n k with h | h
  · obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le h
    have hsub : n + d - n = d := by omega
    rw [hsub]
    have hle : 2 ^ d ≤ 2 ^ (n + d) := Nat.pow_le_pow_right (by norm_num) (by omega)
    have hval : (2 : ℚ) ^ (n + d) * (1 - (1 / 2) ^ n) = ((2 ^ (n + d) - 2 ^ d : ℕ) : ℚ) := by
      rw [Nat.cast_sub hle]
      push_cast
      rw [mul_sub, mul_one, two_pow_mul_half_pow]
    rw [hval, Int.floor_natCast]
  · obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le h
    have hsub : k - (k + d) = 0 := by omega
    rw [hsub, pow_zero]
    have hpos : 1 ≤ 2 ^ k := Nat.one_le_two_pow
    have hv : (2 : ℚ) ^ k * (1 - (1 / 2) ^ (k + d)) = 2 ^ k - (1 / 2) ^ d := by
      rw [mul_sub, mul_one, two_pow_mul_half_pow']
    rw [hv, eq_comm, Int.floor_eq_iff]
    have hd1 : (0 : ℚ) < (1 / 2) ^ d := pow_pos (by norm_num) d
    have hd2 : ((1 : ℚ) / 2) ^ d ≤ 1 := pow_le_one₀ (by norm_num) (by norm_num)
    push_cast [Nat.cast_sub hpos]
    constructor <;> linarith

end GodelQ.TwoChoices

#print axioms GodelQ.TwoChoices.zenoQ_lt_one
#print axioms GodelQ.TwoChoices.zenoQ_mono
#print axioms GodelQ.TwoChoices.zenoQ_close
#print axioms GodelQ.TwoChoices.zenoQ_cauchy
#print axioms GodelQ.TwoChoices.zenoReading_eq_floor
