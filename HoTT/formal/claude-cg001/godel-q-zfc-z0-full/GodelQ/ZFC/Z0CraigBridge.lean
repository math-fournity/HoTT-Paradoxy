import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import Foundation.FirstOrder.Incompleteness.StandardProvability

/-!
# WorkBuddy CG-007 W8: conditional Craig bridges

The bridges below are explicit hypotheses, not proved facts.
This file checks only the assembly to D3 or to the full Z0 statement.
It neither changes the existing predicate nor proves its internalization.
- current scope: the WorkBuddy candidate branch, Lean 4.34.0 / Foundation 1fb01b72.
- model-universe scope for Z0 is the same `Type` scope consumed by Z0Full.
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full

namespace GodelQ.WorkBuddyZ0CraigBridge

noncomputable example : (Sh.craig : ArithmeticTheory).Δ₁ := inferInstance
noncomputable example : (Sh.craig.standardProvability).HBL3 := inferInstance

/-- WB-CG007-C-001: a reverse bridge only on sentences of the form zfcTr σ
suffices for D3. The bridge remains a hypothesis. -/
theorem hbl3_of_reverse_on_image
    (bridge : ∀ σ : ArithmeticSentence,
      𝗜𝚺₁ ⊢ provabilityPred Sh.craig (zfcTr σ) 🡒 zfcTr (zfcTr σ)) :
    zfcTr.HBL3 := by
  refine ⟨fun {σ} ↦ ?_⟩
  have hc : 𝗜𝚺₁ ⊢ zfcTr σ 🡒 provabilityPred Sh.craig (zfcTr σ) :=
    provable_sigma_one_complete (T := Sh.craig) (zfcTr_sigma1 σ)
  exact C_trans hc (bridge σ)

/-- The restricted reverse bridge assembles to the full statement,
but this theorem does not supply that bridge. -/
theorem zfc_z0_full_of_reverse_on_image
    (bridge : ∀ σ : ArithmeticSentence,
      𝗜𝚺₁ ⊢ provabilityPred Sh.craig (zfcTr σ) 🡒 zfcTr (zfcTr σ)) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) := by
  letI : zfcTr.HBL3 := hbl3_of_reverse_on_image bridge
  exact zfc_z0_full

/-- WB-CG007-C-002: full pointwise equivalence is sufficient, but stronger
than the restricted reverse bridge used by this assembly. -/
theorem hbl3_of_pointwise_equivalence
    (keyE : ∀ σ : ArithmeticSentence,
      𝗜𝚺₁ ⊢ zfcTr σ 🡘 provabilityPred Sh.craig σ) : zfcTr.HBL3 := by
  apply hbl3_of_reverse_on_image
  intro σ
  cl_prover [keyE (zfcTr σ)]

/-- WB-CG007-C-003: if only the final Z0 statement is needed,
a reverse bridge at bottom suffices. This does not establish zfcTr.HBL3. -/
theorem zfc_z0_full_of_reverse_at_bottom
    (bridge : 𝗜𝚺₁ ⊢ provabilityPred Sh.craig (⊥ : ArithmeticSentence) 🡒 zfcTr ⊥) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) := by
  intro h
  have hz : Sh ⊢ (𝗭𝗙𝗖.consistent : ArithmeticSentence) := (Sh_provable_iff _).mpr h
  have he : Sh ⊢ zfcTr.con 🡘 (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
    WeakerThan.pbl zfcTr_con_iff
  have hp : Sh ⊢ zfcTr.con := by cl_prover [he, hz]
  have hb : Sh ⊢ provabilityPred Sh.craig (⊥ : ArithmeticSentence) 🡒 zfcTr ⊥ :=
    WeakerThan.pbl bridge
  have hc : Sh ⊢ Sh.craig.consistent.val := by
    change Sh ⊢ ∼provabilityPred Sh.craig (⊥ : ArithmeticSentence)
    change Sh ⊢ ∼zfcTr (⊥ : ArithmeticSentence) at hp
    cl_prover [hb, hp]
  exact craig_consistent_unprovable_of_RE Sh hc

end GodelQ.WorkBuddyZ0CraigBridge

#print axioms GodelQ.WorkBuddyZ0CraigBridge.hbl3_of_reverse_on_image
#print axioms GodelQ.WorkBuddyZ0CraigBridge.zfc_z0_full_of_reverse_on_image
#print axioms GodelQ.WorkBuddyZ0CraigBridge.hbl3_of_pointwise_equivalence
#print axioms GodelQ.WorkBuddyZ0CraigBridge.zfc_z0_full_of_reverse_at_bottom
