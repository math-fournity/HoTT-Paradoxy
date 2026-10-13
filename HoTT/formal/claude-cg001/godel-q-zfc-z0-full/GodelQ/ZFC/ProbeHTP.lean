import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeHExsTP
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ### hExs 的 `t'`：由 `iT 0 (substs1 ℒᵣ t p)` 的**实际值**反推

取最简 `p = ^rel 2 cEqN ?[^#0, ^#1]`（层 1），`t = ^&0`。

**LHS**：
```
substs1 ℒᵣ ^&0 p = subst ℒᵣ ?[^&0] p
  = ^rel 2 cEqN (termSubstVec 2 ?[^&0] ?[^#0, ^#1])   -- substs_rel
  = ^rel 2 cEqN ?[^&0, ^&0]                              -- termSubstVec_cons₂ ×2
iT 0 (^rel 2 cEqN ?[^&0, ^&0]) = iTR 0 2 cEqN ?[^&0, ^&0]
  = qqAlls (imp ℒₜ (conjunct 2 0 0 (iVE 0 ^&0) ⋏ (conjunct 2 0 1 (iVE 0 ^&0) ⋏ ⊤))
              (subst ℒₜ ?[^#0,^#1] (cRel cEqN))) 2
```

**所以 RHS 应是** `substs1 ℒₜ t' (iT 1 p)`，其中
`iT 1 p = qqAlls (imp ℒₜ (conjunct 2 1 0 (iVE 1 ^#0) ⋏ (conjunct 2 1 1 (iVE 1 ^#1) ⋏ ⊤))
                  (subst ℒₜ ?[^#0,^#1] (cRel cEqN))) 2`

**关键观察**：两边都是 `qqAlls · 2`，层的差别在 `conjunct 2 n i (...)` 的 `n`。
LHS 的 `conjunct` 已经用了 `n=0` 与代入后的 `^&0`；
RHS 的 `conjunct` 用的是 `n=1` 与未代入的 `^#0`/`^#1`，要靠 `subst'` 把 `#0 ↦ ^&0` 补上。

**先做一步可证的：LHS 的 `substs_rel` + `termSubstVec`。** -/

-- 第一步：substs1 → subst ?[^&0]（def-eq），再 substs_rel
example : substs1 ℒₒᵣ (^&(0:V) : V))
      ((^rel (0+1+1) (↑cEqN) ((?[^#0, ^#(0+1)] : V)) : V)
    = ((^rel (0+1+1) (↑cEqN)
        (termSubstVec ℒₒᵣ (0+1+1) ((?[^&0] : V)) ((?[^#0, ^#(0+1)] : V)))) : V) := by
  have hR : (ℒₒᵣ).IsRel (0+1+1) (↑cEqN) := by
    rw [show (0:V) + 1 + 1 = 2 by norm_num, cEqN]; exact codeIn_rel_quote _
  have hv : IsUTermVec ℒₒᵣ (0+1+1) ((^#0 : V) ∷ ((^#(0+1) : V) ∷ (0 : V))) :=
    IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (0:V))))
      (IsUTerm.bvar (z := (0+1:V)))
  show subst ℒₒᵣ ((?[^&0] : V)) ((^rel (0+1+1) (↑cEqN) ((?[^#0, ^#(0+1)] : V))) : V)) = _
  rw [Bootstrapping.substs_rel hR hv]

-- 第二步：termSubstVec 逐分量算出来
example : substs1 ℒₒᵣ (^&(0:V) : V))
      ((^rel (0+1+1) (↑cEqN) ((?[^#0, ^#(0+1)] : V)) : V)
    = ((^rel (0+1+1) (↑cEqN) ((?[^&0, ^&0] : V)) : V) := by
  have hR : (ℒₒᵣ).IsRel (0+1+1) (↑cEqN) := by
    rw [show (0:V) + 1 + 1 = 2 by norm_num, cEqN]; exact codeIn_rel_quote _
  have hv : IsUTermVec ℒₒᵣ (0+1+1) ((^#0 : V) ∷ ((^#(0+1) : V) ∷ (0 : V))) :=
    IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (0:V))))
      (IsUTerm.bvar (z := (0+1:V)))
  show subst ℒₒᵣ ((?[^&0] : V)) ((^rel (0+1+1) (↑cEqN) ((?[^#0, ^#(0+1)] : V))) : V)) = _
  rw [Bootstrapping.substs_rel hR hv]
  congr 1
  rw [show ((?[^#0, ^#(0+1)] : V)) = ((^#0 : V) ∷ ((^#(0+1) : V) ∷ (0 : V))) from rfl,
    show (0 : V) + 1 + 1 = 2 by norm_num,
    termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (0+1:V))),
    termSubst_bvar, termSubst_bvar]
  sorry

end GodelQ.ProbeHExsTP
