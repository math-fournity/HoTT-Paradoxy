import GodelQ.ZFC.SetLanguage
import Foundation.FirstOrder.SetTheory.Schemata
import Foundation.FirstOrder.Incompleteness.Definability

/-!
# CG-006 · S2b：ℒₛₑₜ 上“公理模式”的 Δ1 识别（通用部分）与分离模式 `𝗦𝗘𝗣`

仿 Foundation `Incompleteness/Definability.lean` 中归纳模式的做法（`InductionR`、`chInd`、
`inductionR_quote_iff`、`InductionScheme.delta1_of`），但对 ℒₛₑₜ 写成通用形式：

* `SchemaR n F p`：`p` 编码 `∀¹* β`，`β` 无自由变量，把 `β` 的约束变量换成自由变量后，
  其编码等于 `F K`，`K` 是某个 n 元公式的编码。`F` 是“由公式编码算出公理主体编码”的函数。
* `chSchema n G`：它的 Δ1 定义（`G` 是 `F` 的 Σ1 图）。
* `schemaR_quote_iff`：在 ℕ 中，`SchemaR n F ⌜φ⌝` 恰好说 `φ` 是某个 `(body ψ).univCl`。
* `schemaDelta1`：由以上得到理论的 `Theory.Δ₁` 实例。

分离模式：`sepBodyVal k = ^∀ ^∃ ^∀ (⌜z∈y⌝ ↔ ⌜z∈x⌝ ∧ k)`。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping SetTheory
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.ZFCDelta1

section general

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## ℒₛₑₜ 版的两条通用引理（Foundation 只给了 ℒₒᵣ 版） -/

lemma fvarVec_val_eq_set (m : ℕ) :
    fvarVec ((m : ℕ) : V)
      = SemitermVec.val
          (fun i : Fin m ↦ (Semiterm.fvar (↑(i : ℕ)) : Bootstrapping.Semiterm V ℒₛₑₜ 0)) := by
  apply nth_ext (by simp)
  intro i hi
  rw [len_fvarVec] at hi
  obtain ⟨j, rfl⟩ := eq_nat_of_lt_nat hi
  have hj : j < m := by exact_mod_cast hi
  rw [nth_fvarVec _ _ hi, show ((j : ℕ) : V) = ((⟨j, hj⟩ : Fin m) : ℕ) from rfl,
    SemitermVec.val_nth_eq
      (fun i : Fin m ↦ (Semiterm.fvar (↑(i : ℕ)) : Bootstrapping.Semiterm V ℒₛₑₜ 0)) ⟨j, hj⟩]
  simp

lemma subst_fvarVec_quote {m : ℕ} (β : SetTheorySemiproposition m) :
    Bootstrapping.subst ℒₛₑₜ (fvarVec ((m : ℕ) : V)) (⌜β⌝ : V)
      = (⌜(β ⇜ (fun i : Fin m ↦ (&↑i : SyntacticTerm ℒₛₑₜ)))⌝ : V) := by
  rw [fvarVec_val_eq_set]
  change ((⌜β⌝ : Bootstrapping.Semiformula V ℒₛₑₜ m).subst _).val
    = (⌜β ⇜ (fun i : Fin m ↦ (&↑i : SyntacticTerm ℒₛₑₜ))⌝ : Bootstrapping.Semiformula V ℒₛₑₜ 0).val
  simp [FirstOrder.Semiformula.typed_quote_substs, Semiterm.typed_quote_fvar]

/-! ## 通用的模式识别谓词及其 Δ1 定义 -/

def SchemaR (n : ℕ) (F : V → V) (p : V) : Prop :=
  ∃ m ≤ p, ∃ b ≤ p,
    p = qqAlls b m ∧ IsUFormula ℒₛₑₜ b ∧ shift ℒₛₑₜ b = b ∧ bv ℒₛₑₜ b = m
    ∧ ∃ K ≤ subst ℒₛₑₜ (fvarVec m) b,
        IsSemiformula ℒₛₑₜ (n : V) K ∧ subst ℒₛₑₜ (fvarVec m) b = F K

