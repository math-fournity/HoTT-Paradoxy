# C2B4：set.mm `geoihalfsum` 与 dense half-process 的 source-to-spec 保真卡

> **身份：** `C2_SOURCE_TO_SPEC_FIDELITY / Q_MATH_ONLY / NOT_A_CORE_VERDICT`。
>
> **TaskCard：** [C2B4](ZFC-META-SUBTHEORY-ADEQUACY-001-C2B4-TASKCARD.md)。
>
> **固定证据：** `set.mm@160ebb…`的 `df-sum`、`df-seq`、`df-rlim`、`geoihalfsum`，以及 [C1B4 replay](../HoTT/verification/runs/20261005-SOURCE-REPLAY-SETMM-GEO-LIMIT-001/RUN.json)；C-361、C2C与IEP Standard Solution source。
>
> **判词：** `SETMM_Q_MATH_FIDELITY_PARTIAL_WITH_SCOPE / FINITE_STAGE_AND_PHYSICAL_Q_UNPAID / C2B4_LOCAL_LEAF_CLOSED`。

## 1. 对齐表

| C2B4 field | fixed set.mm content | C2C/C-361 counterpart | 支付状态 |
|---|---|---|---|
| term sequence | `geoihalfsum`使用 `1/(2^k)`、`k ∈ NN`。 | C-361 partial sum `s_n = 1-(1/2)^n`；将n个项的index shift为`k=1,…,n`。 | `MATH_SHAPE_ALIGNED`。 |
| partial sums / limit | `df-sum`对upper-integer index sets以partial sums的limit定义无限和；`df-seq`给相应recursive sequence。 | C-361 `FormalA = Tendsto s_n (𝓝 1)`。 | `FORMAL_DONE_INTERPRETATION_ALIGNED_WITH_SCOPE`。 |
| final series value | `geoihalfsum : Σ_{k∈NN}1/2^k=1`，本轮external verifier accepted。 | C-361 limit target `1`。 | `SOURCE_REPLAYED_OBJECT_LEVEL_THEOREM`。 |
| finite-stage nonarrival | 当前 theorem叙述的是无限sum值，不是`∀n, s_n≠1`。 | C-361明确证明 no finite natural-stage endpoint。 | `UNPAID_BY_SETMM_THEOREM / CONTROL_AVAILABLE_ELSEWHERE`。 |
| physical movement / quantized control | source无runner、path、minimum unit、measurement或physical Done。 | IEP physical application、C-370 finite lattice、user premise。 | `UNPAID`。 |

## 2. 这条对齐允许和不允许什么

允许说：一个 version-fixed ZF-side object theory确有与用户半程级数同形的实分析／无穷和资源；这使 `S_setmm` 成为比“proof checker可以验证proof”强得多的数学子理论候选。

不允许说：`geoihalfsum` 单独证明了 IEP physical runner完成，或者它已经对 user/C2C 的finite-stage `OriginDone`作出判断。特别是，`Σ=1`与“某个自然数阶段已经zero”是不同谓词；C-361正是这个差别的单独机器控制。

## 3. 后继

进入 **C3B4：IEP → set.mm actual promotion audit**。尽管当前网页没有`Metamath`字符串，也不能只凭无命中直接写“绝不存在使用”；要明确冻结“IEP page自身没有消费该formalization”的有限 source boundary，并检查是否有同一来源将 `geoihalfsum` 或同一 database theorem提升为 physical Q。若无，则关闭这条 exact P route，返回 C0 选择F-C或新的object-level source ingress。
