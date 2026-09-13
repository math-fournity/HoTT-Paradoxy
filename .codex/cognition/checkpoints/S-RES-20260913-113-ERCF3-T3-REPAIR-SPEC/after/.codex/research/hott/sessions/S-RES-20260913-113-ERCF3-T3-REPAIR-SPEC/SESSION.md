# S-RES-20260913-113-ERCF3-T3-REPAIR-SPEC

- 目标「全部做完再停下」，第二线 T3 第十六脉冲：编码修复规格。
- 交付：`HoTT/formal/ercf3-t3/CodingRepair.agda`；canonical run `HoTT/verification/runs/20260913-MP-ERCF3-T3-REPAIR-SPEC-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`；矩阵追加节（`C-163`–`C-165`）；
  `HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 `later_packages` 第 4 条（later claims 14→17）；`HoTT/formal/ercf3-t3/README.md` / `HoTT/formal/README.md` /
  `HoTT/verification/runs/README.md` 索引同步（两条 owner record revalidation 重绑）。
- 三条 claim：C-163 结构化树编码往返 ⇒ 单射（正控制）；C-164 往返 ⇒ 单射的通用规格引理；C-165 当前 `codeT` 无解码器。
- 结论：修复义务固定为“Nat 值编码 + 解码器 + 往返证明”；**结构半完成、算术半待做**（配对/列表编码 + 算术引理）。
- 边界：不给 Nat 值修复编码本身；不涉及 P 表示性/反射/对角不动点；ERCF-3 保持 `GATED`；不改写历史脉冲文件；不 push。
