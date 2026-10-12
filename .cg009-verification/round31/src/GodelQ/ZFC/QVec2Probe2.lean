-- CG-009: probe the exact index range of the conjunct vector at mm+1.
import GodelQ.ZFC.QVec2Probe

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.QVec2Probe2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11 GodelQ.IVEOpenFunc12

-- the conjunct vector at n = mm+1: ^#i ∷ shiftVec 3 (mm+1), length mm+2
-- its entries: index 0 = ^#i, index j+1 = ^#(3+j) for j < mm+1
-- so max index used = 3 + (mm+1-1) = mm+3, and length = mm+2.

example (mm : V) : len ((^#0 : V) ∷ shiftVec 3 (mm + 1)) = mm + 2 := by
  have h := isSemitermVec_shiftVec_V 3 (mm + 1)
  rw [len_adjoin, h.lh]
  ring

-- The qVec^2 conjunct law needed by the func branch of `iVE_open`:
-- `subst (QvecV mm) (conjunct 3 mm i y) = conjunct 3 mm i y`.
-- Inside `ve2`'s `qqAlls … 2`, `subst (QvecV mm)` descends two binders, so the
-- conjunct sees `qVec^2 (QvecV mm) = QvecV (mm+2)`.  `QvecV (mm+2)` has length
-- `mm+3` and is the identity on `0..mm+1`; the conjunct's own vector
-- `^#i ∷ shiftVec 3 mm` has length `mm+1` and reads only indices `0..mm-1`
-- plus the head `i`, all `< mm+2`.  Hence both substituted subformulas are fixed.
/-!
## 结论：为什么 `subst (QvecV mm) (conjunct 3 mm i y)` 不能直接消掉

`conjunct` 的两条代入向量分别是 `?[^#i]`（长度 1）与 `^#i ∷ shiftVec 3 mm`
（长度 `mm+1`，最大索引 `3 + mm - 1 = mm+2`）。
`substs_substs` 要求**内层**向量 `v` 的层数 = **外层**向量 `w` 的长度，
所以外层若是 `QvecV mm`（长度 `mm+1`），内层就得到层 `mm+1`，
`isSemitermVec_single_bvar` 就要求 `i < mm+1`——但 `i` 可以是 `mm+2`。
所以这条 direct 路线**不成立**。

正确路线：`ve2` 的体外面套着 `qqAlls … 2`。`subst` 穿过一个 `qqAlls`
要把 `w` 换成 `qVec w`（Foundation `substs_all`）。穿过两个后
`qVec² (QvecV mm) = QvecV (mm+2)`（`QvecV_succ` 两次 + `qVec_QvecV`），
长度 `mm+3`，内层向量于是可以取层 `mm+3`，`i < mm+3` 足够。

也就是说 func 支必须**先** `substs_all` 下降到体，再对体用
`subst_QvecV_conjunct`（它的假设正是 `i < n+3`、层 `QvecV (n+3)`）。
下面这条就是那个可用的版本。

`subst (QvecV (mm+2)) (conjunct 3 mm i y) = conjunct 3 mm i y` 对 `i < mm+3`。
注意 `QvecV (mm+2)` 长度 `mm+3`。
-/
lemma subst_QvecV_mm2_conjunct {mm i y : V} (hy : IsSemiformula ℒₛₑₜ (mm + 1) y)
    (hi : i < mm + 3) :
    subst ℒₛₑₜ (QvecV (V := V) (mm + 3)) (conjunct 3 mm i y) = conjunct 3 mm i y := by
  exact subst_QvecV_conjunct hy hi

end GodelQ.QVec2Probe2
