import GodelQ.ZFC.SchemaDelta1

/-!
# CG-006 · S2b（二）：替换模式 `𝗥𝗘𝗣𝗟` 是 Δ1 的

`Axiom.replacementSchema φ = (replBody φ).univCl`，
`replBody φ = (∀x ∃!y φ(x,y)) → ∀X ∃Y ∀y (y ∈ Y ↔ ∃x ∈ X, φ(x,y))`。
展开 `∃!`（`Semiformula.existsUnique`）与有界存在（`bexsMem`）之后，φ 出现三次：
`φ ⇜ ![#1,#0]`、`φ ⇜ ![#2,#0]`（两处要内部代换）与 `φ ⇜ ![#0,#1]`（只是 `castLE`，编码不变）。
最后一处使界 `k ≤ replBodyVal k` 结构性成立。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping SetTheory
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.ZFCDelta1

/-! ## 代换的编码（通用） -/

/-- 代换向量 `v` 的编码（与 Foundation 的 `substCode` 同法）。 -/
def vecCode {k n : ℕ} (v : Fin k → SyntacticSemiterm ℒₛₑₜ n) : ℕ :=
  Matrix.vecToNat fun i ↦ Encodable.encode (v i)

lemma vecCode_eq {k n : ℕ} (v : Fin k → SyntacticSemiterm ℒₛₑₜ n) :
    vecCode v = SemitermVec.val (fun i ↦ (⌜v i⌝ : Bootstrapping.Semiterm ℕ ℒₛₑₜ n)) := by
  rw [vecCode, Semiterm.quote_eq_encode' (V := ℕ) v, natCast_nat]

/-- `φ ⇜ v` 的编码由 `φ` 的编码经内部代换算出。 -/
lemma quote_substs_eq {k n : ℕ} (φ : SetTheorySemiproposition k)
    (v : Fin k → SyntacticSemiterm ℒₛₑₜ n) :
    (⌜φ ⇜ v⌝ : ℕ) = subst ℒₛₑₜ ↑(vecCode v) (⌜φ⌝ : ℕ) := by
  change (⌜φ ⇜ v⌝ : Bootstrapping.Semiformula ℕ ℒₛₑₜ n).val = _
  rw [FirstOrder.Semiformula.typed_quote_substs, vecCode_eq]
  rfl

/-! ## 替换公理主体的形状 -/

/-- 等号原子 `#0 = #1`（三元上下文），即 `existsUnique` 里的那个。 -/
def eqF : SetTheorySemiproposition 3 :=
  Semiformula.Operator.operator Semiformula.Operator.Eq.eq ![#0, #1]
/-- 属于原子 `#0 ∈ #1`（三元上下文）。 -/
def memF : SetTheorySemiproposition 3 :=
  Semiformula.Operator.operator Semiformula.Operator.Mem.mem ![#0, #1]
/-- 有界存在里的属于原子 `#0 ∈ bShift #2`（四元上下文）。 -/
def mem2F : SetTheorySemiproposition 4 :=
  Semiformula.Operator.operator Semiformula.Operator.Mem.mem
    (Matrix.vecCons #0 (Matrix.vecCons (Rew.bShift (#2 : SyntacticSemiterm ℒₛₑₜ 3)) Matrix.vecEmpty))

/-- 留出三个公式空位的模板。 -/
def replTemplate (A : SetTheorySemiproposition 2) (B : SetTheorySemiproposition 3)
    (C : SetTheorySemiproposition 4) : SetTheorySemiproposition 0 :=
  (∀¹ (∃¹ (A ⋏ (∀¹ (B 🡒 eqF))))) 🡒 (∀¹ (∃¹ (∀¹ (memF 🡘 (∃¹ (mem2F ⋏ C))))))

/-- 替换公理主体（未闭包）。 -/
def replBody (φ : SetTheorySemiproposition 2) : SetTheorySemiproposition 0 :=
  “(∀ x, ∃! y, !φ x y) → ∀ X, ∃ Y, ∀ y, y ∈ Y ↔ ∃ x ∈ X, !φ x y”

lemma replacementSchema_eq (φ : SetTheorySemiproposition 2) :
    Axiom.replacementSchema φ = (replBody φ).univCl := rfl

lemma replBody_eq (φ : SetTheorySemiproposition 2) :
    replBody φ = replTemplate (φ ⇜ ![#1, #0]) (φ ⇜ ![#2, #0]) (φ ⇜ ![#0, #1]) := by
  have h1 : (φ ⇜ ![(#1 : SyntacticSemiterm ℒₛₑₜ 2), #0])
        ⇜ (Matrix.vecCons #0 fun x ↦ #(BinderNotation.finSuccItr x 1))
      = φ ⇜ ![(#1 : SyntacticSemiterm ℒₛₑₜ 2), #0] := by
    show Rew.subst _ ▹ (Rew.subst _ ▹ φ) = Rew.subst _ ▹ φ
    rw [← TransitiveRewriting.comp_app]
    apply Semiformula.rew_eq_of_funEqOn
    · intro x
      match x with
      | ⟨0, _⟩ => rfl
      | ⟨1, _⟩ => rfl
    · intro x _; simp [Rew.comp_app]
  have h2 : (φ ⇜ ![(#1 : SyntacticSemiterm ℒₛₑₜ 2), #0])
        ⇜ (Matrix.vecCons #0 fun x ↦ (#(BinderNotation.finSuccItr x 2) : SyntacticSemiterm ℒₛₑₜ 3))
      = φ ⇜ ![(#2 : SyntacticSemiterm ℒₛₑₜ 3), #0] := by
    show Rew.subst _ ▹ (Rew.subst _ ▹ φ) = Rew.subst _ ▹ φ
    rw [← TransitiveRewriting.comp_app]
    apply Semiformula.rew_eq_of_funEqOn
    · intro x
      match x with
      | ⟨0, _⟩ => rfl
      | ⟨1, _⟩ => rfl
    · intro x _; simp [Rew.comp_app]
  show replTemplate
      ((φ ⇜ ![(#1 : SyntacticSemiterm ℒₛₑₜ 2), #0])
        ⇜ (Matrix.vecCons #0 fun x ↦ #(BinderNotation.finSuccItr x 1)))
      ((φ ⇜ ![(#1 : SyntacticSemiterm ℒₛₑₜ 2), #0])
        ⇜ (Matrix.vecCons #0 fun x ↦ (#(BinderNotation.finSuccItr x 2) : SyntacticSemiterm ℒₛₑₜ 3)))
      (φ ⇜ ![#0, #1]) = _
  rw [h1, h2]

/-- `φ ⇜ ![#0,#1]`（二元到四元）只是 `castLE`。 -/
lemma substs_bvar01_eq_castLE (φ : SetTheorySemiproposition 2) :
    (φ ⇜ ![(#0 : SyntacticSemiterm ℒₛₑₜ 4), #1]) = Rew.castLE (by omega : 2 ≤ 4) ▹ φ := by
  show Rew.subst _ ▹ φ = _
  apply Semiformula.rew_eq_of_funEqOn
  · intro x
    match x with
    | ⟨0, _⟩ => rfl
    | ⟨1, _⟩ => rfl
  · intro x _
    simp [Function.comp]

lemma quote_substs_bvar01 (φ : SetTheorySemiproposition 2) :
    (⌜(φ ⇜ ![(#0 : SyntacticSemiterm ℒₛₑₜ 4), #1])⌝ : ℕ) = ⌜φ⌝ := by
  rw [substs_bvar01_eq_castLE, Semiformula.quote_castLE]

noncomputable def eqCode : ℕ := ⌜eqF⌝
noncomputable def memCode : ℕ := ⌜memF⌝
noncomputable def mem2Code : ℕ := ⌜mem2F⌝
noncomputable def swapCode : ℕ := vecCode ![(#1 : SyntacticSemiterm ℒₛₑₜ 2), #0]
noncomputable def liftCode : ℕ := vecCode ![(#2 : SyntacticSemiterm ℒₛₑₜ 3), #0]

lemma quote_replTemplate (A : SetTheorySemiproposition 2) (B : SetTheorySemiproposition 3)
    (C : SetTheorySemiproposition 4) :
    (⌜replTemplate A B C⌝ : ℕ)
      = imp ℒₛₑₜ (^∀ ^∃ ((⌜A⌝ : ℕ) ^⋏ ^∀ (imp ℒₛₑₜ (⌜B⌝ : ℕ) ↑eqCode)))
          (^∀ ^∃ ^∀ (iff ℒₛₑₜ ↑memCode (^∃ (↑mem2Code ^⋏ (⌜C⌝ : ℕ))))) := by
  change (⌜replTemplate A B C⌝ : Bootstrapping.Semiformula ℕ ℒₛₑₜ 0).val = _
  simp [replTemplate]
  rfl

section

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 由公式编码 `k` 算出替换公理主体的编码。 -/
noncomputable def replBodyVal (k : V) : V :=
  imp ℒₛₑₜ
    (^∀ ^∃ (subst ℒₛₑₜ ↑swapCode k ^⋏ ^∀ (imp ℒₛₑₜ (subst ℒₛₑₜ ↑liftCode k) ↑eqCode)))
    (^∀ ^∃ ^∀ (iff ℒₛₑₜ ↑memCode (^∃ (↑mem2Code ^⋏ k))))

lemma le_replBodyVal (k : V) : k ≤ replBodyVal k := by
  have h1 : k < (↑mem2Code ^⋏ k : V) := lt_K!_right _ _
  have h2 : (↑mem2Code ^⋏ k : V) < ^∃ (↑mem2Code ^⋏ k) := lt_exists _
  have h3 : (^∃ (↑mem2Code ^⋏ k) : V) < imp ℒₛₑₜ (↑memCode : V) (^∃ (↑mem2Code ^⋏ k)) := by
    unfold imp; exact lt_or_right _ _
  have h4 : imp ℒₛₑₜ (↑memCode : V) (^∃ (↑mem2Code ^⋏ k))
      < iff ℒₛₑₜ (↑memCode : V) (^∃ (↑mem2Code ^⋏ k)) := by
    unfold iff; exact lt_K!_left _ _
  have h5 : (^∀ ^∃ ^∀ (iff ℒₛₑₜ ↑memCode (^∃ (↑mem2Code ^⋏ k))) : V) < replBodyVal k := by
    unfold replBodyVal imp; exact lt_or_right _ _
  exact (h1.trans <| h2.trans <| h3.trans h4).le.trans <|
    (lt_forall _).le.trans <| (lt_exists _).le.trans <| (lt_forall _).le.trans h5.le

noncomputable def replBodyValGraph : 𝚺ᴬ₁.Semisentence 2 := .mkSigma
  “y k.
    ∃ s1, !(substsGraph ℒₛₑₜ) s1 ↑swapCode k ∧
    ∃ s2, !(substsGraph ℒₛₑₜ) s2 ↑liftCode k ∧
    ∃ i1, !(impGraph ℒₛₑₜ) i1 s2 ↑eqCode ∧
    ∃ a1, !qqAllDef a1 i1 ∧
    ∃ w1, !qqAndDef w1 s1 a1 ∧
    ∃ e1, !qqExsDef e1 w1 ∧
    ∃ A, !qqAllDef A e1 ∧
    ∃ w2, !qqAndDef w2 ↑mem2Code k ∧
    ∃ e2, !qqExsDef e2 w2 ∧
    ∃ f, !(iffGraph ℒₛₑₜ) f ↑memCode e2 ∧
    ∃ b1, !qqAllDef b1 f ∧
    ∃ b2, !qqExsDef b2 b1 ∧
    ∃ B, !qqAllDef B b2 ∧
    !(impGraph ℒₛₑₜ) y A B”

instance replBodyVal.defined : 𝚺ᴬ₁-Function₁ (replBodyVal : V → V) via replBodyValGraph :=
  .mk fun v ↦ by simp [replBodyValGraph, numeral_eq_natCast, replBodyVal]

end

lemma replBodyVal_quote (φ : SetTheorySemiproposition 2) :
    replBodyVal (⌜φ⌝ : ℕ) = (⌜replBody φ⌝ : ℕ) := by
  rw [replBody_eq, quote_replTemplate, quote_substs_bvar01,
    quote_substs_eq φ ![(#1 : SyntacticSemiterm ℒₛₑₜ 2), #0],
    quote_substs_eq φ ![(#2 : SyntacticSemiterm ℒₛₑₜ 3), #0]]
  simp only [replBodyVal, natCast_nat]
  rfl

lemma mem_replacement_iff (σ : Sentence ℒₛₑₜ) :
    σ ∈ 𝗥𝗘𝗣𝗟 ↔ ∃ ψ : SetTheorySemiproposition 2, σ = (replBody ψ).univCl := by
  constructor
  · rintro ⟨ψ⟩; exact ⟨ψ, rfl⟩
  · rintro ⟨ψ, rfl⟩; exact Replacement.replacement ψ

/-- **替换模式是 Δ1 的。** -/
noncomputable instance Replacement.delta1 : (𝗥𝗘𝗣𝗟 : SetTheory).Δ₁ :=
  schemaDelta1 (n := 2) 𝗥𝗘𝗣𝗟 replBodyValGraph (fun V _ _ ↦ replBodyVal (V := V))
    (fun V _ _ ↦ replBodyVal.defined) fun φ ↦ by
      rw [schemaR_quote_iff (F := fun V _ _ ↦ replBodyVal (V := V)) replBody replBodyVal_quote
        (fun V _ _ ↦ le_replBodyVal (V := V))]
      constructor
      · rintro ⟨ψ, rfl⟩; exact ⟨_, Replacement.replacement ψ, rfl⟩
      · rintro ⟨σ, hσ, rfl⟩
        obtain ⟨ψ, rfl⟩ := (mem_replacement_iff σ).mp hσ
        exact ⟨ψ, rfl⟩

#print axioms Replacement.delta1

end GodelQ.ZFCDelta1
