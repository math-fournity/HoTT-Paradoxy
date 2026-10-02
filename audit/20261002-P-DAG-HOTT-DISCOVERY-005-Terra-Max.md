# P-DAG-HOTT-DISCOVERY-005：D-L5 原生任务锚点的 HoTT 发现与来源验证

> **身份：** `P_DISCOVERY_TERMINAL_OUTPUT / D_L5_DISCOVERY_PASS / P1_L6_TRIVIAL_CONTROL / NOT_A_HOTT_REPLAY_PASS`。
>
> **最终判词：** H-005 在无答案泄漏的薄 HoTT source packet 上首次把候选 `Q?` 写成一项原生等价使用任务；但固定 HoTT Book 来源显示该任务正是 univalence 所承诺的逆方向。因此它通过 D-L5，随后在 P1 的 L6/Q-friction 被拒绝，不能成为 HoTT 重放的张力 Q。

## 1. 执行收据与隔离边界

| Field | Value |
|---|---|
| Parent NodeCard | [`20261002-P-DAG-HOTT-DISCOVERY-005-DL5-NODECARD.md`](20261002-P-DAG-HOTT-DISCOVERY-005-DL5-NODECARD.md) |
| Session | `01a0fd94-d625-7f50-a64e-88bc80e39f6e` |
| CLI banner | `gpt-5.6-terra / max / read-only / never` |
| Visible material | Only the frozen HOTT-DISCOVERY-003 / HOTT-REPLAY-001 source packet and the D0–D5 discovery contract. |
| Prohibited material | Project answers, prior discovery outputs, Book §8.8 examples, questioning code, web, Git, local files, tools, and delegation. |
| Terminal output | `/tmp/hott-p-dag-hott-discovery-005-final.md` |
| SHA-256 / bytes | `f6f6728f0ea112b6a1632c2e208936cad65abaef673ebb74a0670a9dbc9a32bc` / `2214` |

The SHA-256 above is the immutable output receipt for this node. It is a public MatchTrace, not a disclosure of hidden reasoning or of model training data.

## 2. Worker 的公开发现 trace

The worker selected one candidate and one nearby alternative:

```text
D1 candidate:
  u = U_i
  F = univalence(A,B) : isEquiv(idtoeqv_{A,B})
  Q? = given e : A ≃ B, may the stated isEquiv witness be used in its
       inverse direction to form p : A = B?

D2 alternative:
  Type_n = Σ(X : Type). isType(n)(X), with an identity/equivalence question.

D3 native-task anchor:
  use the univalence witness on an equivalence to seek a term p : A = B.

D4–D5:
  C/I/O/Done and P2/P3 are UNKNOWN; a controlling source can falsify
  applicability by withholding an inverse direction.
```

This is materially different from H-004. The candidate is an actual prospective formation/equivalence-use task: from an equivalence, form a path in a universe. It is not a question about universe labels, encoding, or an external formalization decision.

## 3. Master 的独立来源验证

The Master then read the repository-local frozen HoTT Book source at:

```text
HoTT/theory-schema/upstream/book-578b85cc/formal.tex:1001–1012
HoTT/theory-schema/upstream/book-578b85cc/basics.tex:1715–1793
HoTT/theory-schema/upstream/book-578b85cc/equivalences.tex:1–24, 495–508
```

The checked file hashes are:

```text
formal.tex        e621484e2e457e70536a92367cca452f34df8ecfc9a17a3bdf0e4ee67e5f0cec
basics.tex        516b469d7356e9d20df5539e726a0468760f9fa7b7f440b9c054981e803d7533
equivalences.tex  037dce18db74526a3f7148c353bb5459da1c4b65e046780a208de39633df1722
```

Those source passages support these limited facts:

