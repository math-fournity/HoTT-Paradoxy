# HANDOFF — CG-007 W8 (Z0 D3) · Codex 接管实测交接（2026-10-11）

> 本文件由 Codex 接管会话在**实际读代码 + 实际跑 Lean 编译**后写出，专门纠正并补全前序交接文档
> 里已经过时的 HEAD 数字、错误的"已编译"声称，以及未落实的 git 真相。判定标准只有一条：
> **对应 `.lean` 能被 `devbuild_ns.py` 编译（exit 0、无 `sorry`）才算数**。
> 本会话**没有继续推进证明**，只做了状态核对、纪律校正与本文档落地；下一步见末尾提示词。

---

## 0. 工作目录（唯一真值，别搞错）

- **唯一工作根（写这里）：专用 worktree** `/Volumes/D/HoTT-worktrees/cg007-w8-d3`
  - `git rev-parse --show-toplevel` → `/Volumes/D/HoTT-worktrees/cg007-w8-d3`
  - 分支：`codex/cg007-w8-d3`；从 `dev @ fb073d5c` 建立（用户 2026-10-11 裁定：CG-007 在独立 worktree 推进，
    不干扰 `dev` 上的既有内容）。
  - 编译缓存真实位置：`.claude/goals/CG-007-formalization-completion/tools/devbuild_ns/`（已被 `.gitignore` 排除，可重算）。
- **`dev` 主检出是集成目标，不是开发区**：`/Volumes/D/HoTT_AI_HANDOFF_20260911`（分支 `dev`，
  `origin/dev` → `87b65dfd`，未 push）保持干净；只有候选通过验收并经用户授权后，才按精确路径回写 `dev`。
- **绝对禁止写入**：`/Users/aurolafly/WorkBuddy/Worktrees/.../dev-f65ca154`
  - 这是 `dev` 的 git linked worktree，但停在 `workbuddy/dev-f65ca154` 分支、HEAD `87b65dfd`，
    其 `HoTT/formal/.../GodelQ/ZFC/` 仍是 2026-10-10 的旧快照（缺全部 W8 文件），也没有 `devbuild_ns` 入口。
  - 接到"当前目录 / 这个 worktree"式指令时先 `git rev-parse --show-toplevel` 与 `git rev-parse HEAD` 比对；
    若不是 `codex/cg007-w8-d3`，回到 `/Volumes/D/HoTT-worktrees/cg007-w8-d3`。
- **不要碰**：`外部资料/`、`Z0-D3-攻关包-最小完整版/`（用户目录）；并行会话未提交物
  （`Z0Layer1.lean` / `Z0Layer1Emb.lean` / `WrongZ0Layer1Overclaim.lean` / `CLAIM-Z0-LAYER1.md` 及 6 个治理文件的纯追加）。
- **不要碰**：`sources/`、`private-audit/`、他人未提交文件；不 push / 不 tag / 不 publish。

---

## 1. 一分钟状态（已机器核实，2026-10-11）

- `zfcTr_D3_internalize` 仍未证——这是 Z0 完整形式 `𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)ᵗ` 的唯一实质缺口；它当前以
  `sorry` 显式占位在 `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/Z0Blocked.lean`。
- C-120 的影子形式 `𝗭𝗙𝗜 ⊬ (Sh.craig.consistent)ᵗ` 已无条件成立，不受本缺口影响。
- 缺口已收缩为一条句法等价 `keyE` 的 ← 方向：一条 **V 内部的语法解释定理**（ℒₒᵣ → ℒₛₑₜ 的推导翻译）。
- 已编译确认可用的地基（exit 0）：`SeqTranslateFormula.lean` 的 `isSemiformula_iT`（CG001-C-391）、
  `isSemiformula_iTR` / `isSemiformula_domZero` / `isSemiformula_iVE` / `isSemiformula_conjunct` /
  `isSemiformula_cRel` 等；`InternalTranslate.lean` 的 `iT_rel/nrel/verum/falsum/and/or/all/exs` 与 `iT_quote`。

---

## 2. 当前仓库内真实的两处未提交改动（必须知道）

`git status --porcelain=v1` 在 canonical `dev` 上只显示这两处 package 内改动：

