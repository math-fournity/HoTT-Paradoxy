# MP-VERIFICATION-EVENT-001：验证事件与时标边界（导入并项目内重放）

> 来源：另一个 AI 会话 `01a099e9-66ee-7270-8bf9-04f7f1c81e62` 在 repo 外完成；交接说明与原件见
> `audit/imports/verification-event-20260913-01a099e9/`（整树 SHA-256 `56376a96…` 的 170 文件原件包）。
> 本文只陈述**本 repo 当前机器结果**；外部原件的历史身份见导入目录。

## 1. 精确命题范围

固定有限验证事件模型：

- `Stage` 只有 `initial`、`afterP`、`afterHistory`；
- `Step` 只有 `issueP`、`recordHistory`；
- `Claim` 只有 `atom`、`historical`、`current`；
- `Registered` 只有三项明示登记；`P = Unit`；
- `K(s,c) = Trunc (Registered s c)`，`Trunc` 是源码定义的原生高阶归纳命题截断；
- `Historical` 固定引用 `initial`，`Current s` 引用给定状态；
- 原生 `Path` 与 `transport` 来自 Agda 内建 Cubical 原语；**未调用 univalence，未导入 `Cubical.*`**。

## 2. 判词

> 固定有限验证事件模型内，保留时标的历史核查可完成；把固定过去改成当前的转换不成立，完全阶段擦除不保留相关真值判断。
> 原生 Cubical Agda 核查通过（项目内 capture + 独立 rerun）。该最小候选**未构成 HoTT 自身非现实性实例**。

判词标签：`VERIFICATION_EVENT_STAGE_BOUNDARY_WITH_POSITIVE_CONTROL`。
八项精确 claim 见 `HoTT/CLAIM_EVIDENCE_MATRIX.md` `C-149`–`C-156`（本地 ID `EVT-01`–`EVT-08`）。

## 3. 证据

| 类型 | 位置 |
|---|---|
| 当前主源码（唯一 owner） | `HoTT/formal/verification-event/VerificationEvent.agda`（SHA-256 `04f18440…`，与导入原件逐字节相同） |
| 固定工具链 | `TOOLCHAIN.json` + `AGDA_LIBRARIES`（Agda 2.8.0-3d04bac、Cubical v0.9 载入命令；证明的导入闭包只有 Agda 内建模块） |
| 项目内正向 run | `HoTT/verification/runs/20260913-MP-VERIFICATION-EVENT-001-01/`（exit 0、stderr 0、`EXACT_INDEX_SNAPSHOT_MATCH`、rerun `EXACT_EXIT_STDOUT_STDERR_MATCH`） |
| 负向校准（故意不通过） | `negative/BadCast.agda`；项目探针 `audit/imports/.../project-negative-probe/`（exit 42、`[UnequalTerms]`、`BadCast.agda:10`、`afterP != initial`）；外部原件 `negative-002` 收据保留 |
| 外部原件与异目录重放 | `audit/imports/verification-event-20260913-01a099e9/original-package/`、`relocated-replay/` |

`negative/` 只作校准，**不**纳入正向构建；外部旧收据保持原始字节与 schema，不改写冒充项目收据。

## 4. 禁止外推

- 不是实际设备或真实验证流程的运行轨迹；
- 不证明 HoTT 自身全局健全性、一般知识判定算法、完整 Fitch/Gödel 定理；
- 不说明任意不同时标命题都不同，也不证明所有抽象都会丢掉阶段信息；
- 不把 `Trunc` 上的否定外推到未加该截断的接口；
- 本最小候选未构成 HoTT 自身非现实性实例，也不关闭时间/时序方向的其它问题。
