# project-local governance v3.3.0：文档分片迁移（CP-2 证据）

> 会话：`S-GOV-20260913-095-DOC-SHARD-MIGRATION`（revision 95）
> 范围：把 6 个活跃且混装的逻辑文档迁为 v2 索引 + 有序分片；不改任何 KC、数学判词、proof source/run/index
> 回滚边界：annotated tag `governance-v3.2.0-pre-sharding`（commit `4022206`，迁移前的最后一个单文件状态）
> 不 push；`governance-v3.3.0` 只在本 checkpoint 提交后指向本地 commit

## 1. 迁移结果

| 逻辑文档 | 模式 | 分片 | 正文行数 | 对账 |
|---|---|---|---|---|
| `README.md` | topical | 4（入口 / 历史交接包 / 加载与验证 / 交换·归档·接手） | 228 | 拼接 == boundary tag（逐字节） |
| `MEMORY.md` | sequential（`append_target`=`MEMORY/003`） | 3（当前执行队列 / 当前证据上限与恢复入口 / 当前验证状态与顺序日志） | 105 | 每片为原文连续切片；因顺序日志需作为末片而重排片序，按逐行多重集对账 |
| `理解章节/C1-后续研究方向独立复审-20260912.md` | topical | 4 | 455 | 拼接 == boundary tag |
| `理解章节/C2-历史悖论谱与HoTT处理机制全解-20260912.md` | topical | 6 | 676 | 拼接 == boundary tag |
| `理解章节/C3-HoTT悖论后续主攻方向与判别路线-20260912.md` | topical | 5 | 522 | 拼接 == boundary tag |
| `理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md` | topical | 6 | 773 | 拼接 == boundary tag |

合计 6 个索引 + 28 个分片。所有 canonical 路径不变，旧链接、旧 run receipt 与 STATE record path 继续有效。
分片标题采用可读短名，原始 H2 标题保留在每片的正文内与索引的“语义范围”列。

独立复核（`scripts/audit/logical_document.py`）：`README`/`C1`/`C2`/`C3`/`C4` 五个逻辑文档按索引顺序重建的正文，
与 `governance-v3.2.0-pre-sharding` 版本**逐字节相同**；`MEMORY` 按逐行多重集相同（每片仍是原文连续切片）。

## 2. 加载链与 consumer 同步

- `.codex/tools/cognition_runtime.py` 3.3.0：`plan` 展开逻辑文档（索引 + 按 table 顺序全部分片，逐片 hash/bytes/lines、
  `logical_id`/`logical_role`/`full_load`、`plan.logical_documents`）；`check` 必须覆盖每一片；`MEMORY` 的三片同时进入
  `HEAD.json.tracked`，与索引在同一原子事务写入。
- `scripts/audit/build_history_ledgers.py`：claim 枚举改按逻辑文本（索引 + 全部分片），避免未来重建时丢掉 C1–C4 的
  ~2,400 条句级 claim；本次**未重建** ledger，历史 receipt 保持 point-in-time。
- `scripts/audit/build_understanding_merge_manifest.py` / `verify_understanding_merge.py`：逐文件比较改用逻辑文本，
  并新增 `logical_sha256` 校验；`top`/`nested` 目录枚举只取文件（分片目录不是章节）。重建后计数不变：
  union 35、same-name 24、identical 15、different 9、top-level unique 11、unresolved 0。
- STATE re-pin：`audit/understanding-chapter-merge-manifest.json`（14 条 record）、`理解章节/C3`（2 条）、`理解章节/C4`（8 条）
  的全部 source hash 在同一 checkpoint 内更新，并写入 `revalidation`（说明这是载体分片而非主张变化）。
- 复核：对上述 10 个 record 逐一跑 `plan --profile research --task <ID>`，`review_required` 中**没有新增** stale；
  剩下的 8 个 `REVIEW_REQUIRED` record 在 boundary tag 时已是同一集合。

## 3. 验证

| 检查 | 结果 |
|---|---|
| `verify_governance_shards.py`（pin 校验器） | `PASS`；indexes=7（6 canonical + 1 个 CP-2 checkpoint after 副本）、notices=0、`line_targets_blocking=false` |
| runtime 单测 | `Ran 37 tests ... OK`（含 5 条分片负向测试：展开顺序、缺片、孤儿/未列片、标记不一致、`HEAD` 跟踪、`SHARD_NOT_IN_CHECKPOINT`） |
| fresh 冷启动 | `PASS_WITH_SCOPE`，revision 95，governance_documents=22、research_documents=27、4 项负向用例通过 |
| projection freshness / three-way | `PASS_WITH_SCOPE` / `PASS`（revision 95 = 投影 revision） |
| math proof Gate 结构 | `PASS_WITH_SCOPE`（`HoTT/CLAIM_EVIDENCE_MATRIX.md` 未被分片） |
| merge / core / cross-source / history | 全部 `PASS`/`PASS_WITH_SCOPE` |
| canonical checkpoint | `.codex/cognition/checkpoints/S-GOV-20260913-095-DOC-SHARD-MIGRATION/result.json` = `CHECKPOINT_COMMITTED`（revision 95） |

## 4. 执行中发现的真实缺陷与修正

