# P-DAG-HOTT-DISCOVERY-007：盲态 CLI 上下文泄漏与终止收据

> **身份：** `ACCESS_LEAK_SUSPECTED / GLOBAL_INSTRUCTION_INJECTION_OBSERVED / TERMINATED_BY_MASTER_SIGINT / NO_VALID_DISCOVERY_OUTPUT`。

## 1. Frozen node and observed execution

H-007 had a prelaunch NodeCard, a hashed D-L6b prompt, an isolated `/tmp` working directory, `--ephemeral`, `--ignore-user-config`, `--ignore-rules`, `--skip-git-repo-check`, `read-only`, and `approval=never`. The requested runtime banner did confirm `gpt-5.6-terra / max / read-only / never`.

Despite that setup, the visible console showed the model receiving a global governance instruction and then attempting tool use:

```text
assistant: 我会先按项目的认知闭包流程确认该 prompt 在当前仓库中的位置…
exec: wc -l /Users/aurolafly/.codex/skills/repo-cognitive-closure/SKILL.md ...
exec: rg --files -g AGENTS.md ...
exec: git rev-parse --show-toplevel ...
```

The NodeCard prohibited files and tools. The process was sent `SIGINT` immediately after this observation. There was no final artifact at `/tmp/hott-p-dag-hott-discovery-007-final.md`.

## 2. Verdict

```text
BLIND_CARD_CONTEXT_ISOLATION: NOT_QUALIFIED
H-007 output: NO_VALID_DISCOVERY_OUTPUT
failure class: ACCESS_LEAK_SUSPECTED / RUNNER_OR_EVIDENCE_FAILURE
mathematical/theory verdict: NONE
```

This is not a conclusion about HoTT, P1, Terra, or the D-L6b rule. It is a concrete failure of the intended blind-node environment: a worker that must only receive a sealed prompt instead saw global instructions sufficiently strong to redirect it into repository-governance/tool behavior.

## 3. Retroactive evidence correction

H-005 and H-006 used the same fresh CLI family. Their output files show no observed project-file access, but the H-007 observation means their **blind-context isolation was never qualified**. Therefore:

| Artifact | Still usable | Must be downgraded |
|---|---|---|
| H-005 Master Book read | The fixed-source conclusion that `ua` directly supplies the inverse direction. | Its worker output is no longer evidence of a verified no-leak blind discovery pass. |
| H-006 prompt/output text | The explicit D-L6/D-L6b prompt-control design and its recorded output. | It is not an independent blind Terra/Max behavior measurement. |
| H-007 | Prelaunch prompt/NodeCard and observed failure trace. | No candidate, negative theory claim, or D-L6b behavior result may be inferred. |

The P1 D-L5/D-L6/D-L6b specifications remain a Master-owned, source/prompt-grounded tool design. Their empirical blind-replay status is now `BLIND_RUNNER_ISOLATION_UNQUALIFIED` until a new runner control passes.

## 4. Delta SelfAuditCard

| Field | Record |
|---|---|
| Original units | C12/C14/C20–C22 require actual Terra/Max work without cheating; C25 requires NodeCard-level access control; O11/O13/O19/O22 require evidence rather than prompt promises. |
| Actual action | A D-L6b differential blind run was launched with an isolated scratch cwd and CLI flags, then terminated on visible global-instruction/tool injection. |
| Alignment verdict | `RUNNER_OR_EVIDENCE_FAILURE`: Master stopped rather than consuming contaminated output. |
| Repair | Suspend fresh CLI `BLIND_CARD` nodes. Before another HoTT/ZFC blind replay, create a zero-theory runner-isolation health NodeCard that proves neither global instruction injection nor any tool call occurs. |
| Affected scope | H-005/H-006 blind evidence downgraded; Master source controls remain separately labeled; P2/P3 and ZFC status unchanged. |
| Falsifier | A newly isolated runner, with visible prompt-only behavior and no tool event, may requalify future blind nodes but cannot retroactively make H-005/H-006 blind. |

## 5. Boundary

No secret, project answer, or final H-007 text was consumed. The only retained execution evidence is the visible runner/banner/tool-attempt sequence and the absence of the final artifact.
