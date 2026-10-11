import GodelQ.ZFC.ShiftTools
import GodelQ.ZFC.TranslateShiftCompat

/-!
# CG-007 · W8 第二层（十三）：`iT` 与 `shift` 的相容律 `iT_shift`

`hAll` / `hShift` 两支需要

```
iT n (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT n p)
```

（`p` 是 V 内任意公式码）。归纳谓词照 `isSemiformula_iT` / `iT_neg` 同形，
带 `param = n` 护罩。**量词支的关键**是 `shift_domZero`
（`iT` 给每个量词多引一个 `domZero`，`shift` 不引；这个错位被此式抹平）。

## 状态（2026-10-11）

**七支已证**：`verum` / `falsum` / `and` / `or` / `all` / `exs`（本文件），
外加 `rel`/`nrel` 两支所依赖的项层地基（`TranslateShiftCompat.lean` 的
`iVE_shift_bvar`/`_fvar` 与 `ShiftTools.shift_ve0`）。

**剩余两支**：`rel` / `nrel`——它们需要项层 `iVE_shift` 的 **func 支（`k ≠ 0`，即 `ve2`）**，
其展开需 `shift_conjunct`（`conjunct` 是叠合，用 `shift_and` + 归纳）、
`shift (subst (^#2 ∷ [#0,#1]) (cFunc k f)) = 自身`（闭代换，走 `shift_quote` 路线）、
以及 `resultVec` 与 `termShiftVec` 的点相容（`nth_resultVec` 逐分量 + 项级 IH）。

**来源**：骨架与量词支写法来自并行工位 `elegant-mclaren-767fb0` 的
`IShiftFull-6of8.lean`（CG-009），本 worktree 独立重编译核验后吸收，
改用本包的 `ShiftTools`（不依赖其 `GateBranches`）。
-/

set_option maxHeartbeats 2000000

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate
open GodelQ.ShiftTools

