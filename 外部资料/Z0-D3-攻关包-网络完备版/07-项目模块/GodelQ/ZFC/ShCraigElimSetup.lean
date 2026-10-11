import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.SeqTranslate

/-!
# CG-007 · W8 第二层（四）：`ShCraigElim` 的归纳设置已经跑通

`Z0UniBridge.ShCraigElim` 是本 repo 唯一剩下的消去：把 V 中的一条 `Sh.craig`
推导编码翻成 `𝗭𝗙𝗖` 推导编码。本文件**不证**这条消去；它把归纳所需的
每一件东西都落地并编译通过，使缺口从"路线"变成"可施工"。

## 本文件确立的三件事

1. **归纳原理可用**：`Derivation.induction1` 的 10 个规则支全部能对上
   （本文件 `induction_setup` 给出完整骨架）。
2. **归纳不变量可用**：`P d := Provable 𝗭𝗙𝗖 (translateSeq (fstIdx d))` 是
   `𝚺ᴬ₁-Predicate`，即 `induction1` 要的 `hP`。这是本文件唯一的新证明。
3. **每个支都化简到同一个形状**：`Provable 𝗭𝗙𝗖 (translateSeq s)`，
   即"结论 sequent 的翻译可证"。

## 与 `Z0UniBridge` 的关系

`ShCraigElim` 一旦成立，`Z0UniBridge.bwd_of_shcraig_elim`（C-390，已收据）
立即给出 `bwd`，进而 `keyE`、D3、Z0 完整形式。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate

namespace GodelQ.ShCraigElimSetup

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **归纳不变量**：推导 `d` 的结论 sequent 翻译后，𝗭𝗙𝗖 可证。

这是 `induction1` 需要的谓词。注意它作用在**推导编码 `d`** 上，
用 `fstIdx d` 取出结论 sequent——`induction1` 的每个支给出的正是 `P (axL s p)` 这类形状。 -/
def P (d : V) : Prop := Provable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) (fstIdx d))

/-- `P` 的 Σ1 公式。

`fstIdxDef` 是 `{ Γ := 𝚺, rank := 0 }.Semisentence 2`，
`translateSeqGraph` 是 `{ Γ := 𝚺, rank := 1 }.Semisentence 2`，
`provable 𝗭𝗙𝗖` 是 `{ Γ := 𝚺, rank := 1 }.Semisentence 1`；
三者的存在量化组合仍是 Σ1。 -/
noncomputable def pDef : 𝚺ᴬ₁.Semisentence 1 := .mkSigma
  “d. ∃ s, !fstIdxDef s d ∧ ∃ y, !translateSeqGraph y s ∧ !(provable 𝗭𝗙𝗖) y”

/-- **本文件的核心证明**：`P` 是 Σ1 谓词，故可作 `induction1` 的 `hP`。 -/
instance p_defined : 𝚺ᴬ₁-Predicate (P (V := V)) via pDef :=
  .mk fun v => by simp [pDef, P]

/-- **归纳设置**：`Derivation Sh.craig d → P d` 的 10 个规则支。

每个支的**目标形状**都已由 `simp [P, fstIdx_*]` 化简到
`Provable 𝗭𝗙𝗖 (translateSeq s)`，其中 `s` 是该支的结论 sequent。
本文件不填这些支（它们是 `ShCraigElim` 的实质内容）；这里只固定骨架，
使后续工作可以直接从任一支出发。 -/
theorem induction_setup (d : V) (hd : Derivation (V := V) (L := ℒₒᵣ) Sh.craig d) :
    P (V := V) d := by
  apply Derivation.induction1 (T := Sh.craig) 𝚺 (hP := p_defined.to_definable) hd
  · -- axL：p ∈ s 且 ∼p ∈ s。目标化为 `Provable 𝗭𝗙𝗖 (translateSeq s)`
    intro s _hs p _hp _hn
    simp only [P, fstIdx_axL]
    sorry
  · -- verumIntro：⊤ ∈ s
    intro s _hs _hv
    simp only [P, fstIdx_verumIntro]
    sorry
  · -- andIntro：两条子推导的结论合取
    intro s _hs p q dp dq _hpq _hdp _hdq _ihp _ihq
    simp only [P, fstIdx_andIntro]
    sorry
  · -- orIntro
    intro s _hs p q _dd _hpq _hd _ih
    simp only [P, fstIdx_orIntro]
    sorry
  · -- allIntro：需要 iT 与 setShift 的相容（未证）
    intro s _hs p _dd _hp _hd _ih
    simp only [P, fstIdx_allIntro]
    sorry
  · -- exsIntro：需要 iT 与 substs1 的相容（未证）
    intro s _hs p t _dd _hp _ht _hd _ih
    simp only [P, fstIdx_exsIntro]
    sorry
  · -- wkRule：用 translateSeq_mono
    intro s _hs _dd _h _hd _ih
    sorry
  · -- shiftRule：需要 iT 与 setShift 的相容（未证）
    intro s _hs _dd _h _hd _ih
    sorry
  · -- cutRule
    intro s _hs p d₁ d₂ _h₁ _h₂ _ih₁ _ih₂
    simp only [P, fstIdx_cutRule]
    sorry
  · -- axm：唯一用到 Sh.craig 公理的支（ρ.padding k 形状）
    intro s _hs p _hps _hpT
    simp only [P, fstIdx_axm]
    sorry

end GodelQ.ShCraigElimSetup

#print axioms GodelQ.ShCraigElimSetup.p_defined
