import GodelQ.ZFC.ShCraigElimSetupQ

/-! ## `hExs` 核心等式的判定性一步：`subst ?[^&0]` 过两层量词后变成 `qVec²`（2026-10-13）

### 已机器验证（exit 0）

```
substs_qqAlls_two (X : V) (hX : IsUFormula ℒₜ X) :
  subst ℒₜ ?[^&0] (qqAlls X 2) = qqAlls (subst ℒₜ ?[^#0, ^#1, ^&0] X) 2
```

**这条把此前两件事接上了**：

1. 先前探针 `W8-qVec2-atomic-rename-20261012` 验证了**原子层**的换名在 `qVec²` 形状下成立：
   `subst ?[^#0,^#1,^&0] (^rel 2 cEqN ?[^#0,^#2]) = ^rel 2 cEqN ?[^#0,^&0]`。
2. 本轮证明：**要过两层 `qqAlls` 就必须用 `qVec²` 这个向量**——不是可选的美化，是 `substs_qqAlls` 的强制产物。

所以 `iT` 的 rel 支（`iTR = qqAlls (...) 2`）与 `substs1` 的相容律，
**正确的中间形状就是 `qVec²`**。这正面回答了一直含混的问题：
`qVec²` 不是外推出来的猜想，是 `subst` 推过两层绑定后的必然形式。

### 对 hAll / hExs 的意义

`hExs` 的核心 `iT n (substs1 ℒᵣ t p) = substs1 ℒₜ X (iT n p)` 中，
`iT n p` 的 rel 子式是 `qqAlls ... 2`，所以 RHS 的 `substs1` 作用上去会强制长出 `qVec²`。
LHS 的 `substs1 ℒᵣ t p = subst ℒᵣ ?[t] p` 只改 bvar、层数不变。
**两边要相等，向量必须按 `substs_qqAlls` 的规则逐层长**——这正是 rel 支数学的内容。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeQQ2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 已证：subst ?[^&0] 过两层 qqAlls 强制成长为 qVec²
example (X : V) (hX : IsUFormula ℒₛₑₜ X) :
    subst ℒₛₑₜ ((?[^&0] : V)) (qqAlls X 2)
      = qqAlls (subst ℒₛₑₜ ((?[^#0, ^#1, ^&0] : V)) X) 2 := by
  exact substs_qqAlls_two hX

-- 原子层换名（先前探针的结论，此处一并复核）
example : subst ℒₛₑₜ ((?[^#0, ^#1, ^&0] : V))
      (^rel (0 + 1 + 1) (↑cEqN) ((?[^#0, ^#2] : V)))
    = (^rel (0 + 1 + 1) (↑cEqN) ((?[^#0, ^&0] : V)) : V) := by
  have hv : IsUTermVec ℒₛₑₜ (0 + 1 + 1) ((^#0 : V) ∷ ((^#2 : V) ∷ (0 : V))) :=
    IsUTermVec.adjoin
      (IsUTermVec.adjoin (IsUTermVec.empty (L := ℒₛₑₜ) (V := V)) (IsUTerm.bvar (z := (2:V))))
      (IsUTerm.bvar (z := (0:V)))
  have hR : (ℒₛₑₜ).IsRel (0 + 1 + 1) (↑cEqN : V) := by
    rw [show (0:V) + 1 + 1 = 2 by norm_num, cEqN]
    exact codeIn_rel_quote _
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) hR (by simpa using hv)]
  congr 1
  rw [show ((?[^#0, ^#2] : V)) = ((^#0 : V) ∷ ((^#2 : V) ∷ (0 : V))) from rfl,
    show (0 : V) + 1 + 1 = 2 by norm_num,
    termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (2:V))),
    termSubst_bvar, termSubst_bvar]
  simp

end GodelQ.ProbeQQ2
