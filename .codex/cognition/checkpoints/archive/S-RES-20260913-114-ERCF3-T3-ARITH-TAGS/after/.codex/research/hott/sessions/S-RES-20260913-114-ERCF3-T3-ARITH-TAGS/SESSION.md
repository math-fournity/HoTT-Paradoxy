# S-RES-20260913-114-ERCF3-T3-ARITH-TAGS

- 目标「全部做完再停下」，第二线 T3 第十七脉冲：修复编码的算术半第一片。
- 交付：`HoTT/formal/ercf3-t3/ArithmeticTags.agda`；canonical run `HoTT/verification/runs/20260913-MP-ERCF3-T3-ARITH-TAGS-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`；矩阵追加节（`C-166`–`C-168`）；
  `HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 `later_packages` 第 5 条（later claims 17→20）；`HoTT/formal/ercf3-t3/README.md` / `HoTT/formal/README.md` /
  `HoTT/verification/runs/README.md` 索引同步（两条 owner record revalidation 重绑）。
- 三条 claim：C-166 偶/奇标签算术（`double` 单射、`double n ≢ odd m`）；C-167 var/num 片段 Nat 值编码单射；
  C-168 非满射（`1` 无原像）⇒ 全解码器需缺省分支。
- 边界：只覆盖 var/num 片段；应用结点、配对函数、全解码器与往返未做；不涉及 P 表示性/反射/对角不动点；
  ERCF-3 保持 `GATED`；不改写历史脉冲文件；不 push。
