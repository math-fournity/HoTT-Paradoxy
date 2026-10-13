-- CG-009: layer-monotonicity for `IsSemiterm`/`IsSemitermVec`.
--
-- Foundation's `IsSemitermVec.def` shows the layer is just an *upper bound*
-- (`termBV ≤ n`), so it can be relaxed freely.
import GodelQ.ZFC.IVEOpenFunc8

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.LayerMono
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma IsSemiterm.mono {L : Language} [L.Encodable] [L.LORDefinable] {n n' t : V}
    (h : IsSemiterm L n t) (hn : n ≤ n') : IsSemiterm L n' t :=
  ⟨h.1, le_trans h.2 hn⟩

lemma IsSemitermVec.mono {L : Language} [L.Encodable] [L.LORDefinable] {k n n' v : V}
    (h : IsSemitermVec L k n v) (hn : n ≤ n') : IsSemitermVec L k n' v := by
  rw [IsSemitermVec.def] at h ⊢
  exact ⟨h.1, fun i hi => le_trans (h.2 i hi) hn⟩

end GodelQ.LayerMono

#print axioms GodelQ.LayerMono.IsSemiterm.mono
#print axioms GodelQ.LayerMono.IsSemitermVec.mono
