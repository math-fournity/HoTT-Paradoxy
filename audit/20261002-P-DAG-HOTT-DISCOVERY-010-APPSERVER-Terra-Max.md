# P-DAG-HOTT-DISCOVERY-010：脱敏询问过程的隔离 App Server 发现收据

> **身份：** `BLIND_DISCOVERY_EXECUTION_OBSERVATION / PROCESS_SHAPE_MODEL_RECALL_SITE_CANDIDATE / NOT_A_HOTT_RESULT`。

## 1. 冻结身份与运行边界

| 项 | 值 |
|---|---|
| NodeCard | [HOTT-DISCOVERY-010 NodeCard](20261002-P-DAG-HOTT-DISCOVERY-010-APPSERVER-NODECARD.md) |
| Parent | H009 的 pre-auth prompt-wrapper failure；H010只修正 fenced payload 的传送方式 |
| Runner | `scripts/pattern_p_appserver_blind_discovery.py`，SHA-256 `95f720e50fd1ce05d68bff56e0a53e7fad5e23179fc6c560dc2cc4bc4d9b1b09` |
| Fenced payload | 2425 bytes，SHA-256 `9eaf50c72bb9d42b4b9a57c07f50ed36c15fcd29776814ffdbb346d190dfcdec` |
| Actor | requested/echoed `gpt-5.6-terra / max`；fallback=false |
| Environment | isolated text-only cwd、`governance-regression-fresh`、read-only、network=false、`approvalPolicy=never` |
| Terminal | `completed`，91.081 seconds；public final 1772 bytes / 249 words / SHA-256 `c7dbe3267518370089ea975cf06e888b2b302d46211902323b95caa29f69e890` |
| Side effects | command=0、file-change=0、approval-request=0；post-auth permission gate=`PASS`，borrowed auth已清理 |

prompt-input gate=`PASS`，其项目根、过程实现名、既有 `never`／universe 答案、Power Set、ZFC和 Pattern-P
标记的排除项全部为 true。原始 prompt-input、wire、stderr、final和home receipt保持私有。

## 2. 终态 trajectory 收据

H010 是新 SOP 下第一张预先声明 `TrajectoryReceipt` 的 NodeCard。当前 shared reader 将其 private direct
wire识别为 `codex-app-server-wire`：562 records、210698 bytes、SHA-256
`494335282ec23524f947f239fc74bb6445f4ac084591dec835c294cd75270db9`，其中4 outbound、558 inbound。

| 可观察项 | 结果 |
|---|---|
| identity | one thread `01a0fe1e-c951-7712-996f-a79128082348`、one terminal turn `01a0fe1e-ca17-7f11-a45d-8c39de736043` |
| terminal | `turn_completed=1` |
| tools / approvals | `tool_call=0`、`tool_result=0`、`approval_request=0` |
| visible output transport | `assistant_message=1`、`assistant_message_delta=477` |
| reasoning visibility | `reasoning` summary item=8、summary delta=23；完整 reasoning=`OPAQUE/UNAVAILABLE` |
| persisted rollout | 0；状态=`PERSISTED_ROLLOUT_UNAVAILABLE / BIDIRECTIONAL_APP_SERVER_WIRE_AVAILABLE` |
| private extracts | user=2 events, SHA-256 `0e972991f7999a6809028b5e16cfc4983161cdbb5f3c499dc0d9771b41ed7c18`; assistant=509 events, SHA-256 `a68da71c07227d49c4b460cc56ebbfb06b1fcf9378f2d54a98de4ff7de358e52`; both mode 0600 |

L1=`NOT_TESTED`（无完整 injected system compare）；L2=`NOT_OBSERVED`（0 tool item不等于完整读取结论）；
L3=`NOT_TESTED`；L4=`REQUIRES_SEMANTIC_REVIEW`；L5=`REQUIRES_ACCEPTANCE_EVIDENCE`。这些状态不能由
自然 terminal、output schema或模型自述升级。

## 3. 公开 D0–D5 DiscoveryTrace

该节点的公开结果筛了三个位置：

1. 固定阶段 `J(k) : Dec(isType(k+1,C))`：通过 `Dec` elimination直接给出 yes/no，故为
   `DISCOVERY_DIRECT_RULE_ANSWER`；
2. 单层 `isType`递归展开：所问的递归条款由显示的方程直接给出，亦为 direct control；
3. `Delay(ℕ)` 的 `now/later`接口：问题是由 `J`驱动的延迟搜索是否会观察到 `now k`、若会则识别 k。
   该接口只给一步观察，不给实际 `J`的分支、命名搜索项、eventual `now`或返回阶段。

模型因此返回：

```text
MODEL_RECALL_SITE_CANDIDATE
u = Delay(ℕ)
F = now/later coinductive observation
Q? = whether repeated observation of the J-driven delayed search ever exposes now k
```

它没有声明 HoTT defect、定理、UR、P2/P3、C/I/O/Done或 ZFC结论。它也没有在盲态中把一般 `C`特化为宇宙 `U`。

## 4. 本节点可支持与不能支持的内容

**可支持：** 在不见项目实现名称、既有答案或原典文件的隔离输入条件下，Terra/Max 依据脱敏的 `J`／`Delay`／
`now/later`画像，定位到了一个延迟询问过程的第一类对象／接口位置，并给出了自身的 D-L5、D-L6和反事实说明。

**不能支持：** 这不等于已重放同一个宇宙特例、已建立真实 consumer、已做 P2/P3、已证明不终止、已给出
现实相对判词，或已通过 HoTT replay release。下一步必须是来源核验：比较这一过程形状与既有 `QuestioningDelay`
源的对象、形成、返回条件与宇宙特例；来源答案不得反写成模型在盲态中已经知道的内容。
