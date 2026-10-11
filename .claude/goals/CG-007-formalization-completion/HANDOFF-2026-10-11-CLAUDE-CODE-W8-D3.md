# HANDOFF — CG-007 W8（Z0 D3）· Claude Code 会话实测交接（2026-10-11，worktree 版）

> 判定标准只有一条：**对应 `.lean` 能被 `devbuild_ns.py` 编译（exit 0、无 `sorry`）且最好有
> `HoTT/verification/runs/<id>/` 正式收据才算数**。本文件全部结论来自本机 Lean 4.34.0 实编译，
> 不来自任何对话摘要。与本文冲突的旧摘要（`STATE.json`、`HANDOFF-*`、`形式化追踪/08-*`）一律以本文为准。
>
> **前一版交接**：`HANDOFF-2026-10-11-CODEX-W8-D3.md`（Codex 会话，记录阶段 A 修法）。
> 本文是**它之后的实测续接**：那条"当前拦路石"`iT_neg` 已被证出，并连带推进了归纳接线。

---

## 0. 工作目录（全 PATH，先校准再动手）

### 0.1 开发工作根（**写这里**）

```text
/Volumes/D/HoTT-worktrees/cg007-w8-d3
```

- 分支：`codex/cg007-w8-d3`，从 `dev @ fb073d5c` 建立。
- 当前 HEAD：`c7ffb629`（动手前先 `git log --oneline -1` 复核）。
- `git rev-parse --show-toplevel` 应返回上面这个路径；不是就先停下来核对。
- **开工第一条命令**（只读，约 1 秒）：

```bash
cd /Volumes/D/HoTT-worktrees/cg007-w8-d3
python3 -B .claude/goals/CG-007-formalization-completion/tools/selfcheck_worktree.py
# 期望最后一行：结果：全部就绪，可以在本 worktree 独立开工。
```

### 0.2 集成目标（**保持干净，日常不要写**）

```text
/Volumes/D/HoTT_AI_HANDOFF_20260911
```

- 分支 `dev`，HEAD `2e06293b`。候选通过验收并经研究发起人授权后才按精确路径回写。

### 0.3 禁止写入

```text
/Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911/dev-f65ca154
```

- 停在 `workbuddy/dev-f65ca154 @ 87b65dfd`（实测**是 `dev` 的祖先**，落后 47 个提交），
  缺 `SeqTranslateFormula.lean`、`NegInvolution.lean`、`ShCraigElimNegLaw.lean` 三个 W8 文件。
- 另外不要碰：`外部资料/`、`Z0-D3-攻关包-最小完整版/`、`sources/`、`private-audit/`。
- 不 push / 不 tag / 不 publish（**除非研究发起人明确授权**——本次授权了推送，见 §7）。

---

## 1. 一分钟状态（2026-10-11 实编译核实）

**本会话（Claude Code）的成果：3 条正式收据 + 4 组开发引理 + 6 项判定。**

### 1.1 三条正式收据（各走完 F-011 五件事，`--rerun` 全部 `PASS_WITH_SCOPE`）

| Claim | 内容 | run |
|---|---|---|
| **CG001-C-398** | `ShCraigElimNegLaw.iT_neg`——一般（V 内任意公式码）的 `iT`/`neg` 相容律，**九支全证** | `20261011-CG001-Z0-W8-ITNEG-01` |
| **CG001-C-400** | `ShCraigElimBranches.lean` 归纳**七支**（`isFormulaSet_translateSeq`/`hWk`/`hVerumIntro`/`hAxL`/`hAnd`/`hOr`/`hCut`） | `20261011-CG001-Z0-W8-BRANCHES-02` |
| **CG001-C-401** | `NegInvolution.neg_neg_code` 码层对合律 | `20261011-CG001-Z0-NEGINVOL-CODE-01` |

**C-398 是本会话最重要的成果**：它是前一版交接标记的"当前拦路石"，九支全证后 `hAxL`/`hCut` 立刻接上了。

### 1.2 四组开发引理（探针文件，未出收据）

