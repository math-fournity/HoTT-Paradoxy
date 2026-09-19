# 状态账本层重设计：STATE v3 热/冷拆分与 checkpoint 瘦身

（对应《机制报告》007：STATE.json、动态附加、checkpoint 的调查结论）

## 1. STATE.json → v3（本方案最大单项）

**原来存在什么问题**（姊妹报告 006 + 机制报告 007 的合并实测）：
(a) 三重身份压一个 always_full_boot 文件——指针价值占 0.x%，records 占
97.5%（其中 174 条历史 session 占 33.8%）；(b) 只进不出：5 天 7.4K→840K
（113 倍）；(c) 双状态轴挡住了"历史复活"的任务资格，挡不住字节过境——
机制只建了一半；(d) 其重量直接导致重事务被 S170–176 绕过、HEAD 漂移、
canonical plan 被锁死。

**打算如何调整**（schema v3 骨架）：

```json
{ "schema_version": "hott-working-state/v3",
  "hot": { "revision", "current_core", "active", "latest_session",
           "unresolved", "structural_tension", "review_due" },
  "records": { "<ID>": { "kind", "path", "lifecycle_status",
                          "evidence_status", "depends_on",
                          "source_hashes", "archive_ref" } },
  "archive_manifest": { "files": ["archive/records-<n>.json"],
                          "record_count": 322, "sha256": "…" } }
```

三刀：(1) **记录瘦身**——STATE 内每条记录只留身份+状态+hash+指针
（`archive_ref` 指向完整叙述），判词/收据叙述回到 SESSION.md/runs（本来就有
owner）；(2) **退休机制**——`kind=session` 或 lifecycle ∈ {CLOSED, HISTORICAL,
SUPERSEDED} 的完整记录迁入 `archive/records-<n>.json`（query_first 层；
`query --record` 命中冷档时透明水合）；(3) **迁移走 manager**
（`state_archive.py`，仿 core generation 的 transition 收据模式：
分母 322 条全部可定位、remainder=0、旧版全量备份+tag 可回滚）。

**为什么调整后更好**：hot+瘦 records 目标 **≤3 万 est tokens**（现 22.4 万，
-87%）；每会话读的是"当前状态"，账本与档案按需——层归属与三重身份对齐；
退休机制使增长有界（这是 core 七代零失控的同款保险）；drift 依旧 fail-closed
（机制不变，只是守护对象小了两个数量级，事务重新变得付得起——直接回应
S170–176 绕过的根因）。证据零损失：archive 是搬不是删，且进了 query_first
（框架已验证的水合机制）。

## 2. 动态附加机制（latest session + active 路径）

**原来存在什么问题**：无——机制报告 007 认定这是框架中增量续接的正确样本
（指针常驻、内容按 ID 水合）。

**调整**：仅随 tier 参数化（T0 不加载、T1+ 加载）。**为什么**：好部件
不动；档位化只是让它不再为轻任务付费。

## 3. checkpoint 瘦身

**原来存在什么问题**（姊妹报告 007）：每次事务复制全部可变文档
before/after（单次 ≈2.9M，139 次=187M）；无保留上限；事务重到被绕过——
而审计集被 020 合同瘦身后 AI 反而自愿写（被绕过的是事务包装不是审计内容，
这个不对称是设计信号）。

**打算如何调整**：(1) **payload 减容**——STATE v3 后事务复制对象自动缩到
≈1/10（hot+瘦 records+受影响投影片；冷档不入事务）；(2) **保留策略**——
近 5 期保全量 before/after，更早转 `checkpoints/archive/`（只留
transaction.json+result.json 收据索引，before/after 移出 HEAD.tracked）；
(3) 补齐已登记的 `after/` 分片覆盖缺口（或显式声明 git-side）。

**为什么调整后更好**：单次事务 ≈0.3M 级（-90%），磁盘 187M → ≈15M；
原子性/回滚能力在活跃窗口内完整保留（超出窗口回滚走 git/tag——本 repo
的既有回滚边界本来就是 git）；事务重新"付得起"，绕过动机消失。

## 4. 治理 ROI 遥测（新增）

**设计**：SESSION.md 新增 `element_usage` 表——框架各元件（四件套/启动核各件/
水合/审计/门禁/checkpoint）× 三态（实际用到 / 未用但若用会拦住什么 / 未用且
无影响），每轮 ≤30 行。**为什么**：让"框架值不值"从感觉变成数据；
S170–176 式消融不再靠事故发生才被观察，每轮都是受控采样；为下一轮裁剪
提供分元件依据（这是对用户"引起警觉"的方法论回应——把警觉制度化）。
