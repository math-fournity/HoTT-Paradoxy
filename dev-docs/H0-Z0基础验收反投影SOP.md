# H0-Z0-FOUNDATION-ADEQUACY-SOP：从 main HoTT H0 反投影 ZFC 的基础验收

> **身份：** TASK_SCOPED_H0_Z0_BACKPROJECTION / F050 / RESEARCH_PROFILE_GOVERNED / NOT_A_PREDECLARED_ZFC_INCONSISTENCY。
>
> **稳定引用名：** H0-Z0-FOUNDATION-ADEQUACY-SOP。
>
> **状态：** SOURCE_VALIDATION_COMPONENT / H0_FIXED / DISCOVERY_ORDER_OWNED_BY_H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP。

> **路由更新（2026-10-04）：** 本文继续拥有来源、理论变体、`H0Map`、`C_accept`和`AdequacyLift`的验证合同；它不再决定 Z0 的发现顺序。发现必须先通过[H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP](H0-Z0模式P优先收敛SOP.md)的 A/B 同一政策门。MPIM／一般模型论文在该门之前仅是 parked controls。

## 1. 为什么 C-364 不是终点

F-049 的 C-364 已完成一项必要校准：一个 ZFC-supported Standard Solution 的粗完成接口可以丢掉 OriginDone，rich contract view 可以恢复它。这个结果说明怎样描述 Q，却不把 main HoTT 的实际 B 放进 ZFC 的基础验收链。

研究发起人的结构是：

    A = 芝诺侧标准解法来源接受的 revised completion／“已解决”
    B = main 中 fixed H0 的 `never`／无有限 halt witness 程序性质
    Q = 基础验收对时间化过程完成的缺失观察力
    P = 在 Q 缺失下允许的 completion / adequacy promotion

没有 H0，研究只会停在芝诺侧的 application contract。H0 使 B 变成一个已有形式证据的、可被 ZFC 元理论验收过程检验的对象。H0 的 UR／现实不合理读法仍是研究发起人的解释桥，不能被这段来源合同改写成内核定理。

## 2. H0：必须固定的 main HoTT 现象

H0 不是泛指“HoTT 很复杂”，而是下列固定程序与命题：

| 字段 | 固定内容 |
|---|---|
| T_H | Cubical Agda 2.8.0 + cubical 0.9 的固定 Q 包；包含 univalence、h-level、相关 HIT 依赖和 delay 运行语义。 |
| u_H | Type ell-zero。 |
| F_H | QuestioningDelay：逐层询问目录中的相同是否在某个 h-level 落定。 |
| FormalH0 | 对任意 Judge，宇宙上的 question 等于 never；任何有限 fuel 都没有答案，且不存在 finite halt witness。 |
| Done_H0 | 程序交出某个有限 h-level 的 now k。 |
| H0 controls | Nat、Bool 和有 h-level 上界的目录会停；集合截断的粗 Q 会在第一步停；固定粗完成不能反射为原 Q 的有限完成。 |
| interpretation boundary | main 的 UR／现实不合理判定是研究发起人的判定和解释桥，不是 kernel 对现实任务的定理。 |

权威资产为 main 的 CLAIMS.md，及 dev 的 QuestioningDelay、C-77 至 C-83、C-357、C-358 和相应 run。

## 3. Z0：不是“再造一个集合版 H0”

Z0 的候选不是任意一个集合论中的无穷过程。它是一个实际基础验收事件：

    ZFC 或明确的 ZFC 扩展／模型元理论
      -> 对一个理论 T 的模型、一致性、基础资格或 adequacy claim
      -> 是否把 H0 的过程完成性质列入观察、保存或明确排除

必须冻结：

| 字段 | 含义 |
|---|---|
| T_meta | 精确的 set-theoretic theory，包含所有额外假设。 |
| T_sub | 来源明确处理的 HoTT／Cubical 演算，而不是笼统“HoTT”。 |
| C_accept | 实际发出 model、relative-consistency、foundational adequacy 或应用充分性判词的来源消费者。 |
| I/O/Done_meta | 它接收什么规则、交出什么模型／一致性／foundation verdict、何时算完成。 |
| H0Map | main H0 的理论构造、主体、程序、观察和 Done 在 T_sub／模型中的逐字段对应，或明确缺失。 |
| AdequacyLift | 来源是否从 Done_meta 升格到“该理论可以作为基础”或“足以回答同一过程”以及其 payment。 |
| QObservation | H0 被保留、被观察、被明确排除、理论变体不匹配，还是无支付地被忽略。 |

Z0 的正确问题是：

> 一个宣称基础资格或充分性的 ZFC-side acceptance contract，是否必须在作出这项判词前观察 main H0 的完成性质？若不必，它的来源给出的理由、范围和 payment 是什么？

## 4. 不能混用的模型来源

| 来源族 | 已知用途 | 当前不能替代什么 |
|---|---|---|
| Kapulkin–Lumsdaine–Voevodsky 单纯集模型 | 给特定 Martin-Löf type theory 加一个 univalent universe 的模型和相对一致性范围；强度涉及 ZFC 加两个不可达基数。 | 不等于 fixed Cubical Agda Q 的同理论变体。 |
| CCHM cubical type theory / cubical set model | 提供计算性 univalence 的 cubical 语义路线。 | 尚未证明覆盖 main H0 的完整 library、Delay、HIT 和 h-level package，也未自动给 foundation adequacy claim。 |
| Cubical Agda 论文与实现文档 | 说明 native computational univalence 和 HIT 支持。 | 实现支持不等于 ZFC-side semantic model 或基础充分性判词。 |
| HoTT Book 的 foundations 话语 | 是 foundation／adequacy source 的候选入口。 | 泛称“HoTT 可作基础”不等于它覆盖 H0 或支付过程 bridge。 |

