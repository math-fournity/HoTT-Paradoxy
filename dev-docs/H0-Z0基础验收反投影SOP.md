# H0-Z0-FOUNDATION-ADEQUACY-SOP：从 main HoTT H0 反投影 ZFC 的基础验收

> **身份：** TASK_SCOPED_H0_Z0_BACKPROJECTION / F050 / RESEARCH_PROFILE_GOVERNED / NOT_A_PREDECLARED_ZFC_INCONSISTENCY。
>
> **稳定引用名：** H0-Z0-FOUNDATION-ADEQUACY-SOP。
>
> **状态：** CONTRACT_READY / H0_FIXED / Z0_SOURCE_AND_VARIANT_NOT_YET_FROZEN。

## 1. 为什么 C-364 不是终点

F-049 的 C-364 已完成一项必要校准：一个 ZFC-supported Standard Solution 的粗完成接口可以丢掉 OriginDone，rich contract view 可以恢复它。这个结果说明怎样描述 Q，却不把 main HoTT 的实际 B 放进 ZFC 的基础验收链。

研究发起人的结构是：

    A = 芝诺侧被数学共同体接受的“已解决”
    B = main 中 HoTT 的实际不合理现象
    Q = 基础验收对时间化过程完成的缺失观察力
    P = 在 Q 缺失下允许的 completion / adequacy promotion

没有 H0，研究只会停在芝诺侧的 application contract。H0 使 B 变成一个已有形式证据的、可被 ZFC 元理论验收过程检验的对象。

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

### HZ0-5：再接回 A/B

只有 H0 到 Z0 的 acceptance contract 固定之后，才重新检验芝诺 A、HoTT B 与 Q/P 是否为同一政策。C-359 仍只提供显式前提下的逻辑 consequence；不得先假定 SameFullQ。

## 6. P-DAG 和来源纪律

第一个 source node 只能是 PINNED_PRIMARY_SOURCE 或 PRIMARY_WEB_SOURCE 的版本核对，不做盲态“猜 ZFC 有什么问题”。它必须输出 Claims、Evidence、Conflicts、Unknowns、Mutations、Verification 及 E0 到 E7 MatchTrace。

只有 H0Fingerprint、ModelVariantMatrix 和 AcceptanceContract 均冻结后，才允许 Terra/Max source-match node 处理 H0Map。若使用 App Server，按现有 P-DAG 的 exact Terra/max、read-only、isolated-home、trajectory policy 执行。

### 6.1 发现态优先与来源支线的停止合同（2026-10-04）

模型的既有数学知识和模式 P 负责**先发现**：从 fixed H0 出发，在不注入特定论文、模型名字或既有答案的条件下，定位 ZFC 的显眼基础承诺，构造 Z0／Q 候选。这个阶段的交付是可反驳的候选卡，不是来源事实或数学结论。

来源工作只在候选已经指向实际`C_accept`，或验证一个明确的`H0Map`确有直接必要时启动。它必须说明本节点将改变哪一项主线判断：`T_sub` identity、`C_accept`、`Done_meta`、`H0Map`、`AdequacyLift`或`QObservation`。只有“又发现一个 cubical model”或“讲座提到 proof translation”而不改变其中任一字段，判为`REPEATED_SOURCE_BRANCH_NO_MAINLINE_DELTA`，停止该支线。

MPIM／AWCCRS 类节点的正确身份是条件性控制：它们防止把不同 model family 误拼成一个 H0→Z0 合同。已经取得`SOURCE_CHAIN_SPLIT_NO_H0MAP_OR_ADEQUACY_LIFT`后，后续命名或 variant 阅读只有在实际`C_accept`引用该来源、或它是已冻结 H0Map 的最短验证路径时才恢复。

用户修正来源优先级、靶点、停止条件或成功定义时，先执行：

    用户原件 / rulings
      -> Feature 的 active / parked / next action
      -> MEMORY 当前队列
      -> direction 与本 SOP
      -> 回读所有改动 owner
      -> 才继续任何依赖该判断的节点

