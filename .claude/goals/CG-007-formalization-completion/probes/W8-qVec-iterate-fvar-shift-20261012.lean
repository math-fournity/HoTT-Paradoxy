import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeAC
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 干净解法：把 `subst` 推过 `qqAlls` 写成**递归引理**，全程 `k+1`

反复失败的原因是「多处 numeral + `qqAlls_succ` 要 `k+1`」互相牵制。
**绕开办法**：把这条推入写成**对 `k` 的递归引理**，陈述里只有 `k + 1`，
没有字面量 `2`；用 `Nat` 归纳，每步只出现一次 `k+1`。 -/

/-- `subst` 推过 `qqAlls`：`subst w (qqAlls X k) = qqAlls (subst ((qVec L)^[k] w) X) k`。 -/
lemma substs_qqAlls : ∀ (k : ℕ) (X w : V), IsUFormula ℒₛₑₜ X →
    subst ℒₛₑₜ w (qqAlls X (k : V))
      = qqAlls (subst ℒₛₑₜ ((qVec ℒₛₑₜ)^[k] w) X) (k : V) := by
  intro k
  induction k with
  | zero =>
    intro X w _
    simp
  | succ j ih =>
    intro X w hX
    rw [show ((j + 1 : ℕ) : V) = (j : V) + 1 by push_cast; ring]
    rw [qqAlls_succ]
    have hu : IsUFormula ℒₛₑₜ (qqAlls X (j : V)) := isUFormula_qqAlls.mpr hX
    rw [Bootstrapping.substs_all (L := ℒₛₑₜ) hu]
    rw [ih X (qVec ℒₛₑₜ w) hX]
    rw [qqAlls_succ]
    -- 目标：`^∀ qqAlls (subst ((qVec)^[j] (qVec w)) X) j
    --      = ^∀ qqAlls (subst ((qVec)^[j+1] w) X) j`
    congr 3

/-! ## 用 `substs_qqAlls` 收 `iT_free` 的原子情形 -/

example {R : V} (hR : (ℒₒᵣ).IsRel 2 R) :
    iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 R (?[^#0, ^#0] : V)))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) (^rel 2 R (?[^#0, ^#0] : V))) := by
  have hbB : IsSemiterm ℒₒᵣ 1 (^#(0:V) : V) := IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1)
  have hvB : IsSemitermVec ℒₒᵣ 2 1 (?[^#0, ^#0] : V) := IsSemitermVec.doubleton.mpr ⟨hbB, hbB⟩
  have htv : termSubstVec ℒₒᵣ 2 (?[^&0] : V) (?[^#0, ^#0] : V) = (?[^&0, ^&0] : V) := by
    rw [show (?[^#0, ^#0] : V) = (^#0 : V) ∷ ((^#0 : V) ∷ (0 : V)) from rfl]
    rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (0:V)))]
    simp only [termSubst_bvar, nth_adjoin_zero]
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hvB.isUTerm, htv]
  rw [iT_rel (V := V) (n := (0 : V)) (k := (2 : V)) (R := R)
    (v := (?[^&0, ^&0] : V)) hR
    (IsSemitermVec.doubleton.mpr ⟨IsSemiterm.fvar (n := 1) 0, IsSemiterm.fvar (n := 1) 0⟩).isUTerm]
  rw [iT_rel (V := V) (n := (1 : V)) (k := (2 : V)) (R := R)
    (v := (?[^#0, ^#0] : V)) hR hvB.isUTerm]
  simp only [iTR]
  -- 右侧：用 `substs_qqAlls` 把 `subst` 推过 `qqAlls · 2`
  rw [show (2 : V) = ((2 : ℕ) : V) by norm_num]
  rw [substs_qqAlls (2 : ℕ) _ (?[^&0] : V) (by sorry)]
  -- 剥掉 `qqAlls`，比较内层体
  congr 1
  -- 化简两侧的 `.[0]`/`.[1]`
  rw [show (?[^&0, ^&0] : V) = (^&(0:V) : V) ∷ ((^&(0:V) : V) ∷ (0 : V)) from rfl,
    show (?[^#0, ^#0] : V) = (^#(0:V) : V) ∷ ((^#(0:V) : V) ∷ (0 : V)) from rfl]
  simp only [nth_adjoin_zero, nth_adjoin_one]
  -- 先只算 `(qVec)^[2] ?[^&0]` 到底是什么（用 `rfl` 探）
  rw [show (qVec ℒₛₑₜ)^[2] (?[^&0] : V) = (?[^#0, ^#1, ^&1] : V) from by
    rw [show (2 : ℕ) = 1 + 1 from rfl, Function.iterate_succ_apply',
      Function.iterate_one]
    rw [show qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) from by
      rw [qVec, show len (?[^&0] : V) = 1 from by simp]
      rw [show termBShiftVec ℒₛₑₜ 1 (?[^&0] : V) = (?[^&0] : V) from by
        rw [show (1 : V) = 0 + 1 by norm_num,
          termBShiftVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty, termBShift_fvar,
          termBShiftVec_nil]]
      rfl]
    rw [qVec, show len (?[^#0, ^&0] : V) = 2 from by simp]
    rw [show termBShiftVec ℒₛₑₜ 2 (?[^#0, ^&0] : V) = (?[^#1, ^&1] : V) from by
      rw [show (2 : V) = 1 + 1 by norm_num,
        termBShiftVec_cons (IsUTerm.bvar (z := (0:V)))
          (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.fvar (x := (0:V)))),
        termBShift_bvar, termBShift_fvar,
        termBShiftVec_cons₁ (IsUTerm.fvar (x := (0:V))), termBShift_fvar]
      rfl]
    rfl]
  exact absurd rfl (by simp)
end GodelQ.ProbeAC
