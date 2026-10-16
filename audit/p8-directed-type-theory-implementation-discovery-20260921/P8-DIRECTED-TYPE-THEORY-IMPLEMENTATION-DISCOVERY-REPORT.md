# P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-001：Rzk 版本固定实现审计

**状态：** `NOT_A_CONSUMER / DEFENSE_PRESERVES_DIRECTIONAL_INPUT / P9_SHOTT_DIRUNIV_CORPUS_DENOMINATOR_NEXT / NO_NEW_HOTT_DEFECT_CLAIM`  
**日期：** 2026-09-21  
**固定分母：** `rzk-lang/rzk@01b081e602a80156966b92de935b7d62a43fceac`。  
**任务：** 对一个实际 directed/simplicial type-theory proof assistant 的源码入口，逐项执行 P7 的 K 准入条件；不把“有 directed interval”误报为“把裸同胚当作原圆环完成”。

## 1. 来源和本地去重

公开检索发现 Rzk 的官方仓库将自己描述为用于 synthetic ∞-categories 的实验性 proof assistant，并说明其目的是实现 Riehl–Shulman 的 type theory with shapes；2026 年的 Rzk 论文也把它定位为 RSTT 的计算性变体。[Rzk 官方仓库](https://github.com/rzk-lang/rzk)，[Rzk 论文](https://arxiv.org/abs/2607.12207)

本地资产侦察发现，历史材料早已把 Riehl–Shulman directed interval 作为边界引注，且文献 discovery 数据中登记了 Rzk，但都没有完成一个 P7 五项 K 审计。故本次不是第一次发现该理论，而是第一次对**固定实现版本**执行 `K-input / K-output / K-claim / K-forgetting / K-version`。

冻结文件、blob、SHA-256、raw URL 和负检索范围见 [`P8-RZK-SOURCE-FREEZE.json`](P8-RZK-SOURCE-FREEZE.json)。本报告没有下载二进制或运行 Rzk；它是版本固定的源码审计。

## 2. 实现实际提供什么

Rzk 的 README 说明它能检查各类 formalisation；其定向区间文档把 `2` 明确设为 directed interval，有 source `0_2`、target `1_2` 和定向不等式 `≤`。Cube layer 进一步区分有序 `2` 与非全序 Dedekind cubical interval `𝕀`。

这正是 P6/P7 所要求的“方向不是从普通同一性自动恢复，而是显式结构”的正控制。它也说明 Rzk 中确有 HIT circle 示例，但该示例只定义点构造子与 loop path；在本次冻结的 README、directed-interval、cube layer、data/circle 文档及两个测试文件中，没有 `OriginPresentation` 的去点、指定 completion、`CurveRun`、`Done_s` 或等价术语命中。

这一零命中严格限于六文件的固定词汇范围，不能外推为 Rzk 全库不存在相关形式化。

## 3. P7 五项 K 判别

| 条件 | Rzk `01b081e…` 的直接证据 | 判定 |
|---|---|---|
| `K-version` | Git remote HEAD、局部 detached clone、commit、六个 blob/SHA 与 raw URLs 均冻结。 | `PASS_VERSION_IDENTITY` |
| `K-input` | 定向结构通过 cube `2`、`0_2/1_2`、`≤`、shape/tope 与 extension-type 边界显式出现。不是 `U_bare(OriginDirectedDiagram)`。 | `FAIL_AS_K / DEFENSE_PRESERVES_DIRECTIONAL_INPUT` |
| `K-output` | 审计到的是 typechecker/形式化基础设施与 directed shapes；未找到从裸圆环/同胚输入输出一个 P7 `Done_s` 的入口。 | `NO_K_OUTPUT_WITHIN_DECLARED_SCOPE` |
| `K-claim` | Circle 示例是 HIT path/消去规则，不声称完成“去点圆—闭合—复原”的过程。 | `NO_SAME_TASK_DONE_CLAIM_WITHIN_DECLARED_SCOPE` |
| `K-forgetting` | 被审接口显式要求 direction/shape/boundary 条件，而非忘去后免费补回。 | `FAIL_AS_K / EXPLICIT_STRUCTURE_DEFENSE` |

## 4. Rzk 作为控制而非被攻击对象

Rzk 是本路线的有价值正控制：它显示一个实际 proof assistant 可以把方向、源/靶点和形状条件放入语言，而不是把它们隐含进普通同伦等价。这个事实支持“若任务需要方向，就应显式给方向”的工程/对象理论做法。

它没有回答用户最终问题，因为它不是标准 HoTT Book 的一个裸同胚消费者，也没有接受 `U_bare` 后宣称 P7 的 `Done_s`。因此不能从 Rzk 的存在推出“HoTT 已被修复”，也不能从它的非命中推出“所有 directed type theory 都无 K”。

## 5. 波次反思

1. **最终目标连接：** P8 首次把 P7 的 K 准入合同应用于一个真实、版本冻结、可定位的实际实现。
2. **新增事实：** Rzk 的 directed input 是显式 source/target/order/shape 结构；它没有在固定入口内作原圆环强完成承诺。
3. **为何不继续同一 Rzk 分母：** README、directed interval/cube layer、circle example 和 interval tests已足以否定 K-input/K-claim；增加同义文档检索无法把它变成 P7 K。
4. **最强反解释：** Rzk 可能在未审文件或关联 sHoTT corpus 中含更复杂案例。因此本结论严格限定当前 Rzk 六文件入口分母，不称“Rzk 全库无 K”。
5. **下一选择：** Rzk 自己把 `sHoTT` 的形式化语料列为相关大型 formalisation；其中 `diruniv` 分支被其文档列为 directed-univalence 模态形式化。因此 P9 应冻结该独立 corpus/branch、入口和代码，而不能复扫 Rzk README。

## 6. 结论

Rzk `01b081e…` 是 `NOT_A_CONSUMER / DEFENSE_PRESERVES_DIRECTIONAL_INPUT`。它没有提供 P7 所定义的实际 K，也没有产生 HoTT 缺陷结论。下一步是 `P9-SHOTT-DIRUNIV-CORPUS-DENOMINATOR-001`，其任务是版本固定地检查 Rzk 所指向的 directed-univalence formalisation corpus 是否在真实使用中显式保留结构，还是出现 P7 所禁止的任务升级。
