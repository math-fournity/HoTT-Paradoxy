# 成果-IShiftDomZero：ishift 的两个量词支（本会话新证）

> 2026-10-11 12:4x，CG-009 会话。**本会话原创成果**，非吸收。
> 全部 exit 0、0 sorry、`#print axioms` 仅 `[propext, Classical.choice, Quot.sound]`。

## 一、内容

| 定理 | 文件 | 意义 |
|---|---|---|
| `shift_domZero` | `ShiftDomZero.lean` | **枢纽原子**：`shift domZero = domZero` |
| `rew_shift_emb` | 同上 | `Rewriting.shift` 固定 `emb` 化句子的引号 |
| `shift_imp` | `IShiftAllExs.lean` | `shift` 对 `imp` 分配（`imp p q = neg p ⋎ q`） |
| `ishift_all` | 同上 | `ishift` 的**全称支**：IH@n+1 ⇒ 支@n |
| `ishift_exs` | 同上 | `ishift` 的**存在支**（对偶） |
| `isSemiformula_mono_or` | 同上 | ℒₒᵣ 层单调（`SeqTranslateFormula` 的 ℒₛₑₜ 版对偶） |

## 二、为什么 `shift_domZero` 是枢纽

`iT` 给每个量词**多引一个 `domZero` 约束变量**（`iT_all : iT n (^∀ p) = ^∀ (domZero → iT (n+1) p)`），
而 `shift` 的 `all` 支**不引新变量**（`shift (^∀ p) = ^∀ (shift p)`）。两边量化结构逐层错位一个 `domZero`。

`ishift` 的 `all` 支展开：
- LHS：`iT n (^∀ (shift q))` = `^∀ (imp domZero (iT (n+1) (shift q)))`
- RHS：`shift (^∀ (imp domZero (iT (n+1) q)))` = `^∀ (shift (imp domZero (iT (n+1) q)))`
- 用 `shift_imp` 展开 RHS 得 `^∀ (imp (shift domZero) (shift (iT (n+1) q)))`
- **只剩 `shift domZero = domZero`**（再配 IH）。`exs` 支同构（`^⋏` 替 `imp`）。

## 三、`shift_domZero` 的证明路线（本会话发现）

`domZero = subst [#0] cDomN` 且 `cDomN = ⌜arithTrln.domain⌝`（闭项引号）。关键：
- `Semisentence L n = Semiformula L Empty n`——**自由变量域是 `Empty`**；
- `Rewriting.shift` 只作用于自由变量，故对 `Empty` 域公式是恒等；
- Foundation 已有 `Semiformula.rew_eq_self_of`（无自由变量 ⇒ rewriting 恒等）
  与 `Semiformula.fvSup_sentence`（`emb σ` 的 `fvSup = 0`）；
- `Sentence.quote_def : ⌜σ⌝ = ⌜Rewriting.emb σ⌝` 是 `rfl`（引号定义自带 emb）。

证明：`domZero = ⌜domain/[#0]⌝`（`quote_domain_zero` + `emb_app_self`）
→ `quote_def` 换成 `emb` 形式 → `← Semiformula.quote_shift` → `rew_shift_emb`。

## 四、边界（不得读成已完成）

- **`ishift` 主定理未组装**：两支各自需要 IH（本文件把它们作为**显式前提**），
  完整的 `ishift` 需要跨 `iT`/`iVE` 与 `shift` 的**双结构互归纳**——尚未做。
- `tshift ⇐ ishift` 的归约已过核（`GateBranches.tshift_of_ishift`），但 `ishift` 未证，
  故 `tshift` 仍**未证**。
- `hAll`/`hExs`/`hShift` 三支**未接线**到 `ShCraigElimSetup.induction_setup`。
- `ShCraigElim`、`zfcTr_D3_internalize` 仍未证。

## 五、给下一会话的最短路线

`ishift` 的完整证明需要 `IsSemiformula` 上的双归纳（`semiformula_result_induction`
或 `IsSemiformula.pi1_structural_induction`），谓词形如
`P n p := iT n (shift p) = shift (iT n p)`（注意 `iT` 改层、`shift` 不改，
可能需要 `param = n` 式护罩或层单调配合）。原子支已由 `IShiftAtom.lean` 覆盖
（`iVE_termShift_bvar`/`fvar` + `shift_eqAtom`），量词支由本文件覆盖；
**剩 `and`/`or` 支（用 `shift_and`/`shift_or` + `iT_and`/`iT_or` 直接组合）与组装**。

## 六、追加（12:5x）：`ishift` 主体八支中六支已证

`IShiftFull-6of8.lean`（sha256 `e7bd939f…`）：**verum / falsum / and / or / all / exs 六支全部无 sorry**，
exit 0、公理干净。剩 `rel` / `nrel` 两支，卡在：

