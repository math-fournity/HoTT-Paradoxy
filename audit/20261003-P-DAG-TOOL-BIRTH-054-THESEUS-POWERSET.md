# Tool-BirthCard：忒修斯之船、历史身份与 Power Set

> **身份：** `TOOL_BIRTH_RESEARCH_OPEN / DERIVED_TOOL_HYPOTHESIS / NOT_A_POWERSET_OR_ZFC_DEFECT_CLAIM`。

## 1. 候选花纹

设有限部件宇宙为 `U`。一个替换历史是按阶段改变当前部件集合的 trace：

```text
h : stage → current component subset of U
snapshot(h,n) ⊆ U
```

两条历史可以有相同当前 snapshot，却在“逐件替换形成的连续对象”与“将已经移除的部件重新组装”的 provenance 上不同。忒修斯任务不是询问两个集合是否有相同成员，而是一个给定 consumer 是否应把它们判为**同一持续对象**。

Power Set 的候选作用只是提供所有当前 snapshots 的 extensional state space：`snapshot(h,n) ∈ 𝒫(U)`。它不天然保存 `h`，也不天然声称历史身份。故本卡不把“所有 snapshots 同时可列出”当作缺陷。

## 2. 用户来源与边界

当前研究发起人明确提出“忒修斯之船能否用于进攻 Power Set”。历史用户原文的可定位前驱是：

- `AI对话录/用户发言逐句审计账本-20260911.md` 的 `G-12-S115`：“当前状态相同，不等于生成历史相同”；
- `G-12-S118`：结构同一性、复制、逆操作或组合是否承担原任务中的历史与消耗条件；
- `G-12-S108`：不能用“历史信息丢失”替换圆环原本的复原过程问题。

第三点是本卡的硬边界：Thisues 花纹不能借圆环的名字或一般信息丢失获得资格。它需要自己固定 identity consumer、过程、观察和 Done。

## 3. P1/P2/P3 容纳尝试

| 刀具 | 尝试映射 | 保留的内容 | 当前缺口或扭曲 |
|---|---|---|---|
| P1 | `u=𝒫(U)` 或其中的 snapshot；`F`为当前部件配置形成；`C`为身份连续性判断任务。 | 能定位 state space 和要求 identity 的 consumer。 | bare Power Set 没有这个 consumer；若把 membership/equality直接写成 consumer，会换题。 |
| P2 | `history h → snapshot(h)` 是表示／quotient-like bridge；extensional equality把同 snapshot 的 histories压成同一表示。 | 能写 representation collapse。 | 现有 P2 的核心是同一对象的 Bind/Form/Reenter/Polarity，不专门记录多条 trace 到同 snapshot 的 many-to-one collapse，也不含 provenance observer。 |
| P3 | 替换阶段、部件可用性、连续 replacement 和 Done 可成为状态过程。 | 能记录演化与完成。 | 现有 P3 的核心问“未获资格者是否已被算符使用”，不直接判两个已完成 traces 的 diachronic identity。 |

当前初判不是 `UNCONTAINED_PATTERN_CANDIDATE`。最可能的结构是一个 `DERIVED_TOOL_CANDIDATE`：P2 提供 trace→snapshot 的表示／等同塌缩，P3 提供 trace 与完成，另加一个不可省略的 identity/provenance observer。是否需要独立新刀，取决于这个 observer 能否由 P2×P3 的显式派生 operator 忠实表示。

## 4. Distortion witness

若强行只用 P2，则 `h₁`、`h₂` 在同一 snapshot 后失去可比较的过程；若强行只用 P3，则它们只是两条完成轨迹，缺少为什么 consumer 对“是否同一”有不同答案的观察关系；若只用 P1，则得到一个裸集合／成员问题，丢失替换历史。

最小 distortion witness：

```text
h_gradual  : original artifact undergoes one-by-one replacement
h_rebuild   : removed parts are reassembled
snapshot(h_gradual, final) = snapshot(h_rebuild, final)
identity-observer(h_gradual, h_rebuild) may still require different answers
```

若 observer 不存在，或任务接受 snapshot equality 作为完整答案，则不存在攻击；若 observer 必须区分而理论只允许 snapshot equality 进入判断，才出现同一任务压力。

## 5. 控制与验证计划

| 控制 | 目的 | 预期作用域 |
|---|---|---|
| H054 脱敏 replacement-history blind card | 检查模型是否在不见“忒修斯”“Power Set”名称时定位 trace/snapshot/identity consumer。 | 只验证 pattern recognition。 |
| history-carrying negative control | 把状态编码为 `(snapshot, history)`；若 consumer 可区分，则证明缺口在 erasure 而非集合论表达能力。 | 排除“集合永远不能表达历史”。 |
| actual Power Set source card | 核对 `𝒫(U)` / extensional equality 是否真被一个 source-defined consumer 当作历史身份的完整代理。 | 没有此卡不升级为ZFC Q。 |
| P2×P3 derived-operator card | 固定 `Trace → Snapshot → Equality/Observer → Done`，比较是否可由已有刀具无扭曲表示。 | 决定派生工具或新刀。 |

## 6. 当前裁定与反证条件

```text
verdict: TOOL_BIRTH_RESEARCH_OPEN
provisional containment: DERIVED_TOOL_CANDIDATE or NOT_ENOUGH_EVIDENCE
new numbered tool: NOT PROPOSED
Power Set attack: NOT LOCATED
```

反证当前派生假设的任一事实：

1. P2×P3 能在不新增独立判断职责的情况下完整表示 trace、snapshot、identity observer 与 Done；则它是旧刀字段／派生合同；
2. 某个真实 consumer 确实以 extensional snapshot 作历史身份的充分代理，且同一任务显示原任务条件丢失；则它成为强候选；
3. 所有自然 consumer 都显式携带 history 或只问 snapshot equality；则 Power Set 路线在该范围内无攻击。
