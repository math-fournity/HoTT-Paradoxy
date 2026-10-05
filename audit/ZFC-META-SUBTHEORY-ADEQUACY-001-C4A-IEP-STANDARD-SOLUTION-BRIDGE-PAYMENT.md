# C4A：IEP Standard Solution 的 bridge payment card

> **身份：** `C4_BRIDGE_PAYMENT_CARD / MODEL_BRIDGE_PAID / PHYSICAL_BRIDGE_SCOPE_UNPAID`。
>
> **TaskCard：** [C4A](ZFC-META-SUBTHEORY-ADEQUACY-001-C4A-TASKCARD.md)。
>
> **判词：** `BRIDGE_MODEL_PAID / BRIDGE_PHYSICAL_ASSERTED_NOT_SOURCE_TO_SPEC_PAID / BRIDGE_STRICT_EXPLICIT_TASK_REVISION / C4A_LOCAL_LEAF_CLOSED`。

## 1. 四字段审计

| bridge field | 已有来源／形式材料 | payment status | 边界 |
|---|---|---|---|
| input | IEP 把 runner/course、real time和continuum path设为 Standard Solution 的模型输入；C2B 的 MML `τ : [0,1] → ℝ`是数学 proxy。 | `APPLICATION_ASSERTED / FORMAL_PROXY_FIXED` | 无 source-defined mapping把某个 material runner识别为MML function。 |
| operation | IEP说运行路径、finite positive speed；MML有 real function、continuity、derivative predicate。 | `MATHEMATICAL_STRUCTURE_PAID / PHYSICAL_OPERATION_MAP_UNPAID` | “running”不等于evaluate/differentiate一个函数。 |
| observation | IEP使用 time-indexed position / derivative-style speed；MML可给值和导数。 | `MODEL_OBSERVATION_PAID / MEASUREMENT_CORRESPONDENCE_UNPAID` | 没有精确 observation/measurement relation。 |
| completion | C2B的 `τ(1)=1`给 model endpoint；IEP称 physical course/path已完成。 | `MODEL_DONE_PAID / PHYSICAL_DONE_ASSERTED_BUT_BRIDGE_UNPAID` | 来源主张应用结果，没有给出从 formal endpoint到原 physical completion的完整保持证明。 |

这里 `UNPAID` 的语义是“当前版本固定来源未提供 SOP 所定义的 source-to-spec payment”，不是“数学上已证明没有 bridge”，也不是“IEP不得提出模型”。

## 2. 四种强制控制

### `BridgePaidControl`：模型内部 bridge

在 `Q_model` 内部，`τ(1)=1` 与“trajectory reaches its model endpoint”是同一已定义状态。C2B 的 MML identity-function source以及现有 C-361 closed-time endpoint control都支持这一点。它防止把本卡误报成“continuity没有到达”。

### `Control+`：闭连续时间端点

`ZenoLimitControl.lean` 的 `ClosedTime = [0,1]`、`continuousTrajectory(t)=t` 和 `terminalTime=1` 为一个已机器检查的正控制：端点参数可以存在且被取到。它严格只覆盖这个 continuous mathematical model。

### `Control−`：strict/revised completion

Norton 当前文的 strict “including the last action”与 revised “doing all the actions”分开；他明确说删除前者使原不可能性不再推出。对应的 C-362 source-contract control防止将 `P_standard` 偷改为已证明的 strict last-action completion。

### `DifferentTaskControl`：model target 与 physical target

IEP 本身承认 continuous real-analysis account是否真正描述 time/space/concrete reality可争论。SEP Scientific Representation则把数学模型如何适用于 physical target当作独立的 adequacy问题。这说明 `Q_model` 和 `Q_physical` 可以相关，却没有自动成为同一完成合同。

## 3. C4A 结论

```text
FormalDone_model → Done_model           = paid by definition/model witness
FormalDone_model → OriginDone_physical  = asserted by application P, not source-to-spec paid
FormalDone_model → StrictLastActionDone = not paid; Norton uses task revision
```

这正是 C5 需要的输入：不是从一个空白处猜 ZFC 有问题，而是一份实际 application P 加上一份来源支持的 `ApplicationAdequacy` criterion，以及一个可定位的 physical-bridge payment gap。

它还没有给出 final core verdict：C5必须先把 criterion写成精确 contract；C6才可机器检查在该 contract下的逻辑后果和正反控制。
