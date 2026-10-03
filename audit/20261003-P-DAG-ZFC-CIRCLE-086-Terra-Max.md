# P-DAG H086：ZFC 圆环“观察力不完备”机器证明的范围反控制

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / FORMAL_SCOPE_CONTROL / Q_CAPABILITY_CALIBRATION / Q_NARROW / NOT_A_ZFC_Q_OR_MATHEMATICAL_THEOREM_ABOUT_ZFC`。
>
> **节点：** `P-DAG-CONTROL-086-ZFC-CIRCLE-OBSERVATION-FORMAL-SCOPE`。
>
> **范围：** 审核两组已接受 Lean 定理能够支持的归因范围；不搜索新的 ZFC 来源，不形成 ZFC 的数学结论，也不替原过程指定 `Done_origin`。

## 1. 为什么需要这张控制卡

本轮新增了两类机器结果：

1. `MP-ZFC-OBSERVATION-BOUNDARY-001`把“粗观察合并 Done 异值状态时，无法只经该观察判定 Done”写成一般逻辑定理，并把相对概念命名为`CompletionObservationIncomplete observe done`；
2. `MP-ZFC-GEOMETRIC-COMPLETION-001`对` s(n)=1-(1/2)^n `证明：每个自然数阶段严格小于`1`、没有阶段等于`1`，但该数列在实数通常拓扑中趋于`1`，从而`hasLimitOutcome`不蕴含`hasFiniteStageEndpoint`。

它们很接近研究发起人的直觉，却仍可能被过度解释成“ZFC 已被证明缺少时间维度”。H086把**只有上述冻结形式卡**交给一个隔离的 Terra/Max，并要求它逐项说明：若要把该候选归因落到一个实际 ZFC 接口，究竟还缺什么。

NodeCard 与冻结payload分别见[NodeCard](20261003-P-DAG-ZFC-CIRCLE-086-NODECARD.md)和[payload](20261003-P-DAG-ZFC-CIRCLE-086-PROMPT.md)。

## 2. 运行事实

| 字段 | 记录 |
|---|---|
| actor | `gpt-5.6-terra / max`；`thread/start`回显模型、effort、read-only permission profile和`approvalPolicy=never`。 |
| profile | `source-match`；唯一模型输入是冻结形式卡。 |
| isolation | 项目根外的`/Users/aurolafly/.codex-experiments/pattern-p-h086-zfc-formal-scope`；worker无工具、文件、web、Git或delegation许可。 |
| terminal | thread `01a103e3-234e-7f72-851f-d5d2f3055b70`；turn `01a103e3-241c-7d63-8819-e841c61612ae`；正常`completed`。 |
| output | E0–E7齐备，818 words，SHA-256 `8c3f7b9ce79ea037c76db3edffad1c24ed027b12748688c6c1da545c4d56c010`。 |
| side effects | `command=0`、`file_change=0`、`approval_request=0`；约99.086秒自然完成；无自动墙钟中断。 |
| input gate | `PASS`：唯一fenced payload、`P-VALIDATION` marker和frozen-source边界均通过。 |

私有wire、认证借用收据和运行期环境不进入项目提交；本报告只保留可审计的公开输出摘要、身份、hash和分层轨迹结论。

## 3. Terra/Max 的公开 MatchTrace：它如何定位证据边界

### E0–E2：两组已证明事实各自说了什么

Terra 将 Card A 读为**条件性观察不足定理**：只有当一个指定的`observe`确实把已完成与未完成状态压成同一输出时，才不能从该输出判定指定的`done`。加入terminal-event字段的正控制说明，问题在于那一个粗接口遗漏了区分字段，不在于所有表示都必然失败。

它将 Card B 读为**有限阶段与拓扑极限的严格分离**：对指定几何序列，趋于`1`不等于某个自然数编号阶段到达`1`。它明确保留了关键限制：这不决定一个连续时间端点上的物理或哲学过程是否已经完成。

### E3–E4：为什么这还不是 ZFC 的实际消费者

worker按冻结卡复述：`T_meta`只是“可能的 ZFC-supported classical-analysis interface”，`C = none`。因此目前没有源定义的 ZFC consumer、没有具体 ZFC 公式／子理论接口、没有已固定的原过程状态空间，也没有将原过程历史映射到数学观察的来源内桥。

它将目前的对应关系写成：

```text
Done_formal = hasLimitOutcome / formalCompletion
Done_origin = 必须独立固定的原过程完成条件
```

冻结结果没有等同二者。此项正是“有限阶段到达”与“连续端点完成”不能被悄悄并成一个`Done`的地方。

### E5：三把刀的具体判词

| 刀具 | H086 的公开判词 | 含义 |
|---|---|---|
| P1 | `SOURCE_CONSUMER_GAP` | 没有实际`C/I/O/Done`消费者；不得从“ZFC可能支撑该分析”凭空造出使用者。 |
| P2 | `NOT_APPLICABLE` | 冻结卡没有同一对象的 bind/form/bridge/reenter；极限或无限阶段不能代替罗素式再入。 |
| P3-C | `BRIDGE_REQUIRED` | 未来必须给出同一原过程到形式接口的桥，并逐项交代对象、输入、operation、observation、Done和payment。 |

Terra特别列出未来桥必须补的六项：命名的ZFC-supported interface；同一对象的历史映射；独立的`Done_origin`；有限阶段和连续端点两种完成条件的区分；实际的Done异值观察碰撞或等价不可因子化证明；以及把结论限制在该接口而非裸 ZFC 的范围。

### E6–E7：反控制改变了什么

如果观察中加入 Card A 的terminal-event字段，toy Done可被判定。因此，未来即使找到观察不足，也必须针对**那个实际的粗观察接口**，不能因“使用了 ZFC”或“存在一个极限”一概推出。

这与 Master 的解释一致：本轮机器证据把“时间维度”压缩成一个可反驳问题——某接口是否忘掉了原完成条件所需的历史／端点字段——但尚未把这种接口实证为 ZFC 的实际理论责任。

## 4. TrajectoryReceipt

canonical `session_trajectory.py`按`catalog → tree → scan/search → tail → coverage`审读 private bidirectional App Server wire：一个 session、一个 turn、1230个事件；`turn_completed`在wire locator `:1240`，且为`completed`、无错误。公开终态、runner行为收据和trajectory的零工具结果一致。

| 层 | 判词 | 范围 |
|---|---|---|
| L1 context injection | `NOT_FULLY_CERTIFIED` | runner的prompt-input gate确认隔离worker contract和冻结payload，但wire coverage不含两个AGENTS正文，不能把路径／运行器准备冒充完整上下文注入。 |
| L2 selected read | `NOT_OBSERVED_EXPECTED` | source-match NodeCard禁止tools；wire search、runner计数与行为收据均为零tool。 |
| L3 model recall | `NOT_TESTED` | 这不是fresh-recall或盲理论定位实验，而是冻结形式卡的范围控制。 |
| L4 cognition execution | `MASTER_REVIEWED_WITH_SCOPE` | 输出保持`C=none`、未伪造P2、未把连续端点折叠成有限阶段、未称ZFC不一致或Q已会合。 |
| L5 behavior verdict | `NODE_ACCEPTED_WITH_SCOPE` | exact model/effort/权限回显、payload gate、E0–E7 schema、自然终态与零副作用均通过；只说明这个受控scope判断，不说明任何更广泛的模型能力。 |

## 5. Master 裁决与对后续工作的影响

```text
Target-Q      = 实际的未付款 Done_formal → Done_origin 提升
Candidate-Q   = ZFC-CIRCLE-Q0/Q1
Control-Q     = H086形式范围反控制
effect        = Q_NARROW / Q_SAFETY_REPAIR
global state  = Q-1_SEED（不变）
P2            = NOT_APPLICABLE
P3-C           = completion-observation adequacy 作为桥的可检验判据
ZFC_Q_LOCATED / UR / P4 / 新刀 = no / no / no / no
```

H086没有把工作停在“还缺来源”这一句话。它精确给出了下一张合格卡的判据：必须找到一个版本固定的、实际将`T_sub`输出交付为原过程解答的来源／接口；然后用同一过程的两个历史或等价的因子化失败，检验它是否丢掉了`Done_origin`所需的字段。若来源有显式bridge、改Done、或保留完整观察，那个来源就是付款／反控制，不能用来指控 ZFC。

因此这张卡既保护了研究发起人的核心直觉，也防止机器证明被过度外推。它让“ZFC在时间维度上的理论观察力不完备”成为一条可以被实际接口、反例和支付桥推翻的研究命题，而不是一句无法审计的总评语。
