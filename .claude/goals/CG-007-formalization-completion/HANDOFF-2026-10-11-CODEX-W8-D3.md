# HANDOFF — CG-007 W8（Z0 D3）· Codex 实测交接（2026-10-11，worktree 版）

> 判定标准只有一条：**对应 `.lean` 能被 `devbuild_ns.py` 编译（exit 0、无 `sorry`）才算数**。
> 本文件全部结论来自本机 Lean 4.34.0 实编译与逐文件 SHA-256，不来自任何对话摘要。
> 与本文冲突的旧摘要（`STATE.json`、`HANDOFF-*`、`形式化追踪/08-*`、`形式化追踪/09-*`）一律以本文与实编译为准。

---

## 0. 工作目录（全 PATH，先校准再动手）

### 0.1 开发工作根（**写这里**）

```text
/Volumes/D/HoTT-worktrees/cg007-w8-d3
```

- 分支：`codex/cg007-w8-d3`，从 `dev @ fb073d5c` 建立（用户 2026-10-11 裁定：CG-007 在独立
  worktree 推进，不干扰 `dev` 主检出上的既有内容）。
- 当前 HEAD：`35a8ee0c`（"move the work root into a dedicated worktree"），工作区干净。
- `git rev-parse --show-toplevel` 应返回上面这个路径；不是就先停下来核对。
- 编译缓存：`.claude/goals/CG-007-formalization-completion/tools/devbuild_ns/`（`.gitignore` 排除、可重算，
  已随仓库复制过来，省掉约 60 秒冷启动）。

### 0.2 集成目标（**保持干净，日常不要写**）

```text
/Volumes/D/HoTT_AI_HANDOFF_20260911
```

- 分支 `dev`；`git rev-parse HEAD` → `5983e2fb`；`origin/dev` → `87b65dfd`；领先 44 个提交、**未 push**。
- 当前只有用户自己的 untracked：`外部资料/Z0-D3-*.zip` 与 `外部资料/zfcTr-D3-plan-revision.md`。
- 候选通过验收后、并经用户授权，才按精确路径把实物提取回这里；不在 `dev` 上直接做日常证明开发。

### 0.3 禁止写入

```text
/Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911/dev-f65ca154
```

- 它是 `dev` 的 git linked worktree（`.git` 是文件，指向 `/Volumes/D/.../.git/worktrees/dev-f65ca154`），
  停在分支 `workbuddy/dev-f65ca154`、HEAD `87b65dfd`，缺 `SeqTranslateFormula.lean` 等全部 W8 文件，
  也没有 `devbuild_ns` 入口。**只读**。
- 另外不要碰：`外部资料/`、`Z0-D3-攻关包-最小完整版/`（用户目录）、`sources/`、`private-audit/`、
  以及其它会话在 `形式化追踪/` 下的未提交改动。不 push / 不 tag / 不 publish。

### 0.4 目标证明包

```text
/Volumes/D/HoTT-worktrees/cg007-w8-d3/HoTT/formal/claude-cg001/godel-q-zfc-z0-full
```

---

## 1. 一分钟状态（2026-10-11 实编译核实）

- `zfcTr_D3_internalize` 仍未证，以 `sorry` 占位在包内 `GodelQ/ZFC/Z0Blocked.lean`。
  它是 Z0 完整形式 `𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)ᵗ` 的唯一实质缺口。
- C-120 的影子形式 `𝗭𝗙𝗜 ⊬ (Sh.craig.consistent)ᵗ` 已无条件成立，不受本缺口影响。
- 缺口收缩为一条句法等价 `keyE` 的 ← 方向：一条 **V 内部的语法解释定理**（ℒₒᵣ → ℒₛₑₜ 的推导翻译）。
- 已编译可当地基（exit 0）：`SeqTranslateFormula.lean` 的 `isSemiformula_iT`（CG001-C-391）、
  `isSemiformula_iTR` / `isSemiformula_domZero` / `isSemiformula_iVE` / `isSemiformula_conjunct` /
  `isSemiformula_cRel`；`InternalTranslate.lean` 的 `iT_rel/nrel/verum/falsum/and/or/all/exs` 与 `iT_quote`。
