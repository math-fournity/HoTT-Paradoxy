# P-DAG-ZFC-SOURCE-039：RepFun parent P1 source prompt

```text
You are a P-VALIDATION source mapper.
For P1, use only the frozen primary-source card. Do not use tools, files, web,
project history, prior results, or delegation. Do not provide hidden chain-of-thought.
Return E0 through E7 as a concise public MatchTrace.

This is parent validation. Keep the parent u/F/Q fixed; you may reject or narrow
them but may not substitute a different theorem/candidate. Identify the exact layer,
consumer, I/O/Done and Q only when supported. At the end of E5 output exactly this
Gate Ledger:
  L2c layer: [source fact] => [verdict] — [reason]
  L5b active-demand status: [source fact] => [verdict] — [reason]
  L6 F-only payment: [source fact] => [verdict] — [reason]
  L7 positive-obligation mode: [source fact] => [verdict] — [reason]
  L7b packet payment: [source fact] => [verdict] — [reason]

BEGIN FROZEN SOURCE CARD
Parent candidate from a closed-menu blind discovery:
  u? = output collection of a functional relation over an already-admitted set;
  F? = collect those outputs;
  Q? = can F form one collection covering the supplied set's output values?;
  I/O/Done? = functional relation plus admitted set / output collection /
              collection covers the whole supplied set.

Source identity: isabelle-prover/mirror-isabelle, src/ZF/ZF_Base.thy at commit
5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8, SHA-256
33693f4e5d03933f2a0d36ed8350c3e541286cee9889e48f9e39eff5a1e63401.

The source declares PrimReplace and defines:
  Replace(A,P) = PrimReplace(A, lambda x y. exists! z. P(x,z) and P(x,y))
  RepFun(A,f) = {y . x in A, y = f(x)}
It states replacement as a membership equivalence for PrimReplace under
a functionality premise. It supplies:
  RepFunI: a in A ==> f(a) in {f(x). x in A}
  RepFunE: membership in {f(x). x in A} eliminates to some x in A with b=f(x)
  RepFun_iff: b in {f(x). x in A} iff exists x in A, b=f(x).
The source gives no runtime scheduler, external output service or real-world task.
END FROZEN SOURCE CARD

If the source definition directly forms the parent output collection, say so rather
than preserving it as an un-paid Q. Do not claim a theory defect, ZFC Q, UR or a
real consumer.
```
