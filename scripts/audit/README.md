# 审计脚本

脚本分为原文派生、历史账本和验证三类。派生文件必须通过脚本重建；脚本不修改来源快照，不访问网络，不替代语义审计。

- `build_source_manifest.py`：源 repo、快照树、显式文件和移走路径 provenance。
- `build_core_cognition.py` / `verify_core_cognition.py`：三份 primary + Codex supplemental 的 core 账本和逐单元 hash 往返。
- `build_history_ledgers.py` / `verify_history_ledgers.py`：LocalGPT canonical trajectory、WebGPT sections、Gemini records、work products 和 claims。
- `build_core_cognition_audit.py`：为 session 生成全部 `KC-*` 的逐编号回评表；语义内容仍由当前 AI 负责。
- `verify_three_way_cognition.py` / `test_three_way_cognition.py`：验证 `核心认知.md`→`方向追踪.md`→`全景视野.md` 固定顺序、projection revision、方向↔成果双向引用以及错序/孤儿负向场景。
- `build_understanding_merge_manifest.py` / `verify_understanding_merge.py`：对顶层与 nested 理解章节逐文件比较，记录 canonical 决定、唯一内容、回滚源和非破坏性验证。
- `build_cross_source_reconciliation.py` / `verify_cross_source_reconciliation.py`：逐项登记 WebGPT STATE 和 LocalGPT response/tool/work-product/claim ledger；规则路由不替代句级语义或数学认证。
- `verify_fresh_three_way.py`：在新 Python 进程中读取当前完整 load graph，验证三件套 EOF/hash 和 stale/incomplete/tampered 的 fail-closed 行为。
- `verify_projection_freshness.py`：只读核对当前 STATE revision、projection revision、core/merge/reconciliation hash 和 fresh receipt，避免旧 projection 被误当 current。
- `prepare_history_reconciliation_checkpoint.py`、`prepare_fresh_verification_checkpoint.py`：受控 runtime checkpoint 适配器；通过 runtime 原子写，不直接编辑 STATE/HEAD。
- `initialize_cognition_head.py`：建立当前 mutable cognition state 的初始 HEAD receipt。