- 当前最硬拦路石：`GodelQ/ZFC/ShCraigElimNegLaw.lean` 的 `iT_neg` **编译失败**，解锁
  `ShCraigElimBranches` 的 `hAxL`/`hCut`/`hShift`。

---

## 2. 两个版本的 `iT_neg` 都编不过（这是本轮最重要的实测发现）

仓库里同时存在两份 `ShCraigElimNegLaw.lean`，**两份都 exit 1**，但失败方式不同。不要相信任何
"只剩两支"或"8 支已通过"的摘要——以你自己跑出来的编译器输出为准。

| 版本 | 位置 / SHA-256（前 16） | 实编译结果 |
|---|---|---|
| 我保存的开发版 | worktree `GodelQ/ZFC/ShCraigElimNegLaw.lean`，`c67f14288359221c` | exit 1 |
| `dev` HEAD 版 | `git show HEAD:...`，`41935eb32aebdc87` | exit 1 |

**worktree 开发版（`c67f1428`）的报错**

- `line 30`：`unknown namespace FFL.FirstOrder.Arithmetic.Bootstrapping.Syntax.Formula`（非法 `open`）。
- `line 43`：`neg_imp_domZero has already been declared`——文件里有两个同名引理，第二个引用**不存在**的 `Ls`。
- `line 52` / `all` / `exs` 支：`unsolved goals`（量词支没证完）。
- `line 89`：`unexpected token '·'`——证明体后多一个游离的 `·`。
- 其余 `line 35/40/65/70/72/75/81/87`：`rw`/`show` 目标不匹配。

**`dev` HEAD 版（`41935eb3`）的报错**（把该文件单独复制成 `ProbeHeadVersion.lean` 编译所得）

- `line 38`：`No goals to be solved`
- `line 81/84`：`Application type mismatch`
- `line 88/91/93/97`：`Tactic rewrite failed: Did not find an occurrence of the pattern`
- `line 101`：`Failed to rewrite using equation theorems for 'imp'`
- `line 111`：`Function expected at`

> 结论：`形式化追踪/09-Codex接手-现状核验与下一步-20261011.md` 声称"8 个非量词支已通过、只剩
> `all`/`exs` 两支"，与本机实编译不符（HEAD 版有 10 处错误，横跨 `and/or/verum/falsum` 等多个支）。
> 那份文件的方向性判断（缺口是 `ShCraigElim`、要闭 `iT_neg`）仍然正确，**但进度数字不可信**。

---

## 3. 阶段 A 修复路线：`ShCraigElimNegLaw.iT_neg`

目标命题（V 内任意公式码，层数 `n`）：

```lean
theorem iT_neg {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)
```

### 3.1 已实测的 Foundation API（源码 `/Volumes/D/HoTT-toolchain-cache/foundation-src`，commit `1fb01b72`）

**`IsUFormula` 是 `structure`-free 的谓词定义（`Basic.lean:290` 起 `namespace IsUFormula`），
没有 `.qqAlls` / `.and` / `.subst` / `.rel` 这类构造引理——旧代码里的这些名字全部非法。**

- 可用（`Functions.lean`，都是码层面等式、多数带 `@[simp]`）：
  - `IsUFormula.neg`（:102）、`IsUFormula.neg_neg`（:127，**核心**）、`IsUFormula.neg_iff`（:140）
  - `neg_rel`（:75）/ `neg_nrel`（:78）/ `neg_verum`（:81）/ `neg_falsum`（:84）
  - `neg_and`（:87）/ `neg_or`（:90）/ `neg_all`（:93）/ `neg_ex`（:96）
  - `IsUFormula.imp`（:185）/ `IsUFormula.iff`（:208）/ `IsUFormula.shift`（:321）
