# CG-007 交接说明（第三轮）：Z0 缺口的 ← 方向已拆成可施工的第二层，地基已消掉一块

> **身份**：`TASK_HANDOFF / GOAL_LOCAL`。本文件是 CG-007 目标包内的一份工作交接，
> **不是**项目 current truth 的所有者；实时状态以 `形式化追踪/` 与各 `CLAIM.md` 为准。
>
> **写出者**：WorkBuddy 会话（Agent 模式），2026-10-10 16:00 – 2026-10-11 00:10（EDT），
> 工作根与主检出都是 `/Volumes/D/HoTT_AI_HANDOFF_20260911`（分支 **`dev`**）。
>
> **接力链**：Claude Opus `d58e0c0d`（停在 `zfcTr_D3_internalize`）
> → Codex `01a120e6` 第一轮（W4b–W9b，交接 `HANDOFF-TO-NEXT-SESSION.md`）
> → Codex `01a120e6` 第二轮（缺口重新定位 + 攻关包，交接 `HANDOFF-2026-10-10-Z0D3-SESSION-2.md`）
> → **WorkBuddy 会话（本文件，W9c 归位 + W8 第二层）** → 你
>
> **本轮用户指令**（按顺序）：① 核验并归位上一会话散落在旧基线 worktree 的成果；
> ② "完成全面的形式化和机器证明工作"；③ 选定攻 `keyE` 的 **← 方向**；④ 多轮 "继续"。

---

## 0. 一分钟版本

**`zfcTr_D3_internalize` 仍未证。** 本轮**没有**证出它，也没有证出它的直接前置。

本轮做成了三件事：

1. **把上一会话（Codex 第二轮）散落在旧基线 worktree `/Users/aurolafly/.codex/worktrees/9276`
   的成果安全归位到 `dev`**（那次搬运有一个真实回退陷阱，见 §5）。
2. **把 `keyE` 的 ← 方向拆成可施工的三层**，并逐条**实测排除**了四条"看似能省"的捷径（§4）。
3. **在第二层真的证出东西**：`SeqTranslateFormula.lean` 从 0 条增到 **9 条已证引理 + 2 条实例**
   （全部本机 exit 0、无 `sorry`），并找到两个此前没人踩到的**机制性关键**（§6）。

**最重要的两个机制发现**（都能复用，是本轮最大的可继承资产）：

> **(a)** `definability` 证不出 `fun v ↦ f b (v 78)` 这类**部分应用**，是因为 `f` 只登记了
> `𝚺ᴬ₁-Function₂`；**同时登记层级版 `Γᴬ_[m+1]-Function₂` 实例**即可（Foundation 自己的
> `disjSeqSubst` 就是这么做的）。补上后 3 秒通过。
>
> **(b)** `UformulaRec1.Construction.semiformula_result_induction` 的结论把**输出层 `param`**
> 与**输入层 `n`** **独立量化**；而 `iT` 改层（`iTR param …` 要求 `v` 在层 `param`），
> 所以归纳谓词必须带 `param = n` 护罩。

**影子形式不受影响**：C-120（`𝗭𝗙𝗜 ⊬ (Sh.craig.consistent)ᵗ`）已无条件成立，不依赖本缺口。

---

## 1. 你是谁、在哪

| 项 | 值 |
|---|---|
| 主检出（**所有 CG-007 工作在这里**） | `/Volumes/D/HoTT_AI_HANDOFF_20260911` |
| 分支 / HEAD | **`dev` @ `a62f9269`** |
| `origin/dev` | `87b65dfd` —— **dev 领先 12 个提交，本轮未 push** |
| 目标包 | `.claude/goals/CG-007-formalization-completion/` |
| Z0 形式包 | `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/` |
| 上一会话的旧 worktree | `/Users/aurolafly/.codex/worktrees/9276/HoTT_AI_HANDOFF_20260911`（detached HEAD @ `770272ae`，**已归位，别再动**） |

**先读**：`HANDOFF-TO-NEXT-SESSION.md`（第一轮）→ `HANDOFF-2026-10-10-Z0D3-SESSION-2.md`（第二轮）
→ 本文件。以及 `W8-下一单元-V内部语法解释定理-规格.md`（**施工规格，最重要**）
与 `W8-第二层进展-公式保持性地基.md`（本轮进展笔记）。

---

