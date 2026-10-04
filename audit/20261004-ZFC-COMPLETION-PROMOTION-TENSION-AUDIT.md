# ZFC completion-promotion tension：形式化与机器证据审计

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / KERNEL_ACCEPTED_WITH_SCOPE / POLICY_SEMANTIC_REFINEMENT / NOT_A_ZFC_OBJECT_LANGUAGE_THEOREM`。
>
> **证明包：** `MP-ZFC-COMPLETION-PROMOTION-TENSION-001`。

## 1. 这次形式化回答的精确问题

用户提出的“数学幻觉 P”不能被写成“极限对象不存在”或“ZFC 证明了假命题”。本包把 P 定义为一种更准确的、可审计的推理行为：

```text
formal completion
    ── P：未经单独支付的 promotion rule ──> origin-process completion
```

`A` 是一个固定过程状态的 formal-completion judgment；`B` 是同一状态的 origin process 尚未完成；`Q` 是能够从 meta observation 审查 origin Done 的能力。这里的“未经支付”不是 Lean 中的神秘谓词，而是一个严格区分：**P 是政策可导性；CompletionBridge 才是使 P 在过程语义上健全的事实。**

该区分直接解释“数学幻觉”的含义：如果一个政策能从 A 推导“原过程完成”，但同一状态保留 B，则它产生的是不健全的 completion judgment。它不是由此就推出 `ZFC ⊢ False`。

## 2. 形式资产

| 资产 | 作用 |
|---|---|
| `HoTT/formal/zfc-observation-boundary/CompletionPromotionTension.lean` | 正向 Lean 4 core 形式化。 |
| `…/WrongCompletionPromotionTension.lean` | 刻意声明“coarse fixture 上 P 仍健全”的错误负控制。 |
| `…/CompletionPromotionTension-CLAIM.md` | 命题范围、符号映射、正负控制与非目标。 |
| `…/capture_completion_promotion_tension.py` | 临时编译依赖 `.olean`、正负运行、不可覆盖 receipt 和 source manifest。 |
| `HoTT/verification/runs/20261004-MP-ZFC-COMPLETION-PROMOTION-TENSION-001-02/` | 当前正向 kernel receipt。 |
| `HoTT/verification/runs/20261004-MP-ZFC-COMPLETION-PROMOTION-TENSION-NEG-001-02/` | 当前预期拒绝的负向 receipt。 |

## 3. 机器检查的逻辑链

### 3.1 P 不是 bridge

`PAdopted policy` 只说明政策允许 `Derives.promote`。它并未把
`formalDone → originDone` 写入定义。相反，
`sound_adopted_P_pays_completion_bridge` 由内核证明：**若**一个采用 P 的政策在过程语义上健全，**则**它必须给出该 statewise bridge。

这把“支付 bridge”从一句解释变成了明确的证明义务。P 的采纳、bridge 的真值、来源是否实际支付 bridge，分别是三件不同的事情。

### 3.2 A 与 B 使用同一状态

在 `coarseSubtheory.task` 的 `TwoState.unresolved`：

- `coarse_unresolved_has_formal_resolution_A`：formal Done 成立；
- `coarse_unresolved_has_origin_countertrace_B`：origin Done 不成立；
- `promoted_policy_derives_origin_completion_at_countertrace`：采用 P 后，政策仍能推出 origin-complete judgment；
- `P_A_B_fixture_breaks_policy_soundness`：因此政策相对于该过程语义不健全。

这不是把两个不同案例硬说成同一个 Q；A 与 B 都明确落在同一个 `unresolved` 状态上。

### 3.3 Q 缺失不自动推出 P

`coarse_fixture_lacks_Q_observation_capacity` 证明 coarse meta observation 无法审查 origin Done。可是
`Q_missing_alone_does_not_entail_P_adoption` 同时证明：相同的 Q-missing fixture 可采用 `guardedPolicy`，而该政策根本不采纳 P。

所以用户提出的“Q 缺失让 P 被允许”在实际研究中仍须通过来源给出 `absence → permission → adoption` 的中间链；它不能从“观察不足”本身偷渡出来。这与 `CommunityObservationPolicy.CommunityAdoption` 的字段分解严格一致。

### 3.4 正控制

`promoted_policy_is_sound_when_bridge_is_paid` 和 `paid_fixture_has_completion_bridge` 在 `paidSubtheory` 上通过。这里 formal Done 与 origin Done 恰好同值，因而同一 promotion rule 是健全的。它排除了“任何形式化完成都是数学幻觉”的误读。

## 4. 运行证据

| run | 结论 | 关键事实 |
|---|---|---|
| `…TENSION-001-01` | `KERNEL_REJECTED`，历史保留 | 初版把 `import MetaSubtheoryAudit` 放在 module doc comment 后；Lean 拒绝 import placement。负向同轮因正依赖未构建而是 import failure，不能作数学负控制。 |
| `…TENSION-001-02` | `KERNEL_ACCEPTED_WITH_SCOPE` | Lean 4.34.1 exit 0；14 个导出定理均显示 `does not depend on any axioms`。 |
| `…TENSION-NEG-001-02` | `KERNEL_REJECTED`，预期命中 | Lean 在 `unresolved` 分支拒绝 `PolicySound promotedPolicy coarseSubtheory.task`；diagnostic 是 `Tactic \`assumption\` failed`，receipt 的 `outcome_matches_expectation=true`。 |

The first pair is deliberately retained because it distinguishes an implementation-preparation error from a mathematical rejection. The `-02` pair is the only current evidence for this package.

## 5. 已证明与未证明的边界

### 已由 Lean 内核验证的条件性结论

```text
P adopted + policy soundness
    ⇒ semantic CompletionBridge

same state: A(formal Done) + B(not origin Done) + P promotion
    ⇒ policy not sound

Q missing alone
    ↛ P adopted

bridge paid
    ⇒ same promotion rule can be sound
```

### 仍待来源、任务和现实对应核查的内容

- actual ZFC 是否缺少一项可定义的 Q；
- 数学共同体是否实际采纳 P；
- 极限理论对芝诺或圆环的某一具体宣称是否实例化 A；
- main 分支 HoTT 过程是否是同一过程上的 B；
- P 是否在实际来源中违反计算/现实 bridge；
- A 与 B 在某一个实际形式系统中是否不相容。

因此，本包将“矛盾”定位为**已构造政策的语义不健全性**。只有有了实际来源所承诺的 A/B 同一过程、以及满足适当不相容条件的映射，才有资格进一步讨论任何对象层 `False`。

## 6. 与路线级文献回流的关系

本包与 `20261004-P-FORGE-LITERATURE-BACKFLOW-HOTT-MOTIVE-ZFC-CANDIDATE-AUDIT.md` 是相互约束的两半：

1. 形式包给出“若 P 被采纳，它怎样需要 bridge、何时变得不健全”的精确语义结构；
2. 文献回流说明现有候选资料还没有给出同层同任务的 P adoption、P→B provenance 或未支付 bridge；它尤其阻止把 totality、Power Set、model、program 或 universe 词汇直接填进这份结构。

因此当前最强的交付不是“已证明 ZFC 矛盾”，而是一个更窄也更可靠的研究收束：**P 已经从比喻变成可检验的 completion-promotion policy；实际 ZFC 的 P/Q 实例仍需同一任务、consumer 和 source payment 的证据。**
