# S-RES-20260913-069-N23-T3-DIAGONAL-BODY

- 触发：S068 路由的 N23（T3 对角引理本体）。
- T3 第三脉冲（有界）：新增 `HoTT/formal/ercf3-t3/DiagonalLemma.agda`——**编码上的替换函数** `_⟨_/_⟩c` 与 `substTc`（纯 Agda builtins，复用 DiagonalCore 的 code/codeF/codeT），即对角引理的算术心脏：对象语言可以用具体数字运算表示"替换后的公式编码"。
- 运行：`agda --ignore-interfaces -i . DiagonalLemma.agda` EXIT=0、stderr 0 字节、零 warning。
- 剩余义务：把该替换运算**反映**进谓词 `P`（即 `repr` 的算术化版本），才能得到对象层的 `φ ↔ ¬P(⌜φ⌝)`；ERCF-3 本体保持 gated，不新增 claim 行。
- 边界：未 commit/tag/push；三件套 revision 69/generation 053；core 不变。
