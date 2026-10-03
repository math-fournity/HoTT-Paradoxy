# HOTT-MOTIVE-ZFC：HoTT 创建动机反投影 ZFC 文献调查档案

> **身份：** `PROJECT_ARCHIVE_ROOT / HUMAN_EDITED / PROJECT_DEFINED / RUN_NOT_STARTED`。
>
> **SOP：** [HOTT-MOTIVE-ZFC-SOP](../../dev-docs/HoTT创建动机反投影ZFC文献调查SOP.md)
>
> **路线种子：** [HoTT创建动机反投影ZFC候选路线](../../dev-docs/菲尔兹奖后续理论级目标路线图/009%20-%20HoTT创建动机反投影ZFC候选路线.md)

## 项目边界

本目录是文献调查项目 `HOTT-MOTIVE-ZFC-INVESTIGATION` 的档案根。它保存每次已启动调查的冻结来源分母、
原件与派生阅读材料的身份、R/Z/Q 卡、消费者控制、覆盖收据与 findings；它不保存或替代项目的数学证明资产。

当前状态：**SOP 与档案根已定义，但尚未启动任何调查 run。** 因而这里没有可报告的 HoTT 动机分母、
ZFC 候选、`H0→Z0` 传输判词或文献完成度。

## Run 命名与目录合同

用户在 `/goal` 中引用 `HOTT-MOTIVE-ZFC-SOP` 后，执行者为每次冻结的来源分母建立：

```text
audit/HOTT-MOTIVE-ZFC/YYYYMMDD-HMZ-###-scope/
```

其中 `scope` 是短的、可读的来源范围名。每个 run 至少按 SOP 保存：

```text
MANIFEST.md
SOURCE-CATALOG.md
R-CARDS.md
Z-CARDS.md
Q-CARDS.md
CONSUMER-CONTROLS.md
COVERAGE.md
FINDINGS.md
```

`README.md` 只维护项目级入口和 run registry；不能复制任一 run 的 current findings，也不能把已关闭的
`Q-R`、`SOURCE_PAYMENT` 或 `ANTI_ANALOGY_CONTROL` 自动重开。

## Run registry

| Run ID | 冻结范围 | 状态 | Findings | 备注 |
|---|---|---|---|---|
| — | — | `RUN_NOT_STARTED` | — | 等待用户以 `HOTT-MOTIVE-ZFC-SOP` 启动。 |

## 本次整备的影响边界

| 项目面 | 处置 |
|---|---|
| 用户要求／路线 | `UPDATE`：调用名、来源调查和存档范围已固定。 |
| SOP／Skill／任务路由 | `UPDATE`：项目 Skill、SOP、AGENTS、TASK_ROUTING和SKILL_ROLES已连接。 |
| Archive／证据 | `UPDATE`：档案根、run ID、coverage与原件身份合同已定义。 |
| 外部来源／下载／worker／P-DAG | `NO_RUNTIME_ACTION`：尚未启动任何调查、下载或模型运行。 |
| 数学结论／STATE／Power Set station | `NO_CHANGE`：本项目整备不产生理论候选或数学主张。 |
