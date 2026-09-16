<!-- governance-shard-index:v2
logical_id: PREMISE-001
mode: topical
shard_root: PREMISE-001
last_shard: PREMISE-001/001 - 分母 V1 冻结（A-G 条目、P1 前提与出处）.md
append_target: -
soft_line_target: 300
-->

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 1 个分片；缺一片即未完成。索引冻结任务与分母身份，
> 分片拥有分母条目本体与逐条登记结果。step-2 产出后 append_target 生效。

# PREMISE-001：HoTT 前提集穷尽清单与 P1–P4 分工

> 版本：`premise-001/v1.0`
> 冻结日：`2026-09-16`
> 当前判词：`DENOMINATOR_V1_FROZEN / P1_COMPLETE / P2_NOT_STARTED / P3P4_PENDING_USER`
> 方案权威：`Atria的方案/修订片/008 - PREMISE-001 HoTT 前提集穷尽清单与 P1–P4 分工.md`
> 当前 Goal：`goal-1.md`（索引；权威为 STATE）
> 程序化父级：`.codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md`

本逻辑文档把 **HoTT 自己的前提集**当作被穷尽枚举的分母。它不把前提的"存在登记"
当作"该前提已被判定非现实"，也不把分母完成写成发现已完成。非现实性判定（P3/P4）
永远由用户作出，AI 不得自证。

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [分母 V1 冻结（A-G 条目、P1 前提与出处）](<PREMISE-001/001 - 分母 V1 冻结（A-G 条目、P1 前提与出处）.md>) | A–G 七类共 30 条编号条目，每条 P1 前逐字前提陈述 + 出处；冻结收据（remainder=0） | current |
<!-- governance-shard-table:end -->

## 分母身份（冻结字段）

```text
PREMISE_DENOMINATOR_V1
  / 版本: v1.0（2026-09-16 冻结）
  / 条目总数: 35  (A=11, B=4, C=4, D=5, E=4, F=2, G=5)
  / 条目 id 格式: PREMISE-<类别字母>-<序号>，如 PREMISE-C-03
  / 理论基线: HoTT/THEORY_SCHEMA.md v0.2（C01–C18 / E01–E15 / D01–D12）
  / 域外: 证明助手实现现象、第三方库 API、性能（R0–R3 / IMPLEMENTATION_PHENOMENON）
  / 扩版: 新构造进入须显式 PREMISE_DENOMINATOR_V2，旧版保留不静默重写
  / remainder=0（分母内无未编号条目）；unknown ingress 保持开放
  / 分母 shard sha256: 5cd1b44fb49fc9dc6afeeddaad6e3a8b3a0430d04f752b45979a851505c9c3be
```

## 证据入口

- 方案正文：`Atria的方案/修订片/008`（分母定义、P1–P4 分工、必填字段、验收判词）
- 修订依据：`Atria的审计报告集/09 - 反思路径的结构性边界与前提清单的可枚举性.md`
- 认识论锚点：`核心认知.md` generation-7 的 KC-000044 / KC-000045 / KC-000046
- 理论规则回源：`HoTT/theory-schema/CORE_RULES.md`、`EXTENSIONS_AND_METATHEORY.md`、
  `DERIVED_STRUCTURES.md`、`SOURCES_AND_COVERAGE.md`（21 个 HoTT Book 原字节快照）
- 机器统观引擎证据（外部导入快照，引擎本体不在本 repo）：
  `audit/imports/machine-overview-ce-map-20260915/`、
  `audit/imports/machine-overview-computability-20260914/`
- 当前队列与下一动作：`.codex/research/hott/STATE.json`（active 队首 `A-PREMISE-001`）
- 方案演化账本：`git log --grep=plan-revise`；步骤账本：`git log --grep=PREMISE-001`

## 角色分工（不越界）

| 栏 | 内容 | 归属 |
|---|---|---|
| P1 | 前提逐字是什么、出处在哪里 | 角色 A（AI）—— step-1 已完成 |
| P2 | 现实骨架映射、解释断裂点、省略形状 | 角色 A（AI）—— step-2 |
| P3 | 在什么任务下被节省的条件重新不可省 | 角色 B（用户） |
| P4 | 替代物换了什么 | 角色 B（用户） |
| C | 冻结任务族 → 枚举 → 保归约 → 原生核收据 | 角色 C（引擎，GEN-001 链） |

## 验收判词（沿用 008 §6）

```text
PREMISE_INVENTORY_COMPLETE_WITH_SCOPE
  / 分母全部条目完成 P1/P2，每条带 omission_shape 或显式 NO_OMISSION_IDENTIFIED
  / remainder=0；P3/P4 已交用户，用户已逐条给出判定或显式"暂不判定"
  / 不声称覆盖 HoTT 全部可能的未命名前提；unknown ingress 保持开放

PREMISE_AUDITED_NO_NONREAL_PREMISE_WITH_SCOPE
  / 用户对全部分母条目判定为无非现实前提
  / 这是有分母的负结论，不是"反思不够"
  / 不声称分母外无非现实前提
```