1. The formal presentation types `univalence(A,B)` as `isEquiv(idtoeqv_{A,B})`.
2. `idtoeqv` maps a path `p : A = B` to an equivalence `A ≃ B`.
3. The Book states the univalence axiom as the assertion that this `idtoeqv` is an equivalence, then presents `ua : (A ≃ B) → (A = B)` as its introduction rule and says `ua` is the inverse of `idtoeqv`.
4. Its equivalence discussion explicitly requires a map from `isEquiv(f)` to a quasi-inverse and chooses a well behaved equivalence notion for that purpose.

Therefore, for the source variant at issue, the candidate action

```text
e : A ≃ B  ⟼  ua(e) : A = B
```

is an interface-provided direction of the univalence rule. This audit does **not** run a proof assistant or prove a new HoTT theorem; it only determines how the frozen source answers the candidate question.

## 4. P1 verdict and why it matters

| Gate | Verdict | Reason |
|---|---|---|
| `P-DISCOVERY` | `MODEL_RECALL_SITE_CANDIDATE` | The agent produced one bounded, source-packet-based candidate without answer leakage. |
| `D-L5` | `PASS` | `Q?` names a native equivalence-use/formation task. |
| source validation | `P1_L6_TRIVIAL_CONTROL` | The exact inverse direction is supplied by the stated univalence interface; the task is not an unpaid obligation. |
| `L2b/L2c/L7` | `NOT_EVALUATED_AS_A_COMMON_Q` | The thin discovery packet does not furnish a frozen actual consumer with C/I/O/Done, and no positive completion obligation is established. |
| P2 / P3 | `UNKNOWN / NOT_TRIGGERED` | A trivial P1 Q cannot be handed forward as a common task. |
| HoTT replay release | `BLOCKED` | No source-grounded P1/P2/P3 same-task convergence or reidentification of the existing HoTT Q occurred. |

The correct label is **not** `D_L5_FAILED`. D-L5 did the work it was designed to do: it excluded the meta-level universe-index question from H-004. The next gate then did its own work by preventing a rule-provided inverse from being misreported as a nontrivial completion tension.

## 5. Delta SelfAuditCard

| Field | Record |
|---|---|
| Original units | C11/C14: a one-pass test must produce a meaningful line before source validation; C17: preserve the original computation/formation tension rather than accepting a syntactic substitute; O10/O13/O16 in the full origin audit. |
| Actual action | One permitted D-L5 regression retry on the same thin packet, followed by Master source validation. |
| Alignment verdict | `ALIGNED_WITH_CALIBRATION`: the discovery stage produced an actual native task, and validation immediately checked whether it was already paid by the theory. |
| Deviation class | `EXPECTED_CALIBRATION_FAILURE`, not `ORIGINAL_IDEA_CHALLENGED`. The fixed packet found a native task but not a nontrivial one. |
| Tool impact | D-L6 is added as a discovery-stage direct-payment screen; it predicts only packet-visible direct answers and does not replace validation L6. P2/P3 remain unchanged and no P4 is created. |
| Falsifier | A source-grounded HOTT candidate that meets D-L5 and remains nontrivial under L6/L7 would change this particular control; a repeat of the same thin packet is prohibited. |
| Next trigger | A separately justified, richer no-answer-leak HoTT source packet must be frozen before another discovery run. It must not expose the existing project answer. |

## 6. Scope boundary

This artifact establishes a bounded finding about the P-DAG method and the named source presentation. It does not establish a defect, inconsistency, nontermination result, UR, or mathematical theorem about HoTT. It also does not release the ZFC gate.

## 7. Follow-up specification receipt

The resulting D-L6 specification is recorded in [`20261002-P-DAG-DL6-DISCOVERY-DIRECT-PAYMENT-SPEC.md`](20261002-P-DAG-DL6-DISCOVERY-DIRECT-PAYMENT-SPEC.md). It changes the next discovery contract, rather than reinterpreting H-005 after the fact: H-005 remains an admissible D-L5 candidate under the prior contract and the regression input for the new direct-payment screen.