## 2. 目标与缺口（精确定位）

**目标**：Z0 完整形式，读作 `𝗭𝗙𝗜 ⊬ Con(𝗭𝗙𝗜)`。唯一缺口是 `zfcTr_D3_internalize`。

**为什么只剩一条句法等价**：2026-10-10 本机实测发现
`(Sh.craig.standardProvability).HBL3` 由 `inferInstance` **直接合成成功** ——
Foundation 已提供 `Sh.craig` 的完整 D3。正确入口是 `Sh.craig`（Craig 化），
不是 `Sh`（`Sh` 只可枚举不可判定）。缺口因此收缩为：

```lean
lemma keyE (σ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ zfcTr σ 🡘 provabilityPred Sh.craig σ
```

**两个方向不等难**（本轮实测修正了前几轮的判断）：

| 方向 | 内容 | 现状 |
|---|---|---|
| **→** | `zfcTr σ → provabilityPred Sh.craig σ` | 有路线（走 V 内部的 Δ1 机器：`Derivable.of_ss`、`provable_standardProvability_imp_of_Δ₁Class_subset`、`Theory.reWitness_spec`+`mem_craig_codes_iff`）。**仍未证。** |
| **←** | `provabilityPred Sh.craig σ → zfcTr σ` | **核心难点**。等价于一条 **V 内部的语法解释定理**（ℒₒᵣ → ℒₛₑₜ 的推导翻译）。**仍未证。** |

**← 方向的三层拆解**（规格 §3）：

1. **第 1 层：`arithTrln.translate` 的语法交换律** —— 本轮判定**基本不需要做**：
   连接词部分是 `LogicalConnective.Hom` 实例（免费），量词/原子部分是 Foundation 的 `rfl` 引理。
   **并行会话已把这一层收据化（CG001-C-388）**，见 §8。
   剩下的 `subst`/`shift`/`free`/`setShift`/`emb` 五项**未证**。
2. **第 2 层：V 内部的推导翻译** —— 不必显式构造"翻译推导"函数；用
   `Derivation.induction1`（`Proof/Basic.lean:642`）**按 10 条规则逐条消**，归纳谓词取
   `P d := Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`。**唯一用到 𝗭𝗙𝗖 的地方是 `axm` 支。**
3. **第 3 层：组装 + 出正式收据。**

---

## 3. 本轮（第三轮）实际做了什么

### 3.1 归位（提交 `dbebffe3`）

把上一会话（Codex 第二轮）散落在 `/Users/aurolafly/.codex/worktrees/9276`
（**detached HEAD @ `770272ae`，是 `dev` 的祖先**）的未提交成果搬到 `dev`。

**这一步有个真实陷阱，务必记住**：9276 的编辑**不是追加，是顶替同名章节**（因为它基线是旧提交）。
直接整体拷贝 `99-更新日志.md` / `05-分支上的形式包/README.md` / `CLAIM_EVIDENCE_MATRIX.md` /
`证据索引.md` 这四份，会**删掉 CG001-C-127 的整节**，并把 W9 的 run 号从 `-06`/`-NEG-02`
**回退**成 `-05`/`-NEG-01`。
**正确做法**：以 `dev` 为准，逐个 `diff` 出真正的增量，**逐字插入**。
（教训：**不要信 `git status` 的 "M"** —— 9276 那 16 个 "M" 里 5 个与 dev 完全相同、4 个是 dev 反而更新。）

搬运的 4 件（dev 完全没有）：`HoTT/formal/claude-cg001/external-foundation-incompleteness/`
（D09-C-369 重放包）+ 两条运行收据 `20261010-CG001-FFL-INCOMPLETENESS-R3-REPLAY-01`/`-NEG-01`
+ `HANDOFF-2026-10-10-Z0D3-SESSION-2.md`。三方合并 11 个治理文件。

**顺带确认**：dev-09 的 external-Foundation 重放**已完成**（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、
C-387 已进矩阵）。上一会话把这件事列为"待办"是**会话中途快照**，别重复劳动。

### 3.2 缺口第二次收窄（提交 `112ac597`）

