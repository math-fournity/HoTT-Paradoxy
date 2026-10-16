# L3 bounded natural-consumer audit

- Status: `BOUNDED_NEGATIVE_COMPLETE / ZERO HITS IN 7 FIXED SOURCES / L3 CANDIDATE NOT UPGRADED`
- Scope: `SCOPE.json`, frozen before full-text extraction and per-source
  classification
- Decision owner: `DECISIONS.json`
- Machine inventory: `KEYWORD-INVENTORY.json`, deterministic digest
  `89972826f625e03a303d8de2985319dee7a5c9c44cd1e32bccc1039324aa81e5`
- Boundary: this is a source-set result, not a global nonexistence theorem

## Question and decision rule

The audit asked whether one fixed, natural HoTT/Cubical construction satisfies
all six conditions below:

1. Path or cubical dimension is actually the carrier of an activity's time;
2. that same carrier promises exact observation of a discrete completion;
3. no separate clock, tick, later modality, event/stage type, directed morphism
   or scheduler carries progression;
4. the added obligation arises from the HoTT/Cubical rule in use rather than an
   independently chosen continuous model;
5. the source does not explicitly qualify the capability as partial,
   approximate, axiomatic or additional; and
6. failure is attributed to the original activity rather than the selected
   representation.

A hit required PASS on E1-E6 in one construction.  Keyword matches only routed
the full-text review; they never decided a criterion.

## Retrieval and mechanical coverage

The set contains the current fetched first-edition HoTT Book PDF, the exact
Agda 2.8.0 cubical manual source at commit
`3d04bacca842729f9c0869b9287256321b5f450f`, the full 1,111-file Cubical v0.9
tree, the 2019 Cubical Agda paper, Guarded Cubical Type Theory v2, Clocked
Cubical Type Theory v3, and Directed HoTT v1.

All remote bytes, headers, derived page text, extraction runtime and SHA-256
values are recorded in `RETRIEVAL-MANIFEST.json`.  Full PDFs remain in the
external cache rather than Git.  `natural_consumer_audit.py` verified those
bytes, rechecked the Cubical v0.9 tree hash, scanned all seven sources, and
replayed the same inventory digest.

Two retrieval irregularities remain visible:

- the HoTT Book stable link returned a 128-byte meta-refresh, so the named
  `hott-online-82-g578b85c.pdf` target was fetched and pinned;
- the frozen Agda URL used the stale filename `cubical.rst`; the v2.8.0 Git tree
  showed `cubical.lagda.rst`.  `SCOPE-CORRECTION-001.json` records the 404,
  peeled tag commit, tree blob and corrected URL without changing the selected
  source or rewriting the frozen scope.

## Result table

| source | E1 | E2 | E3 | E4 | E5 | E6 | hit |
|---|---|---|---|---|---|---|---|
| HoTT Book | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | no |
| Agda 2.8.0 Cubical manual | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | no |
| Cubical library v0.9 | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | no |
| Cubical Agda paper | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | no |
| Guarded Cubical Type Theory | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | no |
| Clocked Cubical Type Theory | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | no |
| Directed HoTT | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | no |

Every FAIL has a page/section or file/line reason in `DECISIONS.json`.  The
uniform row does not mean the sources say the same thing.  Three of them reach
the boundary through especially informative, different routes.

## The strongest literal-time reading: the HoTT Book

The HoTT Book's Chapter 2 motivation says that a classical path
`[0,1] → X` can be thought of as a point at each moment in time.  This is the
strongest text in the set for reading a path parameter temporally.

The same book places two limits on that reading.  The Introduction says the
types/spaces are treated purely homotopically, without ordinary notions such as
open subsets or convergence, and warns that other topological concepts are not
automatically applicable.  Chapter 2 uses the interval story to motivate
identity, path concatenation and homotopy.  It does not define an activity-time
interface, a Pending/Done predicate, or an exact completion consumer.

The result is an analogy relevant to the user's L3 question, but not the natural
consumer required to upgrade the candidate.

