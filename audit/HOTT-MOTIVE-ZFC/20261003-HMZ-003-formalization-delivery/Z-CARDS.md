# HMZ-003：Z-Cards — ZF existence / naming / use interface

## HMZ-Z-011 — `Inf`：非唯一无限集合的显式命名

```text
R source:
  HMZ-R-011, HMZ-R-012.
exact layer:
  Isabelle/ZF proof-formalization, not bare object-language ZFC alone.
u:
  Inf : i, a named infinite set.
formation F:
  The Infinity axiom gives a set containing 0 and closed under successor;
  the manual says this set is not uniquely defined.
consumer C:
  The formalization names Inf “in order to simplify the construction of the
  natural numbers.”
I/O/Done:
  Input is the theory's declared constant plus its axiom. Operation constructs
  or bounds natural-number development. Done is the stated derived construction,
  not a computation of an arbitrary witness from a bare existential sentence.
Z-A:
  At raw axiom level, infinity is an existence assertion without a unique object.
Z-B:
  The practical formalization explicitly extends the signature with Inf and
  records the axiom that constrains it; this is a visible naming/Skolem-style
  payment, not an invisible use of a missing object.
P1:
  u/F/C are source-visible, but the constant is introduced with its formation
  assumption; no active unpaid existence question is exhibited.
P2/P3:
  No same-object negative reentry, admission lifecycle or unfinished Done is
  present.
disposition:
  EXPLICIT_FORMATION_PAYMENT / NOT_A_Q.
```

## HMZ-Z-012 — `Pow`, `Replace`, `The`: practical syntax pays for bare existence

```text
R source:
  HMZ-R-012, HMZ-R-013.
exact layer:
  Isabelle/ZF formalization.
source facts:
  Bare traditional axioms assert existence of powersets, unions and other sets;
  the manual says this is intolerable for practical reasoning, so Isabelle
  declares constants and derived syntax. Replace has a stated single-valued
  condition; definite description has a stated unique-existence rule.
consumer:
  Proof construction using derived rules for Pow, Replace, RepFun, The and
  related operations.
payment:
  Named symbols, single-valuedness/unique-existence premises and derived rules
  distinguish an object-level theorem from a free executable delivery.
P qualification:
  The source does not show a consumer applying an operator to an unformed
  object or recursively querying the same object's legitimacy.
disposition:
  SOURCE_PAYMENT / FORMALIZATION_INTERFACE_CONTROL.
```

## HMZ-Z-013 — weak typing / representation error is a language boundary

```text
R source:
  HMZ-R-011.
exact layer:
  Expository comparison of untyped set-theoretic language and richer type
  discipline.
source fact:
  Set-theoretic encodings can make certain category mistakes harder to catch;
  systems based on set theory may add a weak type system.
control:
  The source does not say ZFC asserts the mistaken representation is structural,
  nor does it identify an object that lacks formation but is used by a ZFC
  operator.
disposition:
  REPRESENTATION/TYPE-DISCIPLINE_BOUNDARY / NOT_A_P_CANDIDATE.
```
