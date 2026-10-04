# ZFC-HOTT-Q-UNIFORMITY-SOP：芝诺与 HoTT 同一 Q 的统一判词验证 SOP

> **稳定引用名：** `ZFC-HOTT-Q-UNIFORMITY-SOP`
>
> **身份：** `TASK_SCOPED_QPROFILE_MAPPING_AND_CONDITIONAL_INSTANTIATION / CONTRIBUTOR_CANDIDATE_NOT_CURRENT / NOT_AN_AUTOMATIC_ZFC_INCONSISTENCY_CLAIM`。
>
> **当前起点：** `MP-ZFC-META-OBSERVATION-CONSISTENCY-001` 已机器证明条件性 O1–O5/QProfile 政策定理；H094 的当前判词是 `PROFILE_MATCH_NOT_YET_PROVED`。

## 0. 目的与不改变的研究问题

本 SOP 只推进这一件事：检验研究发起人提出的芝诺—HoTT比较能否被填成**同一个完整 QProfile**，从而把已机器证明的条件定理实例化为对一套 ZFC 基础性 O3–O5 观察政策的具体不一致判词，或者诚实地得到字段级不匹配／证据不足结论。

固定的条件定理是：

```text
QProfile(Zeno) = QProfile(HoTT)
∧ Judgment(Zeno) = originalResolved
∧ Judgment(HoTT) = bridgeRequired
⟹ ¬ QUniform
```

它的 O3–O5 版本还要求：一个`requiresBridge=true`的案例若被宣称为`originalResolved`，必须有O3区分、O4同一任务bridge、O5元审查、bridge payment和原任务保持；缺这些项目即不满足`O3O5Adequate`。

本 SOP 不把下列事情混为一谈：

1. `ZFC ⊢ ⊥`的对象语言形式矛盾；
2. 一套基础性完成观察政策的条件性不一致；
3. IEP／Bathfield／HoTT来源之间的哲学分歧；
4. 一个正式程序、一个现实过程和一个来源所说任务是否同一；
5. `revisedResolved`与`originalResolved`。

## 1. 固定的 QProfile 合同

每个站点都必须填写同一张卡，不能只凭“都涉及完成、极限、永不停机或bridge”宣布同Q：

| 字段 | 含义 | 最低证据 |
|---|---|---|
| `State` | 被比较的共同过程状态域；两边如何嵌入／映射到它 | 版本固定的定义或明确数学模型 |
| `O1` | 时间、阶段、trace、递归或过程状态是否被表示 | 理论或来源直接定义 |
| `O2` | 数学／模型层是否给出完成类型的输出 | 精确定理、模型或来源断言 |
| `O3` | 是否区分`Done_formal`和`Done_origin` | 两个命名谓词、反例或区分规则 |
| `O4` | 是否有同一任务的状态映射与bridge验证 | 明确 transport/preservation/equivalence 证据 |
| `O5` | 元框架是否实际审查O3/O4，而不只可表达它们 | 来源定义的审查责任、调用或判词 |
| `requiresBridge` | 为什么从formal输出到原任务完成需要额外桥 | 同一任务风险的直接论证 |
| `bridgePaid` | 哪个来源、定理或模型假设真正支付了桥 | 精确支付物；不能用同名标签代替 |
| `originalTaskPreserved` | 新判词是否仍回答原任务，而非改写后的任务 | 共同State上的`Done_formal ↔ Done_origin`，或等价强度的保持证据 |
| `Judgment` | `originalResolved`、`revisedResolved`或`bridgeRequired` | 来源的精确句子和上下文 |

**铁律：** `requiresBridge`相同不等于QProfile相同；`revisedResolved`不等于`originalResolved`；能编码O1/O2不等于已实现O3/O4/O5。

## 2. 执行阶段

### U0：冻结本轮实例合同

先冻结两份站点卡及当前基线：

```text
Zeno site:
  IEP Standard Solution 全文相关段落；Bathfield pp.12–13；
  已有 H083–H093 来源控制；
  几何级数、闭连续时间与 CompletionBridge 机器控制。

HoTT site:
  CG001 QuestioningDelay 的精确程序、C-77–C-83 claim/runs；
  “解释为现实／存在性任务”仍是 bridge 的源级边界；
  对应的有界目录、截断与 Lean模型正负控制。
```

