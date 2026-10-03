# HMZ-001：覆盖收据

## 冻结分母计数

| 类别 | Included items | relevant locators read | 未完成必须追踪 |
|---|---:|---:|---:|
| A. HoTT／UF primary motives | 5 | 5 | 0（本 run 的对应 Z 映射均已有 disposition） |
| B. technical realization | 2 个来源角色 | 2 | 0 |
| C. ZFC／集合论 source | 3（Metamath, Shulman, Isabelle/ZF） | 3 | 0（后续新分母可扩展，但不属于本 run） |
| D. actual consumer | 3（Mumford, Shulman, Isabelle/ZF） | 3 | 0：本分母为 explicit payment / no-hit。 |
| E. comparison / counterexample | 6 个来源角色 | 6 | 0（在本轮已由 Book compatibility、Awodey 与 Shulman/NBG 分支覆盖）。 |
| **合计** | **10 unique `HMZ-S` sources** | **10** | **0 within frozen denominator** |

## R/Z/Q 覆盖

| 项目 | 本轮数量 | 处置 |
|---|---:|---|
| R-Cards | 6 | 全部有精确 source locator 与“不主张什么”字段。 |
| Z-Cards | 7 | `Z-006` 给出 ZFC class/meta-language 的精确边界与 NBG支付；`Z-007` 给出实际 ZF formalization payment；其余边界保持。 |
| Q-Cards | 5 | 0 个候选种子；2 个 `Q-R REJECTED_WITH_SCOPE`；其余未资格化。 |
| C+ / C− | 1 对 | Mumford 的 automorphism-free positive control 与 explicit maps defense。 |
| H0 transport | 1 | `TRANSPORT_UNDER_SPECIFIED`；T0–T5 没有被填满。 |

## 来源终态

| Source ID | 当前终态 | remainder / reason |
|---|---|---|
| `HMZ-S-001` | `READ_RELEVANT_LOCATORS` | 整本书不等于已读；本轮锁定的 locators 已覆盖。 |
| `HMZ-S-002` | `READ_RELEVANT_LOCATORS` | 需同其它原典一起核其 ZFC 指向。 |
| `HMZ-S-003` | `READ_RELEVANT_LOCATORS` | `HMZ-MF-001` 需由非 Voevodsky 自我陈述的理论层来源支付。 |
| `HMZ-S-004` | `READ_VIA_WEB` | 官方 HTML 的本地复制受 403 阻断；URL、日期和可见内容已存档为 access fact。 |
| `HMZ-S-005` | `READ_RELEVANT_LOCATORS` | 仅作 pre-UF comparison，不承担 ZFC 诊断。 |
| `HMZ-S-006` | `READ_RELEVANT_LOCATORS` | 支持当期表述，不替代 Voevodsky 个体动机。 |
| `HMZ-S-007` | `READ_RELEVANT_LOCATORS` | 固定为 `PROOF_FORMALIZATION_ONLY`；未补理论语义与消费者。 |
| `HMZ-S-009` | `READ_RELEVANT_LOCATORS / VISUAL_SOURCE_CHECKED` | 是强反控制，未发现其同一任务里的 unpaid consumer。 |
| `HMZ-S-010` | `READ_RELEVANT_LOCATORS` | `HMZ-MF-001` 的具体 large-class/predicate-language部分已处理；2-theory同一对象仍无。 |
| `HMZ-S-011` | `READ_RELEVANT_LOCATORS` | `HMZ-MF-003` 的实际ZF formalization/payment部分已处理；无未付交付consumer。 |

## 本轮 completion verdict

```text
R_EXTRACTION_FOR_FROZEN_PRIMARY_CORPUS = COMPLETE_WITH_SCOPE
Z_RECONSTRUCTION = COMPLETE_WITH_SCOPE / TWO_SOURCE_PAYMENTS / ONE_REPRESENTATION_BOUNDARY
Q_QUALIFICATION = NO_CANDIDATE_SEED
MUST_FOLLOW_REMAINDER = 0_WITHIN_FROZEN_DENOMINATOR
DENOMINATOR_COMPLETE_WITH_SCOPE = REACHED
```

本轮外的 successor 入口不是“继续搜更多同类口号”，而是：

1. 新的 HoTT/UF 作者原典明确提出与 R-STRUCT/R-HIGHER 不同的 ZFC 任务；
2. 新的 ZFC-side consumer 在同一 Done 下确实未支付 mapping/choice/formation；
3. 新一手来源将 Power Set 与某一 R 连接成相同 `u/F/C/I/O/Done`；或
4. 新来源让 `H0 → Z0` 的 T0–T5 有真实正向输入。

只有这类新证据才创建 successor 或重新考虑 Q/P-DAG。
