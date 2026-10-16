# C - EXP 表达保真提前增补

> 对应 GPT 原片：`../GPT的方案/HoTT机器统观后续工作方案/002`（工作包表）、`007`（§8–§10）、
> `009`（里程碑表）。
> 修改性质：**修正排序**——把 EXP-001 的最小表达保真单元从 `PLANNED_AFTER_EXACT_TARGET`
> 提前为 PSJ 第一批之后的独立低成本单元。这是对 007 片 §8"不能被 PSJ/TGSQ/R4 替代"与
> 002 片 `PLANNED_AFTER_EXACT_TARGET` 之间**内部矛盾**的修复。

## C1. 矛盾所在（本审计定位）

- 007 片 §8：EXP-001 的两项（最小理想理论覆盖检验 KC-000031；HoTT 表达用户悖论理论 KC-000035）
  "不能被 PSJ、TGSQ 或 R4 自动替代"；
- 002 片工作包表：`EXP-001 = PLANNED_AFTER_EXACT_TARGET`；
- 009 片里程碑 M0–M6：EXP 无任何早于 R4X 的位置。

三者合起来 = "一个不可替代、且是用户核心认知显式要求的单元，被无限期顺延到一条可能长期不
收敛的线（R4X）之后"。这是方案内部自相矛盾的硬缺口。

## C2. 修正：EXP-MIN 提前为独立单元

新增一个最小单元 `EXP-MIN-001`，排在 PSJ 第一批（M1-A/M1-C）之后、R4X 深化（M2-B）之前：

```text
EXP-MIN-001（最小表达保真，低成本独立单元）：
  输入：
    - 一个最小 source theory（理论对象/操作、形成与构造历史、观察/完成关系、
      abstraction map、ASK 资格关系、所需保持）；
    - 用户核心认知 KC-000031/000035 的原文锚点；
  动作：
    - 在"任何足够强的类型论"层面（无需等 R4X exact target）构造 interpretation；
    - 分别判 SYNTAX_ENCODABLE / DERIVATION_PRESERVED /
      OBSERVATION_COMPLETION_PRESERVED / ONLY_EXTERNAL_PARAMETER_PRESERVES_TASK /
      NO_FAITHFUL_INTERPRETATION_CANDIDATE_WITH_SCOPE / INCONCLUSIVE；
  交付：EXP-MIN TaskSpec + 判词 + 未决；
  停止：一个最小 source theory 的 interpretation 与 preservation 判词闭合。
```

关键点：EXP-MIN 的"最小 source theory"不必依赖 R4X 选定的 community cubical calculus——
它只问"HoTT/类型论能否表达用户的抽象/否定/完成/ASK 结构"，这是表达力问题，可在任一
具名类型论（含当前已有的 Cubical Agda 工具链）上先行。R4X 选定 exact target 后，EXP 再
升级为"在该 exact target 上的完整保真检验"。

## C3. 里程碑落点

在 009 片里程碑表插入：

| 里程碑 | 工作 | 可验结果 |
|---|---|---|
| `M1-D` | EXP-MIN-001（最小表达保真） | SYNTAX_ENCODABLE 或具名 scope 否证 |

排在 M1-C（PSJ-001B）之后、M2-B（R4X）之前。它不阻塞 R4X，但不再被 R4X 阻塞。

## C4. 采纳判据

- [ ] 002 片工作包表 EXP-001 状态改为 `EXP-MIN PLANNED_INDEPENDENT / FULL_AFTER_EXACT_TARGET`；
- [ ] 009 片里程碑表新增 `M1-D EXP-MIN-001`；
- [ ] 007 片 §10 停止条件同步（EXP-MIN 首轮判词闭合后停止，不等待 R4X）。
