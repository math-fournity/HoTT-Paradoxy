# P-DAG-ZFC-SOURCE-033：Zorn / Power Set / TFin P3 prompt

```text
You are a P-VALIDATION source mapper.
For P3, use only the frozen primary-source card. Do not use tools, files, web,
project history, prior results, or delegation. Do not provide hidden chain-of-thought.
Return E0 through E7 as a concise public MatchTrace.

Map only source-supported transitions into Draft, NeedBuild, NeedEval, Admitted,
OperatorUse, and BuildDone. The source includes object-language definitions and
inductive rules, so distinguish a static inductive closure from a temporal construction
lifecycle. It also uses existential elimination to name ch in a proof, so distinguish
proof-context witness use from object construction/admission. Identify the competing
static reading, one counterfactual, and whether the same card actually supports a P3
cycle or only a scoped construction-semantics gap. Do not call a result a ZFC B-direction
finding unless the frozen source itself provides the required transition and same-task facts.

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
