import GodelQ.ZFC.OpenTranslate
import GodelQ.ZFC.SeqTranslate
import GodelQ.ZFC.TranslateRE

/-!
# 012-Opus · W8：自由变量不受 ω 限制，“证明逐条翻译”的不变量在 ℕ 中就不成立

Foundation 的翻译 `arithTrln.translate` 把量词限制在 ω 上，但**不给自由变量加“属于 ω”的前提**
（自由变量仍是集合变量）。内部翻译 `iT` 也一样（`OpenTranslate.iT_pquote`）。于是，一个自由变量
若取 ω 以外的集合，原子公式的翻译 `∀y₀y₁((y₀∈ω ∧ y₀=x) ∧ … → …)` 就因前件不可满足而为真，
它的否定为假。

本文件在标准模型 V = ℕ 中给出三条机器证明的反例，都用同一组公式：`#0 < 0`（层数 1）、
`&0 < 0`（自由变量 &0）、`∃x, x < 0`；求值在 Foundation 的 𝗭𝗙𝗖 模型 `Universe` 中进行，自由变量
取 ω（ω ∉ ω，由正则公理）。

1. `exsBridge2_false`：舰队 round31 钉住的 `ExsBridge2`（`IsUFormula p → IsTerm t →
   Provable 𝗭𝗙𝗖 (imp (iT 0 (substs1 t p)) (^∃ (domZero ^⋏ iT 1 p)))`）在 ℕ 中不成立：
   取 p = ⌜#0 < 0⌝、t = ^&0。
2. `dCounter_not_Q`：纯逻辑推导 `dCounter`（结论 sequent `{∃x (x<0), ¬(&0<0)}`，由 ∃ 引入作用在
   公理 `{&0<0, …, ¬(&0<0)}` 上；不用任何理论公理，所以对每个理论 T 都是 T 的推导，
   `dCounter_derivation`）的结论翻译后，𝗭𝗙𝗖 不可导。于是舰队的归纳不变量
   `Q d := Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`（`ShCraigElimPredicate.lean:65`）对
   `Sh.craig` 的推导不成立（`q_invariant_false`）。
3. `exsBlockerQ_false`：舰队的 `ExsBlockerQ`（`ShCraigElimSetupQ.lean`，把 `Q` 展开逐字写出）
   在 ℕ 中不成立：上面的实例满足它的全部前提，结论却不成立。

`translateSeq` 取自 `SeqTranslate.lean`（与 `dev`、`codex/9276-cg007-w8-d3`、舰队 round31 与
master-assembly 各处的副本逐字节相同，SHA-256 `c8d044db…26bd7`）。

这些反例只说明：**按 `Q` 这个不变量逐条翻译推导**的路线走不通；它们不否定舰队的
`ShCraigElim`（只对句子 σ 陈述）本身，也不涉及 Z0 的真假。修正的方向是让不变量带上自由变量的
ω 前提，或绕开证明翻译（见本包 `PLAN.md`）。
-/

namespace GodelQ.FreeVarCounter

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open GodelQ.ZFCArith GodelQ.Translate GodelQ.OpenTranslate GodelQ.SeqTranslate GodelQ.ZFCZ0
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

/-! ## 1. 三个算术公式 -/

/-- 零的项。 -/
abbrev zeroT {n : ℕ} : SyntacticSemiterm ℒₒᵣ n :=
  Semiterm.func (Language.ORing.Func.zero : (ℒₒᵣ).Func 0) ![]

