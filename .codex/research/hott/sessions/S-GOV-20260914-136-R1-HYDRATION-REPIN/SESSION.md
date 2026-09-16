# S-GOV-20260914-136-R1-HYDRATION-REPIN

- 发现：显式 `A-CUBICAL-MACHINE-HALTING-001` hydration 把零字节 `HoTT/verification/runs/20260914-MP-CUBICAL-MACHINE-HALTING-001-01/stderr.txt` 当作必读正文，runtime 返回 `EMPTY_REQUIRED_FILE`。
- 修复：空文件从 stable record 的 `full_sources/source_hashes` 移除；其 bytes/hash 仍由 `HoTT/verification/runs/20260914-MP-CUBICAL-MACHINE-HALTING-001-01/RUN.json` 保存。
- 同步：`scripts/audit/test_hott_programmatic_exploration_completeness.py` 更新为 R1 main 当前语义，5/5 PASS。
- 边界：C-188–C-190、run、索引与 S135 判词均未修改；下一 R2 不变。