- 可用（`Basic.lean`，↔ iff 形式）：`IsUFormula.rel`（:321）/ `.nrel`（:332）/ `.verum`（:342）/
  `.falsum`（:345）/ `.and`（:349）/ `.or`（:360）/ `.all`（:371）/ `.ex`（:382）。
- **`imp` 的定义**：`noncomputable def imp (p q : V) : V := neg L p ^⋎ q`（`Functions.lean:169`）。
  所以 `neg L (imp L p q) = neg L (neg L p ^⋎ q) = neg L (neg L p) ^⋏ neg L q = p ^⋏ neg L q`。
- `IsSemiformula` 是 **structure**：`{isUFormula : IsUFormula L p, bv_le : bv L p ≤ n}`（`Basic.lean:1317`）。
  因此 `h.isUFormula` 和 `h.bv_le` 都能直接用；`IsSemiformula.imp`（`Functions.lean`）是 ↔ 形式。
- `UformulaRec1.Construction.result_all`（`Basic.lean:1142`）：
  `c.result L param (^∀ p) = c.all param p ?[c.result L (c.allChanges param 0) p]`（需 `hp : IsUFormula L p`
  与 `hs : c.allSize param p = 1`）。`result_exs` 同形（:1147）。
- `semiformula_result_induction`（`Basic.lean:1574` 起）签名要点：`P : V → V → V → V → Prop`，
  `hall : ∀ n param p, IsSemiformula L (n + 1) p → (∀ i < c.allSize param p, P (c.allChanges param i) (n+1) p
  (c.result L (c.allChanges param i) p)) → P param n (^∀ p) (c.result L param (^∀ p))`。
  结论 `∀ {param n p}, IsSemiformula L n p → P param n p (c.result L param p)`——**输出层 `param` 与
  输入层 `n` 独立量化**，这是必须加 `param = n` 护罩的原因。

### 3.2 具体修法（按依赖顺序）

1. **删** `line 30` 的 `open FFL.FirstOrder.Arithmetic.Bootstrapping.Syntax.Formula`（非法 namespace）。
2. **删**重复的第二个 `neg_imp_domZero`（引用 `Ls` 那条），保留并订正第一条。
   **下面这条已在 worktree 里实编译通过（exit 0）**，直接照抄：

   ```lean
   lemma neg_imp_domZero {x : V} (hx : IsUFormula ℒₛₑₜ x) :
       neg ℒₛₑₜ (imp ℒₛₑₜ domZero x) = domZero ^⋏ neg ℒₛₑₜ x := by
     have hd : IsUFormula ℒₛₑₜ (domZero : V) := (isSemiformula_domZero (n := 0)).isUFormula
     rw [imp, neg_or (L := ℒₛₑₜ) (IsUFormula.neg hd) hx, IsUFormula.neg_neg hd]
   ```

   原理：`imp p q = neg p ^⋎ q`（`Functions.lean:169`），故
   `neg (imp domZero x) = neg (neg domZero ^⋎ x) = neg (neg domZero) ^⋏ neg x = domZero ^⋏ neg x`。

   **两个实测过的坑（都别踩）**：
   - `have hd : IsUFormula ℒₛₑₜ domZero := ...` 会失败，报
     `hd has type IsUFormula.{0,0} ℒₛₑₜ domZero but is expected to have type IsUFormula.{u_1,0} ℒₛₑₜ domZero`。
     **必须写成 `IsUFormula ℒₛₑₜ (domZero : V)`**，把 `domZero` 的 universe 钉到 `V`。
   - `simp [imp, IsUFormula.neg_neg hd]` 这种一步到位写法**不成立**（实测 `unsolved goals`）；
     必须用上面那条显式的三连 `rw`。
3. `isUFormula_iTR` 用**已证的** `isSemiformula_iTR` 投影，不要重拼：

   ```lean
   lemma isUFormula_iTR {n k R v : V} (hR : (ℒₒᵣ).IsRel k R) (hv : IsSemitermVec ℒₒᵣ k n v) :
       IsUFormula ℒₛₑₜ (iTR n k R v) :=
     (isSemiformula_iTR hR hv).isUFormula
   ```

   注意 `isSemiformula_iTR` 要 `IsSemitermVec ℒₒᵣ k n v`；若手上只有 `IsUTermVec`，用
   `IsUTermVec.isSemitermVec`（`Term/Basic.lean:796`）或 `IsSemiterm.isSemiterm` 转。
