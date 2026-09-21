# P1-RMIN-SPEC-001：最小来源—操作—复原规格资格化

> 状态：`R_MIN_ACCEPTED_WITH_SCOPE / SOURCE_AND_INTERFACE_AUDIT / NO_NEW_MATHEMATICAL_CLAIM`。
> 分支：P1，四分支计划的共同规格支。
> 任务：判定既有 `RichCurve` 是否足以使 P2 的规则级桥和 P3 的 ABX 消费者审计使用同一强任务；不重跑 C-250–C-324、Flash、D1/D2/D3、Book 或既有几何构造。

## 1. 判词改变凭据

| 项目 | 本 wave 的固定内容 |
|---|---|
| 要改变的判词 | `P1-RMIN-SPEC-001` 的三种预注册结果之一；若接受，P2 获得固定强任务 oracle；若不确定，P2/P3 暂停 |
| 新输入 | `goal-3.md` 的四分支/波次 SOP、总体计划 P1，以及现有 `RichCurve`、`NativeSourceContract`、`NativeTaskIntegration` 的直接代码审计 |
| 新分母 | 这五个现有接口及其现有 formal receipts；不是新的外部理论扫描或内核重跑 |
| 最小行动 | 将现有字段按来源、表示、观察、操作和完成重新组合为 `R_min`，测试是否有独立任务理由和现有正反控制 |
| 正控制 | `reexpressed` 将完整 `CurveData` 沿 encoding 运输，`satisfiesReexpression` 与 `actualRun` 成立 |
| 最强反解释 | 预选直线 `nRich` 的裸 carrier 合格但不 `Denotes`，且同一 pair 在 `CurveRun` 与 `Success` 下答案不同 |
| 停止 | 给出三种 P1 判词之一；不扩展为完整 OriginTop、新物理模型或 P2/P3 搜索 |

## 2. 为什么 `RichCurve` 单独不足

`RichCurve = Σ A. CurveData(A)` 已记录一个载体、开区间参数化、平面实现、闭参数图、连续性和内点一致。它足以让闭图成为类型字段，但它本身没有指定：哪个富化曲线是原对象、要变到哪个 target carrier、哪条 H/encoding 被允许、采用哪种操作、或何种 Done 才算完成。

因此 P1 的结果不是“另造一个取代 RichCurve 的玩具结构”。当前最小规格是对现有接口的组合：

```text
R_min(i, O, D) :=
  i : Input
    = (source : RichCurve, targetCarrier, encoding : Bare(source) ≃ targetCarrier)
  observation = ClosedParameter → RealPlane
  denotation  = Denotes(i, r)
  O           = 明确选择的 State i 上操作合同
  D           = 明确选择的操作性完成条件
  soundness   = D(r) → Satisfies(i, r)

Done_w(i,r)  = Bare(r) = targetCarrier(i)
Done_s(i,r)  = Satisfies(i,r) = Done_w(i,r) × Denotes(i,r)
```

`D` 不能被偷偷省略：`NativeSourceContract.Done` 规定 `r = reexpressed(i)`，它由 `doneIsSound` 推出 `Done_s`；`CurveRun` 和 `Success` 则是两种不同的操作/完成合同。`R_min` 要求选择一个合同，而不宣称其中任何一个等于所有物理或几何复原。

## 3. 字段—任务理由与现有证据

| `R_min` 成分 | 现有代码锚点 | 对圆环任务为什么必要 | P1 判断 |
|---|---|---|---|
| 原对象与目标载体 | `Input.source`、`Input.targetCarrier`、`Input.encoding` | 没有指定源和目标，只有抽象的两个裸空间，无法问“是否保持同一来源过程” | 已覆盖 |
| 当前案例的圆/删点锚 | `actualInput.source = mRich`；`mRich = StrongPuncture,mData`；`mCompletion` 两端到 `east` | 使当前合同确实落在指定去点圆与闭合图，而非任意线段故事 | 已覆盖为指定案例；不外推全历史来源 |
| 富化闭图 | `CurveData.parametrization/realize/close/closeContinuous/agrees` | 闭合/复原过程至少要能观察闭参数图及其与开参数呈现的一致 | 已覆盖 |
| 强观察 | `Observation`、`observe`、`Denotes` | 仅 carrier 同型无法判定闭图是否仍代表原过程 | 已覆盖 |
| 弱/强完成 | `Satisfies`、`Done`、`doneIsSound`、`checkedOutput` | 区分载体到达与来源图保持的完成，防止把静态 H 当过程 Done | 已覆盖 |
| 操作合同 | `AmbientStep/Success` 与 `CurveRun` | 同一 pair 在不同允许操作下可有相反答案，必须把操作公开为参数 | 已覆盖为两个可比合同；不是全物理操作全集 |
| 反向与正向控制 | `plainNNotSatisfied`、`bareCheckIsInsufficient`、`satisfiesReexpression`、`samePairDifferentOperations` | 防止规范把恢复不可能性写进去，或把所有同胚改写为失败 | 已覆盖 |

这些锚点的唯一源码位置是 `HoTT/formal/agda-unimath/hott-z/NativeRichCurve.agda`、`NativeSourceContract.agda`、`NativeTaskIntegration.agda` 与 `NativeCurveTask.agda`。报告不把模块名的短写当作另一个路径；后续验证器会拒绝不存在的旧短路径。

### 3.1 本地 kernel 收据的适用范围

本 wave 没有重跑 Agda。它复核已有的两个本地 run receipt：`20260920-MP-ASTRA-NATIVE-SOURCE-CONTRACT-001-01`（`C-295`/`C-296`）和 `20260921-MP-ASTRA-NATIVE-TASK-INTEGRATION-001-01`（`C-320`）。两份 receipt 都记录了对应源码、`KERNEL_ACCEPTED_WITH_SCOPE` 和明确 non-goals；它们支持“现有接口和正反控制确实已被该次 kernel 检查”的受限事实。

