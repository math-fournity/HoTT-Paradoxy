# P-DAG-RUNNER-ISOLATION-002：空 CODEX_HOME 认证边界结果

> **身份：** `ZERO_THEORY_RUNNER_HEALTH / EMPTY_CODEX_HOME_AUTHENTICATION_UNAVAILABLE / NO_MODEL_SAMPLE / RUNNER_ISOLATION_NOT_QUALIFIED`。

## 1. What was tested

The prelaunch NodeCard used an empty, mode-`0700` temporary `CODEX_HOME`, a separate scratch cwd, `--ephemeral`, `--ignore-user-config`, `--ignore-rules`, read-only sandbox, `approval=never`, exact Terra/Max request, and `cli_auth_credentials_store="keyring"`. The only prompt was the exact one-line health marker in [the frozen prompt](20261002-P-DAG-RUNNER-ISOLATION-002-PROMPT.md).

The banner confirmed the requested model, effort, sandbox, and approval values. Before any model response, the CLI repeatedly received:

```text
401 Unauthorized: Missing bearer or basic authentication in header
```

It exhausted retry/fallback behavior without creating `/tmp/hott-p-dag-runner-isolation-002-final.md`.

## 2. What this establishes

| Question | Result |
|---|---|
| Did this test expose a theory prompt or project answer? | No. The prompt contains no theory material. |
| Did a model sample or tool call occur? | No observable model sample, terminal answer, or tool event occurred. |
| Did empty `CODEX_HOME` authenticate through the requested OS keyring? | No; the connection failed before sampling with `401 Unauthorized`. |
| Is the new runner a qualified prompt-only blind lane? | No. It has no usable authentication, so isolation behavior cannot yet be tested. |

Official OpenAI documentation explains why the preceding H-007 failure matters: Codex CLI automatically injects `AGENTS.md` files from `~/.codex` and the cwd ancestry. [The official Codex guide](https://developers.openai.com/api/docs/guides/latest-model) describes those injected instructions and recommends auditing all accessible instruction files. The empty-home attempt is intended to remove that global path, but it cannot sample without a dedicated authentication boundary.

## 3. Credential boundary preserved

The current authenticated CLI uses a user-owned file store. The file's existence, mode `0600`, and byte count were inspected only to diagnose the storage class; its contents were not read, copied, linked, logged, or mounted. Copying that file into the temporary home would make it reachable by the same process family whose file/tool boundary failed in H-007, so it is not a safe repair.

No pre-existing alternate isolated authenticated Codex home was found in the inspected configuration locations.

## 4. Delta SelfAuditCard

| Field | Record |
|---|---|
| Original units | C12/C14/C20–C22 require a real Terra/Max no-cheat test; C25 requires Master to control access by NodeCard. |
| Actual action | Zero-theory, empty-home health node with no credential copying. |
| Alignment verdict | `RUNNER_OR_EVIDENCE_FAILURE` with credential boundary preserved. |
| Repair status | A blind node remains blocked until the user provides or authorizes a dedicated isolated authenticated runner. |
| Forbidden workaround | Do not copy/symlink the user file-auth credential into a model-readable temporary home. |
| Effect on math | None: no HoTT/ZFC/P claim changes. |

## 5. Required external state

One of the following must exist before a new blind theory node can be launched:

1. a separately authenticated `CODEX_HOME` with no global/project `AGENTS.md` on the worker's discovery path and a credential boundary not readable by its tools; or
2. an isolated external/App Server harness that returns exact model/effort, read-only/never, visible context, and no-tool health evidence.

Until then, Master-only source analysis and tool design can continue, but they cannot substitute for the requested independent Terra/Max blind replay.
