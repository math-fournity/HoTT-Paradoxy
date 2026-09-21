# P12-THIRD-SUCCESSOR-DISCOVERY-001：选择环境对关系的 `R` 资格化分母

**状态：** `SUCCESSOR_SELECTED / AMBIENT_PAIR_RMIN_REQUALIFICATION_CANDIDATE / P13_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM`
**日期：** 2026-09-21
**当前目标边：** P1/P6 的独立结构理论边；P12 不重跑既有 Lean 证明，也不声称找到 K。

## 1. 判词改变凭据

P8/P9/P11 已经在两个定向 source 与一个非定向 Circle/Coeq source 中得到“字段、glue 或 coherence 被显式保留”的有界防御。P12 必须避开这些 source clusters，并比较未审规则、非 Circle/Coeq 消费者、独立更强 `R/Done` 与实现差异。

本轮唯一能改变最终见证链的现有证据不是另一份 Circle 定义，而是 `MP-ASTRA-AMBIENT-CIRCLE-001`：它在固定实平面中同时给出内在 homeomorphism 与更强的 ambient operation 失败。若这个关系能以独立数学理由进入 `R_min` 的专门化，它会把“来源/复原差异”从纯叙事字段提升为一个标准的 pair/embedding-preserving 比较对象；若不能，它只能留作已有局部控制。无论结果都不推出 HoTT 缺陷。

## 2. 公开与本地侦察

公开搜索的 `ambient homeomorphism`、`homeomorphism of pairs` 和 HoTT 组合没有给出用户精确 `C,p,M,N,e,Done_s` 的 HoTT consumer。它确实确认“空间连同子空间”的 pair，以及要求环境 homeomorphism 保持子空间的比较，是标准拓扑语言；这与裸空间同胚是不同的判据。这个结果应标为 `KNOWN_STANDARD_STRUCTURE / NO_EXACT_HOTT_TASK_WITHIN_DECLARED_SEARCH`，而不能伪称“学界已经解决圆环问题”。

本地侦察发现：

| 资产 | 覆盖裁决 | 直接事实 | 对 P12 的作用 |
|---|---|---|---|
| `AmbientCircle.lean` / C-266..268 | `PARTIAL_REUSE`，而非新证明任务 | 指定 `Plane` 中 `M` 与 `N` 内在同胚；但不存在将一者像到另一者的整平面 homeomorphism；有限环境 homeomorphism 操作也不能复原。 | 可作为 `R_ambient` 的强、具体、操作受限实例。 |
| `PuncturedCircle.lean` / C-265 | `EXACT_COVERAGE_OF_INTRINSIC_HOMEOMORPHISM` | 去点圆与开区间的内在 homeomorphism 已保存。 | 是 `R_ambient` 必须保留的正控制，不能改写成“不同拓扑”。 |
| P6 `OriginPresentation` 字段矩阵 | `PARTIAL_REUSE` | P6 已要求显式 `N→M→C`、boundary、closure 与 process，但未把这个已证明的 ambient operation relation 作为独立字段—操作实例。 | P13 只补这一缺口，不重做 P6 或 C-266..268。 |
| P4 / Coq-HoTT `Admitted` | `NO_TRIGGER` | 没有同一规则跨实现的可重放语义差异。 | 不把 source trust boundary改名为实现不忠实。 |

当前源哈希与保存的 ambient run manifest 一致。该 run 是 `KERNEL_ACCEPTED_WITH_SCOPE` 的经典 Lean 几何证明，且明确标为 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`；它不是原生 HoTT 证明，也不能替代 P3 的实际 K。

## 3. 选择 P13：`AMBIENT_PAIR_RMIN_REQUALIFICATION`

P13 的输入是**已有** C-265..268，而不是一轮重跑：

```text
H_intrinsic(M,N)  := M 与 N 作为子空间的 homeomorphism
R_ambient(M,N)    := 指定 ambient Plane、嵌入/闭包余集和允许的 ambient operation
Done_ambient      := 在固定 operation class 中把 N 复原为指定 M 的任务
```

P13 要做四件事：

1. 将上述 `R_ambient` 明确标为 `R_min` 的**专门化候选**，不是用户完整现实历史的替代；
2. 使用已保存的 C-266 内在同胚正控制、C-267 环境同胚反控制、C-268 有限操作反控制，逐一映射 Input、Operation、Observation 与 Done；
3. 核对它与 `OriginDirectedDiagram` 的静态/操作字段兼容，而不把 Lean 的经典点集定理冒充 HoTT 内部命题；
4. 判断这一结构是否真提供了未来 K 可以消费的非任意强完成条件；若只是现有字段的同义翻译，结论必须是 `RESTATEMENT_ONLY`。

## 4. 波次定位与停止

1. **最终目标连接：** P12 重新打开 P1/P6 的独立 `R` 边，直接检验用户“内在同胚不足以刻画嵌入/复原”的直觉能否具有标准、机器化的专门化。
2. **全局坐标：** P1 固定受限 `R_min`；P6 做结构承载比较；P12 发现一个 P6 未显式纳入、已有直接 Lean 控制的 ambient-pair specialization；P13只资格化它。
3. **实际价值：** 不新增证明，却把已有精确 C-266..268 从历史资产转为可审计的 future-K task contract 候选，避免重复写同样的 Circle/interval 代码。
4. **为什么不继续 P12：** 四类入口已作有界比较；P13 是唯一同时满足“独立数学理由、当前 proof evidence、原圆环直接相关、未被 P6 显式吸收”的候选。继续列关键词没有新的判别力。
5. **裁决：** `SWITCH_BRANCH / SUCCESSOR_SELECTED`。P13 尚未启动；它不自动产生 P14。

## 5. 禁止外推

- C-266..268 的有限环境 operation class 不覆盖加点、切割、重嵌入、一般连续过程或无限极限；
- `R_ambient` 不是“现实同一性”的完整定义，也不能单独形成 HoTT 指控；
- 经典 Lean proof 的接受不证明 native HoTT 命题；
- P12 没有发现实际 K、理论规则桥、实现差异或 HoTT 缺陷。