1. `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/NegInvolution.lean`
   - **已编译通过（exit 0，仅 3 条标准公理，无 sorry）**。关键命题 `neg_neg_code`
     `{n p} (hp : IsSemiformula ℒₒᵣ n p) : neg ℒₒᵣ (neg ℒₒᵣ p) = p` 已实现，证法是直接用 Foundation 的
     `IsUFormula.neg_neg hp.isUFormula`（旧路线想走 `UformulaRec1` 归纳触发 implicit-lambda bug 且漏 `sorryAx`）。
   - 本会话已 `git status` 核实其改动存在、且 `devbuild_ns.py` 对该文件直接 `## skip`（缓存命中 = 上一次 exit 0）。
   - **建议**：这一步的收据还没出；接手后把它并入"阶段 A 收据"一起出，不要单独遗留。

2. `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/ShCraigElimNegLaw.lean`
   - **当前是破损状态（exit 1），不要当成品**。实测编译报错：
     - line 30：`unknown namespace FFL.FirstOrder.Arithmetic.Bootstrapping.Syntax.Formula`
       （该 `open` 多余且非法，原文已有足够 namespace）。
     - line 43：`ShCraigElimNegLaw.neg_imp_domZero has already been declared`（文件里有两个同名 `neg_imp_domZero`，
       第二处引用了**不存在**的 `Ls`）。
     - line 35 / 40 / 52 / 70 / 72 / 81 / 87：归纳支的 `rw` / `show` 目标不匹配、all/exs 支遗留 `unsolved goals`。
     - line 89：`unexpected token '·'`——`iT_neg` 证明体结束后多了一个游离的 `·`。
   - 即：前序交接"已重写 iT_neg"是**假的**，它现在根本过不了编译器。

> 除上述两处外，canonical `dev` 在 package 内**没有其它未提交改动**；`外部资料/` 下的 zip 与
> `zfcTr-D3-plan-revision.md` 是 untracked 用户目录内容，别动、别提交、别清理。

---

## 3. 阶段 A 的真实最小修复路线（iT / neg 相容律，`iT_neg`）

目标：`theorem iT_neg {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p → iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)`
在 V 内对任意公式码成立（解锁 `ShCraigElimBranches` 的 `hAxL`/`hCut`/`hShift`）。

### 3.1 已实测、可直接复用的 Foundation API（commit `1fb01b72`，源码在 `/Volumes/D/HoTT-toolchain-cache/foundation-src`）

- `IsUFormula`（是 `def` 谓词，不是结构；**没有** `.mpr`/`.qqAlls`/`.subst` 之类构造引理）：
  - `@[simp] neg_neg {p} : IsUFormula L p → IsUFormula L (neg L p)`（`Functions.lean:127`）
  - `@[simp] neg_rel / neg_nrel / neg_verum / neg_falsum / neg_and / neg_or / neg_all / neg_ex`
    （`Functions.lean:75–96`，都是码层面等式，需要 `IsUFormula` / `IsRel`/`IsUTermVec` 参数）
  - `@[simp] rel / nrel / verum / falsum / and / or / all / ex`（`Basic.lean:290–382`，是 ↔ iff）
- `IsUFormula` 没有构造子 `.qqAlls`/`.and`/`.subst`/`.rel`；旧代码 `IsUFormula.qqAlls` 之类全部非法。
- 项目里已编译通过的 `isSemiformula_iTR {n k R v} (hR : (ℒₒᵣ).IsRel k R) (hv : IsSemitermVec ℒₒᵣ k n v)`
  返回 `IsSemiformula ℒₛₑₜ n (iTR n k R v)`；其结构字段就是 `.isUFormula`，所以
  `isUFormula_iTR hR hv := (isSemiformula_iTR hR hv).isUFormula` 是**最省事的真 API**。
- `IsUTermVec.isSemitermVec`（`Term/Basic.lean:796`）可把 `IsUTermVec ℒₒᵣ k v` 转到
  `IsSemitermVec ℒₒᵣ k _ v`，但 `isSemiformula_iTR` 本身已吃 `IsSemitermVec`，需要把 `iT_neg` 的
  nrel 支里 `IsUTermVec` 输入用 `.isSemitermVec` 投影后再喂 `isSemiformula_iTR`（或直接让 `iT_neg`
  的归纳输入保持 `IsSemiformula` 并在 rel/nrel 支用 `iT_rel`/`iT_nrel` 已证的 `IsUTermVec` 版本）。

### 3.2 `ShCraigElimNegLaw.lean` 的具体修法（按依赖）

