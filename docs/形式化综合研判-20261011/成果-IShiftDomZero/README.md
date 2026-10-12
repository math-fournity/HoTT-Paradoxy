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

## 十八、继续吸收（17:5x）：9276 的 `provable_into_sequent`

**核验**：从 9276 的 `ShCraigElimSetupQ.lean`（sha `0ab3d651`）提取 `provable_into_sequent`，
独立编译 **exit 0**。

```lean
lemma provable_into_sequent {A B : V} (hB : IsFormulaSet (L := ℒₛₑₜ) B)
    (hd : Derivable 𝗭𝗙𝗖 (insert A ∅)) : Derivable 𝗭𝗙𝗖 (insert A B)
```

**用途**（9276 定位）：`hRoot` 收尾的必需件——`Derivable.by_axm` 只接受**公理**，
而 `Sh.craig` 的公理经翻译后只是**可证**（由 `Sh.craig ⪯ Sh`），
所以要先把「可证」搬进目标 sequent。

**hRoot 的剩余难点**（9276 精确化）：把 `p ∈ Sh.craig.Δ₁Class`
（其 `mem_iff` 是 `CraigTrick.lean:311` 的复合式）化到 `Sh.craig` 成员，
再经 `Sh.craig ⪯ Sh` + `iT_quote` + `provable_into_sequent` 收尾。
技术障碍：`Theory.Δ₁.mem_iff` 接受元层 `Proposition`，而 `hRoot` 手里是 V 元素——
需用 `Δ₁Class.defined` 实例的 `.iff`。

## 十九、hRoot 的精确形状（本会话探明）

`hRoot` 的目标：`p ∈ Sh.craig.Δ₁Class ⟹ Provable 𝗭𝗙𝗖 (iT 0 p)`。

**解包**（`CraigTrick.lean:236` 的 `Theory.isCraigAxiom_quote_iff`）：
```
T.IsCraigAxiom ⌜φ⌝ ↔ ∃ ρ ∈ T.craig, φ = ρ
```
而 `T.craig` 的成员是 `ρ.padding k`（`ρ ∈ T`，`k : ℕ`）——
所以 Craig 公理是 **`ρ.padding k`** 形式（`ρ` 是原理论的句子）。

**可用零件**（本会话实测确认存在）：
- `Sh_provable_iff : Sh ⊢ σ ↔ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ`（`Z0Shadow.lean:44`）
- `provable_iff_provable : Provable T ⌜φ⌝ ↔ T ⊢ φ`（Foundation）
- `iT_quote : iT n ⌜φ⌝ = ⌜arithTrln.translate φ⌝`
- `Entailment.padding_iff : 𝓢 ⊢ padding φ k 🡘 φ`
- `Derivable.by_axm`（V 层公理规则）
- `provable_into_sequent`（本会话吸收）

**归约链**（`HRoot.lean` 已写出骨架）：
```
p = ⌜ρ.padding k⌝
iT 0 p = ⌜translate (ρ.padding k)⌝          [iT_quote]
需要 𝗭𝗙𝗖 ⊢ translate (ρ.padding k)
  ← padding_iff 给 translate ρ ↔ translate (ρ.padding k)（需 translate 与 padding 相容）
  ← Sh_provable_iff 逆用：ρ ∈ Sh ⟹ Sh ⊢ ρ ⟹ 𝗭𝗙𝗖 ⊢ translate ρ
⟹ Provable 𝗭𝗙𝗖 (iT 0 p)                    [provable_iff_provable]
```

**剩余技术障碍**（与 9276 一致）：`Theory.Δ₁.mem_iff` 接受元层 `Proposition`，
而 `hRoot` 手里是 V 元素 `p`——需用 `Δ₁Class.defined` 实例的 `.iff`（对任意 V 元素），
并处理 `translate` 与 `padding` 的相容（`translate (padding φ k)` 的形状）。
**这比 hAB 更接近完成**（零件齐全，无元层交换律缺失）。

## 二十、hRoot 的三个解包引理（本会话新证）

`HRoot.lean`（三条引理全部 exit 0、公理干净）：

