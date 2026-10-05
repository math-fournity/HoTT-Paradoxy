# C6D：actual M/S/Q/P/Bridge/Adequacy 合同的内核判词

> **身份：** `C6_SOURCE_TO_SPEC_FINALIZATION / CORE_ADEQUACY_FAILURE_WITH_SCOPE / NOT_A_BARE_ZFC_OBJECT_LANGUAGE_THEOREM`。
>
> **TaskCard：** [C6D](ZFC-META-SUBTHEORY-ADEQUACY-001-C6D-TASKCARD.md)。
>
> **kernel claim：** `C-369` / `MP-ZFC-META-SUBTHEORY-ADEQUACY-001` / [primary run](../HoTT/verification/runs/20261005-MP-ZFC-META-SUBTHEORY-ADEQUACY-001-04/RUN.json)。
>
> **判词：** `CORE_ADEQUACY_FAILURE_WITH_SCOPE`。

## 1. 最终 source-to-spec table

| core field | actual owner / evidence | C-369 field or control | 支付状态 |
|---|---|---|---|
| `M_actual` | C1D：IEP把ZFC/ZFC-with-Choice作为standard real analysis / Standard Solution的foundation context。 | foundation context of the source card | `SOURCE_SUPPORTED_WITH_SCOPE`。 |
| `S_actual` | C1D/C3C：standard real analysis、calculus、linear continuum。 | model side of `ApplicationCase` | `SOURCE_SUPPORTED_WITH_SCOPE`。 |
| `Q_user` / `OriginDone` | C2C与用户 primary：有限自然数阶段余量精确为零；C-370为离散 control。 | fixed original-target completion policy | `USER_FIXED_RESEARCH_CONTRACT`。 |
| `FormalDone` | C-361的几何极限/closed endpoint controls；IEP continuous model/series language。 | `applicationUnpaid` model completion side | `KERNEL_CONTROL_PLUS_SOURCE_SUPPORTED`。 |
| `P_actual` | C3C：IEP对Standard Solution的Zeno/Achilles/Dichotomy resolution/application language。 | `applicationClaim = true` | `SOURCE_SUPPORTED`。 |
| `claimsOriginalResolution` | C5E：用户将“极限理论声称解决芝诺／圆环”固定为本项目审查对象，IEP仍使用resolution语言。 | `claimsOriginalResolution = true` | `USER_TASK_POLICY + SOURCE_LANGUAGE`。 |
| `BridgePaid` | C4A/C4C：连续model endpoint与C2C finite-stage Done未有source-to-spec completion equivalence；C-371防止本项目偷换。 | `bridgePaid = false` | `SOURCE_TO_SPEC_UNPAID_WITH_SCOPE`，不是数学`¬Bridge`全称。 |
| `explicitTaskSwitch` | C5E：在用户原任务下，IEP一边称resolution一边拒绝其Done，不满足“明确改题且不声称原题已解”的C5A control。 | `explicitTaskSwitch = false` | `USER_TASK_POLICY_ADJUDICATED`；C5D保留另一读法作反控制。 |
| `Adequacy` | C5A：SEP application/representation criterion；C5E user task policy。 | `requiresBridge = true` | `SOURCE_SUPPORTED_APPLICATION_CRITERION + USER_ORIGIN_POLICY`。 |

所有字段都明确自己的证据层。尤其 `Q_user`、original-resolution 与 explicit-switch classification 是本项目研究合同，不是网页或ZFC公理自己会产生的谓词。

## 2. 内核后果

在上表的字段实例化下，C-369的 `applicationUnpaid` 正好具有：

```text
applicationClaim           = true
claimsOriginalResolution   = true
requiresBridge             = true
bridgePaid                 = false
explicitTaskSwitch         = false
```

其 Lean 4.34.1 core theorem `application_unpaid_is_failure` 已经证明：

```text
ApplicationAdequacyFailure applicationUnpaid.
```

所以得到本SOP允许的最终形态：

> **在用户固定的 finite-stage `OriginDone`、固定 IEP ZFC-founded Standard Solution application 与 source-backed application adequacy criterion 下，Standard Solution 的 `FormalDone` 被用于resolution claim，而没有支付把它保持为用户原任务完成的 bridge；该 application/foundation adequacy contract 失败。**

这就是 `CORE_ADEQUACY_FAILURE_WITH_SCOPE` 的完整含义。

## 3. 机器与来源控制

| control | status | 它防止的误读 |
|---|---|---|
| C-369 paid bridge | kernel accepted | 付桥的模型不能被误判failure。 |
| C-369 explicit task switch | kernel accepted | 真正改题且不称原题解决时，不是unannounced failure。 |
| C-369 model-only | kernel accepted | 单有数学端点不足以启动physical application failure。 |
| C-369 negative control | expected Lean rejection | paid case不能伪造failure。 |
| C-361 | verified | continuous limit不蕴含有限自然数endpoint；closed continuous endpoint同时存在。 |
| C-370 | verified | fixed eight-unit process有限完成，防止“离散只是一句口号”。 |
| C-371 | verified | fixed dense/quantized finite-stage Done不能被逐点同一化。 |
| C0D1 / H0 control | source audit + C-369 control | H0未付SameQ，不能被偷运为本判词前提。 |

## 4. 禁止外推

此判词**不**是：

- `ZFC ⊢ False` 或 bare ZFC不一致；
- ZFC不能表示时间、过程、离散模型或量子化运动；
- standard real analysis的数学定理错误；
- 真实时空已由本项目证明离散；
- IEP或数学共同体已经接受用户的 `OriginDone`；
- HoTT H0与芝诺是同一完整 Q。

它是一个更窄但实质性的结论：ZFC作为基础被带进一个实际 Standard Solution application时，若按用户明确保留的过程完成要求审查，它的来源支持的application policy没有支付该要求，而仍把连续模型结果用作resolution。C5D的另一读法说明，这一批判取决于保住用户原任务，不能伪装成不带任务合同的纯对象语言定理。

## 5. 自动后继

**C0R5 已完成。** C0 manifest的冻结候选宇宙、SOP 004的八门、C-369/C-370/C-371的selected proof-version closure、current owners和候选分支的Git记录均已复核。这个结果关闭本冻结合同下的Goal；若用户改写`OriginDone`、接受C5D的revised task，或出现能支付actual bridge／H0 SameQ的新来源，按相应reopen条件重新启动，而不把当前判词外推为bare ZFC对象语言结论。
