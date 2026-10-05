# ZFC MSS 时间消去：定义域恢复与无定义域观察边界控制

> **package ID：** `MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001`
> **claim IDs：** `C-375`、`C-376`
> **状态：** `FORMAL_SOURCE_MOTIVATED_CONTROL / NOT_A_BARE_ZFC_VERDICT`。

## 研究对象

Sant'Anna 与 Bueno 在其 ZFC 中的 MSS classical particle mechanics 表述里，把
`T` 解释为从原点计量的 elapsed time real-number set；`s`、`f`、`g` 的定义域
依赖 `T`。他们据此报告 `Time is eliminable in a MSS system`：在该
set-theoretic function conception 下，`T` 可以由这些函数的 domain 定义。
原文随后把 MSS 改写到 domainless function theory `N`，同时明确说该 N-MSS
system **not exactly equivalent** to ZFC MSS，因为 N 中 functions do not have
domains。

这给出一个比“ZFC 缺少时间”精确得多的判别问题：

```text
省去时间这个独立 primitive 名称
  是否仍保留能够恢复 time carrier 的 data？
若不保留，某个具体 temporal observation 是否因此不再由该表示决定？
```

## 固定的 Lean 规格

本包刻意只使用 Lean 4.34.1 core 和 `Nat`，不宣称它是 MSS、ZFC 或 N 的完整形式化。

| 表示 | 固定数据 | 用于本包的 endpoint observation |
|---|---|---|
| `GraphTrace` | `graph : Time → State → Prop`，外加 `domain_is_time : (∃ state, graph t state) ↔ time t` | `endpoint ∈ time` |
| `graphOnly` | 删除单独的 `time` field，保留图 | `∃ state, graph endpoint state` |
| `DomainlessCandidate` | `time` 与 total `function : Time → State` 分列，仅投影 function | `endpoint ∈ time` |

`Determines project observe` 的含义是：存在只看 `project` 的 decoder，对每个
输入恰好给出 `observe`。

## 机器检查的命题

- **C-375：**在 `domain_is_time` 的明确假设下，`graphOnly` 仍决定
  `EndpointAvailable`；也就是说，去掉显式 `time` field 但保留 graph-domain 后，
  endpoint membership 可恢复。
- **C-376：**对于固定的 `shortCandidate`（time `{0}`）和 `longCandidate`
  （time `{0,1}`），二者有同一 `sharedFunction`，但 `1` 是否属于 time 不同。因此
  function-only projection 不能在全域决定这一 endpoint observation。

所有陈述都在源码末尾通过 `#print axioms` 报告；目标定理在此 core-only 文件中
不依赖额外公理。

## 来源与对应边界

一手来源固定为 Sant'Anna--Bueno 2014 的本地 snapshot：

- PDF p.16 / printed p.272：ZFC MSS、`T` 的 elapsed-time 解释、`s/f/g` 的
  time-indexed domain；
- PDF p.17 / printed p.273：Theorem 8 及 `T` 由 domain 恢复的说明；
- PDF p.18 / printed p.274：N-MSS 与 ZFC MSS 不完全等价，明确归因于
  domainless functions。

Lean 不能证明论文的历史文本，也不重放 Theorem 8。它只检查上述来源解释所要求的
两个最小表示控制的逻辑结果。

## 这对 C0 的作用

本包是 `C0R8` 的 **P capability calibration / anti-false-positive control**：

```text
ZFC graph/domain presentation
  -> 对本包固定的 endpoint observation 有 recoverable decoder
  -> 不支持“ZFC 一旦消去 time primitive 就必然失去时间观察”的推断。

domainless function projection
  -> 存在同 function、不同 endpoint-membership 的 pair
  -> 说明真正需要审查的是具体 projection 是否丢掉 domain/time data，
     而不是把 primitive eliminability 本身写成 Q。
```

它不支付 `M / S / Q / FormalDone / OriginDone / P / Bridge / Adequacy` 的
actual core contract；不裁定 physical motion、Zeno、圆环、HoTT、N-MSS 的完整
语义或 bare ZFC 的理论充分性。
