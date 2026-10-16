# P-DAG-ZFC-SOURCE-061：可及性归纳 / Power Set 正向再入 source-match prompt

```text
You are a P-VALIDATION source mapper.
Use only the frozen primary-source card below. Do not use tools, files, web,
project history, prior results, or delegation. Do not provide hidden
chain-of-thought. Return E0 through E7 as a concise public MatchTrace in no
more than 900 words.

This is a same-source PS5 control, not a request to find a ZFC defect. Do not
call t in Pow(R) a negative Russell self-membership condition, do not infer a
runtime lifecycle, and do not turn the proof-package use into a standard-ZFC
semantic consumer or a real-world task.

At E3 map T/u/F/C/I/O/Done with layer. At E5 show this exact P2/P3 ledger:
  Bind/Form: [source fact] => [verdict] — [reason]
  Bridge/Reenter: [source fact] => [verdict] — [reason]
  polarity/guard: [source fact] => [verdict] — [reason]
  P3 transition: [source fact or absence] => [verdict] — [reason]
At E6 provide the exact PowerSetDefenseLedger table:
  PS0 source/variant: [fact] => [verdict]
  PS1 defended Russell feature: [fact] => [verdict]
  PS2 actual guard: [fact] => [verdict]
  PS3 guard scope: [fact] => [verdict]
  PS4 candidate surplus: [fact or absence] => [verdict]
  PS5 same-task counterfactual: [fact] => [verdict]
  PS6 final verdict: [one bounded verdict] — [reason]

Give one neighboring reading the source does not support and one changed fact
that would alter the verdict.

BEGIN FROZEN SOURCE CARD
Source A is Isabelle/ZF Fixedpt.thy at commit
5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8, SHA-256
fccd5ac849c2496dcc3f0da4a0e0ce133f1c6dc2281bc1475f5871e1af66b69b.
It defines bnd_mono(D,h) as h(D) <= D plus monotonicity below D, and defines
lfp(D,h) using subsets X in Pow(D). Its fixedpoint equation and induction
rule require bnd_mono(D,h).

Source B is Paulson's official Isabelle/ZF fixedpoint package manual, PDF
SHA-256 892f6b99e49a3aaa968da70cc5b8dfba2a6cd3c3234a59231cb5b3e6154c9daf.
The manual says an inductive premise t in M(R) is permitted when M is a
monotone operator. It states that P is monotone and that:
  t in P(R) expresses t subseteq R.
For the accessible part of a relation r on D, it describes acc(r) as the
least set containing a when all r-predecessors of a are already in acc(r).
It rewrites the premise as membership of the predecessor set:
  r^-1[{a}] in P(R),
equivalent to all predecessors y of a satisfying y in R.
The manual says the induced rule uses an induction hypothesis in the positive
set {z in acc(r). P(z)} and explains this as well-founded induction. It also
states that the package accepts the use because P is monotone. No source fact
provides a negative bridge, an unbounded h=Pow fixedpoint, a standard-ZFC
semantic consumer, a Draft/Admitted/OperatorUse lifecycle, or a real task.

For comparison only, the same manual says h=Pow has no suitable bounded domain
for lfp(D,Pow), while valid bounded definitions use a domain such as P(A).
END FROZEN SOURCE CARD
```
