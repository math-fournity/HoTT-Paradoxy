# CLAIM-PACKAGE-GOLD：金形态 cut·四条件完整版（MP-DEDEKIND-OMEGA-GOLD）

> 状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / GOLD_FORM_FOUR_CONDITIONS_COMPLETE`
> 日期：2026-09-18（四条件完整版）。run：`20260918-MP-DEDEKIND-OMEGA-GOLD-02`（`--ignore-interfaces` 全量 clean 重放，exit 0 / stderr 0）。
> 历史：第一装配期 `20260917-MP-DEDEKIND-OMEGA-GOLD-01`（rounded→ 双向 + located，commit `615fbd2`）与 δ 路线 `roundedL←`（commit `4bc020d`）保留为分阶段收据。
> 来源：修订片 027 §5/§9 + CutGoldForm-DESIGN.md（**勘误版**，plan-revise `0150b29`）。

## 1. 已装配并经核接受（KERNEL_ACCEPTED_WITH_SCOPE，exit 0 / stderr 0）

### CutInfra.agda（ℚ 序算术基础设施；队列 1 全量）

| 引理 | 陈述 | 路线 |
|---|---|---|
| `<-≤` | `m < n → m ≤ n` | elimProp2 + `ℤ.<-weaken` |
| `·-mono-≤-nn` | `(k a b : ℚ) → 0r ≤ k → a ≤ b → k·ℚa ≤ k·ℚb`（**crux**） | elimProp3 降代表元；`0≤k` 提取分子非负见证 `j`（`+pos-pos0`）；hab 两侧乘 `pos w`（`w := j·dm`，恒非负）经 `ℤ.≤-·o`；`stepA`/`stepB` 以 `·Assoc`/`·Comm`/`pos·pos`/ℕ`·-comm` 完成交乘重排 |
| `·-mono-<-nn` | `0r < k → a < b → k·ℚa < k·ℚb`（strict 版） | 同上，`0<k` 给 `p ≡ pos (suc j)`；`w := (suc j)·dm` 定义性 suc 形；`0<pos w` 显式见证（`+pos-pos1`）；`ℤ.0<o→<-·o` |

### CutGoldForm.agda（勘误版谓词 + Book §11.2 四条件·全部 7/7 方向）

- 谓词（勘误版）：`L q := (q<0r) ⊎ ((0r≤q) × (q·ℚq<2r))`；`U q := (0r<q) × (2r<q·ℚq)`。
  两支不相容（`L-disj` 经 `isAntisym≤`+`isIrrefl<`）⇒ `isPropL`/`isPropU`；`Lₚ`/`Uₚ : ℚ → hProp ℓ-zero`。
- `inhabL : L 1r`（见证 `(1,refl),(0,refl)`，全点归约）；`inhabU : U 2r`。
- `disjoint : ∀ q r → L q → U r → q < r`（三分 `q≟r`；eq 支双 transport、gt 支双严格单调链 + `isIrrefl<`）。
- `roundedL→ : q < p → L p → L q`；`roundedU→ : q < r → U q → U r`（两支单调链）。
- `located : q < r → L q ⊎ U r`（三分 `q≟0r` 后三分 `q²≟2r`；**eq 支消费 M2 `√2-irrational`**——金形态与第二枚导弹的首次链式消费）。

## 2. rounded← 双向见证方向（已装配并过核；原登记义务清零）

- `roundedL← : L q → Σ[ p ], (q < p) × (L p)`（commit `4bc020d`）。
- `roundedU← : U r → Σ[ q ], (q < r) × (U q)`（本 Session，工作树已过核）。
  `r > 2r` 取 `q := 2r`（`inhabU` 见证）；否则
  `t := (r·ℚr) -ℚ 2r`、`δ := t ·ℚ ¼r`、`q := r -ℚ δ`，
  `U q` 的正性由 `0r<q`（δ<r 消去）与 `2r<q·ℚq`（`sq-minus` 差平方展开
  归约到 `2r + ((t+δδ) - X)`，`X := rδ+rδ ≤ t` 后 `pos-add<`）给出。
- **原登记工程障碍已解决**：依赖代表元的见证（`(4ab+1)/(4b²)`、Pell 中项）
  在商上确实不良定义，故改用 **内在 ℚ 项** δ 路线（`δ := t ·ℚ ¼r` 是 q/r 的
  内在项，不依赖代表元选择）；U 侧未需要 `inv`（正性合取 + δ 归约即足够）。
  补齐的基础设施：`sq-minus`（差平方展开）、`pos-add<`、`diff-pos`、
  `b-a+a`、`·-reshuffle`、`·-idR-≤`、封闭常数界 `boundU`。

## 3. 语义边界（不可漂移）

本包是 ℚ 层标准序算术与 cut 构造（Book §11.2 的构造性前半），**不是** HoTT 内部
矛盾，不声称 HoTT 不一致；LEM/resizing 的收费位置在把 cut 取等价类、把「ℝ 取值
命题」塌缩到单一 Ω 的下一升格（DESIGN §4，仅登记未机械化）；全部收据
LOCAL，GOLD-02 与本说明随本执行单元提交、非 VERSION_CLOSED（以最终 Git commit
回读为准）、push 未授权。

## 4. 复现命令

见 `HoTT/verification/runs/20260918-MP-DEDEKIND-OMEGA-GOLD-02/RUN.json`
的 `command_argv`（仓库根、绝对路径、`--ignore-interfaces`、固定 AGDA_LIBRARIES
与 cubical-0.9）；源码哈希见同目录 `source-manifest.json`。等价入口：
`sh HoTT/formal/dedekind-omega-missile/compile.sh CutGoldForm.agda --ignore-interfaces`。
