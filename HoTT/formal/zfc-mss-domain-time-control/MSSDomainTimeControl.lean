/-!
`MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001` is a source-motivated control derived
from Sant'Anna--Bueno's distinction between the ZFC MSS presentation and their
domainless function theory `N`.

It does not formalize ZFC, the MSS axioms, the paper's Theorem 8, physical
motion, or an actual completion judgment.  It fixes two small representations:

* a graph view whose domain is certified to be the temporal carrier; and
* a function-only view that deliberately omits a designated temporal carrier.

The kernel proves that the first view preserves endpoint membership, whereas the
second does not determine that observation in a two-instance control.  The
mathematical role is to distinguish definitionally eliminating a *separate name*
for time from erasing the data needed to observe a temporal boundary.
-/

namespace ZFCMSSDomainTimeControl

abbrev Time := Nat
abbrev State := Nat
abbrev TimeSet := Time → Prop
abbrev GraphView := Time → State → Prop
abbrev FunctionView := Time → State

/-- A minimal set-theoretic graph presentation.  `domain_is_time` is the exact
    retained-information condition: the graph's domain recovers the designated
    temporal carrier. -/
structure GraphTrace where
  time : TimeSet
  graph : GraphView
  domain_is_time : ∀ t, (∃ x, graph t x) ↔ time t

/-- The representation after removing only the *separate field name* `time`.
    The graph is still a domain-bearing object. -/
def graphOnly (trace : GraphTrace) : GraphView :=
  trace.graph

/-- The temporal carrier reconstructed from a graph domain. -/
def recoveredTime (view : GraphView) : TimeSet :=
  fun t => ∃ x, view t x

/-- The narrowly fixed temporal observation for this control: an endpoint is
    admissible precisely when it belongs to the process's time carrier. -/
def EndpointAvailable (trace : GraphTrace) (endpoint : Time) : Prop :=
  trace.time endpoint

def EndpointFromGraph (view : GraphView) (endpoint : Time) : Prop :=
  recoveredTime view endpoint

/-- A view determines an observation when a decoder defined only on the view
    yields exactly the observation for every source instance. -/
def Determines {A B : Type} (project : A → B) (observe : A → Prop) : Prop :=
  ∃ decode : B → Prop, ∀ a, decode (project a) ↔ observe a

/-- In the graph/domain representation, removing an explicit primitive name for
    time preserves the chosen endpoint observation. -/
theorem graph_only_recovers_time
    (trace : GraphTrace) (endpoint : Time) :
    EndpointFromGraph (graphOnly trace) endpoint ↔
      EndpointAvailable trace endpoint := by
  exact trace.domain_is_time endpoint

/-- Therefore this source-side kind of definitional elimination has an explicit
    decoder for the endpoint observation. -/
theorem graph_only_determines_endpoint (endpoint : Time) :
    Determines graphOnly (fun trace => EndpointAvailable trace endpoint) := by
  refine ⟨fun view => EndpointFromGraph view endpoint, ?_⟩
  intro trace
  exact graph_only_recovers_time trace endpoint

/-- A deliberately domainless function presentation.  This is not asserted to
    be a full model of `N`-MSS; it isolates the information-loss possibility that
    the source itself marks by saying that its domainless reformulation is not
    exactly equivalent to the ZFC MSS formulation. -/
structure DomainlessCandidate where
  time : TimeSet
  function : FunctionView

def functionOnly (candidate : DomainlessCandidate) : FunctionView :=
  candidate.function

def EndpointAllowed (candidate : DomainlessCandidate) (endpoint : Time) : Prop :=
  candidate.time endpoint

def time0Only : TimeSet :=
  fun t => t = 0

def time0Or1 : TimeSet :=
  fun t => t = 0 ∨ t = 1

def sharedFunction : FunctionView :=
  fun _ => 0

def shortCandidate : DomainlessCandidate where
  time := time0Only
  function := sharedFunction

def longCandidate : DomainlessCandidate where
  time := time0Or1
  function := sharedFunction

/-- The two candidates have the same domainless function representation. -/
theorem domainless_views_equal :
    functionOnly shortCandidate = functionOnly longCandidate := by
  rfl

/-- Yet their temporal endpoint membership differs. -/
theorem short_endpoint_not_allowed :
    ¬ EndpointAllowed shortCandidate 1 := by
  intro h
  change 1 = 0 at h
  exact Nat.noConfusion h

theorem long_endpoint_allowed :
    EndpointAllowed longCandidate 1 := by
  change 1 = 0 ∨ 1 = 1
  exact Or.inr rfl

/-- No decoder using only the deliberately domainless function view can decide
    this endpoint observation for every candidate. -/
theorem function_only_does_not_determine_endpoint :
    ¬ Determines functionOnly (fun candidate => EndpointAllowed candidate 1) := by
  intro h
  rcases h with ⟨decode, hdecode⟩
  have noShort : ¬ decode (functionOnly shortCandidate) := by
    intro decoded
    exact short_endpoint_not_allowed ((hdecode shortCandidate).mp decoded)
  have yesLong : decode (functionOnly longCandidate) :=
    (hdecode longCandidate).mpr long_endpoint_allowed
  rw [← domainless_views_equal] at yesLong
  exact noShort yesLong

/-- The paired result states the exact scope of the control: graph-domain
    recovery is sufficient for this observation; a function-only projection is
    insufficient in the displayed two-instance family. -/
theorem domain_information_control (endpoint : Time) :
    Determines graphOnly (fun trace => EndpointAvailable trace endpoint) ∧
      ¬ Determines functionOnly (fun candidate => EndpointAllowed candidate 1) := by
  exact ⟨graph_only_determines_endpoint endpoint,
    function_only_does_not_determine_endpoint⟩

#print axioms graph_only_recovers_time
#print axioms graph_only_determines_endpoint
#print axioms domainless_views_equal
#print axioms short_endpoint_not_allowed
#print axioms long_endpoint_allowed
#print axioms function_only_does_not_determine_endpoint
#print axioms domain_information_control

end ZFCMSSDomainTimeControl
