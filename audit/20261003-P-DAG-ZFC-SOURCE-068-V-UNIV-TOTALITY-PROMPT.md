# P-DAG-ZFC-SOURCE-068：V / univ(A) totality source-match payload

```text
You are a P-VALIDATION source mapper. Use only the frozen primary-source card below. Do not use tools, files, web, project history, prior results, or delegation. Do not provide hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace of at most 900 words.

BEGIN FROZEN SOURCE CARD
Source: Lawrence C. Paulson, Isabelle's Logics: FOL and ZF, official Isabelle PDF, SHA-256 4ce0ae256cb7506832fdc5d3605ff752c932c3c5721e3140c4658d84e56b0fcb.

Frozen source facts:
1. Classes are collections too big to be sets. The class of all sets, V, cannot be a set without admitting Russell's Paradox.
2. In ZF all variables denote sets; classes are identified with unary predicates. A class cannot belong to another class or to a set.
3. The document says its ZF theory implements Zermelo-Fraenkel set theory as an extension of classical FOL.
4. The document separately says Theory Univ defines a set “universe” univ(A), used by the datatype package. It contains A and the natural numbers, is closed under finite products, and is a simple generalization of Vω.
END FROZEN SOURCE CARD

## Frozen parent TaskCard — echo these exact fields in E3

T = Isabelle documented ZF/BG class/set distinction
u = universal class V, contrasted with the small set univ(A)
F = ZF treats classes as unary predicates; univ(A) is a bounded set universe / Vω-like construction used by the datatype package
C = documented syntax/semantic layer distinction; no V-as-set consumer is supplied
I = a set variable / class predicate reading; A as parameter for univ(A)
O = source says V cannot be a set; univ(A) is a set with stated package use
Done = source-layer classification only, no runtime completion asserted
Q? = whether the totality V is a native first-class ZF object used in a same-layer task that leaves an unpaid formation/identity/operator Q

## Required analysis

E0 scope; E1 source identity; E2 source-bearing facts; E3 exact parent TaskCard; E4 direct correspondence; E5 P1/P2/P3 ledger; E6 PowerSetDefenseLedger; E7 bounded verdict and changing fact.

At E5, distinguish V's class/predicate status from univ(A)'s set/package use. Do not invent a V-as-set consumer, a same-object reentry, or a lifecycle.

At E6 use exactly this semantic table:

| field | question |
| PS0 source/variant | Which V/class or univ(A)/set variant and layer are examined? |
| PS1 defended Russell feature | What feature does the source actually say is constrained? |
| PS2 actual guard | Which source distinction blocks V-as-set or limits univ(A)? |
| PS3 guard scope | Which documented theory/package task is covered? |
| PS4 candidate surplus | With guard retained, which source-supported same-task active Q, negative reentry, lifecycle or unpaid remainder remains? |
| PS5 same-task control | What is the nearest source contrast and is it truly the same task? |
| PS6 verdict | Give one bounded verdict from DEFENSE_IDENTIFIED, CANDIDATE_GUARD_BLOCKED, BEYOND_DEFENSE_CANDIDATE, SOURCE_GUARD_SCOPE_UNSET or NOT_ENOUGH_EVIDENCE. |

Use ABSENT/UNSUPPORTED or UNKNOWN for source gaps. The source phrase “cannot be a set” is a source-level boundary; do not inflate it into an internal inconsistency, a historical conclusion, a real task, or a theorem about all forms of set theory.
```