必须声明本轮的共同候选任务 `u`。若无法写出共同`u`，立即判`COMMON_STATE_NOT_YET_DEFINED`，不可启动同Q异判结论。

**最低产物：** 一张`QPROFILE-MAPPING-CARD`，逐字段列`SOURCE_SUPPORTED / SOURCE_REFUTED / UNKNOWN / CANDIDATE_INTERPRETATION`。

### U1：芝诺站点的完整字段核证

对 IEP、SEP、Bathfield以及必要的一手补充材料分别填写：

1. 谁在宣称解决？是原任务、修订任务还是模型内任务？
2. “无最后一步”是显式Done替换、bridge、还是未声明前提？
3. 连续时间端点、实际无穷、几何级数与顺序动作各自属于什么观察？
4. 来源是否真的提出／支付`Done_formal → Done_origin`，还是只为`revisedDone`付款？

不能把 IEP 的模型付款删去，也不能把 Bathfield 的批评升级为数学定理。若新来源已经给出共同State与明确端点保持关系，须登记为`ZENO_PAYMENT_CONTROL`，它可能反驳候选。

### U2：HoTT站点的完整字段核证

对`QuestioningDelay`及选定的 H0 证据逐项填卡：

1. 形式程序实际问什么、在哪个演算／宇宙／判定器中运行；
2. `never`、有界停机和截断／Lean对照分别说明什么；
3. 哪句话把它提升为现实过程、存在性追问或“同一任务”；
4. 该提升是机器定理、来源断言、候选解释还是未支付bridge；
5. HoTT侧是否真的被某个来源／基础政策判为`bridgeRequired`，而非仅有内部程序现象。

不能把`never`定理自行重命名为现实失败，也不能把一个不同演算的正控制删去。

### U3：共同State与同一任务归约

只有U1/U2各自有可回源字段后，才定义：

```text
embedZ : ZenoState → State
embedH : HoTTState → State
Done_origin : State → Prop
Done_formal_Z / Done_formal_H : State → Prop
```

随后检验：

1. 两侧的对象、输入、操作和观察是否被同一`State`保留；
2. 每一`Done`是否是同一个原任务的谓词；
3. 是否存在来源支付的`CompletionBridge`或更强的`CompletionEquivalent`；
4. 若任意一个映射改变了任务，立即登记`INTERPRETATION_BRIDGE_TASK_SWITCH`。

### U4：完整QProfile相等或不等的判定

逐字段比较，输出唯一一种状态：

| 状态 | 条件 | 可得结论 |
|---|---|---|
| `PROFILE_EQUAL_SOURCE_SUPPORTED` | 所有字段有相称来源且逐项相等 | 可进入U5。 |
| `PROFILE_MISMATCH_SOURCE_SUPPORTED` | 至少一个字段由来源证明不同 | 同Q异判不适用；记录哪个字段解释了异判。 |
| `PROFILE_MATCH_NOT_YET_PROVED` | 字段未知、只有类比或缺共同State | 保留条件定理，不实例化。 |
| `SOURCE_CONFLICT_UNRESOLVED` | 一手来源对同一字段相冲突 | 启动有界Battle或增加一手来源。 |

### U5：条件定理的实际实例化

只有`PROFILE_EQUAL_SOURCE_SUPPORTED`后，才可把实际源级值填进 Lean 的`Assessment`，并新增一个**独立 proof ID**：

```text
actualSameQ : profile zeno = profile hott
zenoOriginal : judgment zeno = originalResolved
hottBridgeRequired : judgment hott = bridgeRequired

=> ¬ QUniform actualAssessment
```

同一 run必须保存源卡hash、每个字段的来源定位、命题、内核输出、负控制和禁止外推。若Zeno来源只是`revisedResolved`，此阶段应证明该事实并返回U1/U3，不能强行套用`originalResolved`。

### U6：终局分类与停止