4. `iT_neg` 归纳谓词保持 `P param n p q := param = n → iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q`，
   并**照抄 `SeqTranslateFormula.lean:348–406` 的 `isSemiformula_iT` 骨架**（同构造子、同护罩、
   同 `ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])` 调用形态），只把每支的结论
   从"公式性"换成"neg 交换律"：
   - rel 支：`rw [neg_rel (L := ℒₒᵣ) hR hv.isUTerm, iT_nrel hR hv.isUTerm]; rfl`
   - nrel 支：`rw [neg_nrel (L := ℒₒᵣ) hR hv.isUTerm, iT_rel hR hv.isUTerm]`，再
     `exact IsUFormula.neg_neg (isUFormula_iTR hR hv.isUTerm)`
   - verum/falsum：`neg_verum`/`neg_falsum` + `iT_falsum`/`iT_verum` + `rfl`
   - and 支：`neg_and`（左）+ `iT_or`（右，注意 `iT` 把 `^⋏` 映到 `^⋎`），再 `congrArg₂`
   - or 支：对称（`neg_or` + `iT_and` + `congrArg₂`）
   - all 支：左用 `neg_all (L := ℒₒᵣ)`；右先 `iT_exs` 得 `^∃ (domZero ^⋏ iT (n+1) p)`，
     再用 `neg_ex` + `neg_and` + `neg_imp_domZero` 归到同一形状，最后 `congrArg` 接
     `ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])`
   - exs 支：对称（`neg_ex` + `iT_all` + `neg_imp_domZero`）
   - **量词支最容易错的地方**：`iT.construction.all _ _ ys = ^∀ (imp ℒₛₑₜ domZero ys.[0])`、
     `exs _ _ ys = ^∃ (domZero ^⋏ ys.[0])`（`InternalTranslate.lean:231–256`），
     `allSize/exsSize = 1`、`allChanges/exsChanges n _ = n + 1`。展开 `c.result L param (^∀ p)` 时必须
     同时给 `result_all` 传 `hp.isUFormula` 和 `(rfl : iT.construction.allSize param p = 1)`，
     然后用 `nth_adjoin_zero` 把 `ys.[0]` 落回子结果（`isSemiformula_iT` 的 `change` 行就是这么做的）。
5. **删**证明体后游离的 `·`，并删文件尾重复的 `end`。

### 3.3 验收

```bash
cd /Volumes/D/HoTT-worktrees/cg007-w8-d3
PKG=HoTT/formal/claude-cg001/godel-q-zfc-z0-full
T=.claude/goals/CG-007-formalization-completion/tools
python3 -B $T/devbuild_ns.py $PKG GodelQ/ZFC/NegInvolution.lean GodelQ/ZFC/ShCraigElimNegLaw.lean
# 期望：NegInvolution 为 ## skip（缓存命中）；ShCraigElimNegLaw 为 ## lean … exit 0
```

再过一遍 `#print axioms GodelQ.ShCraigElimNegLaw.iT_neg`，应只剩三条标准公理
（与 `NegInvolution.neg_neg_code` 一致：`propext`、`Classical.choice`、`Quot.sound`）。

**注意**：文件里若还有 `sorry`，`capture_run.py` 会拒绝出收据。修好后先跑上面的开发回路，
确认 exit 0 且 `grep -c sorry` 为 0，再进入 §5 的正式收据流程。

---

## 4. 后续路线（阶段 B–D，每步可独立验收）

