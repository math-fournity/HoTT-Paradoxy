# 同一个定义在 HoTT 中接受不相干的数据（C-64）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325；目标包 CG-002，完成门 G2。
>
> **起因**：用户采纳 CN-034 的推荐（A7 无穷相干为主线）：“按照你的推荐，进行后续的探索工作。”本包与 Lean 包 `wild-sst-lean`（C-65）组成“同一定义两侧”的对照。
>
> - proof id：`MP-CG001-WILD-SST-001`（主包）；负控制 `MP-CG001-WILD-SST-NEG-001`。
> - claim：`CG001-C-64`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9（`HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`），`--safe --cubical --guardedness`，无公设，零警告。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §16（GOAL_LOCAL_INDEX_ONLY）。

## 命题全文（`WildSST.agda`）

**定义**（与 Lean 包逐项相同）：
- `Fin n` 按 n 递归定义：`Fin 0 = ⊥`，`Fin (n+1) = Unit ⊎ Fin n`；`fzero = inl tt`，`fsuc = inr`；`weaken` 按递归定义；次序 `_≤F_` 按递归定义；引理 `≤F-trans`、`weaken≤`、`weaken≤suc`。
- `WildSST`（预层式的半单纯结构，即事实层通用的那一行定义）：`X : ℕ → Type`；面映射 `d n : Fin (n+2) → X (n+1) → X n`；半单纯恒等式 `sid n i j (i ≤F j) x : d n i (d (n+1) (fsuc j) x) ≡ d n j (d (n+1) (weaken i) x)`（重编号形式，即 i < j 时 d_i d_j = d_{j−1} d_i）。
- 两条路线（把 d_i d_{j+1} d_{k+2} 改写成 d_k d_j d_i，i ≤ j ≤ k）：
  - `routeA`：先改写 d_{j+1} d_{k+2}（在 d_i 下），再改写 d_i d_{k+1}，再改写 d_i d_{j+1}（在 d_k 下）；
  - `routeB`：先改写 d_i d_{j+1}，再改写 d_i d_{k+2}（在 d_j 下），再改写 d_j d_{k+1}。
- 六边形相干 `Coh₂ S`：对一切 m、i ≤ j ≤ k 与 x，`routeA ≡ routeB`。

**定理**：
- (a) `setsCohere`：若每个 `X n` 都是集合，则 `Coh₂ S` 对该实例成立。
- (b) `spin`：`X n = S¹`，一切面映射为恒等，一切恒等式取 `refl`，唯有 `sid 0 fzero fzero` 取 `rotLoop`（在 `base` 处为 `loop`）。它是 `WildSST` 的一个实例，即满足定义中的全部面恒等式。
- (c) `windsOnce : winding routeA-spin ≡ pos 1`，`windsTwice : winding routeB-spin ≡ pos 2`，均由 `refl` 成立（内核直接算出绕数）；这里 `routeA-spin`、`routeB-spin` 是 m = 0、i = j = k = 0、x = base 时的两条路线。
- (d) `spinIncoherent : ¬ Coh₂ spin`。

## 这件事说明什么（解释，非机器证明）

- 【解释】同一段文字（点、面映射、面之面相合），在相同是事实的世界里就是半单纯集合的完整定义（(a)；Lean 一侧 C-65 对一切实例成立）；在 HoTT 中，它定义的是一种会接受不相干数据的结构，不是半单纯类型。面恒等式每条都成立，两种化简顺序给出的证明却绕了不同的圈数。
- 【解释】这是 A7 无穷后退的第一级：要让定义正确，必须把六边形相干作为新字段加进去；而新字段的数据又要满足下一层的相干（C-66，完成门 G3）。
- 【来源】这类“野”结构与相干结构的差别是已知现象；半单纯类型的统一定义在书式 HoTT 中仍是开放问题（见 `../sst-finite-levels/CLAIM.md` 的来源）。

## 禁止外推

- 不证明半单纯类型在 HoTT 中不可定义；不证明 HoTT 不一致。
- 反例只用了一个具体实例与一组具体下标；它说明预层式定义缺少相干，不刻画全部缺少的相干。
- `spin` 的面映射都是恒等，只用来显示恒等式的证明本身携带信息；它不代表任何几何上自然的半单纯类型。

## 负控制

`WrongSpinCoherent.agda`：断言路线 A 也绕两圈（`winding routeA-spin ≡ pos 2`，`refl`）。预期被拒：`1 != 2 of type Nat`。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-WILD-SST-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-WILD-SST-NEG-01`。
