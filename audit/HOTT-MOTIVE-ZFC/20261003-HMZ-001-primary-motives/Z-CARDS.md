# HMZ-001：Z-Cards — ZFC 侧重建与来源层判别

> **重要：** “ZFC 侧”在本轮被拆成 ZFC 对象语言、形式化证明系统、数学实践和 construction bridge。没有
> 理论内对象、formation 与同层 consumer 的卡，不能进入模式 P 的 Q 卡。

## HMZ-Z-001 — 结构同一性接口：分类、代表与实际 family

```text
R source:
  HMZ-R-003.
exact theory / source layer:
  Classical set-theoretic mathematical practice, not yet a version-fixed ZFC
  axiomatization. Consumer source is Mumford 1965.
candidate u:
  A moduli/classification object and the curve data it classifies.
formation F:
  A coarse moduli/classification construction, as used in the source.
consumer C:
  Asking for an actual universal family or for invariants of a definite model.
I/O/Done:
  Input: moduli data. Operation: form a family/model. Observation: pullback or
  isomorphism data. Done: a family satisfying the stated universal property.
Z-A reading:
  The HoTT motive identifies a presentation cost: set-theoretic equality does
  not simply turn isomorphic structures into one object.
Z-B reading:
  The source preserves the missing structure rather than silently paying it:
  automorphisms and concrete maps remain explicit.
standard defense / payment:
  Mumford's automorphism-free restriction is the positive control; with
  nontrivial automorphisms the source says maps must be specified.
nearest control / task-switch risk:
  “Some representative exists” differs from “a natural family is delivered”.
  Requiring naturality without source support switches Done.
disposition:
  REAL_CONSUMER_CONTROL / DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT.
```

**P qualification.** `u/F/C/I/O/Done` are visible at the mathematical-practice layer, but no evidence yet says a
ZFC consumer promotes isomorphic classification into a naturally chosen family. P1 therefore does not yield an
active unpaid obligation. P2/P3 are not attempted. This is a **control**, not an attack on ZFC.

## HMZ-Z-002 — “谓词逻辑过于有限／不能直接表达”还没有成为 ZFC 对象卡

```text
R sources:
  HMZ-R-001, HMZ-R-002, HMZ-R-004.
exact theory / source layer:
  Voevodsky's contrast between ZFC/predicate-logic presentation and a native
  homotopy-type language; no independent ZFC syntax/encoding source has yet
  been read.
candidate u / formation / consumer:
  UNFIXED. “2-theory object”, “higher object” and “direct expression” are not
  a ZFC object, a formation rule, or a same-layer consumer by themselves.
Z-A reading:
  The issue may be an expression/representation cost in a first-order,
  set-coded presentation.
Z-B reading:
  The issue may be a preference for native language and proof architecture;
  an encoding can still exist and serve its stated ZFC task.
standard defense / payment:
  HMZ-R-006: the Book itself constructs an internal cumulative hierarchy and
  describes a ZFC model under assumptions.
disposition:
  Z_SIDE_UNDER_SPECIFIED / MUST_FOLLOW HMZ-MF-001.
```

This card deliberately does **not** bind to Power Set. An axiom that forms a set of subsets and a claim about
direct descriptions of higher objects are not yet the same formation or task.

## HMZ-Z-003 — 机器验证动机：四个层级仍未会合

```text
R sources:
  HMZ-R-001, HMZ-R-005.
layers that must remain separate:
  (a) ZFC object language;
  (b) an external formalization of ZFC;
  (c) proof search/checking runtime;
  (d) a mathematician's usable delivery task.
candidate u/F/C/I/O/Done:
  UNFIXED at the ZFC-object layer. A theorem, proof object, compiler process or
  timeout cannot replace a source-defined ZFC consumer.
Z-A reading:
  Voevodsky's motivation makes daily, machine-verifiable work a real design goal.
Z-B reading:
  This goal may distinguish type-theoretic tooling rather than expose an
  unpaid ZFC formation commitment.
standard defense / payment:
  Metamath is recorded only as a proof-formalization presentation; it does not
  establish what ordinary ZFC use promises about execution or delivery.
disposition:
  P_REQUALIFICATION_REQUIRED / MUST_FOLLOW HMZ-MF-003.
```

No runtime observation may be upgraded to a theorem about ZFC, and no source in this run states the required
same-task bridge.

## HMZ-Z-004 — Power Set is a real formation rule, but not yet an R-derived candidate