1. 删掉 line 30 的 `open FFL.FirstOrder.Arithmetic.Bootstrapping.Syntax.Formula`（非法 namespace，整行删）。
2. 删掉重复的第二个 `neg_imp_domZero`（引用 `Ls` 的那条）；保留/订正第一条：
   `lemma neg_imp_domZero {x : V} (hx : IsUFormula ℒₛₑₜ x) : neg ℒₛₑₜ (imp ℒₛₑₜ domZero x) = domZero ^⋏ neg ℒₛₑₜ x`
   证明体用 `rw [imp, neg_and (L := ℒₛₑₜ), neg_falsum (L := ℒₛₑₜ), IsUFormula.neg_neg hx]; simp`。
3. `isUFormula_iTR` 按 §3.1 改成 `(isSemiformula_iTR hR hv).isUFormula`；注意 `hv` 的类型要匹配
   `IsSemitermVec ℒₒᵣ k n v`（若归纳支给的是 `IsUTermVec`，先 `.isSemitermVec`）。
4. `iT_neg` 的归纳谓词保持 `P param n p q := param = n → iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q`。
   - rel 支：`rw [neg_rel (L := ℒₒᵣ) hR hv.isUTerm, iT_nrel hR hv.isUTerm]; rfl`
   - nrel 支：`rw [neg_nrel (L := ℒₒᵣ) hR hv.isUTerm, iT_rel hR hv.isUTerm];
     exact IsUFormula.neg_neg (isUFormula_iTR hR hv.isUTerm)`
   - verum/falsum 支：用 `neg_verum`/`neg_falsum` + `iT_falsum`/`iT_verum` + `rfl`。
   - and 支：先把外层 `neg (p ^⋏ q)` 用 `neg_and`，再用 `iT_or`（注意 iT 把 `^⋏` 映到 `^⋎`）；
     or 支对称（`neg_or` + `iT_and`）。目标结构对照 `isSemiformula_iT` 的 and/or 支。
   - all 支（`iT n (^∀ p)`）：用 `neg_all (L := ℒₒᵣ)` 展开左；右用 `iT_exs` 得 `^∃ (domZero ^⋏ iT (n+1) p)`，
     再 `neg_ex`/`neg_and`/`neg_imp_domZero` 与 `isSemiformula_domZero`/`isSemiformula_iT` 把两侧化归到
     `^∃ (domZero ^⋏ …)`；最后 `congrArg` 接 `ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])`。
   - exs 支对称（`neg_ex` + `iT_all`）。
5. 删掉证明体后那个游离的 `·`（line 89 附近的报错来源），并去掉文件尾多余的重复 `end` / 重复 `neg_imp_domZero`。

### 3.3 验收

```bash
cd /Volumes/D/HoTT_AI_HANDOFF_20260911
PKG=HoTT/formal/claude-cg001/godel-q-zfc-z0-full
T=.claude/goals/CG-007-formalization-completion/tools
python3 -B $T/devbuild_ns.py $PKG GodelQ/ZFC/NegInvolution.lean GodelQ/ZFC/ShCraigElimNegLaw.lean
# 期望两文件都 ## skip / lean … exit 0，且无 sorry
```
`#print axioms GodelQ.ShCraigElimNegLaw.iT_neg` 应只剩三条标准公理（与 `NegInvolution` 一致）。

---

## 4. 后续机器证明路线（阶段 B–D 概要，每步可独立验收）

- **阶段 B**：`ShCraigElimBranches.lean` 的 `hAxL`/`hCut`（用阶段 A 的 `iT_neg`）、`hAnd/hOr/hWk/hVerumIntro`
  （据称已好或接近）；以及 `hAll/hExs/hShift`——需要 `iT` 与 `substs1`/`shift`/`free`/`setShift` 相容，
  非平凡：翻译给每个量词多引一个约束变量，de Bruijn 结构变化，先定位 Foundation 的对应 `@[simp]`。
- **阶段 C**：`axm` 支（唯一用到 `𝗭𝗙𝗖` 处）：需 `codeOfREPred` 的一般 V 表示引理（Foundation 的
  `codeOfREPred_spec` 仅 ℕ 层）；由 `mem_craig_codes_iff + reWitness_spec` 得 `zfcTr ρ`，再用 `ρ.padding` 接回。
- **阶段 D**：`derivable_translateSeq` 的 10 个 case 组装（先搬 `probes/SeqTranslateDerivable.lean` 进包逐条修，
  其构造子调用与辅助引理均为猜测、从未编译）；`bridge`/`keyE ←`；最终 `zfcTr_D3_internalize` 替换
  `Z0Blocked.lean` 的 `sorry`。
