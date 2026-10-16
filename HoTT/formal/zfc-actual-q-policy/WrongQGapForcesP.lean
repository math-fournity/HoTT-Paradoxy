/-!
Negative control for C-359.  A Q gap is not itself a proof of P; the policy
field `gapPermitsZenoP` must be supplied and source-audited.
-/

theorem wrongQGapForcesP : ∀ (qGap P : Prop), qGap → P := by
  intro qGap P gap
  exact gap
