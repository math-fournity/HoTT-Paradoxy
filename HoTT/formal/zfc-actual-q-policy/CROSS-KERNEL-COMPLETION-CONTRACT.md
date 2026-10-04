# C-362 / C-363：完成合同的跨证明器对应表

> **身份：** `CROSS_KERNEL_SCHEMA_CORRESPONDENCE / NOT_A_SAME_FULL_Q_PROOF`。

## 1. 共同 schema

两个 kernel 分别证明了下列抽象形状的一个实例：

```text
CompletionGap =
  RevisedDone 有 witness
  ∧ OriginalDone 没有 witness
  ∧ ¬ (RevisedDone → OriginalDone)
```

| schema 槽位 | C-362：Zeno 来源合同 / Lean | C-363：固定 HoTT Q / Cubical Agda | 对应状态 |
|---|---|---|---|
| `RevisedDone` | 对每个自然数编号的动作都完成 | 截断问题在 stage one 返回 `just 1` | `FORMAL_CHECKED_IN_OWN_KERNEL` |
| `OriginalDone` | 有一个覆盖所有自然数动作的最后动作 | 原 universe 问题有一个有限 halt witness | `FORMAL_CHECKED_FALSE_IN_OWN_KERNEL` |
| `¬ bridge` | revised completion 不能推出 strict last-action completion | coarse completion 不能推出 original finite halting | `FORMAL_CHECKED_IN_OWN_KERNEL` |
| 来源／现实解释 | Norton/IEP 的严格／缩减 completion 区分 | 用户对 HoTT Q 的 UR / 完成解释 | `SOURCE_OR_USER_INTERPRETATION` |

## 2. 允许的结论

机器检查允许的结论是：**两个固定实例都展示“较弱或修订完成不能自动反射为较强原完成”的合同结构。**

这足以把 `ResolutionByRevision` 作为可审的 P 候选，并解释为什么 C-360 是 A2 的相关反控制。

## 3. 禁止的跨越

下列命题尚未被证明，不能由这张表推出：

1. Zeno 的每个动作与 HoTT 的每层 h-level 问题是相同 State／Op；
2. 两个 `OriginalDone` 是同一现实任务；
3. IEP/Norton 的 ZFC-supported standard solution 政策也适用于 HoTT；
4. 一条 proof assistant 中的 theorem 可被另一条 kernel 自动使用；
5. `CompletionGap` schema 相同就是 `SameFullQ`。

因此 `B_bridge` 当前状态是 `SHAPE_MATCH_ESTABLISHED / SAME_FULL_Q_UNPAID`。这张表缩小了未知，不伪造跨理论或跨 kernel 的等同。
