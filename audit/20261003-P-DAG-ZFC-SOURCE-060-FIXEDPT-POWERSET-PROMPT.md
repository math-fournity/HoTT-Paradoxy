# P-DAG-ZFC-SOURCE-060：有界不动点 / Power Set 防御 source-match prompt

```text
You are a P-VALIDATION source mapper.
Use only the frozen primary-source card below. Do not use tools, files, web,
project history, prior results, or delegation. Do not provide hidden
chain-of-thought. Return E0 through E7 as a concise public MatchTrace in no
more than 900 words.

This is a Power Set defense-ledger probe. Do not claim ZFC has a defect, that
Power Set is safe in every use, that an author had any unquoted historical
intention, or that h=Pow supplies a Russell Q. Keep proof-system/package,
object-level and runtime/real-task layers separate.

At E3 map source facts to P1 fields T/u/F/C/I/O/Done and state the layer.
At E5 provide the fixed-order P1 Gate Ledger:
  L2c layer: [source fact] => [verdict] — [reason]
  L5b active-demand: [source fact] => [verdict] — [reason]
  L6 F-only payment: [source fact] => [verdict] — [reason]
  L7 positive obligation: [source fact] => [verdict] — [reason]
  L7b packet payment: [source fact] => [verdict] — [reason]
Then give this exact PowerSetDefenseLedger table at E6:
  PS0 source/variant: [fact] => [verdict]
  PS1 defended Russell feature: [fact] => [verdict]
  PS2 actual guard: [fact] => [verdict]
  PS3 guard scope: [fact] => [verdict]
  PS4 candidate surplus: [fact or absence] => [verdict]
  PS5 same-task counterfactual: [fact] => [verdict]
  PS6 final verdict: [one bounded verdict] — [reason]

Compare h=Pow to the supplied valid Fin(A) control without claiming that the
control is the same theory task. State one neighboring reading that the source
does not support, and one changed source fact that would alter the verdict.

BEGIN FROZEN SOURCE CARD
Source A: isabelle-prover/mirror-isabelle, src/ZF/Fixedpt.thy,
commit 5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8,
SHA-256 fccd5ac849c2496dcc3f0da4a0e0ce133f1c6dc2281bc1475f5871e1af66b69b.

It declares a proof theory `Fixedpt` importing Isabelle/ZF equalities.
Lines 10--13 define:
  bnd_mono(D,h) iff h(D) <= D and
    for all W X, W <= X and X <= D imply h(W) subseteq h(X).
Lines 15--24 define:
  lfp(D,h) = Inter({X: Pow(D). h(X) subseteq X})
  gfp(D,h) = Union({X: Pow(D). X subseteq h(X)})
and say the theorem is proved in the lattice of subsets of D, namely Pow(D).
Lines 34--44 derive h(D) subseteq D and h(X) subseteq D from bnd_mono.
Lines 103--114 prove:
  bnd_mono(D,h) implies lfp(D,h) = h(lfp(D,h)).
Lines 124--138 give an induction rule only with bnd_mono(D,h) and
  a in lfp(D,h) as premises.

Source B: the accompanying official Isabelle/ZF fixedpoint package manual,
Paulson, "A Fixedpoint Approach to (Co)Inductive Definitions", §2--§3.2.
It states that least and greatest fixedpoints require h to be bounded by D
and monotone below D. It explicitly says:
  "The powerset operator is monotone, but by Cantor's theorem there is no set
   A such that A = P(A). We cannot put A = lfp(D,P) because there is no
   suitable domain D."
It gives a valid finite-powerset control:
  Fin(A) = lfp(P(A), lambda X.
    {z in P(A). z = empty or
      (exists a b. z = {a} union b and a in A and b in X)})
and says the package must prove its fixedpoint operator is applied to a
monotonic function. It describes this as a fixedpoint package over ZF set
theory, not a runtime or real-world process.

No frozen source fact supplies a standard-ZFC semantic consumer, a P2
same-object negative reentry, a P3 Draft/Admitted/OperatorUse lifecycle, or
an unpaid Q after the stated guard holds.
END FROZEN SOURCE CARD
```