- **阶段 B**：`ShCraigElimBranches.lean` 的 `hAxL`/`hCut`/`hShift`（用阶段 A 的 `iT_neg`）、
  `hAnd/hOr/hWk/hVerumIntro`；以及 `hAll/hExs/hShift`——需要 `iT` 与 `substs1`/`shift`/`free`/`setShift`
  相容。**非平凡**：翻译给每个量词多引一个约束变量，de Bruijn 结构变了，不是平凡交换。
  先定位 Foundation 对应 `@[simp]`（`substs_all`/`substs_and`/`substs_or` 在
  `Formula/Functions.lean:476–485`，`IsUFormula.shift` 在 :321），再逐支归纳。
- **阶段 C**：`axm` 支（唯一用到 `𝗭𝗙𝗖` 处）。需要 `codeOfREPred` 的**一般 V 表示引理**
  （Foundation 的 `codeOfREPred_spec` 只在 ℕ 层）；拿到后由 `mem_craig_codes_iff` + `reWitness_spec`
  得 `zfcTr ρ`，再用 `ρ.padding s = ρ ⋏ ⊤ ⋏ …` 接回。
- **阶段 D**：`derivable_translateSeq` 的 10 个 case 组装。注意
  `.claude/goals/CG-007-formalization-completion/probes/SeqTranslateDerivable.lean` 是**施工图、从未编译**，
  构造子调用与辅助引理（`translateSeq_isFormulaSet`、`fstIdx_axL` 等）都是猜测；先搬进包再逐条修。
  之后 `bridge` / `keyE` 的 ← 方向，最终 `zfcTr_D3_internalize` 替换 `Z0Blocked.lean` 的 `sorry`。

---

## 5. 正式收据流程（F-011 五件事，缺一不可）

1. 命题的类型逐字落在包的 `.lean` 源里（不在对话、不在内存）。
2. 主运行 + 至少一个负控制，用包内冻结的
   `.claude/goals/CG-007-formalization-completion/tools/capture_run.py`（带沙箱、拒 `sorry`）
   抓成 `HoTT/verification/runs/<run-id>/` 的 `RUN.json`、`stdout.txt`、`stderr.txt`、
   `environment.txt`、`source-manifest.json`。
   （`devbuild_ns.py` **只**用于开发迭代，它去掉沙箱，不能当收据。）
3. `verify_cg001_run.py --rerun` 精确重放一致。**必须先在 CG-001 证据索引
   `.claude/goals/CG-001-targeted-overview/证据索引.md` 里写好该 proof/run/claim 的行**，
   否则校验器报 `GOAL_INDEX_ROW_COUNT`。
4. `HoTT/CLAIM_EVIDENCE_MATRIX.md` 追加一节（Package 表 + Claim 表）。
5. 更新 `形式化追踪/`：该线 README 状态表与"下一步"、总览对应行、`99-更新日志.md` 追加一行；
   并按精确路径 `git add` 提交（**不要** `git add -A`），提交信息写清哪些是新收据、哪些只是分析。

**收据完成后**：如果用户授权，再把候选实物按精确路径提取回 `dev` 并在 `dev` 上原位重述被接受的变化。
在此之前 `dev` 保持干净。

---

## 6. 环境与工具链

| 项 | 路径 / 值 |
|---|---|
| Lean | 4.34.0 @ `/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0` |
| Foundation 源码 | `/Volumes/D/HoTT-toolchain-cache/foundation-src`（commit `1fb01b72`） |
| Foundation 构建树 | `/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0`（olean 在 `lib/lean/` 下） |
| Mathlib | `/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-*` |
| 开发编译回路 | `.claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py`（无沙箱，仅开发） |
| 正式收据 | `.claude/goals/CG-007-formalization-completion/tools/capture_run.py`（带沙箱、拒 sorry） |

**上下文目标类型**：`{V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]`。

**已知陷阱**

- `omega` 在 V（`ORingStructure V`）上**不工作**；算术不等式用 `lt_add_self_add_one`（`PeanoMinus.lean:14`）；`ring` 可用。
- `↑(n+1) : V` 的层级转换要 `push_cast`；`(b+n)+1` vs `b+(n+1)` 要 `add_assoc`。
- `Semiformula.quote_isSemiformula` 只收 `Semiproposition`，要用 `Sentence.quote_isSemiformula`。
- `simp only [cFunc, cFuncN, reduceIte]` 约化 `0 = 0` 但**不**约化 `1 = 0` / `2 = 0`；后者要显式 `split` +
  `absurd h (by decide)` 关掉不可能支。