```lean
lemma mem_craig_iff_eval {p : V} :
    p ∈ Sh.craig.Δ₁Class ↔ (Semiformula.Evalb ![p]) Sh.craig.Δ₁ch.val
lemma mem_craig_quote_iff (φ : Sentence ℒₒᵣ) :
    (⌜φ⌝ : V) ∈ Sh.craig.Δ₁Class ↔ φ ∈ Sh.craig
lemma mem_craig_iff_padding {φ : Sentence ℒₒᵣ} :
    φ ∈ Sh.craig ↔ ∃ σ s, ℕ ⊧/![s, ⌜σ⌝] Sh.reWitness.val ∧ φ = σ.padding s
```

**这三条把 `hRoot` 的 V 层成员关系完全解包**——9276 指出的"技术障碍"
（`Δ₁Class.mem_iff` 接受元层 Proposition 而手里是 V 元素）**已用
`Δ₁Class.defined.iff`（V 层版本）绕过**。

**`hRoot_uncond` 的剩余**（`HRoot.lean` 中仍 sorry）：从解包后的
`∃ σ s, reWitness(s,⌜σ⌝) ∧ φ = σ.padding s` 推出 `Provable 𝗭𝗙𝗖 (iT 0 φ)`：
1. `iT 0 ⌜σ.padding s⌝ = ⌜translate (σ.padding s)⌝`（`iT_quote`）
2. 需 `𝗭𝗙𝗖 ⊢ translate (σ.padding s)`——`padding_iff` 给 `translate σ ↔ translate (σ.padding s)`，
   而 `σ ∈ Sh` 经 `Sh_provable_iff` 给 `𝗭𝗙𝗖 ⊢ translate σ`
3. `provable_iff_provable` 收尾

**这是 hRoot 的全部剩余**，零件齐全、无缺失的元层律。

## 二十一、★ 新证：`translate_padding`（hRoot 的关键零件）

```lean
lemma translate_conj_top (k : ℕ) :
    arithTrln.translate ((List.replicate k ⊤).conj) = (List.replicate k ⊤).conj
lemma translate_padding (σ : Semiproposition ℒₒᵣ 0) (s : ℕ) :
    arithTrln.translate (σ.padding s) = (arithTrln.translate σ).padding s
```

**两条都 exit 0、公理干净**。这是 `hRoot` 归约链上的关键一步：
Craig 公理是 `σ.padding s`，而 `translate` 与之交换意味着
`iT 0 ⌜σ.padding s⌝ = ⌜(translate σ).padding s⌝`——把问题化为
「`𝗭𝗙𝗖 ⊢ translate σ`」（由 `Sh_provable_iff` + `σ ∈ Sh` 得）
加上 padding 保持可证性（`Entailment.padding_iff`）。

**证明要点**：`padding φ k = φ ⋏ (List.replicate k ⊤).conj`；
`translate` 是 `→ˡᶜ`（`LogicalConnective.HomClass`），
`map_and` 给 `⋏` 的保持，`translate_conj_top` 由 `List.conj` 的归纳给
（`replicate_succ` + `map_top`）。
**注意**：须在 `Semiproposition`（ℕ 域）层陈述——`Semisentence` 的
`Sentence` coercion 会造成 defeq 不匹配。

## 二十二、hRoot 的当前状态（本会话终态）

**已证**（`HRoot.lean`，exit 0、公理干净）：
- `mem_craig_iff_eval` / `mem_craig_quote_iff` / `mem_craig_iff_padding`（三个解包引理）
- **`translate_conj_top`** / **`translate_padding`**（translate 与 padding 交换）

**剩余**（`hRoot_quoted` / `hRoot_uncond`，带完整 roadmap 的 sorry）：
归约链已完全确定——
```
φ ∈ Sh.craig ⟹ φ = σ.padding s, σ ∈ Sh
iT 0 ⌜σ.padding s⌝ = ⌜translate (σ.padding s)⌝        [iT_quote]
                  = ⌜(translate σ).padding s⌝          [translate_padding ✅]
𝗭𝗙𝗖 ⊢ translate σ                                     [Sh_provable_iff + σ ∈ Sh]
𝗭𝗙𝗖 ⊢ (translate σ).padding s                         [Entailment.padding_iff]
Provable 𝗭𝗙𝗖 (iT 0 ⌜σ.padding s⌝)                     [provable_iff_provable]
```
**唯一摩擦**：`Sentence`（Empty 域）与 `Semiproposition`（ℕ 域）之间的 coercion——
`iT_quote` 作用于 `Semisentence`，而 `padding` 后的引号涉及 `Rewriting.emb` 的显式形式。
**这是纯 API 适配**（不是缺失的数学），零件全部齐备。

