# 派生结构与全书理论分支

类型：HUMAN_EDITED；v0.2。这里给出定义和依赖方向，不把每个章节的全部定理冒充已经审计。
“依据 §n.m”均指 [锁定 HoTT Book](upstream/README.md)，精确文件/行在
[SOURCES_AND_COVERAGE](SOURCES_AND_COVERAGE.md) 的 105 节索引中。

## D01 · 命题、集合和同伦层级

**依据**：§3.1、§3.3、§3.11、§7.1；核心 C05/C06/C11。

```text
isContr(A) := Σ(a:A).Π(x:A).a=x
isProp(A)  := Π(x y:A).x=y
isSet(A)   := Π(x y:A).isProp(x=y)

isTrunc(-2,A) := isContr(A)
isTrunc(n+1,A) := Π(x y:A).isTrunc(n,x=y)
```

- (-2)-type 是可缩类型；
- (-1)-type 是 mere proposition；
- 0-type 是 set；
- 高阶层级递归检查 identity types。

“命题为类型”的一般证据读法不等于“每个类型都是 mere proposition”。一般 HoTT 保留高阶路径，
并非把所有证明压成同一个点。“set”指 0-type，不是一个全局成员宇宙的任意子类。

**时间接口**：需要区分信息是由某个类型本来无多样性，还是通过截断主动忘掉。二者不可混称。

**下标对照**：truncation index n 与常用 h-level n+2 不同：可缩 (-2,0)、mere proposition
(-1,1)、set (0,2)、1-type (1,3)。不能只记录一个未说明约定的 level=0；旧文献/库还须核其实际记法。

## D02 · 命题截断与存在

**依据**：§3.7、§6.9；HIT/额外类型构造，不仅由 C01–C13 自动得到。

```text
A:U → ∥A∥:U
a:A → |a|:∥A∥
isProp(∥A∥)

P:U, isProp(P), f:A→P
→ rec∥∥(f):∥A∥→P
```

相应点计算遵循所选呈现；不能不加条件把消去余域 P 改成任意类型。依赖消去同样要求恰当的
mere-proposition family。若有额外结构证明某个非命题目标也可恢复，需要另外证明，不能偷渡。

有具体见证的 Σ 与只保留存在的 ∥Σ∥ 不相同。因此“存在”并非总是一个已选定可返回的见证。

**重要对照**：截断明确提供了“可以忘”与“不能任意拿回来”的规则，既是信息损失机制，也是
防止不合法恢复的机制。理论拒绝一般见证提取并不说明它错误。

## D03 · 逻辑运算与选择

**依据**：§1.11、§3.6–3.9。

对 mere propositions，可用乘积表示合取、函数表示蕴含、P→0 表示否定；析取与存在使用
`∥P+Q∥`、`∥Σx.P(x)∥`，不是无条件读取未截断数据。

构造性“选择”：从 `Πx.Σy.R(x,y)` 可以取出函数和证明，因为每个 x 已给出一个 y。
这不同于从 `Πx.∥Σy.R(x,y)∥` 中选出实际见证。

书中集合级选择公理有截断，且限定相应 set 假设；不能取消量词域再套用。独特见证时可用 unique
choice，和一般选择不同。双重否定不能一般用于提取一个任意类型的项。

## D04 · 可选公理与禁止默加的假设

**依据**：§3.4–3.5、§3.8；第 10–11 章具体使用处。

| 假设 | 精确注意点 | Schema 默认 |
|---|---|---|
| LEM | 对 mere propositions 的 P+¬P | 不默加，逐定理声明 |
| 全类型 ΠA.(A+¬A) | 不是前一条的同义式 | 不允许冒充普通 LEM |
| 集合级 AC | 域和纤维的 set 条件、截断层次 | 不默加 |
| 命题 resizing | 不同宇宙中命题的缩放等价 | 不默加，非任意 type resizing |
| UIP/K | 全类型路径唯一性 | 不属标准 HoTT 全局假设 |
| Equality reflection | 从内部路径推出判断相等 | 不属本书核心 |
| Type-in-Type | U:U | 不属累积宇宙基线 |
| 任意一般递归 | 没有递减/生产性限制的 fix | 不属本书核心 |

书中附加公理、模型中的外部集合论和 proof assistant 内核的公理必须分开登记。特别是第 11 章
实数讨论显式处理命题大小/Ω 的便利假设，不能把每个实数结论都标成“纯最小核心”。

## D05 · 归纳对象与同伦初始性

**依据**：第 5 章；核心 C09/C10。

