# S-RES-20260913-117-ERCF3-T3-FORMULA-CODING

- 目标「全部做完再停下」，第二线 T3 第二十脉冲：修复编码的公式层（复用项层解码器）。
- 交付：`HoTT/formal/ercf3-t3/FormulaCoding.agda`；canonical run `HoTT/verification/runs/20260913-MP-ERCF3-T3-FORMULA-CODING-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（5 行冻结）；矩阵追加节（`C-177`–`C-180`）；
  `HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 `later_packages` 第 8 条（later claims 27→31）；`HoTT/formal/ercf3-t3/README.md` / `HoTT/formal/README.md` /
  `HoTT/verification/runs/README.md` 索引同步（两条 owner record revalidation 重绑）。
- 四条 claim：C-177 公式符号层与迭代数精确的流式 `run`；C-178 项层解析器复用（燃料=剩余位数）；
  C-179 长度对账 `STEPS φ ≤ LEN (bitsF φ)`；C-180 `codeF'` 带全解码器 `decF`、往返 ⇒ 单射。
- 交叉核对：`BitCoding.agda` 与 `StreamingParser.agda` 的哈希在各自注册 run 与本 run 的 `source-manifest.json` 中一致
  （逐字节未改）。
- 边界：只覆盖 `Fml` 的编码/解码与单射性；不做公式层替换对齐、`⌜·⌝` 算术化、P 表示性/反射/对角不动点；
  ERCF-3 保持 `GATED`；不 push。
