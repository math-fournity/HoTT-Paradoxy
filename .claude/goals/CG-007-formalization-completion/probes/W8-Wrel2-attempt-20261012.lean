import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeWrel2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `subst W (^rel 2 cEqN ?[^#0,^#2]) = ^rel 2 cEqN ?[^#0,^&0]`（`W = ?[^#0,^#1,^&0]`）

思路：把 `W` 与 `?[^#0,^#2]` 都写成 `∷` 形式，用 `substs_rel` 剥到 rel，
再用 `termSubstVec_cons₂` 逐分量算（下标 0、1 都 < 3）。
numeral 一律先 `norm_num` 归到 `0+1+1` 形式。 -/

lemma Wrel2 : subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V)
    (^rel 2 (↑cEqN) (?[^#0, ^#2] : V)) = (^rel 2 (↑cEqN) (?[^#0, ^&0] : V) : V) := by
  -- witness：W 是层 3、长度 3 的项向量。
  -- `cons_iff : IsSemitermVec L (k+1) n (t ∷ w) ↔ IsSemiterm L n t ∧ IsSemitermVec L k n w`
  -- 三次 cons：`(^#0 ∷ (^#1 ∷ (^&0 ∷ 0)))`，Base case 是 empty（长度 0）
  have hW : IsSemitermVec ℒₛₑₜ 3 3 ((^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0 : V)))) := by
    rw [show (3 : V) = 0 + 1 + 1 + 1 by norm_num]
    rw [IsSemitermVec.cons_iff, IsSemitermVec.cons_iff, IsSemitermVec.cons_iff]
    exact ⟨IsSemiterm.fvar (V := V) (n := 3) 0, IsSemiterm.bvar.mpr (by norm_num : (1:V) < 3),
      IsSemiterm.bvar.mpr (by norm_num : (0:V) < 3), IsSemitermVec.empty (L := ℒₛₑₜ) (V := V) (3 : V)⟩
  have hW' : IsSemitermVec ℒₛₑₜ 3 3 (?[^#0, ^#1, ^&0] : V) := by
    rw [show (?[^#0, ^#1, ^&0] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0 : V))) from rfl]
    exact hW
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _) (by simpa using hW')]
  congr 1
  -- 现在目标：`termSubstVec 3 W ?[^#0,^#2] = ?[^#0,^&0]`
  -- 全部展开成 ∷ 形式，numeral 归一
  rw [show (?[^#0, ^#1, ^&0] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0 : V))) from rfl]
  rw [show (?[^#0, ^#2] : V) = (^#0 : V) ∷ ((^#(0 + 1 + 1) : V) ∷ (0 : V)) from rfl]
  -- 长度归一到 cons₂ 需要的 `2` 形式放在其后
  --（termSubstVec_cons₂ 的模式是 `termSubstVec L (k+1) w (t ∷ ts)`）
  rw [show (0 : V) + 1 + 1 = (2:V) by norm_num]
  rw [show (?[^#0, ^&0] : V) = (^#0 : V) ∷ ((^&0 : V) ∷ (0 : V)) from rfl]
  -- 目标是 `termSubstVec 2 W ?[^#0,^#2]`（长度 2）
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (2:V))),
    termSubst_bvar, termSubst_bvar, nth_adjoin_zero]
  -- 剩：`(^#0 ∷ ^#1 ∷ ^&0 ∷ 0).[2] = ^&0`
  rw [nth_adjoin_two, nth_adjoin_one, nth_adjoin_zero]

end GodelQ.ProbeWrel2
