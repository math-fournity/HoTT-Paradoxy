# S-RES-20260912-028-ERCF-FACTORIZATION-LEAN

- 触发：MEMORY/方向/C4 把 ERCF-1/2 设为 F-011 下第一最小可验结果。
- 构造：在 `HoTT/formal/ercf-factorization/ERCF.lean` 固定一般 `Type` 值 `FactorsThrough`、`FiberConstant`、`ParadoxWitness`、E₀ 正反控制、subsingleton、分离观察族和 identity 控制。
- 运行：Lean 4.33.1 final run `20260912-MP-ERCF-001-02` exit 0；source/output/index hashes 通过；`verify_formal_proof_run.py --rerun` 为 `EXACT_EXIT_STDOUT_STDERR_MATCH`。
- 数学状态：`C-59`–`C-66 = MACHINE_PROVED_LOCAL_UNCOMMITTED`。没有 univalence/cubical Path/HIT/truncation，因此不是 HoTT 悖论；C4 整体仍 paper-only。
- 研究转向：E₀ 被排除为 coverage-gap 候选；下一步固定 HoTT 原生 truncation 或 quotient/HIT abstraction 及正/负 consumer，不直接跳 ERCF-3。
- 三件套：core `NO_CHANGE`；direction/panorama 更新到 revision 28，并新增 `OUT-TOP-ERCF-FACTORIZATION-LEAN`。
- Git：未 commit、未 tag、未 push。
