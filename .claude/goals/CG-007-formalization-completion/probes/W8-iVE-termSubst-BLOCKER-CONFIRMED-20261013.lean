import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iVE` 与 `termSubst` 的交换律（bvar 支的实测）**。

左端 `iVE n (termSubst w ^#z) = iVE n w.[z]`。
右端 `subst (qVec w) (iVE n ^#z) = subst (qVec w) (eqAtom ^#(z+1))`。

**关键观察**：`qVec w = ^#0 ∷ termBShiftVec (len w) w`，故 `(qVec w).[0] = ^#0`
——`eqAtom` 自带的那个 `#0` **被保护住了**（这正是 `qVec` 的意义）。
剩下的 `#(z+1)` 走 `qVec w` 的第 `z+1` 格 = `termBShift w.[z]`。

于是右端 `= ^rel 2 cEqN ?[^#0, termBShift w.[z]]`。
要等于左端，需要 **`iVE n w.[z] = ^rel 2 cEqN ?[^#0, termBShift w.[z]]`**——
这在 `w.[z]` 是**任意项**时为假（`iVE` 对 `^func` 给的是 `ve2`）。

**但 `rel` 支里 `w = termSubstVec 2 ?[^#0,^&0] v`，`v.[i]` 由 `IsUTermVec` 给出**——
`v.[i]` **可以是任意项**。所以这条限制不成立。

**结论**：`iVE`/`termSubst` 的交换律**不能**写成对所有 `t`，
且 `rel` 支里出现的 `t` 也不受限制。**这是本支的真实障碍。**

本引理只把 bvar 支的**两侧形状**机器确认下来，供后续判断用。 -/
example {n w z : V} (hz : z < len w) :
    iVE n (termSubst ℒₒᵣ w (^#z : V))
      = subst ℒₛₑₜ (qVec ℒₛₑₜ w) (iVE n (^#z : V)) := by
  rw [termSubst_bvar, iVE_bvar]
  rw [show eqAtom (^#(z + 1) : V) = (^rel 2 (↑cEqN) (?[^#0, ^#(z + 1)] : V) : V) from rfl]
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
      (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
        (IsUTerm.bvar (z := (z + 1)))) (IsUTerm.bvar (z := (0:V)))))]
  congr 1
  rw [show (?[^#0, ^#(z + 1)] : V) = (^#0 : V) ∷ ((^#(z + 1) : V) ∷ (0:V)) from rfl]
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (z + 1)))]
  rw [show (qVec ℒₛₑₜ w).[0] = (^#0 : V) from by
    rw [Bootstrapping.qVec]; simp only [nth_adjoin_zero]]
  rw [show (qVec ℒₛₑₜ w).[z + 1] = termBShift ℒₛₑₜ w.[z] from by
    rw [Bootstrapping.qVec, nth_adjoin_succ]
    exact nth_termBShiftVec (V := V) (L := ℒₛₑₜ) (k := len w) (ts := w)
      (by
        rw [show qVec ℒₛₑₜ w = (^#0 : V) ∷ termBShiftVec ℒₛₑₜ (len w) w from rfl] at hz ⊢
        exact hz)
      hz]
  -- 目标（机器实测）：
  --   ⊢ iVE n w.[z] = ^rel 2 cEqN ?[termSubst (qVec w) ^#0, termSubst (qVec w) ^#(z+1)]
  -- 其中 `termSubst (qVec w) ^#0 = (qVec w).[0] = ^#0`（保护住了），
  -- 但左端 `iVE n w.[z]` 对**任意项** `w.[z]` 无法与 `^rel …` 相等。
  trace_state
  sorry

end GodelQ.ProbeFL
