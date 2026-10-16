# MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001：内部 universe no-go 与 crisp 修复

冻结 claims 计划为 `C-233`–`C-238`：

| claim | 精确范围 |
|---|---|
| `C-233` | 官方 Cambridge ZIP 的 13 个 Agda source 与 `README.agda` 导入闭包按 hash 固定；作者 Agda-flat 2.6.0.1 工具链从 `flat@70899fb` 构建。 |
| `C-234` | `IntUniv.fiberwise-fibrant-is-fibrant`：普通内部 weak classifier 会把逐点 fibrant family 提升为整体 fibration；`NoIntUniv` 在 interval transport 与 constant strict-equality fibrancy下导出 `⊥`。 |
| `C-235` | 官方源码分别实例化 CCHM 与 Cartesian Cubical composition，得到 `NoIntCCHMUniv` 与 `NoIntCCTTUniv`。 |
| `C-236` | crisp Theorem 5.2 在 path functor具有外部/tiny right adjoint的显式假设下构造 `U`、`El`、crisp `code`、`Elcode`、`codeEl` 与 `prf : Univ l`。 |
| `C-237` | Agda-flat modal control：crisp argument 版本通过；把同一 argument 改为 local variable 后被编译器拒绝，诊断固定为 `Variable x is declared top, so it cannot be used here`。 |
| `C-238` | `README.agda` 还重放相对 universe 版本与 Proposition 6.2；后者在已给定 universe classifiers/β/η 前提下构造 fibration-notion morphisms 的 identity/composition。 |

外部源码显式假设 `funext`、`uip`、非平凡 interval、cofibrancy；crisp 正向又显式假设 tiny/path-functor right adjoint的 `√/R/L/LR/RL/R℘`。Proposition 6.2 另显式假设相应 universe/`El`/`code`/β/η。kernel acceptance 证明这些假设下的推演与 modal typing，不证明这些 postulates 在任意 HoTT 模型中自动成立。

该双结果提供真实 natural consumer：将 fibrations 打包成 universe classifier，以支持内部模型构造、univalent universes、HIT 和 directed/cubical type theory。普通 internalisation 允许 `code` 吃入含 local `i : I` 的 pointwise fibration，进而错误提升 family fibrancy并坍缩 interval；crisp 版本要求被编码的 base/fibration 只依赖 global/crisp variables，机械禁止这次 substitution。

它是用户方向 A/B 的强实例候选，但仍需现实相对判别。当前可以机器支持“抽象掉来源层级会产生非现实推演，而重新保留 global/local 区分可恢复任务”；尚不能支持“basic HoTT 有 BUG”“学界未发现该问题”或“所有现实消费者都拒绝 crisp 支付”。
