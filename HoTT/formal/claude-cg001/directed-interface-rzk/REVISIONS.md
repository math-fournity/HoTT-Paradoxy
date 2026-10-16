# directed-interface-rzk 的修订记录

> 本包 `CLAIM.md` 已入运行收据的哈希（`20260925-CG001-DIRECTED-INTERFACE-01`、`-NEG-01`），不改原文；修订记在这里。形式命题 C-57 与负控制不受影响。

## 2026-09-25 · 会话 91a6cdaa（Terra 复审 013 §2.4、T-027；CN-031；回信 014）

1. **标签**（接受）：`RZK_TYPECHECKED_RELATIVE_TO_EXPLICIT_DIRECTED_UNIVALENCE_INTERFACE / ACTUAL_TT_BOXSLASH_CONSTRUCTION_NOT_REPLAYED`。C-57 是接口层面的条件式比较：不是 GWB 的 TT_□ 构造在 Rzk 中的重放，也没有具体的 `Nat ∈ S` 见证；“同一个演算”指 sHoTT 加显式假设，不指完整的 TT_□。
2. **两镇往返**（接受 Terra 的指正，并用证明补上）：C-57 的箭头分支是自箭头 `Gl A A s` 走两次，不是 `A → B → A`。C-58（`two-town-rzk/`）把两镇任务写定一次，两种步子跑同一个任务；C-57 的 (a)、(b) 在其中作为 `A = B` 的特例被推出。
3. **GWB 的编号**（对辩，不更改原编号）：本包沿用 GWB v2 PDF 的编号——引理 5.11、定理 6.13、定义 6.14、引理 6.15、引理 6.16、推论 3.20——它们是正确的。arXiv v2 HTML 未渲染与定理共用计数器的 Remark 6.6、Notation 6.7、Remark 6.9（第 3、5 节亦有同类环境），编号因此少 3（第 3 节少 6，第 5 节少 1 或 2）：HTML 中分别为 5.10、6.10、6.11、6.12、6.13、3.14。今后引用写“PDF 编号（HTML 编号）”。回源记录见 CN-031 §2。
4. **复合的来源**（自查更正）：`coe-comp`（复合的协变运输是运输的复合）最直接的来源是 GWB 推论 6.17（HTML 6.14：S 中态射的复合由普通函数复合实现）；引理 6.16（HTML 6.13：S 是 Segal 的）给出复合的存在。原文“引理 6.16 与 RS17 的函子性”改为“引理 6.16、推论 6.17（RS17 函子性为旁证）”。
