# P-DAG-ZFC-SOURCE-025–027：constructible-inner-powerset 来源控制与隔离运行修复

> **身份：** `PRIMARY_SOURCE_CONTROL / CONCRETE_INNER_MODEL_SCOPE / RUNNER_FAILURE_PRESERVED / NOT_A_ZFC_Q_OR_MATHEMATICAL_INCONSISTENCY_RESULT`。

## 1. 冻结来源与问题边界

唯一模型可见来源是 `05-02-07/lean-constructible-universe` 的
`MATHEMATICAL_SCOPE.md`，固定提交
`7f5a7d03d63d9769172f17350bbe8303996e5b53`，SHA-256
`3b8acf8ab9e50ec473ab9793f7fc9060b6e0a135b547b0e9b7925ccb97746cea`。它是一个 Lean
形式化的 concrete `ZFSet`／`LCarrier` 内模型说明，不是任意标准 ZFC 的证明演算，也未经本轮对其 Lean
源码和 kernel run 的独立重放。

卡片冻结：`u = P(a) ∩ L`、`F = PowerSet`、候选 `C` 是有限域 tuple/function-space 的内部化，`Q = UNSET`。
source 说有限域上用 internal Power Set 与 Separation 构造 full ambient finite function space，并用
`FunctionAbsoluteTo`包住这个有限域结果；它同时明确不把 infinite domain 的 internal Power Set 认作 ambient
Power Set，也不声明 bare general function-space formula absolute。

## 2. H025/H026：采样前运行链失败

| Node | 冻结输入 | 可观察结果 | 身份 |
|---|---|---|---|
| H025 | source/prompt 已冻结，experiment root 错放在业务项目 `private-audit/` 下 | `debug prompt-input` 空输出并在加载 AGENTS 时 `Operation not permitted`；无 auth 借用、thread、turn、wire 或模型输出 | `RUNNER_OR_EVIDENCE_FAILURE / NO_AGENT_OUTPUT` |
| H026 | H025 同一 source/prompt；shared method repo已允许读取生成的安全 home `AGENTS.md` | 同一预检仍失败；配置显示 home agents 已 allow，但 experiment root 仍是项目后代 | `RUNNER_OR_EVIDENCE_FAILURE / NO_AGENT_OUTPUT` |

这两次失败不支持“worker 未命中”、来源没有 consumer、P 失效或 ZFC 无问题。它们显示了两个独立运行条件：安全 home 指令要能读；workspace 的祖先目录也不能把业务项目 `AGENTS.md`带进预检。

## 3. H027：外部 experiment root 的同字节重试

H027使用同一来源和同一 prompt（SHA-256
`49c687d02004c491d4a979bdff4c41d23bd14443e27e04f4b95d16879cb277e7`），只改变运行边界：experiment root
位于业务项目根之外；current wrapper 同时拒绝未来 project-descendant root。它获得：

| 运行面 | 观察到的事实 |
|---|---|
| model / effort | `gpt-5.6-terra / max` exact echo |
| cwd / instructions | 外部 text-only workspace；`instructionSources`只列 run-generated home/workspace `AGENTS.md`，完整注入文本仍未取得 |
| permissions | `governance-regression-fresh`、`approval=never`、read-only、network disabled |
| prompt / terminal | prompt-input PASS；自然 terminal；E0–E7 完整 |
| tool boundary | command/file-change/approval 均为 0 |
| liveness | `RUNNING@1.337s → STILL_RUNNING@61.338s → TERMINAL@64.512s`，v2 明示无自动墙钟中断 |
| private trajectory | wire 614 raw records / 604 normalized events，SHA-256 `e58b9782b9c0a403d78466250364ccb82042c0d3ff4d01573efee4daa9f92576`；一个 completed turn、0 tool/result/approval |

trajectory 的 L1 仍为 `NOT_TESTED`，L2为`NOT_OBSERVED`，L4/L5分别需要语义和验收证据；因此不能从成功终态推断完整 context 或隐藏 reasoning。

## 4. P1 的来源受控判词

Terra/Max 的公开 E0–E7 MatchTrace 与冻结 source 相符：

```text
T = concrete LCarrier model layer, not arbitrary standard ZFC
u/F = P(a) ∩ L / PowerSet
C = finite-domain internal tuple/function-space construction
Done = guarded finite-domain FunctionAbsoluteTo result
Q = UNSET
L6/L7 = no surviving formation residual and no affirmative-only Done obligation
```

有限域 guard 是适用范围，不是被 consumer 等待的新对象事实；无限域的一般 formula 没有被 source 认作 absolute，
也不因此变成同层内的 pending Q。该卡的强作用是一个**正面的防线控制**：它示范了“先构造内部图或对象语言
公式、再在内模型里使用”的 source discipline。它没有交给 P2/P3 的 Q，故二者按 DAG 合同不启动。

## 5. 当前边界与下一触发

这第五类来源卡将当前 Power Set 分母扩展为：直接 formation、formal API false-branch、proof/formula层、relative
model comparison、以及 guarded concrete inner-model consumer。五类都没有同层 positive obligation。最强状态仍是：

```text
ZFC_SITE_SELECTED
SOURCE_REPORTED_GUARDED_MODEL_CONSUMER_WITH_SCOPE
Q_UNSET / NO_COMMON_Q / NOT_ZFC_Q_LOCATED
```

后继只能是一张新版本固定的 standard-ZFC 或真实数学使用来源卡，它必须同时给出同层 `C/I/O/Done` 与不能由
formation/false branch 支付的正义务；否则继续开 P2/P3 或宣称 ZFC张力都会违反当前合同。
