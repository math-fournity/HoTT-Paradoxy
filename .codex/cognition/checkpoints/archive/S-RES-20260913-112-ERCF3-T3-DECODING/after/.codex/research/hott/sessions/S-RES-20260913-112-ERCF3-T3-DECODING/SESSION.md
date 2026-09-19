# S-RES-20260913-112-ERCF3-T3-DECODING

- 目标「全部做完再停下」，第二线 T3 第十五脉冲：编码可解码性/单射性围栏。
- 交付：`HoTT/formal/ercf3-t3/DecodingFence.agda`；canonical run `HoTT/verification/runs/20260913-MP-ERCF3-T3-DECODING-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`；矩阵追加节（`C-160`–`C-162`）；
  `HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 `later_packages` 第 3 条（later claims 11→14）；`HoTT/formal/ercf3-t3/README.md` 的包清单与专节；
  `HoTT/formal/README.md` / `HoTT/verification/runs/README.md` 索引同步（两条 owner record revalidation 重绑）。
- 三条 claim：C-160 编码非单射（`var 2`/`num 0` 碰撞，无单射解码器）；C-161 公式层同碰撞；C-162 数字片段正控制。
- 结论：`ObjectSyntax` 记录的 decodability/injectivity 义务**不能被当前编码满足**；修复（标签值域不相交或列表编码）是下一有界脉冲。
- 边界：不给修复方案；不涉及 P 表示性/反射/对角不动点；ERCF-3 保持 `GATED`；不改写历史脉冲文件与 `⌜-injective` 命名；不 push。
