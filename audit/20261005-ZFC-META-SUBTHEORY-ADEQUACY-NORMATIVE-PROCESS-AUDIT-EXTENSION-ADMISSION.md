# `ZFC+Q_norm` 过程完成审计扩展：既有机器证明的准入与边界

> **身份：** `NORMATIVE_EXTENSION_ADMISSION / MACHINE_PROOF_REUSE_AUDIT / NOT_A_BARE_ZFC_THEOREM`。
>
> **用户规范来源：** [ZFC 元理论—子理论—时间与完成桥原文](../sources/prompts/Codex-ZFC元理论子理论时间与完成桥-用户原文-20261003.md)。

## 1. 显式规范对象

用户提出的不是简单“ZFC没有时间”，而是一项 MetaTheory 规范：若 M 被当作支撑 S 的基础性框架，M 应能够检查 S 对过程任务 Q 的边界，尤其是 `FormalDone → OriginDone` 是否真的成立，或者 Q 是否被改写。

本卡将它明确称为外加规范：

```text
Q_norm / ProcessCompletionAudit:
  对每个 P : FormalDone → "Q solved"，
  要么支付 input/operation/observation/OriginDone bridge，
  要么输出 ExplicitTaskSwitch / BridgeRequired，
  不得以 coarse resolved view 直接给出 OriginalResolved。

ZFC+Q_norm = bare-ZFC foundational role + this explicit audit norm.
```

这一定义尊重 C0R3/F-C 的来源裁决：`Q_norm` 不是当前 bare ZFC 的公理，不是数学共同体已采纳的 ZFC semantics。

## 2. 既有控制核与新增专用规范包

| 规范义务 | 已有形式资产 | 最新重放 | 实际证明的内容 |
|---|---|---|---|
| coarse `resolved` 不能冒充 original Done | C-364 / `MP-BARE-ZFC-Q-PRECISION-001` | run `…-03`, exact replay PASS | 同一 coarse view 的两个 world 可有相反 `OriginDone`；rich contract/code view可恢复。 |
| revised completion不自动支付 strict completion | C-362 / `MP-ZFC-ACTUAL-Q-SOURCE-CONTRACT-001` | run `…-01`, exact replay PASS | strict last-action contract 与 revised all-actions contract分离；无 bridge。 |
| 若一个 use-model压制Q观察、接受P、再有同一Q的HoTT B，矛盾如何出现 | C-359 / `MP-ZFC-ACTUAL-Q-POLICY-001` | run `…-07`, exact replay PASS | `QMissing ∧ SameFullQ ∧ P ∧ B → False`，并证明缺 Q 不会凭逻辑自动生成 P。 |
| 连续极限并不等于有限自然阶段到终点 | C-361 / `MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001` | run `…-08`, exact replay PASS | 具体 geometric sequence 的 limit 与 finite stage endpoint分离；闭连续时间 endpoint正控制保留。 |
| `Q_norm` 自身应怎样作审计判词 | C-370–C-374 / `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001` | `20261005-MP-ZFC-NORMATIVE-PROCESS-AUDIT-001-02`, Lean core exact replay PASS，Lean binary digest已入manifest | paid bridge 才给 `originalResolved`；explicit task switch只能给`revisedResolved`；missing bridge给`bridgeRequired`；后二者不能静默成为原任务完成。 |

既有 C-359/C-361/C-362/C-364 仍分别给出 promotion、bridge、coarse-observation和positive-control；新的 C-370–C-374 不重做它们，而是把研究发起人的 `Q_norm` 本身固定成一个可消费的 Lean core audit interface。这样，后续工作不必再把“应当审查 bridge”留在自然语言里，也不能误把该 interface 的存在倒写成 bare ZFC 已经具备它。

专用 package 的 source-to-spec、run、环境 pin 与 pipeline repair 由[package 审计](20261005-ZFC-META-SUBTHEORY-ADEQUACY-NORMATIVE-PROCESS-AUDIT-PACKAGE.md)拥有。