| 文件 | 内容 | 状态 |
|---|---|---|
| `ProbeITVE.lean` | `iVE`-`shift` 相容律的地基：`shift_eqAtom_bvar`、`shift_eqAtom_fvar` | exit 0 |
| `ProbeHAxm.lean` | `axm` 支三块：`zfc_provable_of_mem_craig`、`iT_of_mem_delta1`、`derivable_of_provable_mem` | exit 0 |
| `ProbeHAxm2.lean` | `axm` 支第四块：`isCraigAxiom_of_mem_delta1` | exit 0 |
| `ShCraigElimInduction.lean` | **正式文件**：用 `Q` 重开归纳，**六支已接线**（10 个 `sorry` → 4 个） | exit 0，带 4 个 sorry |

### 1.3 六项判定（含**两次推翻自己的错误判定**）

1. `NegInvolution.neg_neg_code` 实为 exit 0（推翻"未编译"记载）→ 已出收据 C-401
2. `ShCraigElimNegLaw.iT_neg` 的真因是 `all`/`exs` 两支 `rw` 形状不匹配（非"`qqAlls` 命名不存在"）→ 已修，C-398
3. `hShift` 的 `ofSetEq` 绕行**不成立**——展开后剩余目标正是相容律本身
4. `axm` 支**不需要** V 层 `codeOfREPred`（推翻早先判定）——`Sh.craig ⪯ Sh` 那条路够用
5. `iVE`-`shift` 相容律的 func 支**障碍确证**：`cFunc` 不是 `shift`-不变
6. `axm` 支最后一环需 V 层 `reWitness` 见证的引号化（早先判定的残余部分）

---

## 2. 唯一实质缺口与当前进展

`zfcTr_D3_internalize`（`GodelQ/ZFC/Z0Blocked.lean:29`，带 `sorry`）仍是 Z0 完整形式
`𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)ᵗ` 的唯一实质缺口。C-120 影子形式不受影响。

经 C-390 `bwd_of_shcraig_elim` 归约为一条消去 `ShCraigElim`。
`ShCraigElim` 的归纳有 10 个支，**现状：6 支已接线、4 支待补**。

### 2.1 已接线（`ShCraigElimInduction.lean`）

| 支 | 用的引理 | 依赖 |
|---|---|---|
| `axL` | `hAxL` | **`iT_neg`（C-398）** |
| `verumIntro` | `hVerumIntro` | `iT_verum` |
| `andIntro` | `hAnd` | `translateSeq_insert` + `iT_and` |
| `orIntro` | `hOr` | 同上 + `iT_or` |
| `wkRule` | `hWk` | `Derivable.wk` + `translateSeq_mono` |
| `cutRule` | `hCut` | **`iT_neg`（C-398）** |

**为什么用 `Q` 而不是 `P`**：`Q d := Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`，
`P d := Provable 𝗭𝗙𝗖 (...)`。`Derivable.wk`/`and_m`/`or_m`/`cut`/`em` 都是 `Derivable` 侧的规则，
`Q` 版可直接接；`P` 版要在每支里做 `Provable ↔ Derivable` 转换。
`ShCraigElimPredicate.lean` 的注释早已指出，本会话落实了。`q_defined` 已证 `Q` 是 Σ1 谓词。

### 2.2 待补四支

| 支 | 缺什么 | 难度 |
|---|---|---|
| `allIntro` | `iT` 与 `setShift` 的相容律 | 大 |
| `shiftRule` | 同上 | 大 |
| `exsIntro` | `iT` 与 `substs1` 的相容律 | 大 |
| `axm` | 四块已证；最后一环需把 V 层 `reWitness` 见证认成引号化 | 中 |

---

## 3. 待补四支的精确缺口（本会话判定，避免重走死路）

### 3.1 `allIntro` / `shiftRule`：`iT`-`setShift` 相容律

**已证的地基**（`ProbeITVE.lean`，exit 0）：

```lean
shift_eqAtom_bvar : shift ℒₛₑₜ (eqAtom ^#z) = eqAtom ^#z
shift_eqAtom_fvar : shift ℒₛₑₜ (eqAtom ^&x) = eqAtom ^&(x+1)
```

这两条正好是相容律 bvar/fvar 两支所需的全部内容
（`iVE` 的 bvar 支产出 `eqAtom ^#(z+1)`、fvar 支产出 `eqAtom ^&x`；
`termShift` 在 `ℒₒᵣ` 侧把 `^&x ↦ ^&(x+1)`）。

**func 支的障碍**（三条路径全部实测排除）：

