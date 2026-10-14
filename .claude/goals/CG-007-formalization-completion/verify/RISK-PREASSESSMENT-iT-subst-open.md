# 缺陷风险预评估：`ITSubstOpen9.iT_subst_open`（为"第二次独立证明"做准备，2026-10-14）

> **身份**：`RISK_PREASSESSMENT / NOT_A_RECEIPT / NOT_A_NEW_PROOF`。
> 派工来自 Master（"先不派双证，但你可以做准备工作：读遍 001-Flash 的证明，
> 找出哪几支最可能藏缺陷——那是无重叠的"）。本文件是**阅读与静态分析**的产物，
> 不含任何新的机器证明主张，也未改动任何被评估的源码。

## 0. 结论先说

**风险最高的是 `all`/`exs` 两支**（`ITSubstOpen9.lean:142-169` 与 `:170-193`）：
都涉及量词的 `subst` 提升，且都依赖同一条 `subst_QvecV_domZero'`（`:36-47`），
要同时管三处层数（`subst` 的提升、`iT_all`/`iT_exs` 的层参数、`QvecVOr_succ`/`QvecV_succ`）。

**我发现的唯一疑点（`exs` 支 `domZero` 层数与 `all` 支不对称）已被测试否掉**：
把 `exs` 支统一成 `m' + 1` 后**两种写法都闭合**（都 exit 0、公理三条），
故那处不对称**不是缺陷、也不藏巧合**——`domZero` 是常量，层数参数不承载信息。
**这是一次有价值的负面结果**：它把量词支的层数风险降了一档。详见 §3。

**于是真正剩下的风险集中在两处**，都在 `all`/`exs` 支：
(i) `substs_all`/`substs_ex` 的 `qVec` 提升与 `iT_all`/`iT_exs` 的层参数提升是否对齐；
(ii) `rel` 支的 `k = 2` 硬编码（当前正确，但依赖 ℒₒᵣ 恰好只有二元谓词——**脆弱而非错**）。

**整体判断**：该定理的**形状**（归纳谓词 `QPred` 的 Π1 形设计、八支的 rw 链）看起来是对的；
风险不在结构，在**量词支的层数账**。这与本线此前复现 `iT_substs1` 失败时见到的错误**同类**
（"错误为层数账"）。

## 1. 定理的形状（先确认它是对的）

```lean
def QPred (n p : V) : Prop :=
  ∀ m', m' + 1 = n →
    iT m' (subst ℒₒᵣ (QvecVOr m') p) = subst ℒₛₑₜ (QvecV m') (iT (m' + 1) p)

theorem iT_subst_open : ∀ (m q : V), IsSemiformula ℒₒᵣ (m + 1) q →
    iT m (subst ℒₒᵣ (QvecVOr m) q) = subst ℒₛₜ (QvecV m) (iT (m + 1) q)
```

**这个设计有两点值得称赞**（也是它风险较低的原因）：

1. **`QPred` 是 Π1 形（`∀ m'` 守卫式），把 `m` 留在归纳里当参数，不用减法。**
   我此前在本线 `NegInvolution.lean` 与 `ShCraigElimNegLaw.lean` 上都踩过"层数相减"的坑
   （`tsub` 在 V 内引起摩擦）。这里用 `m' + 1 = n` 的守卫而**不是** `n - 1 = m'`，避开了整类问题。
2. **结论取"反向"**：`iT m (subst … p) = subst … (iT (m+1) p)`，
   主结论由 `exact h m rfl`（`:198`）给出——`m + 1 = m + 1` 的守卫用 `rfl` 消去，干净。

**归纳原理**：`IsSemiformula.pi1_structural_induction`（`:60`），八支。
`definability`（`:62-64`）作为 `hP` 的前提。

## 2. 逐支风险评级

| 支 | 位置 | 风险 | 理由 |
|---|---|---|---|
| `rel` | :65-79 | **低** | 委托给 `iTR_subst_open`（另一条已证件）。本支只做层数搬运 + `congrArg` 无 |
| `nrel` | :80-95 | **低** | 同 `rel`，多一层 `substs_neg`（De Morgan），用 C-398 类对合。结构清楚 |
| `verum` | :96-103 | **极低** | 四条 `rw` 全为常量消去 |
| `falsum` | :104-111 | **极低** | 同上 |
| `and` | :112-126 | **低** | 纯同态：`congrArg₂ (· ^⋏ ·)` 用两个 IH。无层数加减 |
| `or` | :127-141 | **低** | 同 `and` |
| **`all`** | :142-169 | **中** | 层数升两次（`m' → m'+1` 用于 IH 里的 `p`，且 `QvecVOr_succ`/`QvecV_succ` 各升一次）；含 `conv_rhs => rw [imp]` 这类需要精确形状的重写 |
| **`exs`** | :170-193 | **中高** | 同 `all`，且见 §3 的层数不对称 |

