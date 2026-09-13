# N1 有界自然消费者审计：截断、partiality 商、univalent transport 与成本

> 文档身份：`CURRENT AUDIT EVIDENCE / BOUNDED_NEGATIVE`
> 日期：2026-09-12
> 触发：C5 判定当前唯一决定性缺环是 E6（natural consumer）
> 审计集合：Cubical library v0.9 全库（与十个机器证明相同的库身份）＋四份一手外部入口
> 结论：**`BOUNDED_NEGATIVE_MOVE_TO_RP_B01`——在本次固定审计集合内没有找到把较弱资格当较强资格使用的 natural consumer；被审计接口均以显式假设、条件、相干数据或类型围栏把该升级挡住。**

## 0. 方法与范围

本次审计把 E6 候选定义为一个真实、固定版本、可回查的接口或使用流程，同时满足：

1. 它接受一个较弱资格（结果商、命题截断、裸函数、等价存在、仅 ret/tau 的 delay、结构等价）； 
2. 它在一个后续操作中要求该资格未保留的维度（完成先后、竞争、point preservation、成本、时序、来源）； 
3. 它对**同一任务**作出实际承诺，而不是把“可疑”留给读者推断； 
4. 它没有显式添加神谕、全知未来、额外输出或明示选择公理来改变任务。 

审计集合固定如下，不随搜索结果扩大：

| 编号 | 审计对象 | 身份 | 可核层级 |
|---|---|---|---|
| S1 | Cubical library v0.9 全库 | tag commit `b150186d2544e7efeddd31e5d14a8b9ecbb100f7`；tree SHA-256 `73ccfbaf960f252800da02dac6a9bbef72d1214e2907940466dc2abef2060a81`；1111 files / 7,511,145 bytes（`HoTT/formal/partiality-race-timeout/TOOLCHAIN.json`） | 代码级完整搜索 + 关键模块全文阅读 |
| S2 | Chapman–Uustalu–Veltri, *Quotienting the delay monad by weak bisimilarity*（MSCS 29(1)） | Cambridge Core 文章页；抓取 840,241 bytes，SHA-256 `f9f2656940e2aae7a0b5c923e12dd3966a92252473764b985fd5fa1386dda65c` | 公开摘要级 |
| S3 | Altenkirch–Danielsson–Kraus, *Partiality, Revisited*（arXiv:1610.09254） | 全文 HTML 抓取 322,823 bytes，SHA-256 `188d3f718f03d8f601cf86364f7c31fdf7d807741243d62cc0e91c5734d9d359`；纯文本 63,103 chars | 全文关键词级 |
| S4 | Møgelberg–Zwart, *What Monads Can and Cannot Do with a Few Extra Pages*（arXiv:2311.15919） | 摘要页 41,258 bytes，SHA-256 `8ddb3b9db7cbe3ff914af83d97186696ed01e25ba36359073114e88a69aa831b`；全文 HTML 不可得 | 公开摘要级 |
| S5 | *Cost-Aware Type Theory*（arXiv:2011.03660） | 全文 HTML 抓取 1,421,832 bytes，SHA-256 `9ee3f929a3d0e05c3df5133a1b6b8b8663f817a295394367dbc855bee57d1224`；纯文本 225,602 chars | 全文关键词级 |

抓取日期为 2026-09-12（本地时间）；保存位置：
`.codex/research/hott/sessions/S-RES-20260912-043-NATURAL-CONSUMER-AUDIT/evidence/sources/`。
摘录文本 `abstracts.txt` SHA-256 `785697cb5203391fc4d051fecf6348cba611ad962b1ae187bc6012400759dca6`。

审计限制：S2/S4 只核到公开摘要；S3/S5 只做全文关键词与相关段落级核对，不是逐行数学复核；S1 的搜索是确定性的词汇/路径搜索，但“没有找到”只能支持本审计集合内的负结论。

## 1. T1：partiality/delay 商消费者

### 1.1 本地 Cubical v0.9

全库只有一处 delay 定义：

`Cubical/Codata/M/itree.agda`（`{-# OPTIONS --guardedness #-}`）：

```text
delay R = M (delay-S R)
delay-ret : R → delay R
delay-tau : delay R → delay R
```

它是 **M-type 的裸 delay**：只有 `ret` 与 `tau`，没有 `bind`、没有 weak bisimilarity 商、没有 race/timeout/deadline/scheduler、没有消费者。全库对它的唯一引用是索引模块 `Cubical/Codata/Everything.agda`。

对 `race`/`timeout`/`scheduler` 做词边界搜索：**0 命中**（`trace` 等子串命中已排除）。

结论：S1 内不存在 delay 商消费者；也就没有把结果商提升为含完成前后续能力的本地接口。

### 1.2 外部一手来源

S2 摘要（Chapman–Uustalu–Veltri）：setoid 路线下 “the delay datatype quotiented by weak bisimilarity is still a monad”；商类型路线下 “it is difficult to define the intended monad multiplication for the quotiented datatype”，其解法 “postulate some principles, crucially proposition extensionality and the (semi-classical) axiom of countable choice”。

