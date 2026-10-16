# run 20260924-CG001-MEASUREMENT-LOG-01：作废记录

- 捕获：内核接受（exit 0，stderr 0 B），见 `HoTT/verification/runs/20260924-CG001-MEASUREMENT-LOG-01/`。
- 第一次目标内校验（源码未改时）的原始错误输出，抄自执行会话 bb204ea1 的工具输出：
  `{"status": "FAIL", "error": "ProofRunError: AGDA_UNSAFE_MARKER:HoTT/formal/claude-cg001/measurement-log/MeasurementLog.agda:postulate"}`
  原因：目标内校验器比规范校验器多一条子串标记 `postulate`，命中了源码头注释里的 “never postulated”。源码在 `--safe` 下本来就不能有公设。
- 处理：没有放宽校验器；把注释改为 “never assumed as an axiom”，重捕获为 `20260924-CG001-MEASUREMENT-LOG-02`。
- 第二次目标内校验（改注释之后）的输出在同目录 `20260924-CG001-MEASUREMENT-LOG-01.verify.err`：`SOURCE_HASH_OR_SIZE_MISMATCH`。这是预期结果，因为本 run 的清单记录的是改注释之前的源码哈希。第一次的错误输出被这次覆盖，所以抄在上面。
- 同目录 `…-01.verify.json` 为空（失败时 stdout 无输出）；`…-01.canonical.out` 是第一次规范校验的输出（`RUN_NOT_INDEXED`）。
- 本 run 不作为任何命题的证据。
