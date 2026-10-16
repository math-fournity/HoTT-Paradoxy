# P-DAG-SOURCE-005：Isabelle/ZF Cantor 来源卡的 Master 直接审读

> **身份：** `MASTER_PRIMARY_SOURCE_READ / TARGET_LAYER_NEGATIVE_CONTROL / NOT_AN_AGENT_RESULT / NOT_A_ZFC_Q_RESULT`。
>
> **判词：** `SOURCE_INSUFFICIENT_FOR_SEMANTIC_CONSUMER_CARD / PROOF_TASK_PRESENT / NO_NATIVE_Q / NO_P2_OR_P3_MAPPING`。这张来源卡说明一个 Power Set 相关的正式数学定理可以存在，而不提供 P1 所需的“同一 `u` 作为真实消费者输入”的合同，也不提供 P2/P3 所需的结构。

## 1. 固定来源与读取范围

Master 于 2026-10-02 以 Git remote 查询将 [`isabelle-prover/mirror-isabelle`](https://github.com/isabelle-prover/mirror-isabelle) 的 `master` 固定为 commit:

```text
5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8
```

直接读取的 raw source 是：

[`src/ZF/ZF_Base.thy`](https://raw.githubusercontent.com/isabelle-prover/mirror-isabelle/5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8/src/ZF/ZF_Base.thy)

读取 SHA-256：

```text
33693f4e5d03933f2a0d36ed8350c3e541286cee9889e48f9e39eff5a1e63401
```

直接审读范围是 source 的 `Pow` signature／`Pow_iff` axiom、lines 640–660 的 `PowI`、`PowD` 和 `cantor`。该文件是 Isabelle 对 ZF 的形式化，不应被写成标准 ZFC 本身或一个可执行的对象构造过程。

## 2. 可直接支持的来源事实

```isabelle
lemma PowI: "A ⊆ B ⟹ A ∈ Pow(B)"
lemma PowD: "A ∈ Pow(B) ⟹ A ⊆ B"

lemma cantor: "∃S ∈ Pow(A). ∀x∈A. b(x) ≠ S"
  by (best elim!: equalityCE del: ReplaceI RepFun_eqI)
```

`Pow_iff` 在相同 source 中被公理化为 `A ∈ Pow(B) ↔ A ⊆ B`。`cantor` 的注释说明 `b` 可以是从 `A` 到 `Pow(A)` 的映射；它陈述任意此类候选映射都不能覆盖 `Pow(A)`。

## 3. 冻结层与 P1 字段审读

| 字段 | 来源实际支持 | 不可补造的内容 |
|---|---|---|
| `T` | Isabelle/ZF formalization @ fixed commit | 标准 ZFC 的全部语义或实践。 |
| `u` | `Pow(A)` 是 ZF object-language term，`PowI`/`PowD` 规定成员等价于 subset。 | 一个实际构造过程中的 pending object。 |
| `F` | `Pow_iff`、`PowI` 和 `PowD`。 | 一个由 source 展开的“所有子集逐一完成”的算法。 |
| candidate theorem task | `cantor` 是一个已命名的**证明任务**：给定 `A,b`，证明存在 `S∈Pow(A)` 与分离性质。 | 一项 source-defined object-level operation 以既有 `Pow(A)` 为输入并交付下游对象。 |
| `I/O/Done` | 在 proof-system/formal-theorem 层：assumptions/statement/proof accepted。 | mathematical runtime／实际使用层的 consumer I/O/Done。 |
| candidate `Q` | `S∈Pow(A)` 出现在 `cantor` 的 existential conclusion。 | `Q` 是 formation 未支付债务、native positive prerequisite 或在 Q 未完成时已发生的 preemptive use。 |

`cantor` 的 `S` 是 theorem 输出约束中的见证，`Pow(A)` 是该见证所属集合的限制。卡中没有命名一个操作把 `u=Pow(A)` 当作输入交给下一步，因而不满足 P1 L2/L2b 所要求的 same-`u` consumer contract。它也不以源中可见的方式定义 diagonal `S`、证明 `S⊆A`，再用 `PowI` 完成一项同一任务；`by best` 不能替代被审计的数学构造／consumer。

## 4. P1/P2/P3 Master verdict

```text
P1: SOURCE_INSUFFICIENT_FOR_SEMANTIC_CONSUMER_CARD
    (proof task exists; same-u consumer input / source-defined semantic Done absent)
P2: NOT_APPLICABLE_ON_SOURCE_SCOPE
    (no represented formula → bridge → legal reentry chain in the read slice)
P3: CONSTRUCTION_SEMANTICS_NOT_SUPPLIED
    (no Draft/Admitted/OperatorUse/BuildDone transition)
Q: NOT_NATIVE_TO_CURRENT_CARD
MasterVerdict: NO_COMMON_Q / NOT_ZFC_Q_LOCATED
```

This is not a negative result about Cantor's theorem. It is a P1 control: a mathematical theorem that mentions `Pow(A)` and proves an existential set does not automatically furnish the required consumer/Done contract. It also confirms that the current L2/L2b and L2c wording already blocks the false promotion; no new mathematical knife or new P1 layer is warranted from this source alone.

## 5. Relation to the origin audit and successor

The full origin audit currently blocks ZFC Q promotion until an independent, no-answer-leak HoTT replay succeeds. This Master source read is therefore a **calibration control only**. A future Terra/Max node may re-audit this fixed source after runner health succeeds, but its output must remain an independent receipt and cannot be backfilled from this Master analysis.

## 6. Delta SelfAuditCard

| Field | Record |
|---|---|
| Original units | C14 (HoTT replay before ZFC upgrade), C25 (source/Battle must be controlled), O22 (layered dynamic DAG). |
| Actual action | Master read a fixed primary source after the independent runner failed, and labeled the action `MASTER_PRIMARY_SOURCE_READ`. |
| Alignment verdict | `ALIGNED_WITH_GATE`: calibration source work is permitted; no ZFC Q upgrade, agent claim, or Battle was opened. |
| Deviation class | None in the source reasoning. The absent independent replay remains the previously recorded `RUNNER_OR_EVIDENCE_FAILURE`, not cured by this Master read. |
| Affected tools | P1 receives a same-`u` theorem-statement negative control; P2/P3 unchanged. |
| Falsifier / next trigger | A source that gives `Pow(A)` as an actual target-layer consumer input with native Q/Done, or a healthy independent Terra/Max runner that can re-audit this exact source. |
| Git eligibility | Yes: a fixed primary source, a bounded verdict, a source-preserving control, and a completed delta audit form one natural calibration unit. |
