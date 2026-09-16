<!-- governance-shard-index:v2
logical_id: GPT-HOTT-MACHINE-OVERVIEW-PLAN
mode: topical
shard_root: HoTT机器统观后续工作方案
last_shard: HoTT机器统观后续工作方案/010 - 治理写回、自证伪、文本终止与最终验收.md
append_target: -
soft_line_target: 300
-->

# HoTT 机器统观后续工作方案

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 10 个分片；缺一片即未完成。任何执行、审计或采纳判断必须按表顺序读取全部分片，不能把本索引或单个工作包冒充完整方案。

> 方案版本：`gpt-hott-machine-overview-plan/v2.1`  
> 日期：2026-09-15  
> 身份：`USER_REQUESTED_UPDATED_GPT_PLAN / COMPLETE_LOGICAL_DOCUMENT / NOT_PROJECT_CURRENT_QUEUE_UNTIL_CANONICAL_WRITEBACK`  
> 工作根：`/Volumes/D/HoTT_AI_HANDOFF_20260911`  
> 当前合格见证数：`0`  
> 数学证据身份：方案与既有证据综合；本逻辑文档不新增数学定理  
> 取代关系：本逻辑文档取代 [旧单文件 GPT 方案](../GPT的回应/HoTT机器统观后续工作方案-七轮审计共识综合与执行论证-20260915.md) 作为 GPT 当前方案；旧文件保留为历史 proposal evidence  
> 审计修订依据：[GLM 深度审计](../GLM的回应/对GPT七轮综合工作方案的深度审计-20260915.md)、[GPT 第八轮复审](../GPT的回应/GLM第八轮深度审计报告-20260915.md)、[GLM 第九轮回应](../GLM的回应/对GPT第八轮反馈的审计-20260915.md)与[GPT 第九轮复审](../GPT的回应/GLM第九轮回应审计报告-20260915.md)  
> current-truth 边界：用户本轮授权更新并拆分 GPT 方案；未授权本轮直接改写 `goal.md`、STATE、MEMORY、方向、全景、Feature、rulings、claim matrix 或执行 Git 提交

本方案的第一执行链是：

```text
FR-001 source identity reconciliation
  → PSJ-001A Delay/race/deadline
  → TGSQ-001A time/geometry source denominator
  → PSJ-001B same-function/different-time
  → evidence-driven review
  → direct A1 candidate or ATD/R4X/CAN
```

`FR-001` 是当前必要前置，因为 active Goal 与 R4 record 的实际文件 hash 已与 STATE pin 不一致。它完成来源身份重建，不把 hash 改成现值当作修复。PSJ 与 TGSQ 随后用最低成本分别解决提升来源和时间／现实来源；R4 保留为 exact-HoTT/Gödel 诊断线，并优先做 arithmetic-only 消融。

v2.1 在 v2.0 的执行结构上新增两项：内容“存在／缺席／属于哪个来源”的分层验证纪律；FR 旧 bytes 缺失时，对全部受影响审计引用建立完整 anchor manifest，而不是以 4 个选定锚点代表全部结论。

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [共识基线、证据边界与审计谱系](<HoTT机器统观后续工作方案/001 - 共识基线、证据边界与审计谱系.md>) | 方案身份、权威顺序、零见证状态、七轮往返与第八轮修订 | current |
| 002 | [总体执行架构与统一判词](<HoTT机器统观后续工作方案/002 - 总体执行架构与统一判词.md>) | 三条发现线、两条支撑线、P0/P1/A1 与失败判词 | current |
| 003 | [FR来源身份重建与版本闭合](<HoTT机器统观后续工作方案/003 - FR来源身份重建与版本闭合.md>) | active record mismatch、可恢复/不可恢复双路径、VC 分批版本闭合 | current |
| 004 | [PSJ提升来源与HoTT必要性判决](<HoTT机器统观后续工作方案/004 - PSJ提升来源与HoTT必要性判决.md>) | 候选批次、九字段、comparison calculus、判词和停止条件 | current |
| 005 | [时间几何来源与应用任务建模](<HoTT机器统观后续工作方案/005 - 时间几何来源与应用任务建模.md>) | 时间/时序双分支、TGSQ、ATD、OperationalTaskModel、TGF | current |
| 006 | [R4X与CAN精确HoTT计算诊断](<HoTT机器统观后续工作方案/006 - R4X与CAN精确HoTT计算诊断.md>) | R4 十门、formal calculus/implementation、Gödel 消融、canonicity 五对照 | current |
| 007 | [COV程序化统观与EXP表达保真](<HoTT机器统观后续工作方案/007 - COV程序化统观与EXP表达保真.md>) | 八轴、六生成器、相对完备性、unknown ingress、最小理论与用户理论表达 | current |
| 008 | [机器证明、反解释、独立评估与文献](<HoTT机器统观后续工作方案/008 - 机器证明、反解释、独立评估与文献.md>) | F-011、正反控制、六类 holdout、评价指标、五条学术来源线 | current |
| 009 | [里程碑、首三单元与执行转向](<HoTT机器统观后续工作方案/009 - 里程碑、首三单元与执行转向.md>) | M0–M6、前三个可直接执行单元、结果驱动转向 | current |
| 010 | [治理写回、自证伪、文本终止与最终验收](<HoTT机器统观后续工作方案/010 - 治理写回、自证伪、文本终止与最终验收.md>) | 单工作面、owner 写回、动态测量、方案自证伪、文本终止、Goal 门 | current |
<!-- governance-shard-table:end -->

## 使用规则

- 本方案是完整的工作方法和执行路线，具体动态状态仍由 current Goal、MEMORY、STATE、TaskSpec、proof/run 和来源证据决定。
- 用户采纳方案不等于任何工作包已经实现；每项从 `PLANNED` 开始，以本分片中的证据判据提升。
- 新事实若推翻本方案，不保护方案；按第 010 片的自证伪条款调整路线并保留旧版本。
- 数学结论继续服从项目 F-011；来源、现实解释、HoTT 必要性与原创性不得由单一 kernel PASS 代替。
