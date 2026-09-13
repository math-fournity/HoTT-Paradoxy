# S-RES-20260913-116-ERCF3-T3-STREAMING-PARSER

- 目标「全部做完再停下」，第二线 T3 第十九脉冲：符号层 + 流式解析器 + 修复后的 Nat 值编码。
- 交付：`HoTT/formal/ercf3-t3/StreamingParser.agda`；canonical run `HoTT/verification/runs/20260913-MP-ERCF3-T3-STREAMING-PARSER-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（5 行冻结）；矩阵追加节（`C-173`–`C-176`）；
  `HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 `later_packages` 第 7 条（later claims 23→27）；`HoTT/formal/ercf3-t3/README.md` / `HoTT/formal/README.md` /
  `HoTT/verification/runs/README.md` 索引同步（两条 owner record revalidation 重绑）。
- 四条 claim：C-173 自定界一元索引层；C-174 符号层与燃料精确的流式解析器；C-175 长度对账/界即和分解/
  多余燃料分解；C-176 `codeT'` 带全解码器 `dec`、往返 ⇒ 单射（**编码层修复义务闭合**）。
- 边界：只覆盖 Tm 的编码/解码与单射性；不修复 `codeF` 实现、不重做旧 `codeT`/`codeF` 的对象层替换一致义务；
  不涉及 P 表示性/反射/对角不动点；ERCF-3 保持 `GATED`；历史脉冲文件逐字节未改；不 push。