noncomputable def chSchema (n : ℕ) (G : 𝚺ᴬ₁.Semisentence 2) : 𝚫ᴬ₁.Semisentence 1 := .mkDelta
  (.mkSigma “p.
    ∃ m < p + 1, ∃ b < p + 1,
      !qqAllsDef p b m ∧ !(isUFormula ℒₛₑₜ).sigma b
      ∧ !(shiftGraph ℒₛₑₜ) b b ∧ !(bvGraph ℒₛₑₜ) m b
      ∧ ∃ fv, !fvarVecDef fv m ∧ ∃ s, !(substsGraph ℒₛₑₜ) s fv b
        ∧ ∃ K < s + 1, !(isSemiformula ℒₛₑₜ).sigma ↑n K ∧ !G s K”)
  (.mkPi “p.
    ∃ m < p + 1, ∃ b < p + 1,
      (∀ y, !qqAllsDef y b m → y = p) ∧ !(isUFormula ℒₛₑₜ).pi b
      ∧ (∀ y, !(shiftGraph ℒₛₑₜ) y b → y = b)
      ∧ (∀ y, !(bvGraph ℒₛₑₜ) y b → y = m)
      ∧ ∀ fv, !fvarVecDef fv m → ∀ s, !(substsGraph ℒₛₑₜ) s fv b
        → ∃ K < s + 1, !(isSemiformula ℒₛₑₜ).pi ↑n K ∧ ∀ ib, !G ib K → s = ib”)

instance SchemaR.defined {n : ℕ} {F : V → V} {G : 𝚺ᴬ₁.Semisentence 2}
    [hG : 𝚺ᴬ₁-Function₁ F via G] :
    𝚫ᴬ₁-Predicate[V] (SchemaR n F : V → Prop) via chSchema n G := .mk <| by
  constructor
  · intro v
    simp [chSchema, Bounding.HierarchySymbol.Semiformula.val_sigma, eq_comm, numeral_eq_natCast]
  · intro v
    simp [chSchema, Bounding.HierarchySymbol.Semiformula.val_sigma, SchemaR, lt_succ_iff_le,
      eq_comm, numeral_eq_natCast]

end general

