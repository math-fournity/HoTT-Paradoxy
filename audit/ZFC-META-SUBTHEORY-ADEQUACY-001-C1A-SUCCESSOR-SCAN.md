# C1A 后继扫描：从 TG/MML 的 `M → S` 到可判定的核心合同

> **身份：** `SUCCESSOR_SCAN / CORE_GOAL_ACTIVE / NOT_A_COMPLETION_RECORD`。
>
> **前叶：** [C1A Mizar/TG 来源核验](ZFC-META-SUBTHEORY-ADEQUACY-001-C1A-MIZAR-FOUNDATION-TO-SUBTHEORY.md)。
>
> **结果：** `C1A_LOCAL_LEAF_CLOSED / C2A_SELECTED / FINAL_CORE_VERDICT_NOT_PROVED`。

## 1. 叶结论改变了什么

`C1A` 支付了一个版本固定的 `M → S`：Mizar 的 TG 是来源支持的 ZFC-founded extension，MML 的 `SERIES_1` 给出几何级数的形式化子理论。它没有支付：

```text
Mizar theorem ↔ IEP's concrete Standard Solution consumer,
FormalDone → OriginDone,
or an adequacy rule saying why M must reject an unpaid promotion.
```

因此 `C1` 取得一个实际 foundation-to-subtheory leg，但 `actual_core_contracts = 0`、C2–C6 仍未开始。任何把它叫作 final proof、bare ZFC verdict 或“ZFC 已被证明有问题”的说法都会违反 SOP 001–004。

## 2. 仍可改变总判词的候选后继

| 候选 | 能改变什么 | 当前材料 | 最小判别动作 | 为什么不先选／或为何保留 |
|---|---|---|---|---|
| `C2A` **已选**：IEP geometric-series 至 MML `SERIES_1` 的 source-to-spec card | 决定这条 `M/S` 是否能进入一个可审计的 `Q / FormalDone` 合同，或只能留为平行 formalization。 | IEP 当前页第 100–104 行显式说明 `1/2+1/4+…`、partial sums 接近有限值的定义；MML 固定定义／Th22／Th24 已有。 | 做逐字段 `QContract` / `FormalDoneSpec`，并加入 `DifferentTaskControl`。 | 它是目前最短、直接且能把 C1 推进到 C2 的行动；不先另搜更多 library。 |
| `C0B`：第二个 direct ZF/ZFC formalization inventory | 可提供更贴近 bare ZFC 的 M→S，或否定 Mizar 的代表性。 | F-B 仍余下 Isabelle/ZF、其它可执行 libraries。 | 只收集同时具有版本、foundation identity 与具体 limit theorem 的候选。 | 重要但不能替代先测 C1A 是否能接到实际 Q；若 C2A 坏掉，自动升为最高优先。 |
| `C0C/C5`：foundation adequacy literature | 决定 Bridge 是否是 M 的实际责任而非项目偏好。 | SEP 只给表示／foundation 语言；Mizar source给 M→S，不给 adequacy。 | 寻找明确 foundation-to-subtheory semantic fidelity／interpretation statement，并标明是否涉及应用／任务合同。 | 必须做；但先固定当前 S/Q 能使其避免泛泛讨论“基础”。 |
| `C0E/C4`：Norton task-switch control | 可给 core defense，或暴露实际 promotion。 | Norton 已明确 strict/revised divergence。 | 与 C2A 的同一 Q 卡同表比较。 | 是 C2A 的强制负／不同任务控制，不独立替代 C2。 |
| `C0D/H0` | 只有 SameQ_H0 后才改变 core consequence。 | H0 fixed，SameQ 未支付。 | 不启动；保持 control。 | SOP 明确禁止抢跑。 |

## 3. 自动选择：`C2A`

```text
unit_id: C2A-IEP-MIZAR-GEOMETRIC-QCONTRACT
parent: C2
M: Mizar TG / MML 5.94.1493 (C1A fixed)
S: SERIES_1, exact Partial_Sums / summable / Sum / Th22 / Th24 fragment
Q: IEP's geometric-series component of the Dichotomy Standard Solution
FormalDone: IEP partial-sum convergence, translated only where the MML definitions match
OriginDone: keep Norton strict and IEP revised readings separate
P: do not assume; C3 owns its source admission
Bridge: do not assume; C4 owns its payment/task-switch audit
proof target: none before source-to-spec fidelity table is paid
mandatory controls: DifferentTaskControl (strict vs revised), Mizar-not-IEP consumer control
```

**C2A 的最强反证者**是字段比对发现 IEP 的数学对象（连续路径、微积分或 physical continuum）并不能由 `SERIES_1` 的几何级数 fragment 忠实承载。若发生，关闭 C2A 为 `MODEL_MISMATCH`，立刻转 `C0B`，绝不把这个 mismatch 当作 ZFC 的缺陷或本 Goal 的结束。

## 4. 重开与停止边界

`C1A` 只有出现下列新证据时重开：Mizar/TG version、TG 的 ZFC relation、`SERIES_1` source identity 或 IEP/Mizar consumer mapping 被直接反驳或补付。当前主 Goal 不因 C1A 关闭而暂停；下一动作为建立 C2A TaskCard 并对现有一手来源做逐字段 source-to-spec 审计。
