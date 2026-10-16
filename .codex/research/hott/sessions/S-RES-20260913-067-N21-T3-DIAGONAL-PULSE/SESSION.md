# S-RES-20260913-067-N21-T3-DIAGONAL-PULSE

- 触发：S066 路由的 N21（E6 复扫）+ C8 的 T3 义务（Gödel 编码/对角引理）。
- T3 脉冲（有界）：在 T2 语法包上用**纯 Agda builtins**新增 `DiagonalCore.agda`——具体编码 `code`、对角实例 `diagonalize φ = substF (code φ) 0 φ`、引号在编码上的表示引理与两个结构引理；`agda --ignore-interfaces -i . DiagonalCore.agda` EXIT=0、零 warning、stderr 空。
- 停止条件：ERCF-3 本体保持 gated；本脉冲**不新增 claim 行**（无 natural consumer），只作为 T3 义务的证据进展。
- 边界：不证明对角引理本体（仍需 Prov 可表示性）；未 commit/tag/push。