**项级 `iVE`/`termShift` 相容律缺 `func` 情形**（`IShiftAtom.lean` 只有 `bvar`/`fvar` 两个原子情形）。
`rel` 支展开：
- `iT_rel : iT n (^rel k R v) = iTR n k R v`
- `shift_rel : shift (^rel k R v) = ^rel k R (termShiftVec k v)`
- `iTR n k R v = qqAlls (imp (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ⊤)) (subst [#0,#1] cRel R)) 2`
- 需：`iVE n (termShift t) = shift (iVE n t)` 的一般项级版（含 `func` 情形）——
  `iVE.construction.func := fun p k f _ w ↦ if k = 0 then ve0 k f else ve2 (p 0) k f w`
  （递归，需 `IsSemiterm.sigma1_induction` 或 `TermRec` 归纳）。

`IShiftRelProbe.lean` 固定了归约点（`iTR param k R (termShiftVec k v) = shift (iTR param k R v)`）。
**这是本会话交接给下一会话的最短路线**：先证项级 `iVE`/`termShift` 相容（三支：bvar/fvar/func），
再填 `rel`/`nrel`，`ishift` 即完成；随后 `tshift ⇐ ishift`（已过核）即解锁。

## 七、追加（13:1x）：通用工具 `shift_quote` + `func` 情形 0 元支 `shift_ve0`

| 定理 | 文件 | 内容 |
|---|---|---|
| `shift_quote` | `ShiftQuote.lean` | **通用工具**：`shift` 固定任意 `Semisentence` 的引号 |
| `rew_shift_quote` | 同上 | Rewriting 层版本 |
| `shift_cFunc0` | `ShiftVe0.lean` | `shift` 固定 `cFunc 0 f`（numeral = 句子引号） |
| `shift_subst_cFunc0` | 同上 | `shift` 固定 `subst [#0] (cFunc 0 f)` |
| `shift_ve0` | 同上 | **`iVE` 的 `func` 情形 k=0 支**：`shift (ve0 0 f) = ve0 0 f` |

`shift_quote` 的证明用 `Sentence.quote_def`（`⌜σ⌝ = ⌜emb σ⌝` 是 `rfl`）
+ `← Semiformula.quote_shift` + `Semiformula.rew_eq_self_of`（无自由变量 ⇒ rewriting 恒等）。
**这是可复用的工具**：任何闭项引号（`cDomN`、`cFuncN`、`cRelN`、numeral）的 shift-不变性都走它。

## 八、`rel`/`nrel` 支剩余工作（精确化）

`iVE` 的 `func` 情形现况：
- **k = 0 支**：✅ `shift_ve0`（本文件）
- **k ≠ 0 支**：`ve2 n k f w`——需 `shift (ve2 n k f w) = ve2 n k f (shiftVec w)`，
  其中 `w = resultVec ![n] k v`。含 `conjunct 3 n i w.[i]`（层数记账）与 `subst (^#2 ∷ …) (cFunc k f)`。
  **这是 `rel`/`nrel` 支的最后一个障碍**。

完成 `iVE`/`termShift` 一般相容（`iVE n (termShift t) = shift (iVE n t)`，项归纳三支）后：
- `rel`/`nrel` 两支可填（探针 `IShiftRelProbe.lean` 已固定归约点）；
- `ishift` 完成 ⇒ `tshift`（`GateBranches.tshift_of_ishift` 已过核）⇒ `hShift` 支。

## 九、第 33 轮吸收（13:2x）：9276 的 `iVE_shift` 原子支

**扫描捕获**：`9276-cg007-w8-d3` 新增未跟踪 `TranslateShiftCompat.lean`（12:50）——
**与本站线相同**（其文件头分析与本会话完全一致：三支归结为 `iT_shift` → `iVE_shift`）。

**独立核验**：sha `966fb6a7d0f7b743`，**exit 0**、五条定理公理仅三条标准公理。
**已吸收**为 `TranslateShiftCompat-966fb6a7.lean`（防回退副本）。

内容（本会话此前没有的）：
- `shift_eqAtom_bvar`：`shift (eqAtom ^#z) = eqAtom ^#z`
- `shift_eqAtom_fvar`：`shift (eqAtom ^&x) = eqAtom ^&(x+1)`
- `iVE_shift_bvar` / `iVE_shift_fvar`：`iVE_shift` 的两支

**两工位互补关系**（诚实记录）：
| 零件 | 来源 |
|---|---|
| `shift_domZero`、`shift_quote`、`ishift_all`/`ishift_exs`、`ishift` 六支 | **本会话（elegant-mclaren）** |
| `iVE_shift` bvar/fvar 两支、`shift_eqAtom_*` | **9276**（本会话核验吸收） |
| `func` 支（`ve2`） | **双方都确认是剩余障碍** |

**警告**：9276 该文件仍是**未跟踪**状态（不在 git 中）——若其清理工作树会丢失。
本会话已防回退复制。
