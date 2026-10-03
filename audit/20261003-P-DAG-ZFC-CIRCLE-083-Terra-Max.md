# P-DAG H083：SEP *Supertasks* 的 Zeno completion LiftClaim 审计

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / SOURCE_MATCH_VALIDATION / SOURCE_TASK_CONTRACT_SPLIT / Q_NARROW / NOT_A_ZFC_Q_OR_MATHEMATICAL_THEOREM`。
>
> **节点：** `P-DAG-SOURCE-083-ZFC-CIRCLE-SUPERTASK-LIFTCLAIM`。
>
> **范围：** 审一份版本固定的实际来源是否将实数拓扑中的极限结果无条件升级为芝诺过程的原始强 Done；不证明 ZFC、极限理论、现实物理或圆环原案的数学结论。

## 1. 为什么这一来源是下一张卡

`ZFC-CIRCLE-Q0/Q1`在 H076–H082 后只允许寻找一个实际的 `LiftClaim`：有来源把数学的 `Done_formal` 说成原运动／圆环的 `Done_origin`，并让我们检查对象、operation、observation与Done是否仍是同一任务。

SEP 的[*Supertasks*](https://plato.stanford.edu/entries/spacetime-supertasks/) 是一个合格的来源入口。它在第 1.1 节把 Zeno Dichotomy 明确写成没有 final step 的 task；又以标准实数拓扑中几何级数收敛为 1 来解释 Achilles 怎样完成 supertask，并明确说 Achilles “actually does complete all of the supertask steps in the limit”。它因而提供了真正的 `C`，而不是仅有一条极限公式。

但同一段紧接着区分两种 `complete`：

```text
Done_final_action = 执行一个最终动作
Done_every_step   = 完成每一个步骤
```

来源说 Dichotomy 不能在第一种意义完成、能在第二种意义完成，并承认两种意义只在有限任务中等价；它还保留“标准拓扑是否合适”以及连续 Zeno run 与通常离散 machine task 的差异。这个显式区分是本卡的决定性事实。

## 2. 冻结 TaskCard

| 字段 | 冻结内容 |
|---|---|
| `T_meta` | ZFC 支撑的经典实分析背景；SEP 本身没有把它命名为 ZFC，故不预设 ZFC 层消费者。 |
| `T_sub` | 实数标准拓扑与几何级数收敛。 |
| `u/F` | 半程距离的 partial sums 及其收敛到 1 的极限。 |
| `C` | SEP 对 Achilles 完成 supertask 的显式断言。 |
| `I/Op` | Achilles 连续执行递减的半距离步骤。 |
| `O` | 无 final step、是否执行了 every step、拓扑选择、连续／离散差异。 |
| `Done_formal` | 级数在实数标准拓扑中收敛到 1。 |
| `Done_origin` | 用户圆环／顺序过程所要求的强 Done。 |
| `Q?` | 该来源是否无付款地把 `Done_formal` 交付为 `Done_origin`。 |

NodeCard 与冻结 prompt 分别见[NodeCard](20261003-P-DAG-ZFC-CIRCLE-083-NODECARD.md)和[payload](20261003-P-DAG-ZFC-CIRCLE-083-PROMPT.md)。

## 3. H083 运行事实

| 字段 | 记录 |
|---|---|
| actor | `gpt-5.6-terra / max`；`thread/start`回显模型、effort、readOnly与network关闭。 |
| profile | `source-match`；唯一用户输入是冻结来源卡。 |
| method repo | `/Users/aurolafly/.codex-experiments/method-repo-h081`，启动前 clean。 |
| private root | 项目根外的`/Users/aurolafly/.codex-experiments/pattern-p-h083-zfc-supertask`。 |
| prompt-input gate | `PASS`；唯一 fenced text、`P-VALIDATION` marker与frozen-card边界均通过。 |
| terminal | thread `01a103c1-303c-7cf0-8b6e-bea1e1e1095f`；turn `01a103c1-3158-7771-8d62-d4e5bc23ffde`；正常 `completed`。 |
| output | E0–E7齐备，822 words，SHA-256 `affccadf6fb8e673f703f276d1b87588b905ad9827399ec4a983e712542e93da`。 |
| side effects | `command=0`、`file_change=0`、`approval_request=0`；76.743秒自然完成，无自动墙钟中断。 |

私有 wire、认证借用收据和完整终态仅保存于隔离目录；本报告不复制认证内容、完整运行期指令或加密 reasoning。

## 4. 来源与 Terra/Max MatchTrace 的共同结论

### P1：有真实消费者，却没有未付款的强 Done

SEP 给出了来源定义的 `C/I/O/Done`：它有明确 completion claim、半程任务、无 final step 的观察，以及两种非等价 Done。它因此比 H076 的仅 formation 来源更强。

但它没有把这两种 Done 偷偷等同。来源只在 `Done_every_step` 意义下将 completion 赋给 Achilles；对 `Done_final_action` 明确作否定。用户的更强 `Done_origin`与该第二种 Done 是否相同，来源没有无条件给出。因此判为：

```text
ACTUAL_C_LANE_SOURCE
SOURCE_DONE_DISTINCTION_PAYMENT
SOURCE_TASK_CONTRACT_SPLIT
NOT_AN_UNPAID_DONE_ORIGIN_LIFT
```

### P2：不适用

无 final step、无穷多 stages 或理论层次并不构成同一对象的 `bind/form/bridge/reenter`。H083没有发现可交给 P2 的罗素式 reentry，正确判词为 `NOT_APPLICABLE`。

### P3-C：来源把付款写出来了

| ConstructionBridgeCard 字段 | H083来源中的内容 |
|---|---|
| Representation | partial sums／standard real topology 表示半程距离。 |
| Operation | Achilles 连续执行逐步缩短的半距离移动。 |
| Observation | 无 final step；every-step reading；拓扑适合性；continuous/discrete 区分。 |
| Done | convergence=1；在 final-action 意义中不完成；在 every-step 意义中完成。 |
| LiftClaim | “Achilles actually does complete all of the supertask steps in the limit”。 |
| Payment | 明示 two meanings of complete、拓扑疑问与连续／离散限制。 |

因此 SEP 并未为物理／历史保持的`Done_origin`给出普遍 bridge；但它清楚支付了自己采用的 qualified `Done_every_step`。这与 Norton 的显式 `Done_strict → Done_revised`控制同方向，而不是新的未付款 LiftClaim。

## 5. Master verdict 与 QConvergenceLink

```text
Target-Q     = 来源未付的 Done_formal → Done_origin 提升
Candidate-Q  = ZFC-CIRCLE-Q0/Q1
Control-Q    = SEP 的显式双 Done、拓扑资格、连续/离散差异、Norton、C-269/C-272
effect       = Q_NARROW
global state = Q-1_SEED (unchanged)
P2           = NOT_APPLICABLE
P3-C          = SOURCE_TASK_CONTRACT_SPLIT / PAYMENT_VISIBLE
ZFC_Q_LOCATED / UR / P4 / station switch = no / no / no / no
```

这张卡排除了一种很诱人的粗叙述：“现代数学一说极限收敛，就把没有 final step 的原过程直接宣布为已完成。”至少 SEP 的实际文字不是这样工作。它在结论中公开修改／区分了完成条件，并留下拓扑与连续性限制。

它也没有形成 Q1 所需的 `Z_meta`：SEP 没有把 ZFC 的基础地位、模型或一致性提升为原过程的充分认证。因此 H083是`SOURCE_LIFTCLAIM_FOUND_BUT_EXPLICITLY_PAID_CONTROL`，不是“ZFC 放过子理论”的证据。

## 6. TrajectoryReceipt

canonical `session_trajectory.py` 已按 `catalog → tree → scan → search → coverage`审读 private bidirectional App Server wire：一个session、一个turn、1,333 events、thread/turn身份与终态均闭合。原始 locator 留在私有 wire；不从 encrypted reasoning 重建思维链。

| 层 | 判词 | 范围 |
|---|---|---|
| L1 context injection | `NOT_FULLY_CERTIFIED` | wire回显两个隔离AGENTS路径，但coverage无法取得完整正文；路径回显不被写成完整注入。 |
| L2 selected read | `NOT_OBSERVED_EXPECTED` | source-match NodeCard禁止tools；wire、runner与行为收据都记录零tool。 |
| L3 model recall | `NOT_TESTED` | 本节点不是fresh recall实验。 |
| L4 cognition execution | `MASTER_REVIEWED_WITH_SCOPE` | 输出维持冻结TaskCard、未伪造P2或ZFC／物理结论，且按E0–E7分层。 |
| L5 behavior verdict | `NODE_ACCEPTED_WITH_SCOPE` | model/effort/权限回显、prompt gate、completed terminal、output schema与零副作用都通过；只验证本source-match节点。 |

## 7. 下一行动与停止边界

H083完成了 `SOURCE_LIFTCLAIM_CONSUMER_SEARCH` 的第一张真正实际 completion-claim 来源卡，但它只形成了一个付款控制。后续不应重复“Zeno + geometric series”文本；下一来源必须改变以下至少一个事实：

1. 明确将其强 Done 与原 `Done_origin`同一化，且没有 SEP/Norton 式支付；或
2. 明确将 ZFC／集合论元理论的模型、语义或一致性结论提升为 `H0_process`／原过程已经解决；或
3. 直接反驳本卡的 payment，说明双 Done 在同一原任务中本应等价。

若后续来源继续显式区分Done、只给模型／一致性、或明确提供 endpoint／保持关系，则收为进一步的`SOURCE_BRIDGE_DEFENSE`，而不无限扩张同类检索。

本贡献尚未进入 canonical `dev` current owner。当前 canonical target 已在本次运行后推进，且其工作树仍有未闭合写入；任何接受、择取、rebase或current-state更新应由该目标的唯一 integrator 按当时HEAD重新审阅。