Primary source: [HoTT Book](https://homotopytypetheory.org/book/), fetched
version `hott-online-82-g578b85c`, especially PDF pages 15 and 71.

## The implementation boundary: Agda and Cubical v0.9

The Agda 2.8.0 manual gives `I : IUniv`, describes Path as proof-relevant
equality represented like a function out of I, and explicitly says a Path is
not exactly an ordinary function.  It contains no time, clock, tick, event,
arrival or completion consumer in the audited source.

The full Cubical v0.9 tree likewise contains no whole-word clock, tick,
temporal, concurrency or arrival hit.  The closest exact endpoint example is
`partialBool` in `Cubical/Papers/Synthetic.agda:61-63`: different Bool values
are given under a `Partial` endpoint formula.  The type is the fence.  It does
not produce a total `I → Bool` path between false and true.

The 2019 Cubical Agda paper makes the same distinction more explicitly.  Its
interval variables form Path equality; its stream example uses finite-time
productivity for projection unfolding and then separately uses an interval
variable to prove equality between streams.  Section 3.1 states that Path's
continuous behavior prevents arbitrary endpoint results.  That is the intended
equality semantics, not a promise to encode a discrete completion event.

Primary sources: [Agda Cubical manual](https://agda.readthedocs.io/en/stable/language/cubical.html),
[Cubical v0.9](https://github.com/agda/cubical/tree/b150186d2544e7efeddd31e5d14a8b9ecbb100f7),
and [Cubical Agda paper](https://doi.org/10.1145/3341691).

## The temporal extension boundary: guarded and clocked cubical theories

Guarded Cubical Type Theory is the closest formal case in which cubical
dimension and temporal progression interact.  It uses the interval to constrain
fixed-point unfolding and to construct Path equalities between a fixed point
and its unfolding.  It assigns delayed availability to a distinct `later`
type, delayed substitutions and the omega coordinate of a product presheaf
model.  Its conclusion describes the combination directly: cubical Path
supports extensional reasoning about guarded operations; guarded recursion
supplies the progression structure.

Clocked Cubical Type Theory makes the separation explicit.  Clock-indexed
`later` encodes time steps, ticks witness that time has passed, and clocks/ticks
have their own formation and elimination rules.  Cubical Path is used for
extensionality, tick irrelevance and the identification of bisimilarity with
equality.  The paper even compares the sorts of clock and I while maintaining
their distinct syntax and roles.

These are natural temporal Cubical systems, but their natural design response
is to add clocks, ticks or a later modality.  They fail E3 and do not ask a
single ordinary Path coordinate to expose an exact discrete completion phase.

Primary sources: [Guarded Cubical Type Theory v2](https://arxiv.org/abs/1611.09263v2)
and [Clocked Cubical Type Theory v3](https://arxiv.org/abs/2102.01969v3).

## The process boundary: Directed HoTT

Directed HoTT is the clearest source in the set where path language represents
real process structure.  Its concurrency example represents states by points
and possible executions by directed paths, then defines reachable and safe
states using those witnesses.

Its central motivation is precisely that ordinary identity paths describe
reversible paths.  The paper introduces a new `hom` type former for irreversible
or directed paths and keeps it distinct from Martin-Löf identity.  Thus it is a
natural process consumer that supports the need for additional directed/event
structure; it is not an example in which ordinary HoTT identity already serves
as an activity clock and then falsely blocks completion.

Primary source: [Towards a Directed Homotopy Type Theory](https://arxiv.org/abs/1807.10566v1),
especially PDF pages 2-3 and 15-16.

## Cross-source judgment

The strongest counter-readings are all real:

- classical paths admit a moment-in-time intuition;
- GCTT's interval participates in fixed-point unfolding coherence; and
- directed paths model executions.

None meets E1-E6 in one construction.  The first is bounded to homotopical
identity, the second gives availability to `later/ω`, and the third introduces
a separate directed `hom` type.  CCTT strengthens the same pattern by assigning
time steps to clocks and ticks.

The bounded conclusion is therefore:

> In these seven fixed primary-source versions, no construction was found that
> uses ordinary HoTT/Cubical Path or dimension as an activity-time carrier,
> promises exact discrete completion through that same carrier, omits separate
> temporal/event structure, and attributes the resulting obstacle to the
> original activity.

This result does not prove global nonexistence.  It changes the status of the
current project candidate in a narrower and useful way: the formal L3
obstruction remains a checked consequence of its declared I-indexed
theoryization, but the natural-use bridge is not established.  Within this
audited set, the best classification is `REPRESENTATION_BOUNDARY /
DEFENSE_WORKS`; the explicit Stage task in M4-lite supplies the corresponding
positive repair.

## What would reopen the result

This bounded negative should be reopened only by a fixed source/construction
that plausibly passes E1 and E2 together.  It must then be checked against E3-E6
without moving the task or adding its missing event structure after the fact.
Broader search may enlarge the source set as a new audit revision; it must not
rewrite this seven-source denominator.

No mathematical claim package is created by this audit.  Its source findings
are literature/code assessments, and the M4 tasks remain exploration and
control evidence outside `HoTT/CLAIM_EVIDENCE_MATRIX.md`.