- `Semisentence` 版 `quote_shift`——Foundation **没有**（`Rewriting.shift` 对 `Semisentence` 无实例）
- `shift_substs` 绕行——展开后仍归到 `subst ?[^#0] (shift (cFunc k f)) = subst ?[^#0] (cFunc k f)`，
  还是需要那条引理
- `simp` 自动——无进展

**根因**：`cFunc k f` 是 `Semisentence ℒₛₑₜ 1` 的引号化（层数 1、含自由变量），
而 Foundation 的 `shift_quote`（`Coding.lean:466`）**只对 `ArithmeticSentence`**（层数 0、无自由变量）
成立，且只在 `ℒₒᵣ` 上。

**已有的零件**（`SeqTranslateFormula.lean`，不必重造）：
`isSemiformula_cFunc_zero`（层 1）、`isSemiformula_cFunc_arity0`（层 1，任意 f）、
`isSemiformula_cFunc_arity2`（层 3，`k ≠ 0`）。

**注意语言**：`iVE` 把 `ℒₒᵣ` 项翻译成 `ℒₛₑₜ` 公式，两侧 `shift` 的 bvar 语义不同——
这是本律比 `iT_neg` 难的原因。

### 3.2 `exsIntro`：`iT`-`substs1` 相容律

同 3.1 量级。`free p = substs1 ^&0 (shift p)`（`Functions.lean:826`）。

### 3.3 `axm`：四块已证，最后一环待补

**已证四块**：

| # | 引理 | 位置 |
|---|---|---|
| 1 | `σ ∈ Sh.craig ⟹ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ` | `ProbeHAxm.lean` |
| 2 | `⌜φ⌝ ∈ Sh.craig.Δ₁Class ⟹ ∃ σ ∈ Sh.craig, iT 0 ⌜φ⌝ = ⌜translate σ⌝` | `ProbeHAxm.lean` |
| 3 | `IsFormulaSet ℒₛₑₜ s → φ ∈ s → Provable 𝗭𝗙𝗖 φ → Derivable 𝗭𝗙𝗖 s` | `ProbeHAxm.lean` |
| 4 | `p ∈ Sh.craig.Δ₁Class ⟹ Sh.IsCraigAxiom p` | `ProbeHAxm2.lean` |

**路线一的三步**（1 的来源）：`Sh.craig ⪯ Sh`（Foundation `CraigTrick.lean:321` **已有实例**）
→ `Sh_provable_iff`（`Z0Shadow.lean:45`）→ `Entailment.by_axm`。
**不需要 V 层 `codeOfREPred`**——这推翻了早先判定。

**最后一环**：从 `Sh.IsCraigAxiom p`（即 `∃ s q, p = q ^⋏ qqVerums s ∧ V ⊧/![s,q] Sh.reWitness.val`）
得 `∃ σ k, p = ⌜σ⌝ ^⋏ qqVerums k`——**即需证 `q` 是引号化**。
`reWitness` 是 `reCh` 的存在量化展开（`reWitness_spec`），而 `reCh` 的语义
（`rePred_codes_of_RE` + `codeOfREPred_spec`）只在 **ℕ 层**刻画 `q` 是编码。

**关键引理**（Foundation）：`Δ₁Class.mem_iff_s`，**全限定名**
`FFL.FirstOrder.Arithmetic.Bootstrapping.Δ₁Class.mem_iff_s`，结论是
`⌜φ⌝ ∈ T.Δ₁Class ↔ ∃ σ ∈ T, φ = Rewriting.emb σ`。用 `.mp` **显式应用**
（`rw` 的模式匹配会失败）。配 `Rewriting.emb_injective` 化到 `φ = σ`。

---

## 4. 环境与工具链

| 项 | 路径 / 值 |
|---|---|
| Lean | 4.34.0 @ `/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0` |
| Foundation 源码 | `/Volumes/D/HoTT-toolchain-cache/foundation-src`（commit `1fb01b72`） |
| Foundation 构建树 | `/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0` |
| 开发编译回路 | `.claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py`（无沙箱，仅开发） |
| 正式收据 | `.claude/goals/CG-007-formalization-completion/tools/capture_run.py`（带沙箱、拒 sorry） |
| **自检** | `.claude/goals/CG-007-formalization-completion/tools/selfcheck_worktree.py`（只读，开工前先跑） |

### 4.1 收据回路的两个实测坑（本会话踩过）