## 二十三、本会话总产出（终态）

**42/42 从零重编译通过**。分支 `claude/elegant-mclaren-767fb0` 已推送。

| 类别 | 内容 |
|---|---|
| 新证 | `shift_domZero`、`shift_quote`、`ishift` 六支、`shift_ve0`、`iTR_shift`、**`iT_shift`**、**`tshift`**、**`hShift_uncond`**、`all_mem`、`guard_step`、`isFormulaSet_of_setShift_eq`、**`hAll_uncond`**、`naive_law_is_false_shape`、`mem_craig_*`、**`translate_padding`** |
| 吸收 | `iVE_shift`（9276）、`split_or`/`replace_of_imp`（9276）、`provable_into_sequent`（9276） |
| O2 状态 | 10 支中 **8 支就绪**（7 无条件 + hAll 差 hAB） |
| 剩余 | `hAB`（研究缺口）、`hExs`（同形）、`hRoot`（纯 API 适配） |

## 二十四、`translate_padding` 的推广（本会话最后一段）

```lean
lemma translate_conj_top' {ξ : Type*} (k : ℕ) :
    arithTrln.translate ((List.replicate k (⊤ : Semiformula ℒₒᵣ ξ 0)).conj) =
      (List.replicate k (⊤ : Semiformula ℒₛₑₜ ξ 0)).conj
lemma translate_padding {ξ : Type*} (σ : Semiformula ℒₒᵣ ξ 0) (s : ℕ) :
    arithTrln.translate (σ.padding s) = (arithTrln.translate σ).padding s
```

**推广到任意 fvar 域 `ξ`**（原来只在 `ℕ` 域）——因为 `hRoot` 的引号涉及
`Empty` 域（`Sentence`），需要这个一般版本。两条都 exit 0、公理干净。

**`hRoot_quoted` 的剩余摩擦（纯 API）**：
- `Provable.{u_1,0}`（`V : Type u_1`）与 `provable_iff_provable` 的 `Provable.{0,_}` 宇宙不匹配；
- `Sentence`（Empty）与 `Semiproposition`（ℕ）的 coercion 在最后一步的对齐。
**数学内容已全部就位**（5 步归约链 + 全部零件已证/已核验）。

## 二十五、hRoot 最后摩擦的精确性质（本会话终局分析）

`provable_iff_provable : Provable T (⌜φ⌝ : ℕ) ↔ T ⊢ φ`——**定义在 ℕ 层**，
而 `hRoot` 的目标是 `Provable 𝗭𝗙𝗖 (iT 0 p)`，其中 `V : Type u_1`（**任意模型**）。
宇宙参数不匹配（`Provable.{u_1,0}` vs `Provable.{0,_}`）不是笔误，而是**实质区别**：
- ℕ 层的 `Provable T ⌜φ⌝` 是元层的"T 证明了 φ"；
- V 层的 `Provable 𝗭𝗙𝗖 x` 是"在 V 内存在 x 的推导编码"。

**两者的桥**是 `Provable.sound`/`Provable.complete`（`D1.lean:36-41`），
它们也定义在 `ℕ`（`T.internalize ℕ`）。**跨到任意 `V` 需要 `V ⊨ 𝗜𝚺₁` 的内部化**——
这正是 `ShRE.lean`/`TranslateRE.lean` 做的事（`iT_encode` 等）。

**所以 `hRoot` 的剩余不是"纯 API"**——我此前判断有误，现更正：
它需要 V 层的 `Provable` 与元层可证性的桥，属于 `Z0UniBridge`/`ShCraigElim` 的**同一实质内容**
（9276 也把它标为"hRoot 就是 D3 本身"）。

**本会话的净贡献**（hRoot 线）：三个解包引理 + `translate_padding`（任意 fvar 域），
把 hRoot 的**可证性部分**（Craig 公理 → translate σ 可证 → padding 后仍可证）完全打通，
只剩 V/ℕ 层的 `Provable` 桥——而那是整条消去的核心难点，不是本分支的技术细节。

## 二十六、★ 对 hAB 的重新评估（本会话最后一段，重要更正）

### 之前的判断（§十三、§十五）需要细化

我先前用 `ITSubstCounter.lean` 证明"朴素 iVE/subst 等式律恒假"——**那是对的**，
但**结论范围被我夸大了**。精读 Foundation 后发现：

