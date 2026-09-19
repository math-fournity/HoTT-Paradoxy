# S-RES-20260913-110-ERCF3-T3-JOINT

- 目标「全部做完再停下」：执行 FRONTIER 第二线（T3 共享判定联合递归），完成 F-011 全链。
- 交付：`HoTT/formal/ercf3-t3/README.md`；`HoTT/formal/ercf3-t3/JointRecursion.agda`；canonical run `HoTT/verification/runs/20260913-MP-ERCF3-T3-JOINT-001-02`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）；失败尝试 `HoTT/verification/runs/20260913-MP-ERCF3-T3-JOINT-001-01`（`--safe` pragma ⇒ `CoInfectiveImport`，保留）；
  矩阵追加节 `HoTT/CLAIM_EVIDENCE_MATRIX.md`（`C-157`–`C-159`）；`HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 `later_packages` 第 2 条（later claims 8→11）。
- 三条 claim：C-157 显式共享判定一致；C-158 原始逐出现判定的项层恒等式（N34 的剩余义务）；C-159 修正后的公式层恒等式
  （修正 `CodeStoreFixF` 的 `all` 影子分支双重编码）。
- 状态边界：不是 ERCF-3 本体（无 P 表示性/反射/对角不动点）；ERCF-3 保持 `GATED`；不使用 univalence/cubical Path/HIT/truncation；
  历史脉冲文件逐字节未改；不 push。