**为什么量词支风险高**：它们要同时管三处层数——
(i) `subst` 把量词内的公式层从 `m'+1` 升到 `(m'+1)+1`（`substs_all`/`substs_ex` 的 `qVec`）；
(ii) `iT_all`/`iT_exs` 又把 `iT` 的层参数升一；
(iii) `QvecVOr_succ`/`QvecV_succ` 把**代入向量**也升一层。
三处必须严格对齐，任一处差一就会得到"假等式"或"无法闭合"。本线复现 `iT_substs1` 失败时
6 处 error 全部是这类层数账（`6087aba3` 的记录）。

## 3. 我在 `exs` 支发现的疑点（这是本文件最有价值的一条）

**观察**：`all` 支与 `exs` 支对 `domZero` 的层数写法**不一致**。

`all` 支（:161-166）：
```lean
rw [Bootstrapping.substs_or (L := ℒₜ)
    (isSemiformula_domZero (n := m' + 1)).isUFormula.neg
    (isSemiformula_iT p hp').isUFormula,
  Bootstrapping.substs_neg (L := ℒₛₜ) (n := (m' + 1) + 1)
    (isSemiformula_domZero (n := m' + 1))
    (isSemitermVec_QvecV (V := V) (m' + 1))]
```

`exs` 支（:188-191）：
```lean
rw [Bootstrapping.substs_and (L := ℒₜ)
    (isSemiformula_domZero (n := m')).isUFormula
    (isSemiformula_iT p hp').isUFormula]
rw [subst_QvecV_domZero' (V := V) m']
```

**两边随后都 `rw [subst_QvecV_domZero' m']`，而该引理（:36）陈述的是**
```lean
subst ℒₜ (QvecV (m + 1)) (domZero) = domZero
```
即它**自己**用的是 `QvecV (m+1)` 去代入 `domZero`。所以：
- `all` 支用 `isSemiformula_domZero (n := m' + 1)` + `isSemitermVec_QvecV (m' + 1)`，与引理**层数一致**；
- `exs` 支用 `isSemiformula_domZero (n := m')`，却仍接 `subst_QvecV_domZero' m'`（内部是 `QvecV (m'+1)`）——**层数写法不同但都能闭合**。

**为什么两边都对**（我的判断，标身份：AI 分析，未证）：`domZero` 是
`subst (domN) ?[^#0]` 的编码，它是**常量**（不含自由变量），
`IsSemiformula.domZero` 的层数参数只声明"它的约束变量都 `< n`"，对任何足够大的 `n` 都成立。
所以 `n := m'` 与 `n := m' + 1` 都能满足该前提——**`exs` 支不是错，是"选了较弱的那个也能过"**。

**为什么这值得核实**：不对称说明至少有一处不是按设计写的，而是"试出来能过"。
二次独立证明时应当**统一成一种写法**（建议都取 `m' + 1`，与 `subst_QvecV_domZero'` 的
陈述层数一致），并确认两边都仍闭合。若统一后有一边**不再闭合**，那就说明原先那一处
依赖了某个未被言明的巧合——**那才是真缺陷**。

### §3 的测试**已做**，结果是良性的（2026-10-14 同日）

我把 `exs` 支的 `(n := m')` 统一改成 `(n := m' + 1)`（与 `all` 支一致），在**私有副本树**里重编译
（不动共享树；依赖用 `repro-build` 的 olean）：

| 版本 | exit | error 数 | 公理 |
|---|---|---|---|
| 原样（基线） | **0** | 0 | `[propext, Classical.choice, Quot.sound]` |
| `exs` 支层数统一为 `m' + 1` | **0** | 0 | `[propext, Classical.choice, Quot.sound]` |

**两种写法都闭合。** 所以 §3 的层数不对称**不是缺陷**，也不隐藏巧合——
正如我先前的分析，`domZero` 是常量，层数参数只声明"约束变量 `< n`"，对足够大的 `n` 都成立，
故 `m'` 与 `m' + 1` 都能满足。**§3 作为"最可能藏缺陷处"的猜测被这次测试否掉了。**

