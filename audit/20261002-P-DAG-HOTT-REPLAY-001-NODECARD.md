# P-DAG-HOTT-REPLAY-001：无答案泄漏 HoTT 校准 NodeCard

> **身份：** `PRELAUNCH_HOTT_CALIBRATION_NODE / BLIND_SOURCE_PACK / NOT_A_MATH_RESULT`。
>
> **目标：** 检验当前 P1/P2/P3 的公开规格能否仅从固定 HoTT Book 原典片段，定位一个理论自身的基础接口与候选 Q。它不要求代理重述项目既有的 `QuestioningDelay`、`never`、宇宙无层级结论或任何审计答案；这些材料均不在输入中。

## Frozen TaskCard

```text
task_id: P-DAG-HOTT-REPLAY-001
T: HoTT Book / book-style HoTT source packet, fixed local source snapshot book-578b85cc
target: no-answer-leak P calibration, not a theorem proof or a ZFC comparison
candidate u/F/C/Q/I/O/Done: all UNKNOWN before agent output
layer: theory-object / book-rule layer only
disallowed task switches: project code, QuestioningDelay/PedometerSemantics, existing HoTT results,
                         internet, source outside packet, new axioms, source-invented lifecycle
success for agent: terminal public E0–E7 MatchTrace or an honest no-qualified-site verdict
release predicate (Master-only): source-grounded P1 location, nontrivial native Q/consumer demand,
                                 task-fidelity review; P2/P3 may legitimately be blocked but cannot be invented
deadline: 45 seconds after healthy runner confirmation
```

## Source identity and no-leak pack

The upstream book source snapshot is `HoTT/book` local snapshot `book-578b85cc`. Source file hashes:

```text
formal.tex  e621484e2e457e70536a92367cca452f34df8ecfc9a17a3bdf0e4ee67e5f0cec
hlevels.tex cfa75d289487f91affc4f5a9907857135c8a307b59dbc1cb9e3e9f41399618cc
```

The external worker receives only these neutral excerpts:

```text
formal.tex §Type universes:
  U_0, U_1, U_2, ... ; U_m : U_n for m<n;
  if A:U_m and m≤n then A:U_n; an object of a universe can serve as a type.

formal.tex §Function extensionality and univalence:
  for A,B:U_i, univalence(A,B) inhabits isEquiv(idtoeqv_{A,B}).
  Higher inductive types are stated as additional core theory features.

hlevels.tex §Homotopy n-types:
  isType(n)(X) is defined recursively through path spaces;
  Type_n := Σ(X:Type). isType(n)(X); identities of such pairs are related to equivalences.
```

Excluded: Book §8.8 examples, the repository's questioning programs and formal proofs, all past agent outputs, source code, network, project files, and any statement that a particular HoTT question has already been found.

## NodeCard H-001-A

```text
role: blind P1/P2/P3 calibration mapper
runner: fresh Codex CLI --no-daemon --ephemeral
model/effort: gpt-5.6-terra / max
sandbox/approval: read-only / never
access: frozen prompt only; no web, no local filesystem, no Git, no delegation
output: public E0–E7 + Claims/Evidence/Conflicts/Unknowns/Mutations/Verification/Recommendation
timeout: 45 seconds; terminal result required
partial output: fail closed
```

## Master acceptance boundary

The agent cannot by itself release the HoTT gate. Master must compare its completed public trace against original-task fidelity and fixed source facts. A merely plausible mention of universes, univalence, h-levels, infinity or self-reference does not pass; nor does an agent's failure refute P. The exact public result, regardless of outcome, receives a delta SelfAuditCard and Git record.

## H-001-A execution outcome

Fresh CLI session `01a0fd84-90c6-7a33-889b-fe955c624e42` displayed the requested Terra/Max/read-only/never banner and began generating a structured answer. At the 45-second NodeCard deadline it had not returned terminal output through the host runner; before Master could collect a final answer, its process had exited and no recoverable result artifact existed.

```text
TIMEOUT_NO_TERMINAL_OUTPUT
NO_MATCHTRACE_AVAILABLE_TO_MASTER
NOT_A_HOTT_REPLAY_VERDICT
```

This is a runner/output-capture failure. Exactly one successor retry is permitted because it changes the execution contract: CLI final output must be saved to a unique `/tmp` path and polled by Master, with a 90-second deadline. Same prompt/source without that capture repair must not be repeated.