实测：`Sh.reCh.val` 展开是 `mkSigma (codeOfREPred (Encodable.encode '' Sh))`，
`trProv.val` 是 `mkSigma (∃¹ iTDef/[#0,↑0,#1] ⋏ (provable 𝗭𝗙𝗖)/[#0])` ——
**内容相同但不是同一个公式**（`rfl` 失败）。后果：推导翻译的 `axm` 支要先补一条
**`codeOfREPred` 的一般 V 表示引理**（Foundation 的 `codeOfREPred_spec` 只在 ℕ 层）。

### 3.3 下一单元规格（提交 `3a48d133`）+ 第 1 层判定（`7ce21383`）+ `translateSeq`（`aa040872`）

见 §4、§5。

### 3.4 第二层真的证出东西（提交 `7d58b10e`、`10b2e73c`、`c43bdd66`、`a62f9269`）

`HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/SeqTranslateFormula.lean`
**9 条已证引理 + 2 条实例**，本机 exit 0、无 `sorry`：

| 引理 | 内容 |
|---|---|
| `isSemiformula_cRel` | `IsSemiformula ℒₛₑₜ 2 (cRel R)` |
| `isSemiformula_cDomN` | `IsSemiformula ℒₛₑₜ 1 (↑cDomN : V)` |
| `isSemiformula_cFunc_zero` | `IsSemiformula ℒₛₑₜ 1 (cFunc 0 0)` |
| `isSemiformula_cFunc_arity0` | `IsSemiformula ℒₛₑₜ 1 (cFunc 0 f)` |
| `isSemiformula_cFunc_arity2` | `k ≠ 0 → IsSemiformula ℒₛₑₜ 3 (cFunc k f)` |
| `isSemitermVec_shiftVec` | `IsSemitermVec ℒₛₑₜ (n:V) (b+n) (shiftVec b n)`（`n : ℕ`） |
| `isSemitermVec_single_bvar` | `i < n → IsSemitermVec ℒₛₑₜ 1 n ?[^#i]` |
| `isSemitermVec_shiftVec_V` | `∀ n : V, IsSemitermVec ℒₛₑₜ n (b+n) (shiftVec b n)` |
| `isSemiformula_conjunct` | `IsSemiformula ℒₛₑₜ (n+1) y → i < b+n → IsSemiformula ℒₛₑₜ (b+n) (conjunct b n i y)` |
| `shiftVec_definable` / `shiftVec_definable'` | `𝚺ᴬ₁-Function₂` / 层级版 `Γᴬ_[m+1]-Function₂` |

**负控制已做**：把 `isSemitermVec_shiftVec_V` 的结论改成 `shiftVec b (n+1)` 后内核拒绝（exit 1）。

---

## 4. 已排除的路（**别重复**）

### 4.1 第一轮交接列的（仍然有效）

1. `Sh.Δ₁` 取 `ch := trProv`：`ProperOn` 要求 `trProv ↔ ¬trProv`，假。
2. 给 `Provable 𝗭𝗙𝗜 x` 找有界形式 `∃ d < x`：对 `Sh` 这样的界不存在（否则 `Sh` 可判定）。
3. `provable_D3 (T := Sh)`：需 `Sh.Δ₁`，循环。正解是 `T := Sh.craig`。
4. `T := Sh.craig` 直接套 `provable_internalize`：理论不对，还要翻译回 ZFC，更难。
5. 把 `Provable 𝗭𝗙𝗜 ⌜σᵗ⌝ (V)` 当元层 `𝗭𝗙𝗜 ⊢ σᵗ` 用：只在 ℕ 层成立；非标准 V 下 `d` 可能非标准。

### 4.2 本轮新排除的（← 方向的四条捷径）

| 想省的办法 | 为什么省不掉（已读码确认） |
|---|---|
| 用 `DirectInterpretation.of_provability` 直接搬 | 它是**语义**证明（走 `Theory.Proof.complete_on_eq_models`），**不产生非标准 V 里的证明编码** |
| 用 `Derivable.of_ss`（V 内部弱化） | **只在同一语言内**（`Δ₁Class ⊆ Δ₁Class`），ℒₒᵣ → ℒₛₑₜ 跨不过去 |
| 用 `Derivation.sound` | **只对 `d : ℕ`（标准推导）**成立，V 内部的 `d` 可能非标准 |
| 走 `Diagonalization 𝗭𝗙𝗖` 岔路 | `Provability T₀ T` 要求 `T₀ ⪯ T` 是**同语言**关系，`𝗜𝚺₁ ⪯ 𝗭𝗙𝗖` 类型不过；且 Foundation 的 `provabilityPred` 是算术的（`Semisentence ℒₒᵣ 1`），拿不到集合论语言的可证性公式 |