/-- 层数 1 的 `#0 < 0`。 -/
def ltB : Semiproposition ℒₒᵣ 1 :=
  Semiformula.rel (Language.ORing.Rel.lt : (ℒₒᵣ).Rel 2) ![#0, zeroT]

/-- 开公式 `&0 < 0`。 -/
def ltZ : Proposition ℒₒᵣ :=
  Semiformula.rel (Language.ORing.Rel.lt : (ℒₒᵣ).Rel 2) ![&0, zeroT]

lemma ltB_subst : ltB ⇜ ![&0] = ltZ := by
  simp [ltB, ltZ, Rew.func]

/-! ## 2. 在 `Universe` 中求值：自由变量取 ω -/

abbrev U := Universe.{0}

/-- 把每个自由变量都赋值为 ω。 -/
noncomputable def fω : ℕ → U := fun _ ↦ (ω : U)

lemma arithTrln_domain : arithTrln.domain = GodelQ.ZFCArith.domainDef := rfl

lemma arithTrln_rel {k} (R : (ℒₒᵣ).Rel k) : arithTrln.rel R = relDef R := rfl

lemma arithTrln_func {k} (f : (ℒₒᵣ).Func k) : arithTrln.func f = funcDef f := rfl

lemma dom_iff_mem (x : U) : arithTrln.Dom x ↔ x ∈ (ω : U) := by
  rw [DirectTranslation.dom_iff, arithTrln_domain, eval_domainDef]

/-- 原子翻译的求值（任意赋值；照 Foundation `eval_translateRel_iff` 的第一步）。 -/
lemma eval_translateRel {n k} (b : Fin n → U) (f : ℕ → U) (R : (ℒₒᵣ).Rel k)
    (v : Fin k → SyntacticSemiterm ℒₒᵣ n) :
    Semiformula.Eval b f (arithTrln.translateRel R v) ↔
      ∀ w : Fin k → U, (∀ i, arithTrln.Dom (w i) ∧
        Semiformula.Eval (w i :> b) f (arithTrln.varEqual (v i))) → U ⊧/w (arithTrln.rel R) := by
  simp [DirectTranslation.translateRel, Matrix.comp_vecCons', Semiformula.eval_embSubsts,
    Matrix.constant_eq_singleton, ← DirectTranslation.dom_iff, Function.comp_def]

/-- `(&0 < 0)ᵗ` 在 &0 ↦ ω 时为真：前件要求 ω ∈ ω。 -/
lemma eval_tLtZ : Semiformula.Evalf fω (arithTrln.translate ltZ) := by
  show Semiformula.Eval ![] fω (arithTrln.translateRel _ _)
  rw [eval_translateRel]
  intro w hw
  exfalso
  have h0 := hw 0
  have hd : w 0 ∈ (ω : U) := (dom_iff_mem _).mp h0.1
  have he : w 0 = (ω : U) := by
    simpa [DirectTranslation.varEqual, fω] using h0.2
  exact mem_irrefl (ω : U) (he ▸ hd)

/-- `(∃x, x < 0)ᵗ` 在 `Universe` 中为假。 -/
lemma not_eval_tExLtB : ¬ Semiformula.Evalf fω (arithTrln.translate (∃¹ ltB)) := by
  rw [DirectTranslation.translate_ex]
  simp only [Semiformula.Evalf, DirectTranslation.Model.eval_exs]
  rintro ⟨x, hx⟩
  rw [show arithTrln.translate ltB = arithTrln.translateRel _ _ from rfl, eval_translateRel] at hx
  have hz : (∅ : U) ∈ (ω : U) := by simp
  have h := hx ![(x : U), ∅] (fun i ↦ by
    match i with
    | 0 => exact ⟨by simp, by simp [DirectTranslation.varEqual]⟩
    | 1 =>
      refine ⟨(dom_iff_mem _).mpr hz, ?_⟩
      simp [DirectTranslation.varEqual, arithTrln_func, Matrix.conj])
  rw [arithTrln_rel, eval_relDef_lt] at h
  simp at h

/-! ## 3. 可靠性：ℕ 中的内部可导性给出真推导，推导在 `Universe` 中可靠 -/

lemma derivation2_sound {Γ : Finset (Proposition ℒₛₑₜ)} (d : 𝗭𝗙𝗖 ⟹₂ Γ) (f : ℕ → U) :
    ∃ φ ∈ Γ, Semiformula.Evalf f φ := by
  rcases LK2.Derivation.toProofData d with ⟨A, hA, b⟩
  rcases LK.Derivation.sound f b with ⟨φ, hφ, h⟩
  rcases Multiset.mem_add.mp hφ with hφ | hφ
  · exact ⟨φ, hφ, h⟩
  · exfalso
    have : ∃ σ ∈ A, ∼(Rewriting.emb σ : Proposition ℒₛₑₜ) = φ := by
      simpa [LK.Sequent.embed, Multiset.tilde_def] using hφ
    rcases this with ⟨σ, hσ, rfl⟩
    have hU : U↓[ℒₛₑₜ] ⊧ σ := Semantics.ModelsSet.models _ (hA σ hσ)
    simp [models_iff] at hU
    simp [hU] at h

lemma derivable_sound {Γ : Finset (Proposition ℒₛₑₜ)}
    (h : Derivable (V := ℕ) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (⌜Γ⌝ : ℕ)) (f : ℕ → U) :
    ∃ φ ∈ Γ, Semiformula.Evalf f φ := by
  rcases h with ⟨d, hd1, hd2⟩
  rcases FFL.FirstOrder.Arithmetic.Bootstrapping.Derivation.sound hd2 with ⟨Δ, hΔ, ⟨b⟩⟩
  have : Δ = Γ := LK2.Derivation.Sequent.quote_inj (V := ℕ) (hΔ.trans hd1)
  subst this
  exact derivation2_sound b f

lemma provable_sound {φ : Proposition ℒₛₑₜ}
    (h : Provable (V := ℕ) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (⌜φ⌝ : ℕ)) (f : ℕ → U) :
    Semiformula.Evalf f φ := by
  rcases derivation2_sound (Provable.sound2 h) f with ⟨ψ, hψ, H⟩
  simp only [Finset.mem_singleton] at hψ
  exact hψ ▸ H

/-! ## 4. 码的计算 -/

lemma quote_ltB_isUFormula : IsUFormula ℒₒᵣ (⌜ltB⌝ : ℕ) := pquote_isUFormula ltB

lemma isTerm_fvar0 : IsTerm ℒₒᵣ (^&(0 : ℕ) : ℕ) := by simp

lemma substs1_ltB : substs1 ℒₒᵣ (^&(0 : ℕ)) (⌜ltB⌝ : ℕ) = ⌜ltZ⌝ := by
  rw [← ltB_subst, pquote_substs]
  rfl

lemma iT_ltZ : iT (0 : ℕ) (⌜ltZ⌝ : ℕ) = ⌜arithTrln.translate ltZ⌝ := by
  simpa using iT_pquote (V := ℕ) ltZ

lemma iT_negLtZ : iT (0 : ℕ) (⌜∼ltZ⌝ : ℕ) = ⌜arithTrln.translate (∼ltZ)⌝ := by
  simpa using iT_pquote (V := ℕ) (∼ltZ)

lemma iT_exLtB : iT (0 : ℕ) (⌜(∃¹ ltB : Proposition ℒₒᵣ)⌝ : ℕ) = ⌜arithTrln.translate (∃¹ ltB)⌝ := by
  simpa using iT_pquote (V := ℕ) (∃¹ ltB)

lemma exs_domZero_ltB :
    (^∃ (domZero (V := ℕ) ^⋏ iT (1 : ℕ) ⌜ltB⌝) : ℕ) = ⌜arithTrln.translate (∃¹ ltB)⌝ := by
  rw [← iT_exLtB, Semiformula.quote_ex, iT_exs quote_ltB_isUFormula]
  simp

/-! ## 5. `ExsBridge2` 在 ℕ 中为假 -/

/-- **反例一**：舰队的 `ExsBridge2` 在标准模型 ℕ 中不成立（p = ⌜#0 < 0⌝，t = ^&0）。 -/
theorem exsBridge2_false :
    ¬ ∀ {p t : ℕ}, IsUFormula ℒₒᵣ p → IsTerm ℒₒᵣ t →
      Provable (L := ℒₛₑₜ) 𝗭𝗙𝗖
        (imp ℒₛₑₜ (iT (0 : ℕ) (substs1 ℒₒᵣ t p)) (^∃ (domZero (V := ℕ) ^⋏ iT (1 : ℕ) p))) := by
  intro H
  have h := H quote_ltB_isUFormula isTerm_fvar0
  rw [substs1_ltB, iT_ltZ, exs_domZero_ltB, ← pquote_imp] at h
  have := provable_sound h fω
  simp only [LogicalConnective.HomClass.map_imply] at this
  exact not_eval_tExLtB (this eval_tLtZ)

/-! ## 6. 纯逻辑推导 `dCounter`：`Q` 不变量与 `ExsBlockerQ` 在 ℕ 中为假 -/

/-- 结论 sequent `{∃x (x<0), ¬(&0<0)}` 的码。 -/
noncomputable def sC : ℕ := insert (⌜(∃¹ ltB : Proposition ℒₒᵣ)⌝ : ℕ) (insert (⌜∼ltZ⌝ : ℕ) ∅)

/-- 公理 `{&0<0, ∃x (x<0), ¬(&0<0)}`。 -/
noncomputable def ddC : ℕ := axL (insert (⌜ltZ⌝ : ℕ) sC) ⌜ltZ⌝

/-- ∃ 引入，见证 &0。 -/
noncomputable def dCounter : ℕ := exsIntro sC ⌜ltB⌝ (^&(0 : ℕ)) ddC

lemma sC_isFormulaSet : IsFormulaSet ℒₒᵣ sC := by
  simp [sC]

lemma exs_mem_sC : ^∃ (⌜ltB⌝ : ℕ) ∈ sC := by
  simp [sC, Semiformula.quote_ex]

lemma ddC_fstIdx : fstIdx ddC = insert (substs1 ℒₒᵣ (^&(0 : ℕ)) (⌜ltB⌝ : ℕ)) sC := by
  rw [substs1_ltB]; simp [ddC]

lemma ddC_derivation (T : ArithmeticTheory) [T.Δ₁] : Derivation (V := ℕ) T ddC := by
  apply Derivation.axL
  · simp [sC]
  · simp
  · rw [← pquote_neg]; simp [sC]

/-- `dCounter` 不用任何理论公理，所以它是每个理论的推导，特别是 `Sh.craig` 的推导。 -/
theorem dCounter_derivation (T : ArithmeticTheory) [T.Δ₁] : Derivation (V := ℕ) T dCounter :=
  Derivation.exsIntro exs_mem_sC isTerm_fvar0 ⟨ddC_fstIdx, ddC_derivation T⟩

lemma translateSeq_sC :
    translateSeq sC =
      (⌜({arithTrln.translate (∃¹ ltB), arithTrln.translate (∼ltZ)} : Finset (Proposition ℒₛₑₜ))⌝ : ℕ) := by
  rw [sC, translateSeq_insert, translateSeq_insert, translateSeq_empty, iT_exLtB, iT_negLtZ]
  simp

/-- **反例二**：`dCounter` 的结论翻译后，𝗭𝗙𝗖 不可导。 -/
theorem dCounter_not_Q : ¬ Derivable (V := ℕ) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (fstIdx dCounter)) := by
  intro h
  rw [dCounter, fstIdx_exsIntro, translateSeq_sC] at h
  rcases derivable_sound h fω with ⟨φ, hφ, H⟩
  simp only [Finset.mem_insert, Finset.mem_singleton] at hφ
  rcases hφ with rfl | rfl
  · exact not_eval_tExLtB H
  · simp only [LogicalConnective.HomClass.map_neg] at H
    exact H eval_tLtZ