- `if_neg` 已弃用（用 `ite_eq_right`）。
- `InternalTranslate.lean:212` 把 `shiftVecDef`/`cFuncDef`/`conjunctDef`/`iVEDef`/`cRelDef`/`iTRDef`
  标了 `irreducible`；definability 靠**实例**而不是展开定义。definability 处理不了"部分应用"时，
  通常是缺层级实例：给函数同时登记 `𝚺ᴬ₁` 版与 `Γᴬ_[m+1]-Function₂` 版（对照 Foundation 的 `disjSeqSubst`，
  `Formula/Iteration.lean:211`）。
- 模块文档注释必须在 `import` 之后；`noncomputable` 会传染；`Jeroslow.lean` 不在本地导入闭包里。
- **`IsUFormula` 的 universe 坑（本轮实测）**：在 `{V : Type*} [ORingStructure V]` 语境下，
  `have hd : IsUFormula ℒₛₑₜ domZero := ...` 会推断成 `IsUFormula.{0,0}`，与目标里的 `{u_1,0}` 不匹配，
  报 `Application type mismatch`。**凡给 `domZero` 这类顶层 `def : V` 的常量写 `IsUFormula`/`IsSemiformula`
  假设，都要显式标注 `(domZero : V)`**。这条坑会以"`rw` 找不到模式"或"`Application type mismatch`"的
  形式出现，看起来像 `neg_or` 的引理不对，其实只是 universe 不一致。

---

## 7. 本轮已落实的治理动作（已提交在 `codex/cg007-w8-d3`）

1. **工作根迁移**：`dev` 上的四个未提交实物（`AGENTS.md`、`NegInvolution.lean`、`ShCraigElimNegLaw.lean`、
   本交接文档）已逐文件 SHA-256 核验后搬入本 worktree，提交 `35a8ee0c`。
2. **`AGENTS.md` 纪律重写**：把"只在 `dev` 开发"改成"专用 worktree 开发 + `dev` 保持干净、只作集成目标"，
   并登记禁止写入的 WorkBuddy worktree、编译缓存真实路径与本交接文档指针。
3. **`dev` 已还原干净**：三个被改的跟踪文件用 `git restore --source=HEAD` 精确路径还原；本会话新建的
   交接文档从 `dev` 移入备份 `/Volumes/D/HoTT-worktrees/_dev-dirty-backup-20261011/`（非删除）。
   `dev` 现在只剩用户自己的 `外部资料/` untracked 六项。
4. **并行写者已核实无冲突**：`dev` 上另一会话在 09:14–09:24 写 `形式化追踪/09-*`、`99-更新日志.md`
   并自行提交 `b5d703c1`、`5f1c0abf`；其改动只在 `形式化追踪/` 与 `外部资料/`，与本轮还原的三个文件无交集；
   其 `ShCraigElimNegLaw.lean` 校验副本（08:54）与本 worktree 保存的版本 SHA-256 完全一致。

---

## 8. 诚实边界

- 只有"新命题被机器证明并出正式收据"才算新收据；分析与规格不算。
  `NegInvolution.neg_neg_code` 已 exit 0、无 `sorry`，但**尚未出收据**，目前只能标
  `MACHINE_CHECKED_LOCAL / NO_RECEIPT`。
- 卡住就把精确 Lean 命题写回 `Z0Blocked.lean`（带未证标记，自动不进收据）并在 `CLAIM.md` §4 说明实缺口。
- C-120 影子形式已无条件成立，不受本缺口影响。
- 本轮未 push 任何东西；`origin/dev` 仍在 `87b65dfd`。

---

## 9. 给下一步接手会话的提示词（直接复制）

