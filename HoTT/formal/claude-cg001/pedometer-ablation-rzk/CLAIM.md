# 有向类型论自身中的携带：方向只能住在哪里（C-53，Rzk 原生）

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。
>
> **起因**：用户要求用其他机器证明系统与方法检验有向预测（原话见 `pedometer-ablation/CLAIM.md`）。Rzk 0.11.3 没有有向单价性，造不出“运输为 `suc` 的协变族”。但它能在有向类型论 sHoTT **自身**中回答另一半问题：在这个理论里，携带的可逆性管到哪里为止。
>
> - proof id：`MP-CG001-PEDOMETER-ABLATION-RZK-001`（主包）；负控制 `MP-CG001-PEDOMETER-ABLATION-RZK-NEG-001`。
> - claim：`CG001-C-53`。
> - 工具链：Rzk 0.11.3（`HoTT/formal/claude-cg001/directed-native/RZK_TOOLCHAIN.json`）。sHoTT，无公设，不加公理，不用模态。运行由 `.claude/goals/CG-001-targeted-overview/tools/capture_rzk_proof_run.py` 捕获。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §12（GOAL_LOCAL_INDEX_ONLY）。

## 命题全文（`CarriedMonotone.rzk`）

定义沿用 RS17 与 rzk-lang/sHoTT 库的写法：`hom`、`dhom` 为 1-单形上的扩张类型；离散按 RS17 定义 7.1；协变族按 RS17 定义 8.2，即每支箭头从纤维的每一点唯一提升。文件自包含。

- **路径**：
  - **(a)** `transport-there-and-back`：沿 `p` 携带再沿 `rev p` 带回，得到原物。
  - **(b)** `monotone-is-invariant`：对任意类型 `N`、任意满足反对称的关系 `R`、任意读数 `r`，若没有路径上的携带使读数降低，则没有路径上的携带使读数改变。
  - **(c)** `two-way-forces-fixed-point`：若沿 `p` 与沿 `rev p` 携带都对读数施加 `s`，则起点读数 `r` 满足 `r = s (s r)`。对计步器（自然数上的后继）而言，这样的 `r` 不存在；这一步在本文件中没有证明，因为不需要自然数的消去。
- **箭头**：
  - **(d)** `covariant-transport-id`：对协变族，沿恒等箭头的协变运输是恒等（由唯一提升推出，不是定义性的）。
  - **(e)** `covariant-transport-hom-eq`：沿由路径得来的箭头（`hom-eq p`），协变运输等于普通运输。
  - **(f)** `discrete-covariant-monotone-is-invariant`：若底类型离散，则没有箭头使之降低的协变读数，也没有箭头能使之改变。
- **负控制**：`WrongArrowReverse.rzk` 仿照路径取逆，把一支从 `x` 到 `y` 的箭头当作从 `y` 到 `x` 的箭头使用（`\ t → f t : hom A y x`），被拒：`cannot unify term y with term x`（在 `t ≡ 0₂` 处）。有向区间 `2` 上没有反转运算。

## 解读【解释】

- 在有向类型论内部，群胚律仍管着**路径**：沿路径的携带可逆，只增不减即不变，与 HoTT 相同（C-49 的核心在另一个理论、另一个内核中重现）。
- 在**离散**的底类型上，群胚律连**箭头**也管着：协变读数只增不减即不变。
- 所以在 sHoTT 中，不可逆的携带变化（计步器）只能住在**非离散底类型上真正不可逆的箭头**所引起的协变运输里。
- 这样的底与族是否存在，本文件不裁定：Rzk 0.11.3 既没有有向单价性，也没有有向高阶归纳类型。
  - 集合层的模型见 C-51、C-52；
  - TT_□ 中的来源依据见 GWB 定理 6.13、定义 6.14、引理 6.15（`pedometer-ablation/CLAIM.md` 解读第 5 条，来源，未重放）。
- 对照 HoTT 的出路（C-50）：HoTT 要数来回，需要在位置上造一个非平凡的自同一（地点类型不是集合），并容许一次步数为 −1 的反向行走；sHoTT 要数来回，需要底类型带真正不可逆的箭头（不离散），不需要反向行走。

## 禁止外推

- 不证明存在非离散的底类型，也不证明存在运输为后继的协变族。
- 不证明 Bool、ℕ 的离散或非离散（见 C-45 及其来源说明）。
- 不重放 GWB，也不涉及 TT_□ 的模态公理。
- “携带”“计步器”是解释标签。
- 数学内容标准（RS17 的定义与路径归纳），**不主张原创**。
