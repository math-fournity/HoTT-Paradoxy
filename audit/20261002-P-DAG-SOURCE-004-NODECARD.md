# P-DAG-SOURCE-004：Isabelle/ZF Cantor 消费者的预封存 NodeCard

> **身份：** `PRELAUNCH_NODECARD / PINNED_SOURCE_PACK / NOT_A_SOURCE_RESULT`。
>
> **状态：** `RUNNER_CONNECTION_FAILURE / NO_AGENT_OUTPUT`。本卡在 worker 启动前写入；它保留冻结输入和运行失败，未包含任何 P1 source judgement，也不预设 ZFC Q。

## TaskCard

```text
task_id: P-DAG-SOURCE-004
theory variant T: Isabelle/ZF Base, official Isabelle2025-1-RC1 library page
research target: Power Set 在数学语义／证明任务层的 named consumer contract
target layer: mathematical semantic proof task
u: Pow(A)
F: PowI / Pow_iff (only as source pack provides)
C/Q/I/O/Done: UNKNOWN; worker may fill only from the frozen source text
disallowed switches: proof-system acceptance as semantic Done; runtime/implementation timing;
                    source outside the pack; paradox or lifecycle invention
success: one E0–E7 public trace that classifies the source card and L6/L7 status
stop: 90 seconds wall-clock; no terminal output = TIMEOUT_NO_TERMINAL_OUTPUT
```

## Frozen primary-source pack

**URL/version identity:** [Isabelle2025-1-RC1, `FOL/ZF/ZF_Base`](https://isabelle.in.tum.de/website-Isabelle2025-1-RC1/dist/library/FOL/ZF/ZF_Base.html), official library page. The Master obtained the following source excerpts from the official page's indexed result on 2026-10-02; the pack is intentionally limited to these quoted formulas and headings.

```text
Rules for Powersets
lemma PowI: "A ⊆ B ⟹ A ∈ Pow(B)"
lemma PowD: "A ∈ Pow(B) ⟹ A ⊆ B"

Cantor's Theorem: There is no surjection from a set to its powerset.
lemma cantor: "∃S ∈ Pow(A). ∀x∈A. b(x) ≠ S"
by (best elim!: equalityCE del: ReplaceI RepFun_eqI)
```

The pack supports no hidden diagonal definition, no full proof trace, no verified runtime, and no construction lifecycle. A returned claim must state those limits.

## NodeCard N-004-A

```text
role: P1 semantic-card mapper
runner: fresh Codex CLI --ephemeral
model/effort: gpt-5.6-terra / max
sandbox/approval: read-only / never
access: PINNED_SOURCE_PACK only; no network, local project, Git, scratch, prior answers or delegation
output: public E0–E7 + Claims/Evidence/Conflicts/Unknowns/Mutations/Verification/Recommendation
deadline: 90 seconds; Master sends SIGINT if no terminal result
partial-output policy: fail closed; no interim plan or console text becomes a source fact
```

## Acceptance and successor

The only acceptable result is a source-bounded classification of whether `cantor` supplies a mathematical semantic proof-task C/I/O/Done and whether its `S ∈ Pow(A)` is a positive nontrivial Q, an immediately discharged formation consequence, or an insufficiently specified subgoal. `P2`, `P3`, Battle and Q review do not begin unless the resulting card is terminal, source-grounded and layer-labeled.

## Execution outcome: no source result

The initial background attempt created no console or final artifact, so it is not counted as an agent turn. A foreground retry did create session `01a0fd6f-a6d8-7db1-a4a4-7184ff2ac118` and showed the requested `gpt-5.6-terra / max / read-only / never` banner. Before the model returned any answer, the runner repeatedly failed workspace routing and ended with `workspace routing discovery failed`.

```text
RUNNER_CONNECTION_FAILURE
NO_AGENT_OUTPUT
NO_MATCHTRACE
NO_SOURCE_CARD_UPDATE
```

This is an infrastructure/connection failure, not a source-negative verdict or evidence about P1. The next independent-agent retry requires an observable healthy runner first; until then, only the Master may read the frozen official source directly, with its evidence identity kept separate from a worker result.
