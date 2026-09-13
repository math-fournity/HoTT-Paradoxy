# S-RES-20260913-118-ERCF3-T3-REPAIRED-SYNTAX

- 目标「全部做完再停下」，第二线 T3 第二十一脉冲：修复编码之上的替换一致与引用。
- 交付：`HoTT/formal/ercf3-t3/RepairedSyntax.agda`；canonical run `HoTT/verification/runs/20260913-MP-ERCF3-T3-REPAIRED-SYNTAX-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（4 行冻结）；矩阵追加节（`C-181`–`C-183`）；
  `HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 `later_packages` 第 9 条（later claims 31→34）；`HoTT/formal/ercf3-t3/README.md` / `HoTT/formal/README.md` /
  `HoTT/verification/runs/README.md` 索引同步（两条 owner record revalidation 重绑）。
- 三条 claim：C-181 项层码级替换一致；C-182 公式层同型；C-183 引用单射 + 对角实例 + 其码。
- 诚实边界：码级替换经解码器定义（解码—替换—编码），不主张对象理论可表示该替换/引用。
- 交叉核对：`BitCoding`/`StreamingParser`/`FormulaCoding` 的哈希在各自注册 run、S117 run 与本 run 的
  `source-manifest.json` 中一致（逐字节未改）。
- 边界：不构造 P、不证表示性/反射/对角不动点（门 B）；ERCF-3 保持 `GATED`；不 push。