/-- 复制自 Foundation 的私有引理 `allClosure_eq_univCl'`（ℒₛₑₜ 版）。 -/
lemma allClosure_eq_univCl'_set {m : ℕ} (β : SetTheorySemiproposition m)
    (hfree : β.freeVariables = ∅) (hbv : bv ℒₛₑₜ (⌜β⌝ : ℕ) = m) :
    (∀¹* β : SetTheorySemiproposition 0)
      = (β ⇜ fun i : Fin m ↦ (&↑i : SyntacticTerm ℒₛₑₜ)).univCl' := by
  obtain ⟨χ, hχ⟩ : ∃ χ, β ⇜ (fun i : Fin m ↦ (&↑i : SyntacticTerm ℒₛₑₜ)) = χ := ⟨_, rfl⟩
  rw [hχ]
  have hcodeβ : (⌜(Rew.fixitr 0 m ▹ χ : SetTheorySemiproposition (0 + m))⌝ : ℕ) = ⌜β⌝ := by
    have : (Rew.fixitr 0 m ▹ χ : SetTheorySemiproposition (0 + m))
        = Rew.castLE (Nat.le_add_left m 0) ▹ β := by
      rw [← hχ, ← TransitiveRewriting.comp_app]
      apply Semiformula.rew_eq_of_funEqOn
      · intro x; simp [Rew.comp_app, Rew.fixitr_fvar, Fin.ext_iff]
      · intro x hx; simp [Semiformula.FVar?, hfree] at hx
    rw [this, Semiformula.quote_castLE]
  have hfvle : χ.fvSup ≤ m := by
    by_contra! h
    have hx := Semiformula.fvar?_fvSup_pred χ (by omega)
    rw [← hχ] at hx
    rcases Semiformula.fvar?_rew hx with (⟨i, hi⟩ | ⟨z, hz, -⟩)
    · have : χ.fvSup - 1 = i := by
        simpa [hχ, Rew.subst_bvar, Semiterm.FVar?, Semiterm.freeVariables_fvar] using hi
      omega
    · simp [Semiformula.FVar?, hfree] at hz
  have hcode : (⌜(Rew.fixitr 0 m ▹ χ : SetTheorySemiproposition (0 + m))⌝ : ℕ)
      = ⌜(Rew.fixitr 0 χ.fvSup ▹ χ : SetTheorySemiproposition (0 + χ.fvSup))⌝ := by
    have : (Rew.fixitr 0 m ▹ χ : SetTheorySemiproposition (0 + m))
        = Rew.castLE (by omega : 0 + χ.fvSup ≤ 0 + m) ▹ (Rew.fixitr 0 χ.fvSup ▹ χ) := by
      rw [← TransitiveRewriting.comp_app]
      apply Semiformula.rew_eq_of_funEqOn₀
      intro x hx
      have := Semiformula.lt_fvSup_of_fvar? hx
      simp [Rew.comp_app, Rew.fixitr_fvar, this, show x < m by omega]
    rw [this, Semiformula.quote_castLE]
  have hm : m = χ.fvSup := by rw [← hbv, ← hcodeβ, hcode]; exact bv_quote_fixitr χ
  apply (Semiformula.quote_inj_iff (V := ℕ)).mp
  rw [quote_allClosure, Semiformula.univCl', quote_allClosure, ← hcodeβ, hcode, hm]
  simp

/-- 通用的编码判定：`SchemaR n F ⌜φ⌝` 恰好说 `φ` 是某个 `(body ψ).univCl`。 -/
lemma schemaR_quote_iff {n : ℕ}
    {F : ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁], V → V}
    (body : SetTheorySemiproposition n → SetTheorySemiproposition 0)
    (hF : ∀ ψ, F ℕ (⌜ψ⌝ : ℕ) = (⌜body ψ⌝ : ℕ))
    (hle : ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (k : V), k ≤ F V k)
    (φ : SetTheorySemiproposition 0) :
    SchemaR n (F ℕ) (⌜φ⌝ : ℕ) ↔ ∃ ψ : SetTheorySemiproposition n, φ = (body ψ).univCl := by
  constructor
  · rintro ⟨m, -, b, -, hp, hU, hsh, hbv, K, -, hK, hsubst⟩
    have hK' : IsSemiformula ℒₛₑₜ n K := by simpa using hK
    obtain ⟨γ, rfl⟩ := IsSemiformula.sound hK'
    obtain ⟨β, rfl⟩ := IsSemiformula.sound (hbv ▸ hU.isSemiformula)
    have hβγ : β ⇜ (fun i : Fin m ↦ (&↑i : SyntacticTerm ℒₛₑₜ)) = body γ :=
      (Semiformula.quote_inj_iff (V := ℕ)).mp <| by
        simpa [hsubst, hF] using (subst_fvarVec_quote (V := ℕ) β).symm
    have hφ : φ = ∀¹* β := (Semiformula.quote_inj_iff (V := ℕ)).mp <| by
      simp [hp, quote_allClosure]
    have hfree : β.freeVariables = ∅ := Semiformula.freeVariables_eq_empty_of_shift_eq <|
      (Semiformula.quote_inj_iff (V := ℕ)).mp <| by rw [Semiformula.quote_shift]; exact hsh
    exact ⟨γ, by simp [hφ, allClosure_eq_univCl'_set β hfree hbv, hβγ]⟩
  · rintro ⟨ψ, rfl⟩
    set χ := body ψ
    have hs : subst ℒₛₑₜ (fvarVec (0 + χ.fvSup : ℕ))
        (⌜(Rew.fixitr 0 χ.fvSup ▹ χ : SetTheorySemiproposition (0 + χ.fvSup))⌝ : ℕ)
          = F ℕ (⌜ψ⌝ : ℕ) := by
      simpa [quote_subst_fvar_fixitr, hF]
        using subst_fvarVec_quote (V := ℕ) (Rew.fixitr 0 χ.fvSup ▹ χ)
    rw [Semiformula.coe_univCl_eq_univCl', quote_univCl', natCast_nat]
    exact ⟨_, index_le_qqAlls _ _, _, le_qqAlls _ _, rfl,
      (Semiformula.quote_isSemiformula _).isUFormula, quote_shift_fixitr χ,
      (bv_quote_fixitr χ).trans (zero_add _).symm, ⌜ψ⌝, by rw [hs]; exact hle ℕ _,
      by simpa using (Semiformula.quote_isSemiformula (V := ℕ) ψ), hs⟩

/-- 由编码函数与它的 Σ1 图，得到一个公理模式理论的 `Theory.Δ₁` 实例。 -/
noncomputable abbrev schemaDelta1 {n : ℕ} (T : SetTheory) (G : 𝚺ᴬ₁.Semisentence 2)
    (F : ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁], V → V)
    (hG : ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁], 𝚺ᴬ₁-Function₁ (F V) via G)
    (hmem : ∀ φ : SetTheorySemiproposition 0, SchemaR n (F ℕ) (⌜φ⌝ : ℕ) ↔ ∃ σ ∈ T, φ = σ) :
    T.Δ₁ where
  ch := chSchema n G
  mem_iff φ := by
    have := hG ℕ
    simpa using hmem φ
  isDelta1 :=
    Bounding.HierarchySymbol.Semiformula.ProvablyProperOn.arithmetic_ofProperOn.{0} _
      fun V _ _ ↦ (SchemaR.defined (hG := hG V)).proper

