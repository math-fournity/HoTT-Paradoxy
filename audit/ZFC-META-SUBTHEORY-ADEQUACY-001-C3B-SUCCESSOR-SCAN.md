# C3B 后继扫描：逐字段审计 Standard Solution 的 bridge

> **身份：** `SUCCESSOR_SCAN / CORE_GOAL_ACTIVE / NOT_A_COMPLETION_RECORD`。
>
> **前叶：** [C3B application promotion](ZFC-META-SUBTHEORY-ADEQUACY-001-C3B-IEP-APPLICATION-PROMOTION-AUDIT.md)。
>
> **结果：** `C3B_LOCAL_LEAF_CLOSED / C4A_SELECTED / FINAL_CORE_VERDICT_NOT_PROVED`。

## 1. 为什么 C4 现已被释放

现在有一份来源实际提出的 application P，也有 C2B 固定的 mathematical model proxy。未付问题不再是“是否存在 P”，而是 P 是否完成了 SOP 001 所列四种保真：

```text
input / operation / observation / completion.
```

Norton strict/revised 和 C-361 discrete/closed-time controls必须同时存在，防止我们把 bridge缺失说成“连续模型无端点”或把一份不同任务的成功说成本 Q已完成。

## 2. 后继比较

| 后继 | 改变的核心字段 | 裁决 |
|---|---|---|
| `C4A`：IEP Standard Solution BridgePaymentCard | 具体 `BridgePaid` / explicit task switch / missing bridge。 | **已选**。 |
| `C5A`：ApplicationAdequacy formal contract | needs bridge verdict to avoid abstract norm. | 等 C4A。 |
| `C0B2` | independent formalization. | 保留为 C4A 比较 control，不抢当前 actual P。 |
| `C0E` | defense source. | Norton already mandatory control；C4A检查是否有同任务 defense。 |

## 3. 自动选择：`C4A-IEP-STANDARD-SOLUTION-BRIDGE-PAYMENT`

它必须建立一张四字段 bridge table，并分别记录：

1. `BridgePaid_model`：在数学 model内 endpoint是否真被到达；
2. `BridgePaid_physical`：source 是否给 target mapping，而非只作 application assertion；
3. `BridgePaid_strict`：strict last-action reading是否被支付或被明确改写；
4. `Control+`：closed real-time endpoint；`Control−`：Norton strict/revised；不得用任一边代替另一个。
