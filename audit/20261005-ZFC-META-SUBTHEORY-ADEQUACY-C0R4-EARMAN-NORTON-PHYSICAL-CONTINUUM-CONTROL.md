# C0R4 / F-A：Earman–Norton 对连续物理 runner 与 supertask 的正控制

> **身份：** `CORE_ADEQUACY_SOURCE_AUDIT / PHYSICAL_MODEL_BRIDGE_CONTROL / NOT_A_BARE_ZFC_VERDICT`。
>
> **TaskCard：** [C0 successor reselection 003](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0-SUCCESSOR-RESELECTION-003-TASKCARD.md)。
>
> **冻结原件：** [Earman–Norton 1996 snapshot](../sources/external/zfc-meta-subtheory-c0r4-earman-norton-20261005/README.md)。

## 1. 为什么这个来源有资格进入 F-A

它不是又一篇“几何级数有有限和”的说明。它明确谈物理跑者、Newtonian motion、速度／加速度、外力、kinematic/dynamic possibility、理想化球体和终态。因此它能够检验当前问题中真正缺失的那一段：一个连续数学描述何时被物理理论接到“该过程完成”的判词。

原件 PDF pp. 2–4（printed pp. 232–237）已视觉核验；MinerU OCR 只作定位，不替代原页。

## 2. 字段化合同

| 字段 | Earman–Norton 提供的内容 | 范围与未支付项 |
|---|---|---|
| `M` | Newtonian mechanics 的一致性作为相对前提。 | **不是** bare ZFC，也未给 ZFC-founded semantics。 |
| `S` | 连续时空中的 Newtonian motion；跑者可被表为有速度／加速度与力 `F(t)=ma(t)` 的 trajectory。 | 不是 IEP/Mizar/Isabelle 的同一版本 theorem。 |
| `Q_EN` | 从 A 到 B 的连续 journey；来源讨论其能否完成及其是否可被分析为无穷子行程。 | 不等于 “必须存在最后一个离散操作” 的 strict-Q。 |
| `OriginDone_EN` | “complete the journey/race from A to B”；该任务在来源中可由连续 journey 或来源指定的物理 setting完成。 | 不是用户尚未固定的所有现实 process contract。 |
| `FormalDone_EN` | 几何／连续模型与 explicit runner construction；在假设的 possible Newtonian world 中，Newton laws “guarantee” runner performs the supertask。 | 是模型内、条件性 payment；不证明 actual world。 |
| `P_EN` | 由 standard resolution与明确的 Newtonian model 从无穷子行程描述到 journey completion。 | 只适用于该来源的 Q_EN / physics 假设。 |
| `Bridge_EN` | 物理动力学：continuity、velocity、acceleration、force law、possible Newtonian world。 | 支付的是这一物理模型桥，不是 ZFC 对所有 subtheory 的 adequacy duty。 |
| `Adequacy` | 作者明确只给相对 consistency；某些附加要求会令相应 supertask kinematically/dynamically impossible；理想化 ball 不声称在实际世界实现。 | actual-world applicability与bare-ZFC责任仍未支付。 |

## 3. 原件实际说了什么

1. **没有最后一个 act 与不能完成全部 acts 不是同一件事。** §2 区分 two senses of “incompletable”：无限序列没有可指认的最后 act，但这不蕴含不能 carry out totality of acts。该区别直接拒绝把 `NoLastAct` 自动当成 `¬ OriginDone_EN`。

2. **连续旅程的任务合同可以不同于离散动作合同。** 作者引用 Benacerraf 对连续、不中断的 A→B journey 的描述，并把“无穷 journeys”说成对 single continuous journey 的一种不同描述；若另加物理 distinct acts、finite pauses等条件，则是不同的任务规定。

3. **物理 bridge 不是纯极限。** 在一项有递减速度且连续速度／加速度的 staccato construction 中，作者引入 `F(t)=ma(t)`，只在某个 possible Newtonian world 的条件下说 Newton laws guarantee runner performs a supertask。其结论被明示限制为相对于 Newtonian mechanics 无内部矛盾的 relative consistency result。

4. **同一个有限时间结构不自动保证全部过程模型。** 作者同时给出 flags/terminal instant 的 kinematic/dynamic impossibility，并把 bouncing ball的无限 bounce model限定为idealized、非 actual ball；这保留了 `Control−`，阻止“任何几何级数收敛就有物理完成”的偷换。

## 4. 判词

```text
F_A_PHYSICAL_MODEL_BRIDGE_POSITIVE_CONTROL_WITH_SCOPE
CONTINUOUS_JOURNEY_COMPLETION_IS_SOURCE_SUPPORTED_IN_A_CONDITIONAL_NEWTONIAN_MODEL
NO_LAST_ACT_DOES_NOT_BY_ITSELF_ENTAIL_NOT_ORIGINDONE_FOR_Q_EN
ACTUAL_WORLD_PAYMENT_UNPAID
ZFC_FOUNDATION_LINK_UNPAID
DIFFERENT_TASK_CONTROL_REQUIRED_FOR_STRICT_LAST_ACTION_Q
NO_BARE_ZFC_OBJECT_LANGUAGE_CONTRADICTION
```

它对当前研究的重要作用是双面的：它证明“过程 bridge”并不只是项目自造偏好，因为一篇物理／数学物理来源会显式交代它；同时它阻止我们把 `NoLastAct` 作为对所有连续运动任务的无条件反证。

## 5. 对 C6 的影响

这不是 core contract：`M` 是 Newtonian mechanics 而不是 ZFC 或明确 ZFC-founded foundation，`Q_EN` 也不是已支付的 strict-Q/H0 SameFullQ。因此不能进入 C6，也不能作为 bare ZFC 的 failure 或 defense。

它确实关闭一个更窄的错误路径：**不能再声称所有连续物理模型都只用极限偷换了过程完成。** 一个实际物理 model 可以明示其 `OriginDone`、dynamics和条件性 bridge；要批评它，必须在同一 model/task contract上展示未付义务或矛盾。

## 6. controls、停止与 successor

| 项 | 内容 |
|---|---|
| `Control+` | Earman–Norton 的 possible Newtonian runner / `F(t)=ma(t)`；连续 journey与super task completion在该假设下获得source-level payment。 |
| `Control−` | staccato+flag导致terminal instant的无限 discontinuity；idealized bouncing ball不等于 actual ball。 |
| 最强反证条件 | 同一来源若否认其物理 bridge、或原页显示其只谈纯数学而非Newtonian process，则本卡失效。原页复核不支持该反证。 |
| local stop | F-A 已得到一个明确 physics-model bridge positive control，而非同一 ZFC core M。 |
| successor | 进入 `F-C direct-M duty`：只寻找 foundation source 是否明确把这种 physical-process bridge 审计列为 set-theoretic foundation 自身职责；不得把本 Newtonian control重命名为 ZFC contract。 |

## 7. 禁止外推

- 不证明现实世界或标准模型实际允许这种 runner／ball；
- 不证明所有 supertasks 可完成，或连续时间必然允许任意无穷离散过程；
- 不证明极限理论已经、或没有，解决用户所定义的芝诺／圆环任务；
- 不证明 bare ZFC 已具备、缺失或拒绝过程完成观察力；
- 不证明 HoTT 的 Q 与本卡任务相同。
