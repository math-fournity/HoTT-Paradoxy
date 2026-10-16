import GodelQ.ZFC.SeqTranslateFormula

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

open GodelQ.Translate GodelQ.ZFCArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

instance iVE_definable : 𝚺ᴬ₁-Function₂ (iVE : V → V → V) := iVE_defined.to_definable
instance iVE_definable' (Γ m) : Γᴬ_[m + 1]-Function₂[V] iVE := iVE_definable.of_sigmaOne

lemma isSemiformula_eqAtom {n t : V} (hn : 0 < n) (ht : IsSemiterm ℒₛₑₜ n t) :
    IsSemiformula ℒₛₑₜ n (eqAtom t) := by
  rw [eqAtom, IsSemiformula.rel]
  refine ⟨?_, ?_⟩
  · rw [cEqN]; exact codeIn_rel_quote _
  · rw [show (?[^#0, t] : V) = (^#0 : V) ∷ (t ∷ 0) from rfl]
    rw [show (2 : V) = 1 + 1 by simp [one_add_one_eq_two], IsSemitermVec.cons_iff]
    refine ⟨IsSemiterm.bvar.mpr hn, ?_⟩
    rw [show (1 : V) = 0 + 1 by simp, IsSemitermVec.cons_iff]
    exact ⟨ht, by simp⟩

-- iVE 计算规则（正式名）
@[simp] lemma iVE_bvar (n z : V) : iVE n (^#z) = eqAtom (^#(z + 1)) := by
  simp [iVE, iVE.construction]

@[simp] lemma iVE_fvar (n x : V) : iVE n (^&x) = eqAtom (^&x) := by
  simp [iVE, iVE.construction]

lemma iVE_func {n k f v : V} (hkf : (ℒₒᵣ).IsFunc k f) (hv : IsUTermVec ℒₒᵣ k v) :
    iVE n (^func k f v) =
      (if k = 0 then ve0 k f else ve2 n k f (iVE.construction.resultVec ℒₒᵣ ![n] k v)) := by
  rw [iVE, iVE.construction.result_func' hkf hv]; rfl

-- [2] isSemiformula_iVE：先写 bvar / fvar 两支实测
example {n : V} : ∀ z, z < n → IsSemiformula ℒₛₑₜ (n + 1) (iVE n (^#z)) := by
  intro z hz
  rw [iVE_bvar]
  exact isSemiformula_eqAtom (by simp) (IsSemiterm.bvar.mpr (by simpa using hz))

example {n : V} : ∀ x, IsSemiformula ℒₛₑₜ (n + 1) (iVE n (^&x)) := by
  intro x
  rw [iVE_fvar]
  exact isSemiformula_eqAtom (by simp) (IsSemiterm.fvar (n + 1) x)

end GodelQ.SeqTranslate
