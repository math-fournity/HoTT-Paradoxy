# 接力：层数记账障碍已被证伪（给正在攻 iT_neg 的会话）

> 2026-10-11，CG-009 会话产出。请转达给 canonical 或新工位 `cg007-w8-d3` 上正在攻
> `ShCraigElimNegLaw.iT_neg` 的会话。**本文件不改任何共享文件、不改他人源码**，只是接力信息。

## 一句话

**9276 会话判定"层数记账走不通"是误判，已机器证伪**：`listMax (termBVVec k v) ≤ n`
从归纳假设 `IsSemiformula ℒₒᵣ n (^nrel k R v)` 的 **`bv_le` 字段直接可得**——
不需要从 `IsUTermVec` 单打独斗。

## 证据（三条定理，全过核、公理干净）

文件：`docs/形式化综合研判-20261011/成果-NrelFix/NrelFixProbe.lean`
（sha256 `5b8006c3…`；本会话 pinned Lean 4.34.0 + Foundation `1fb01b72`，exit 0）

```lean
-- 1. 那条"不成立"的不等式，从公式侧假设直接得
lemma listMax_le_of_semiformula {n k R v : V}
    (hp : IsSemiformula ℒₒᵣ n (^nrel k R v)) :
    listMax (termBVVec (L := ℒₒᵣ) k v) ≤ n

-- 2. IsUTermVec 也从它分解出来
lemma isUTermVec_of_nrel (hp : IsSemiformula ℒₒᵣ n (^nrel k R v)) :
    IsUTermVec ℒₒᵣ k v

-- 3. nrel 支所需的公式性：完整可达
lemma isSemiformula_iTR_of_nrel (hp : IsSemiformula ℒₒᵣ n (^nrel k R v)) :
    IsSemiformula ℒₛₑₜ n (iTR n k R v)
```

关键机制：`IsSemiformula` 是两字段结构 `⟨isUFormula, bv_le : bv L p ≤ n⟩`；
`bv (^nrel k R v) = listMax (termBVVec k v)`（Foundation `bv_nrel`，Basic:1289）。
Foundation 自己在 `IsSemiformula.rel`（Basic:1361）就从这个字段推同一不等式。

## 对 `iT_neg` 修复的直接含义

1. **`nrel` 支**：不需要层数升级障碍的"出路"——直接携带 `hp : IsSemiformula ℒₒᵣ n (^nrel k R v)`
   （归纳原理本来就给），需要公式性时用 `isUFormula_iTR hR hv.isUTerm`（注意：
   **`isUFormula_iTR` 只要求 `IsUTermVec`**，不是 `isSemiformula_iTR` 的 `IsSemitermVec`——
   9276 把这两个引理混淆了，它文件里的 `isUFormula_iTR` 本来就够用）。
2. **`all`/`exs` 支**：`iT.construction.allChanges/exsChanges := n + 1`（按定义），
   展开顺序应为：先 `result_all`/`result_exs`（镜像已过核的 `isSemiformula_iT`，
   `SeqTranslateFormula.lean` 内的写法），再 `nth_adjoin_zero`，最后 IH 实例化 `i 0`。
   **不要**先 `simp only [iT.construction]`（它对 `allChanges` 的 lambda 不化简）。
3. **注意**：修复应在**该文件自己的依赖上下文**（新工位 `cg007-w8-d3`）里做——
   它在 canonical 依赖集下会因 `SeqTranslateFormula` 差异产生无关错误（本会话实测）。

## 附：对"对话录版九支填法"的独立实测（2026-10-11 11:16）

新工位创建的 `ProbeNegLawFromTranscript.lean`（把 WorkBuddy 对话录 1265–1345 行的
`iT_neg` 九支填法原样搬来）经本会话独立编译：**exit 1**。根因：该填法的归纳谓词
`P := fun param _n p q => iT param (neg p) = neg q` **缺 `param = n` 护罩**。
`semiformula_result_induction` 的输出层 `param` 与输入层 `n` 独立量化，而 `iT` 改层——
必须用 `P := fun param n p q => param = n → iT param (neg p) = neg q`
（照已过核的 `isSemiformula_iT` 的形状），各支加 `intro h` 并在 IH 处传 `h`。
**该填法不能原样使用**；改护罩形状后其余九支的逻辑（`neg_rel`/`iT_nrel` 等配对）是可复用的。

## 参考

- 完整证伪记录：`docs/形式化综合研判-20261011/成果-NrelFix/README.md`
- 扫描日志第 23–26 轮：`docs/形式化综合研判-20261011/增量扫描日志.md`