S3 摘要与全文（Altenkirch–Danielsson–Kraus）：用 QIIT 直接构造 partiality monad，不依赖 countable choice；并证明 “in the presence of countable choice, our partiality monad is equivalent to the delay monad quotiented by weak bisimilarity”。全文关键词计数：`countable choice` 17、`quotient` 38、`monad` 49、`weak bisimilar` 7；`race`/`timeout`/`deadline`/`scheduler`/`concurr` 均为 0。

S4 摘要（Møgelberg–Zwart）：系统研究 delay monad 与其它效应的组合，给出 “general theorems stating which algebraic effects distribute over the delay monad, and which do not”，并对不可能情形 “salvage some of the impossible cases by considering distributive laws up to weak bisimilarity”。

三者共同指向的接口事实：

- 这些工作的消费者是 partiality monad（`return`/顺序 `bind`、`ω`、weak bisimilarity）；
- 商/单子的存在性要么依赖显式 choice 假设，要么改用 QIIT；差异被写成定理；
- 效应组合的失败被明确记录为“不可分配”，或降级为 “up to weak bisimilarity”；
- 没有任何摘要声称“结果商就是含竞争/调度语言的完整程序身份”。

判定：**T1 在本次审计集合内没有 E6；最接近的接口都把假设或失败条件显式写出，属于 documented boundary。**

## 2. T2：truncation 消费者

S1 的截断接口给出四层围栏：

1. 命题消去必须给 `isProp`：`rec : isProp P → (A→P) → ∥A∥₁→P`（`HITs/PropositionalTruncation/Properties.agda`）；n 级截断要求 `isOfHLevel n B`（`HITs/Truncation/Properties.agda`）。
2. 集合/群胚消去必须给相干数据：`rec→Set` 要求 `2-Constant f`，`rec→Gpd` 要求 `3-ConstantCompChar` 一类相干证明；库内 `recPT→CommRing`、`PropTrunc→Group` 都显式携带这些数据。
3. `SplitSupport A = ∥ A ∥₁ → A` 被定义为**假设类型**（`Relation/Nullary/Base.agda`）。其全部出现都是“假设之间的等价/推导”（`PStable→SplitSupport`、`SplitSupport→Collapsible`、`Collapsible→SplitSupport`、`HSeparated↔Collapsible≡`），没有无条件生产者。
4. `MagicTrick` 的 near-inversion 是最接近的“提取器”：

```text
recover : (tx : ∥ A ∥₁) → typ (B∙ tx)
recover∣∣ : (x : A) → recover ∣ x ∣₁ ≡ x
```

它逐点定义相等，但编码不是 `∥ A ∥₁ → A`；模块注释明确写出 `recover : ∥ A ∥₁ → A` **不能通过类型检查**，且 `cong recover (squash₁ ∣ x ∣₁ ∣ y ∣₁)` 不能给出 `x ≡ y`；模块头还引用了专门的后续说明 “Composition is not what you think it is! Why ‘nearly invertible’ isn’t”。

判定：**T2 的最近候选（MagicTrick / SplitSupport）都被类型规则或显式假设围栏挡住；S1 内没有 E6。**

## 3. T3：univalent transport 消费者

S1 的 univalence 接口给出的是**结构性计算规则**：

```text
uaβ : (e : A ≃ B) (x : A) → transport (ua e) x ≡ equivFun e x
```

可观察量由等价的结构签名决定；结构同一性原则要求比较的就是这些字段。全库搜索：

- “preserve/same cost|time|runtime”一类声明：0 命中；
- race/timeout/scheduler：0 命中（词边界）；
- 没有 cost/timing 模块。

判定：**S1 内没有接口承诺结构等价会保持签名之外的观察量；没有 E6。** 这不排除库外用户自行作出的越界解释，但那是使用者的额外承诺，不是被审计接口的承诺。

## 4. T4：成本/时序接口

S5（CATT）摘要：函数外延性与复杂度 “often at odds”；CATT 引入 “a primitive notion of cost (the number of evaluation steps)” 和 “a new dependent function type ‘funtime’”，并把它描述为 “a cost-aware version of function extensionality”。全文关键词：`race`/`timeout`/`deadline` 0；`schedul` 1（编译/调度策略的动机性提及）；`concurr` 4（其他效应的背景）；`substitut` 8（类型论结构规则语境）。

它做的是**把成本加入类型结构**，不是声称可以从裸函数恢复成本。本 repo 的 `MP-COST-FACTORIZATION-001`（C-96–C-99）已用机器证明给出同一结构：裸函数上无可区分谓词、无成本恢复 consumer，细化表示可恢复。

判定：**T4 的接口是 refinement interface，不是 E6 消费者。**

## 5. 候选总表