**结论**：← 方向不是"再读一遍源码就能补上"的引理，是要单独立项的形式化工程；
但比前几轮判断的小得多（第 1 层基本免费，第 2 层已拆成 10 个 case + 4 条引理）。

---

## 5. 已完成的骨架与真产物

| 路径 | 状态 | 说明 |
|---|---|---|
| `GodelQ/ZFC/SeqTranslate.lean` | ✅ **已提交**（`aa040872`） | `translateSeq : V → V`（sequent 的翻译）。**做法照搬 `setShift`**：用 `sigma₁_replacement`，不是原先设想的"对 `s` 强递归"。含 `mem_translateSeq_iff`、`translateSeq_empty/insert/union/mono`，实例 `translateSeq.defined : 𝚺ᴬ₁-Function₁[V]` |
| `GodelQ/ZFC/SeqTranslateFormula.lean` | ✅ **已提交** | §3.4 的 9 引理 + 2 实例 |
| `/tmp/d3build/src/.../SeqTranslateDerivable.lean` | ⚠️ **只在 /tmp，未进包、未编译** | 第二层主定理的**骨架**：`derivable_translateSeq` 用 `Derivation.induction1` 逐条填 10 个 case，`axm` 支调 `derivable_translateSeq_of_axm`。**10 个 case 的 `Derivation.*` 构造子调用是占位/猜测，未验证**；`translateSeq_isFormulaSet`、`fstIdx_axL` 等辅助引理**不存在**。**它是一张施工图，不是可编译产物。** 下一位要把它先搬进包再逐条修 |

**别把它当既有成果**：`SeqTranslateDerivable.lean` 从未编译过。

---

## 6. 两个关键机制（本轮最大可继承资产）

### 6.1 `definability` 处理不了部分应用 → 补**层级实例**

失败形态（规格 §11.2 原记录的卡点）：

```
⊢ { Γ := 𝚺, rank := 1 }.DefinableFunction fun v => shiftVec b (v 78)
```

`aesop` 撞规则深度上限（`maxRuleApplicationDepth` 30 / 50）失败，**不是数学问题**。

**解法**（照抄 Foundation 的 `disjSeqSubst`，`Formula/Iteration.lean:211`）：

```lean
instance shiftVec_definable : 𝚺ᴬ₁-Function₂ (shiftVec : V → V → V) :=
  shiftVec_defined.to_definable
instance shiftVec_definable' (Γ m) : Γᴬ_[m + 1]-Function₂[V] shiftVec :=
  shiftVec_definable.of_sigmaOne
```

**`disjSeqSubst` 同时登记了 `𝚺ᴬ₁-Function₃` 与层级版 `Γᴬ_[m+1]-Function₃`**，
`definability` 才认得出部分应用。补上后 **3 秒通过**。
**这条对 `iVE`（`iVE_defined` 已有）、`iT`（`iT_definable` 已有）同样适用。**

### 6.2 主定理的归纳谓词必须带 `param = n` 护罩

`semiformula_result_induction`（`Formula/Basic.lean:1578`）的结论是

```lean
∀ {param n p : V}, IsSemiformula L n p → P param n p (c.result L param p)
```

`param`（**输出层**）与 `n`（**输入层**）**独立量化**。而 `iT` 的 `param` 就是输出层：
`iTR param k R v` 要求 `v` 在层 `param`，但 `hRel` 只给 `IsSemitermVec ℒₒᵣ k n v`（层 `n`）。
`param ≠ n` 时**证不出来**。

**出路**：

```lean
P param n p q := param = n → IsSemiformula ℒₛₑₜ param q
```

结论实例化 `param := n` 即得目标；`hRel` 支由 `param = n` 把 `v` 的层搬过去；
`hall` 支的递归是 `P (param+1) (n+1) p …`，护罩自动保持。
**对照**：Foundation 自己的 `semiformula_subst_induction`（`Formula/Functions.lean:523`）
**不需要**护罩，因为 `subst` 不改层；`iT` 改层所以要。

### 6.3 其它实测到的小机制

