# C-369：来源认证的 ApplicationAdequacy contract 内核结论

> **proof ID：** `MP-ZFC-META-SUBTHEORY-ADEQUACY-001`
> **claim ID：** `C-369`
> **状态：** `FORMAL_CHECKED_WITH_SCOPE / SOURCE_CERTIFIED_APPLICATION_ADEQUACY_CONTRACT`。
> **primary run：** `20261005-MP-ZFC-META-SUBTHEORY-ADEQUACY-001-04`（Lean 4.34.1 core；九条 selected theorem 的 axiom report 均为空）。

## 精确形式命题

在 Lean 的 `ApplicationCase` 中：

```text
applicationClaim ∧ claimsOriginalResolution ∧ requiresBridge
∧ ¬ bridgePaid ∧ ¬ explicitTaskSwitch
→ ApplicationAdequacyFailure.
```

另有四个内核控制：paid bridge、explicit task switch、model-only case、以及未付 `SameQ_H0` 时 H0 不可进入核心前提。

## source-to-spec fidelity table

| 来源字段 | Lean 字段 | 本地保真义务 |
|---|---|---|
| IEP Standard Solution 的 physical application claim | `applicationClaim` | 来源卡 C3B 认证其在固定文本中存在。 |
| IEP application 的 original-resolution language | `claimsOriginalResolution` | 仅在 C3B 指定 scope；不等于 ZFC object-language theorem。 |
| SEP Scientific Representation 的 application adequacy question | `requiresBridge` | C5A 将其编译为本项目的受限规范前提。 |
| C4A source-to-spec bridge payment 审计 | `bridgePaid` | `False` 是当前来源卡分类，Lean 不读取网页。 |
| Norton explicit task revision | `explicitTaskSwitch` | 只在对应 fixture 中为真；不得自动套到 IEP 所有句子。 |
| H0 SameQ义务 | `H0Admission.sameQ` | 当前 control 设置为 `False`，阻止跨理论偷运。 |

## 允许结论

若正 run 接受，C-369 只证明：固定的、来源认证的 application contract 及其 explicit classification 会得出 `ApplicationAdequacyFailure`；paid bridge、explicit switch和model-only controls不会被同样判为 failure。

## 禁止外推

- 不证明 `ZFC ⊢ False`、ZFC不一致或ZFC无法表示时间；
- 不证明所有数学／物理模型缺 bridge；
- 不把 IEP/Norton 网页真值变成 Lean kernel theorem；
- 不证明 HoTT与芝诺是同一个完整 Q；
- 不完成本 SOP 的全部候选族和总完成门。
