import GodelQ.ZFC.Effective

/-!
# CG-006 · S4：𝗭𝗙𝗖 的数字句 Σ1 可靠（经 Foundation 的 `Universe` 模型）

在 `Universe`（Foundation 在 Lean 中构造的 𝗭𝗙𝗖 标准模型）里，ω 恰好是 `{ofNat n}`，于是 ω 上的
算术结构（S3 的翻译）与 ℕ 同构。由“结构双射保持求值”得到：𝗭𝗙𝗖 证明的数字句在 ℕ 中为真，
特别地 `𝗭𝗙𝗖 ⊢ “e 停机” → e 确实停机`。这一步用的是 Lean 元层的模型，与 `zfc_consistent` 相同，
不是 𝗭𝗙𝗖 内部可证的事。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic

namespace GodelQ.ZFCSound

open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.ZFCEff

/-! ## 结构双射保持求值（通用；仿 Foundation 的 `eval_ofEquiv_iff`） -/

section equiv

variable {L : Language} {M₁ M₂ : Type*} [s₁ : Tarski.Structure L M₁] [s₂ : Tarski.Structure L M₂]

lemma val_equiv (Θ : M₁ ≃ M₂)
    (hf : ∀ {k} (f : L.Func k) (v : Fin k → M₁),
      Θ (Tarski.Structure.func f v) = Tarski.Structure.func f (Θ ∘ v))
    {ξ : Type*} {n : ℕ} (b : Fin n → M₂) (ε : ξ → M₂) (t : Semiterm L ξ n) :
    t.val b ε = Θ (t.val (Θ.symm ∘ b) (Θ.symm ∘ ε)) := by
  induction t <;> simp [*, Semiterm.val_func, Function.comp_def]

lemma eval_equiv_iff (Θ : M₁ ≃ M₂)
    (hf : ∀ {k} (f : L.Func k) (v : Fin k → M₁),
      Θ (Tarski.Structure.func f v) = Tarski.Structure.func f (Θ ∘ v))
    (hr : ∀ {k} (r : L.Rel k) (v : Fin k → M₂),
      Tarski.Structure.rel r v ↔ Tarski.Structure.rel r (Θ.symm ∘ v)) :
    ∀ {ξ : Type*} {n : ℕ} {b : Fin n → M₂} {ε : ξ → M₂} {φ : Semiformula L ξ n},
      Semiformula.Eval (s := s₂) b ε φ ↔ Semiformula.Eval (s := s₁) (Θ.symm ∘ b) (Θ.symm ∘ ε) φ
  | _, _, b, ε, .rel r v => by
    simp [Semiformula.eval_rel, hr, val_equiv Θ hf, Function.comp_def]
  | _, _, b, ε, .nrel r v => by
    simp [Semiformula.eval_nrel, hr, val_equiv Θ hf, Function.comp_def]
  | _, _, b, ε, ⊤ => by simp
  | _, _, b, ε, ⊥ => by simp
  | _, _, b, ε, φ ⋏ ψ => by
    simp [eval_equiv_iff Θ hf hr (φ := φ), eval_equiv_iff Θ hf hr (φ := ψ)]
  | _, _, b, ε, φ ⋎ ψ => by
    simp [eval_equiv_iff Θ hf hr (φ := φ), eval_equiv_iff Θ hf hr (φ := ψ)]
  | _, _, b, ε, ∀¹ φ => by
    simp only [Semiformula.eval_all]
    constructor
    · intro h x
      have h' := (eval_equiv_iff Θ hf hr (φ := φ)).mp (h (Θ x))
      simpa only [Matrix.comp_vecCons'', Equiv.symm_apply_apply] using h'
    · intro h y
      apply (eval_equiv_iff Θ hf hr (φ := φ)).mpr
      simpa only [Matrix.comp_vecCons''] using h (Θ.symm y)
  | _, _, b, ε, ∃¹ φ => by
    simp only [Semiformula.eval_ex]
    constructor
    · rintro ⟨y, h⟩
      exact ⟨Θ.symm y, by
        simpa only [Matrix.comp_vecCons''] using (eval_equiv_iff Θ hf hr (φ := φ)).mp h⟩
    · rintro ⟨x, h⟩
      exact ⟨Θ x, (eval_equiv_iff Θ hf hr (φ := φ)).mpr (by
        simpa only [Matrix.comp_vecCons'', Equiv.symm_apply_apply] using h)⟩

end equiv

/-! ## `Universe` 中的 ω 恰是标准数 -/

section universeModel

lemma universe_empty_eq : (∅ : Universe.{0}) = Universe.empty := by
  ext z; simp

lemma universe_succ_eq (x : Universe.{0}) : SetTheory.succ x = x.insert x := by
  ext z; simp [mem_succ_iff]

