# 审计脚本

脚本分为原文派生、历史账本和验证三类。派生文件必须通过脚本重建；脚本不修改来源快照，不访问网络，不替代语义审计。

- `build_source_manifest.py`：源 repo、快照树、显式文件和移走路径 provenance。
- `core-cognition-curation-v3.json`：HUMAN_EDITED 的 88 条 primary message 逐项处置与 27 个精确语义范围 owner。
- `build_core_cognition.py` / `verify_core_cognition.py`：默认 check、显式 `--write` 的 generation-3 manager；只从三份 primary 复制直接用户原文，并验证 913/913 generation transition。supplemental/AI relay 只留历史。
- `build_history_ledgers.py` / `verify_history_ledgers.py`：LocalGPT canonical trajectory、WebGPT sections、Gemini records、work products 和 claims。
- `build_core_cognition_audit.py`：为 session 生成全部 `KC-*` 的逐编号回评表；语义内容仍由当前 AI 负责。
- `verify_three_way_cognition.py` / `test_three_way_cognition.py`：验证 `核心认知.md`→`方向追踪.md`→`全景视野.md` 固定顺序、projection revision、方向↔成果双向引用以及错序/孤儿负向场景。
- `build_understanding_merge_manifest.py` / `verify_understanding_merge.py`：对顶层与 nested 理解章节逐文件比较，记录 canonical 决定、唯一内容、回滚源和非破坏性验证。
- `build_cross_source_reconciliation.py` / `verify_cross_source_reconciliation.py`：逐项登记 WebGPT STATE 和 LocalGPT response/tool/work-product/claim ledger；规则路由不替代句级语义或数学认证。
- `verify_fresh_three_way.py`：在新 Python 进程中完整读取 governance/research profile，验证三件套 EOF/hash、冷资产不常驻、stable task hydration 和 stale/incomplete/tampered/profile-mismatch；不调用模型。
- `verify_projection_freshness.py`：只读核对当前 STATE revision、projection revision、core/merge/reconciliation hash 和 fresh receipt，避免旧 projection 被误当 current。
- `prepare_history_reconciliation_checkpoint.py`、`prepare_fresh_verification_checkpoint.py`：受控 runtime checkpoint 适配器；通过 runtime 原子写，不直接编辑 STATE/HEAD。
- `initialize_cognition_head.py`：建立当前 mutable cognition state 的初始 HEAD receipt。

## 分片逻辑文档（governance-shard-index/v2）

- `validate_governance_shards.py`：pin 的共享 3.16.0 候选校验器副本（source commit `2e4e4d2`，source sha256 `fb75648…`）。不要在项目内手改；共享主库打 `governance-v3.16.0` 后从主库重新同步并更新 provenance 头。
- `verify_governance_shards.py`：包装器，校验副本 sha256（漂移即 `VALIDATOR_PINNED_COPY_DRIFT` 并退出 1），执行 `--scan <repo>` 并输出 `governance-shard-verification/v1` receipt。
- `shard_migrate_document.py`：一次性迁移工具，按标题边界把既有单文件拆成 v2 索引 + `NNN - 子主题.md` 分片，并输出标题/行对账（默认 dry-run；`--apply` 才写）。
- 合同与判定标准见 `docs/quality/长治理文档分片与索引合同.md`；300 行是软目标，不是上限。

## 历史 prepare 脚本（FREEZE 说明）

- `prepare_*.py` 中约 58 个是**逐 revision 一次性 receipt**：各自 pin 了当时的 `expected_sha256` 与 `STATE.revision`，只对其目标 revision 有效，现在重新运行必然 stale。它们作为历史证据保留，不批量改写、不重新运行。
- 迁移 `MEMORY.md`/分片结构后，新的 checkpoint 必须使用当前 runtime（3.3.0）与新的 prepare 适配器；历史 receipt 记录的是当时的路径与 hash，不因结构迁移而失效，也不被追溯改写。
