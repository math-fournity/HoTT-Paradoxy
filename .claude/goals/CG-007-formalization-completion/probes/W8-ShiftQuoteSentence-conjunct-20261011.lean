import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

set_option maxHeartbeats 800000

namespace GodelQ.ProbeE

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ══ 1. 引号化句子的码在 shift 下不变 ═══════════════════════════════════════

lemma rew_shift_eq_self {n : ℕ} (φ : Semiproposition ℒₛₑₜ n)
    (hf : ∀ x, ¬ φ.FVar? x) : Rewriting.shift φ = φ :=
  Semiformula.rew_eq_self_of (by intro x; rfl)
    (by intro x hx; exact absurd hx (hf x))

lemma not_fvar_emb {n : ℕ} (σ : Semisentence ℒₛₑₜ n) (x : ℕ) :
    ¬ (σ : Semiproposition ℒₛₑₜ n).FVar? x := by
  intro hx
  have h := Semiformula.lt_fvSup_of_fvar? hx
  rw [Semiformula.fvSup_sentence] at h
  exact absurd h (by simp)

lemma shift_quote_sentence {n : ℕ} (σ : Semisentence ℒₛₑₜ n) :
    shift ℒₛₑₜ (⌜σ⌝ : V) = ⌜σ⌝ := by
  have h : Rewriting.shift (σ : Semiproposition ℒₛₑₜ n) = (σ : Semiproposition ℒₛₑₜ n) :=
    rew_shift_eq_self _ (not_fvar_emb σ)
  rw [show (⌜σ⌝ : V) = ⌜(σ : Semiproposition ℒₛₑₜ n)⌝ from rfl,
      ← Semiformula.quote_shift (V := V) (σ : Semiproposition ℒₛₑₜ n), h]

@[simp] lemma shift_cFuncN (k f : ℕ) :
    shift ℒₛₑₜ ((cFuncN k f : ℕ) : V) = ((cFuncN k f : ℕ) : V) := by
  simp only [cFuncN]
  split <;> split <;>
    · rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote]
      exact shift_quote_sentence _

@[simp] lemma shift_cFunc (k f : V) : shift ℒₛₑₜ (cFunc k f) = cFunc k f := by
  simp only [cFunc]
  split <;> split <;> rw [shift_cFuncN]

@[simp] lemma shift_cDomN : shift ℒₛₑₜ ((cDomN : ℕ) : V) = ((cDomN : ℕ) : V) := by
  rw [show (cDomN : ℕ) = ⌜(arithTrln.domain : Semisentence ℒₛₑₜ 1)⌝ from rfl,
      FFL.FirstOrder.Sentence.coe_quote_eq_quote]
  exact shift_quote_sentence _

@[simp] lemma shift_cRelN (R : ℕ) :
    shift ℒₛₑₜ ((cRelN R : ℕ) : V) = ((cRelN R : ℕ) : V) := by
  simp only [cRelN]
  split <;>
    · rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote]
      exact shift_quote_sentence _

@[simp] lemma shift_cRel (R : V) : shift ℒₛₑₜ (cRel R) = cRel R := by
  simp only [cRel]
  split <;> rw [shift_cRelN]

-- ══ 2. shiftVec 的分量是 bvar，且 termShift 不动它 ════════════════════════

lemma nth_shiftVec (b : V) : ∀ n : V, ∀ i < n, (shiftVec b n).[i] = ^#(b + i) := by
  intro n
  induction n using ISigma1.sigma1_succ_induction
  · definability
  case zero => intro i hi; exact absurd hi (by simp)
  case succ n ih =>
    intro i hi
    rw [shiftVec_succ]
    rcases zero_or_succ i with rfl | ⟨j, rfl⟩
    · simp
    · rw [nth_adjoin_succ]
      have hj : j < n := (add_lt_add_iff_right (a := (1 : V)) (b := j) (c := n)).mp hi
      rw [nth_termBShiftVec (isSemitermVec_shiftVec_V b n).isUTerm hj, ih j hj, termBShift_bvar]
      congr 1
      ring

