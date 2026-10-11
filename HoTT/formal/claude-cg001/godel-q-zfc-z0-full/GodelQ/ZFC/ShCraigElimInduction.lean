import GodelQ.ZFC.ShCraigElimBranches

/-!
# CG-007 · W8 第二层（十一）：`ShCraigElim` 归纳的接线

`ShCraigElimSetup.induction_setup` 用 `P`（`Provable` 版）固定了 10 个支的骨架，
但 `ShCraigElimBranches` 里证出的支都是 `Q`（`Derivable` 版）——
`Derivable` 版的支直接对得上 `Derivable.wk` / `Derivable.and_m` 这类规则。

`Q` 也是 Σ1 谓词（`ShCraigElimSetup.q_defined`），故可以**用 `Q` 重开一份归纳**，
把已证的支直接接进去。本文件就是这份归纳。

## 已接线（7 支）

| 支 | 用的引理 |
|---|---|
| `axL` | `ShCraigElimBranches.hAxL`（用一般相容律 `iT_neg`，C-398） |
| `verumIntro` | `ShCraigElimBranches.hVerumIntro` |
| `andIntro` | `ShCraigElimBranches.hAnd`（用 `translateSeq_insert` + `iT_and`） |
| `orIntro` | `ShCraigElimBranches.hOr`（同上，`iT_or`） |
| `wkRule` | `ShCraigElimBranches.hWk`（`Derivable.wk` + `translateSeq_mono`） |
| `cutRule` | `ShCraigElimBranches.hCut`（用 `iT_neg`，C-398） |
| `shiftRule` | `ShCraigElimBranches.hShift`（用 `iT_shift`，2026-10-11 证出） |

## 待补（3 支）

| 支 | 缺什么 |
|---|---|
| `allIntro` | `iT` 与 `free`/`setShift` 的相容律；`setShift` 半边已由 `translateSeq_setShift` 解决，还差 `free` 半边（`iT` 与 `substs1`/`free` 的相容） |
| `exsIntro` | `iT` 与 `substs1` 的相容律，同上量级 |
| `axm` | 四块已证（`ProbeHAxm.lean` / `ProbeHAxm2.lean`）；最后一环需把 V 层 `reWitness` 见证认成引号化 |

**本文件不是 `ShCraigElim`**：待补的 3 支填完、且整条消去与 `bwd_of_shcraig_elim`
接上之后，才谈得上 `ShCraigElim`。`zfcTr_D3_internalize` 仍未证。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ShCraigElimInduction

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`ShCraigElim` 归纳（`Q` 版）**：六支已接线，四支待补。

`Q d := Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`。 -/
theorem induction_setup_Q (d : V) (hd : Derivation (V := V) (L := ℒₒᵣ) Sh.craig d) :
    ShCraigElimSetup.Q (V := V) d := by
  apply Derivation.induction1 (T := Sh.craig) 𝚺
    (hP := ShCraigElimSetup.q_defined.to_definable) hd
  · -- axL
    intro s _hs p _hp _hn
    exact ShCraigElimBranches.hAxL _hs _hp _hn
  · -- verumIntro
    intro s _hs _hv
    exact ShCraigElimBranches.hVerumIntro _hs _hv
  · -- andIntro
    intro s hs p q dp dq hpq hdp hdq ihp ihq
    exact ShCraigElimBranches.hAnd hs hpq ihp ihq hdp.1 hdq.1
  · -- orIntro
    intro s hs p q dd hpq hd ih
    exact ShCraigElimBranches.hOr hs hpq ih hd.1
  · -- allIntro（待补：需 iT-setShift 相容律）
    intro s _hs p _dd _hp _hd _ih
    sorry
  · -- exsIntro（待补：需 iT-substs1 相容律）
    intro s _hs p t _dd _hp _ht _hd _ih
    sorry
  · -- wkRule
    intro s _hs _dd _h _hd _ih
    exact ShCraigElimBranches.hWk _hs _h _ih
  · -- shiftRule
    intro s hs _dd h _hd ih
    exact ShCraigElimBranches.hShift hs h ih
  · -- cutRule
    intro s hs p d₁ d₂ h₁ h₂ ih₁ ih₂
    have hp : IsSemiformula ℒₒᵣ 0 p :=
      h₁.isFormulaSet p (mem_bitInsert_iff.mpr (Or.inl rfl))
    exact ShCraigElimBranches.hCut hs hp ih₁ ih₂ h₁.1 h₂.1
  · -- axm（待补：四块已证，最后一环需 V 层见证的引号化）
    intro s _hs p _hps _hpT
    sorry

end GodelQ.ShCraigElimInduction

#print axioms GodelQ.ShCraigElimInduction.induction_setup_Q