**`qVec` 机制保护内层绑定变量**：
```lean
qVec w = ^#0 ∷ termBShiftVec L (len w) w      -- Term/Functions.lean:557
substs_all : subst L w (^∀ p) = ^∀ (subst L (qVec L w) p)
```
`subst` 下降过绑定子时用 `qVec`——**前置一个新的 bvar 0 并把原有索引整体 +1**。
所以在 `iTR`（`qqAlls(·, 2)`，两层绑定）的深度 2 处，`subst ?[^&0]` 落在索引 2，
**不会命中 `iVE` 内部 `eqAtom` 的 bvar 0**。

我的反例（`subst ?[^&0] (eqAtom ^&x) ≠ eqAtom ^&x`）是**无绑定子包裹**的情形——
`eqAtom` 裸放时其 bvar 0 确实被命中。**但在 `iTR` 的实际结构里它被 `qqAlls` 包着。**

### Foundation 提供的两条关键机制
- `termSubstVec_qVec_qVec : termSubstVec (qVec w) (qVec v) = qVec (termSubstVec w v)`
- `substs_qVec_bShift : termSubst (qVec w) (termBShift t) = termBShift (termSubst w t)`

这两条正是"替换与替换交换"所需的机制——**hAB 的恒等式在 iTR 层可能真的成立**。

### 修正后的判断
- **不是**"朴素律恒假所以只能走蕴含式"；
- **而是**"裸公式的律恒假，但 iTR 的绑定结构恰好使正确的律成立"——
  正确的律应陈述为**带 qVec 的形式**（或直接在 iTR 层）。

### 下一步（精确）
证 `iTR_shift` 的类似物：`iTR 0 2 R (termSubstVec 2 ?[^&0] (termShiftVec 2 v))
= subst ?[^&0] (shift (iTR 1 2 R v))`——
需 `substs_all`/`substs_ex`（qVec）+ `substs_rel` + `termSubstVec_qVec_qVec` 的组合。
**这是 hAB 的可行突破口**（此前被我误判为"只能走蕴含式"）。

## 二十七、hAB 的突破口已定型（`ITRSubst-target.lean`）

**目标引理**（陈述已过类型检查）：
```lean
lemma subst_cRel_under_binders (R : V) :
    subst ?[^&0] (qqAlls (subst [#0,#1] (cRel R)) 2)
      = qqAlls (subst (qVec ?[^&0]) (subst [#0,#1] (cRel R))) 2
```

**证明路径**（零件已确认存在）：
- `qqAlls_succ : qqAlls p (k+1) = ^∀ (qqAlls p k)`——**归纳骨架**（照 9276 的 `shift_qqAlls`）
- `substs_all : subst L w (^∀ p) = ^∀ (subst L (qVec L w) p)`——每层下降
- `termSubstVec_qVec_qVec`——qVec 的嵌套律
- `cRel R` 是闭项（numeral）——`subst` 对其无作用（需证，见下）

**唯一待证的小件**：`subst w (cRel R) = cRel R`（闭项不受替换影响）。
Foundation **没有**现成的 subst-numeral 引理（本机实测确认），
需自证——但 `cRel R = ↑n` 是 numeral，路径应短。

**这是本会话留给下一会话的精确突破口**：一旦 `subst_cRel` 与 qVec 归纳完成，
`hAB` 的恒等式即成立，`hAll`/`hExs` 随之解锁。

## 二十八、撤回 §二十六 的"更正"（诚实记录，第三次修正）

**§二十六 说"qVec 保护内层绑定，hAB 有突破口"——这个更正本身是错的。** 逐项推理：

`iTR n 2 R v = qqAlls (imp (conjunct 2 n 0 (iVE n v.[0]) ⋏ …) (subst [#0,#1] (cRel R))) 2`

关键区分：**`v` 是项向量，不是公式**。
- **LHS** = `iT 0 (free p)` = `iTR 0 2 R (termSubstVec 2 ?[^&0] v)`
  → 替换作用在 **v 的元素（项）**上，`iVE 0` 随后把 `^&0` 变成 `eqAtom ^&0`。
- **RHS** = `free (iT 1 p)` = `subst ?[^&0] (shift (iTR 1 2 R v))`
  → 替换作用在 **iTR 内部公式的 bvar** 上（经 qVec，前缀恒等 `[#0,#1,…]`）。

