-- CG-009: 用 m = 0 的实例把开口律两侧展开，确认层数。
import GodelQ.ZFC.OpenLawCheck

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.OpenLawCheck2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.LayerMono GodelQ.OpenLawCheck

/-! ## m = 0 的 `iTR` 展开

`iTR 1 2 R v` 的体：`conjunct 2 1 0 (iVE 1 v.[0])`，其第二半
`subst (^#0 ∷ shiftVec 2 1) (iVE 1 v.[0])`。

* `shiftVec 2 1 = [^#2]`（长度 1，`nth_shiftVec 2 1 0 _` 给 `^#(2+0)`）；
* 故该向量是 `^#0 ∷ ^#2 ∷ 0`，长度 2；
* `subst` 下降 `iTR` 的两层 `qqAlls` 后，向量变 `qVec² (QvecV 0) = QvecV 2`；
* `QvecV 2` 的长度是 3，条目 `[^#0, ^#1, ^&0]`。
-/

-- `QvecV 0` 的长度与条目：
example : (QvecV (V := V) 0) = (?[^&0] : V) := QvecV_zero
-- 下降两层：
example : qVec ℒₛₑₜ (qVec ℒₛₑₜ (QvecV (V := V) 0)) = QvecV (V := V) 2 := by
  rw [← QvecV_succ, ← QvecV_succ]; norm_num
-- `QvecV 2` 的条目：
example : (QvecV (V := V) 2).[0] = (^#0 : V) := nth_QvecV_lt 2 0 (by norm_num)
example : (QvecV (V := V) 2).[1] = (^#1 : V) := nth_QvecV_lt 2 1 (by norm_num)
example : (QvecV (V := V) 2).[2] = (^&0 : V) := nth_QvecV_last 2

-- **关键**：`conjunct 2 1 0 (iVE 1 v.[0])` 的第二半向量是 `^#0 ∷ ^#2 ∷ 0`（长度 2），
-- `termSubst (QvecV 2)` 读它的第 0 和第 1 项（索引 0、1），
-- 而 `QvecV 2` 在索引 0、1 处是 `^#0`、`^#1` —— **不是** `^#0`、`^#2`。
-- 所以确实差一层：需要 `QvecV 3`（其索引 0、1 仍是 `^#0`、`^#1`，索引 2 是 `^#2`）。
example : (QvecV (V := V) 3).[2] = (^#2 : V) := nth_QvecV_lt 3 2 (by norm_num)

end GodelQ.OpenLawCheck2