/-! ## 分离模式 -/

section separation

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 分离公理主体（未闭包）。 -/
def sepBody (φ : SetTheorySemiproposition 1) : SetTheorySemiproposition 0 :=
  “∀ x, ∃ y, ∀ z, z ∈ y ↔ z ∈ x ∧ !φ z”

lemma separationSchema_eq (φ : SetTheorySemiproposition 1) :
    Axiom.separationSchema φ = (sepBody φ).univCl := rfl

/-- `φ ⇜ ![#0]` 只是把唯一的约束变量放进更深的层。 -/
lemma substs_bvar_zero_eq_castLE (φ : SetTheorySemiproposition 1) :
    (φ ⇜ ![(#0 : SyntacticSemiterm ℒₛₑₜ 3)]) = Rew.castLE (by omega : 1 ≤ 3) ▹ φ := by
  show Rew.subst _ ▹ φ = _
  apply Semiformula.rew_eq_of_funEqOn
  · intro x
    match x with
    | ⟨0, _⟩ => rfl
  · intro x _
    simp [Function.comp]

lemma quote_substs_bvar_zero (φ : SetTheorySemiproposition 1) :
    (⌜(φ ⇜ ![(#0 : SyntacticSemiterm ℒₛₑₜ 3)])⌝ : ℕ) = ⌜φ⌝ := by
  rw [substs_bvar_zero_eq_castLE, Semiformula.quote_castLE]

noncomputable def memZY : ℕ := ⌜(“z y x. z ∈ y” : SetTheorySemiproposition 3)⌝
noncomputable def memZX : ℕ := ⌜(“z y x. z ∈ x” : SetTheorySemiproposition 3)⌝

/-- 由公式编码 `k` 算出分离公理主体的编码。 -/
noncomputable def sepBodyVal (k : V) : V :=
  ^∀ ^∃ ^∀ (iff ℒₛₑₜ ↑memZY (↑memZX ^⋏ k))

lemma le_sepBodyVal (k : V) : k ≤ sepBodyVal k := by
  have h1 : k < (↑memZX ^⋏ k : V) := lt_K!_right _ _
  have h2 : (↑memZX ^⋏ k : V) < imp ℒₛₑₜ (↑memZY : V) (↑memZX ^⋏ k) := by
    unfold imp; exact lt_or_right _ _
  have h3 : imp ℒₛₑₜ (↑memZY : V) (↑memZX ^⋏ k) < iff ℒₛₑₜ (↑memZY : V) (↑memZX ^⋏ k) := by
    unfold iff; exact lt_K!_left _ _
  unfold sepBodyVal
  exact (h1.trans (h2.trans h3)).le.trans <|
    (lt_forall _).le.trans <| (lt_exists _).le.trans (lt_forall _).le

lemma sepBodyVal_quote (φ : SetTheorySemiproposition 1) :
    sepBodyVal (⌜φ⌝ : ℕ) = (⌜sepBody φ⌝ : ℕ) := by
  have e : (⌜sepBody φ⌝ : Bootstrapping.Semiformula ℕ ℒₛₑₜ 0) =
      ∀¹ ∃¹ ∀¹ (⌜(“z y x. z ∈ y” : SetTheorySemiproposition 3)⌝ 🡘
        (⌜(“z y x. z ∈ x” : SetTheorySemiproposition 3)⌝ ⋏
          ⌜φ ⇜ ![(#0 : SyntacticSemiterm ℒₛₑₜ 3)]⌝)) := by
    unfold sepBody
    simp
  change _ = (⌜sepBody φ⌝ : Bootstrapping.Semiformula ℕ ℒₛₑₜ 0).val
  rw [e]
  generalize hC : (⌜φ ⇜ ![(#0 : SyntacticSemiterm ℒₛₑₜ 3)]⌝ : Bootstrapping.Semiformula ℕ ℒₛₑₜ 3) = C
  have hCv : C.val = (⌜φ⌝ : ℕ) := by
    rw [← hC]
    change (⌜φ ⇜ ![(#0 : SyntacticSemiterm ℒₛₑₜ 3)]⌝ : ℕ) = _
    exact quote_substs_bvar_zero φ
  simp [sepBodyVal, memZY, memZX]
  rw [hCv]
  rfl

noncomputable def sepBodyValGraph : 𝚺ᴬ₁.Semisentence 2 := .mkSigma
  “y k.
    ∃ a, !qqAndDef a ↑memZX k ∧
    ∃ i, !(iffGraph ℒₛₑₜ) i ↑memZY a ∧
    ∃ q1, !qqAllDef q1 i ∧
    ∃ q2, !qqExsDef q2 q1 ∧
    !qqAllDef y q2”

instance sepBodyVal.defined : 𝚺ᴬ₁-Function₁ (sepBodyVal : V → V) via sepBodyValGraph :=
  .mk fun v ↦ by simp [sepBodyValGraph, numeral_eq_natCast, sepBodyVal]

end separation

lemma mem_separation_iff (σ : Sentence ℒₛₑₜ) :
    σ ∈ 𝗦𝗘𝗣 ↔ ∃ ψ : SetTheorySemiproposition 1, σ = (sepBody ψ).univCl := by
  constructor
  · rintro ⟨ψ⟩; exact ⟨ψ, rfl⟩
  · rintro ⟨ψ, rfl⟩; exact Separation.separation ψ

/-- **分离模式是 Δ1 的。** -/
noncomputable instance Separation.delta1 : (𝗦𝗘𝗣 : SetTheory).Δ₁ :=
  schemaDelta1 (n := 1) 𝗦𝗘𝗣 sepBodyValGraph (fun V _ _ ↦ sepBodyVal (V := V))
    (fun V _ _ ↦ sepBodyVal.defined) fun φ ↦ by
      rw [schemaR_quote_iff (F := fun V _ _ ↦ sepBodyVal (V := V)) sepBody sepBodyVal_quote
        (fun V _ _ ↦ le_sepBodyVal (V := V))]
      constructor
      · rintro ⟨ψ, rfl⟩; exact ⟨_, Separation.separation ψ, rfl⟩
      · rintro ⟨σ, hσ, rfl⟩
        obtain ⟨ψ, rfl⟩ := (mem_separation_iff σ).mp hσ
        exact ⟨ψ, rfl⟩

#print axioms Separation.delta1

end GodelQ.ZFCDelta1