- **收据**：`capture_run.py`（带沙箱、拒 sorry）+ 先写 CG-001 证据索引行（`verify_cg001_run.py --rerun`
  才过，否则报 `GOAL_INDEX_ROW_COUNT`）+ 更新 `HoTT/CLAIM_EVIDENCE_MATRIX.md` + `形式化追踪/` + `LOG.md`/`STATE.json`，
  每步按精确路径提交。

---

## 5. 本轮落实的治理校正与工作根迁移

1. `AGENTS.md` 的 "CG-007 W8（Z0 D3）工作根纪律" 小节按用户 2026-10-11 裁定重写：
   **CG-007 在专用 worktree `/Volumes/D/HoTT-worktrees/cg007-w8-d3`（分支 `codex/cg007-w8-d3`）推进，
   `dev` 主检出保持干净、只作集成目标**。原先"只在 `dev` 上开发"的旧纪律已被取代。
2. 工作根迁移已执行并逐文件 SHA-256 核验：`AGENTS.md`、`NegInvolution.lean`、`ShCraigElimNegLaw.lean`、
   本交接文档从 `dev` 的工作区原样搬入 `codex/cg007-w8-d3`，`dev` 侧恢复为 HEAD 状态。
3. 重申核心资产纪律：**核心代码、形式化源、治理文档、工作记录的唯一副本必须留在仓库内**
   （`.claude/goals/CG-007-formalization-completion/` 及其 `probes/` 子目录），绝不允许只存在于
   `/tmp` 或任何系统可清理目录。`/tmp/d3build/` 只是遗留参考副本，不回写、不接收成果。

---

## 6. 诚实边界

- 只有"新命题被机器证明并出正式收据"才算新收据；分析与规格不算。
- 卡住就把精确 Lean 命题写回 `Z0Blocked.lean`（带未证标记，自动不入收据）并在 `CLAIM.md` §4 说明实缺口。
- C-120 影子形式已无条件成立，不受本缺口影响。
- 本会话未 push 任何东西；`origin/dev` 仍在 `87b65dfd`。

---

## 7. 给下一步接手会话的提示词（直接复制）

