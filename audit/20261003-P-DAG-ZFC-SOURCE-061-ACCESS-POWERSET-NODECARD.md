# P-DAG-ZFC-SOURCE-061：可及性归纳 / Power Set 正向再入 NodeCard

> **身份：** `PRELAUNCH_NODECARD / SAME_SOURCE_PS5_CONTROL / P2_P3_GUARD_PROBE / NOT_A_ZFC_Q_OR_MATHEMATICAL_RESULT`。

```text
node_id: P-DAG-ZFC-SOURCE-061-ACCESS-POWERSET-P2P3
parent: H060 Fixedpt / PowerSetDefenseLedger
purpose: inspect the official Isabelle/ZF fixedpoint-package explanation of
         accessible-part induction. It rewrites the recursive premise "all
         predecessors are in R" as t in Pow(R), where t is the predecessor
         set. Determine whether the reentry is source-defined positive,
         bounded and monotone, whether any P3 lifecycle is actually supplied,
         and whether this supplies PS5's same-family guard control or a PS4
         residual obligation.
actor: gpt-5.6-terra / max; fallback=false
runner: scripts/pattern_p_appserver_blind_discovery.py @ b839b7fe
private root: /Users/aurolafly/.codex-experiments/pattern-p-h061
access profile: PINNED_PRIMARY_SOURCE / source-match
permission/approval: governance-regression-fresh / never; no tools, files,
                     web, Git, or delegation
primary source A: isabelle-prover/mirror-isabelle Fixedpt.thy
                  @ 5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8
                  SHA-256 fccd5ac849c2496dcc3f0da4a0e0ce133f1c6dc2281bc1475f5871e1af66b69b
primary source B: Paulson, A Fixedpoint Approach to (Co)Inductive Definitions,
                  official Isabelle/ZF package manual, 2009 PDF SHA-256
                  892f6b99e49a3aaa968da70cc5b8dfba2a6cd3c3234a59231cb5b3e6154c9daf,
                  frozen excerpts in prompt.
source scope: official package documentation and Isabelle/ZF proof theory;
              no standard-ZFC semantic consumer, runtime or real-world task.
frozen prospective card:
  T      = Isabelle/ZF fixedpoint / inductive-definition package
  u      = Pow(R), used as the set of subsets of a recursive approximation R
  F      = t in Pow(R) iff t subseteq R, for t the predecessors of a
  C      = accessible-part acc(r) introduction/induction rule
  I/O    = relation r, element a, predecessor set r^-1[{a}], recursive R
           -> membership / induction conclusion for acc(r)
  Done   = guarded inductive membership/proof use only under bounded
           monotonicity; no runtime lifecycle asserted
  Q?     = whether this source-defined reentry is a negative/unpaid
           same-object obligation, or a positive monotone guard control.
PowerSetDefenseLedger target:
  PS0--PS3 inherit H060 source family; PS4 asks whether a post-guard residual
  is present; PS5 compares this valid positive use to h=Pow's invalid bound.
nonnegotiable:
  - t in Pow(R) must not be called Russell negative self-membership;
  - induction hypothesis / proof premise must not become a P3 Draft/Admitted
    runtime state without source transition;
  - a proof-package control must not become standard-ZFC or real-task result;
  - do not invent a Q merely because R reappears under Pow.
success: terminal E0--E7 public MatchTrace <=900 words; exact source fields,
         P2 Bind/Form/Bridge/Reenter/polarity ledger, P3 source transition
         check, PS0--PS6, an h=Pow counterfactual and bounded verdict.
expected outcomes: POSITIVE_MONOTONE_REENTRY_GUARD_CONTROL /
                   P3_CONSTRUCTION_SEMANTICS_NOT_SUPPLIED /
                   NO_PS4_SURPLUS, or a source-supported narrow deviation.
observation cadence: 60 seconds; automatic wall-clock interruption: absent
```
