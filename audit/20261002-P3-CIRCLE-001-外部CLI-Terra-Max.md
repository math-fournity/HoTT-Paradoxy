# P3-CIRCLE-001：外部 Codex CLI 原对象／repair 语义边界盲测

> **身份：** `EXTERNAL_CLI_BEHAVIOR_PROBE / P3_SOURCE_CONTRACT_BOUNDARY / NOT_A_MATHEMATICAL_RESULT`。
>
> **结论：** `CONSTRUCTION_SEMANTICS_NOT_SUPPLIED`。在给定 origin package、weak Done／strong Done 区分但没有 repair transition 的条件下，独立 Terra / Max 实例拒绝伪造 P3 状态机，并给出最小证据缺口。

## 运行身份

| 字段 | 记录 |
|---|---|
| CLI | `codex-cli 0.157.0` |
| 工作根 | `/tmp/pattern-p-forge-p3-circle` |
| 模型请求 / effort | `gpt-5.6-terra` / `max` |
| sandbox / approval | `read-only` / `never` |
| session | `01a0fcac-51d5-7da1-b10b-52b3cfa4a9c3` |
| prompt | `PROMPT.md`；无项目读取、网络、命令和历史名称 |

## 输出

代理判定：admission-order state machine 和 completion-process state machine 均未 supplied。它要求六类最小补充：

1. 含 `C,p,M,N`、边界、逼近表示与 preservation observations 的 state record；
2. 缺失点／来源数据的 pending、recognition、admission predicate；
3. repair operation 的 relation/function、输入条件、非确定性与输出观察；
4. reconnection 的必要充分 guard 与后继 boundary state；
5. weak Done 与 strong Done 的明确 terminal predicate；
6. P3 labels 间的 allowed transitions、guards 和 terminal ordering evidence。

它明确区分：紧化或空间等价定理本身不能提供这些 process semantics，也不能自动证明 repair procedure 的完成或阻断。

## Master 判词

PASS。P3 的正确行为正是：在没有 transition／guard 时输出 `CONSTRUCTION_SEMANTICS_NOT_SUPPLIED`，而不是把圆环用户原案改写成一个未经来源支持的 state machine。该结果形成 P3 对圆环的第一份来源边界收据；它不是圆环原案的否定、证明或结案。