首轮迁移把分片目录写到了仓库根（`README/`、`C1-…/`），因为工具按仓库根解析 shard 路径，而规范与 validator
都要求 shard 路径**相对索引所在目录**解析。只按仓库根解析时，根目录文档（README/MEMORY）会通过、子目录文档
（`理解章节/C*`）会静默失败——正是 runtime 的 hydration 首次暴露了 `MISSING_OR_UNREADABLE`。

处置：错误产物移出仓库（`/tmp/hott-shard-misfire-20260913/`，未提交）；5 个受影响文件用
`git restore --source=governance-v3.2.0-pre-sharding` 精确还原并核对 SHA 后重做；`parse_shard_index` 与迁移工具同时
修正为“按索引目录解析 + 归一化为仓库相对路径”；该教训写入 `.codex/research/hott/LESSONS.md` 第 74 条。

第二处回归（提交前由最终验证发现）：曾在 `理解章节/README.md` 加一行 C 系列分片说明，但该文件是 merge manifest 的
`top_level` 条目之一，修改使 manifest 的 `top_level.sha256` 失效，`verify_understanding_merge` 与
`verify_projection_freshness` 同时报 `TOP_HASH_MISMATCH:README.md` / `MERGE_SOURCE_STALE:README.md:top_level`。
处置：回退该行（分片路由信息已由合同 §7、根 `AGENTS.md`、`README.md` 与 `MEMORY.md` 索引承担），
避免为一行注释再开第三个 checkpoint 重签 14 条 record；回退后两个验证器立即恢复 `PASS`。
结论：**`理解章节/*` 的当前内容与 merge manifest 是互相 pin 的一对，任何编辑都必须连同 manifest 重建与 STATE re-pin 一起做。**

第三处回归（发布后调查"未来 AI 如何驾驭分片"时发现，已修并移动本地 tag）：
本项目合同文档 `docs/quality/长治理文档分片与索引合同.md` 在第 39 行的示例代码块里**逐字引用**了
`<!-- governance-shard-index:v2`。共享 validator 只扫描前 20 行（示例不在窗口内），因此结构检查一直 PASS；
但 runtime/审计辅助的 `parse_shard_index` 原本扫描全文，于是把该合同误判成索引，并在 S094/S095 两个
session record 的 `full_sources` 水合时直接 `BLOCKED: SHARD_INDEX_LAST_SHARD_MISMATCH`。

处置：把"是索引"的判定窗口统一为与共享 validator 相同的**前 20 行**（真索引的 marker 恒在第 1 行；
spec 也要求索引文件顶部包含该块），并在 runtime 单测中加入回归用例
`test_quoted_marker_in_documentation_is_not_an_index`。修复后：38/38 单测通过；S094/S095 两个 record 的
research hydration 恢复正常（docs=35，logical=[README×4, MEMORY×3]）；validator 仍 PASS（indexes=7）。
教训：**文档中"逐字举例"与"真实标记"必须由解析层的定位规则区分；解析窗口必须与 canonical validator 对齐。**

## 5. C01–C10 影响分类（本轮增量）

| ID | 判定 | 说明 |
|---|---|---|
| C01 | NO_CHANGE | 需求与用户裁定已在 CP-1 记录（rulings §17、F-013）；本轮只升级 F-013 交付状态 |
| C02 | UPDATE | 逻辑文档的真值 owner 与读取语义在合同中细化（含 checkpoint 副本计数口径） |
| C03 | NO_CHANGE | Skill/协议文本未改；只按已有分片规则执行 |
| C04 | UPDATE | `理解章节/README.md` 增加 C 系列分片路由说明 |
| C05 | UPDATE | Feature F-013 交付状态、README/MEMORY 载体、merge manifest 与 STATE hash 同步 |
| C06 | UPDATE | 迁移对账 + 逻辑文本校验进入 `verify_understanding_merge.py`；runtime 负向测试沿用 |
| C07 | NO_CHANGE | 未改 config/Rules/Hooks/权限/secret |
| C08 | NO_CHANGE | 共享主库未改；3.16.0 仍为候选 |
| C09 | UPDATE | `governance-v3.3.0` 本地 annotated tag（不 push）、回滚边界 `governance-v3.2.0-pre-sharding` |
| C10 | UPDATE | LESSONS 第 74 条记录路径解析缺陷；残余未知见下 |

## 6. 残余未知与边界

- **fresh model behavior NOT_RUN**：只证明结构与字节层行为；未来模型是否按分片正确读写仍需真实 Session 观察。
- **第二波保留项**（触发条件见合同 §7）：三件套 `核心认知.md`/`方向追踪.md`/`全景视野.md`、
  `HoTT/CLAIM_EVIDENCE_MATRIX.md`（行级 proof 收据耦合）、`HoTT/HoTT研究三问…md`、
  `docs/quality/数学结论机器证明与证据留存规范.md`。
- **历史 receipt 不自洽的旧路径不受影响**：58 个逐 revision 的一次性 `prepare_*.py` 已冻结说明（不重跑、不批量改写）。
- 数学目标、E6 consumer、T3 联合递归等研究状态不受本轮影响；未新增或修改任何数学结论。
