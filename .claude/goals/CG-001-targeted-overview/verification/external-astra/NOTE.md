# 外部运行的复核记录（Astra 的 Markov 链）

> Claude（Opus 5.5），会话 91a6cdaa，2026-09-25。用途：CN-024 引用 Astra 的 C-319、C-322、C-324 时，记录本会话实际做过的校验。这些运行属于共享矩阵（已登记），本目录只存校验器的输出，不改动 `HoTT/verification/runs/` 下的任何文件。

| 运行 | 命题 | 本会话校验 | 结果 |
|---|---|---|---|
| `20260920-MP-ASTRA-NATIVE-MOTION-BUNDLE-001-01` | C-318、C-319 | 规范校验器，不重放 | `PASS_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；其模块作为依赖在下一行的重放中被重新检查 |
| `20260921-MP-ASTRA-WEAK-COVERAGE-MARKOV-001-01` | C-321、C-322 | 规范校验器 `--rerun` | `PASS_WITH_SCOPE`，`EXACT_EXIT_STDOUT_STDERR_MATCH` |
| `20260921-MP-ASTRA-MARKOV-REVERSE-001-01` | C-323、C-324 | 规范校验器 `--rerun` | `PASS_WITH_SCOPE`，`EXACT_EXIT_STDOUT_STDERR_MATCH` |

校验器：`scripts/audit/verify_formal_proof_run.py`（共享矩阵索引检查在内）。原始输出：同目录 `*.canonical-check.json`、`*.canonical-rerun.json`。