## 3. 此 extension 真正能说明什么

在现有 source-bound data 下，`ZFC+Q_norm` 会对 IEP/Norton fixed strict-Q contract 给出：

```text
FormalDone / revised resolution present
strict OriginDone bridge not paid
⇒ audit verdict = ExplicitTaskSwitch or BridgeRequired
```

这与 C5C/C0R3 的来源分类一致。它不宣布 Standard Solution 的 revised task无效；它拒绝把 revised task写成未说明的 strict original resolution。

若未来存在付费 bridge，C-364 的 rich-view positive control说明：`Q_norm` 可以接受带有足够 contract data的模型，而不是机械反对 continuum、limit或ZFC。

## 4. 此 extension 不能说明什么

```text
not: bare ZFC itself already contains Q_norm
not: bare ZFC is inconsistent because Q_norm is absent
not: IEP/Norton source actually adopted ZFCOneUse / MathematicalIllusionP
not: H0 and Zeno have SameFullQ
not: physical time is discrete or classical analysis is false
```

特别是 C-359 的 `False` 需要 `SameFullQ`、具体 P 适用和 HoTT B 的跨核对应；当前 C5/C0 source audit没有支付这些前提。因而它是用户 A/B 推理的完整**条件性**机器化，不是实际 bare-ZFC contradiction。

## 5. 准入判词

```text
USER_NORMATIVE_PROCESS_COMPLETION_AUDIT_MACHINE_PROVED_WITH_SCOPE
DEDICATED_Q_NORM_INTERFACE_C370_C374_VERSION_CLOSED_PENDING_GIT_COMMIT
ACTUAL_BARE_ZFC_INSTANTIATION_STILL_UNPAID
CORE_C6_REMAINS_NOT_RELEASED
```

这次准入审计最大化利用了已有的真实 kernel runs，同时防止两个相反错误：

1. 因为 bare ZFC source不含 Q_norm，就声称没有任何可形式化结果；
2. 因为已有控制的 Lean theorem，就声称 Q_norm 已是 bare ZFC 的现成规则。

## 6. 后继

接下来的工作分成两条不可互相替代的线：

- **bare-ZFC evidence line：**继续寻找 actual M/S/Q/P/Adequacy source chain，才可能改变 C6；
- **normative-extension line：**`MP-ZFC-NORMATIVE-PROCESS-AUDIT-001` 已完成其最小明确合同和 kernel run；它可在未来扩展到具体模型／来源消费，但始终保留“extension”身份。它不替代 bare-ZFC evidence line，也不会释放 C6。

当前核心 SOP 继续走第一条；第二条已获得可重放的逻辑核，等待用户决定是否将其提升为独立研究对象。

## 7. 运行链修复与版本边界

第一次专用 capture（`…-01`）已经通过 Lean core，但通用
`capture_lean_proof_run.py` 当时只把 Lean executable 写进 `environment.txt`，没有把二进制摘要写进
`source-manifest.json`。proof-version verifier 因此正确拒绝其 version closure；该 receipt保留为
`PIPELINE_RECEIPT_SUPERSEDED_NOT_VERSION_CLOSED`，不作为本 package 的主证据。

捕获器随后补上 `external_dependencies = [lean-core-binary]`。`…-02` 已据此重新捕获、索引、冻结与
exact rerun；之后本审计文件本身补入专用 package 链接，使得 `…-02` 的 source-manifest 有意失效。
它保留为 `SOURCE_MANIFEST_SUPERSEDED_BY_DOCUMENTATION_CHANGE`，不被事后改写。最终的 `…-03` 固定了
已完成的 source-to-spec 文档、Lean binary、proof source和工具链，并成为 registry primary run。整个
修复序列只加强证明工具和环境的可审计绑定，不改变任何 Lean 命题、source classification 或 bare-ZFC 结论。
