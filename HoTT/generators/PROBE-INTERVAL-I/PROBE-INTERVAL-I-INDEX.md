# PROBE-INTERVAL-I 设计探针索引

> 本索引是**设计探针单元索引**，不是数学结论索引，不是生成器族索引，也不是缺口闭合单元索引。
> 本单元 `registers_new_claim: false`，**不进入** `HoTT/CLAIM_EVIDENCE_MATRIX.md`。
> 唯一登记的有界负结论 = 「Bool 观察器形态的分离在真实区间 I 上结构性不可写」，
> 作用域 = Cubical Agda 2.8.0 + cubical v0.9 的消去子/宇宙/sort 结构。

## 索引行

| unit_id | 类型 | 探针对象 | 引擎 runs | 核结论 | 判词 |
|---|---|---|---|---|---|
| `PROBE-INTERVAL-I` | 设计探针单元（语言片段探针） | 真实区间 I 上可写的分离形态 | `PROBE-INTERVAL-I-FORMS`（exit 0，ACCEPT）、`PROBE-INTERVAL-I-BOOL-DISC`（exit 42，REJECT `[SplitError.NotADatatype]`）、`PROBE-INTERVAL-I-EQ-ATTEMPT`（exit 42，REJECT `[UnequalSorts]`） | 可写 = 类型族+PathP / cofibration 条件层；不可写 = Bool 观察器层（c1 等式类型不可成型、c2 端点模式匹配被拒） | `INTERVAL_I_SEPARATION_FORMS_FAMILY_AND_COFIBRATION_BOOL_OBSERVER_UNWRITABLE` |

## 证据定位

- 验收报告（判词语义 + EXP-001 收尾 + 与缺口 A/GEN-001 关系 + 未闭合项）：
  `PROBE-INTERVAL-I-REPORT.md`
- 引擎内完整收据：`/Volumes/D/HoTT-machine-overview/machine-overview/runs/`
  （分支 `feat/machine-overview-m1`，commit `36d27e0`；三个 run 目录各含
  RUN.json + stdout.txt + stderr.txt + environment.txt + command.json +
  source-manifest.json，退出码/sha256/时长全部登记）
- 探针源码：`machine-overview/formal/IntervalIForms.agda` /
  `IntervalIBoolDiscriminator.agda` / `IntervalIEqualityAttempt.agda`（同提交）

## 与缺口 A 的关系

- 缺口 A 的 **DM3 分支已闭合**（revision 168，判词
  `DM3_DE_MORGAN_CONFIRMED_NON_BOOLEAN_LIFT`，`boolean_law_needed=false` kernel-confirmed）。
- 本探针处理**区间 I 分支**，结论 = 「Bool 形态结构性不可写且替代形态改变分离定义」
  → 按 STATE revision 168 指引**登记有界负结论并转下一单元**。
- `interval_i_confirmed = false` 继续保持：V2-DM3 的 availability / level / density
  见证**仍不得**作为关于区间 I 的结论证据。

## 与 GEN-001 / 下一单元的关系

- 本单元**不是** GEN-001 验收单元，不扩大 GEN-001 分母。
- 下一单元（经 020 审计分片 008 裁决，本探针不改变该裁决）：**SUPPLY-010
  知识谱反观 + 现实对齐断裂供给单元**（F2 缺口层 7 条）。

## 禁止外推

- 不声称任何分离在真实区间 I 上成立（本探针只刻画表达界限与可写形态）。
- 不声称「Bool 观察器不可写」对其他工具链/未来版本成立（作用域已固定）。
- 不声称本探针穷尽 I 上一切可写形态（第三形态问题开放，登记 unknown ingress）。
- 不声称任何 pending-audit 前提的非现实判定成立。
- 不声称引擎具备自主发现能力（探针模块由 AI 设计与冻结供给，003 §5 角色纪律）。