- **`ISigma1.sigma1_succ_induction` 名义上要 `𝗜𝚺⁺₁`，但现有 `[V ⊧ 𝗜𝚺₁]` 就够**：
  `ISigma_equiv_IBroadSigma 1 : 𝗜𝚺 1 ≊ 𝗜𝚺⁺ 1`（`Induction/Equiv.lean:232`，`Examples.lean:29` 有实例）。
- **`Sentence.coe_quote_eq_quote (σ : Semisentence L n) : (↑(⌜σ⌝ : ℕ) : V) = ⌜σ⌝`**
  （`Formula/Coding.lean:440`）：`cRelN`/`cDomN`/`cFuncN` 全是 **ℕ 层**引号，
  而 `Sentence.quote_isSemiformula` 说的是 **V 层**引号，差一个 `↑`。**每条公式性引理都要先 `rw` 它。**
- **`Semiformula.quote_isSemiformula` 只收 `Semiproposition`**，要用 `Sentence.quote_isSemiformula`。
- **`simp only [cFunc, cFuncN, reduceIte]` 约化 `0 = 0` 但 `不` 约化 `1 = 0` / `2 = 0`**：
  后者要显式 `split`，把不可能支用 `absurd h (by decide)` 关掉。
- **`if_neg` 已弃用**（用 `ite_eq_right`）。
- 项侧**没有**带层数的 TermRec 归纳；要用 **`IsSemiterm.sigma1_induction`**
  （`Term/Basic.lean:936`）：`{P : V → Prop} → 𝚺ᴬ₁-Predicate P → (∀ z < n, P ^#z) → (∀ x, P ^&x) → (∀ k f v, …) → ∀ t, IsSemiterm L n t → P t`。
- **规则集**：V 内部推导只有 **10 条规则**（`blueprint`，`Proof/Basic.lean:412`，全 Σ0）：
  `axL`/`verumIntro`/`andIntro`/`orIntro`/`allIntro`/`exsIntro`/`wk`/`shift`/`cut`/`axm`。
  `Derivation.induction1`（`Proof/Basic.lean:642`）**已把 10 条支逐条列成假设**。
- **sequent 的表示**：`Sequent.quote Γ = ∑ φ ∈ Γ, Exp.exp ⌜φ⌝`（`Coding.lean:24`），不是树。
  但 `sigma₁_replacement` 让它可做（见 `setShift`）。
- **层数已算准**：`iVE n t` 层 `n+1`；`ve2 n k f w` 层 `n+1`（不是 `n`）；
  `iTR n k R v` 层 `n`（`conjunct 2 n i _` 层 `n+2` 正好是 `qqAlls … 2` 的体内层）；
  `conjunct b n i y` 层 `b+n`；`shiftVec b n` 层 `b+n`、长度 `n`。

---

## 7. 你下一步（按顺序，可执行）

### A. 第二层（← 方向）——**这是当前唯一的数学推进路**

规格 `W8-下一单元-V内部语法解释定理-规格.md` §9.3 与进展笔记 §3 列了精确清单，
按依赖顺序：

