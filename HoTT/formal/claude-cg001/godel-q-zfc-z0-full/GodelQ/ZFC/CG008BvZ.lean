import GodelQ.ZFC.CG008Bv2

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008BvZ
open GodelQ.ZFCArith GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 第 1 步：`bv_rel` 之后是 `listMax (termBVVec 2 ?[^#0,t])`
example (t : V) (ht : Bootstrapping.IsUTerm ℒₛₑₜ t) :
    Bootstrapping.bv ℒₛₑₜ (Translate.eqAtom t)
      = Arithmetic.listMax (Bootstrapping.termBVVec ℒₛₑₜ 2 (?[^#0, t] : V)) := by
  have hv : Bootstrapping.IsUTermVec ℒₛₑₜ 2 (?[^#0, t] : V) :=
    Bootstrapping.IsUTermVec.mkSeq₂_iff.mpr
      ⟨Bootstrapping.IsUTerm.bvar (L := ℒₛₑₜ) (z := 0), ht⟩
  have hR : (ℒₛₑₜ).IsRel 2 (Translate.cEqN : V) := by
    rw [Translate.cEqN]
    exact (Bootstrapping.isRel_quote_quote (V := V) (L := ℒₛₑₜ) (k := 2)
      (x := Encodable.encode (Language.Eq.eq : (ℒₛₑₜ).Rel 2))).mpr
      ⟨Language.Eq.eq, rfl⟩
  rw [Translate.eqAtom, Bootstrapping.bv_rel hR hv]

-- `termBVVec_nil` 的宇宙不匹配用 `len_zero_iff_eq_nil` 绕开。
lemma termBVVec_nil' : Bootstrapping.termBVVec ℒₛₑₜ (0 : V) (0 : V) = (0 : V) := by
  rw [← Arithmetic.len_zero_iff_eq_nil]
  rw [Bootstrapping.len_termBVVec (k := (0 : V)) (v := (0 : V))
    (Bootstrapping.IsUTermVec.empty (V := V) (L := ℒₛₑₜ))]

/-- 第 2 步：`termBVVec ℒₛₑₜ 2 ?[^#0, t] = ?[termBV ^#0, termBV t]`。 -/
theorem termBVVec_eqAtom (t : V) (ht : Bootstrapping.IsUTerm ℒₛₑₜ t) :
    Bootstrapping.termBVVec ℒₛₑₜ 2 (?[^#0, t] : V)
      = (?[Bootstrapping.termBV ℒₛₑₜ (^#0 : V), Bootstrapping.termBV ℒₛₑₜ t] : V) := by
  rw [show (2 : V) = 0 + 1 + 1 by norm_num]
  rw [Bootstrapping.termBVVec_cons
    (Bootstrapping.IsUTerm.bvar (L := ℒₛₑₜ) (z := 0))
    (Bootstrapping.IsUTermVec.adjoin
      (Bootstrapping.IsUTermVec.empty (V := V) (L := ℒₛₑₜ)) ht)]
  rw [Bootstrapping.termBVVec_cons ht
    (Bootstrapping.IsUTermVec.empty (V := V) (L := ℒₛₑₜ))]
  rw [termBVVec_nil']

end GodelQ.CG008BvZ