```text
你是接手 CG-007 目标包 W8（Z0 D3）的新会话，目标是把 zfcTr_D3_internalize 这条唯一缺口证明落地并出正式收据。

工作根（写这里）：/Volumes/D/HoTT-worktrees/cg007-w8-d3，分支 codex/cg007-w8-d3，从 dev @ fb073d5c 建立。
dev 主检出 /Volumes/D/HoTT_AI_HANDOFF_20260911 是集成目标、必须保持干净，日常开发不要直接在上面留 dirty 文件；
回写 dev 需要用户明确授权。
绝不要向 /Users/aurolafly/WorkBuddy/Worktrees/.../dev-f65ca154 等 WorkBuddy 链接 worktree 写任何源码或文档——
它们停在 workbuddy/dev-f65ca154 @ 87b65dfd，且缺全部 W8 文件。接到"当前目录"类指令先 git rev-parse 比对，
确认落在 codex/cg007-w8-d3 再动手。
核心资产必须留在仓库内（.claude/goals/CG-007-formalization-completion/），绝不留只在 /tmp。

先读（全部读完再动手）：
1) 顶层 最高指示.md、AGENTS.md、README.md、MEMORY.md、feature-list.md、rulings.md
2) 核心认知.md、方向追踪.md、全景视野.md、扩展认知.md
3) .claude/goals/CG-007-formalization-completion/ 下：HANDOFF-2026-10-11-CODEX-W8-D3.md（本轮实测交接）、
   W8-下一单元-V内部语法解释定理-规格.md、W8-第二层进展-公式保持性地基.md、STATE.json、GOAL.md、工作台.md、LOG.md
4) HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/Z0Blocked.lean 的 §4 与 §8

当前已核实状态：
- zfcTr_D3_internalize 仍未证，以 sorry 占位在 Z0Blocked.lean；这是 Z0 完整形式 𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)ᵗ 的唯一实质缺口。
- C-120 影子形式 𝗭𝗙𝗜 ⊬ (Sh.craig.consistent)ᵗ 已无条件成立，不受影响。
- 已编译地基（exit 0）：SeqTranslateFormula.lean 的 isSemiformula_iT(CG001-C-391)、isSemiformula_iTR/
  isSemiformula_domZero/isSemiformula_iVE/isSemiformula_conjunct/isSemiformula_cRel；InternalTranslate.lean 的
  iT_rel/nrel/verum/falsum/and/or/all/exs 与 iT_quote。
- 两处未提交改动：NegInvolution.lean 已 exit 0（neg_neg_code 用 IsUFormula.neg_neg，无 sorry，但没出收据）；
  ShCraigElimNegLaw.lean 是破损状态（exit 1，重复 neg_imp_domZero 引用不存在的 Ls、非法 open namespace、
  iT_neg 的 all/exs 支 unsolved goals、证明体后多一个游离 ·）——前序"已重写 iT_neg"是假的，必须按
  HANDOFF-2026-10-11-CODEX-W8-D3.md 第 3 节修。

下一步顺序（每步可独立验收）：
[A1] 修 ShCraigElimNegLaw.lean：删非法 open、删重复 neg_imp_domZero、isUFormula_iTR 改用
     (isSemiformula_iTR hR hv).isUFormula、iT_neg 的 rel/nrel/verum/falsum/and/or/all/exs 支按文档第 3.2 节
     用 neg_rel/neg_nrel/neg_verum/neg_falsum/neg_and/neg_or/neg_all/neg_ex + iT_rel/iT_nrel/iT_and/iT_or/
     iT_all/iT_exs + neg_imp_domZero 拼，删掉游离 ·。编译到 exit 0、#print axioms 干净（仅 3 条标准公理）。
[A2] 出阶段 A 收据：NegInvolution.neg_neg_code + ShCraigElimNegLaw.iT_neg，用 capture_run.py（拒 sorry）抓
     主运行+负控制，先写 CG-001 证据索引行（否则 verify_cg001_run.py --rerun 报 GOAL_INDEX_ROW_COUNT），
     再更新 HoTT/CLAIM_EVIDENCE_MATRIX.md、形式化追踪/、LOG.md、STATE.json，按精确路径 git add 提交。
[B] 填 ShCraigElimBranches.lean：hAxL/hCut（用 iT_neg）、hAnd/hOr/hWk/hVerumIntro，以及
     hAll/hExs/hShift（iT 与 substs1/shift/free/setShift 相容，非平凡）。
[C] axm 支：需要 codeOfREPred 的一般 V 表示引理（Foundation 的 codeOfREPred_spec 仅 ℕ 层），由
     mem_craig_codes_iff + reWitness_spec 得 zfcTr ρ，再用 ρ.padding 接回。
[D] derivable_translateSeq 的 10 个 case（先搬 probes/SeqTranslateDerivable.lean 进包逐条修，构造子与辅助
     引理均为猜测未编译）、bridge/keyE ←、最终 zfcTr_D3_internalize 替换 Z0Blocked.lean 的 sorry。
[E] 每步按精确路径提交，更新 LOG.md/STATE.json；只有机器证+正式收据才算新收据，卡住就写回 Z0Blocked.lean 带未证标记。

环境：Lean 4.34.0 @ /Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0；
Foundation 源码 /Volumes/D/HoTT-toolchain-cache/foundation-src（commit 1fb01b72）；
开发编译回路：cp 改动到包内后，cd /Volumes/D/HoTT_AI_HANDOFF_20260911 && python3 -B .claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py HoTT/formal/claude-cg001/godel-q-zfc-z0-full <相对路径…>。
正式收据仍必须用 .claude/goals/CG-007-formalization-completion/tools/capture_run.py（带沙箱、拒 sorry）。

陷阱：omega 在 V(ORingStructure V) 上不工作，算术不等式用 lt_add_self_add_one；ring 可用。
InternalTranslate.lean 把 shiftVecDef/cFuncDef/conjunctDef/iVEDef/cRelDef/iTRDef 标了 irreducible，definability 靠实例。
simp only [cFunc, cFuncN, reduceIte] 约化 0=0 但不约化 1=0/2=0，后者要 split + absurd h (by decide)。
Semiformula.quote_isSemiformula 只收 Semiproposition，要用 Sentence.quote_isSemiformula。
别碰 外部资料/ 与并行会话未提交文件；不 push/tag/publish。
```

---

*本文件在工作根 `codex/cg007-w8-d3`（从 `dev @ fb073d5c` 建立）上落地；`dev` 主检出已恢复干净。
工作根迁移与 AGENTS.md 纪律校正的提交见该分支 git log。*
