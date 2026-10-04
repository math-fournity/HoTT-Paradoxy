# P-DAG H106：H100 冻结输入哈希漂移的 source-match 修复重跑

> **身份：** `Q_SAFETY_REPAIR / PRELAUNCH_NODECARD / READ_ONLY / NO_WRITE / CONTRIBUTOR_CANDIDATE_NOT_CURRENT`。

```text
node_id: P-DAG-H106-IEP-COMPLETION-SUBSTITUTION-CURRENT-BYTE-REPLAY
parent: H100; ZFC-P-100 TaskCard; formal-closure verifier hash-drift finding
trigger: H100's actual App Server turn was run on the pre-format source bytes.
         The current TaskCard and H100 prompt preserve semantic text but have
         different SHA-256 after trailing-blank normalization.
objective: rerun the exact H100 source-match question using the currently
           committed TaskCard/prompt bytes; establish a fresh source receipt
           whose input hashes match current closure verification.
non-goals: no new source search, no altered theory claim, no ZFC/HoTT theorem,
           no P→B, no community adoption, no Q convergence or new knife.
actor: gpt-5.6-terra / max; fallback=false
runner: scripts/pattern_p_appserver_blind_discovery.py --profile source-match
private_root: /Users/aurolafly/.codex-experiments/pattern-p-h106-iep-current-byte-replay
method_repo: /Users/aurolafly/.codex-experiments/method-repo-h081 (must be clean)
workspace: run-scoped text-only workspace outside business repo
access_profile: PINNED_PRIMARY_SOURCE; current H100 frozen payload only; no
                tools/files/web/Git/delegation; permission=governance-regression-fresh;
                approvalPolicy=never; network=false; recursion=false.
input: audit/20261004-P-DAG-ZFC-P-100-PROMPT.md;
       current SHA-256=65e3e438f2c7501de45ec8f8e4a9c2d253822a1fe22f15358d2f33e5f7a271c8.
taskcard: audit/20261004-P-DAG-ZFC-P-100-TASKCARD.md;
          current SHA-256=6492ca5890e559f2f374ff9e4baafb0b4c81d15633bf6cecc3b399fd6e0812bb.
output: E0-E7 public MatchTrace ≤900 words; `Mutations=none`.
prelaunch: exactly one fenced text payload; P-VALIDATION marker; frozen-card
           boundaries; read_frozen_turn and prompt-input gate must pass.
observation: 60 seconds; never automatic interruption.
terminal audit: required private direct-wire trajectory receipt.
acceptance: exact model/effort/cwd/permissions echo; zero tool/file/approval;
            E0–E7; source status must be scoped to H100's existing question.
failure: INPUT_CONTRACT_FAILURE / NO_AGENT_OUTPUT; RUNNER_CONNECTION_FAILURE;
         FAIL_OUTPUT_OR_TOOL_CONTRACT; ACCESS_LEAK_SUSPECTED.
QConvergenceLink: Q_SAFETY_REPAIR only. It changes no theory-card status; it
                  repairs the hash binding that prevents a current evidence
                  closure from silently using stale prompt bytes.
```
