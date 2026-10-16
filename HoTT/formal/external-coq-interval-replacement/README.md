# Boulier–Tabareau interval type theory replacement 正负对照

本包重放 Simon Boulier 与 Nicolas Tabareau 的 `InternalCubical-Coq` 源码切片，固定论文所指 `emptyctx` branch commit `28a256848a134d9111a2f332083b3d3ff35a58d3`。

- paper：*Model structure on the universe of all types in interval type theory*，DOI `10.1017/S0960129520000213`
- source：`https://gitlab.inria.fr/sboulier/thesis-formalizations.git`
- source subtree：20 文件 / 177,150 bytes / git tree `51ec7ae99395e8db73d2b48c6c4658df32dfd36e`
- license boundary：该 subtree 未发现 license 文件，本项目不复制其正文，只保存 hash manifest、外部 archive identity、项目 probe 与运行收据
- proof ID：`MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001`
- planned claims：`C-239`–`C-243`

负向 `Inconsistency.v` 假设 regular family replacement 并导出 `False`；正向 `FibRepl.v` 以 private inductive/QIT reduction 构造只保证 degenerate fibrancy 的 replacement。`Fibrations.v` 把 regular fibrancy分解为 degenerate fibrancy加 transport，`repl_ind'` 只允许 regular-fibrant motives，`repl_J` 另显式依赖 `extension_rule__emptyctx`。精确主张和禁止外推见 `CLAIM-DEGENERATE-REGULAR-FIBRANCY.md`。
