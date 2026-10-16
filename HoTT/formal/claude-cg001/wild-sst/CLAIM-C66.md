# 后退的第二级：补上六边形之后，填充不唯一，下一层也不自动成立（C-66）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325；目标包 CG-002，完成门 G3。与 C-64（`CLAIM.md`）同包，导入同一个 `WildSST` 定义。
>
> - proof id：`MP-CG001-WILD-SST2-001`（主包，`WildSST2.agda`）；负控制 `MP-CG001-WILD-SST2-NEG-001`（`WrongSurfTrivial.agda`）。
> - claim：`CG001-C-66`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，`--safe --cubical --guardedness`，无公设，零警告。
> - 辅助计算：`p4_faces.py` 与其输出 `p4_faces.out.txt`（组合核对，不是证明）。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §16（GOAL_LOCAL_INDEX_ONLY）。

## 命题全文（`WildSST2.agda`）

- **(a) Hopf 族检测出 `surf`**：本地的 `Hopf : S² → Type` 与 cubical 库 `S¹Hopf.HopfS²` 的 Glue 定义逐项相同；`carry β = cong (λ r → subst Hopf r base) β`。
  - `surfWinds : winding (carry surf) ≡ negsuc 0`，由 `refl` 成立（内核直接算出）；
  - `surf≢refl : ¬ (surf ≡ refl)`。
- **退化结构 `flat`**：0 维单形是 S² 的点，更高维单形是 Unit 的点；0 维以上的面映射都到 `tt`，从 1 维到 0 维的面映射都到 `north`；一切面恒等式取 `refl`。于是第 0 层每个六边形两边的路线都是同一条复合路径 `r = refl ∙ refl ∙ refl`，一个填充就是 `r ≡ r` 的一个元素。
  - `ρ : r ≡ refl`；`σr = ρ ∙ surf ∙ sym ρ : r ≡ r`；`σr≢refl : ¬ (σr ≡ refl)`（由群胚律化回 `surf≢refl`）。
- **(b) 填充是新的、不唯一的数据**：`WildSST₂` 是 `WildSST` 加上每个六边形的填充（字段 `hexagon : Coh₂ underlying`）。`cohTrivial`（全取 `refl`）与 `cohSurf`（第 0 层 (0,0,0) 处取 `σr`，其余 `refl`）都是 `Coh₂ flat` 的元素，给出 `flatTrivial`、`flatSurf` 两个 `WildSST₂`；`twoFillings : ¬ (cohTrivial ≡ cohSurf)`。
- **(c) 下一层在 `flat` 上的形式**：`Deg₃ C` 要求对 Fin 2 中一切 i ≤ j ≤ k ≤ l，`C(jkl) ∙ C(ijl) ≡ C(ikl) ∙ C(ijk)`（C(abc) 指第 0 层 (a,b,c) 处的填充）。
  - `trivialSatisfies : Deg₃ cohTrivial`；
  - `surfViolates : ¬ Deg₃ cohSurf`（在 (0,0,0,1) 处化为 `σr ≡ refl`）。

## 手推与脚本核对的部分（不是机器证明）

**要说明的是**：半单纯恒等式的第二级相干（置换多面体 P₄ 的相干），在 `flat` 上恰好化为 `Deg₃`。一般的 P₄ 相干没有在 Agda 中写成类型，这一步是手推加脚本核对：

1. 从 d_i d_{j+1} d_{k+2} d_{l+3} 出发，按 d_a d_b → d_{b−1} d_a（a < b）改写，得到置换多面体 P₄：24 个字、36 条改写、6 个正方形、8 个六边形，终点 d_l d_k d_j d_i。
2. 作用在最左三个字母上的 4 个“底部”六边形，是第 0 层的填充，经最右一个字母预复合后取值；它们的起点分别是 (i,j,k)、(i,j,l)、(i,k,l)、(j,k,l) 对应的字，各一次。
3. 另外 4 个六边形作用在最右三个字母上，是第 1 层的填充，在 `flat` 上位于 Unit，经常值面映射推到 S² 后是平凡的 2-胞腔；6 个正方形是不相交改写的自然性方块，在 `flat` 上一切 1-胞腔都是 `refl`，所以也是平凡的。
4. 因此 P₄ 相干在 `flat` 上化为四个底部填充之间的一条关系；由于 `r ≡ r` 这个群是交换的（Eckmann–Hilton），关系的具体排列不影响真假。`Deg₃` 取的是交错符号 h(jkl) − h(ikl) + h(ijl) − h(ijk) = 0 的排列。
5. 关键的一点与符号无关：在 (0,0,0,1) 处四个底部三元组是 (0,0,0)、(0,0,1)、(0,0,1)、(0,0,1)，(0,0,0) 恰出现一次；当 (0,0,1) 处的填充为 `refl` 时，关系化为 ±σr = 0，即 `σr ≡ refl`，不成立。

`p4_faces.py` 对一切 i ≤ j ≤ k ≤ l ∈ {0,1,2}（15 个四元组）核对了第 1、2 条与“(0,0,0) 的出现次数”，输出 `ALL_OK`（`p4_faces.out.txt`）。第 3、4 条是按定义的论证。

## 这件事说明什么（解释，非机器证明）

- 【解释】第一级（C-64）说明：那一行定义少了六边形。补上六边形作为数据之后，第二级出现两件事：填充不唯一（在 UIP 下它唯一，C-65 的理由相同），而且各个填充之间还要满足下一层的相容（P₄），这一层同样不自动成立。每一次修补都长出下一层的义务，这就是 A7 的无穷后退在机器上看得见的前两级。
- 【来源】Kolomatskaia（*You wouldn't permutahedron*，arXiv 2024）给出各阶置换多面体交换相干关系的公式，并说明它们与构造半单纯类型的问题密切相关；半单纯类型的统一定义在书式 HoTT 中仍是开放问题（见 `../sst-finite-levels/CLAIM.md`）。

## 禁止外推

- 不证明半单纯类型在 HoTT 中不可定义；不证明 HoTT 不一致。
- “P₄ 在 `flat` 上化为 `Deg₃`”是手推加脚本核对，未机器证明；机器证明的是 `Deg₃` 的满足与违反、填充的不唯一、`surf ≠ refl`。
- `flat` 是退化的结构，只用来显示第二级数据的自由度与下一层的约束，不代表任何几何上自然的半单纯类型。

## 负控制

`WrongSurfTrivial.agda`：断言 `winding (carry surf) ≡ pos 0`（`refl`）。预期被拒：`negsuc zero != pos 0 of type ℤ`。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-WILD-SST2-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-WILD-SST2-NEG-01`。
