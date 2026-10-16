# 05 - goal 与治理修订草案

> 权限声明：以下是**建议草案**，供所有者裁定。未获裁定前，`goal.md`、四件套、
> STATE、方向/全景 projection 的现行文本不受本目录任何影响（自审计 G9）。采纳时
> 建议按 WAI 已熟悉的外部评审吸收模式（字节保全导入 + 逐项核验 + 登记）进行。

## 1. goal.md 双轨完成门修订草案（可直接采纳的文本）

在 `goal.md` §11 之前插入新节，原 §11 整体保留并更名：

```markdown
## 10.5 双轨验收（DELIVERY_TRACKS_V1）

本 Goal 的验收分为两条互不阻塞的轨道：

- **定理线（原 §11 全文保留，更名"定理线完成门"）**：至少一个候选贯通
  "exact HoTT 规则/表示 → 抽象或资格变化 → natural consumer → 机器证明的不完成/
  不相容 → HoTT 必要性 → 现实同任务对应 → 方向 A 或 B"。此门不变、不降格。
- **组装线（新设）**：交付《Z 铁律最强机器证据报告》（非因子化实例族 + 提升语义 +
  支付-债务目录 + 计算合法性对照，全部锚点可回溯 claim/run），并通过仓库所有者评审。
  满足后 Goal 增设状态 `DELIVERED_ASSEMBLED`（仅标记组装线交付，不是定理线终点，
  不是 `complete`，不进入 `全景视野` 结果状态词表）。

两线关系：组装线交付后定理线**继续**（P7 不延期：每轮 bounded unit 结束必须给出
下一个具体构造）；定理线出现贯通见证时按原门完成，组装线状态自动并入最终报告。
generic 类结果（§1 禁报清单）按 KC-000027 的"继承"框架呈现，不冒充两线任何一方的
完成。
```

配套状态字段：`STATE.execution_control.status` 可表达
`CORE_GEN4_ASSEMBLED_THEOREM_LINE_ACTIVE`（示例），`goal.status ∈ {ACTIVE,
DELIVERED_ASSEMBLED, COMPLETE}`。

## 2. 版本纪律（第 0 步，当天执行）

1. 精确 stage 以下路径并 commit（不动其他 dirty 文件）：`HoTT/formal/`（全部新包）、
   `HoTT/verification/runs/`（20260913 之后全部）、`HoTT/CLAIM_EVIDENCE_MATRIX.md`、
   `HoTT/verification/PROOF_VERSION_CLOSURE.json`、两个 README 索引；
2. commit 后回读 HEAD、重跑 `verify_proof_version_closure.py` 与 `verify_formal_proof_run.py`，
   把 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` 逐行翻转为 version-closed；
3. 之后每完成一个 F-011 run 即 commit（单 run 粒度），不再积压两天量。

## 3. 治理预算上限（防 T2"治理吞噬"）

| 项 | 上限建议 | 超限处置 |
|---|---|---|
| `STATE.json` 体积 | ≤1MB | 触发分片（records 按 ID 前缀拆 JSON，主文件只留索引）——比逻辑文档分片更保守地走同一合同 |
| KC 回评 | TOUCHED 行全文；NOT_TOUCHED 行合并为一行计数（保留 KC 编号清单） | 每个 session 至少省 ~10KB 仪式文本 |
| corrective re-pin session | ≤1/工作日 | 连续超限说明索引设计有问题，停下修设计 |
| 抽样批次 | 已停（04 §4） | — |
| 每个 bounded unit 的治理开销 | ≤数学工作的一半（session 内时间计） | 超限记入该 unit 复盘 |

## 4. 截止日纪律（防 B6 复发）

1. 任何具名截止日到期，必须在其 owner 文件产出**逾期处置记录**：完成/顺延（附新日期
   与理由）/降级（缩小分母）三选一，不得静默继续；
2. `LIT-DENOMINATOR-001`（截止 2026-09-14，已逾期）的处置建议：顺延至 PHY 族并入后
   的新日期，`COMPREHENSIVE_COVERAGE_NOT_ACHIEVED` 保持为诚实判词。

## 5. 采纳路径（建议）

1. 所有者审阅本目录（含 07 自审计的 G1–G10 处置表）；
2. 裁定：双轨门文本是否采纳、Q1–Q8 队列优先级、治理上限数值；
3. 交 WAI 按其吸收流程执行：goal.md 修订 → 方向追踪新增
   `DIR-TOP-REALITY-TASK-MODEL`（ACTIVE_USER_DIRECTION，KC 关联 000003/010/011/012/
   013/022/024）→ 阶段 A/B/C 作为 TaskSpec 冻结 → 正常走 F-011/checkpoint 体系；
4. 07 号自审计作为外部评审证据归档（`audit/imports/` 模式）。
