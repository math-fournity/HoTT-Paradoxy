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

## 十、追加（14:2x）：`ve2` 支的第一块——`shift_subst_domN3`

**新证**：`shift_subst_domN3`（`Ve2ShiftPieces.lean`，sha 见文件）——
`conjunct` 的 domZero 部分在**层 3** 下被 `shift` 固定：
`shift (subst ?[^#i] cDomN) = subst ?[^#i] cDomN`（`i < 3`，即 ve2 的 `conjunct 3 …` 语境）。

**为什么层 3**：`shift_substs` 要求 `IsSemitermVec ℒₛₑₜ 1 m ?[^#i]`，
而 `isSemitermVec_single_bvar` 给的是 `IsSemitermVec ℒₛₑₜ 1 n ?[^#i]`（需 `i < n`）——
`i ∈ {0,1,2}` 时取 `m = 3` 即可。这是**层数记账**的一个具体实例。

**同时确认的关键事实**（供后续用）：
- `shiftVec b n = [^#b, ^#(b+1), …, ^#(b+n-1)]`——**全是 bvar**；
- `termShift` 对 bvar 恒等（`termShift_bvar`），故 `termShiftVec` 对 `shiftVec` 应为恒等；
- 缺 `IsUTermVec.shiftVec`（本机实测不存在）——证 `termShiftVec 1 (shiftVec b n) = shiftVec b n` 需要它
  （或用 `nth_ext'` + `nth_termBShiftVec` + `termShift_bvar` 逐元素，并同时构造 `IsUTermVec`）。

**`ve2` 支剩余**：
1. `termShiftVec 1 (shiftVec 3 n) = shiftVec 3 n`（上一条）；
2. `shift_conjunct`：把 `conjunct 3 n i y` 的 shift 归结为 `conjunct 3 n i (shift y)`
   （用 1 + `shift_subst_domN3` + `shift_and`）；
3. `shift (subst (^#2 ∷ …) (cFunc k f)) = 自身`——闭项，走 `shift_quote`；
4. `shift_qqAlls` 或直接展开 `qqAlls` 的两层 `^∀`。

## 十一、★ 重大吸收（14:4x）：`iVE_shift` 完整版（9276 证出，本会话独立核验）

**9276 已证出 `iVE_shift` 全称版**——正是 `ishift` 的最后障碍。本会话独立核验：

- 文件：`TranslateShiftCompat-2002d386.lean`（sha `2002d386cf4b48be`，15500 B，**0 sorry**）
- **exit 0、`#print axioms` 全部仅三条标准公理**
- 16 条定理：`isUTermVec_eqAtom_vec`、`shift_eqAtom_bvar/fvar`、`iVE_shift_bvar/fvar`、
  `shift_quote_sentence`、`shift_cFunc`、`shift_cDomN`、`shift_cRel`、
  `termShiftVec_shiftVec_V`、`shift_conjunct`、`shift_ve0`、`shift_qqAlls`、`shift_ve2`、
  `iVE_shift_func`、**`iVE_shift`（全称版）**

**这意味着**：`ishift` 的 `rel`/`nrel` 两支的障碍**已清除**。本会话据此推进：

### 本会话新增：`iT_shift` 七支（`ITShift-7of9.lean`）
`iT n (shift p) = shift (iT n p)` 的九支中 **verum/falsum/and/or/all/exs 六支 + 骨架**已过核；
`rel`/`nrel` 两支的组装进行中（用 `iVE_shift` + 9276 的 `shift_conjunct`/`shift_cRel`/`shift_qqAlls`）。

**下游链条现状**：`iVE_shift` ✅ → `iT_shift`（七支 ✅，`rel`/`nrel` 组装中）
→ `tshift` → `hShift` 支 → O2 只剩 `hAll`/`hExs`/`hAxm`。

## 十二、★ 重大进展（16:xx）：hAll 组装完成，只差一条算术蕴含式

### 吸收自 9276（独立核验后）
- `TranslateShiftCompat-a841872c.lean`（837 行，0 sorry，exit 0）：含 **`iT_shift` 完整版**
  （与本会话的 `ITShift-FULL.lean` 独立得到同一结论——**双路互证**）、
  `free_imp_domZero`、`domZero_eq_cDomN`、`shift_imp_domZero`、`shift_iTR` 等。
- `SetupQTools.lean`：从 9276 的 `ShCraigElimSetupQ.lean` 提取的 **`split_or` + `replace_of_imp`**
  （两条完整的 sequent 演算工具），本会话独立核验 exit 0。