/-- **归纳不变量为假**：存在 `Sh.craig` 的推导 d（在 ℕ 中），其结论翻译后 𝗭𝗙𝗖 不可导。 -/
theorem q_invariant_false :
    ∃ d : ℕ, Derivation (V := ℕ) (L := ℒₒᵣ) Sh.craig d ∧
      ¬ Derivable (V := ℕ) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (fstIdx d)) :=
  ⟨dCounter, dCounter_derivation _, dCounter_not_Q⟩

lemma ddC_Q : Derivable (V := ℕ) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (fstIdx ddC)) := by
  rw [ddC, fstIdx_axL, translateSeq_insert, iT_ltZ]
  apply Derivable.em (p := (⌜arithTrln.translate ltZ⌝ : ℕ))
  · rw [translateSeq_sC]; simp
  · simp
  · rw [← pquote_neg, translateSeq_sC, ← LogicalConnective.HomClass.map_neg]; simp

/-- **反例三**：舰队的 `ExsBlockerQ`（`Q` 展开写）在 ℕ 中不成立。 -/
theorem exsBlockerQ_false :
    ¬ ∀ {s p t dd : ℕ}, IsFormulaSet (L := ℒₒᵣ) s → ^∃ p ∈ s → IsTerm ℒₒᵣ t →
      fstIdx dd = insert (substs1 ℒₒᵣ t p) s → Derivation (V := ℕ) (L := ℒₒᵣ) Sh.craig dd →
      Derivable (V := ℕ) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (fstIdx dd)) →
      Derivable (V := ℕ) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (fstIdx (exsIntro s p t dd))) := by
  intro H
  exact dCounter_not_Q (H sC_isFormulaSet exs_mem_sC isTerm_fvar0 ddC_fstIdx (ddC_derivation _) ddC_Q)

end GodelQ.FreeVarCounter

#print axioms GodelQ.FreeVarCounter.eval_tLtZ
#print axioms GodelQ.FreeVarCounter.not_eval_tExLtB
#print axioms GodelQ.FreeVarCounter.derivable_sound
#print axioms GodelQ.FreeVarCounter.provable_sound
#print axioms GodelQ.FreeVarCounter.exsBridge2_false
#print axioms GodelQ.FreeVarCounter.dCounter_derivation
#print axioms GodelQ.FreeVarCounter.dCounter_not_Q
#print axioms GodelQ.FreeVarCounter.q_invariant_false
#print axioms GodelQ.FreeVarCounter.exsBlockerQ_false