两份 receipt 同时都标记 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。因此 P1 不把它们误写成跨版本、完整物理过程或 HoTT 理论结论；P1 的新增结论只是对当前本地接口、既有运行范围和任务合同的审计性组合。

## 3.2 本 wave 的学术与社区检查

本次搜索的固定问题是：来源、标记、闭图、允许操作和完成条件的附加结构，是否已有成熟的数学/HoTT 语言；这些成果会不会改变 `R_min` 的命名、独立性或 P2 的理论分母。搜索采用公开一手论文、HoTT Book 和相关拓扑研究，结果如下。

| 来源 | 与 `R_min` 的关系 | 分类 | 对本 wave 的影响 |
|---|---|---|---|
| [HoTT Book §9.8](https://homotopytypetheory.org/wp-content/uploads/2013/03/hott-online-611-ga1a258c.pdf) | 给出载体上的结构族 `P`、保持结构的态射 `H` 和结构对象 `Σ x.Px`；标准结构时讨论结构等同与同构 | `KNOWN_ANALOGUE`，且是新的 P2 理论分母 | 证明“把载体和结构分开”不是新想法；但它要求结构保持，并不把裸 carrier 等价自动升格为 `Done_s` |
| [Shulman 2015，real-cohesive HoTT](https://arxiv.org/abs/1509.07584) | 明确区分拓扑/连续结构与 homotopical shape，研究由前者到后者的过程 | `KNOWN_DEFENSE_OR_BOUNDARY` | 支持不把普通 HoTT 的 homotopy identifications 等同于连续过程；以后可作为 P2/P3 的比较/反例来源，不是当前桥 |
| [Douteau 2019，stratified homotopy theory](https://arxiv.org/abs/1908.01366) 与 [Douteau 2018](https://arxiv.org/abs/1801.04797) | 研究带 strata/过滤数据的空间；相关不变量只在保持 strata 的同伦下不变 | `NEARBY_NOT_SAME_TASK` | 说明带附加结构的等价是已有严格数学主题；当前闭图/operation/Done 合同不是一个已证明等同于 stratification 的结构 |
| pointed/relative homotopy 的标准定义 | 固定基点、子空间或相对边界可使普通 homotopy 细化为保持指定数据的关系 | `NEARBY_NOT_SAME_TASK` | 为 `C,p` 与端点观察提供已有语言，但没有编码当前 source/encoding/Run/Done 的完整合同 |

该搜索没有发现“圆去一点的来源历史”已经被命名为与当前 `R_min` 完全相同的理论，也没有发现 HoTT Book §9.8 或 cohesive HoTT 声称裸 H/U 自动满足当前 `Done_s`。因此不能声称原创性，也不能把相邻理论当作已经解决圆环任务。

## 4. P1 判词

`R_MIN_ACCEPTED_WITH_SCOPE`。

接受的不是“完整现实创造史已经形式化”，也不是“传统拓扑已被推翻”。接受的是一个足以供 P2/P3 使用的、最小且任务相关的合同：当前原对象、编码、闭图观察、弱/强完成和明确操作合同都已有直接类型/运行锚点；RichCurve 单独不足，但不需要增加新的原始数学字段，只需把现有 `Input + CurveData + Denotes/Satisfies + O + D` 作为同一规格使用。学术检查进一步将其定位为已有 structure-preserving 思路的受限实例，而非新名词本身。

边界仍然清楚：材料、制造史、任意物理可行性、所有环境操作、完整范畴 `OriginTop`、自然性的一般定理和新颖性比较都没有在 P1 完成。若用户认为其中一项是当前强 Done 的必要组成，它是一个新的、独立的更强 R 合同，不可倒灌进这次 P1 结论。

## 5. 波次定位与后继裁决

| 波次问题 | P1 回答 |
|---|---|
| 最终目标连接 | P1 固定最终合格见证链中的“同一任务/强完成 oracle”边；没有它，P2 的理论桥和 P3 的消费者都无法被判为真的强提升或正确防线 |
| 全局坐标 | P1 的上游是 H/R/K 整备与原生已证控制；下游是 P2 的一个新规则级理论分母，P3/ABX 仍等待 |
| 实际价值 | 将已有散落在三个模块的 source、denotation、operation 和 Done 合成一套不可事后换题的规范；学术检查表明它应按结构保持、cohesion 和相对/分层结构的已知语言比较，而非孤立宣称新拓扑 |
| 继续同支？ | 不继续。下一步若继续 P1 将变成完整 OriginTop 或物理模型的新研究，已超出这次最小资格化；没有新的独立字段凭据 |
| 不延续理由 | P1 的声明范围已闭合；继续只会重复已有 Rich/SourceContract/TaskIntegration 控制，而 P2 现在已有可固定的问题 |
| 裁决 | `CLOSE_WITH_SCOPE`；`SWITCH_BRANCH` 到 P2，但尚未启动 P2 的来源检索 |

## 6. 当前后继

下一最小工作单元为 `P2-KTHEORY-SIP-001`：冻结 HoTT Book §9.8 的精确版本、`(P,H)` 标准结构条件、结构态射与结论，检验当前 `R_min` 哪些字段可写入该框架、哪些不满足其前提，以及 SIP 是否只保持显式结构而非把 H/U 升格为 `Done_s`。该分母在原 D3 Book-core 审计之外，但必须先做版本和命题资格化；不能先假定理论桥存在，更不能开始外部 K_app 扫描。

本报告不新增数学定理；它是已存在类型化接口的规格资格化和路线裁决。
