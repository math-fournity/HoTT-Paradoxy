# P16-FOURTH-SUCCESSOR-DISCOVERY-001：选择 Cubical Agda Cauchy 实数语料

**状态：** `SUCCESSOR_SELECTED / CUBICAL_HOTT_CAUCHY_REALS_ACTUAL_FORMALISATION_CANDIDATE / P17_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM`

## 判词改变凭据

P15 已关闭一个组合图 embedding/isotopy 分母：其 `Map`、face、walk 和 spherical 结构显式保留，且任务不同于 P13 的 M/N operation-sensitive Done。P16 必须换分母，不能再扩展 P15 的关键词或网页范围。

公开的一手来源发现 Jackson Brough 2026 年论文《Formalizing the Real Numbers in Homotopy Type Theory with Cubical Agda》。论文明确声称直接形式化 HoTT Book 的 Cauchy real higher inductive-inductive family，并在 Cubical Agda 中无 postulate/hole 地 type-check。它将“已完成实数对象、构造过程和理论经济性”带入一个实际 HoTT 相关构造，因而是与 P15 不同且值得 P17 审计的候选。

## 双重侦察

- **公开学术来源：** [arXiv:2604.24782](https://arxiv.org/abs/2604.24782) 的版本为 v1、2026-04-23。摘要将三类构造代价并列：经典 Cauchy 完备性常需 countable choice、Bishop setoid 持续 bookkeeping、Dedekind cut 的 universe tracking；并说明其 HoTT Book Cauchy reals 形式化直接利用 Cubical Agda HIT 支持。
- **本地历史资产：** `LIT-DENOMINATOR-001` 的发现表已经有同一标题/URL，但状态只是 `DISCOVERY_UNREVIEWED`，triage 也只是 `ADJACENT_TITLE_SIGNAL`。本项目尚无该论文或其源码的 P7 五项审计、版本冻结或 K 判词。
- **已排除范围：** P2 Book SIP、P3 UniMath、P8 Rzk、P9 sHoTT、P11 Coq-HoTT Circle/Coeq、P13 几何对照和 P15 Prieto-Cubides 已不再是本轮分母；P16 不重审它们。

## P17 候选卡

| 字段 | 冻结内容 |
|---|---|
| Candidate | `P17-CUBICAL-HOTT-CAUCHY-REALS-CORPUS-001` |
| 版本身份 | arXiv `2604.24782v1`，submitted 2026-04-23；作者 Jackson Brough |
| 理论/实现 | HoTT Book Cauchy reals 的 higher inductive-inductive family；Cubical Agda formalisation |
| 初步 Input | rationals、Cauchy approximation/limit constructors、relation/identification data；P17 必须从固定 paper/code locator 精确化，不能用摘要补齐 |
| 初步 Operation | HIT/HII construction、truncation/elimination 与 constructive-analysis operations；P17 必须审实际接口 |
| 初步 Observation/Done | real-number construction、Cauchy completeness/algebra/order等声明；P17 必须区分“数学对象存在”与 P13 的 M/N operation-sensitive Done |
| P7 任务 | `K-input`、`K-output`、`K-claim`、`K-forgetting`、`K-version`；先判 task-equivalence，再谈可能的 bridge |
| 正控制 | 若源码/论文显式携带 approximation、modulus、relation、truncation或choice条件，应登记为结构保留，不能误报为无条件完成 |
| 最强反解释 | 这是实数构造，不是圆去点 M/N 复原；即使它完成 Cauchy reals，也可能完全不含 P13 的 bare-H-to-Done 调用 |
| 停止 | P17 只读固定 arXiv v1、作者公开 code locator（如可核）与直接论文段落；不下载/编译/全库扫描 |

## 波次定位

1. **最终目标连接：** P16 为实际消费者链新增一个真实的 real-layer construction，而不是继续寻找相同的 embedding 关键词。
2. **全局坐标：** P3 `K_app` 的 successor discovery；尚未触发 P4。
3. **实际价值：** 它把本地仅有的未审题录升级为带版本、理论构造、候选输入/操作/Done 和任务差异控制的 P17 卡。
4. **为何不继续 P16：** 新分母、公开来源与本地覆盖缺口已固定；再搜更多词不能替代 P17 的直接 source audit。
5. **裁决：** `SWITCH_BRANCH / SUCCESSOR_SELECTED`。P17 未开始；P16 未发现 K、数学定理、实现缺陷或 HoTT 缺陷。

## 禁止外推

- “无 postulate/hole type-check”是作者论文关于该形式化的来源陈述，不是本项目的 kernel replay。
- 该题名和 abstract 不证明与原圆环任务同一；P17 必须先判定这一点。
