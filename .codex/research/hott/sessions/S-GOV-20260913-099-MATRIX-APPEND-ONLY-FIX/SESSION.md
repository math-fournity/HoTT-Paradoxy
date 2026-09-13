# S-GOV-20260913-099-MATRIX-APPEND-ONLY-FIX

- 背景：S098 吸收外部工作时把 `MP-VERIFICATION-EVENT-001` 的 9 行插在 C-148 之后；`verify_proof_version_closure.py` 报
  `CURRENT_MATRIX_NOT_APPEND_ONLY_SUCCESSOR`（要求当前矩阵以 d3dfb0e 快照为前缀）。
- 修正：把 9 行**按字节原样**移到文末新追加节（不重写任何旧行、不改冻结前缀）；行文本不变使旧 run 的
  `index-row-manifest` 仍判 `ROW_STABLE_AFTER_INDEX_EVOLUTION`。
- 复核：`verify_proof_version_closure.py` → `PASS_WITH_SCOPE`（frozen 17 + later 1 / 8 claims）；
  `verify_formal_proof_run.py --rerun` → `PASS_WITH_SCOPE`、`ROW_STABLE_AFTER_INDEX_EVOLUTION`、`EXACT_EXIT_STDOUT_STDERR_MATCH`。
- 教训写入 LESSONS 第 78 条；本 checkpoint 只同步三件套 revision 字段（98→99）与顺序日志。不 push。
