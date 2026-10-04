# ZFC-HOTT-Q-UNIFORMITY-SOP U1：芝诺站点的 QProfile 来源字段映射

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / U1_COMPLETE_WITH_SOURCE_DIVERGENCE / NOT_AN_ACTUAL_Q_UNIFORMITY_FAILURE`。
>
> **前件：** [U0 共同完成授权状态候选](audit/20261003-ZFC-HOTT-QPROFILE-MAPPING-U0.md)、[H095 来源节点与轨迹审计](audit/20261003-P-DAG-ZFC-HOTT-095-Terra-Max.md)。

## 1. U1 的工作对象

U1 不裁定“芝诺已经解决”或“极限理论掩盖了芝诺”。它只将三份来源如何分别规定或使用完成谓词写成可比较字段，并防止将来源自己的模型完成偷偷升级成共同原过程的完成。

设：

```text
ZenoState = (path, temporal interval, position, speed, indexed subpath/task relation)

Done_IEP(s)         = 在 IEP 的连续物理运动模型中，以正且有限速度到达目标
Done_everyStep(s)   = 每一个被任务索引的步骤都已实行
Done_finalAction(s) = 存在任务的最后／终止行动
```

这些谓词不是已经被证明相等的定义同义词。对 `Done_origin` 的值，本 SOP 仍要求在 U3 固定 `ProcessTask` 后作同一任务检验。

## 2. 来源逐字段表

| QProfile 字段 | IEP Standard Solution | SEP Supertasks | Bathfield 2018 | U1 处置 |
|---|---|---|---|---|
| `State` | 连续时空中的跑者路径、有限正速度、点事件与微积分模型。 | Zeno walk 的逐步二分任务，明确无最后一步。 | progressive/re-gressive Dichotomy、顺序行动与终止操作。 | `SOURCE_SUPPORTED`，但没有已给出的单一共同 State。 |
| O1 表示过程／时序 | 时间、位置、速度、路径均被连续模型表示。 | 步骤顺序明确表示。 | 连续空间、级数和顺序行动均被讨论。 | `SOURCE_SUPPORTED`。 |
| O2 形式完成输出 | finite-time physical arrival；级数/微积分模型。 | 几何级数极限；`everyStep` 读法下完成。 | 级数的有限和／有限总时长。 | `SOURCE_SUPPORTED`。 |
| O3 区分 `Done_formal` 与 `Done_origin` | 隐含以连续到达作为完成；不单列两个谓词。 | 显式区分 final action 与 every step，且证明性叙述为不等价。 | 显式反对由收敛／有限时长直接推顺序行动完成。 | `SOURCE_SUPPORTED`，关键锚为 SEP。 |
| O4 同任务 bridge | 模型和物理解释被 IEP 主张，但没有列出同一状态上的 `Done_IEP ↔ Done_finalAction`。 | 表明需要选定哪个 Done；没有支付三谓词的等价。 | 断言收敛本身不充分。 | `COMPLETION_EQUIVALENT_NOT_SOURCE_SUPPORTED`。 |
| O5 元框架实际审查 O3/O4 | IEP 讨论哲学分歧与可接受解。 | SEP 分析词义与 supertask。 | Bathfield 给出哲学批评。 | 三者均不是 ZFC 元理论对自身子理论的审查责任；`NO_ZFC_META_AUDIT_SOURCE_IDENTIFIED`。 |
| `requiresBridge` | 只有在把 IEP Done 转成更强 sequential Done 时才出现。 | 完成词二义使 bridge 要求显性化。 | 是，若目标是有终止行动的顺序完成。 | `PREDICATE_RELATIVE_SOURCE_SUPPORTED`。 |
| `bridgePaid` | IEP 支付 `Done_IEP` 的连续模型解释。 | 未支付 `Done_finalAction ↔ Done_everyStep`。 | 明确说收敛／有限时长不是该支付物。 | `PARTIAL_AND_TASK_RELATIVE`。 |
| `originalTaskPreserved` | 对 IEP 所选物理连续体任务可说 yes；对未固定的强 sequential contract 未证。 | 显示两个合同并非同一。 | 按更强合同提出未付缺口。 | `NOT_UNIFORMLY_SOURCE_SUPPORTED`。 |
| `Judgment` | `originalResolved`，只相对 IEP 的连续物理任务。 | `Done_finalAction` 不完成；`Done_everyStep` 完成。 | `bridgeRequired`，只相对顺序行动／终止操作的读法。 | 不可压缩为单一无条件标签。 |

## 3. Master 的来源级判词

```text
ZENO_QPROFILE_HAS_MULTIPLE_SOURCE_DEFINED_DONE_PREDICATES
ZENO_O1_O2_PRESENT
ZENO_O3_EXPLICITLY_PRESENT
ZENO_O4_NOT_PAID_AS_A_STATEWISE_EQUIVALENCE
ZENO_O5_NOT_YET_A_ZFC_META_POLICY_SOURCE
ZENO_JUDGMENT_PREDICATE_RELATIVE
COMMON_STATE_NOT_YET_DEFINED
```

IEP 的强 Standard Solution 不应被删去：它是 Zeno 站点的重要付款／反控制。Bathfield 的批评也不应被删去：它阻止我们把“级数收敛”单独冒充为顺序行动完成的 bridge。SEP 把二者之间真正需要比较的 Done 分裂为可见字段。

## 4. 这一步排除了什么、留下什么

### 已排除的捷径

1. `IEP says resolved` 因而 `Done_origin` 已对所有完成读法成立；
2. `finite sum` 因而逐一顺序行动必已完成；
3. Bathfield 的哲学论证因而 `ZFC ⊢ ⊥` 或极限理论错误；
4. 只有“都谈极限／永远／完成”就足以与 HoTT 说成同一个 Q。

### 留给 U2/U3 的最小判别行动

1. **U2：** 对 `QuestioningDelay` 固定其真实 `State`、`Done_formal`、各正负控制及其来源级 Judgment；分清内核 `never` 与用户的 UR 解释 bridge。
2. **U3：** 判断 `ZenoState` 和 `HoTTState` 能否映到同一 `AssessmentState`，并逐项保存 `ProcessTask`、操作、观察及 Done。若只能共用“某理论如何交付完成”的抽象槽位，而不能保留原任务，必须登记 `INTERPRETATION_BRIDGE_TASK_SWITCH`。
3. **U4：** 只有所有字段有来源支付，才可能说 `PROFILE_EQUAL_SOURCE_SUPPORTED`；当前 U1 本身已显示，任何未来相等证明都不能省略 Done 谓词的选择。
