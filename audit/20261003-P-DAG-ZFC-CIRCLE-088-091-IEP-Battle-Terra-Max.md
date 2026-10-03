# P-DAG H088–H091：IEP 的模型付款、Done 改写与同一任务 Battle

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / BOUNDED_BATTLE / SOURCE_DONE_REPLACEMENT_EXPLICIT / PAYMENT_PARTIAL / SAME_TASK_IDENTITY_NOT_PROVED / NOT_A_ZFC_INCONSISTENCY_OR_FINAL_Q`。

## 1. Battle 的真实问题

H087找到了 IEP 的实际来源链。它造成的不是“谁说得更有说服力”的分歧，而是一个精确字段分歧：

```text
IEP 是否已经以连续时间、实分析、ZFC基础和数学物理成功
充分支付了“同一原过程已经完成”的桥？

还是它只支付了一个新的模型完成契约，尚未证明该契约保持
研究发起人所固定的强 Done_origin？
```

H088作付款辩护，H089作同一任务缺口挑战，H090按来源字段而非投票裁决。H091随后加入此前窄摘录遗漏的原文，修正Battle的Done字段。

## 2. 输入合同的两次失败与修复

这两次失败没有被计作来源或理论证据：

| 轮次 | 事实 | 处置 |
|---|---|---|
| preflight | H088/H089的角色句没有运行器所要求的精确`You are a P-VALIDATION source mapper.`标记。 | `INPUT_CONTRACT_FAILURE / NO_AGENT_OUTPUT`；修正payload，以新run ID重启。 |
| R1 | 模型正常完成、零工具，但prompt要求`B0–B6`，runner的source-match合同要求`E0–E7`。 | `FAIL_OUTPUT_OR_TOOL_CONTRACT`；两份R1文本不用作Battle证据，NodeCard与payload同改为`E0–E7`，以R2重跑。 |

这正是一次有价值的调度收据：Battle的论点质量不能补救输出schema不合格，Master没有把看似合理的R1文字偷录为证据。

## 3. R2 的两种公开读法

### H088：付款辩护

H088承认IEP**不是仅说“极限存在”**。它明确给出：实数时间和位置、线性连续统、连续／可微运动、微积分对无穷分割路径的处理、ZFC-with-Choice作为实分析的基础，以及数学物理在时间和运动上的成功。它把这识别为：

```text
real analysis → continuous-motion representation → calculus treatment
→ Achilles goal-arrival claim
```

因此H088判P1／模型表示通过，P2／模型内微积分到到达路径通过，P3-C为`QUALIFIED PASS`。它同时明确让步：IEP的窄摘录没有端点完成谓词、观测准则或独立的`Done`测量条件。

### H089：同一任务缺口挑战

H089不否定上述付款。它把缺口写为五个可以被补证或反驳的字段：

1. 特定 Achilles 原任务到连续模型的表示关系；
2. 哪个模型事实是该任务的可操作完成条件；
3. 到达与未到达的观察／测量准则；
4. `Done(run, goal, time)`式的任务索引谓词；
5. 模型到达保持该同一任务Done的transport／preservation条件。

它的判词是：IEP对模型与其可用性付了钱，但没有在窄摘录中明示这些同一任务字段；这只是`OMISSION_CANDIDATE`，不说明桥不可能或模型错误。

## 4. H090 独立裁决：窄摘录的正确分类

H090只读冻结来源事实与两份公开case，给出逐字段裁决：

| 字段 | H090 判词 |
|---|---|
| 实数时间／位置、连续运动、微积分处理 | `PAID` |
| IEP报告的模型内到达声明 | `PAID_AS_REPORTED_MODEL_LEVEL_CLAIM` |
| ZFC-with-Choice | `PAID_AS_FOUNDATION_CONTEXT`，不是关于特定跑者的ZFC定理 |
| 数学物理成功 | `PAID_AS_SUPPORTING_CONTEXT`，不是单独物理证明 |
| 同一任务表示、操作性端点、观察规则、任务Done、保持条件 | `UNPAID_IN_NARROW_RECORD` |

所以H090给出：

```text
IEP narrow extract: PAYMENT_PARTIAL
same-task Done lift: unpaid in that frozen record
```

这不是多数投票结果：H088和H089在模型付款上实际一致；分歧被准确拆成“模型侧付款”与“同一任务Done保持”两种不同主张。

## 5. H091 的来源扩展：全文明示Done替换，必须修正H090

紧接着读取同页的相关段落发现，IEP不只是遗漏了最后一步条件。它明确问“没有最后一步，旅行如何完成”，然后说 Standard Solution 的回答是“旅行不需要最后一步”，并把拒绝反对直觉列为接受该方案的代价。它还保留关于super task、任务定义、limit state和构成性替代的争论。

H091的来源匹配判词是：

| 问题 | H091判词 |
|---|---|
| IEP是否明确替换最后一步Done？ | **是。**`SOURCE_DONE_REPLACEMENT_EXPLICIT`。 |
| IEP是否证明新的Done与研究发起人的强`Done_origin`相同？ | **否。**没有等价／保持证明。 |
| IEP的ZFC措辞是什么？ | **Foundation/context claim**：实分析的基础、对芝诺的间接解决，不是特定跑者的ZFC定理。 |

因此H090的“窄摘录未给Done clause”被标为**对原摘录过时**；其余关于同一任务身份／观察保持尚未证明的字段仍然有效。

## 6. 与新的 Lean 控制的会合

H091的源事实刚好让新 Lean 定理有了清楚的解释边界。`MP-ZFC-GEOMETRIC-COMPLETION-001`现在证明：

```text
¬ (limitOutcomeDone ↔ finalStageDone)
```

对固定的几何级数模型，`limitOutcomeDone`是数列趋于端点，`finalStageDone`是某个自然数阶段到达端点。该定理不是关于连续物理运动的全面结论；它只证明：**若来源把“需要最终阶段”的条件改名为“有极限结果”，这两个明确谓词本身没有被证明等价。**

这正好解释H091为何是`Done replacement`，而不是同一任务保持的定理。若IEP的连续时间模型要主张仍是同一个完成条件，就必须另给它自己的endpoint／observation／preservation桥；若它承认是新的完成定义，则它解决的是改写后的任务。

## 7. Master 结论：现在真正找到的是什么

现在可以把研究发起人的路线精确地写成一个**来源驱动的候选问题**：

> IEP把 ZFC-supported real analysis 作为 Standard Solution 的基础，并用连续模型和微积分宣布跑者到达；当“没有最后一步”显现时，它明示放弃“完成必须有最后一步”的条件。这个被替换的完成条件与原过程的强`Done_origin`凭什么仍是同一任务？

这不是 ZFC 的形式矛盾，也不是“ZFC完全不能观察时间”。它是已定位到的`Q_BRIDGE_CANDIDATE`：**ZFC支持的标准解在一个真实来源中通过明确重写完成条件来得到解答；其与原过程完成的同一性仍缺一条来源内保持桥。**

更精确的当前状态是：

```text
ACTUAL_C_FOUND
SOURCE_DONE_REPLACEMENT_EXPLICIT
MODEL_PAYMENT_VISIBLE
FORMAL_NON_EQUIV_CONTROL_AVAILABLE
SAME_TASK_IDENTITY_NOT_PROVED
ZFC_Q_LOCATED = NO
```

这个状态比“没有来源”前进了一大步：未来不再盲找 ZFC 的漏洞，而是要检验一条已出现的、公开的 `ZFC foundation → Standard Solution → Done replacement → resolution` 责任链。

## 8. TrajectoryReceipt

成功的R2/H090/H091节点均由canonical `session_trajectory.py`按`catalog → tree → search → coverage`复核为单session、单turn、正常`completed`；runner收据与trajectory都记录零command、零fileChange、零approval。事件数分别为H088=992、H089=1068、H090=1114、H091=1114。

所有节点的L1都保持`NOT_FULLY_CERTIFIED`：隔离runner的prompt gate通过，但private wire不包含完整AGENTS正文。L2是`NOT_OBSERVED_EXPECTED`，因为source-match明令禁止tools且零工具得到双重记录；L3不是fresh-recall测试；L4由Master按冻结来源与formal controls回审；L5仅在该节点的模型、权限、payload、schema和终态范围内接受。没有从加密reasoning重建任何论证。