```text
你是接手 CG-007 目标包 W8（Z0 D3）的新会话，目标是把 zfcTr_D3_internalize 这条唯一缺口证明落地并出正式收据。

工作根（写这里）：/Volumes/D/HoTT-worktrees/cg007-w8-d3，分支 codex/cg007-w8-d3，当前 HEAD 35a8ee0c。
动手前先跑 git -C /Volumes/D/HoTT-worktrees/cg007-w8-d3 rev-parse --show-toplevel 与 --abbrev-ref HEAD 核对；
不是这个 worktree 就先停下来校准。
dev 主检出 /Volumes/D/HoTT_AI_HANDOFF_20260911 是集成目标，必须保持干净，日常开发不要在上面留 dirty 文件；
回写 dev 需要用户明确授权。
绝不向 /Users/aurolafly/WorkBuddy/Worktrees/.../dev-f65ca154 写任何东西——它是停在 87b65dfd 的旧快照。
也绝不碰 外部资料/、Z0-D3-攻关包-最小完整版/、sources/、private-audit/，以及其它会话在 形式化追踪/ 下的未提交改动。
核心资产必须留在仓库内（.claude/goals/CG-007-formalization-completion/），绝不留只在 /tmp。

先读（全部读完再动手）：
1) 工作根内 最高指示.md、AGENTS.md（尤其 §CG-007 W8 工作根纪律小节）、README.md、MEMORY.md、feature-list.md、rulings.md
2) 核心认知.md、方向追踪.md、全景视野.md、扩展认知.md
3) .claude/goals/CG-007-formalization-completion/HANDOFF-2026-10-11-CODEX-W8-D3.md（本文件，以它为准）、
   W8-下一单元-V内部语法解释定理-规格.md、W8-第二层进展-公式保持性地基.md、STATE.json、GOAL.md、工作台.md、LOG.md
4) GodelQ/ZFC/Z0Blocked.lean 与 CLAIM.md 的 §4、§8
   注意：形式化追踪/08-* 与 09-* 的进度数字已被实编译推翻，只可当方向参考，不可当进度依据。

已核实的当前状态：
- zfcTr_D3_internalize 仍未证，以 sorry 占位在 GodelQ/ZFC/Z0Blocked.lean；这是 Z0 完整形式
  𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)ᵗ 的唯一实质缺口。C-120 影子形式 𝗭𝗙𝗜 ⊬ (Sh.craig.consistent)ᵗ 已无条件成立，不受影响。
- 已编译地基（exit 0）：SeqTranslateFormula.lean 的 isSemiformula_iT(CG001-C-391)、isSemiformula_iTR/
  isSemiformula_domZero/isSemiformula_iVE/isSemiformula_conjunct/isSemiformula_cRel；InternalTranslate.lean 的
  iT_rel/nrel/verum/falsum/and/or/all/exs 与 iT_quote。
- NegInvolution.lean 的 neg_neg_code 已 exit 0、无 sorry（用 IsUFormula.neg_neg），但尚未出收据。
- 当前拦路石：ShCraigElimNegLaw.lean 的 iT_neg 编译失败（exit 1）。本文件 §2 记录了 worktree 版与 dev HEAD 版
  两份各自的真实报错；§3 给了精确修法。

下一步顺序（每步可独立验收）：
[A1] 按 HANDOFF-2026-10-11-CODEX-W8-D3.md §3.2 修 ShCraigElimNegLaw.lean：删非法 open
     FFL.FirstOrder.Arithmetic.Bootstrapping.Syntax.Formula、删重复的 neg_imp_domZero（引用不存在的 Ls 那条）、
     把保留的 neg_imp_domZero 换成 §3.2 第 2 条那条已实编译通过的版本（注意 hd 必须写成
     IsUFormula ℒₛₑₜ (domZero : V)，否则 universe 不匹配；不要用 simp 一步到位）、
     isUFormula_iTR 改用 (isSemiformula_iTR hR hv).isUFormula、iT_neg 照 SeqTranslateFormula.lean:348-406 的
     isSemiformula_iT 骨架重写（带 param = n 护罩，rel/nrel/verum/falsum 用 neg_rel/neg_nrel/neg_verum/neg_falsum
     + iT_nrel/iT_rel/iT_falsum/iT_verum，and/or 用 neg_and+neg_or 与 iT_or+iT_and 交叉，
     all/exs 先用 result_all/result_exs + nth_adjoin_zero 展开再 neg_all/neg_ex/neg_imp_domZero 归形，
     最后 congrArg 接 ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])），删掉证明体后游离的 ·。
     编译到 exit 0、grep -c sorry 为 0、#print axioms 只剩三条标准公理。
[A2] 出阶段 A 正式收据：NegInvolution.neg_neg_code + ShCraigElimNegLaw.iT_neg，用 capture_run.py（带沙箱、拒 sorry）
     抓主运行 + 至少一个负控制；先写 CG-001 证据索引 .claude/goals/CG-001-targeted-overview/证据索引.md 的行，
     否则 verify_cg001_run.py --rerun 报 GOAL_INDEX_ROW_COUNT；再更新 HoTT/CLAIM_EVIDENCE_MATRIX.md、
     形式化追踪/（线 README + 总览 + 99-更新日志.md）、LOG.md、STATE.json，按精确路径 git add 提交。
[B] 填 ShCraigElimBranches.lean：hAxL/hCut/hShift（用 iT_neg）、hAnd/hOr/hWk/hVerumIntro，以及
     hAll/hExs/hShift（iT 与 substs1/shift/free/setShift 相容——非平凡，翻译多引约束变量、de Bruijn 结构变化；
     先查 Foundation 的 substs_all/substs_and/substs_or 与 IsUFormula.shift）。
[C] axm 支：需要 codeOfREPred 的一般 V 表示引理（Foundation 的 codeOfREPred_spec 仅 ℕ 层），
     由 mem_craig_codes_iff + reWitness_spec 得 zfcTr ρ，再用 ρ.padding 接回。
[D] derivable_translateSeq 的 10 个 case（先搬 probes/SeqTranslateDerivable.lean 进包逐条修，构造子与辅助引理
     均为猜测、从未编译）、bridge/keyE 的 ← 方向、最终 zfcTr_D3_internalize 替换 Z0Blocked.lean 的 sorry。
[E] 每步按精确路径提交并更新 LOG.md/STATE.json；只有机器证 + 正式收据才算新收据；卡住就把精确 Lean 命题写回
     Z0Blocked.lean 带未证标记，并在 CLAIM.md §4 说明实缺口。

环境：Lean 4.34.0 @ /Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0；
Foundation 源码 /Volumes/D/HoTT-toolchain-cache/foundation-src（commit 1fb01b72）。
开发编译回路（无沙箱，仅迭代）：
  cd /Volumes/D/HoTT-worktrees/cg007-w8-d3
  python3 -B .claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py \
      HoTT/formal/claude-cg001/godel-q-zfc-z0-full GodelQ/ZFC/ShCraigElimNegLaw.lean
正式收据必须用 .claude/goals/CG-007-formalization-completion/tools/capture_run.py（带沙箱、拒 sorry）。

陷阱：omega 在 V(ORingStructure V) 上不工作，算术不等式用 lt_add_self_add_one；ring 可用。
InternalTranslate.lean 把 shiftVecDef/cFuncDef/conjunctDef/iVEDef/cRelDef/iTRDef 标了 irreducible，definability 靠实例。
simp only [cFunc, cFuncN, reduceIte] 约化 0=0 但不约化 1=0/2=0，后者要 split + absurd h (by decide)。
Semiformula.quote_isSemiformula 只收 Semiproposition，要用 Sentence.quote_isSemiformula。
不 push / 不 tag / 不 publish。
```

---

*本文件落在工作根 `codex/cg007-w8-d3`（从 `dev @ fb073d5c` 建立）。`dev` 主检出已恢复干净，只余用户自己的
`外部资料/` untracked 项。*