并发 writer 占用 Feature/MEMORY/direction 时，不把“稍后会改”当作已经更新：先冻结 user source 与 rulings，记录旧节点为`STALE_PENDING_PRIORITY_REALIGNMENT`；节点终态后由 canonical integrator 在同一语义事务中更新其余 owner。该合同的目的不是增加文档，而是阻止失效的下一动作继续驱动来源搜索。

### 6.2 `P-FIRST-Z0-DISCOVERY`：下一实际 TaskCard

此卡是 H0→Z0 的发现态，不是关于 ZFC 的已证结论，也不输入 MPIM、AWCCRS、论文题名、现有 model verdict 或既有 ZFC 答案。

| 字段 | 冻结内容 |
|---|---|
| `T` | ZFC 作为待审基础理论；当前目标是定位一个显眼基础承诺，不预设任何公理已经有问题。 |
| `H0` | fixed Cubical Agda `QuestioningDelay`：宇宙上的 finite completion question 等于 `never`，连同其正控制与解释边界。 |
| `P` | 罗素计算—存在—自指模式：形成／可用／完成尚未支付时，理论是否已经交出对象、算符或完成判词。 |
| `forbidden visible answer` | Power Set、累积层级、模型语义、MPIM、AWCCRS、KLV、CCHM、任何既有 ZFC Q 报告均不得作为任务包中的指定靶点。 |
| `required output` | 1–3 张 `Z0CandidateCard`：理论承诺、理论收益、被改变的过程条件、`u/F/Q/I/O/Done`、与 H0 的关系、同一任务反控制、何种实际`C_accept`或原典才能证伪／支持它。 |
| `negative control` | 至少一张“看似相像但只涉及模型／编码／局部无限过程、不能承接 H0→Z0”的排除卡，防止将任意集合论无穷过程报成 Z0。 |
| success | 发现一个可审、可被来源或反控制推翻的显眼承诺位置；成功不等于已经找到 ZFC Q。 |
| stop | 若只得到泛泛的“ZFC 忽略时间”或只复述已知模型线索，登记`P_FIRST_NO_CONCRETE_Z0_SITE`，换核心承诺或锻造 P，不以继续文献搜索填充。 |

Master 对每一张候选必须先判：它是否是 ZFC 的核心基础承诺；H0 的固定过程为什么使该承诺的形成／完成政策成为问题；没有哪个来源事实时不得把候选升级为实际`C_accept`。只有通过这三项，才可建立来源验证或 Terra/Max source-match NodeCard。

## 7. 完成、停止与重开

| 判词 | 条件 | 允许结论 |
|---|---|---|
| H0_Z0_VARIANT_GAP_WITH_SCOPE | 没有同理论变体／保真 translation。 | 该来源不能评判 main H0。 |
| H0_Q_PRESERVED_WITH_SCOPE | 来源以明确 map 或 theorem 保留 H0 的 relevant observation。 | 该来源对 Q 有防御，不能支撑 ZFC 缺陷。 |
| H0_Z0_UNPAID_ADEQUACY_LIFT_CANDIDATE | 同一来源有 adequacy lift，却没有 H0 observation/payment。 | 获得 ZFC Q 的来源级候选，进入 P1/P3 与机器化。 |
| H0_Z0_ACTUAL_POLICY_CONFLICT_WITH_SCOPE | 同一真实 acceptance policy 同时容纳 A 与 B，且 Q/P/bridge 已逐字段支付。 | 才可重新调用 C-359 的实际实例化。 |
| SOURCE_ACCEPTANCE_UNDERDETERMINED_WITH_SCOPE | 只有模型／一致性结论，无 adequacy lift。 | 停止该 source，不将其写成 ZFC Q。 |

重开只由新的一手来源、精确理论变体的保真 translation，或研究发起人对 H0/OriginDone 的修正触发。不得以更多普通 Zeno 文献、更多 generic factorization fixture 或“ZFC 无时间 primitive”重开。

## 8. 直接调用

    按照 SOP=H0-Z0-FOUNDATION-ADEQUACY-SOP，继续推进，直至无法推进。

第一最小行动是 HZ0-0 和 HZ0-1：冻结 main H0 fingerprint，并只读比较 KLV、CCHM、Cubical Agda 与 HoTT Book 的 exact variant / acceptance coverage。还不启动新的 proof、worker、tag、push或发布。