本 SOP 只有四种合法终局：

1. `ACTUAL_Q_UNIFORMITY_FAILURE_FORMALLY_INSTANTIATED`：U5完成；结论仅为基础观察政策不一致，不升级为ZFC对象语言不一致。
2. `PROFILE_MISMATCH_CONTROL_CONFIRMED`：明确字段不同，解释为何同Q异判不成立。
3. `PAYMENT_OR_TASK_PRESERVATION_CONTROL_CONFIRMED`：至少一侧已经支付共同任务bridge，候选对该来源失败。
4. `EVIDENCE_FRONTIER_REACHED_WITH_SCOPE`：指定分母内仍无法建立共同State／完整profile；保留条件定理和精确未知，不无限扩张检索。

## 3. P-DAG与反控制规则

每个新worker必须有独立的`NodeCard`和`QConvergenceLink`。默认顺序：来源字段核对 → 对立读法 → 独立裁决 → Master 写回。允许的节点类型只有：

```text
PRIMARY_SOURCE_FIELD_MAP
HOTT_CLAIM_FIELD_MAP
COMMON_STATE_MAPPING
PAYMENT_CONTROL
TASK_SWITCH_CONTROL
PROFILE_EQUALITY_ARBITER
```

Battle只在同一字段存在真实来源冲突时启动，且按`advocate → challenger → independent arbiter → Master`单轮结束。多数意见不构成字段事实。worker须为`gpt-5.6-terra / max`、只读、无递归、无Git/current-owner写权；运行、trajectory和source权限遵循`hott-pattern-p-dynamic-dag-orchestration`。

## 4. 机器证明与证据门禁

| 主张 | 所需证明／来源 |
|---|---|
| 条件性政策定理 | 当前 `MP-ZFC-META-OBSERVATION-CONSISTENCY-001`；可复跑，不重复发明。 |
| 实际Profile相等 | 每字段一手来源＋共同State映射＋独立形式命题。 |
| 实际异判 | 两份来源的精确判词；不能由AI解释补全。 |
| bridge已支付 | 显式`CompletionBridge`或`CompletionEquivalent`，并核原任务保持。 |
| 现实／哲学解释 | 标为`SOURCE_INTERPRETATION`或`CANDIDATE_INTERPRETATION`，不能冒充内核定理。 |

每个新数学结论按`MATH_PROOF_BEFORE_DELIVERY_V1`保存源码、run、环境、hash和claim索引。有限模型、来源转述、worker一致或超时都不能替代相称证明。

## 5. 写回、Git与自我审计

本 SOP 的候选分支写入：

```text
audit/<date>-ZFC-HOTT-QPROFILE-MAPPING-*.md
audit/<date>-P-DAG-ZFC-HOTT-*.md
HoTT/formal/zfc-observation-boundary/
HoTT/verification/runs/<run-id>/
```

每一自然单元结束做以下自审：

1. 是否把O1/O2能力误写为O3–O5已完成？
2. 是否把`revisedResolved`误写为`originalResolved`？
3. 是否把来源/解释/机器定理混为同一证据等级？
4. 是否为得到异判而偷换共同State、操作、观察或Done？
5. 新节点是否真的改变了QProfile、字段证据或停止条件；否则登记`TOOL_ONLY_DRIFT`。

用户已授权的P-DAG材料、证明收据和必要路由更新必须精确路径commit，保留Git谱系；不得混入当前dirty canonical owner。由唯一integrator在干净integration worktree上决定是否写入`dev` current truth。

## 6. `/goal` 启动句

```text
按照 SOP=`ZFC-HOTT-Q-UNIFORMITY-SOP`，完成芝诺与 HoTT 的完整 QProfile 映射、来源级判词核证、共同State／Done／bridge 保真检查，并在满足前提时实例化 `MP-ZFC-META-OBSERVATION-CONSISTENCY-001`；直至 SOP 的终局分类触发。
```

短版也可使用：

```text
按照 SOP=`ZFC-HOTT-Q-UNIFORMITY-SOP`，继续推进同 Q 异判验证，直至 SOP 停止条件触发。
```
