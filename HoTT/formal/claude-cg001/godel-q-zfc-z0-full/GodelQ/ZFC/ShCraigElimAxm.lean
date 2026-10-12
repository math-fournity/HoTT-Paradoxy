import GodelQ.ZFC.ShCraigElimBranches

/-!
# CG-007 · W8 第二层（十八）：`axm` 支

`axm` 支的形状：`d = axm s p`，义务是 `Derivable 𝗭𝗙𝗖 (translateSeq s)`，
已知 `p ∈ s` 且 `p ∈ Sh.craig.Δ₁Class`。

## 路线（四块）

1. `p ∈ Sh.craig.Δ₁Class` 给出 `Sh.IsCraigAxiom p`——但 V 层的 `p` 是**裸码**，
   不一定是引号。真正能用的是 `Δ₁Class.mem_iff_s` 的**元层**读法：
   `(⌜φ⌝ : V) ∈ Sh.craig.Δ₁Class ↔ ∃ σ ∈ Sh.craig, φ = σ`，它要求 `p` 是引号。
   对**非标准** `p`，`Δ₁Class` 只说 `V ⊧/![p] Sh.craig.Δ₁ch`。
2. 本文件走的是**元层**路线：把 `p` 认成 `⌜σ⌝`（`σ : ArithmeticSentence`），
   于是 `σ ∈ Sh.craig`，用 `zfc_provable_of_mem_craig` 得 `𝗭𝗙𝗖 ⊢ translate σ`，
   再 `Provable → Derivable` 弱化到 `translateSeq s`。

## 范围

`p = ⌜σ⌝` 这一步**不能**从 `p ∈ Sh.craig.Δ₁Class` 无条件得到（V 可以非标准）。
本文件因此证明的是**引号化版本**：`hAll` 那类支不需要它，
但 `ShCraigElim` 的完整形式需要把这一步补上（见 `Z0UniBridge` 的缺口说明）。
本文件给出**能证的部分**并标出剩下的那一步。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

namespace GodelQ.ShCraigElimAxm

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `σ ∈ Sh.craig ⟹ 𝗭𝗙𝗖 ⊢ translate σ`。 -/
lemma zfc_provable_of_mem_craig (σ : ArithmeticSentence) (h : σ ∈ Sh.craig) :
    𝗭𝗙𝗖 ⊢ arithTrln.translate σ := by
  rw [← Sh_provable_iff]
  exact (inferInstance : Sh.craig ⪯ Sh).pbl (Entailment.by_axm h)

/-- `Provable → Derivable` 弱化（`φ ∈ s` 时）。 -/
lemma derivable_of_provable_mem {φ s : V} (hs : IsFormulaSet ℒₛₑₜ s)
    (hφs : φ ∈ s) (hp : Provable (L := ℒₛₑₜ) 𝗭𝗙𝗖 φ) : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 s := by
  have hd : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert φ (∅ : V)) := hp.toDerivable
  refine hd.wk hs ?_
  intro x hx
  rw [mem_bitInsert_iff] at hx
  rcases hx with rfl | hx
  · exact hφs
  · exact absurd hx (by simp)

/-- **`axm` 支（引号化版本）**：`p = ⌜σ⌝`、`σ ∈ Sh.craig` 时成立。

`iT 0 ⌜σ⌝ = ⌜translate σ⌝`（`iT_quote`），故 `translateSeq s ∋ ⌜translate σ⌝`，
而 `⌜translate σ⌝` 的 `𝗭𝗙𝗖`-可证性由 `zfc_provable_of_mem_craig` 给出。 -/
lemma hAxm_quoted {s : V} (σ : ArithmeticSentence) (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hps : (⌜σ⌝ : V) ∈ s) (hσ : σ ∈ Sh.craig) :
    Q (V := V) (axm s (⌜σ⌝ : V)) := by
  simp only [Q, fstIdx_axm]
  have hmem : iT (0 : V) (⌜σ⌝ : V) ∈ translateSeq (V := V) s :=
    mem_translateSeq_iff.mpr ⟨(⌜σ⌝ : V), hps, rfl⟩
  have hprov : Provable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (iT (0 : V) (⌜σ⌝ : V)) := by
    rw [show iT (0 : V) (⌜σ⌝ : V) = (⌜arithTrln.translate σ⌝ : V) from by
      rw [show (0 : V) = ((0 : ℕ) : V) by simp, iT_quote]]
    exact internalize_provability (V := V) (T := 𝗭𝗙𝗖) (zfc_provable_of_mem_craig σ hσ)
  exact derivable_of_provable_mem (φ := iT (0 : V) (⌜σ⌝ : V))
    (GodelQ.ShCraigElimBranches.isFormulaSet_translateSeq hs) hmem hprov

end GodelQ.ShCraigElimAxm

#print axioms GodelQ.ShCraigElimAxm.zfc_provable_of_mem_craig
#print axioms GodelQ.ShCraigElimAxm.derivable_of_provable_mem
#print axioms GodelQ.ShCraigElimAxm.hAxm_quoted
