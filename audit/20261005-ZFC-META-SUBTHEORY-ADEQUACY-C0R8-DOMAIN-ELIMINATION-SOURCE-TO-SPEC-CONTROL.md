# C0R8：MSS time eliminability 的来源到规格控制

> **身份：** `SOURCE_TO_SPEC_FIDELITY_CARD / C0R8_P_CAPABILITY_CALIBRATION / NOT_A_BARE_ZFC_VERDICT`。
> **来源：** Sant'Anna--Bueno 2014 本地 primary snapshot；精确文件、哈希和版本见 [source README](../sources/external/zfc-meta-subtheory-c0r8-santanna-bueno-2014-20261005/README.md)。
> **机器包：** `MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001`，claims `C-375`、`C-376`。
> **本卡判词：** `ZFC_DOMAIN_RECOVERY_POSITIVE_CONTROL / DOMAINLESS_PROJECTION_OBSERVATION_LOSS_CONTROL / Q_NOT_LOCATED`。

## 1. 一手来源的三个分层事实

| 原页 | 来源实际说了什么 | 本卡可以使用的范围 |
|---|---|---|
| PDF p.16 / printed p.272 | MSS initially presented in ZFC；`T` 是 elapsed time real-number set；`s/g` 的域为 `P × T`，`f` 的域为 `P × P × T`；position/force 都解释为 at instant `t`。 | 固定 ZFC presentation、时间 carrier 和物理解释。 |
| PDF p.17 / printed p.273 | Theorem 8 说 time eliminable；理由是改变 `T` 会改变 `s/f/g` 的 domain，因此剩余 primitives 不保持不变；并明说 MSS 的 time 可由这些 functions 的 domain 定义。 | “eliminable”是 definability/re-presentation conclusion，且 domain 是恢复路径。 |
| PDF p.18 / printed p.274 | N-MSS “is not exactly equivalent” to ZFC MSS；作者给出的原因是 N functions do not have domains。 | domainless reformulation 是一个不同表示层，不能与 ZFC MSS 偷换。 |

本轮对 p.16--p.18 的原 PDF 渲染逐页视觉核验；衍生 OCR/text 只用于定位。

## 2. M / S / Q / P / Bridge 字段

| 字段 | 冻结内容 | 证据身份 |
|---|---|---|
| `M` | ZFC set-theoretic function/domain conception | source-stated |
| `S` | MSS classical particle-mechanics fragment | source-stated |
| `Q` | `T` 是否是独立 primitive，以及在重述后 endpoint-time membership 能否恢复 | 前半 source-stated；后半是本卡新增的受限 observation control |
| `FormalDone` | `T` 可以不再作为显式 primitive 名称出现 | source-reported theorem/conclusion |
| `P` | `T` 由 `s/f/g` 的 domains 取得，因此改写不显式写 `T` | source-stated promotion/recovery route |
| `Bridge` | 本卡只审查 representation → endpoint observation；没有 physical OriginDone bridge | source plus formal-control boundary |
| `Adequacy` | 无 actual physical completion 或 bare-ZFC duty payment | unpaid |

## 3. Lean 规格如何忠实而受限地对应来源

| 来源结构 | Lean structure | 保真点 | 刻意未做的事情 |
|---|---|---|---|
| ZFC function as graph with a domain | `GraphTrace.graph` + `domain_is_time` | 保留 “domain recovers time carrier” 这项 exact source mechanism | 未编码 real interval、particles、force、derivatives 或 MSS P1--P7。 |
| 表示中不单独列 `T` | `graphOnly` | 删除唯一的独立 `time` field，但 graph 保留 | 不把 field deletion 写成 physical time disappearance。 |
| N has functions without domains and is not exactly equivalent | `DomainlessCandidate` / `functionOnly` | 明确测试若 designated carrier 真被丢掉，endpoint observation 是否仍能恢复 | 不声称它是 full N 或 N-MSS model。 |

## 4. 机器结果

### C-375：ZFC-style domain recovery 是正控制

`graph_only_determines_endpoint` 对每一 endpoint 构造 decoder：

```text
EndpointFromGraph(graph, endpoint)
  := ∃ state, graph(endpoint, state).
```

在 `domain_is_time` 假设下，kernel 证明该 predicate 与
`endpoint ∈ time` 等价。因此，**在这个来源所明说的 ZFC domain mechanism 中，消去 `T` 的单独名称不等于丢失此处固定的时间观察。**

### C-376：真正丢弃 carrier 的 function-only projection 是负控制

Lean 固定两个候选：

```text
short.time = {0}
long.time  = {0,1}
functionOnly(short) = functionOnly(long) = sharedFunction
```

但 endpoint `1` 仅在 `long.time` 中。kernel 因而证明没有全域 decoder 能只看
`FunctionView` 决定 endpoint membership。这是表示精度的反例，不是物理运动结论。

### 运行证据

`HoTT/verification/runs/20261005-MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001/` 保存 Lean 4.34.1 core run；其中七个选择定理的 axiom reports 均为 no axioms。该 run 在本卡写入和全局索引更新后会重放为最终 version-closed receipt；当前 `-001` 仅是初次 kernel receipt。

## 5. 对 Q 的反向结论

这张卡否定的是一个过强、会误报 bare ZFC 的推断：

```text
“time is eliminable as a primitive”
  ⇒ “ZFC no longer has a time/process observation”
```

它没有否定研究发起人的更精确问题：bare ZFC 是否在某个实际的连续统子理论上，未能观察或审查某个
`FormalDone → OriginDone` bridge。这个问题仍需要同一 actual `M/S/Q/P/Bridge/Adequacy` contract。

本轮的可迁移 P 规则因此被收紧为：

```text
先问：理论省去的是 primitive name，还是决定目标 observation 的 carrier／order／boundary data？
只有后者，才可能形成 Q 的表示层入口；
前者必须首先通过 recoverability control。
```

## 6. 不能推出与下一动作

不能推出：

1. bare ZFC 已充分或不充分地处理所有时间维度；
2. N 或 N-MSS 有物理错误；
3. Theorem 8 已被本项目重放；
4. endpoint membership 就是 Zeno、圆环或 HoTT 的完整 `OriginDone`；
5. 存在 ZFC 矛盾、ZFC 缺陷或社区 policy。

下一判别动作不是把 C-376 夸大为 Q，而是检索 da Costa--Sant'Anna 2001/2002 或 N/MSS 的真实 downstream consumer：它必须给出同一物理任务中一个 **无法由保留数据恢复** 的过程、顺序、测量或完成观察。若该 consumer 不存在或能经 domain/data 恢复，则 C0R8 保持为控制并停止这一叶。
