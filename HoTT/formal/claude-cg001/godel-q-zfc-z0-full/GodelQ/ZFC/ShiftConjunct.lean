import GodelQ.ZFC.ShiftTools

/-!
# CG-007 · W8 第二层（十四）：`shift` 与 `conjunct` 的相容律

`iVE_shift` 的 func 支（`k ≠ 0`，即 `ve2`）需要 `shift` 与 `ve2` 的三个组成部分相容：

1. **本文件**：`shift_conjunct`——`shift` 与 `conjunct` 的相容；
2. 闭代换 `subst (^#2 ∷ ?[^#0,^#1]) (cFunc k f)` 在 `shift` 下不动（走 `shift_quote`）；
3. `resultVec` 与 `termShiftVec` 的点相容（`nth_resultVec` 逐分量 + 项级 IH）。

## 参数序（本文件用类型探针确认，先前反复出错处）

- `IsSemitermVec L k n v`：`k` = **向量长度**，`n` = **层数**。
- `shift_substs (hp : IsSemiformula L n p) : IsSemitermVec L n m w → ...`：
  这里 `n` 是**长度**、`m` 是**层数**——与 `IsSemitermVec` 的定义顺序**相反**。
  故 `shift_substs` 的 `(n := 1) (m := 1)` 表示「长度 1、层数 1」，
  而 `hp` 必须是层数 1 的公式性。

`conjunct b n i y = (subst ?[^#i] cDomN) ^⋏ (subst (^#i ∷ shiftVec b n) y)`：
第一项闭（`cDomN` 是 `Semisentence ℒₛₑₜ 1` 的引号），第二项含 `y`。
-/

set_option maxHeartbeats 2000000

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ShiftConjunct

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `subst ?[^#i] cDomN` 在 `shift` 下不动（`cDomN` 是句子引号，代换后仍闭）。 -/
lemma shift_subst_cDomN {i : V} (hi : i < (1 : V)) :
    shift (L := ℒₛₑₜ) (subst ℒₛₑₜ (?[^#i] : V) (cDomN : V)) =
      subst ℒₛₑₜ (?[^#i] : V) (cDomN : V) := by
  rw [shift_substs (L := ℒₛₑₜ) (n := 1) (m := 1) (p := (cDomN : V))
    (isSemiformula_cDomN)
    (isSemitermVec_single_bvar hi)]
  congr 1
  · rw [show (1 : V) = 0 + 1 by norm_num,
      termShiftVec_cons (ht := IsUTerm.bvar) (hts := IsUTermVec.empty)]
    rw [termShift_bvar, termShiftVec_nil]
  · rw [cDomN_eq]
    exact GodelQ.ShiftTools.shift_quote _

end GodelQ.ShiftConjunct

#print axioms GodelQ.ShiftConjunct.shift_subst_cDomN
