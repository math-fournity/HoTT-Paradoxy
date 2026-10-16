# 裁决报告：两条 `AllBlockerQ` 路线**不独立**（2026-10-14，本线 CG-007 会话 d58e0c0d）

> **身份**：`INDEPENDENCE_ADJUDICATION / NOT_A_NEW_RECEIPT`。
> 派工来自 Master（"任务②，但换成核两条路线是否真独立"）。结论层面，非编译层面。
> 全部依据为**源码比对**（`fd8b8305` 与 `master-assembly-poc-20261014` 的文件逐字读取）+ 一次机器探针。

## 0. 结论先说

**两条路线不独立。它们在同一条定理的同一个 m=0 实例上汇合**：
`ITSubstOpen9.iT_subst_open`（001-Flash 的一般开口律 ∀m）的 m=0 实例。

这条承载件是**两条路线共同且唯一的**。若它有缺陷，两条路线**同时**失效；
"两条独立证明互证"因此**不能**作为该结论的双重保证。

**但这不等于结论弱**——见 §4：承载件本身已被独立核验（Master + 001-Flash 两侧，非同一人）。

## 1. 路线①（Master 装配）

文件：`master-assembly-poc-20261014/GodelQ/MasterAssemblyProbe.lean`

```
ITSubstOpen9.iT_subst_open (V) (0) q           -- 一般律 ∀m，取 m = 0
  → (QvecVOr_zero, QvecV_zero, zero_add)
bridgeB : subst ℒₜ ?[^&0] (iT 1 q) = iT 0 (subst ℒₒᵣ ?[^&0] q)
  → allKey_of_bridge → AllKey → allBlockerQ_of_key → AllBlockerQ
```

关键落点 `AllKey`：`Provable 𝗭𝗙𝗖 (imp (iT 0 (free p)) (free (iT 1 p)))`——**无 `domZero` 守卫**。

## 2. 路线②（`HABKey` / `HABElim` / `HAllUncond`）

资产：`origin/claude/infallible-mestorf-ce08c0` @ `fd8b8305`，三个文件：

| 文件 | import | 主要声明 |
|---|---|---|
| `HABKey.lean` | `HAllProof`、**`ITSubstOpen9`** | `iT_free_eq` |
| `HABElim.lean` | **`HABKey`**、`TranslateShiftCompat` | `free_iT`、`hAB_derivable` |
| `HAllUncond.lean` | **`HABElim`**、`HAllProof` | `hAll`（无算术前提） |

链条：
```
ITSubstOpen9.iT_subst_open (V) (0) (shift ℒₒᵣ p)   -- 同一个一般律，取 m = 0，q := shift p
HABKey.iT_free_eq : iT 0 (free p) = subst ℒₜ ?[^&0] (iT 1 (shift p))
  → HABElim.free_iT（配 iT_shift，把 B 化成 imp (x∈ω) A）
  → HABElim.hAB_derivable（neg A ⋎ (neg C ⋎ A)，排中律）
  → HAllProof.hAll_uncond 的 hAB 参数
  → HAllUncond.hAll
```

关键落点 `hAB`：`Derivable (neg A ⋎ free ℒₛₜ (imp domZero (iT 1 p))) ∅`——**带 `domZero`，`neg ⋎` 形式**。

## 3. 共同依赖的逐字证据

`HABKey.iT_free_eq` 的证明体：
```lean
show iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) (shift (L := ℒₒᵣ) p)) =
  subst ℒₜ (?[^&0] : V) (iT (1 : V) (shift (L := ℒₒᵣ) p))
have h1 : IsSemiformula ℒₒᵣ ((0 : V) + 1) (shift (L := ℒₒᵣ) p) := …
have h := GodelQ.ITSubstOpen9.iT_subst_open (V := V) 0 (shift (L := ℒₒᵣ) p) h1
rw [GodelQ.QvecVDefs.QvecVOr_zero, GodelQ.QvecVDefs.QvecV_zero] at h
rw [show (0 : V) + 1 = 1 from _root_.zero_add 1] at h
exact h
```

路线①的 `bridgeB` 证明体：
```lean
have h1 : IsSemiformula ℒₒᵣ ((0 : V) + 1) q := …
have h := GodelQ.ITSubstOpen9.iT_subst_open (V := V) (0 : V) q h1
rw [GodelQ.QvecVDefs.QvecVOr_zero, GodelQ.QvecVDefs.QvecV_zero] at h
rw [show (0 : V) + 1 = 1 from _root_.zero_add 1] at h
exact h.symm
```

**同一条定理、同一个 `m := 0`、同样的两条 `rw`。** 差别只有三处，全是表层的：