| # | 缺的引理 | 状态 / 入口 |
|---|---|---|
| 1 | **`iVE` 的三条计算规则**：`iVE n (^#z) = eqAtom (^#(z+1))`、`iVE n (^&x) = eqAtom (^&x)`、`iVE n (^func k f v) = (if k = 0 then ve0 k f else ve2 n k f w)` | ❌ **没有**。`InternalTranslate.lean` 里只有 `iVE_defined`（可定义性），无化简。要从 `iVE.construction.result` 的 fixpoint 语义里抠。**这是下一个可独立验收的单点。** |
| 2 | `isSemiformula_iVE`：`IsSemiterm ℒₒᵣ n t → IsSemiformula ℒₛₑₜ (n+1) (iVE n t)` | ❌。用 `IsSemiterm.sigma1_induction` + `P t := IsSemiformula ℒₛₑₜ (n+1) (iVE n t)`；`definability` 义务需补 `iVE` 的层级实例（§6.1） |
| 3 | `isSemiformula_domZero`：`IsSemiformula ℒₛₑₜ (n+1) domZero` | ❌。`isSemiformula_cDomN` ✅ + `IsSemiformula.subst` |
| 4 | `isSemiformula_iTR`：`IsRel k R → IsSemitermVec ℒₒᵣ k n v → IsSemiformula ℒₛₑₜ n (iTR n k R v)` | ❌。依赖 #2、#3 + `isSemiformula_conjunct` ✅ + `isSemiformula_cRel` ✅ + `IsSemiformula.qqAlls` |
| 5 | **公式保持性主定理**：`IsSemiformula ℒₒᵣ n p → IsSemiformula ℒₛₑₜ n (iT n p)` | ❌。`semiformula_result_induction` + §6.2 的护罩；`all`/`exs` 支用 #3；`rel`/`nrel` 支用 #4 |
| 6 | `iT` 与 `substs1`/`shift`/`free` 的相容 | ❌ **还没核**。`axL`/`cut`/`all`/`shift` 支要用。注意翻译每个量词多引入一个约束变量，de Bruijn 结构变了，**不是平凡交换** |
| 7 | `axm` 支 | ❌ 唯一用到 𝗭𝗙𝗖 的地方。需要 **`codeOfREPred` 的一般 V 表示引理**（`codeOfREPred_spec` 只在 ℕ 层）；拿到后由 `mem_craig_codes_iff` + `reWitness_spec` 得 `zfcTr ρ` |
| 8 | `derivable_translateSeq` 的 10 个 case 组装 | 骨架在 §5（未编译）。先搬进包，再逐条修 |
| 9 | `bridge` / `keyE` 的 ← / `zfcTr_D3_internalize` | ❌ |
| 10 | 正式收据 | 用包内 `tools/capture_run.py`（带沙箱），**拒 `sorry`** |

**建议的开工顺序**：#1 → #2 → #3 → #4 → #5（一过就能看到进度条），然后 #6/#7 是真正的难点。

**→ 方向**（有路线、工作量可控）可作为并行支线：见 §2 表。

### B. 把 `keyE` 的 **→ 方向**先做出来并收据化

§2 表里三件 V 内部工具（`Derivable.of_ss`、`provable_standardProvability_imp_of_Δ₁Class_subset`、
`Theory.reWitness_spec`+`mem_craig_codes_iff`）。单向比 Iff 容易得多。

### C. 归位并行会话的未提交工作（**需要用户裁定**）

见 §8。**我没有动它**，因为它是独立工作流。

### D. W9 收尾（**需研究发起人授权**）

终局报告 §12 已补；剩四种 CLAIMS 译文、`main` 由 `scripts/release/build_main_release.py`
从 dev 生成（父提交 `f3127701`）、推送回读。**main 推送与发布没有授权。**

---

## 8. ⚠️ 并行会话的未提交工作（**待用户裁定**）

2026-10-10 **18:11–19:42**（我最后一轮提交 `281ee5b4` 之后），**另一个会话**
（日志自称 "Codex 会话" / "Claude CG-007 W8-L1"）在主检出里做了一批**全部未提交**的工作。
2026-10-11 00:10 核验时无 `codex`/`claude`/`lean` 进程在跑。

**它产出的文件**（`git status` 的 `??`）：

| 路径 | 内容 |
|---|---|
| `GodelQ/ZFC/Z0Layer1.lean` | **7 条外层 `arithTrln.translate` 交换律**（`map_and/or/neg/all/exs/rel/nrel`），全部是 `HomClass` 实例投影或 `rfl`。**不是新数学** |
| `GodelQ/ZFC/WrongZ0Layer1Overclaim.lean` | 负控制：用第 1 层推 D3 被内核**类型不匹配**拒绝 |
| `GodelQ/ZFC/Z0Layer1Emb.lean` | `emb_term`/`emb_vec` 已证；`emb_id` 的 8 例中 6 例已证，**`all`/`exs` 两例带 `sorry`** |
| `CLAIM-Z0-LAYER1.md` | 命题全文（`MP-CG001-Z0-LAYER1-TRANSLATE-COMMUTATION-001`） |
| `HoTT/verification/runs/20261010-CG001-Z0-LAYER1-TRANSLATE-COMMUTATION-01/` | 收据：exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` |
| `...-NEG-01/` | 收据：exit 1，`KERNEL_REJECTED`，`outcome_matches_expectation = true` |

**我对两条收据做了核验**（读 `RUN.json` + `stdout.txt`）：**自洽**，与它自己的声明一致。

**它对 6 个治理文件的追加**（`git status` 的 `M`）：
`HoTT/CLAIM_EVIDENCE_MATRIX.md`、`.claude/goals/CG-001-targeted-overview/证据索引.md`、
`形式化追踪/99-更新日志.md`、`形式化追踪/01-有哥德尔路线/02-Z0-条件形式与剩余三步.md`、
`.claude/goals/CG-007-formalization-completion/HANDOFF-2026-10-10-Z0D3-SESSION-2.md`、
`.claude/goals/CG-007-formalization-completion/W8-下一单元-V内部语法解释定理-规格.md`。
**全是纯追加（+19 / +36 / +1 / +32 / +41 / +51 行），不回退任何既有内容。**

### 归位时必须先修的一处缺陷

`证据索引.md` 里它新加的节号写成 **`## 38.`**，而 **§38 已被**"Z0 的 D3 收成一条内部解释"
（W8 续，2026-10-09）**占用**；它又补了个 `## 38b.`。
归位时要改成 **§40 / §41**（§39 是本轮归位的 W9c）。

