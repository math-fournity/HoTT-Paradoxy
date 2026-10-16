# P-DAG-ZFC-SOURCE-034：Zorn / Power Set / TFin P1 prompt

```text
You are a P-VALIDATION source mapper.
For P1, use only the frozen primary-source card. Do not use tools, files, web,
project history, prior results, or delegation. Do not provide hidden chain-of-thought.
Return E0 through E7 as a concise public MatchTrace.

Identify the exact theory/layer, u, formation, consumer, I/O/Done and Q only when
the source supports them in one TaskCard. Distinguish object-language definitions,
static inductive closure, proof-system theorem acceptance, runtime and real-task use.
Test L2b/L2c, then L5b/L6/L7/L7b. At the end of E5 output exactly this Gate Ledger:
  L2c layer: [source fact] => [verdict] — [reason]
  L5b active-demand status: [source fact] => [verdict] — [reason]
  L6 F-only payment: [source fact] => [verdict] — [reason]
  L7 positive-obligation mode: [source fact] => [verdict] — [reason]
  L7b packet payment: [source fact] => [verdict] — [reason]
Do not use a theorem conclusion as a consumer or an AC witness as an un-paid Q
without source contract. State a nearby reading, counterfactual and bounded verdict.

BEGIN FROZEN SOURCE CARD
Source identity: isabelle-prover/mirror-isabelle, src/ZF/Zorn.thy at commit
5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8, SHA-256
f0b42dcea6638ce5a85b2c5393ecc6d9875283508ff0c56b6259e23785e24c3a.

The theory imports AC and Inductive. It defines:
  chain(A) = {F in Pow(A). every X,Y in F are subset-comparable}
  increasing(A) = {f in Pow(A)->Pow(A). for every x subset A, x subset f`x}
  maxchain(A) = {c in chain(A). super(A,c)=0}.

It declares an inductive object TFin(S,next) contained in Pow(S), with rules:
  nextI: x in TFin(S,next) and next in increasing(S) ==> next`x in TFin(S,next)
  Pow_UnionI: Y in Pow(TFin(S,next)) ==> Union(Y) in TFin(S,next).

It has a choice-dependent function:
  Hausdorff_next_exists:
    ch in product over X in Pow(chain(S))-{0} of X
    ==> exists next in increasing(S), for every X in Pow(S),
        next`X = if X in chain(S)-maxchain(S) then ch`super(S,X) else X.

The theorem Hausdorff proves exists c. c in maxchain(S) by applying
AC_Pi_Pow [THEN exE] to introduce ch, then Hausdorff_next_exists [THEN bexE]
to introduce next, then using Union(TFin(S,next)) as c. The source gives no
runtime scheduler, no external construction trace, and no same real-world task.
END FROZEN SOURCE CARD
```
