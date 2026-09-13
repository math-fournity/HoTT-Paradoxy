# S-RES-20260913-072-N26-T3-CODE-IDENTITY

- 触发：S071 路由的 N26（T3 两条子义务之一：码级算术恒等式）。
- T3 第五脉冲（有界）：新增 `HoTT/formal/ercf3-t3/CodeCommutation.agda`——机器核查 `codeF (substF k i φ) ≡ φ⟨k/i⟩c` 的**定义性核心**（`bot` 与含数字的等式构造子，两例均由 `refl` 通过），并把比较相关的案例固定为剩余义务（明确不 postulate）。
- 运行：`agda --ignore-interfaces -i . CodeCommutation.agda` EXIT=0、stderr 0 字节、零 warning。
- 停止条件：不新增 claim 行；ERCF-3 本体保持 gated。
- 边界：未 commit/tag/push；三件套 revision 72/generation 056；core 不变。
