---
name: zcode-gui-session-export
description: Export a private, copyable Markdown transcript for one ZCode Desktop session, preserving GUI-visible content only—user's real typed messages, assistant's visible replies, AskUserQuestion interactions (question, options, user's selection), and GUI-visible failed-reply error notices (rate limit, cancellation, provider errors). Use when the user wants "the conversation as seen in the GUI"; use audit mode only when raw-locator breadcrumbs are explicitly required.
---

# ZCode GUI Session Export

## Purpose

Create a private Markdown transcript for exactly one ZCode Desktop session. The
default `gui` mode preserves only what was visible in the GUI:

- the user's real typed messages, verbatim;
- the assistant's visible text replies, verbatim, Markdown unchanged (never
  wrapped in a text fence, so a reply can be copied directly);
- AskUserQuestion interactions as inline capsules: question, options, and the
  user's actual selection (or the raw timeout/cancel note when no answer was
  given);
- failed replies as a marked `### 回复失败（GUI 可见错误提示）` capsule: the
  error code/label plus the GUI-visible error message (truncated to 400
  chars). A turn that failed after partial output keeps both the partial
  text and the error capsule. Intermediate streaming-retry errors
  (`StreamRecoveryDiscarded`) are not GUI-visible failures; they are skipped
  and only counted in the receipt (`errors_intermediate_skipped`).

It reads the local ZCode session database **read-only** and writes only to the
private ignored directory:

~~~text
~/.zcode/trajectory-ref-exports/
~~~

Files are created with mode 0600. Do not copy the transcript body, raw JSON,
reasoning text, tool output, credentials, or unrelated sessions into chat.

`audit` mode is explicit and separate: it keeps everything from `gui` mode plus
raw locators (message ids, part ids, timestamps, fork-origin breadcrumbs) for a
bounded later audit. It is not the default and must not be used when the user
asks only for what was visible in the GUI.

## Storage Model (verified on ZCode Desktop 3.14.4, 2026-10-15)

- Database: `~/.zcode/cli/db/db.sqlite`, opened with `mode=ro`.
- `session` table: `id`, `parent_id` (fork chain: a fork records its parent),
  `project_id`.
- `message` table: `role` (`user`/`assistant`), `time_created`, `data` JSON.
  Real user input is a message **without** `metadata.source`/`synthetic`
  markers; todo reminders, agent-listing deltas and fork markers carry those
  markers and are skipped.
- `part` table: the message body, keyed by `message_id`. `type=text` is the
  visible text; `type=reasoning`, `type=tool` (except AskUserQuestion),
  `type=step-start`/`step-finish`/`timeline` are skipped.
- The rollout JSONL under `~/.zcode/cli/rollout/` is a separate, deeper
  evidence layer; this Skill does not read it. For recursive multi-layer
  trajectory analysis use `repo-agent-session-trajectory`
  (`session_trajectory.py`); for the raw model-io JSONL adapter see the shared
  capability index entry `CAP-TRAJ-ZCODE`.

## Execute

~~~text
python3 ~/.zcode/skills/zcode-gui-session-export/zcode_gui_session_export.py --mode gui --session <session-id-or-unique-prefix>
~~~

Useful variants:

~~~text
--list                     # enumerate sessions with message counts and fork links
--mode audit               # gui content + raw locators (only on explicit request)
~~~

The helper prints only a small JSON receipt: output path, mode, status,
session id, fork parent, turn count, injected-skipped count, assistant message
count, AskUserQuestion count, failed-turn count (`failed_turns`,
`error_capsules`), and intermediate-retry errors skipped
(`errors_intermediate_skipped`). Never print the transcript body in chat; offer
the absolute path or open the file only when the user asks.

## Identity Rules

- Exact session-id match: export.
- Unique prefix match: export.
- No match: report `SESSION_NOT_FOUND` and stop; never guess a near id.
- Ambiguous prefix: report `SESSION_AMBIGUOUS` and stop; ask the user for more
  of the id.
- A fork session is exported by its own id; its header records
  `Fork 来源: <parent id>`. The parent session can be exported separately the
  same way. Never merge a fork with its parent into one transcript.

## What the Transcript Keeps / Omits

Kept: session id, project, time range, fork parent, per-turn timestamp, user
text (verbatim, fenced as `~~~~text`), AskUserQuestion capsules, assistant
visible texts in original order, failed-reply error capsules with their
GUI-visible error message.

Omitted: reasoning, tool calls and tool results (except the AskUserQuestion
capsule), system injections, fork markers, context snapshots, model/provider
metadata, file-change internals, secrets, intermediate streaming-retry errors
(not GUI-visible).

## Completion

`COMPLETE` in the receipt means the session was resolved and every visible
user/assistant message found in the database was rendered. It does not prove
context injection, model behavior, or task success—those are L1–L5 questions
for the shared trajectory tooling, not for a GUI transcript.

## Version

- v1.1.0 (2026-10-16): failed-turn error capsules. A turn whose assistant
  reply failed (rate limit, cancellation, provider error) renders the
  GUI-visible error notice instead of silently appearing as "no reply";
  turns that failed after partial output keep both. Intermediate
  `StreamRecoveryDiscarded` retry errors are skipped with a receipt counter.
  Receipt gains `failed_turns`, `error_capsules`,
  `errors_intermediate_skipped`; the header time range now includes error
  timestamps. Verified on `sess_2af613d9…` (7 failed turns incl. the final
  429 pair; partial-reply turn 39 keeps text + `model_rate_limited` capsule)
  and `sess_464bb196…` (21 intermediate retries skipped, 15 real failures
  rendered).
- v1.0.0 (2026-10-15): first version; verified against a real fork session
  (`sess_cd2f0c1d…`, forked from `sess_52c0b20f…`) on ZCode Desktop 3.14.4:
  19 turns, 12 AskUserQuestion capsules, ledger-consistent with the database
  (19 user text parts, 72 assistant text parts).