| 候选 | 看起来像 E6 的原因 | 实际围栏 | 判定 |
|---|---|---|---|
| `MagicTrick.recover` | `recover ∣ x ∣₁ ≡ x` 逐点成立 | 余域是依赖类型；`∥A∥→A` 类型检查失败；模块注释与后续文章明确警告 | 防御 |
| `SplitSupport A := ∥A∥→A` | 名字就是“支撑分裂” | 它是假设类型，不是库提供的函数；所有引理只在假设间等价 | 显式假设 |
| `satAC`（n 级选择公理） | 选择公理可以把存在提升为选择 | 它是被陈述的公理；Eilenberg–Steenrod 形式化把 `satAC` 作为显式参数传入 | 显式假设 |
| delay 商 partiality monad | 结果等价被当作延迟计算的身份 | 单子乘法需要 countable choice / QIIT；没有竞争/调度承诺 | documented boundary |
| 效应组合（delay × effects） | 组合后的语言可能有额外操作 | 论文给出哪些分配律存在、哪些不存在；不可能情形降级为 up to weak bisimilarity | documented boundary |
| `uaβ` / SIP | 等价类型可替换 | 只保证结构签名的 transport 计算；无签名外观察量承诺 | 结构性保证 |
| CATT | 成本与外延性张力 | 通过新增原生成本与 funtime 类型解决，而不是从裸函数恢复 | refinement |

## 6. 判定、限制与重开条件

判定：`BOUNDED_NEGATIVE_MOVE_TO_RP_B01`。

- 在 S1–S5 固定集合内，没有找到同时满足 E6 四项条件的 consumer；
- 找到的最近候选都被显式假设、条件、相干数据或类型检查围栏挡住；
- 这些围栏不是研究者事后添加的合同，而是被审计接口自身的签名、公理参数或文档所要求；
- 负结论的范围就是 S1–S5；不得写成“所有类型论/所有库中不存在 natural consumer”。

重开条件（满足任一即重开 N1 或直接进入机器化）：

1. 某库/论文版本提供把结果商或截断用于竞争、调度、point preservation 或成本观察的接口，且未把这些假设写成参数；
2. 某真实调用链在同一任务下把 `SplitSupport`、`satAC`、`recover` 一类接口当作无条件能力使用；
3. 新版本/新论文改变了上述围栏（例如去掉 choice 假设、增加 race/timeout 操作而仍宣称商身份完整）。

## 7. 下一工作包 N2：W51×RP-B01 提取接口审计

N1 的负结论把 A 线（race/timeout 商消费者）暂时关闭为 documented boundary；剩下的关键桥梁是 B 线 `B01-TARGET`。下一工作包固定为：

> **N2：W51×RP-B01 的 HoTT 计算/提取接口审计**——固定真实对象层→执行层接口（证明助手/编译/提取入口），逐项判定它是否把“命题 LEM 下的数学分类”承诺为“同规格有效交付”，并设置四组控制：有限步停机检测、经典分支常量、真正停机分类、显式神谕/用户实现。

N2 的完成判据：

- 找到“接口实际承诺统一有效交付” → 进入 F-011 机器化（用 `χ` 与对角证明构造同任务反例）； 
- 接口明确拒绝或要求神谕/用户实现 → 记 `DEFENSE_WORKS`，不得改写为悖论； 
- 来源不可得 → `INCONCLUSIVE_SOURCE_UNAVAILABLE` 并列出缺源。

在此结果出现前，不启动 ERCF-3，也不把一般停机/哥德尔结论改名为 HoTT 悖论。

## 8. 证据锚点

- S1：`/Volumes/D/HoTT-toolchain-cache/cubical-v0.9/cubical/Cubical/Codata/M/itree.agda`；
  `.../Cubical/HITs/PropositionalTruncation/Base.agda`；`.../Properties.agda`；`.../MagicTrick.agda`；
  `.../Cubical/HITs/Truncation/Properties.agda`；`.../Cubical/HITs/SetQuotients/Base.agda`；`.../Properties.agda`；
  `.../Cubical/Relation/Nullary/Base.agda`；`.../Properties.agda`；`.../Cubical/Axiom/Choice.agda`；`.../Cubical/Foundations/Univalence.agda`；
  身份来自 `HoTT/formal/partiality-race-timeout/TOOLCHAIN.json`。
- S2–S5 抓取件与 `abstracts.txt`：`.codex/research/hott/sessions/S-RES-20260912-043-NATURAL-CONSUMER-AUDIT/evidence/sources/`；
  各文件 SHA-256 见本文 §0。
- 上游证据：`HoTT/CLAIM_EVIDENCE_MATRIX.md`（C-59–C-109）；`理解章节/C5-十机证明后的悖论距离与自然消费者审计-20260912.md`。

## 9. 本轮不升级声明

本审计没有新增数学 claim，没有升级任何既有 claim，没有把 negative result 写成全局不存在性，也没有进入 RP-B01 或 ERCF-3 的机器化。`MP-*` 包的 `MACHINE_PROVED_LOCAL_UNCOMMITTED` 状态与 claim matrix 未变。
