# pedometer-ablation 的修订记录

> 本包 `CLAIM.md` 已入运行收据的哈希（`20260925-CG001-PEDOMETER-ABLATION-01`、`-NEG-01`、`-NEG-02`、`-NEG-03`），不改原文；措辞修订记在这里。形式命题 C-49–C-51 与负控制不受影响。

## 2026-09-25 · 会话 91a6cdaa（Terra 复审 009 的 O-027、O-028、O-029；CN-030；回信 012）

**修订**：
1. **C-49 的量词**（O-028）：解读第 2 条“哪种 HoTT 建模都躲不开的一点”过宽，改为：凡把携带完全写成沿恒等路径的运输（P-carry）、并要求对全部这类路径单调的建模，都躲不开。台账、选项 C、C-50 都不在其量词内。
2. **C-49 (e) 与 C-50 的命名**（O-027）：
   - “反向行走”“读数为 −1 的行走”改为形式名 `FORMAL_SIGNED_INVERSE_ACTION_WITH_SCOPE`：`sym go` 的运输作用为前驱。
   - 把它读作“一次 −1 步的行走”，只在 T2（每条路径都是一次行走）之下成立，是解释。
   - 另据 Darcs 文档（`obliterate`、`unrecord` 从仓库删除已记录的补丁），在版本控制领域，有符号计数沿逆操作减少可以是真实的，所以 −1 是否非现实取决于领域，不作一般主张。
3. **两难改为三支**：解读第 3 条的两难不穷尽。第三支（Terra 009 的选项 C）是：实际事件只取生成元 `go`、`back`，`sym go` 是群胚补全的逆。它的代价见 C-56（`pedometer-semantics/`）：方向是附加结构。
4. **有向线的名字**（O-029）：
   - “强形式有核心理论层面的消融”撤回，改为分层的结构对照：模型层 C-51、C-52，sHoTT 定位 C-53，来源 GWB。
   - 进一步更正：有向理论没有去掉 P9，同一演算中路径仍然可逆；准确的名字是“过程原语的切换”（恒等路径还是箭头）。
   - 同一演算、相对于显式有向单价接口的检验见 C-57（`directed-interface-rzk/`）。

**依据**：`HoTT/formal/claude-cg001/pedometer-semantics/CLAIM.md`、`directed-interface-rzk/CLAIM.md`；[darcs.net/Using/Commands](https://darcs.net/Using/Commands)；Terra 009 §5–§6。