归纳定义不只是构造子清单：必须有对应的消去/归纳规则与计算规则，并受正性和宇宙条件限制。
初始代数和 homotopy-initiality 给出了抽象的唯一性刻画；这不是物理形成先后的自动模型。

严格正性是形成许可的一项条件，而不是“任何写成自指的表达式都非法”。§5.6 某个双重函数
Cantor 风格例子还涉及 propositional resizing；引用该反例必须保留这个大小前提。

## D06 · HIT 家族

**依据**：第 6 章；核心 C16。

| 构造 | 基本接口 | 必须回查的条件 |
|---|---|---|
| Interval HIT | 两端点及其路径 | 不等同 cubical primitive interval 或物理时钟 |
| 圆和球 | 点与环/高阶路径，或由悬挂构造 | 路径端点、依赖消去和计算层次 |
| Suspension | 两极及由 A 索引的经线路径 | 输入类型与递归/归纳数据 |
| Cell complexes / hubs-and-spokes | 用生成点/路径及附着数据表达 | 不能只保留“空间”直觉省略边界 |
| Pushout | 两侧点嵌入及沿共同域的 glue 路径 | map/cocone 的相容性 |
| Truncations | 降低同伦层级 | 消去目标的层级限制 |
| Set quotient | 关系识别并要求结果为 set | 关系/截断/商的普遍性质 |
| Algebraic HIT | 自由代数及关系 | 相应代数签名和 coherence |
| Flattening lemma | 纤维族总空间与 HIT 表达联系 | 不是任意删除依赖的规则 |

§6.13 对一般语法的未封闭性是本 Schema 的显式边界。第 11 章高阶归纳-归纳实数构造不能仅凭
C16 的圆规则自动视为已被一个完整机器语法覆盖。

## D07 · n-截断、连通性与模态