### 本会话新证
| 定理 | 文件 | 内容 |
|---|---|---|
| `all_mem` | `HAllProof.lean` | `^∀ (imp domZero (iT 1 p)) ∈ translateSeq s` |
| **`hAll_uncond`** | 同上 | O2 的 hAll 支，**只差 `hAB`**（算术蕴含式，显式前提） |
| `guard_step` | `HAllGuard.lean` | Derivable 层护罩步骤（备用路线） |

### 唯一剩余障碍（精确）

```
hAB : Derivable 𝗭𝗙𝗖 (insert (neg ℒₛₑₜ A ^⋎ B) ∅)
  where A := iT 0 (free ℒₒᵣ p),  B := free ℒₛₑₜ (imp ℒₛₑₜ domZero (iT 1 p))
```

A、B 都是 ℒₛₑₜ **闭公式**（层 0）——属 𝗭𝗖𝗙 内部可证性（Σ1 完全性范围）。
9276 的三条候选路径见其交接文档；`free_imp_domZero` 是把它归约到"代入相容"的关键一步。

`hExs` 同形（用 `substs1`）。

## 十三、★ 负面结果（机器证明）：朴素的 iVE/subst 律不成立

`ITSubstCounter.lean`（exit 0、公理干净）证明：

- `subst_eqAtom_fvar_neq`：`subst ?[^&0] (eqAtom ^&x) = ^rel 2 cEqN [^&0, ^&x]`（**不是** `eqAtom ^&x`）
- `naive_lhs`：`iVE 0 (termSubst ?[^&0] ^&x) = eqAtom ^&x`
- **`naive_law_is_false_shape`**：两者**不同**

**原因**：`subst ?[^&0]` 替换的是**被替换公式自身的 bvar 0**，而 `eqAtom t = ^rel 2 cEqN [#0, t]`
的绑定变量恰在位置 0——替换会命中它。所以"`iVE` 与 `subst` 交换"的等式形状**恒假**。

**这机器验证了 9276 的最终判断**：`hAll` 的剩余义务必须是**蕴含式**（Σ1 完全性范围），
而非等式。三轮反例（9276 的两轮 + 本会话这一条）现已全部机器化。

## 十四、hAB 的精确归约（本会话，路径①推进）

**关键恒等式**（`HABKey.lean`，已定型）：
```
iT 0 (free ℒₒᵣ p) = subst ?[^&0] (iT 1 (shift ℒₒᵣ p))     [p 层 1]
```
若成立，则 `B = free (imp domZero (iT 1 p)) = imp (x∈ω) A`（用 `free_imp_domZero` + `iT_shift`），
于是 `A → B` 由**排中律**立得——`hAB` 变成一条平凡的命题逻辑事实！

**证明该恒等式的元层归约**（路径①）：
- `free p = subst ?[^&0] (shift p)`（定义）
- 对引号化 `φ = ⌜ψ⌝`：`subst ?[^&0] ⌜ψ⌝ = ⌜ψ[^&0]⌝`（`quote_substs'`），
  `iT n ⌜ψ⌝ = ⌜translate ψ⌝`（`iT_quote`）
- 故归结为**元层**：`translate (ψ[^&0]) = (translate ψ)[^&0]`（翻译与代入交换）

**当前卡点**：Foundation 的 `DirectTranslation`（`LK/Interpretation.lean:15`）**没有** subst 相容引理
（本机 grep 确认）。需自证——但它是对 `translate` 的结构归纳（`translate` 由
`translateAux` 定义，各构造子有 `translate_rel`/`_all`/`_ex` 等 `rfl` 级引理），
**比码层等式实质性地易**。这是下一会话的具体动作。

**另注**：`HABKey` 只对 `p = ⌜ψ⌝`（元层标准公式）有效；`hAll` 里 `p` 是 V 内任意码。
9276 已指出这个局限——但若把 `hAll` 的应用场景限制在标准公式（`induction1` 的 `d` 来自
标准推导时），可能够用。**这一点需要用户或更深分析裁定。**

## 十五、hAB 的完整障碍图谱（本会话实测，供裁定）

### 已验证的事实

1. **`A → B` 不是等式**：`A := iT 0 (free p)`、`B := free (imp domZero (iT 1 p))`。
   若 `A = subst ?[^&0] (iT 1 (shift p))`（`HABKey.lean` 陈述的恒等式）成立，
   则 `B = (x∈ω) → A`，`A → B` 由排中律立得。
2. **该恒等式在原子支失败**：`iTR` 定义里的 `conjunct b n i y` 含
   `subst ?[^#i] cDomN`——**自己的 bvar 0**。`subst ?[^&0]` 会命中它
   （与 `ITSubstCounter.lean` 证明的反例同源）。