```text
R sources:
  No direct R→Power Set source bridge in HMZ-S-001…S-008.
exact theory / source layer:
  Metamath's formal ZF presentation: ax-pow / pwex; PROOF_FORMALIZATION_ONLY.
u:
  A set A (formal hypothesis A ∈ V).
formation F:
  ax-pow states existence of a set containing every subset of x; pwex presents
  the derived class notation assertion P(A) ∈ V.
consumer C:
  ABSENT from this source packet.
I/O/Done:
  The source supplies a proof-system statement, not a source-defined task
  contract, process, observation or completion condition.
standard guard:
  rankpw reports rank(P(A)) = suc(rank(A)); ax-reg gives a Foundation/
  non-self-membership guard. These are rule-level guards, not universal
  answers to every formation-origin question.
disposition:
  P_REQUALIFICATION_REQUIRED / MUST_FOLLOW HMZ-MF-004.
```

The card preserves the user’s Power Set intuition as a **separate open station**, but this HoTT-motive corpus
does not license assigning it to R-CONSTRUCT, R-HIGHER or R-MACHINE merely because all mention formation or
generality.

## HMZ-Z-005 — HoTT 内部 V/ZFC 是反类比控制

```text
R source:
  HMZ-R-002 and HMZ-R-006.
exact theory / source layer:
  HoTT Book's internal higher-inductive cumulative hierarchy V, not ZFC itself.
source fact:
  Under choice and a universe, the Book states that V models ZFC.
what it controls:
  “HoTT starts from homotopy types rather than sets” cannot be read as
  “ZFC cannot be represented/used” or as a direct ZFC Q.
disposition:
  ANTI_ANALOGY_CONTROL for a blanket R-002 → ZFC-defect inference.
```

It is not a proof that every particular ZFC consumer pays every requirement; it only blocks the broad
incompatibility inference.

## HMZ-Z-006 — ZFC 的 class-as-formula / meta-language 边界

```text
R sources:
  HMZ-R-001, HMZ-R-002, HMZ-R-004.
exact theory / source layer:
  ZFC as analyzed by Shulman 2008, pp. 10–11: large categories represented
  by classes defined through set-theoretic formulas.
u:
  A formula characterizing a class / a particular large category such as Set or Grp.
formation F:
  A set-theoretic formula defines the class's elements; no new first-order
  ZFC object corresponding to “the class” is introduced.
consumer C:
  A theorem involving quantification over a large category, e.g. the stated
  large-category formulation of the Adjoint Functor Theorem.
I/O/Done:
  Input: a formula-defined large category. Operation: quantify/formally state
  a theorem about it. Observation: whether it is a ZFC formula/theorem.
  Done: the statement is internal to ZFC rather than only a meta-theorem.
Z-A reading:
  The source says ZFC cannot quantify over classes, so the specified theorem
  cannot be stated or proven internally in ZFC.
Z-B reading:
  It also gives an explicit standard response: use a meta-theorem, or move to
  NBG, which permits class quantification and is conservative over ZFC for set
  statements.
standard defense / payment:
  NBG introduces classes with axioms; the source is explicit about this
  language shift and its scope.
P1 position:
  L0 fails for the proposed class-as-object: the source expressly says classes
  are not things ZFC knows about. The internal set/formula data are not the
  same object as a class-quantified theorem.
P2/P3:
  No same-object reentry, admission transition, or unpaid completion cycle is
  supplied by the source.
disposition:
  SOURCE_SUPPORTED_REPRESENTATION_BOUNDARY / NOT_A_P_CANDIDATE.
```

This is the strongest source-level realization so far of Voevodsky's language/directness motivation. It is a
real ZFC limitation of formal expressibility at the chosen layer, but the source's metatheory/NBG response
changes the language and task scope rather than yielding an internal P-shaped Q.

## HMZ-Z-007 — Isabelle/ZF: formalization and practical syntax are explicit payments

```text
R source:
  HMZ-R-005 (machine-verifiable foundations).
exact theory / source layer:
  Isabelle2021-1's ZF formalization: a proof assistant implementation of
  classical first-order ZF with derived rules and practical syntax.
u:
  Isabelle's type i of sets; constants such as Pow / Replace / RepFun.
formation F:
  ZF axioms state existence of empty set, union, powerset and related objects;
  the implementation supplies named constants and derived rules for practical use.
consumer C:
  Formal developments of relations, functions, ordinals, cardinals, inductive
  definitions and recursion under the stated Isabelle/ZF system.
I/O/Done:
  The manual records proof-checking/formalization behavior, not a claim that a
  bare ZFC theorem automatically computes a result for an ordinary mathematician.
Z-A reading:
  Replacement's axiom scheme can be awkward for many theorem provers because
  its instances must be invoked explicitly.
Z-B reading:
  Isabelle reports no difficulty with axiom schemes and explicitly adds the
  practical syntax / derived rules needed to use the theory.
standard defense / payment:
  The implementation names objects and layers its derived operations; it does
  not silently represent these as free execution from existential claims.
P1/P2/P3:
  This is a real formalization but no source-defined consumer has been shown
  to use an unformed object, or to form a self-reentering admission loop.
disposition:
  SOURCE_PAYMENT / MACHINE-MOTIVATION-NOT-YET-A-ZFC-Q.
```