1. **`--source` 是 `action="append"`**：**每个文件一个 `--source`**，不能空格分隔成一条。
2. **必须给完整依赖链**：`capture_run.py` 的驱动在**全新临时目录**从零编译，
   只给目标文件会报 `object file '...SeqFormula.olean' ... does not exist` → `KERNEL_REJECTED`。
   本包约 26–29 个文件，照抄上一份成功收据的 `RUN.json` 的 `command_argv[5:]` 最稳。

### 4.2 `devbuild_ns.py` 的缓存假命中

`## skip` **只说明哈希没变，不说明现在编得过**。要验某文件真能编译，先删
`devbuild_ns/godel-q-zfc-z0-full/_state.json` 里该条目再跑。本会话用此法推翻了
两条假断言（`neg_neg_code` 实为 exit 0；`iT_neg` 真因不是 `qqAlls`）。

### 4.3 命名冲突（本会话踩过）

`ShCraigElimSetup` 与 `ShCraigElimPredicate` **都定义 `pDef`**，同时 import 会报
`environment already contains 'GodelQ.ShCraigElimSetup.pDef'`——只能二选一。

### 4.4 其它陷阱（沿用前一版交接）

- `omega` 在 V（`ORingStructure V`）上**不工作**；算术不等式用 `lt_add_self_add_one`；`ring` 可用。
- `IsUFormula`/`IsSemiformula` 假设里的 `domZero` 必须标 `(domZero : V)`，否则 universe 不匹配。
- `InternalTranslate.lean` 把 `shiftVecDef`/`cFuncDef`/`conjunctDef`/`iVEDef`/`cRelDef`/`iTRDef`
  标了 `irreducible`；definability 靠**实例**。
- `iT_quote` 的模式是 `iT ↑n ⌜φ⌝`（`↑n` 是 `ℕ → V` 强制转换）；目标是 `iT 0` 时需
  `rw [show (0 : V) = ((0 : ℕ) : V) by simp, iT_quote]`。
- `neg_rel`/`neg_nrel` 要 `IsUTermVec`（不是 `IsSemitermVec`）。
- `neg_verum`/`neg_falsum` **无参数**（`[simp]` 引理）。
- `IsUFormula.imp`/`.and`/`.or` 是 **↔ 形式**，不是构造函数——用 `.mp`/`.2`。

---

## 5. 正式收据流程（F-011 五件事，缺一不可）

1. 命题的类型逐字落在包的 `.lean` 源里；
2. 主运行 + 至少一个负控制，用 `capture_run.py` 抓成 `HoTT/verification/runs/<run-id>/`；
3. `verify_cg001_run.py --rerun` 精确重放一致。**必须先在 CG-001 证据索引
   `.claude/goals/CG-001-targeted-overview/证据索引.md` 里写好三张表的行**
   （proof 表、run 表、claim 表），否则校验器报 `GOAL_INDEX_ROW_COUNT`；
4. `HoTT/CLAIM_EVIDENCE_MATRIX.md` 追加一节（Package 表 + Claim 表）；
5. 更新 `形式化追踪/`：该线 README 状态表与"下一步"、总览对应行、`99-更新日志.md` 追加一行；
   并按精确路径 `git add` 提交（**不要** `git add -A`）。

---

## 6. 本会话的治理动作（已提交）

- **工作根越界根源修复**：会话按 `AGENTS.md` 启动闭包第 1 步读 `rulings.md`/`feature-list.md`/
  `MEMORY/001`，而这三处（源自 `rulings.md` §22，2026-09-14）都写着
  "main 是唯一 active write root"——按它执行就会往主检出动工。**这是"总是越出工作树"的机制**。
  已按该文件自身先例加 CG-007 例外注记（未改写原文）。
- **自检脚本**：`selfcheck_worktree.py`（只读，一条命令确认工作根/闭包/工具链/缺口源码就位）。
- **goal-x 开工闭包**：补入 `CLAUDE.md` 第〇节与本轮交接，加工作根警示。
- **总索引 002 的"下一步"**：按清缓存重编译结果校正。

---

## 7. 推送与授权

**本会话经研究发起人明确授权推送**（原话："推送远程"）。推送范围：
`codex/cg007-w8-d3` → `origin`（`https://github.com/math-fournity/HoTT-Paradoxy.git`）。

**未授权**：tag、release、`main` 发布、回写 `dev`。

---

## 8. 给下一步接手会话的提示词（直接复制）