任何 source 只能按它声明的 theory variant 与验收层使用。KLV 与 H083 先前产生的 exact-variant gap 保持为正控制，不得被“都是 HoTT”抹去。

## 5. 分阶段工作

### HZ0-0：H0Fingerprint

固定 main H0 的完整 T/u/F/I/O/Done、依赖、已证明命题、解释边界和 controls。不能用“HoTT 的问题”四字替代 H0。

### HZ0-1：ModelVariantMatrix

对每份候选 source 建一个逐字段 matrix：

    univalence / universe / HIT / h-level / Delay / exact Q term /
    operational reduction / model theorem / extra axioms

可能判词为 SAME_VARIANT_CANDIDATE、PARTIAL_VARIANT_CONTROL 或 VARIANT_GAP。

### HZ0-2：AcceptanceContract

冻结实际 C_accept、I、O、Done_meta。只构造模型或证明相对一致性，而没有 adequacy lift 的来源，判为 MODEL_DONE_ONLY；它不是 ZFC Q。

### HZ0-3：H0Map 与 QObservation

来源必须给出 H0 的逐字段 map，或者明确不能给出。三种合法结果：

| 结果 | 含义 |
|---|---|
| H0_Q_PRESERVED_WITH_SCOPE | 来源模型／验收明确保留或处理 H0；该来源是防御。 |
| H0_Z0_VARIANT_GAP_WITH_SCOPE | source 不覆盖 exact H0；不得把缺口写成看不见。 |
| H0_Z0_UNPAID_ADEQUACY_LIFT_CANDIDATE | 同一来源把 Done_meta 升格为基础／过程充分性，却没有支付 H0 的观察／保持 bridge。 |

### HZ0-4：机器化

只有 HZ0-3 出现保真 H0Map 后，才创建新的 proof package。它必须证明来源定义的 map 是否保持 never、halt witness、粗完成反射或明确的 observation invariant。

既有 C-357、C-358、C-364 是控制库，不能直接重命名为 Z0 证明。

### HZ0-5：来源级复核 A/B

Pattern-First 发现阶段已经以 A/B 同一政策门筛掉单端对象；本组件只在某候选通过该门、且 H0 到 Z0 的 acceptance contract 固定之后，复核来源是否真的把芝诺 A、exact HoTT B 与 Q/P 放进同一政策。C-359 仍只提供显式前提下的逻辑 consequence；不得先假定 SameFullQ。

## 6. P-DAG 和来源纪律

第一个 source node 只能是 PINNED_PRIMARY_SOURCE 或 PRIMARY_WEB_SOURCE 的版本核对，不做盲态“猜 ZFC 有什么问题”。它必须输出 Claims、Evidence、Conflicts、Unknowns、Mutations、Verification 及 E0 到 E7 MatchTrace。

只有 H0Fingerprint、ModelVariantMatrix 和 AcceptanceContract 均冻结后，才允许 Terra/Max source-match node 处理 H0Map。若使用 App Server，按现有 P-DAG 的 exact Terra/max、read-only、isolated-home、trajectory policy 执行。

## 7. 完成、停止与重开

| 判词 | 条件 | 允许结论 |
|---|---|---|
| H0_Z0_VARIANT_GAP_WITH_SCOPE | 没有同理论变体／保真 translation。 | 该来源不能评判 main H0。 |
| H0_Q_PRESERVED_WITH_SCOPE | 来源以明确 map 或 theorem 保留 H0 的 relevant observation。 | 该来源对 Q 有防御，不能支撑 ZFC 缺陷。 |
| H0_Z0_UNPAID_ADEQUACY_LIFT_CANDIDATE | 同一来源有 adequacy lift，却没有 H0 observation/payment。 | 获得 ZFC Q 的来源级候选，进入 P1/P3 与机器化。 |
| H0_Z0_ACTUAL_POLICY_CONFLICT_WITH_SCOPE | 同一真实 acceptance policy 同时容纳 A 与 B，且 Q/P/bridge 已逐字段支付。 | 才可重新调用 C-359 的实际实例化。 |
| SOURCE_ACCEPTANCE_UNDERDETERMINED_WITH_SCOPE | 只有模型／一致性结论，无 adequacy lift。 | 停止该 source，不将其写成 ZFC Q。 |

重开只由新的一手来源、精确理论变体的保真 translation，或研究发起人对 H0/OriginDone 的修正触发。不得以更多普通 Zeno 文献、更多 generic factorization fixture 或“ZFC 无时间 primitive”重开。

## 8. 作为来源验证组件调用

    按照 SOP=H0-Z0-FOUNDATION-ADEQUACY-SOP，对已通过 A/B 同一政策门的 Z0 候选执行来源验证。

当前第一调用入口是`H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP`。只有它产生`AProjection + BProjection + SameQBridge`候选后，本组件才冻结 H0 fingerprint、exact variant、AcceptanceContract与来源分母。它不自动启动新的 proof、worker、tag、push或发布。