| 差别 | 路线① `bridgeB` | 路线② `iT_free_eq` |
|---|---|---|
| `q` 取什么 | `q`（层 1 公式） | `shift ℒₒᵣ p` |
| 方向 | `exact h.symm` | `exact h` |
| LHS 是否先展开 | 直接给 `subst` 形状 | `show` 先把 `free p` 展开成 `subst ?[^&0] (shift p)` |

第三处由 `free` 的定义给出，**机器已核**（探针 `ProbeRouteIndependence.lean:68`，`rfl` 通过）：
```lean
example (p : V) (_hp : IsSemiformula ℒₒᵣ (1 : V) p) :
    free (L := ℒₒᵣ) p = subst (L := ℒₒᵣ) (?[^&0] : V) (shift (L := ℒₒᵣ) p) := rfl
```

⟹ 把①的 `q` 取成 `shift p`、取 `.symm`，就**逐字是**②的 `iT_free_eq`。两者不是两条证明，是**同一条引理的两种朝向**。

## 4. 这削弱了什么，没削弱什么

**削弱的**：
- **不能**说"两条独立证明互证"。它们共享承载件 `iT_subst_open`（∀m 一般律，m=0 实例）。
- 路线②表面上的差异（`domZero` 守卫 vs 无守卫、`neg ⋎` 排中律 vs `imp`）**都是承载件之后的组装差异**，
  不是入口差异。入口相同。
- 因此 `AllBlockerQ` 无条件证成这一结论的**独立性等级 = 1**，不是 2。

**没削弱的**：
- 承载件 `ITSubstOpen9.iT_subst_open` 本身由 **001-Flash** 做出，被 **Master** 独立重编译核验
  （rc=0、公理三条、无 sorryAx、全链 39/39）。**做的人与核的人不是同一个**——这一层独立性仍在。
- 装配与移植保真由本线核验（74/74 skipped=0 + 两处冲突无语义改动）。
- 结论本身**仍然成立**，只是它的强度应表述为：
  > `AllBlockerQ` 无条件证成，依赖于一条已被跨人核验的一般开口律 `iT_subst_open`；
  > 现有两条组装路线共享该律的 m=0 实例，因此不构成双重独立保证。

## 5. 若要真正取得"双重独立"，需要什么

一条**不经** `iT_subst_open`（或其任何实例）到达 `AllBlockerQ` 的路线。候选：

1. **绕开 `free`/`subst` 中介**：`hAll` 的公式层义务本质是"`iT 0 (free p)` 与 ℒₛₜ 侧某形状对齐"。
   若能从 `iT` 的**逐构造子归纳**（`UformulaRec1.Construction.semiformula_result_induction`，
   与 C-398/C-399 用的同一个原理）直接推出对齐，就不经过 `subst` 开口律。
   **代价**：C-399 的 `iT_neg` 已经显示这类归纳在量词支会层数升一，工作量与 `iT_subst_open` 相当。
2. **改 sequent 层的组织**：不走 `Derivable.all_m` + `replace_of_imp`，而用
   `Derivable.all`（带 `IsSemiformula 1 p` 版）直接在 `insert (free ℒₒᵣ p) (setShift ℒₒᵣ s)` 上做。
   但这条路线的 IL 侧仍要对齐两个 `free`，**大概率仍落到同一条律**。
3. **接受独立性等级 1**，改为加强承载件一侧：把 `iT_subst_open` 一般律（∀m）本身做**第二次独立证明**。
   这是最小代价、最直接的做法——**保的不是"两条路线"，是"承载件双证"**。

**我的建议：③。** 理由：两条路线的组装部分已经很薄（各十余行），真正的数学含量全在 `iT_subst_open`；
把它双证，比再造一条不经它的长路线更划算，也更难被同一处缺陷同时打穿。

## 6. 探针

`.claude/goals/CG-007-formalization-completion/probes/adj/ProbeRouteIndependence.lean`（**exit 0**，
无 `sorry`）：固定 `iT_subst_open` 的 ∀m 签名、`QvecVOr_zero`/`QvecV_zero`（都给出 `^&0 ∷ 0`）、
以及 `free p = subst ?[^&0] (shift p)` 的 `rfl`。

## 7. 边界

- 本报告**不**主张 `AllBlockerQ` 有误；它成立，且已被三个独立复现（Master 原收据、004-Flash 41/41、本线 74/74）。
- 本报告只裁定**独立性等级**：两条组装路线共享承载件，等级为 1。
- 未核验：`iT_subst_open` 的证明内容本身（001-Flash 资产，Master 已核）；`allKey_of_bridge`/
  `allBlockerQ_of_key` 的证明内容（004-Flash 资产，Master 已核五条）。本报告核的是**依赖图的汇合点**。
- `HABKey.lean` 虽 `import ITSubstOpen9`，但**不是**仅 import 而未用——`iT_free_eq` 的证明体
  **确实调用**了它（§3 逐字）。这是"真依赖"，不是"可清理的冗余 import"。