lemma universe_ofNat_eq (n : ℕ) : (SetTheory.ofNat n : Universe.{0}) = Universe.ofNat n := by
  induction n with
  | zero => exact universe_empty_eq
  | succ n ih =>
    show SetTheory.succ (SetTheory.ofNat n : Universe.{0}) = (Universe.ofNat n).insert (Universe.ofNat n)
    rw [ih, universe_succ_eq]

lemma universe_omega_isInductive : IsInductive (Universe.omega.{0}) := by
  refine ⟨by rw [universe_empty_eq]; exact Universe.empty_mem_omega, fun y hy ↦ ?_⟩
  rw [universe_succ_eq]
  exact Universe.omega_succ hy

lemma universe_mem_ω {x : Universe.{0}} (hx : x ∈ (ω : Universe.{0})) :
    ∃ n : ℕ, x = SetTheory.ofNat n := by
  have h : x ∈ Universe.omega.{0} := universe_omega_isInductive.ω_subset _ hx
  simp only [Universe.omega, Universe.mem_mk, Set.mem_range] at h
  obtain ⟨n, rfl⟩ := h
  exact ⟨n, (universe_ofNat_eq n).symm⟩

end universeModel

/-! ## ℕ 与 `Universe` 的 ω 结构同构 -/

/-- `n ↦ ofNat n`，作为 ω 上算术结构的元素。 -/
noncomputable def natToN (n : ℕ) : N Universe.{0} := toN (SetTheory.ofNat n) (ofNat_mem_ω' n)

@[simp] lemma natToN_val (n : ℕ) : (natToN n).val = (SetTheory.ofNat n : Universe.{0}) := rfl

lemma natToN_injective : Function.Injective natToN := by
  intro a b h
  exact ofNat_injective (V := Universe.{0}) (by simpa using congrArg DirectTranslation.Model.val h)

lemma natToN_surjective : Function.Surjective natToN := by
  intro x
  obtain ⟨n, hn⟩ := universe_mem_ω (val_mem_ω x)
  exact ⟨n, DirectTranslation.Model.ext (by simp [hn])⟩

/-- 同构 `ℕ ≃ N Universe`。 -/
noncomputable def natEquivN : ℕ ≃ N Universe.{0} :=
  Equiv.ofBijective natToN ⟨natToN_injective, natToN_surjective⟩

lemma natEquivN_apply (n : ℕ) : natEquivN n = natToN n := rfl

lemma vec2_natToN (v : Fin 2 → ℕ) : (natToN ∘ v) = ![natToN (v 0), natToN (v 1)] :=
  funext fun i ↦ match i with | 0 => rfl | 1 => rfl

lemma natEquivN_func {k} (f : (ℒₒᵣ).Func k) (v : Fin k → ℕ) :
    natEquivN (Tarski.Structure.func f v) = Tarski.Structure.func f (natEquivN ∘ v) := by
  simp only [natEquivN_apply]
  show natToN (Tarski.Structure.func f v) = Tarski.Structure.func f (natToN ∘ v)
  cases f with
  | zero =>
    rw [func_zero]; apply DirectTranslation.Model.ext; rfl
  | one =>
    rw [func_one]; apply DirectTranslation.Model.ext; rfl
  | add =>
    rw [vec2_natToN, func_add]; apply DirectTranslation.Model.ext
    show (SetTheory.ofNat (v 0 + v 1) : Universe.{0}) = add (SetTheory.ofNat (v 0)) (SetTheory.ofNat (v 1))
    exact (add_ofNat (v 0) (v 1)).symm
  | mul =>
    rw [vec2_natToN, func_mul]; apply DirectTranslation.Model.ext
    show (SetTheory.ofNat (v 0 * v 1) : Universe.{0}) = mul (SetTheory.ofNat (v 0)) (SetTheory.ofNat (v 1))
    exact (mul_ofNat (v 0) (v 1)).symm

lemma ofNat_mem_ofNat_iff (a b : ℕ) :
    (SetTheory.ofNat a : Universe.{0}) ∈ (SetTheory.ofNat b : Universe.{0}) ↔ a < b := by
  rw [mem_ofNat_iff]
  constructor
  · rintro ⟨i, hi, h⟩; rw [ofNat_injective (V := Universe.{0}) h]; exact hi
  · intro h; exact ⟨a, h, rfl⟩

lemma natEquivN_rel {k} (r : (ℒₒᵣ).Rel k) (v : Fin k → N Universe.{0}) :
    Tarski.Structure.rel r v ↔ Tarski.Structure.rel r (natEquivN.symm ∘ v) := by
  obtain ⟨w, rfl⟩ : ∃ w : Fin k → ℕ, v = natEquivN ∘ w :=
    ⟨natEquivN.symm ∘ v, by funext i; exact (natEquivN.apply_symm_apply (v i)).symm⟩
  have hw : natEquivN.symm ∘ (natEquivN ∘ w) = w := by
    funext i; exact natEquivN.symm_apply_apply (w i)
  rw [hw]
  cases r with
  | eq =>
    show Tarski.Structure.rel _ (natToN ∘ w) ↔ w 0 = w 1
    rw [vec2_natToN, DirectTranslation.Model.rel_iff]
    have hv : (fun i ↦ ((![natToN (w 0), natToN (w 1)] i : N Universe.{0}) : Universe.{0}))
        = ![(SetTheory.ofNat (w 0) : Universe.{0}), SetTheory.ofNat (w 1)] :=
      funext fun i ↦ match i with | 0 => rfl | 1 => rfl
    rw [hv]
    exact (eval_relDef_eq (V := Universe.{0}) _ _).trans (ofNat_injective (V := Universe.{0})).eq_iff
  | lt =>
    show Tarski.Structure.rel _ (natToN ∘ w) ↔ w 0 < w 1
    rw [vec2_natToN, rel_lt]
    simpa using ofNat_mem_ofNat_iff (w 0) (w 1)

/-- ω 的算术结构在 `ofNat a` 处与 ℕ 在 `a` 处满足同样的 ℒₒᵣ 公式。 -/
lemma evalN_iff (φ : ArithmeticSemisentence 1) (a : ℕ) :
    (N Universe.{0}) ⊧/![natToN a] φ ↔ ℕ ⊧/![a] φ := by
  have h := eval_equiv_iff natEquivN natEquivN_func natEquivN_rel
    (b := ![natToN a]) (ε := (Empty.elim : Empty → N Universe.{0})) (φ := φ)
  have hb : natEquivN.symm ∘ ![natToN a] = ![a] := by
    funext i; match i with | 0 => exact natEquivN.symm_apply_apply a
  have hε : natEquivN.symm ∘ (Empty.elim : Empty → N Universe.{0}) = Empty.elim := by
    funext x; exact x.elim
  rw [hb, hε] at h
  exact h

/-! ## Σ1 可靠 -/

/-- **𝗭𝗙𝗖 的数字句可靠**：若 𝗭𝗙𝗖 证明 `∃z (Num_a(z) ∧ (codeOfREPred p)⁺(z))`，则 `p a`。 -/
theorem zfc_haltsS_sound {p : ℕ → Prop} (hp : REPred p) {a : ℕ}
    (h : 𝗭𝗙𝗖 ⊢ haltsS (arithTrln.translate (codeOfREPred p)) a) : p a := by
  have hU : Universe.{0}↓[ℒₛₑₜ] ⊧ haltsS (arithTrln.translate (codeOfREPred p)) a :=
    models_of_provable inferInstance h
  have hN := (models_haltsS_iff (M := Universe.{0}) (codeOfREPred p) a).mp hU
  have hℕ : ℕ ⊧/![a] (codeOfREPred p) := (evalN_iff (codeOfREPred p) a).mp hN
  exact (codeOfREPred_spec hp).mp hℕ

/-- `𝗭𝗙𝗖 ⊢ “e 停机”` 恰好当 e 确实停机。 -/
theorem zfc_provesHalts_iff (e : Process) : zfcEffective.provesHalts e ↔ Done e :=
  ⟨fun h ↦ (haltsNat_encode e).mp (zfc_haltsS_sound haltsNat_re h), zfcEffective.sigma1_complete e⟩

/-- **哥德尔 I 的过程形式，含独立性，落在真实的 𝗭𝗙𝗖 上**：存在过程 `d`，它确实永不停机；𝗭𝗙𝗖
对每个 k 证明“d 在 k 步内尚未停机”，既证明不了“d 永不停机”，也证明不了“d 停机”；并且 d 停机
恰好当 𝗭𝗙𝗖 证明它永不停机。 -/
theorem godel_I_process_form_zfc_full :
    ∃ d : Process, ¬ Done d ∧
      (∀ k : ℕ, 𝗭𝗙𝗖 ⊢ haltsS ΨN (Encodable.encode (d, k))) ∧
      𝗭𝗙𝗖 ⊬ neverS ΦH (Encodable.encode d) ∧
      𝗭𝗙𝗖 ⊬ haltsS ΦH (Encodable.encode d) ∧
      (Done d ↔ 𝗭𝗙𝗖 ⊢ neverS ΦH (Encodable.encode d)) := by
  obtain ⟨d, hnd, hall, hna, hiff⟩ := godel_I_process_form_zfc
  refine ⟨d, hnd, hall, hna, ?_, hiff⟩
  intro hH
  exact hnd ((zfc_provesHalts_iff d).mp hH)

end GodelQ.ZFCSound

#print axioms GodelQ.ZFCSound.eval_equiv_iff
#print axioms GodelQ.ZFCSound.zfc_haltsS_sound
#print axioms GodelQ.ZFCSound.godel_I_process_form_zfc_full
