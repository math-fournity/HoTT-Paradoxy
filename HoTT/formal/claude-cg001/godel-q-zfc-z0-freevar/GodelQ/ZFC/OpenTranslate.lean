import GodelQ.ZFC.InternalTranslate

/-!
# 012-Opus · W8：内部翻译对带自由变量的公式也逐字正确

`InternalTranslate.lean` 的 `iT_quote` 只对句子（不含自由变量）成立。本文件把它推广到带自由变量的
公式（`Semiproposition`，自由变量用 ℕ 编号）：

* `iVE_pquote`：对每个项 t（可含自由变量），`iVE n ⌜t⌝ = ⌜varEqual t⌝`；
* `iT_pquote`：对每个算术公式 φ（可含自由变量），`iT n ⌜φ⌝ = ⌜translate φ⌝`。

证明照搬句子版，只多一个自由变量情形：`iVE` 把 `&x` 送到 `“#0 = &x”`，与 Foundation 的
`varEqual` 一致。注意 Foundation 的 `translate` 不给自由变量加“属于 ω”的限制（自由变量仍是
集合变量），内部翻译 `iT` 也一样；本文件只是如实记录这一点。
-/

namespace GodelQ.OpenTranslate

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open GodelQ.ZFCArith GodelQ.Translate
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 带自由变量公式的引号：通用部件 -/

section quote

variable {L : Language} [L.Encodable] [L.LORDefinable]

lemma pquote_imp {n : ℕ} (A B : Semiproposition L n) : (⌜A 🡒 B⌝ : V) = imp L ⌜A⌝ ⌜B⌝ := by
  simp [Semiformula.quote_def]

lemma pquote_neg {n : ℕ} (A : Semiproposition L n) : (⌜∼A⌝ : V) = neg L ⌜A⌝ := by
  simp [Semiformula.quote_def]