### 它与本轮工作的关系

**互补、不重叠**：它做**外层** `arithTrln.translate`（Lean 层公式的翻译），
本轮做**内部化** `iT`（V 内公式码的翻译）。两者的结论一致：
第 1 层的连接词/量词部分**不是新数学**，是 Foundation 现成件。

**用户此前对同类情形的选择是"先归位记录"**（`AskUserQuestion`，2026-10-10），
故建议：**把它归位成一个独立提交（含 §38→§40 的编号修正），与我的提交分开**。
但这是**独立工作流**，我不擅自动手。

### 另：`外部资料/` 下有大量未跟踪内容

`Z0-D3-攻关包-最小完整版/`（+ zip）、`Z0-D3-Foundation全量源码/`、
`Z0-D3-补充包/`、`Z0-D3-补充包二-全量源码与缺口骨架/`、`zfcTr-D3-plan.md` /
`zfcTr-D3-plan-revision.md` 等。**这是用户的目录，别动、别提交、别清理。**

---

## 9. 环境（**完整可用，别信"90% 环境 / OOM"的历史描述**）

| 项 | 值 |
|---|---|
| Lean | **4.34.0** @ `/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0` |
| Foundation 源码 | `/Volumes/D/HoTT-toolchain-cache/foundation-src`（commit **`1fb01b72`**） |
| Foundation 构建树 | `/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0` |
| **olean 在哪** | **`…/foundation-build-1fb01b72-v4.34.0/lib/lean/`** —— ⚠️ **不是** 交接文档曾写的 `.lake/build/lib/lean`（那个路径不存在） |
| Mathlib | `/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-*` |
| 编译回路（**开发用**） | `/tmp/d3build/devbuild_ns.py` + 工作副本 `/tmp/d3build/src/godel-q-zfc-z0-full` |
| 正式收据 | 包内 `.claude/goals/CG-007-formalization-completion/tools/capture_run.py`（**带沙箱**，拒 `sorry`） |

**编译命令**（开发迭代）：

```bash
cd /tmp/d3build && python3 -B devbuild_ns.py /tmp/d3build/src/godel-q-zfc-z0-full <模块路径…>
```

全链 24 模块冷启动约 60 秒，增量几乎瞬时。改完文件先 `cp` 到 `/tmp/d3build/src/...` 再编译。

**为什么有 `devbuild_ns.py`**：当前宿主**不允许嵌套沙箱**，`devbuild.py` 用的 `sandbox-exec`
直接失败。`devbuild_ns.py` 是去掉沙箱包装的等价驱动，**只用于开发迭代**；
正式收据仍必须用 `capture_run.py`。

---

## 10. 陷阱（本轮及前几轮踩过的）

1. **别信旧 worktree 的 `git status`**：基线是旧提交时，`M` 文件里可能既有"其实没变"的，
   也有"dev 反而更新"的。必须逐个 `diff`（§3.1）。
2. **`omega` 在 `V`（`ORingStructure V`）上不工作**。要算术不等式用 Foundation 自己的
   `lt_add_self_add_one (a b : V) : a < b + a + 1`（`PeanoMinus.lean:14`）。`ring` 倒能用。
3. **`↑(n+1) : V` 的层级转换要 `push_cast`**；`(b+n)+1` vs `b+(n+1)` 要 `add_assoc`。
4. **`Jeroslow.lean` 不在本地构建树的导入闭包里**，要用得先补编译。
5. **模块文档注释必须在 `import` 之后**。
6. **`noncomputable` 传染**：`(Sh.craig).Δ₁` 非计算，用它的 `example` 要标 `noncomputable`；
   `theorem` 不能标。