**依据**：第 7 章及 [Rijke–Shulman–Spitters](https://arxiv.org/abs/1706.07526v6)。

n-截断是向 n-type 的反射；n-connectedness 描述相应截断的可缩性；它们支持映射的纤维分析、
正交分解和 modalities 的讨论。

这里的模态是数学结构，不默认等于“稍后”或因果时间。将第 7 章任意 modality 与 guarded
later 等同，是未证明的跨系统替换。

**审查接口**：反射/商/截断丢失了哪些可观察区分，哪些目标因满足消去条件仍可以忠实保留？
若目标不满足条件，正确结论可能是不能下降，而非理论仍错误宣称可以下降。

进一步区分：

| 结构 | 基本数据/性质 | 必查条件 |
|---|---|---|
| Reflective subuniverse | 指定一类类型、反射器 O、单位 η_A:A→OA；向该类目标的映射有相应普遍性质 | 不是任意函数 A→B 都算反射 |
| Modality | 具有适当依赖消去的反射结构；相关形式下可用 modal Σ-closure 刻画 | 依赖消去是实质条件，不能把所有 reflector 自动叫 modality |
| Localization | 对指定映射族强制局部性；常通过相应 HIT 构造 | 允许的签名/宇宙，是否形成所需 modality 另核 |
| Lex modality | modality 且保有限极限 | 不把 lex 当所有模态的默认性质 |
| n-truncated map | 每个同伦纤维为 n-type | 是纤维条件，不是只有源/目标截断 |
| n-connected map | 每个同伦纤维的 n-截断可缩 | 与 n-truncated 不同；分解定理需准确前提 |

本版补的是结构和侧条件，不声称重证 RSS 的全部等价刻画。研究“忘却”时应先看普遍性质实际
许可向哪些目标消去，不能把正确限制误当悖论。

## D08 · 合成同伦理论

**依据**：第 8 章，全部十节已在覆盖索引登记。

主要结构：带基点类型、loop space、同伦群、纤维序列、悬挂、Hopf fibration、Freudenthal、
van Kampen、Whitehead 相关结果、encode-decode。

本 Schema 不重证这些定理；使用其中一个定理时必须展开它的连通性、截断层级、基点和其它前提。

**关键区别**：loop space 是 `Ω(A,a):=(a=_A a)`，不是 `Map(1,A)`。基点依赖不能被符号相似
掩盖。路径/同伦群的维度不自动成为运行时维度。

## D09 · 范畴与结构同一性

**依据**：第 9 章；§2.14–2.15。

Precategory 由对象类型、每对对象间的 hom-set、恒等、复合和结合/单位律组成。这里的普通态射
不是 identity path；不要求每个态射有逆。

书中 category 在 precategory 上要求对象 identity 与同构的自然映射是等价。函子、自然变换、
伴随、范畴等价、Yoneda、structure identity principle 和 Rezk completion 分别属于不同构造层次。

“结构同一性”要有结构签名和保结构等价；仅底层类型等价不自动保留日期、来源、角色、资源或
任意外部字段。将这些字段加入结构后，要重新检查等价是否保存它们。

## D10 · 集合论与累积层级

**依据**：第 10 章。

主题覆盖：set 的范畴、基数、序数、经典良序、累积层级。集合级商、像、极限/余极限与选择等
各有前提。HoTT 中定义集合论对象，不使所有 HoTT 类型变成朴素集合。

**研究关系**：Russell 类比应明确比较无限制 comprehension 与具体 HoTT formation/宇宙规则，
不能把“都想提供数学基础”当成两个系统有相同形成公理的证据。

## D11 · 实数、完备性与分析

**依据**：第 11 章。

两类主要构造：Dedekind cuts 与 Cauchy reals。Dedekind cuts 的 inhabited、rounded、disjoint、
located 条件都是定义的一部分；“一个切分”不足以替代它们。实数的 universe/Ω 条件要保留。

Cauchy reals 的高阶归纳-归纳式定义、消去、运算与完备性，和 Dedekind reals 的比较、区间紧致性、
surreal numbers 都有独立来源节。v0.1 提供回源地图，不冒充已经逐证明检查。

**时间审查**：完备性/极限存在不能直接解释为某个运行程序完成了无限步骤；反过来，也不能因
没有最后一个有限索引而直接断言连续数学不一致。必须固定实际操作制度与目标观察量。

## 关键结论的依赖读取表（v0.2）

下表是已知来源的阅读入口，不是最小公理集或独立性证明；“此证明使用”不写成“定理不可缺少”。

| 结论/构造 | 需要核的依赖 | 来源 | 本地状态 |
|---|---|---|---|
| 路径逆/复合、ap、transport | Id/J、依赖类型与各签名 | Book §2.1–2.3 | 规则/构造已描述，无本轮新编译 |
| 等价的各正确刻画 | 对应 Π/Σ/Id 数据、命题性证明中的 extensionality 假设 | Book 第4章 | 部分正文已核，不宣称全套无 funext |
| UA 推出 funext | 标准 universe UA，不是任意弱同名原则 | Book §4.9 | 一手定理定位 |
| 截断消去普遍性质 | 指定截断类型与目标层级限制 | Book §3.7、第7章 | 规则已描述 |
| π₁(S¹) 与整数 | 圆、loop、截断、transport/encode-decode 及所用 UA | Book §8.1 | 来源索引，不冒称本地重证 |
| 结构同一性 | 具体结构签名、保结构等价、相应 univalence | Book §9.8、Univalence Principle | 一手入口，逐实例待核 |
| n-connected/n-truncated 分解 | 截断/纤维及相应构造 | Book §7.6、RSS | 结构说明，完整证明未重建 |
| local-universes 严格化 | 输入 comprehension category、弱稳定与基范畴条件 | 语义页 S04 | 论文范围已核，非本地模型实现 |

## D12 · 全书范围与非核心材料

**依据**：main.tex 的 include 顺序与 11 章 section 清单。

| 章 | 内容 | 本 Schema 的职责 |
|---|---|---|
| 1 Type theory | 基础构造与记法 | C01–C11 + 来源索引 |
| 2 Homotopy type theory | 路径、等价、函数外延性、单价性、结构 | C12–C15 + D09 |
| 3 Sets and logic | 命题/集合、截断、选择、resizing | D01–D04 |
| 4 Equivalences | 正确等价定义、性质与 funext 推导 | C13–C15 |
| 5 Induction | W、初始性、语法与推广 | C10、D05 |
| 6 Higher inductive types | HIT 实例与语法边界 | C16、D06 |
| 7 Homotopy n-types | 截断、连通、模态 | D01、D07 |
| 8 Homotopy theory | 合成同伦理论 | D08 |
| 9 Category theory | 范畴、Yoneda、结构同一性 | D09 |
| 10 Set theory | 集合数学与累积层级 | D10 |
| 11 Real numbers | 构造性实分析与 surreal | D11 |
| 附录 A | 两种形式呈现、HoTT 扩展、元理论 | C01–C18 |

每章所有编号 section 均有来源行入口，但“章节入图”不是“每个证明通过”。题目、练习、Notes、
引言历史问题是附加证据，不被计为已经逐题求解。
