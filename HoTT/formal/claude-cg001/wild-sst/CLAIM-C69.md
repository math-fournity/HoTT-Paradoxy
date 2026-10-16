# 六边形相干的公式对不对：圆周值结构上，Coh₂ 恰好是绕数的上闭链方程（C-69）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325；目标包 CG-003，完成门 G2。与 C-64 同包，原样使用 C-64 的 `WildSST` 与 `Coh₂`。
>
> - proof id：`MP-CG001-WINDING-COCYCLE-001`（`WindingCocycle.agda`）。
> - 负控制：`MP-CG001-WINDING-COCYCLE-NEG-001`（`WrongSpinWCocycle.agda`）。
> - claim：`CG001-C-69`。回答 019 的 T-039。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，`--safe --cubical --guardedness`，无公设。
> - 辅助核对：`p3_routes.py` 与其输出 `p3_routes.out.txt`（组合核对，不是证明）。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §17（GOAL_LOCAL_INDEX_ONLY）。

## 为什么要做

C-64 的反例 `spin` 表明，按 `Coh₂` 的写法，六边形相干可以失败。审计要问的是：`Coh₂` 的两条路线写对了吗？公式若写错，会有两种表现：拒绝本来相干的结构，或接受本来不相干的结构。本包对一整族结构刻画 `Coh₂` 何时成立，看它是否正好是应有的条件。

## 命题全文（`WindingCocycle.agda`）

- `rot z x = basechange2 x (intLoop z)` 是圆周上每一点处绕数为 z 的环（库函数；在 base 处就是 `intLoop z`）。
- `windingSST w` 取 `X n = S¹`，每个面映射为恒等，恒等式 `sid n i j` 在 x 处取 `rot (w n i j) x`。
- `cocycle w` 断言：对一切 i ≤ j ≤ k，
  `w(m+1, j+1, k+1) + (w(m, i, k) + w(m+1, i, j)) ≡ w(m, i, j) + (w(m+1, i, k+1) + w(m, j, k))`，
  即两条路线遇到的绕数之和相同。
- **(a)** `coh₂→cocycle`、`cocycle→coh₂`：`Coh₂ (windingSST w)` 与 `cocycle w` 互推。
  - 前者对 base 处的六边形取 `winding`，并用 `winding-hom`。
  - 后者在 base 处由 `intLoop-hom` 得出；对一般的 x，由 `toPropElim` 归结到 base，因为环空间是集合（`isSetΩx`）。
- **(b)** 三种绕数样式：
  - `spinW`（第 0 层、指标 0 0 处绕数 1，其余 0，与 C-64 的 `spin` 同样式）：不满足方程，`spinWIncoherent : ¬ Coh₂ (windingSST spinW)`；
  - `uniformW`（处处绕数 1）：满足方程，`uniformWCoherent`，尽管每一条恒等式都是非平凡的环；
  - `levelW`（第 n 层绕数 n）：不满足方程，`levelWIncoherent`。

## 组合核对（`p3_routes.py`，不是证明）

脚本以 i ≤ j ≤ k 为符号，核对以下几点：
- 从 d_i d_{j+1} d_{k+2} 出发，得到 6 个字、6 条改写；
- 从顶到底恰有两条极大链，改写位置分别是 (1,0,1) 与 (0,1,0)；
- 每条改写由源字与位置唯一确定；
- 两条链用到的恒等式指标对，与 `WildSST.agda` 的 `routeA`、`routeB` 逐项一致。

输出为 `ALL_OK`。所以 `Coh₂ = (routeA ≡ routeB)` 是三字母改写唯一的 2-胞腔，不存在另一种路线选法。

## 这件事说明什么（解释）

- 【解释】在这族结构上，`Coh₂` 恰好是“两条路线的绕数相等”，也就是障碍理论所预期的上闭链条件。它接受非平凡而相干的数据（`uniformW`），只拒绝两条路线绕数不同的数据（`spinW`、`levelW`）。所以 C-64 中 `spin` 的失败反映的是真实的不相干，而不是公式写错。
- 【解释】同一种“上闭链条件”在第二级再次出现：C-68 中两个半球各含两个底部六边形，配对方式与 `Deg₃` 相同。

## 禁止外推

- 刻画只对这一族圆周值结构成立（面映射为恒等，恒等式为 `rot` 环）；不是对一切结构的 `Coh₂` 的一般刻画。
- `p3_routes.py` 是组合核对，不是 Agda 证明。

## 负控制

`WrongSpinWCocycle.agda` 断言 `spinW` 在 m = 0、i = j = k = 0 处满足方程（`refl`）。预期被拒：`1 != 2 of type ℕ`。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-WINDING-COCYCLE-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-WINDING-COCYCLE-NEG-01`。