```text
你是接手 CG-007 目标包 W8（Z0 D3）的新会话。上一会话（Claude Code，2026-10-11）
证出了 iT_neg 并接线了归纳六支，出了三条正式收据。你的任务：继续推进
ShCraigElim 的剩余四支，最终落地 zfcTr_D3_internalize 并出正式收据。

工作根（写这里）：/Volumes/D/HoTT-worktrees/cg007-w8-d3，分支 codex/cg007-w8-d3。
动手前先跑 git rev-parse --show-toplevel 与 --abbrev-ref HEAD 核对；
不是这个 worktree / 不是 codex/cg007-w8-d3 就先停下来校准。
dev 主检出 /Volumes/D/HoTT_AI_HANDOFF_20260911 是集成目标，保持干净；回写需授权。
绝不向 /Users/aurolafly/WorkBuddy/Worktrees/.../dev-f65ca154 写任何东西。
也绝不碰 外部资料/、Z0-D3-攻关包-最小完整版/、sources/、private-audit/。
核心资产必须留在仓库内，绝不留只在 /tmp。

先读（全部读完再动手）：
1) CLAUDE.md（尤其第〇节工作根）
2) .claude/goals/CG-007-formalization-completion/HANDOFF-2026-10-11-CLAUDE-CODE-W8-D3.md（本文件，以它为准）
3) .claude/goals/CG-007-formalization-completion/HANDOFF-2026-10-11-CODEX-W8-D3.md（前一版，阶段 A 修法）
4) 形式化追踪/README.md 与 01-有哥德尔路线/README.md
5) GodelQ/ZFC/ShCraigElimInduction.lean 与 ShCraigElimBranches.lean 的未填表

开工第一条命令（只读）：
  cd /Volumes/D/HoTT-worktrees/cg007-w8-d3
  python3 -B .claude/goals/CG-007-formalization-completion/tools/selfcheck_worktree.py

已核实的当前状态（2026-10-11 实编译）：
- 三条新收据：CG001-C-398（iT_neg 九支）、C-400（归纳七支）、C-401（neg_neg_code）。
- ShCraigElimInduction.lean 用 Q（Derivable 版）重开归纳，六支已接线，剩 4 个 sorry：
  allIntro / exsIntro / shiftRule / axm。
- axm 支四块已证（ProbeHAxm.lean、ProbeHAxm2.lean）；最后一环需把 V 层 reWitness
  见证认成引号化。
- allIntro/shiftRule 需 iT-setShift 相容律；其 bvar/fvar 地基已证（ProbeITVE.lean），
  func 支卡在 cFunc 不是 shift-不变。
- zfcTr_D3_internalize 仍未证。

下一步顺序（每步可独立验收）：
[A] 攻 axm 支最后一环：从 Sh.IsCraigAxiom p 得 ∃ σ k, p = ⌜σ⌝ ^⋏ qqVerums k。
    关键引理：FFL.FirstOrder.Arithmetic.Bootstrapping.Δ₁Class.mem_iff_s（用 .mp 显式应用，
    rw 会失败）；Rewriting.emb_injective；quote_padding。
[B] 攻 iT-setShift 相容律的 func 支。先读 Foundation 的 Rewriting.emb 与 Semisentence
    结构，找把 shift 与 Semisentence 接起来的路径。已有零件：
    isSemiformula_cFunc_zero/_arity0/_arity2。
[C] 填完四支后，把 induction_setup_Q 的 Q 版接回 P 版（或直接用 Q 版走 bwd_of_shcraig_elim）。
[D] 最终 zfcTr_D3_internalize 替换 Z0Blocked.lean 的 sorry。
[E] 每步出正式收据（capture_run.py + verify_cg001_run.py --rerun），按精确路径提交。

环境：Lean 4.34.0；Foundation /Volumes/D/HoTT-toolchain-cache/foundation-src（1fb01b72）。
开发编译回路：python3 -B .claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py \
    HoTT/formal/claude-cg001/godel-q-zfc-z0-full <模块...>

陷阱见本文件 §4（收据回路的两个坑、缓存假命中、命名冲突、iT_quote 的强制转换等）。
不 push / 不 tag / 不 publish，除非研究发起人明确授权。
```

---

*本文件落在工作根 `codex/cg007-w8-d3`。`dev` 主检出已恢复干净，未触碰。*
