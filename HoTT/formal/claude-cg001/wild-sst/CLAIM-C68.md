# 后退的第二级，不再手推：一般的 P₄ 相干写成类型，并在 flat 上机器判定（C-68）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325；目标包 CG-003，完成门 G1。与 C-64、C-66 同包。
>
> - proof id：`MP-CG001-WILD-SST-P4-001`。主文件 `WildSSTP4Flat.agda`，导入 `WildSSTP4.agda`；两者都由 `gen_p4.py` 生成，结构清单为 `P4_STRUCTURE.txt`。
> - 负控制：`MP-CG001-WILD-SST-P4-NEG-001`（`WrongSurfMoveTrivial.agda`）。
> - claim：`CG001-C-68`。回答 019 的 T-040。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，`--safe --cubical --guardedness`，无公设。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §17（GOAL_LOCAL_INDEX_ONLY）。

## 为什么要做

C-66 在 `flat` 上违反的是 `Deg₃`。“一般的第二级相干（置换多面体 P₄）在 `flat` 上化为 `Deg₃`”这一步当时是手推，只用 `p4_faces.py` 核对了组合结构。本包把一般的第二级相干写成类型，由内核直接判定它在 `flat` 上的真假，手推一步不再需要。

## 定义（`WildSSTP4.agda`，生成）

- **`WildSSTᵢ`**：C-64 的定义，`Fin`、`weaken`、次序、面映射、恒等式均不变，只有一处改动：恒等式的次序假设 `i ≤F j` 改为不相关参数。
  - `≤F` 是命题，这一改动只把本来就相等的证明项等同起来。
  - 这样，从不同面到达的同一条边就是同一个项。
  - `toIrr : WildSST → WildSSTᵢ` 把 C-64 的每个结构转过来。
- **`Coh₂ᵢ`**：与 C-64 的 `Coh₂` 相同的两条路线，参数改为不相关。`WildSSTᵢ₂` 是 `WildSSTᵢ` 加上六边形数据。
- **`Coh₃`（第二级相干）**，由 `gen_p4.py` 从四个面映射的改写图生成。生成前脚本核对了以下各项，任一不成立即停止：
  - 从 d_i d_{j+1} d_{k+2} d_{l+3} 出发，得到 24 个字、36 条改写，终点为 d_l d_k d_j d_i。
  - 共 14 个面：6 个正方形、4 个底部六边形、4 个顶部六边形。正方形是不相交改写的自然性方块（库的 `homotopyNatural`）；底部六边形是第 m 层的六边形数据；顶部六边形是第 m+1 层的六边形数据，经外层面映射推出（`topFace`，用 `congFunct` 调整）。
  - 每条改写恰好落在两个面上。
  - 极大链（路线）共 16 条。从字典序最小的路线到最大的路线，找到两串移动 `hem₁`（6 步）与 `hem₂`（8 步），二者用到的面互不相交，合起来恰好是全部 14 个面，每面一次。
- **`Coh₃ S`** 断言：对一切层级 m、一切 i ≤ j ≤ k ≤ l、一切 x，两个半球的复合 2-路径相等，即 `hem₁ ≡ hem₂`。
- 路径代数的约定：路线是六条边的右结合复合，末尾补一个 `refl`；一步移动是 `cong（前缀）(seg₂/seg₃ 面 尾部)`。

## 命题全文（`WildSSTP4Flat.agda`，生成；证明中的引理部分为固定文本）

`flat`、`cohTrivialᵢ`、`cohSurfᵢ` 与 C-66 的子句相同：`flat` 的 0 维单形是 S² 的点，更高维单形是 Unit 的点，恒等式全取 `refl`；`cohSurfᵢ` 在第 0 层 (0,0,0) 处取 σr，其余取 `refl`。

- **(a) `notCoh₃ : ¬ Coh₃ flatSurfᵢ`**。
- **(b) `coh₃Trivial : Coh₃ flatTrivialᵢ`**（正控制）。
- **引理**：
  - `natConst`：常值映射上的 `homotopyNatural` 等于 `refl`，由一个显式的三维 hcomp 给出；
  - `seg2-refl`、`seg3-refl`、`topFace-refl`：平凡的面给出平凡的移动；
  - `conj-triv`、`seg3-inj`：seg₃ 对它的面是单射，经 `compPathr-isEquiv` 与 `isEquiv→isEmbedding`；
  - `∙-triv`。
- **证明的走法**：
  - 在实例 m = 0、(i,j,k,l) = (0,0,0,1) 上，所有边都化为 `refl`。14 步移动中有 13 步的面化为 `refl`、`topFace f refl` 或常值上的 `homotopyNatural`，因而等于 `refl`。
  - 唯一的例外是 `hem₁` 的第 1 步：第 0 层 (i,j,k) = (0,0,0) 处的六边形，这一步等于 `seg₃ (sym σr) T`。
  - 由 `Coh₃` 得 `seg₃ (sym σr) T ≡ refl`，于是 σr ≡ refl，与 C-66 的 `σr≢refl` 矛盾。
  - (b) 在第 0 层对一切指标，14 步都等于 `refl`；0 层以上单形构成 Unit，由 `isOfHLevelUnit 3` 得出。

## 与 C-66 的关系（解释）

- 【证明】C-66 的“下一层在 `flat` 上不成立”，现在直接由一般的第二级相干得出，不再依赖手推。
- 【解释】`P4_STRUCTURE.txt` 显示，底部六边形 (i,j,k)、(i,k,l) 在 `hem₁` 中，(i,j,l)、(j,k,l) 在 `hem₂` 中，与 `Deg₃` 的配对 h(jkl)·h(ijl) = h(ikl)·h(ijk) 相同。这说明 C-66 手推的形式与本包一致，但“`Coh₃` 在 `flat` 上与 `Deg₃` 等价”这一般的等价没有机器证明，机器证明的是 (a) 与 (b)。
- 【解释】填充不唯一（C-66 `twoFillings`），且不是每个填充都满足下一层（本包 (a)，同时 (b) 表明下一层可以满足）。这是后退第二级的完整形态。

## 禁止外推

- 不证明半单纯类型在 HoTT 中不可定义，也不证明 HoTT 不一致。
- “`Coh₃` 就是标准意义下的第二级相干”依赖两点：生成器的组合核对（两个半球划分 P₄ 的 14 个面），以及每个面取的是标准胞腔（自然性方块、六边形数据）。它没有与其他表述（例如索引式 `SST≤4` 或 Reedy 纤维图式）做机器等价。
- `WildSSTᵢ` 与 C-64 的 `WildSST` 相差一个命题参数的不相关性；`toIrr` 是从后者到前者的映射。二者的 `Coh₂` 在一般情形下的等价没有写出（对 `flat` 两边的子句逐字相同）。
- 曾尝试让内核直接算出两个半球的 Hopf 绕数，单步移动的计算在 100 秒内都未完成，所以改用上面的结构化证明。本包不含任何绕数计算。

## 负控制

`WrongSurfMoveTrivial.agda` 断言 `hem₁` 的第 1 步与其他 13 步一样，因面为 `refl` 而平凡。预期被拒：这一步的面是 `sym σr`，不是 `refl`。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-WILD-SST-P4-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-WILD-SST-P4-NEG-01`。