**具体反例**：取 `v.[0] = ^#0`（bvar）。
- LHS：`termSubstVec` 把它换成 `^&0`，`iVE 0 ^&0 = eqAtom ^&0`
- RHS：`iVE 1 ^#0 = eqAtom ^#1`（bvar 加一），外层 qVec 前缀恒等 → 保持 `eqAtom ^#1`
- **`eqAtom ^&0 ≠ eqAtom ^#1`** ⟹ **恒等式为假**。

**结论**：§十三/§十五 的原判断（"必须走蕴含式"）**是对的**；
§二十六 的"更正"**应撤回**。这是本会话的第三次判断修正——
记录在此以免后续会话重复摇摆。

**教训**：`qVec` 保护的是**公式内层绑定**，但 hAB 的错位发生在
**项层替换 vs 公式层替换**——两者根本不同类。

## 二十九、hAB 的正确工具已找到（本会话最后的实质发现）

项目**自己**的模式（`Z0Full.lean:72-84`）证明 V 层可证性蕴含式的方法是：

```lean
complete 𝗜𝚺₁ _ fun (V : Type) _ _ ↦ by
  rw [Semantics.Imp.models_imply, ..., LogicalConnective.HomClass.map_imply]
  exact modus_ponens_sentence (T := 𝗭𝗙𝗖)
```

即：**先对任意 `V ⊨ 𝗜𝚺₁` 证语义蕴含，再由 `Arithmetic.complete` 提升**。

对 hAB 而言，A 与 B 都是 ℒₛₑₜ 闭公式（`A := iT 0 (free p)`、`B := free (imp domZero (iT 1 p))`），
它们**不是算术句**（在 ℒₒᵣ 上），所以要用 `SetTheory.complete`（ℒₛₑₜ 版）或
`Derivable` 层的对应物。

**但关键**：hAB 要的是 **`Derivable 𝗭𝗙𝗖 (insert (neg A ^⋎ B) ∅)`**（`Derivable` 层），
不是 `Provable`。`Derivable` 的语义完全性工具是 `Provable.complete`（ℕ 层）——
与 §3.2 的 V/ℕ 问题同源。

**所以 hAB 的正确路线是**：
1. 证语义蕴含 `V ⊨ A → V ⊨ B`（对任意 `V ⊨ 𝗭𝗙𝗖`）——这部分可能真的可做（A、B 语义等价）；
2. 用 ℒₛₑₜ 的完全性把语义蕴含转成 `Provable`；
3. 再用 `Provable` → `Derivable` 的桥（单元素 sequent）。

**这是本会话能给下一会话的最完整路线**，也是我第三次判断修正后的最终结论。

## 三十、hAB 的最简等价形式（本会话最终定位）

用 `free_imp_domZero`（9276 已证）展开 B：
```
B = imp ℒₛₑₜ (subst ?[^&0] domZero) (free ℒₛₑₜ (iT 1 p))
```
记 `C := free ℒₛₑₜ (iT 1 p)`、`G := subst ?[^&0] domZero`（即"自由变量 0 在 ω 中"）。则
```
B = (G → C)
A → B  ⟺  A → (G → C)  ⟺  (A ∧ G) → C
```
**若 `A ↔ C` 在 𝗭𝗙𝗖 中可证**，则 `A ∧ G → C` 由命题逻辑立得（`A ∧ G → A ↔ C`）。
**所以 hAB 完全归结为一条等价式**：
```
A ↔ C，即 iT 0 (free ℒₒᵣ p) ↔ free ℒₛₑₜ (iT 1 p)
```
用 `iT_shift` 展开：`C = subst ?[^&0] (iT 1 (shift p))`，
而 `A = iT 0 (subst ?[^&0] (shift p))`——**这就是 `iT_subst` 的 iff 形式**。

**与等式形式的区别**：等式形式（§十三）**恒假**（已机器证），
但 **iff 形式可能为真**——因为两式虽然不同码，**语义上都在说同一件事**
（"p 的自由变量 0 所指的对象满足 p"）。
这正是 9276 说的"算术蕴含式（Σ1 完全性范围）"的**最简形式**。

**下一会话的最短路线**：证 `iT 0 (subst ?[^&0] σ) ↔ subst ?[^&0] (iT 1 σ)`（iff，非等式），
`σ = shift p`。工具：`SetTheory.complete`（语义完全性）+ 语义计算。
