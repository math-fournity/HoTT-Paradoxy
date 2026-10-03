# P-DAG-ZFC-SOURCE-060：有界不动点 / Power Set 防御 NodeCard

> **身份：** `PRELAUNCH_NODECARD / PINNED_PRIMARY_SOURCE / POWERSET_DEFENSE_LEDGER_PROBE / NOT_A_ZFC_Q_OR_MATHEMATICAL_RESULT`。

```text
node_id: P-DAG-ZFC-SOURCE-060-FIXEDPT-POWERSET-P1
parent: P-FORGE-SOP / PowerSetDefenseLedger; RK-0 H049-H053 guard result
purpose: inspect a version-fixed Isabelle/ZF least-fixedpoint source in which
         Pow(D) is the lattice of candidate subsets, lfp(D,h) is admitted
         only under bnd_mono(D,h), and the accompanying primary package
         documentation says h=Pow has no suitable domain. Determine whether
         this is a source-defined Power Set guard, whether it supplies a
         same-layer P1 consumer/positive unpaid Q, and what PS4/PS5 require.
actor: gpt-5.6-terra / max; fallback=false
runner: scripts/pattern_p_appserver_blind_discovery.py @ b839b7fe
private root: /Users/aurolafly/.codex-experiments/pattern-p-h060
access profile: PINNED_PRIMARY_SOURCE / source-match
permission/approval: governance-regression-fresh / never; no tools, files,
                     web, Git, or delegation
primary source A: isabelle-prover/mirror-isabelle
                  src/ZF/Fixedpt.thy @ 5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8
                  SHA-256 fccd5ac849c2496dcc3f0da4a0e0ce133f1c6dc2281bc1475f5871e1af66b69b
primary source B: Lawrence C. Paulson, A Fixedpoint Approach to
                  (Co)Inductive Definitions, Isabelle/ZF package manual,
                  §2--§3.2, official Isabelle distribution PDF, frozen
                  excerpts and URL in prompt; this source explains the
                  fixedpoint package's intended use and finite-powerset
                  example.
source scope: Isabelle/ZF theory plus its proof-package documentation. The
              card may support a proof-system / formal-package consumer but
              cannot be silently raised to standard-ZFC object semantics,
              a runtime lifecycle, historical author intent, or real task.
frozen prospective card:
  T     = Isabelle/ZF Fixedpt + fixedpoint package documentation
  layer = proof-system / formal-package contract
  u     = Pow(D), the candidate-subset lattice for lfp(D,h)
  F     = lfp(D,h) = Inter({X: Pow(D). h(X) subseteq X})
  C     = fixedpoint package / lfp-unfold and induction use
  I/O   = D,h plus bnd_mono(D,h) -> lfp(D,h) / induction or fixedpoint law
  Done  = lfp(D,h) = h(lfp(D,h)) only under bnd_mono(D,h)
  Q?    = whether h=Pow leaves a source-defined positive unpaid obligation,
          or is rejected by the domain/monotonicity guard before same-task
          use; do not invent a broader ZFC Q.
PowerSetDefenseLedger target:
  PS0 = exact source / variant / layer
  PS1 = which Russell/RK-0 edge is blocked by bounded monotone fixedpoint use
  PS2 = source-declared guard(s), including h(D) subseteq D
  PS3 = scope limits
  PS4 = source-supported residual, if any, while guard remains
  PS5 = same-task counterfactual; compare h=Pow with valid bounded Fin(A)
  PS6 = bounded verdict
nonnegotiable:
  - do not call the package's proof acceptance an object-level or real-world Done;
  - do not treat the rejection of h=Pow as a theorem that all ZFC questions are safe;
  - do not replace h=Pow with naïve unrestricted comprehension and call that PS4;
  - preserve proof source, package explanation, object-level formulas and runtime
    semantics as separate layers.
success: terminal public E0-E7 MatchTrace <=900 words; exact source facts,
         layer, P1 gate ledger, PS0-PS6 table, one neighboring valid Fin(A)
         control, one counterfactual, no tool/file/approval use.
expected bounded outcomes: DEFENSE_IDENTIFIED / CANDIDATE_GUARD_BLOCKED /
                           SOURCE_GUARD_SCOPE_UNSET / NOT_ENOUGH_EVIDENCE;
                           no ZFC_Q_LOCATED or mathematical conclusion.
observation cadence: 60 seconds; automatic wall-clock interruption: absent
```