7. **收据工具拒 `sorry`**：带未证标记的文件不能进收据源清单（`verify_cg001_run.py` 硬禁）。
8. **`attribute [irreducible]`**：`InternalTranslate.lean:212` 把 `shiftVecDef`/`cFuncDef`/
   `conjunctDef`/`iVEDef`/`iTRDef` 等标了 `irreducible`；`definability` 靠实例而不是展开它们。
9. **主检出有用户未提交的 `外部资料/`，别动。**

---

## 11. 授权与边界（**未变**）

- **有效**：2026-10-07 / 10-08 / 10-09 三段全面授权（见 `HANDOFF-TO-NEXT-SESSION.md` §6）。
- **没有授权**：`main` 推送与发布、tag、Sub Agent、**碰他人未提交文件**、
  改 `sources/` 与 `private-audit/`。
- 本轮**未 push 任何东西**；`origin/dev` 仍在 `87b65dfd`。

---

## 12. 我的主观判断（**供校验，不是结论**）

1. **缺口比第一轮判断的小得多，但比我上一轮的乐观要保守。**
   第 1 层基本免费（已由并行会话收据化）；第 2 层已拆成"4 条引理 + 10 个 case"，
   本轮把其中 9 条地基引理证掉了。**剩下的不是"再读源码就能补"的**：
   `iVE` 的计算规则要从 fixpoint 语义里抠，`axm` 支要一条一般 V 表示引理，
   `iT` 与 `subst/shift/free` 的相容因为 de Bruijn 结构改变而**不是平凡交换**。
2. **但也不是几周。** 按本轮的速度（每轮 2–4 条引理、3 秒编译），
   第 2 层的 4 条引理（#1–#4）是**可预期**的，`#5` 主定理在护罩解决后应该能一次成型。
   真正的未知量是 **#6 和 #7**。
3. **别把 `SeqTranslateDerivable.lean` 当成果**：它没编译过，10 个 case 是施工图。
4. **若第二层也卡住：诚实收尾。** 把精确的 Lean 命题写回 `Z0Blocked.lean` /
   在 `CLAIM.md` §4 说明它为什么是实的缺口，**别为了"完成"收窄命题**。
   父目标不受影响 —— C-120 的影子形式已无条件成立。
5. **并行会话的结论与本轮一致**（第 1 层不是新数学）。它做外层、本轮做内层，
   建议归位时**保持两条线的提交分开**，便于将来追溯。

---

## 13. 本轮提交清单（`dev`，**均未 push**）

| 提交 | 内容 |
|---|---|
| `dbebffe3` | W9c 归位：把 Codex 第二轮散落在 9276 的成果三方合并进 `dev`（32 文件，+20338/−12） |
| `112ac597` | 缺口第二次收窄：`keyE` 两方向不等难 + 三件 V 内部工具 |
| `3a48d133` | 下一单元规格（`W8-下一单元-V内部语法解释定理-规格.md`） |
| `7ce21383` | 第 1 层判定：`arithTrln.translate` 的连接词交换律由 `→ˡᶜ` 免费，内部化版 `iT` 已有 |
| `aa040872` | `translateSeq`（`SeqTranslate.lean`，exit 0、无 `sorry`） |
| `9ec48a49` / `65ae288a` | 公式保持性的拆解与复核（一条 → 约 6 条 → 实为 3 条） |
| `7d58b10e` | 三条公式性引理（`cRel`/`cDomN`/`cFunc 0 0`） |
| `10b2e73c` | 两条向量引理（`shiftVec` 的 `n : ℕ` 版、单元素 bvar 向量） |
| `281ee5b4` | §11.2：`n : V` 升级的卡点（**已被 `c43bdd66` 关掉**） |
| `c43bdd66` | **`isSemitermVec_shiftVec_V` + `isSemiformula_conjunct` + 层级实例**（§6.1） |
| `a62f9269` | **`cFunc` 四例补齐**（`arity0`/`arity2`） |

**未证**：`derivable_translateSeq`、`bridge`、`keyE`（两个方向）、`zfcTr_D3_internalize`。
**C-120 的影子形式无条件成立，不受影响。**
