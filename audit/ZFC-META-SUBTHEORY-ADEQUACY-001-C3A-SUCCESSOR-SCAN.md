# C3A 后继扫描：扩大 S 的连续模型，还是直接寻找 foundation adequacy？

> **身份：** `SUCCESSOR_SCAN / CORE_GOAL_ACTIVE / NOT_A_COMPLETION_RECORD`。
>
> **前叶：** [C3A promotion audit](ZFC-META-SUBTHEORY-ADEQUACY-001-C3A-IEP-MIZAR-PROMOTION-AUDIT.md)。
>
> **结果：** `C3A_LOCAL_LEAF_CLOSED / C0B1_SELECTED / FINAL_CORE_VERDICT_NOT_PROVED`。

## 1. 现有链在哪里断开

```text
TG-founded Mizar M → SERIES_1 S → series FormalDone
                                  ├─→ Done_math (paid)
                                  └─→ physical OriginDone (unpaid)
```

这说明继续让同一个 `SERIES_1` 去承担 runner/path/time 并不会补桥，只会制造 surrogate-interface drift。下一步必须改变 **S 的实际覆盖** 或寻找一个来源明确承担 bridge/adequacy，而不是重复同一 series theorem。

## 2. 可选后继与裁决

| 后继 | 判别价值 | 最小行动 | 裁决 |
|---|---|---|---|
| `C0B1`：MML 连续运动子理论 inventory | 可检验 TG/MML 是否已有 version-fixed real-function / continuity / derivative / trajectory fragment，因而能让 S 真正覆盖 IEP 的 physical-model字段，而非仅级数。 | 只读官方 MML current source，锁定最多三个相连 article/theorem identities，列出输入、连续性、导数、路径的实际覆盖与缺口。 | **已选**：它直接检验 C3A 的最强 model-coverage falsifier。 |
| `C0C1`：foundation adequacy source | 可规定 M 是否需要检查 bridge。 | 寻找 set-theoretic foundation/interpretation source 的实际 fidelity responsibility。 | 保留：若 C0B1 仍不产生 physical S，C0C1 与 C0B2 比较优先。 |
| `C4A` | 可审计 bridge payment。 | 需要 exact P 和 full Q。 | 未释放：C3A 未支付这两个字段。 |
| `C0B2`：Isabelle/ZF / 其他 formalization | 提供独立 M→S model family。 | 只有 C0B1 无连续-model ingress 或模型不匹配时再启动。 | parked。 |
| `C0E` | defense/policy source。 | Norton 已是同层 control。 | 已嵌入 C3A；不重复。 |

## 3. 自动选择：`C0B1-MIZAR-CONTINUOUS-MODEL-INVENTORY`

它不是“再找一个库”。它只回答一个可否证问题：**C1A 的同一 TG/MML 分母中，是否存在一个能表示 IEP 所列 continuous path / time / speed / derivative 的连续模型 subtheory；若有，它是否仍没有 bridge？**

成功只会扩大可审计 S，不会自动支付 P/Bridge/Adequacy；失败只关闭 Mizar 的 richer-S route，并强制转 C0C1 或 C0B2。
