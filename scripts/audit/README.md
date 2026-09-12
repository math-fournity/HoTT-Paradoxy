# 审计脚本

脚本分为原文派生、历史账本和验证三类。派生文件必须通过脚本重建；脚本不修改来源快照，不访问网络，不替代语义审计。

- `build_source_manifest.py`：源 repo、快照树、显式文件和移走路径 provenance。
- `build_core_cognition.py` / `verify_core_cognition.py`：三份 primary + Codex supplemental 的 core 账本和逐单元 hash 往返。
- `build_history_ledgers.py` / `verify_history_ledgers.py`：LocalGPT canonical trajectory、WebGPT sections、Gemini records、work products 和 claims。
- `build_core_cognition_audit.py`：为 session 生成全部 `KC-*` 的逐编号回评表；语义内容仍由当前 AI 负责。
- `initialize_cognition_head.py`：建立当前 mutable cognition state 的初始 HEAD receipt。
