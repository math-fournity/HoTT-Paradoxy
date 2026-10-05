/-!
`MP-ZFC-MSS-PHASE-ORDER-CONTROL-001` is a source-motivated finite control.

The da Costa--Sant'Anna MSS discussion contrasts prediction (which refers to
future/time) with a description of physical state as phase-space points and says
that the phase space does not refer to the time parameter.  This file checks only
the representation boundary in a two-stage Boolean model:

* a parameterized trace determines its ordered start/end observation; but
* the characteristic function of its range does not determine that observation.

It does not formalize MSS, phase space, a physical prediction, ZFC, or an actual
loss claim about the source paper.  Its role is a precise positive/negative control
for whether a proposed time-elimination presentation retains parameter order.
-/

namespace ZFCMSSPhaseOrderControl

abbrev State := Bool
abbrev TemporalTrace := Bool → State
/-- A finite characteristic-vector encoding of the visited-state set: the first
    coordinate records whether `false` occurs, and the second whether `true`
    occurs.  A product avoids using function extensionality merely to compare
    two finite ranges. -/
abbrev RangeView := Bool × Bool

/-- A representation determines an observation when some decoder that sees only
    the representation yields that observation for every source object. -/
def Determines {A B : Type} (project : A → B) (observe : A → Prop) : Prop :=
  ∃ decode : B → Prop, ∀ a, decode (project a) ↔ observe a

/-- A finite characteristic-function encoding of the set of states visited by a
    two-stage trace.  It intentionally retains membership but not stage order. -/
def rangeView (trace : TemporalTrace) : RangeView :=
  ((trace false == false) || (trace true == false),
   (trace false == true) || (trace true == true))

/-- The source-side information that a phase-set view can forget: which state is
    at the initial stage and which is at the final stage. -/
def OrderedForward (trace : TemporalTrace) : Prop :=
  trace false = false ∧ trace true = true

def temporalView (trace : TemporalTrace) : TemporalTrace :=
  trace

def forwardTrace : TemporalTrace :=
  fun stage => stage

def reverseTrace : TemporalTrace :=
  fun stage => !stage

theorem forward_trace_is_ordered : OrderedForward forwardTrace := by
  exact ⟨rfl, rfl⟩

theorem reverse_trace_is_not_ordered : ¬ OrderedForward reverseTrace := by
  intro h
  exact Bool.noConfusion h.1

/-- Reversing the two stages leaves the finite set of visited states unchanged. -/
theorem forward_reverse_same_range :
    rangeView forwardTrace = rangeView reverseTrace := by
  rfl

/-- The order-aware representation has a direct decoder for the observation. -/
theorem temporal_view_determines_ordered_forward :
    Determines temporalView OrderedForward := by
  refine ⟨fun trace => OrderedForward trace, ?_⟩
  intro trace
  rfl

/-- A range/set view alone cannot determine the ordered initial/final observation:
    `forwardTrace` and `reverseTrace` have the same range but opposite verdicts. -/
theorem range_view_does_not_determine_ordered_forward :
    ¬ Determines rangeView OrderedForward := by
  intro h
  rcases h with ⟨decode, hdecode⟩
  have noReverse : ¬ decode (rangeView reverseTrace) := by
    intro decoded
    exact reverse_trace_is_not_ordered ((hdecode reverseTrace).mp decoded)
  have yesForward : decode (rangeView forwardTrace) :=
    (hdecode forwardTrace).mpr forward_trace_is_ordered
  rw [forward_reverse_same_range] at yesForward
  exact noReverse yesForward

/-- The paired positive/negative control, stated together to block the false
    inference that every representation change loses order. -/
theorem parameter_order_control :
    Determines temporalView OrderedForward ∧
      ¬ Determines rangeView OrderedForward := by
  exact ⟨temporal_view_determines_ordered_forward,
    range_view_does_not_determine_ordered_forward⟩

#print axioms forward_trace_is_ordered
#print axioms reverse_trace_is_not_ordered
#print axioms forward_reverse_same_range
#print axioms temporal_view_determines_ordered_forward
#print axioms range_view_does_not_determine_ordered_forward
#print axioms parameter_order_control

end ZFCMSSPhaseOrderControl
