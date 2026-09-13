# S-RES-20260913-115-ERCF3-T3-BIT-CODING

- 目标「全部做完再停下」，第二线 T3 第十八脉冲：修复编码的算术半第二片（位级底座与燃料界）。
- 交付：`HoTT/formal/ercf3-t3/BitCoding.agda`；canonical run `HoTT/verification/runs/20260913-MP-ERCF3-T3-BIT-CODING-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（5 行冻结）；矩阵追加节（`C-169`–`C-172`）；
  `HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 `later_packages` 第 6 条（later claims 20→23）；`HoTT/formal/ercf3-t3/README.md` / `HoTT/formal/README.md` /
  `HoTT/verification/runs/README.md` 索引同步（两条 owner record revalidation 重绑）。
- 四条 claim：C-169 数字算术（`parity`/`half`/`twice`）；C-170 `codeBits`/`unbits` 两侧引理；
  C-171 已知长度往返 `unbits (LEN bs) (codeBits bs) ≡ bs`；C-172 码支配自身长度 `suc (LEN bs) ≤ codeBits bs`。
- 边界：只覆盖位列表编解码与长度界；符号层、解析器与全解码器未做；往返只在已知长度上成立；
  不涉及 P 表示性/反射/对角不动点；ERCF-3 保持 `GATED`；不改写历史脉冲文件；不 push。
