# Foundation Lean 第一不完备性 R3 重放包

本目录是 `GZ-002 / G0-R3-FOUNDATION-001` 的外部 FormalizedFormalLogic/Foundation 重放包。
它固定 [Foundation](https://github.com/FormalizedFormalLogic/Foundation) commit
`f3972f4204fc61e1b736ed843415894c83f35508`，并检查
`Foundation.FirstOrder.Incompleteness.First` 所导出的 Gödel第一不完备性声明。

本包的作用是为 `G0-R3` 提供一个不依赖 Coq/Docker 的独立 Lean kernel 对照：

- `Qualification.lean` 检查第一不完备性、r.e. 变体和两个“真但不可证”存在定理，并打印其 kernel axioms；
- `WrongMissingSoundness.lean` 故意省略 `T.SoundOnHierarchy 𝚺 1`，应在该 typeclass 前提处被拒绝；
- `capture_foundation_incompleteness_run.py` 固定外部 source、Lake 配置、Lean/Lake 二进制、主 build 和主／负检查运行。

这是一阶算术理论的 R3 基准。它不把 `ArithmeticTheory` 实例化为 exact HoTT calculus，也不建立
`Accept_ZFC`、`OriginDone`、`SameFullQ` 或 bare ZFC 的理论精度结论。

精确命题及禁止外推见 [CLAIM-R3-FOUNDATION-INCOMPLETENESS.md](CLAIM-R3-FOUNDATION-INCOMPLETENESS.md)。