lemma pquote_allItr {n : ℕ} : ∀ (k : ℕ) (A : Semiproposition L (n + k)),
    (⌜∀¹^[k] A⌝ : V) = qqAlls ⌜A⌝ (k : V)
  | 0, A => by simp
  | k + 1, A => by
    rw [allItr_succ, pquote_allItr k (∀¹ A), Semiformula.quote_all, Nat.cast_succ, qqAlls_succ']

lemma pquote_substs {k m : ℕ} (φ : Semiproposition L k) (w : Fin k → SyntacticSemiterm L m) :
    (⌜φ ⇜ w⌝ : V) =
      subst L (SemitermVec.val fun i ↦ (⌜w i⌝ : Bootstrapping.Semiterm V L m)) ⌜φ⌝ := by
  rw [Semiformula.quote_def, Semiformula.typed_quote_substs, Bootstrapping.Semiformula.val_substs]
  rfl

omit [L.Encodable] [L.LORDefinable] in
lemma embSubsts_app' {k m : ℕ} (σ : Semisentence L k) (w : Fin k → SyntacticSemiterm L m) :
    Rewriting.app (Rew.embSubsts w) σ = (Rewriting.emb σ : Semiproposition L k) ⇜ w := by
  have : (Rew.embSubsts w : Rew L Empty k ℕ m) = (Rew.subst w).comp Rew.emb := by
    ext x
    · simp [Rew.comp_app]
    · exact Empty.elim x
  rw [this, TransitiveRewriting.comp_app]

lemma pquote_embSubsts {k m : ℕ} (σ : Semisentence L k) (w : Fin k → SyntacticSemiterm L m) :
    (⌜(Rewriting.app (Rew.embSubsts w) σ : Semiproposition L m)⌝ : V) =
      subst L (SemitermVec.val fun i ↦ (⌜w i⌝ : Bootstrapping.Semiterm V L m)) ⌜σ⌝ := by
  rw [embSubsts_app', pquote_substs]
  rfl

lemma pquote_emb {k : ℕ} (σ : Semisentence L k) :
    (⌜(Rewriting.app (Rew.emb : Rew L Empty k ℕ k) σ : Semiproposition L k)⌝ : V) = ⌜σ⌝ := rfl

lemma pval_vec_shift {n m : ℕ} (c : ℕ) (a : Fin m) (g : Fin n → Fin m) (hg : ∀ j, (g j : ℕ) = c + j) :
    (SemitermVec.val fun i ↦
        (⌜((#a :> fun j ↦ #(g j)) : Fin (n + 1) → SyntacticSemiterm L m) i⌝ :
          Bootstrapping.Semiterm V L m)) =
      ^#((a : ℕ) : V) ∷ shiftVec (c : V) (n : V) := by
  rw [show (SemitermVec.val fun i ↦
        (⌜((#a :> fun j ↦ #(g j)) : Fin (n + 1) → SyntacticSemiterm L m) i⌝ :
          Bootstrapping.Semiterm V L m)) =
      matrixToVec fun i ↦ (⌜((#a :> fun j ↦ #(g j)) : Fin (n + 1) → SyntacticSemiterm L m) i⌝ : V)
      from rfl, matrixToVec_succ, ← bvs_eq_fun c n (fun j ↦ (g j : ℕ)) hg]
  rfl

lemma pval_vec_one {m : ℕ} (a : Fin m) :
    (SemitermVec.val fun i ↦
        (⌜(![#a] : Fin 1 → SyntacticSemiterm L m) i⌝ : Bootstrapping.Semiterm V L m)) =
      ^#((a : ℕ) : V) ∷ 0 := rfl

lemma pval_vec_three {m : ℕ} (a b c : Fin m) :
    (SemitermVec.val fun i ↦
        (⌜((#a :> ![#b, #c]) : Fin 3 → SyntacticSemiterm L m) i⌝ : Bootstrapping.Semiterm V L m)) =
      ^#((a : ℕ) : V) ∷ ^#((b : ℕ) : V) ∷ ^#((c : ℕ) : V) ∷ 0 := rfl

lemma pvec_val {k m : ℕ} (w : Fin k → SyntacticSemiterm L m) :
    (SemitermVec.val fun i ↦ (⌜w i⌝ : Bootstrapping.Semiterm V L m)) = matrixToVec fun i ↦ (⌜w i⌝ : V) :=
  rfl

omit [L.Encodable] [L.LORDefinable] in
lemma matrix_conj_two_p {m : ℕ} (A : Fin 2 → Semiproposition L m) :
    Matrix.conj A = A 0 ⋏ (A 1 ⋏ ⊤) := rfl

omit [L.Encodable] [L.LORDefinable] in
lemma matrix_conj_zero_p {m : ℕ} (A : Fin 0 → Semiproposition L m) : Matrix.conj A = ⊤ := rfl

lemma pval_vec_two {m : ℕ} (a b : Fin m) :
    (SemitermVec.val fun i ↦
        (⌜(![#a, #b] : Fin 2 → SyntacticSemiterm L m) i⌝ : Bootstrapping.Semiterm V L m)) =
      ^#((a : ℕ) : V) ∷ ^#((b : ℕ) : V) ∷ 0 := rfl

end quote

/-! ## 项：`iVE` 对带自由变量的项 -/

section term

lemma pquote_eqBvars {m : ℕ} (a b : Fin m) :
    (⌜(“#a = #b” : Semiproposition ℒₛₑₜ m)⌝ : V) = ^rel 2 (cEqN : V) (^#(a : V) ∷ ^#(b : V) ∷ 0) := rfl

lemma pquote_eqBvarFvar {m : ℕ} (a : Fin m) (x : ℕ) :
    (⌜(“#a = &x” : Semiproposition ℒₛₑₜ m)⌝ : V) = ^rel 2 (cEqN : V) (^#(a : V) ∷ ^&(x : V) ∷ 0) := rfl

lemma iVE_pquote_bvar {n : ℕ} (x : Fin n) :
    iVE (n : V) ⌜(#x : SyntacticSemiterm ℒₒᵣ n)⌝ =
      ⌜(arithTrln.varEqual (#x : SyntacticSemiterm ℒₒᵣ n) : Semiproposition ℒₛₑₜ (n + 1))⌝ := by
  simp only [DirectTranslation.varEqual]
  rw [pquote_eqBvars]
  simp [iVE, iVE.construction, eqAtom]

lemma iVE_pquote_fvar {n : ℕ} (x : ℕ) :
    iVE (n : V) ⌜(&x : SyntacticSemiterm ℒₒᵣ n)⌝ =
      ⌜(arithTrln.varEqual (&x : SyntacticSemiterm ℒₒᵣ n) : Semiproposition ℒₛₑₜ (n + 1))⌝ := by
  simp only [DirectTranslation.varEqual]
  rw [pquote_eqBvarFvar]
  simp [iVE, iVE.construction, eqAtom]

lemma pquote_isUTerm {n : ℕ} (t : SyntacticSemiterm ℒₒᵣ n) : IsUTerm ℒₒᵣ (⌜t⌝ : V) :=
  (⌜t⌝ : Bootstrapping.Semiterm V ℒₒᵣ n).isSemiterm.isUTerm

lemma iVE_pfunc_lhs2 {n : ℕ} (f : (ℒₒᵣ).Func 2) (v : Fin 2 → SyntacticSemiterm ℒₒᵣ n) :
    iVE (n : V) ⌜(Semiterm.func f v : SyntacticSemiterm ℒₒᵣ n)⌝ =
      ve2 (n : V) 2 ⌜f⌝ ?[iVE (n : V) ⌜v 0⌝, iVE (n : V) ⌜v 1⌝] := by
  have hu := pquote_isUTerm (V := V) (Semiterm.func f v : SyntacticSemiterm ℒₒᵣ n)
  rw [Semiterm.quote_func] at hu ⊢
  simp only [Nat.cast_ofNat] at hu ⊢
  obtain ⟨hf, hv⟩ := IsUTerm.func_iff.mp hu
  rw [iVE, iVE.construction.result_func' hf hv]
  have h0 : (iVE.construction.resultVec ℒₒᵣ ![(n : V)] 2
      (SemitermVec.val fun i ↦ (⌜v i⌝ : Bootstrapping.Semiterm V ℒₒᵣ n))).[0] =
      iVE (n : V) ⌜v 0⌝ := by
    rw [iVE.construction.nth_resultVec ℒₒᵣ ![(n : V)] hv (by simp)]
    simp [iVE]; rfl
  have h1 : (iVE.construction.resultVec ℒₒᵣ ![(n : V)] 2
      (SemitermVec.val fun i ↦ (⌜v i⌝ : Bootstrapping.Semiterm V ℒₒᵣ n))).[1] =
      iVE (n : V) ⌜v 1⌝ := by
    rw [iVE.construction.nth_resultVec ℒₒᵣ ![(n : V)] hv (by simp)]
    simp [iVE]; rfl
  generalize iVE.construction.resultVec ℒₒᵣ ![(n : V)] 2
    (SemitermVec.val fun i ↦ (⌜v i⌝ : Bootstrapping.Semiterm V ℒₒᵣ n)) = W at h0 h1 ⊢
  simp only [iVE.construction, Matrix.cons_val_zero, two_ne_zero, ite_false]
  simp only [ve2, h0, h1]
  simp

lemma pvarEqual_rhs2 {n : ℕ} (f : (ℒₒᵣ).Func 2) (v : Fin 2 → SyntacticSemiterm ℒₒᵣ n) :
    (⌜(arithTrln.varEqual (Semiterm.func f v) : Semiproposition ℒₛₑₜ (n + 1))⌝ : V) =
      qqAlls (imp ℒₛₑₜ
        (conjunct 3 (n : V) 0 ⌜(arithTrln.varEqual (v 0) : Semiproposition ℒₛₑₜ (n + 1))⌝ ^⋏
          (conjunct 3 (n : V) 1 ⌜(arithTrln.varEqual (v 1) : Semiproposition ℒₛₑₜ (n + 1))⌝ ^⋏ ^⊤))
        (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1]) ⌜(arithTrln.func f : Semisentence ℒₛₑₜ 3)⌝)) 2 := by
  rw [DirectTranslation.varEqual, pquote_allItr, pquote_imp, matrix_conj_two_p]
  simp only [Semiformula.quote_and, pquote_emb, pquote_embSubsts, Nat.cast_ofNat]
  rw [show ∀ {k m : ℕ} (σ : Semiproposition ℒₛₑₜ k) (w : Fin k → SyntacticSemiterm ℒₛₑₜ m),
      Rewriting.app (Rew.subst w) σ = σ ⇜ w from fun _ _ ↦ rfl]
  simp only [pquote_substs, quote_substs']
  rw [pval_vec_shift 3 _ _ (fun j ↦ by simp; omega), pval_vec_shift 3 _ _ (fun j ↦ by simp; omega),
    val_vec_one, val_vec_one]
  simp only [closedVec_val', pvec_val, matrixToVec_succ, matrixToVec_nil, Matrix.vecHead, Matrix.vecTail,
    Matrix.cons_val_zero, Matrix.cons_val_succ, Function.comp_apply, Semiterm.empty_quote_bvar,
    Semiterm.quote_bvar, Semiformula.quote_verum, conjunct, cDomN_eq, val_addCast', Fin.val_addNat,
    Nat.cast_ofNat]
  simp

lemma iVE_pquote2 {n : ℕ} (f : (ℒₒᵣ).Func 2) (v : Fin 2 → SyntacticSemiterm ℒₒᵣ n)
    (h0 : iVE (n : V) ⌜v 0⌝ = ⌜(arithTrln.varEqual (v 0) : Semiproposition ℒₛₑₜ (n + 1))⌝)
    (h1 : iVE (n : V) ⌜v 1⌝ = ⌜(arithTrln.varEqual (v 1) : Semiproposition ℒₛₑₜ (n + 1))⌝) :
    iVE (n : V) ⌜(Semiterm.func f v : SyntacticSemiterm ℒₒᵣ n)⌝ =
      ⌜(arithTrln.varEqual (Semiterm.func f v) : Semiproposition ℒₛₑₜ (n + 1))⌝ := by
  rw [iVE_pfunc_lhs2, pvarEqual_rhs2, h0, h1, ← cFunc_quote2]
  simp [ve2]

lemma iVE_pquote0 {n : ℕ} (f : (ℒₒᵣ).Func 0) (v : Fin 0 → SyntacticSemiterm ℒₒᵣ n) :
    iVE (n : V) ⌜(Semiterm.func f v : SyntacticSemiterm ℒₒᵣ n)⌝ =
      ⌜(arithTrln.varEqual (Semiterm.func f v) : Semiproposition ℒₛₑₜ (n + 1))⌝ := by
  have hu := pquote_isUTerm (V := V) (Semiterm.func f v : SyntacticSemiterm ℒₒᵣ n)
  rw [Semiterm.quote_func] at hu ⊢
  simp only [Nat.cast_zero] at hu ⊢
  obtain ⟨hf, hv⟩ := IsUTerm.func_iff.mp hu
  rw [iVE, iVE.construction.result_func' hf hv]
  simp only [iVE.construction, ite_true, ve0]
  rw [DirectTranslation.varEqual, allItr_zero, pquote_imp, matrix_conj_zero_p,
    Semiformula.quote_verum, pquote_embSubsts]
  simp only [pvec_val, matrixToVec_succ, matrixToVec_nil, Matrix.vecHead, Matrix.cons_val_zero,
    Semiterm.quote_bvar, Fin.val_addNat]
  rw [cFunc_quote0]
  simp

/-- **内部变量等式的正确性（带自由变量）**：对每个项 t，`iVE n ⌜t⌝ = ⌜varEqual t⌝`。 -/
theorem iVE_pquote {n : ℕ} : ∀ t : SyntacticSemiterm ℒₒᵣ n,
    iVE (n : V) ⌜t⌝ = ⌜(arithTrln.varEqual t : Semiproposition ℒₛₑₜ (n + 1))⌝
  | #x => iVE_pquote_bvar x
  | &x => iVE_pquote_fvar x
  | FFL.FirstOrder.Semiterm.func Language.ORing.Func.zero v => iVE_pquote0 _ v
  | FFL.FirstOrder.Semiterm.func Language.ORing.Func.one v => iVE_pquote0 _ v
  | FFL.FirstOrder.Semiterm.func Language.ORing.Func.add v =>
    iVE_pquote2 _ v (iVE_pquote (v 0)) (iVE_pquote (v 1))
  | FFL.FirstOrder.Semiterm.func Language.ORing.Func.mul v =>
    iVE_pquote2 _ v (iVE_pquote (v 0)) (iVE_pquote (v 1))

end term

/-! ## 原子公式与公式归纳 -/

section formula

lemma ptranslateRel_quote2 {n : ℕ} (R : (ℒₒᵣ).Rel 2) (v : Fin 2 → SyntacticSemiterm ℒₒᵣ n) :
    (⌜(arithTrln.translateRel R v : Semiproposition ℒₛₑₜ n)⌝ : V) =
      qqAlls (imp ℒₛₑₜ
        (conjunct 2 (n : V) 0 ⌜(arithTrln.varEqual (v 0) : Semiproposition ℒₛₑₜ (n + 1))⌝ ^⋏
          (conjunct 2 (n : V) 1 ⌜(arithTrln.varEqual (v 1) : Semiproposition ℒₛₑₜ (n + 1))⌝ ^⋏ ^⊤))
        (subst ℒₛₑₜ ?[^#0, ^#1] ⌜(arithTrln.rel R : Semisentence ℒₛₑₜ 2)⌝)) 2 := by
  rw [DirectTranslation.translateRel, pquote_allItr, pquote_imp, matrix_conj_two_p]
  simp only [Semiformula.quote_and, pquote_emb, pquote_embSubsts, Nat.cast_ofNat]
  rw [show ∀ {k m : ℕ} (σ : Semiproposition ℒₛₑₜ k) (w : Fin k → SyntacticSemiterm ℒₛₑₜ m),
      Rewriting.app (Rew.subst w) σ = σ ⇜ w from fun _ _ ↦ rfl]
  simp only [pquote_substs, quote_substs']
  rw [pval_vec_shift 2 _ _ (fun j ↦ by simp; omega), pval_vec_shift 2 _ _ (fun j ↦ by simp; omega),
    val_vec_one, val_vec_one]
  simp only [closedVec_val', pvec_val, matrixToVec_succ, matrixToVec_nil, Matrix.vecHead,
    Matrix.vecTail, Function.comp_apply, Semiterm.empty_quote_bvar, Semiterm.quote_bvar,
    Semiformula.quote_verum, conjunct, cDomN_eq, val_addCast', Nat.cast_ofNat]
  simp

/-- **原子翻译的正确性（带自由变量）**。 -/
lemma iTR_pquote {n : ℕ} (R : (ℒₒᵣ).Rel 2) (v : Fin 2 → SyntacticSemiterm ℒₒᵣ n) :
    iTR (n : V) 2 ⌜R⌝ (SemitermVec.val fun i ↦ (⌜v i⌝ : Bootstrapping.Semiterm V ℒₒᵣ n)) =
      ⌜(arithTrln.translateRel R v : Semiproposition ℒₛₑₜ n)⌝ := by
  have e0 : (SemitermVec.val fun i ↦ (⌜v i⌝ : Bootstrapping.Semiterm V ℒₒᵣ n)).[0] = ⌜v 0⌝ := by
    rw [pvec_val]; simpa using matrixToVec_nth (fun i ↦ (⌜v i⌝ : V)) 0
  have e1 : (SemitermVec.val fun i ↦ (⌜v i⌝ : Bootstrapping.Semiterm V ℒₒᵣ n)).[1] = ⌜v 1⌝ := by
    rw [pvec_val]; simpa using matrixToVec_nth (fun i ↦ (⌜v i⌝ : V)) 1
  rw [ptranslateRel_quote2, iTR, e0, e1, iVE_pquote, iVE_pquote, cRel_quote]

lemma pquote_isUFormula {n : ℕ} (φ : Semiproposition ℒₒᵣ n) : IsUFormula ℒₒᵣ (⌜φ⌝ : V) :=
  (Semiformula.quote_isSemiformula φ).isUFormula

lemma iT_pquote_rel {n : ℕ} (R : (ℒₒᵣ).Rel 2) (v : Fin 2 → SyntacticSemiterm ℒₒᵣ n) :
    iT (n : V) ⌜(FFL.FirstOrder.Semiformula.rel R v : Semiproposition ℒₒᵣ n)⌝ =
      ⌜(arithTrln.translate (FFL.FirstOrder.Semiformula.rel R v) : Semiproposition ℒₛₑₜ n)⌝ := by
  have hu := pquote_isUFormula (V := V) (FFL.FirstOrder.Semiformula.rel R v : Semiproposition ℒₒᵣ n)
  rw [Semiformula.quote_rel] at hu ⊢
  simp only [Nat.cast_ofNat] at hu ⊢
  obtain ⟨hR, hv⟩ := IsUFormula.rel.mp hu
  rw [iT_rel hR hv, iTR_pquote, DirectTranslation.translate_rel]

lemma iT_pquote_nrel {n : ℕ} (R : (ℒₒᵣ).Rel 2) (v : Fin 2 → SyntacticSemiterm ℒₒᵣ n) :
    iT (n : V) ⌜(FFL.FirstOrder.Semiformula.nrel R v : Semiproposition ℒₒᵣ n)⌝ =
      ⌜(arithTrln.translate (FFL.FirstOrder.Semiformula.nrel R v) : Semiproposition ℒₛₑₜ n)⌝ := by
  have hu := pquote_isUFormula (V := V) (FFL.FirstOrder.Semiformula.nrel R v : Semiproposition ℒₒᵣ n)
  rw [Semiformula.quote_nrel] at hu ⊢
  simp only [Nat.cast_ofNat] at hu ⊢
  obtain ⟨hR, hv⟩ := IsUFormula.nrel.mp hu
  rw [iT_nrel hR hv, iTR_pquote, DirectTranslation.translate_nrel, pquote_neg]

lemma pquote_domain_zero {n : ℕ} :
    (⌜(Rewriting.app (Rew.emb : Rew ℒₛₑₜ Empty (n + 1) ℕ (n + 1))
        (arithTrln.domain/[#0]) : Semiproposition ℒₛₑₜ (n + 1))⌝ : V) = domZero := by
  rw [pquote_emb, quote_substs', val_vec_one]
  simp [domZero, cDomN_eq]

lemma pquote_fal {n : ℕ} (φ : Semiproposition ℒₛₑₜ (n + 1)) :
    (⌜(DirectTranslation.fal arithTrln φ : Semiproposition ℒₛₑₜ n)⌝ : V) =
      ^∀ (imp ℒₛₑₜ domZero ⌜φ⌝) := by
  rw [DirectTranslation.fal, FFL.FirstOrder.ball, Semiformula.quote_all, pquote_imp, pquote_domain_zero]

lemma pquote_exs {n : ℕ} (φ : Semiproposition ℒₛₑₜ (n + 1)) :
    (⌜(DirectTranslation.exs arithTrln φ : Semiproposition ℒₛₑₜ n)⌝ : V) =
      ^∃ (domZero ^⋏ ⌜φ⌝) := by
  rw [DirectTranslation.exs, FFL.FirstOrder.bexs, Semiformula.quote_ex, Semiformula.quote_and,
    pquote_domain_zero]

/-- **内部翻译的正确性（带自由变量）**：对每个算术公式 φ（层数 n，可含自由变量），
`iT n ⌜φ⌝ = ⌜arithTrln.translate φ⌝`。 -/
theorem iT_pquote : ∀ {n : ℕ} (φ : Semiproposition ℒₒᵣ n),
    iT (n : V) ⌜φ⌝ = ⌜(arithTrln.translate φ : Semiproposition ℒₛₑₜ n)⌝
  | _, FFL.FirstOrder.Semiformula.rel Language.ORing.Rel.eq v => iT_pquote_rel _ v
  | _, FFL.FirstOrder.Semiformula.rel Language.ORing.Rel.lt v => iT_pquote_rel _ v
  | _, FFL.FirstOrder.Semiformula.nrel Language.ORing.Rel.eq v => iT_pquote_nrel _ v
  | _, FFL.FirstOrder.Semiformula.nrel Language.ORing.Rel.lt v => iT_pquote_nrel _ v
  | _, ⊤ => by
    rw [Semiformula.quote_verum, iT_verum, LogicalConnective.HomClass.map_top, Semiformula.quote_verum]
  | _, ⊥ => by
    rw [Semiformula.quote_falsum, iT_falsum, LogicalConnective.HomClass.map_bot,
      Semiformula.quote_falsum]
  | _, φ ⋏ ψ => by
    rw [Semiformula.quote_and, iT_and (pquote_isUFormula φ) (pquote_isUFormula ψ),
      iT_pquote φ, iT_pquote ψ, LogicalConnective.HomClass.map_and, Semiformula.quote_and]
  | _, φ ⋎ ψ => by
    rw [Semiformula.quote_or, iT_or (pquote_isUFormula φ) (pquote_isUFormula ψ),
      iT_pquote φ, iT_pquote ψ, LogicalConnective.HomClass.map_or, Semiformula.quote_or]
  | _, ∀¹ φ => by
    rw [Semiformula.quote_all, iT_all (pquote_isUFormula φ), ← Nat.cast_succ, iT_pquote φ,
      DirectTranslation.translate_all, pquote_fal]
  | _, ∃¹ φ => by
    rw [Semiformula.quote_ex, iT_exs (pquote_isUFormula φ), ← Nat.cast_succ, iT_pquote φ,
      DirectTranslation.translate_ex, pquote_exs]

end formula

end GodelQ.OpenTranslate

#print axioms GodelQ.OpenTranslate.iVE_pquote
#print axioms GodelQ.OpenTranslate.iT_pquote
