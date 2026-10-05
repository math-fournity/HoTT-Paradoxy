# C2B：IEP 连续运动模型与 MML `S_rich` 的 source-to-spec 合同

> **身份：** `C2_SOURCE_TO_SPEC_CARD / MATHEMATICAL_CONTINUOUS_MODEL_FIDELITY / PHYSICAL_Q_UNPAID`。
>
> **TaskCard：** [C2B](ZFC-META-SUBTHEORY-ADEQUACY-001-C2B-TASKCARD.md)。
>
> **判词：** `Q_MODEL_TO_RICH_S_FIDELITY_SUPPORTED_WITH_SCOPE / Q_PHYSICAL_AND_ORIGINDONE_UNPAID / DIFFERENT_TASK_CONTROL_PRESENT / C2B_LOCAL_LEAF_CLOSED`。

## 1. 一个明确的 MML trajectory witness

设数学 trajectory 为

```text
τ : [0,1] → ℝ,     τ(t) = t.
```

这不是新造的 “completion world”：它是当前 MML 已有 real-function machinery 中 `id [0,1]` 的直接 specialization。

| 所需字段 | MML source evidence | 结论 |
|---|---|---|
| time parameter | `PartFunc of REAL,REAL` / `id [0,1]`。 | `SOURCE_SUPPORTED`。 |
| position function | `id Y` 是 real partial function；对 `Y=[0,1]`，它在每个参数返回自身。 | `SOURCE_SUPPORTED`。 |
| continuity | `FCONT_1.miz`（hash `944078445ed5b23b1e17f65d9d0d29495b9400adb7110f5c9512a6028160dc71`）先给 `id Y` Lipschitzian，后给 Lipschitzian→continuous registration。 | `SOURCE_SUPPORTED`，但本机未重放 Mizar checker。 |
| derivative-speed proxy | current [ASYMPT_2](https://mizar.uwb.edu.pl/version/current/html/asympt_2.html) source-local `Lm5` 给 `id REAL` 在每个 real 点可微且 derivative 为 1。 | `SOURCE_SUPPORTED_AS_SOURCE_LOCAL_LEMMA`。 |
| endpoint | `τ(1)=1` 由 identity function 的定义；`1∈[0,1]`是基础实数不等式。 | `PROJECT_SPECIALIZATION_OF_MML_OBJECTS`，未新建 Mizar theorem。 |

MML 也有 `NFCONT_4` / `NCFCONT1` 的 epsilon-delta 和 sequence-limit continuous definitions，以及 `ORDEQ_02` / `INTEGR26` 对 real-domain differential-function 的较一般处理。它们说明上述 witness不是单一边缘记号，而属于一个可展开的 continuous-analysis fragment。

## 2. 与 IEP Standard Solution 的逐字段对应

| IEP model field | MML counterpart | fidelity status | 不能偷加的内容 |
|---|---|---|---|
| real-valued time coordinate | domain `REAL`, then `[0,1]` restriction | `SUPPORTED` | physical time itself。 |
| position as a function of time | `PartFunc REAL,REAL` / `τ` | `SUPPORTED` | a material runner。 |
| continuous path | FCONT_1 continuity / NFCONT_4 | `SUPPORTED` | a physical path actually realized。 |
| finite positive speed | `diff(id REAL,x)=1` source-local lemma | `SUPPORTED_AS_MATHEMATICAL_PROXY` | empirical speed measurement。 |
| endpoint arrival in the model | `τ(1)=1` | `SUPPORTED_AS_SPECIALIZATION` | original process completion。 |
| physical continuum / runner | no MML source field in the selected fragment | `UNPAID` | no claim of absence from all MML or physics。 |
| OriginDone | no MML predicate/source bridge | `UNPAID` | no inference from endpoint equality。 |

因此 C2B 把 C2 的范围从 `Q_math` 扩大为一个包含时间参数、位置函数、连续性、导数和端点的 **mathematical model task**：

```text
Q_model  = construct/evaluate a continuous real trajectory τ on [0,1]
FormalDone_model = τ is continuous ∧ derivative τ = 1 ∧ τ(1)=1
```

这是 IEP 所使用的数学建模语言的保真 fragment；它仍不等于 IEP 所说 actual runner 的 physical Q。

## 3. `DifferentTaskControl`

两个已有控制防止 `Q_model` 被冒充成原过程：

1. `C-361` 在 `ZenoLimitControl.lean` 中对离散 partial sums 与闭实数时间端点分别建模：没有自然数序列的最后端点，并不否定连续时间 `t=1` 的 endpoint arrival。
2. `C-362` 以 Norton 的 strict/revised completion contract 显示：每个动作有时间或 revised completion 成立，仍不自动支付 strict last-action completion。

故 C2B 没有证明“连续模型错误”，也没有证明“连续模型足以给原任务做结”。它只防止两种相反误读：把 discrete-stage failure当作连续 endpoint failure，或把 continuous endpoint equality当作所有过程合同的完成。

## 4. 叶结论

`S_rich` 是第一个能对应 IEP continuous-model数学字段的 version-fixed formal S；`M → S_rich → Q_model/FormalDone_model` 可以进入后续审计。物理解释、P、Bridge 和 Adequacy 仍然未付。

这意味着下一问题已不再是“ZFC 是否能表示时间”或“有无一条连续函数”：它是 **谁实际把这个 mathematical model 的 endpoint outcome 提升为 physical/original completion，以及该提升是否要求 bridge**。由于 Mizar source 并不是 IEP 的 consumer，下一步不再继续扩展 MML，而转入 foundation-adequacy / actual policy source。
