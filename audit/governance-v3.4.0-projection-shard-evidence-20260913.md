# project-local governance v3.4.0：三件套分片（第二波）证据

> 会话：`S-GOV-20260913-096-PROJECTION-SHARD-MIGRATION`（revision 96）
> 授权：用户审查分片现状后明确说“开始第二波”，见 `rulings.md` §18；触发条件来自合同 §7（三件套迁移必须由用户发起）
> 范围：`方向追踪.md`、`全景视野.md` 迁为 v2 索引 + 行分片，并强化三方校验；`核心认知.md` 保持单文件
> 回滚边界：本地 annotated `governance-v3.3.0`（迁移前最后一个单一投影状态）

## 1. 迁移结果

| 逻辑文档 | 模式 | 分片 | 原文规模 | 对账 |
|---|---|---|---|---|
| `方向追踪.md` | topical | 5 | 162 行 / 28 条 `DIR-*` 行 | 每行恰好消费一次；额外行只有表头 |
| `全景视野.md` | topical | 8 | 206 行 / 89 条 `OUT-*` 行 | 同上（含 1 行跨块归位：`OUT-TOP-THREE-WAY-SKELETON` 归入治理/骨架片） |

分片布局（`全景视野.md`）：001 使用规则与状态语义（§1+§4+§5+§6）、002 治理/门禁/骨架、003 当前机器证明包与原生重放（19 行）、
004 距离综合与消费者审计（14 行）、005 证据队列抽样与证据卫生（16 行）、006 ERCF-3/T3 脉冲与失败台账（14 行）、
007 历史来源结果与关系（23 行 + §2.1 + §3）、008 当前未完成。
`方向追踪.md`：001 三方职责与状态语义、002 治理与用户方向（6 行）、003 LocalGPT/WebGPT 方向（19 行）、
004 证据与覆盖方向 + STATE 覆盖表（3 行）、005 交叉审视/优先级/更新规则。

结果/方向行**文本逐字未变**；片内行序即原表行序（002 除外，仅一行归位），无改写、无压缩、无删除。

## 2. 关键规则（本轮确立）

1. **身份字段留在索引**：`<!-- integrated-…:v…` marker 块、`source_state_revision`、`projection_generation`、
   `semantic_status` 仍由 canonical 路径承载，因为 runtime `graph()` 与 `verify_projection_freshness.py` 直读该物理文件。
2. **行分片自带表头**：大表按家族拆分后，每片必须重复表头两行（否则 Markdown 表格失效）。这是**唯一允许的重复内容**，
   对账规则随之从“整文拼接逐字节相同”升级为“每行恰好消费一次 + 额外行 = 表头行 × (行分片数 − 1)”。
3. **全文身份不变**：索引 + 全部分片才是三件套的“全文”；缺片即未完成，runtime 3.3.0 强制全片覆盖。
   分片只买写入局部性与导航能力，**不减少每次 Session/压缩恢复的必读内容**。
4. **消费端必须逻辑文档感知**：分片前，`verify_three_way_cognition.py` 直接按行解析物理文件且**不校验计数非零**——
   分片后它会以 `PASS` 返回 `direction_count=0 / outcome_count=0`（空壳通过）。本轮改为按逻辑文本解析，
   并新增 `DIRECTION_ROWS_EMPTY`、`OUTCOME_ROWS_EMPTY`、`PROJECTION_SHARD_UNREADABLE` 三条 fail-closed。

## 3. 工具与消费端变更

| 资产 | 变化 |
|---|---|
| `scripts/audit/migrate_projection_shards.py` | 新增：投影专用迁移（头部留索引、行分片、表头重复、逐行对账、`--emit-bundle`） |
| `scripts/audit/projection_edit.py` | 新增：checkpoint 适配器的 canonical 编辑 helper（`replace_in_index`/`replace_in_shard`/`append_to_shard`/`payload_rows`） |
| `scripts/audit/verify_three_way_cognition.py` | `DIR-*`/`OUT-*` 行改读逻辑文本；新增 3 条 fail-closed |
| `scripts/audit/verify_fresh_three_way.py` | 三件套不变量改判为“三个索引按固定顺序出现且各自展开到全部分片”；子进程检查同步（不再假设前三行就是三件套路径） |
| `scripts/audit/test_three_way_cognition.py` | +2 用例（分片投影读穿索引、缺片 fail-closed），6/6 通过 |
| `docs/quality/长治理文档分片与索引合同.md` | 新增行分片规则；§7 已分片表加入两个投影，保留项仅剩 `核心认知.md` |
| `AGENTS.md` / `.codex/AGENTS.md` / `PROTOCOL.md`(v2.5) / 本地治理 Skill(3.4.0) / `LOAD_SET.json`(3.4.0) | 路由与版本写回 |

## 4. 验证（revision 96 实测）

| 检查 | 结果 |
|---|---|
| 分片结构 validator | `PASS`；indexes=13（8 canonical + 5 个 checkpoint before/after 副本）、notices=0 |
| runtime 单测 | 38/38（含 5 条分片负向测试） |
| 三方校验单测 | 6/6（含分片与缺片用例） |
| 三方校验 | `PASS`；`direction_count=28`、`outcome_count=89`、revision 96 |
| fresh 冷启动 | `PASS_WITH_SCOPE`，revision 96；子进程三件套展开检查通过（`trio` 索引位置有序、各片完整） |
| projection freshness | `PASS_WITH_SCOPE`（`source_state_revision: 96` 在索引中） |
| math gate / core / merge / cross-source / history | 全部 `PASS`/`PASS_WITH_SCOPE` |
| canonical checkpoint | `.codex/cognition/checkpoints/S-GOV-20260913-096-PROJECTION-SHARD-MIGRATION/result.json` = `CHECKPOINT_COMMITTED`（revision 96） |
| hydration 回归 | S094/S095/S096 三个 record 的 research hydration 均正常（`DIRECTION`×5、`PANORAMA`×8、`README`×4、`MEMORY`×3 全部展开） |
| STATE re-pin | 仅 `AGENTS.md`（新增路由文本），带 `revalidation`；两个投影本身无 record 以 hash 固定（hashed_by=0），无新增 stale |

## 5. 规范冲突与裁决

全局 3.16.0 的默认读法是**选择性**的（“按任务加载 owner shard，跨范围才扩展”），与本项目三件套“每次全文”的
ruling §9–§12 冲突。本轮明确以**项目不变量 + runtime 全片覆盖**为准，并把该裁决写进合同与 PROTOCOL §3B；
分片不得被解释为降低读取标准。

## 6. 残余未知与边界

- **fresh model behavior NOT_RUN**：结构与字节层已验证；未来模型是否按索引+全片正确读写仍需真实 Session 观察。
- `核心认知.md` 保持单文件（curation+manifest hash 管理，36 条 KC 平铺）；若未来需要分片，必须由
  `build_core_cognition.py` 生成复合 hash，不能手工拆。
- `HoTT/CLAIM_EVIDENCE_MATRIX.md`（行级 proof 收据耦合）继续单文件，触发条件见合同 §7。
- 不改任何 KC、数学判词、proof source/run/index；数学目标（E6 consumer 等）不受本轮影响。
