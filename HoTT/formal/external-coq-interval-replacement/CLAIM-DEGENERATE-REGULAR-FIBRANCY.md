# MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001：regular replacement 不相容与 degenerate replacement 恢复

| claim | 精确范围 |
|---|---|
| `C-239` | `emptyctx@28a2568` 的 `InternalCubical-Coq` 20 文件 subtree、git tree、归档、Coq 8.13.2 image 与项目 probe 被固定；目标闭包从新目录编译。 |
| `C-240` | `Inconsistency.Unnamed_thm : False` 在显式 `repl/η/repl_rec'/RFib_repl` 以及 interval/cofibration/equality公理下通过；`Print Assumptions` 固定 regular-family replacement 依赖。 |
| `C-241` | `FibRepl.Fib_repl`、`repl_ind'`、`repl_rec'` 与 functor laws 从 private inductive/QIT `repl` 和 reduction axiom `qq` 编译；它只自由加入 degenerate composition。 |
| `C-242` | `Fibrations.RFib_DFib`、`RFib_Trans`、`TransFib_HFib` 机器给出 regular fibrancy 与 `DFib + Trans` 的双向分解。 |
| `C-243` | `repl_ind'` 要求 motive `RFib`；`repl_J` 的假设闭包额外出现 `extension_rule__emptyctx`。同一源码由此机械区分可替换的局部/退化结构、保留 transport 后的 regular family 与仅空 context 的扩张。 |

该对照支持一个真实消费者：论文用 replacement 构造 universe of all types 上的 weak factorisation/model structure与 HIT。当前 replay 只闭合 negative `Inconsistency.v`、positive `FibRepl.v`、fibrancy decomposition 和 assumptions probe；`Model_structure.v` 在 Coq 8.13.2 的一个旧式隐式 placeholder 处无法推断，而 source history明确写有 Coq 8.10 compatibility。该版本差异单独保留，不能把部分目标通过写成完整 model-structure theorem 重放。

这与 C-227–C-238 共同说明：可用 replacement 并非被完全放弃；社区通过弱化为 degenerate/local fibrancy、显式保留 transport、限制 motive 或 context 来支付 uniform internalisation 的代价。它仍是已发表方法，不是新发现的 basic HoTT 矛盾；现实同任务桥梁与“支付是否破坏消费者目标”仍需单独判定。
