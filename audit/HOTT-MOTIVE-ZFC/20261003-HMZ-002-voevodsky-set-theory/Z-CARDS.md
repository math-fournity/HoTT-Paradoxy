# HMZ-002：Z-Cards — equivalence 的 ZFC-side 还原

## HMZ-Z-008 — 表现敏感性质与 equivalence-respecting 抽象语言

```text
R source:
  HMZ-R-008.
exact theory / layer:
  ZFC/set-theoretic practice and the language criterion discussed by
  Ahrens/North 2022; compare Shulman 2008.
u:
  A set-coded mathematical structure, together with a property/construction
  written about that presentation.
formation F:
  Standard set-theoretic coding and formula/property formation.
consumer C:
  A mathematician or formal development wishes to treat the property as a
  structural property, i.e. invariant under the appropriate isomorphism or
  equivalence.
I/O/Done:
  Input: a presentation and an isomorphism/equivalence. Operation: state or
  transport a property/construction. Observation: invariance. Done: the chosen
  language/property class licenses a structural claim.
Z-A:
  Pure set-theoretic language permits representation-sensitive sentences such
  as the source example `1 ∈ ℕ`; it has no native syntactic partition that
  automatically marks all abstract properties as invariant.
Z-B:
  Ahrens/North make the required payment explicit: choose the appropriate
  domain and a syntactic class of properties/structures; typed language/FOLDS
  gives a preservation criterion in the cited setting.
standard defense:
  The non-invariant property has not been called structural by the source.
  Changing the language or restricting the property class changes the stated
  contract rather than solving an unpaid internal process.
P1/P2/P3:
  No source-defined unformed object is consumed; no same-object reentry,
  negative bridge, admission state or Done loop is present.
disposition:
  SOURCE_SUPPORTED_REPRESENTATION_BOUNDARY / EXPLICIT_LANGUAGE_PAYMENT /
  NOT_A_P_CANDIDATE.
```

## HMZ-Z-009 — ZFC formalization convenience claim meets actual ZF formalization

```text
R source:
  HMZ-R-007.
exact layer:
  Voevodsky's historical/design claim versus Isabelle/ZF's actual FOL+ZF
  proof-assistant system.
Z-A:
  Axiom schemes and bare existential axioms can make convenient practical
  formalization harder in some systems.
Z-B:
  Isabelle/ZF explicitly handles the scheme, supplies named constants and
  derived syntax, and uses ZF for recursive/inductive formal developments.
disposition:
  SOURCE_PAYMENT / DESIGN-COMPARISON_ONLY / NOT_A_ZFC_Q.
```

## HMZ-Z-010 — well-ordering and standard isomorphism as payment

```text
R source:
  HMZ-R-010.
source layer:
  Technical construction of a univalent model, not ZFC object language.
fact:
  Well-orderings give at most one standard isomorphism of the specified
  simplicial sets.
control significance:
  A source that needs canonical/standard representatives may add an ordering
  condition; this demonstrates explicit payment rather than a free transport
  principle.
disposition:
  ANTI-ANALOGY_CONTROL.
```
