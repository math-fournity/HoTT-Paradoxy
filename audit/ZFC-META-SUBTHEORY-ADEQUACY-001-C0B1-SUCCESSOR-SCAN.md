# C0B1 后继扫描：把 IEP 的连续模型对齐到 `S_rich`

> **身份：** `SUCCESSOR_SCAN / CORE_GOAL_ACTIVE / NOT_A_COMPLETION_RECORD`。
>
> **前叶：** [C0B1 rich-S inventory](ZFC-META-SUBTHEORY-ADEQUACY-001-C0B1-MIZAR-CONTINUOUS-MODEL-INVENTORY.md)。
>
> **结果：** `C0B1_LOCAL_LEAF_CLOSED / C2B_SELECTED / FINAL_CORE_VERDICT_NOT_PROVED`。

## 1. 为什么下一个不是 C4

与 C3A 的 `SERIES_1` 不同，`S_rich` 现在在数学对象层覆盖 IEP 所用的 real parameter、trajectory-type function、continuity 和 derivative。仍要先审计：这种对应是否保留了 IEP 的输入、允许操作与观察，还是只把关键字段换了名称。没有 C2B 的 fidelity table，C4 的 bridge 将没有确定的两端。

## 2. 候选比较

| 后继 | 是否可能改变 C0–C6 | 裁决 |
|---|---|---|
| `C2B`：IEP continuous model ↔ MML `S_rich` | 是：可形成第一个包含 path/time/speed math fields 的 `Q_math-model / FormalDone` contract，或指出 model mismatch。 | **已选**。 |
| `C0C1`：foundation adequacy sources | 是：可给 M responsibility。 | 保留，等 C2B 固定 S/Q。 |
| `C0B2`：独立 ZF/ZFC library | 是：可提供反证或更直接 bare ZFC M。 | 若 C2B mismatch或P仍无实际载体，升为下一候选。 |
| `C4A` | 有，但必须在 P 固定之后。 | 不释放。 |

## 3. 自动选择：`C2B-IEP-MIZAR-CONTINUOUS-MODEL-QCONTRACT`

它必须同时给：

1. IEP `time / position / continuity / derivative` 字段到 MML source fields 的 source-to-spec table；
2. IEP physical-language 与 MML mathematical-language 的明确分界；
3. `DifferentTaskControl`：仅有 real-valued function definition 不蕴含 physical process completion；
4. 不预设 P、Bridge、Adequacy。

若 C2B 只得到表面词汇相同，就判 `MODEL_MISMATCH` 并转 C0C1/C0B2；若它能固定 math-model contract，则 C3B 再审计 actual promotion。
