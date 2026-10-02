# P-DAG-DL6：发现阶段的直接偿付筛查规格

> **身份：** `P1_DISCOVERY_SPEC_REFINEMENT / HOTT_DISCOVERY_005_DERIVED / NOT_A_THEORY_RESULT`。
>
> **问题：** H-005 已通过 D-L5，把候选从 universe-index 元层问题推进到原生 HoTT 等价使用任务；但它仍允许一个由同一规则直接答复的动作进入候选队列，直到来源验证时才被 P1 L6 拒绝。

## 1. 触发证据

H-005 的 public trace 给出：

```text
F = univalence(A,B) : isEquiv(idtoeqv_{A,B})
Q? = from e : A ≃ B, form p : A = B by the inverse direction.
```

The fixed Book source then presents the same interface as:

```text
ua : (A ≃ B) → (A = B)
ua is the inverse of idtoeqv.
```

So the native-task condition was met, but the requested action was already paid by the very interface selected as `F`. This is a distinct failure mode from H-004's `DISCOVERY_META_LAYER_CAPTURE`.

## 2. New discovery rule: D-L6 / direct-payment screen

Before a blind discovery node may emit `MODEL_RECALL_SITE_CANDIDATE`, it must ask:

```text
Does the packet-visible F, by its stated constructor, eliminator, equivalence,
inverse, computation rule, or supplied witness, already deliver a direct answer
to the proposed native task Q? on the same stated input?
```

If yes, its terminal discovery verdict is:

```text
DISCOVERY_DIRECT_RULE_ANSWER
```

and it must show the shortest public `F → answer(Q?)` route. The node is a control, not a candidate for source tracing, P2/P3 mapping, Battle, HoTT replay release, or ZFC relevance.

If the answer is not visible from the frozen packet, discovery may still output a candidate. The later source-validation `L6/Q-friction` remains mandatory, because D-L6 cannot inspect hidden definitions, a wider theory variant, or an external consumer contract.

## 3. Delta SelfAuditCard

| Field | Record |
|---|---|
| Original units | C11/C14 demand a one-pass *line* rather than a generic or already settled reply; C17 requires the original computation/formation tension to remain explicit; O10/O13/O16 retain these constraints in the full origin audit. |
| Actual action | Master compared H-005's D-L5-native task with the fixed source answer after it was rejected by validation L6. |
| Alignment verdict | `IDEA_SPEC_INCOMPLETE → REPAIRED`: D-L5 separated native tasks from meta questions, but the discovery contract still did not screen rule-provided answers. |
| Repair | Add D-L6 as a discovery-stage prediction of L6. It is not a new blade and does not replace source validation. |
| Affected tools | P1 discovery, DiscoveryTrace D0–D5, P-DAG scheduler and the HOTT replay release card. P2 and P3 do not gain or lose any mapping criterion. |
| Regression oracle | H-005 must now be classified `DISCOVERY_DIRECT_RULE_ANSWER` from its own F/Q? description; H-004 remains `DISCOVERY_META_LAYER_CAPTURE`. |
| Falsifier | If a D-L6 compliant discovery candidate later proves its answer was already explicit in the packet, D-L6 was underspecified; if D-L6 rejects a task only answerable after a separate consumer/guard, it is overbroad. |

## 4. Boundary

This refinement only prevents an obvious discovery-stage false positive. It says nothing about HoTT consistency, the existing HoTT research result, ZFC, or a general claim about model capability.

## 5. D-L6b / bounded alternate-site continuation

HOTT-DISCOVERY-006 passed D-L6 but showed that a direct-answer screen can become an early-stop sink: the response discarded univalence correctly, then stopped although the broad profile contained other foundation interfaces. D-L6b is therefore a **selection-protocol** refinement, not another theory condition:

```text
If a first obvious site fails D-L5 or D-L6, record it as a rejected control and
inspect at most two further obvious foundational sites in the same blind response.
Return exactly one eligible MODEL_RECALL_SITE_CANDIDATE if one remains; otherwise
return NO_MODEL_RECALL_CANDIDATE / DIRECT_PAYMENT_ONLY after the bounded scan.
```

The bound of three total sites preserves the user's one-pass heuristic: it is one response with a small, explicit alternative set, not a traversal of theory X or its derived details. Each rejected site must still state its short reason. A direct-answer screen is terminal only when no eligible site remains within that bound.

The new regression oracle is H-006: univalence should appear as a rejected D-L6 control, while the worker must then consider a non-identical foundational alternative or explicitly establish that the bounded profile has none.
