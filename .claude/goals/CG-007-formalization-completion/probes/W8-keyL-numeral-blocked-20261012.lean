import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeH2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- `keyL` 的干净证法：**先 `show` 把 arity 写成 `0+1+1`**，再 `substs_rel`
lemma keyL : subst ℒₛₑₜ ((^#(0:V) : V) ∷ shiftVec (V := V) 2 1) (iVE (1:V) (^#(0:V) : V))
    = (^rel 2 (↑cEqN) (?[^#0, ^#2] : V) : V) := by
  have hs : shiftVec (V := V) 2 1 = (?[^#2] : V) := by
    rw [show (1 : V) = 0 + 1 by norm_num, shiftVec_succ, shiftVec_zero]
    rw [termBShiftVec_nil]
    rfl
  rw [iVE_bvar, eqAtom, hs]
  -- 先把 `^#(0+1)` 归一成 `^#1`
  rw [show (0 : V) + 1 = 1 by norm_num]
  rw [show ((^#(0:V) : V) ∷ (?[^#2] : V)) = ((^#0 : V) ∷ ((^#2 : V) ∷ (0 : V))) from rfl]
  -- 目标里 arity 是 `2`；`substs_rel` 的 `k` 是元变量，应能统一。
  -- 若失败，改成显式 `k := 2` 并先 `show` 成同样的 numeral 形式。
  show subst ℒₛₑₜ ((^#(0:V) : V) ∷ ((^#(2:V) : V) ∷ (0 : V)))
      (^rel (2:V) (↑cEqN) ((^#(0:V) : V) ∷ ((^#(1:V) : V) ∷ (0 : V))))
    = ^rel (2:V) (↑cEqN) ((^#(0:V) : V) ∷ ((^#(2:V) : V) ∷ (0 : V)))
  -- `substs_rel` 的第三个参数是 `v`（被代入的向量，即 `^#0 ∷ ^#1 ∷ 0`），
  -- 而 subst 的向量 `w` 由目标给出。故 `hv` 要证的是 `v` 的项向量性。
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (k := (2:V))
    (v := ((^#(0:V) : V) ∷ ((^#(1:V) : V) ∷ (0 : V))))
    (by rw [cEqN]; exact codeIn_rel_quote _)
    (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (1:V))))
      (IsUTerm.bvar (z := (0:V))))]
  congr 1
  rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0 : V)) from rfl]
  rw [show (0 : V) + 1 + 1 = 2 by norm_num]
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (1:V))),
    termSubst_bvar, termSubst_bvar]
  rfl

end GodelQ.ProbeH2