namespace GodelQ.ITShift

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iT` 与 `shift` 相容**：`iT n (shift p) = shift (iT n p)`。 -/
theorem iT_shift {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (shift (L := ℒₒᵣ) p) = shift (L := ℒₛₑₜ) (iT n p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p →
      param = n → iT param (shift (L := ℒₒᵣ) p) =
        shift (L := ℒₛₑₜ) (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n → iT param (shift (L := ℒₒᵣ) p) =
        shift (L := ℒₛₑₜ) q)
      ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · intro p hp
    simpa [iT] using key hp (rfl : n = n)
  · definability
  · -- rel（待补：需 iVE_shift 的 func 支）
    intro n param k R v hR hv h
    sorry
  · -- nrel（待补：同 rel）
    intro n param k R v hR hv h
    sorry
  · -- verum
    intro n param h
    show iT param (shift (L := ℒₒᵣ) (^⊤ : V)) = shift (L := ℒₛₑₜ) (iT.construction.verum param)
    rw [shift_verum (L := ℒₒᵣ)]
    simp only [iT.construction, iT_verum, shift_verum (L := ℒₛₑₜ)]
  · -- falsum
    intro n param h
    show iT param (shift (L := ℒₒᵣ) (^⊥ : V)) = shift (L := ℒₛₑₜ) (iT.construction.falsum param)
    rw [shift_falsum (L := ℒₒᵣ)]
    simp only [iT.construction, iT_falsum, shift_falsum (L := ℒₛₑₜ)]
  · -- and
    intro n param p q hp hq ihp ihq h
    rw [← h] at hp hq
    rw [shift_and hp.isUFormula hq.isUFormula]
    rw [iT_and (IsUFormula.shift (L := ℒₒᵣ) hp.isUFormula)
      (IsUFormula.shift (L := ℒₒᵣ) hq.isUFormula)]
    show iT param (shift ℒₒᵣ p) ^⋏ iT param (shift ℒₒᵣ q) =
      shift ℒₛₑₜ (iT param p ^⋏ iT param q)
    rw [shift_and (isSemiformula_iT p hp).isUFormula (isSemiformula_iT q hq).isUFormula]
    exact congrArg₂ (· ^⋏ ·) (ihp h) (ihq h)
  · -- or
    intro n param p q hp hq ihp ihq h
    rw [← h] at hp hq
    rw [shift_or hp.isUFormula hq.isUFormula]
    rw [iT_or (IsUFormula.shift (L := ℒₒᵣ) hp.isUFormula)
      (IsUFormula.shift (L := ℒₒᵣ) hq.isUFormula)]
    show iT param (shift ℒₒᵣ p) ^⋎ iT param (shift ℒₒᵣ q) =
      shift ℒₛₑₜ (iT param p ^⋎ iT param q)
    rw [shift_or (isSemiformula_iT p hp).isUFormula (isSemiformula_iT q hq).isUFormula]
    exact congrArg₂ (· ^⋎ ·) (ihp h) (ihq h)
  · -- all
    intro n param p hp ih h
    rw [← h] at hp
    show iT param (shift (L := ℒₒᵣ) (^∀ p)) =
      shift (L := ℒₛₑₜ) (UformulaRec1.Construction.result ℒₒᵣ iT.construction param (^∀ p))
    rw [shift_all hp.isUFormula]
    rw [iT_all (IsUFormula.shift (L := ℒₒᵣ) hp.isUFormula)]
    show (^∀ (imp ℒₛₑₜ domZero (iT (param + 1) (shift ℒₒᵣ p))) : V) =
      shift (L := ℒₛₑₜ) (UformulaRec1.Construction.result ℒₒᵣ iT.construction param (^∀ p))
    rw [UformulaRec1.Construction.result_all (c := iT.construction) (L := ℒₒᵣ)
      hp.isUFormula (rfl : iT.construction.allSize param p = 1)]
    change (^∀ (imp ℒₛₑₜ domZero (iT (param + 1) (shift ℒₒᵣ p))) : V) =
      shift ℒₛₑₜ (^∀ (imp ℒₛₑₜ domZero
        ((UformulaRec1.Construction.result ℒₒᵣ iT.construction
          (iT.construction.allChanges param 0) p ∷ (0 : V)) : V).[0]))
    rw [nth_adjoin_zero]
    change (^∀ (imp ℒₛₑₜ domZero (iT (param + 1) (shift ℒₒᵣ p))) : V) =
      shift ℒₛₑₜ (^∀ (imp ℒₛₑₜ domZero (iT (iT.construction.allChanges param 0) p)))
    rw [shift_all]
    · congr 1
      rw [GodelQ.ShiftTools.shift_imp]
      · rw [GodelQ.ShiftTools.shift_domZero (V := V)]
        exact congrArg (fun x => imp ℒₛₑₜ domZero x)
          (ih 0 (by simp [iT.construction]) (by simp [iT.construction, h]))
      · exact (isSemiformula_domZero (n := param)).isUFormula
      · exact (isSemiformula_iT p (by simpa [iT.construction] using hp)).isUFormula
    · exact (IsUFormula.imp).mpr ⟨(isSemiformula_domZero (n := param)).isUFormula,
        (isSemiformula_iT p (by simpa [iT.construction] using hp)).isUFormula⟩
  · -- exs
    intro n param p hp ih h
    rw [← h] at hp
    show iT param (shift (L := ℒₒᵣ) (^∃ p)) =
      shift (L := ℒₛₑₜ) (UformulaRec1.Construction.result ℒₒᵣ iT.construction param (^∃ p))
    rw [shift_exs hp.isUFormula]
    rw [iT_exs (IsUFormula.shift (L := ℒₒᵣ) hp.isUFormula)]
    show (^∃ (domZero ^⋏ iT (param + 1) (shift ℒₒᵣ p)) : V) =
      shift (L := ℒₛₑₜ) (UformulaRec1.Construction.result ℒₒᵣ iT.construction param (^∃ p))
    rw [UformulaRec1.Construction.result_exs (c := iT.construction) (L := ℒₒᵣ)
      hp.isUFormula (rfl : iT.construction.exsSize param p = 1)]
    change (^∃ (domZero ^⋏ iT (param + 1) (shift ℒₒᵣ p)) : V) =
      shift ℒₛₑₜ (^∃ (domZero ^⋏
        ((UformulaRec1.Construction.result ℒₒᵣ iT.construction
          (iT.construction.exsChanges param 0) p ∷ (0 : V)) : V).[0]))
    rw [nth_adjoin_zero]
    change (^∃ (domZero ^⋏ iT (param + 1) (shift ℒₒᵣ p)) : V) =
      shift ℒₛₑₜ (^∃ (domZero ^⋏ iT (iT.construction.exsChanges param 0) p))
    rw [shift_exs]
    · congr 1
      rw [shift_and]
      · rw [GodelQ.ShiftTools.shift_domZero (V := V)]
        exact congrArg (fun x => domZero ^⋏ x)
          (ih 0 (by simp [iT.construction]) (by simp [iT.construction, h]))
      · exact (isSemiformula_domZero (n := param)).isUFormula
      · exact (isSemiformula_iT p (by simpa [iT.construction] using hp)).isUFormula
    · exact (IsUFormula.and).mpr ⟨(isSemiformula_domZero (n := param)).isUFormula,
        (isSemiformula_iT p (by simpa [iT.construction] using hp)).isUFormula⟩

end GodelQ.ITShift

#print axioms GodelQ.ITShift.iT_shift
