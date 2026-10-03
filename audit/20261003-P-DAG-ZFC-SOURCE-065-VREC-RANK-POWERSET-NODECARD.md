# P-DAG-ZFC-SOURCE-065：`Vrec`／rank／Power Set 完整 source-profile 修复 NodeCard

> **身份：** `PRELAUNCH_NODECARD / UNIQUE_RUNNER_PROFILE_REPAIR / SAME_SOURCE_REGRESSION / NO_THEORY_CLAIM`。

```text
node_id: P-DAG-ZFC-SOURCE-065-VREC-RANK-POWERSET-P1P2P3
parent: H063/H064 INPUT_CONTRACT_FAILURE / NO_AGENT_OUTPUT
purpose: repeat the exact H063/H064 Vrec/rank/Power Set source card after
         the sole functional repair required by the canonical runner profile:
         one fenced payload containing BEGIN/END FROZEN SOURCE CARD markers.
actor: gpt-5.6-terra / max; fallback=false
runner: scripts/pattern_p_appserver_blind_discovery.py @ 544e8f01
private root: /Users/aurolafly/.codex-experiments/pattern-p-h065
access profile: PINNED_PRIMARY_SOURCE / source-match
permission/approval: governance-regression-fresh / never; no tools, files,
                     web, Git, or delegation
source identity, frozen TaskCard, source excerpts, question, word limit,
expected verdict and observation cadence: H063 original source/card content.
sole functional repair:
  - H063 omitted the required single ```text payload.
  - H064 added the payload but omitted BEGIN FROZEN SOURCE CARD / END markers
    inside it, so the runner rejected it before auth/model sampling.
  - H065 adds exactly those runner-required delimiters around the pre-existing
    frozen source identity and excerpts. It changes no source/card/question.
prelaunch verification:
  - invoke the canonical runner module's read_frozen_turn on this prompt;
  - assert the extracted payload has exactly the P-VALIDATION marker and the
    BEGIN FROZEN SOURCE CARD marker before starting any external process.
nonnegotiable:
  - H063/H064 remain INPUT_CONTRACT_FAILURE / NO_AGENT_OUTPUT;
  - this is an execution-spec repair, not a theory result or model failure;
  - new run ID required; no earlier artifact is overwritten.
success: prelaunch parser/profile PASS; prompt-input gate PASS; terminal E0–E7
         public MatchTrace <=900 words, exact parent E3 echo, zero tool/file/
         approval use and bounded verdict.
observation cadence: 60 seconds; automatic wall-clock interruption: absent
```
