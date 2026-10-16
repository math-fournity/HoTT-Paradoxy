# P-DAG-SOURCE-003：Power Set 来源三节点的超时与收据纪律修订

> **身份：** `DYNAMIC_DAG_EXECUTION_FAILURE / NODECARD_TIMEOUT_CONTROL / NOT_A_SOURCE_RESULT`。
>
> **结论：** `TIMEOUT_NO_TERMINAL_OUTPUT / NO_SOURCE_CLAIM / NODECARD_RECEIPT_DISCIPLINE_TIGHTENED`。这次失败不说明 ZFC、Power Set、Cantor 定理或 P3 的任何数学性质；它只说明本轮三个网络来源节点在四分钟观察窗内没有交出可审计的最终输出，因而不能进入 P1/P2/P3 的 source pack。

## 1. 冻结意图与访问边界

Master 在 `P-DAG-SOURCE-002/BATTLE-002` 后冻结了一个更窄的续卡：理论焦点仍是 Power Set；目标层先声明为“数学语义／实际使用层”，proof-system 层仅作对照。三个 fresh Codex CLI 节点均以：

```text
gpt-5.6-terra / max / sandbox=read-only / approval=never
workdir=/tmp / ephemeral / PRIMARY_WEB_SOURCE only
```

启动。它们不得读取项目、Git 分支、先前节点输出或 scratch 文件，不得递归委派或写项目文件。命令行 banner 对 model、effort、sandbox 和 approval 的回显已观察到；这不是对其来源结论或模型能力的一般认证。

| Node | session | 唯一目标 | 到 4 分钟时的状态 |
|---|---|---|---|
| A | `01a0fd5f-0afa-7773-8245-f873a22e49cc` | 找版本固定的 Cantor 型 Power Set 数学消费者，分开 semantic task 与 proof-system acceptance | 无 terminal output |
| B | `01a0fd5f-0abc-7ec2-82f1-fe67d40bfff3` | 在有限的一手 ZF/ZFC／形式化源集中寻找明确 P3 lifecycle/admission transition | 无 terminal output |
| C | `01a0fd5f-0b21-70f0-8a90-7efa8c9ea504` | 独立审计 Cantor 型来源中的 C/I/O/Done 层级和 diagonal-membership Q | 无 terminal output |

三个节点都开始了公开网页检索；没有生成 `-o` 指定的最终文件。Master 没有把途中搜索文字、未完成的浏览动作或模型计划当成 source evidence。

## 2. 超时、停止与证据边界

每个节点在约 4 分 12 秒仍运行。Master 对三个 parent process 发送 `SIGINT`，8 秒后核对：没有相应的 `codex exec` process，`/tmp/hott-p-dag-source-003/` 为空。不存在 close receipt；可观察终态是：

```text
TIMEOUT_NO_TERMINAL_OUTPUT
TERMINATED_BY_MASTER_SIGINT
NO_FINAL_ARTIFACT
NO_USABLE_SOURCE_FACT
```

因此本节点图不会触发 Cantor card 的 P1/P2/P3 映射、Battle 或 Q 审查。它也不能成为“没有这样的 source”的负结论：source set 并未完成可复核的检查，网络检索的中间状态也没有保存为可读 output。

## 3. 由失败驱动的刀具／调度修订

本次运行暴露的不是 P1、P2 或 P3 的数学失败，而是动态 DAG 的收据缺口：启动前只把 NodeCard 放在 Master 的即时执行上下文，未先把一个有 prompt hash、固定 source allowlist、wall-clock deadline 和 partial-output policy 的最小 NodeCard 落入审计收据。以后任何网络或长运行 node 必须在启动**前**保存这些字段；超时后才允许读取／保存终态，且不得从 partial console 推出来源结论。

这一修订增强三把刀的共同使用条件：P1/P2/P3 只有消费已封存、可复核的 source pack。慢或无输出的来源节点只能提供编排层 evidence，不能因其“正在找”而让某把刀临时填充字段。

## 4. 后继条件

下一次尝试不自动重跑这三个泛搜索节点。应选择一个更小、版本已经固定的具体 URL／source file，先写入 NodeCard source allowlist，再给单个 tracer 一个短 deadline。只有该 tracer 返回终态和可核 source locator，才冻结 Cantor 或其它 Power Set consumer card；否则保持 `NO_COMMON_Q / NOT_ZFC_Q_LOCATED`。
