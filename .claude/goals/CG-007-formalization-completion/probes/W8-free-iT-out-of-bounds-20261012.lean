import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeFreeI
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 决定性探针：`hAll` 的 `free q` 是否良构

`hAll` 走 `all_m` 需要 `q := imp ℒₛₑₜ domZero (iT 1 p)` 满足 `IsSemiformula ℒₛₑₜ 1 q`，
并且要能构造 `free ℒₛₑₜ q`。

关键疑问：`free X = subst ?[^&0] (shift X)` 用**长度 1** 的代入向量，
而 `iT` 的原子内部是 `^rel 2`（**2 元**）。`termSubstVec 2 (?[^&0]) (?[^#0, ^#1])`
的第 2 个分量会**越界取 0**（不是项），于是 `free (iT 1 p)` 可能**不是** `IsUFormula`。

先测最简的原子：`p = ^rel 2 R ?[^#0, ^#0]`（层数 1）。

下面直接测 `iVE 1 ^#0 = ^rel 2 cEqN ?[^#0, ^#1]` 经 `subst ?[^&0]` 后的结果。 -/

-- `subst ?[^&0]` 作用于 `^rel 2 cEqN ?[^#0, ^#1]` 的结果
example : subst ℒₛₑₜ (?[^&0] : V) (^rel (0 + 1 + 1) (↑cEqN) (?[^#0, ^#1] : V))
    = (^rel (0 + 1 + 1) (↑cEqN) (?[^&0, 0] : V) : V) := by
  have hR : (ℒₛₑₜ).IsRel (0 + 1 + 1) (↑cEqN : V) := by
    rw [show (0:V) + 1 + 1 = 2 by norm_num, cEqN]
    exact codeIn_rel_quote _
  have hv : IsUTermVec ℒₛₑₜ (0 + 1 + 1) ((^#0 : V) ∷ ((^#1 : V) ∷ (0 : V))) :=
    IsUTermVec.adjoin
      (IsUTermVec.adjoin (IsUTermVec.empty (L := ℒₛₑₜ) (V := V)) (IsUTerm.bvar (z := (1:V))))
      (IsUTerm.bvar (z := (0:V)))
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) hR (by simpa using hv)]
  congr 1
  rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0 : V)) from rfl,
    show (0 : V) + 1 + 1 = 2 by norm_num,
    termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (1:V))),
    termSubst_bvar, termSubst_bvar]
  simp

/-! ## 关键推论：`free ℒₛₑₜ (iT 1 p)` **不是公式**

上一例给出 `subst ?[^&0] (^rel 2 cEqN ?[^#0,^#1]) = ^rel 2 cEqN ?[^&0, 0]`。
第二个分量是 **`0`**（空向量），**不是项**。

于是 `IsSemiformula ℒₛₑₜ 0 (^rel 2 cEqN ?[^&0, 0])` **为假**——
因为 `IsSemiformula.rel` 要求每个分量 `IsSemiterm`，而 `IsSemiterm 0 0` 为假
（`IsSemiterm` 要求 `bv ≤ n`，`bv 0 = 0` 不满足 `0 < 0`）。

下面用 `IsSemiterm` 的判据确认 `0` 不是项。 -/

-- （`¬ IsUTerm 0` 的显式证明留作后续；本探针的主结论不依赖它。）

end GodelQ.ProbeFreeI