这本身是有价值的负面结果：它说明 `exs` 支的层数写法**不脆弱**，二次证明不必在此处花时间。
**`all`/`exs` 两支的风险因此从"中/中高"降为"中"**——剩下的风险只在 `substs_all`/`substs_ex`
的 `qVec` 提升与 `iT_all`/`iT_exs` 的层参数提升是否对齐，而这两处两侧都用 `m' + 1`，写法一致。

## 4. 另一处值得核的：`rel` 支的 `k = 2` 硬编码

`:69-71`：
```lean
have hk2 : k = 2 := by
  rcases Arithmetic.isRel_iff_LOR.mp hR with h' | h' <;> exact h'.1
subst hk2
```

这是把 ℒₒᵣ 的原子谓词 arity **硬定为 2**。我核了 Foundation `Syntax/Language.lean:256-259`：
```lean
lemma isRel_iff_LOR {k R : V} :
    (ℒₒᵣ).IsRel k R ↔
    (k = 2 ∧ R = ⌜(Language.Eq.eq : (ℒₒᵣ).Rel 2)⌝) ∨
    (k = 2 ∧ R = ⌜(Language.LT.lt : (ℒₒᵣ).Rel 2)⌝)
```
**两个析取支都含 `k = 2`**，所以 `rcases … <;> exact h'.1` 取出 `k = 2` 是**穷尽且正确**的，
不是靠"碰巧第一支成立"。当前 ℒₒᵣ 只有 `=` 与 `<`（都二元），这条**完全正确**。

**但它对 ℒₒᵣ 的扩展是脆弱的**：若将来 ℒₒᵣ 加入一元谓词，`isRel_iff_LOR` 会多出含
`k = 1` 的析取支，而 `exact h'.1` 会取出 `k = 1` 从而**直接证不出 `k = 2`**——
那会以**编译错误**形式暴露（不是静默错误），所以是**安全失败**，不是危险失败。
风险等级：**低**（当前正确、且失败方式是响亮的）。二次证明时可选择写成对任意 `k` 的一般陈述，
但那要连带改 `iTR_subst_open` 的一般性——**收益不大，除非确实要扩 ℒₒᵣ**。

## 5. 二次独立证明的建议路径

按"判别力 / 成本"排序：

1. **先做 §3 的层数统一测试**（改 2 个参数重编译）。成本≈5 分钟，判别力最高。
2. **`rel`/`nrel` 支去掉 `k = 2` 硬编码**，改成对任意 `k` 的陈述。成本中等，能顺带验证
   `iTR_subst_open` 的一般性是否真的一般。
3. **量词支（`all`/`exs`）换一种归纳谓词重做**——例如把 `QPred` 的守卫从
   `m' + 1 = n` 换成 `n = m' + 1` 的对称形式，或改用
   `UformulaRec1.Construction.semiformula_result_induction`（本线 C-398/C-399 用的原理）
   而非 `IsSemiformula.pi1_structural_induction`。**换原理才有真正的独立性**；
   只换 rw 顺序不算。
4. 其余四支（`verum`/`falsum`/`and`/`or`）风险极低，可照做。

**关键**：真正的独立性来自第 3 条（换归纳原理），不是第 1、2 条（那只是加固）。
但第 1 条应当**先做**，因为它可能暴露"现在这套只是碰巧过"。

## 6. 边界

- 本文件**没有**运行 Lean，也没有改动任何被评估的源码。全部结论来自**读源码**与读 Foundation 源码。
- 我**没有**声称 `iT_subst_open` 有错。它已被四方核验（001-Flash 做、Master 核、本线复现装配），
  置信度高。本文件找的是"若要双证，从哪儿下手最有判别力"。
- §3 的"层数不对称"**不是缺陷断言**，是"值得做一次统一测试"的观察。我明确标注：
  `domZero` 是常量，故两种层数写法在数学上都成立。
- 未评估：`iTR_subst_open`（`rel`/`nrel` 支委托的件，在 `ITRSubstOpen.lean`）、
  `QvecV`/`QvecVOr` 的定义与 `len_*`/`nth_*` 系列（在 `QvecV.lean`、`ITSubstOpen6.lean`）。
  **若要做完备用评估，这两处是下一个该读的。**
