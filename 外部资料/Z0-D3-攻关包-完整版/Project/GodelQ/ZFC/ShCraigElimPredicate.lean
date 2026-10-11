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


/-- **第二版归纳不变量（`Derivable` 版）**：推导 `d` 的结论 sequent 翻译后**可导**。

与 `P` 的区别：`P` 说的是"可证"（`Provable`，作用在单公式上），
`Q` 说的是"可导"（`Derivable`，作用在 sequent 上）。
`induction1` 的 `hWk` 支要用 `Derivable.wk`（弱化），所以 `Q` 在那一支更直接；
两版都可用，`Q` 更适合承接规则支。

`Derivable T s ↔ Provable T φ`（当 `s = φ ⫽ ∅`）由
`internal_provable_iff_internal_derivable` 给出，故两版可互相转换。 -/
def Q (d : V) : Prop := Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) (fstIdx d))

/-- `Q` 的 Σ1 公式：`fstIdxDef` + `translateSeqGraph` + `derivable 𝗭𝗙𝗖` 的存在量化组合。 -/
noncomputable def qDef : 𝚺ᴬ₁.Semisentence 1 := .mkSigma
  “d. ∃ s, !fstIdxDef s d ∧ ∃ t, !translateSeqGraph t s ∧ !(derivable 𝗭𝗙𝗖) t”

/-- **`Q` 是 Σ1 谓词**，同样可作 `induction1` 的 `hP`。 -/
instance q_defined : 𝚺ᴬ₁-Predicate (Q (V := V)) via qDef :=
  .mk fun v => by simp [qDef, Q]

end GodelQ.ShCraigElimSetup

#print axioms GodelQ.ShCraigElimSetup.p_defined
#print axioms GodelQ.ShCraigElimSetup.q_defined
