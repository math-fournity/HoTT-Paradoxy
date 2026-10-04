# P-DAG H100：IEP 显式完成替换是否满足候选 P 的来源形状

> **身份：** `PRELAUNCH_NODECARD / SOURCE_MATCH / READ_ONLY / NO_WRITE / CONTRIBUTOR_CANDIDATE_NOT_CURRENT`。

```text
node_id: P-DAG-H100-IEP-COMPLETION-SUBSTITUTION-SOURCE-MAP
parent: ZFC-P-100 TaskCard; H091/H093; H099
objective: classify only whether the frozen IEP facts instantiate R1, R2 and
           R3 of CompletionSubstitutionP, distinguishing explicit Done
           replacement from same-task preservation or a logical inconsistency.
non-goals: no web search; no new source facts; no claim that actual ZFC is
           inconsistent, lacks time, or has P as an object-language axiom; no
           claim that all limits are task switches; no HoTT verdict.
actor: gpt-5.6-terra / max; fallback=false
runner: scripts/pattern_p_appserver_blind_discovery.py --profile source-match
private_root: /Users/aurolafly/.codex-experiments/pattern-p-h100-iep-p-source
method_repo: /Users/aurolafly/codex (must be clean)
workspace: run-scoped text-only workspace outside business repo
access_profile: PINNED_PRIMARY_SOURCE; frozen prompt only; no tools/files/web/
                Git/delegation; permission=governance-regression-fresh;
                approvalPolicy=never; network=false; recursion=false.
input: 20261004-P-DAG-ZFC-P-100-PROMPT.md; SHA frozen before launch.
output: E0-E7 public MatchTrace ≤900 words; Claims/Evidence/Conflicts/
        Unknowns/Mutations/Verification/Recommendation; `Mutations=none`.
prelaunch: exactly one fenced text payload; exact `P-VALIDATION` marker and
           BEGIN/END FROZEN SOURCE CARD; runner read_frozen_turn must pass.
observation: 60 seconds; record liveness only; never wall-clock interrupt.
terminal audit: required private direct-wire trajectory receipt; do not expose
                private prompt/wire/credentials/reasoning.
acceptance: exact model/effort/cwd/permissions echo; normal terminal; zero
            tool/file/approval; E0-E7; source-bounded classification.
failure: INPUT_CONTRACT_FAILURE / NO_AGENT_OUTPUT; RUNNER_CONNECTION_FAILURE;
         FAIL_OUTPUT_OR_TOOL_CONTRACT; ACCESS_LEAK_SUSPECTED.
successor: only a field conflict with H091/H093/H099 triggers bounded Battle.
```