3. **元层归约也不通**：Foundation 的 `DirectTranslation`（`LK/Interpretation.lean:15`）
   **无** subst 相容引理；自证需处理 `translateRel` 的 `Rew.subst`/`Rew.emb` 交互，
   工作量与 `iVE_shift` 同级或更大。

### 三条路径的实测评估

| 路径 | 状态（本会话实测） |
|---|---|
| ① 元层引理（`iT_quote` + `free_quote` → 元层 `translate (ψ[^&0]) = (translate ψ)[^&0]`） | 元层引理**不存在**，需自证；且只对 `p = ⌜ψ⌝` 有效，`hAll` 里 `p` 是任意码 |
| ② 对 `p` 结构归纳 | `free` 不是 `UformulaRec1` 构造（它用 `substs1` = `subst`），无法直接套 `semiformula_result_induction` |
| ③ 改 `iT` 定义（`all`/`exs` 支用替换语义而非保护语义） | **接口级改动**：`iT` 已被 C-390/C-391 等收据引用。**须研究发起人裁定** |

### 结论

**`hAll`/`hExs` 的剩余义务是本路线的实质性研究缺口**，不是工程长尾。
`hAll_uncond` 已把它**精确隔离**为一条显式前提（`HAllProof.lean` 的 `hAB`），
其余 9 支的组装、全部工具（`split_or`/`replace_of_imp`/`free_imp_domZero`）都已就位并机器核验。
**这正是"接口级裁定点"**——路径③（改 `iT` 定义）或接受 `hAB` 为假设，需要用户决定。

## 十六、路径①的精确技术卡点（本会话实测）

尝试把 `hAB` 的引号化情形归约到元层 `translate (free ψ) = free (translate ψ)` 时，
遇到**同一类结构障碍**：

- `Semisentence L n = Semiformula L Empty n`（fvar 域 `Empty`），
  而 `Rewriting.free : F (n+1) →ˡᶜ F n` 需要 `Rewriting L ℕ F ℕ F` 实例——
  对 `Semisentence ℒₒᵣ` **不直接可得**（`Rewriting ?m ℕ (Semisentence ℒₒᵣ) ℕ (Semisentence ℒₒᵣ)`
  实例合成失败）。
- 需先走 `Rewriting.emb`（`Empty → ℕ` 提升，`shift_quote` 用的正是这条），
  再谈 `free`——但 `free` 作用后域变回 `Empty`，形成往复。

**结论**：路径① 不是"一条元层引理"，而是**需要先解决 `Semisentence`/`Semiproposition`
域转换下的 `free` 语义**——与 `shift` 遇到的是同一族问题（本会话 `shift_domZero` 用
`rew_eq_self_of` 绕过了它；但 `free` 改变域，绕不过去）。
**这是本会话能给下一会话的最精确卡点描述。**

## 十七、路径①的最终定位（本会话最后一段实测）

**可用的桥**（Foundation `Formula/Coding.lean:125`）：
```lean
free_quote (φ : Semiproposition L 1) :
    (⌜Rewriting.free φ⌝ : Formula V L) = Bootstrapping.Semiformula.free ⌜φ⌝
```
两侧都是**类型化**的 `Formula V L`（`= Semiformula V L 0`）。
而 `Bootstrapping.Semiformula.free (p : V) : V := substs1 L ^&0 (shift L p)`。

**归约链**（引号化 `p = ⌜ψ⌝` 的情形）：
```
iT 0 (free ⌜ψ⌝) = iT 0 ⌜Rewriting.free ψ⌝ = ⌜translate (Rewriting.free ψ)⌝
free (iT 1 ⌜ψ⌝) = free ⌜translate ψ⌝ = ⌜Rewriting.free (translate ψ)⌝
⟹ 需元层：translate (Rewriting.free ψ) = Rewriting.free (translate ψ)
```

**元层定理的难度**：`Rewriting.free` 由
`LawfulSyntacticRewriting.app_subst_fbar_zero_comp_shift_eq_free`
（即 `(shift φ)/[&0] = free φ`）定义；`translate` 是 `DirectTranslation.translate`，
其 `translateRel` 用 `Rew.subst`/`Rew.emb` 与索引映射构造。
**证明需要交换 `translateRel` 的 `Rew.subst` 与 `free` 的 `/[&0]`**——
一条 Foundation 未提供的重写系统交换律。工作量与 `iVE_shift` 同级或更大。

**且**：即使证成，也只覆盖 `p = ⌜ψ⌝`（标准公式）；`hAll` 的 `p` 是 V 内任意码。
（`induction1` 的 `d` 来自 `Derivation Sh.craig d`，其结论句 `zfcTr G` 是标准的，
但 `allIntro` 支里的 `p` 本身不保证标准。）
