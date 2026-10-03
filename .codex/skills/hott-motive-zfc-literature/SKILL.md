---
name: hott-motive-zfc-literature
description: Map and investigate HoTT creation motives as a reproducible literature corpus and source-grounded ZFC candidate seeds when the user invokes HOTT-MOTIVE-ZFC-SOP; never treat local frozen runs or motives as field-wide coverage or ZFC defects.
metadata:
  version: "2.0.0"
  role: "task-scoped-literature-investigation"
  sop_name: "HOTT-MOTIVE-ZFC-SOP"
---

# HoTT 创建动机反投影 ZFC 文献调查

## 何时使用

仅当用户明确引用 `HOTT-MOTIVE-ZFC-SOP`、要求将 HoTT 创建动机反投影为 ZFC 候选并进行系统文献调查／存档，或要求继续该项目时使用。先完成全局 `repo-cognitive-closure`，再按项目路由读取最高指示、四件套与下列 canonical SOP：

- [调查 SOP](../../../dev-docs/HoTT创建动机反投影ZFC文献调查SOP.md)
- [动机反投影路线种子](../../../dev-docs/菲尔兹奖后续理论级目标路线图/009%20-%20HoTT创建动机反投影ZFC候选路线.md)
- [项目档案根](../../../audit/HOTT-MOTIVE-ZFC/README.md)

本 Skill 不因文件存在、路线种子或一个动机关键词自动启动调查、P-DAG、worker、网络检索、Goal／STATE mutation、数学证明或理论结论。

项目档案根可以先于任何调查 run 存在；`PROJECT_DEFINED / RUN_NOT_STARTED` 只证明入口、ID和归档合同已经就绪。只有用户以调用名启动后，才在该根下冻结来源分母并创建实际 run。

## 不可跳过的工作身份

将每项材料分成：

```text
R_i  HoTT 原典动机或能力目标
Z_i  精确 ZFC / set-theoretic rule, presentation cost, guard or consumer
Q_i  经模式 P、同一任务、支付扫描和控制后才成立的候选
E_j  现实／认知任务与 formal totality 的来源桥；不是 R、Z 或 Q 的替代
```

`R_i` 不是 ZFC 错误证据。`H0→Z0→Q0` 必须按 SOP 的 T0–T5 传输门独立审计；传输失败是
`ANTI_ANALOGY_CONTROL`，不能被写成调查失败或 ZFC 安全结论。

若文献本身描述有限或现实过程的 `Done_h`、无限 totality／set formation 的 `Done_Z`，或其间的
metaphor/analogy/critique，建立 `RealityTaskBridgeCard`。它必须逐项固定 subject、operation、observation、Done、
bridge qualifier、理论侧 pairing和正反控制。`metaphor`、每元素定理、formal sethood与实际过程完成不能互相替代；
没有同一任务和独立 P2/P3 evidence 时，它保持 `P_REQUALIFICATION_REQUIRED`。

## 执行路由

1. 先读取 SOP 004 与 LITERATURE-MAPPING-AUDIT，区分 SOURCE_RUN_ONLY、LITERATURE_MAP_REQUIRED、LITERATURE_MAP_ACTIVE 和 MAP_COMPLETE_WITH_SCOPE。局部 run 的 complete-with-scope 不能写成领域文献已完成。
2. 地图仍未完成时，先冻结 LITERATURE-MAP-001 的研究问题、数据库／作者／引文来源、完整 query、时期／语言、纳入排除、去重和停止条件；原始命中、筛选与 coverage 按 SOP 004 保存。
3. 再冻结候选 run 的来源分母与 archive manifest；没有版本、身份、范围或来源权限的材料不得计入“彻底调查”。
4. 逐项提取可定位的 R-card，再重建 Z-card；若有 E-source，另建 RealityTaskBridgeCard。来源事实、AI 解释、bridge qualifier、标准防线和候选状态保持分栏。
5. 只有来源充分的 Z-card 才能按 P1/P2/P3、同一任务与活跃义务进入 Q-card。P-DAG 只在现有独立授权和具体 NodeCard 条件满足时调用。
6. 每个自然单元更新项目 archive；不以文献数量、关键词命中或作者动机的修辞代替候选资格或地图覆盖。

## 完成边界

一次 candidate run 只在声明的来源分母已逐项处置、每个 R-card 有 Z disposition、每个 Q-card 有状态与控制、archive manifest 可复算且下一未处理入口清楚时结束。它不得因此宣称所有 HoTT 动机、所有 ZFC 文献或 ZFC 问题已经穷尽。只有 SOP 004 的 protocol、search log、screening、citation network 和 coverage map 已按冻结范围完成，才能把一个更宽的文献地图称为 MAP_COMPLETE_WITH_SCOPE；独立检索审阅缺席时必须保留其限制。