@[simp] lemma termShiftVec_shiftVec_V (b n : V) :
    termShiftVec ℒₛₑₜ n (shiftVec b n) = shiftVec b n := by
  apply nth_ext' n
  · rw [len_termShiftVec (isSemitermVec_shiftVec_V b n).isUTerm]
  · exact (isSemitermVec_shiftVec_V b n).lh
  · intro i hi
    rw [nth_termShiftVec (isSemitermVec_shiftVec_V b n).isUTerm hi, nth_shiftVec b n i hi,
      termShift_bvar]

-- ══ 3. conjunct 与 shift 交换 ════════════════════════════════════════════

lemma isSemitermVec_shiftVec_cons {b n i : V} (hi : i < b + n) :
    IsSemitermVec ℒₛₑₜ (n + 1) (b + n) (^#i ∷ shiftVec b n) :=
  IsSemitermVec.cons_iff.mpr ⟨IsSemiterm.bvar.mpr hi, isSemitermVec_shiftVec_V b n⟩

lemma shift_conjunct {b n i y : V} (hy : IsSemiformula ℒₛₑₜ (n + 1) y)
    (hi : i < b + n) :
    shift ℒₛₑₜ (conjunct b n i y) = conjunct b n i (shift ℒₛₑₜ y) := by
  have hd : IsSemiformula ℒₛₑₜ 1 ((cDomN : ℕ) : V) := isSemiformula_cDomN
  have hdu : IsUFormula ℒₛₑₜ ((cDomN : ℕ) : V) := hd.isUFormula
  have hyu : IsUFormula ℒₛₑₜ y := hy.isUFormula
  -- 左半：subst ?[^#i] cDomN
  have h1 : shift ℒₛₑₜ (subst ℒₛₑₜ ?[^#i] ((cDomN : ℕ) : V))
      = subst ℒₛₑₜ ?[^#i] ((cDomN : ℕ) : V) := by
    rw [Bootstrapping.shift_substs hd (isSemitermVec_single_bvar (n := i + 1) (by simp)),
      show (termShiftVec ℒₛₑₜ 1 (?[^#i] : V)) = ?[^#i] from by
        rw [show (1 : V) = 0 + 1 by norm_num,
          termShiftVec_cons (IsUTerm.bvar (z := i)) IsUTermVec.empty,
          termShift_bvar, termShiftVec_nil],
      shift_cDomN]
  -- 右半：subst (^#i ∷ shiftVec b n) y
  have h2 : shift ℒₛₑₜ (subst ℒₛₑₜ (^#i ∷ shiftVec b n) y)
      = subst ℒₛₑₜ (^#i ∷ shiftVec b n) (shift ℒₛₑₜ y) := by
    rw [Bootstrapping.shift_substs hy (isSemitermVec_shiftVec_cons hi),
      show (termShiftVec ℒₛₑₜ (n + 1) (^#i ∷ shiftVec b n)) = ^#i ∷ shiftVec b n from by
        rw [termShiftVec_cons (IsUTerm.bvar (z := i)) (isSemitermVec_shiftVec_V b n).isUTerm,
          termShift_bvar, termShiftVec_shiftVec_V]]
  have h1u : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ ?[^#i] ((cDomN : ℕ) : V)) :=
    (IsSemiformula.subst (L := ℒₛₑₜ) hd (isSemitermVec_single_bvar (n := i + 1) (by simp))).isUFormula
  have h2u : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (^#i ∷ shiftVec b n) y) :=
    (IsSemiformula.subst (L := ℒₛₑₜ) hy (isSemitermVec_shiftVec_cons hi)).isUFormula
  show shift ℒₛₑₜ (subst ℒₛₑₜ ?[^#i] ((cDomN : ℕ) : V) ^⋏ subst ℒₛₑₜ (^#i ∷ shiftVec b n) y)
      = subst ℒₛₑₜ ?[^#i] ((cDomN : ℕ) : V) ^⋏ subst ℒₛₑₜ (^#i ∷ shiftVec b n) (shift ℒₛₑₜ y)
  rw [Bootstrapping.shift_and h1u h2u, h1, h2]

end GodelQ.ProbeE
