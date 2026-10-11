from pathlib import Path
D = Path("/Volumes/D/HoTT_AI_HANDOFF_20260911/外部资料/Z0-D3-攻关包-Codex接管版")

def w(rel, text):
    p = D / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    print("wrote", p)

w("00-先读这个/START.md", """# 接手包 · Z0-D3 / ShCraigElim 攻关（Codex 接管版，最小完备）

本包给下一个 AI（或下一个 Session）用来攻下主线“形式化与机器证明”最后唯一未闭合的命题：
`ShCraigElim`（即 Hilbert–Bernays 可导性条件 D3 的唯一实质内容）。

## 0. 你先要纠正的三个误传

接力材料里有三段互相冲突、且与本机事实不符的说法。本包以本机 Lean 4.34.0 实编译为唯一判据。

1. “neg 律（ShCraigElimNegLaw.lean）0 sorry 已证、编译通过” —— 假的。
   本机用 devbuild_ns.py 编译它报错：iT_and / iT_or 的 rewrite 模式匹配不上
   （目标里是 iT (neg (p⋏q))，而引理改写的是 iT (p⋏q)），且文件含 sorry（sorryAx）。
2. “Foundation 缺 140 个模块（第三位 AI 称沙箱里没有 Lean/Mathlib/Foundation）” —— 假的。
   本机 Foundation 源 1fb01b72 共 308 个 .lean 已存在且已构建；“缺模块”是其无网络沙箱的假象。
   本包 06-Foundation闭包/ 已复制全部 308 个模块，离线可用；Foundation地址.md 给网络 URL。
3. “八个工作方向”还开着 —— 假的。八个 git worktree 方向的逐条覆盖已在 2026-10-10 用本机
   Foundation 构建树重放闭合（CG001-C-123..C-127、CG001-C-387）。当前唯一开放方向是 Z0 的 ShCraigElim。

## 1. 最小目标

把 ShCraigElim 证成无 sorry 的定理，使 Z0Blocked.lean 的 sorry 改为引用它，
从而 Z0 完整形式 ZFC ⊬ (ZFC.consistent)^t 在本机工具链下完整成立。

归约链（全部已证）：ShCraigElim ⇐ bwd_of_shcraig_elim（C-390）=> keyE =>
zfcTr_D3_internalize（Z0Blocked.lean）=> zfc_z0_full_of_D3_internalize（C-122）=
ZFC ⊬ arithTrln.translate (ZFC.consistent)。

## 2. 阅读顺序

1. START.md（本文件）
2. 01-目标与缺口/GOAL.md —— 目标命题逐字、归约链、已证零件
3. 01-目标与缺口/STATUS.md —— 逐文件真实编译状态（本机实测）
4. 03-九支归纳任务拆解/ROUTES.md —— 10 个归纳支需要什么、neg 律怎么修
5. 02-API与源码地址/API.md + Foundation地址.md —— 关键 Foundation 引理与源码位置
6. 04-编译与收据/BUILD.md —— 如何编译、如何抓 F-011 收据
7. 07-修订说明/REVISION.md —— 对原计划 zfcTr-D3-plan.md 的独立评审

## 3. 环境（本机已实测可用）

- Lean 4.34.0：/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0
- Foundation 源 1fb01b72：本包 06-Foundation闭包/Foundation/（离线）；网络版见 Foundation地址.md
- 增量编译脚本：.claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py
- 不得修改 Foundation/Mathlib 源码；新引理只能写成包内新文件
""")

print("part1 done")

w("01-目标与缺口/GOAL.md", """# 目标命题与归约链（逐字）

## 1. 最终目标

主线“形式化与机器证明”的全部前提都已证，只差 D3（Hilbert–Bernays 第三可导性条件，
即形式化 Σ1 完全性）这一条。固定写成：

```lean
-- Z0Blocked.lean（当前带 sorry，是唯一的阻塞引理）
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) := by
  sorry
```

读作：在 𝗜𝚺₁ 的每个模型 V 中，若 𝗭𝗙𝗖 证明了 τ 的翻译，则 𝗭𝗙𝗖 也证明“𝗭𝗙𝗖 证明 τ 的翻译”
这句话的翻译。`zfcTr τ := trProv.val/[⌜τ⌝]`，`trProv` 是 Σ1 公式。

## 2. 归约链（全部已证，引用即成立）

| 环节 | 文件 | 状态 |
|---|---|---|
| `zfc_z0_full_of_D3_internalize`：D3 => Z0 完整形式 | Z0Full.lean | 已证（无 sorry） |
| `zfcTr_D3_internalize_of_bridge'`（C-128） | Z0Bridge.lean | 已证 |
| `bwd_of_shcraig_elim`（C-390）宇宙多态桥 | Z0UniBridge.lean | 已证 |
| `ShCraigElim`：Sh.craig 的 V 内推导编码翻成 ZFC 推导编码 | （待建） | 待证 |

```lean
-- Z0UniBridge.lean
abbrev ShCraigElim (V) [..] : Prop :=
  ∀ (σ : ArithmeticSentence),
    Provable Sh.craig (⌜σ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)
```

一旦证出无 sorry 的 ShCraigElim，Z0Blocked.lean 的 sorry 改为
`exact bwd_of_shcraig_elim elim σ h`，整条链闭合。

## 3. 为什么 Foundation 的现成工具填不上

- `of_provability`（Foundation/.../LK/Interpretation.lean:443）经完备性定理语义地得到
  `U ⊢ σ → T ⊢ π.translate σ`；它不给“证明编码上的可计算函数”，搬不进非标准 V。
- `provable_internalize`（DerivabilityCondition/D3.lean）只对算术理论 T:ArithmeticTheory；
  ZFC 不是算术理论，不能直接套。
- `sigma_one_complete` 给的是 Provable 𝗜𝚺₁ 编码，我们要的是 Provable 𝗭𝗙𝗖 编码；两者无现成桥。

结论：必须对 Sh.craig 的推导结构做归纳消去——这正是 ShCraigElim。
Foundation 对 Sh.craig 直接 inferInstance 给出 D3，但那是对“算术理论”的；我们要的是跨到 ZFC 的那一步。
""")

w("01-目标与缺口/STATUS.md", """# 逐文件真实编译状态（本机 Lean 4.34.0 实编译，2026-10-11）

判据：用 .claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py 编译每个文件，看 exit code 与是否含 sorryAx。

## 已编译通过、无 sorry（可直接复用）

- Z0Full.lean、Z0Bridge.lean、Z0UniBridge.lean、Z0Shadow.lean、Z0PA.lean、Z0Probe.lean —— 主链与归约，均通过。
- SeqTranslate.lean、SeqTranslateFormula.lean —— translateSeq 与 isSemiformula_iT 等，通过。
- InternalTranslate.lean —— iT 与 iT_rel/iT_nrel/iT_verum/iT_falsum/iT_and/iT_or/iT_all/iT_exs/iT_quote（仅引号化版本）均通过。
- NegInvolution.lean / NegInvolutionBranches.lean —— 含 sorryAx，不在主链上，与本任务无关，忽略。
- ShCraigElimSetup.lean / ShCraigElimPredicate.lean —— 归纳不变量 P/Q 是 Σ1 谓词，induction_setup 的 10 个支全是 sorry 骨架（编译通过，但无实质证明）。
- ShCraigElimBranches.lean —— 只填了 hWk/hVerumIntro（通过），其余支未填。

## 未编译通过（必须修）

- ShCraigElimNegLaw.lean —— 报错。错误点：
  - and 支：`rw [iT_and hp.isUFormula hq.isUFormula, iT.construction.and, neg_and ..]` 之后目标里是
    `iT param (neg ℒₒᵣ (p ^⋏ q))`，而 iT_and 改写的是 `iT param (p ^⋏ q)`，模式不匹配。
  - or 支：`rw [iT_or ..]` 同样 "Did not find an occurrence of `iT ?m (p ^⋎ q)`"。
  - all/exs 支：`rw [neg_all .., iT_exs .., imp]` 之后 "Failed to rewrite using equation theorems for 'imp'"；
    以及 IsUFormula.imp 被当作函数应用（应为 iff）。
  - 文件末尾 #print axioms 显示 sorryAx，证实含未证。
  修复思路见 03-九支归纳任务拆解/ROUTES.md 的 neg 律一节。

## 包外依赖（第三方 AI 误报“缺失”的，本机齐全）

Foundation 1fb01b72 的 308 个 .lean 全在 06-Foundation闭包/Foundation/；关键模块
DerivabilityCondition/D3.lean、Syntax/CraigTrick.lean、Syntax/Proof/Basic.lean、
Syntax/Proof/Typed.lean、Syntax/Formula/Hierarchy.lean 均在。
（唯一的 FirstOrder/SetTheory/R0/Basic.lean 不在闭包内——因为本包根本不用 R0，无关。）
""")

print("part2 done")

w("03-九支归纳任务拆解/ROUTES.md", r'''# 九支（实为十支）归纳任务拆解与攻坚路线

`ShCraigElim` 用 `Derivation.induction1`（Foundation `.../Bootstrapping/Syntax/Proof/Basic.lean:642`）
对 Sh.craig 的推导做结构归纳。该原理的 10 个规则支是：
`axL`、`verumIntro`、`andIntro`、`orIntro`、`allIntro`、`exsIntro`、`wkRule`、`shiftRule`、
`cutRule`、`axm`。每个支的证明义务是把“当前推导的结论 sequent 翻译后 𝗭𝗙𝗖 可导”
（`Q d`，即 `Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`）从归纳假设推出来。

## 0. 前置：两条已填的支（模板）

- `hWk`：用 `Derivable.wk` + `translateSeq_mono` + `isFormulaSet_translateSeq`（已证在 ShCraigElimBranches.lean）。
- `hVerumIntro`：用 `Derivable.verum` + `iT_verum`（已证）。

## 1. neg 律（hAxL / hCut / hShift 三支配它）—— 必须先修，否则编译不过

`ShCraigElimNegLaw.lean` 想证一般（V 内任意公式码）的
`iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)`。当前文件用 `UformulaRec1.Construction.semiformula_result_induction`
展开，但 and/or/all/exs 支的 rewrite 模式错。修复要点（对照已证的 iT_and 的形状）：

`iT_and` 的真实定义（InternalTranslate.lean:552）是
`iT n (p ^⋏ q) = iT n p ^⋏ iT n q`，即改写的是 `iT (p⋏q)`。
而 neg 律的 `and` 支目标是 `iT param (neg (p⋏q)) = neg (iT param (p⋏q))`，
应先 `rw [neg_and]` 得到 `iT (neg p ⋎ neg q)`，再用 `iT_or`（改写 `iT (neg p ⋎ neg q)`）
得到 `neg (iT p) ⋎ neg (iT q)`，再用 `neg_or` 反向收成 `neg (iT p ^⋏ iT q)`，最后用归纳假设
`ihp : iT (neg p) = neg (iT p)`、`ihq` 代入。和 `ShCraigElimNegFilled.lean` 的 `neg_and_branch`
写法一致（那个文件本身编译通过，可作模板）。**不要再直接 `rw [iT_and, iT.construction.and]`**——
那样会在 `iT.construction.and` 上展开、和目标对不上。

`all`/`exs` 支：目标经 `neg_all`/`neg_ex` 展开后会出现 `imp ℒₛₑₜ domZero (iT (neg p))` 之类；
用 `iT_exs`/`iT_all`（它们改写 `iT (∃ p)`/`iT (∀ p)`，注意层数 +1 由 `domZero`/bound shift 处理），
再用 `IsUFormula.neg_neg` 抵消一次 neg，最后把归纳假设 `ih` 以 `congrArg` 形式代入。
`imp` 是 binder 里的连接词，rewrite 时要写成 `rw [neg_all .., iT_exs ..]` 后手动 `rw [imp]` 一次，
不要指望 simp 透过 binder 记号。`IsUFormula.imp` 是 iff，要用在 `have`/`rw` 时带 `.1`/`.2` 或 `constructor`。

修完 neg 律后，把它接成定理 `iT_neg`（当前文件已有这个名字，把 sorry 去掉即可），
供 hAxL/hCut/hShift 三支把 `iT (neg p)` 化成 `neg (iT p)`。

## 2. 纯语法支（应可直接填，照模板）

| 支 | 需要 | 写法 |
|---|---|---|
| hAnd | iT_and + Derivable.and_m | `iT (p⋏q) = iT p ⋏ iT q`，两子推导的 𝗭𝗙𝗖 推导用 and_m 合取 |
| hOr | iT_or + Derivable.or_m | 同上，or_m |
| hAxL | iT_neg（修后） | `p ∈ s ∧ ¬p ∈ s` => `Derivable 𝗭𝗙𝗖 (insert (iT p) ∅)` 由 `Derivable.by_axL` |
| hCut | iT_neg | 切去 `neg p`，用 Derivable.cut |

## 3. 需要新相容律的支（照 iT_neg 模板各写一个）

| 支 | 需要的相容律 | 说明 |
|---|---|---|
| hAll | iT 与 setShift 的相容 | `allIntro` 在 φ 上加一层量词，翻译后层数 +1，需 `iT (∀p) = ∀(iT p 经 setShift)` |
| hExs | iT 与 substs1 的相容 | `exsIntro` 用项代入，需 `iT (∃p[t]) = ∃(iT p 经 substs1)` |
| hShift | 同 hAll | `shiftRule` 平移自由变量，与 setShift 相关 |

这三个相容律的写法与 iT_neg 同形：用 `UformulaRec1.Construction.semiformula_result_induction`
（对 setShift / substs1 这两个 UformulaRec1 构造）证一般版本。Foundation 的 `setShift`/`substs1`
在 `Rewriting` 或 `Bootstrapping.Syntax` 里定义，先 `#print` 其 `construction` 字段确认可归纳。

## 4. axm 支（唯一用到 ZFC 公理）

`hAxm` 的结论 sequent 由 Sh.craig 的 Craig 公理给出（形状 `ρ.padding k`）。读
`Foundation/.../Bootstrapping/Syntax/CraigTrick.lean` 看 `Theory.craig` 如何把
一个 Σ1 定义挑成一致句；该支要证：`translateSeq` 把这个 Craig 公理翻译成 𝗭𝗙𝗖 的一条定理。
这正是 D3 跨到 ZFC 的实质一步，也是整条链里唯一真正“用”到 ZFC 公理的地方。

## 5. 组装

把 10 支接进 `ShCraigElimSetup.induction_setup`（替换 10 个 sorry），得到无 sorry 的
`ShCraigElim`。`Z0Blocked.lean` 的 sorry 改为 `exact bwd_of_shcraig_elim (fun σ => ...) σ h`。

## 6. 验收（F-011）

1. 精确命题落源码，无 sorry；
2. `#print axioms` 仅含 propext、Classical.choice、Quot.sound；
3. 正运行 + 至少一个负控制（内核应拒绝的变体）；
4. 正式 run receipt（capture_run.py）；
5. 更新 形式化追踪/ 与 CLAIM_EVIDENCE_MATRIX.md。
''')

print("part3 done")

w("02-API与源码地址/API.md", r'''# 可用引理与 API（本机实测精确名字）

## 项目包内（GodelQ/ZFC/）

| 名字 | 文件 | 签名要点 |
|---|---|---|
| `iT` | InternalTranslate.lean:256 | `iT (n p : V) : V := iT.construction.result ℒₒᵣ n p` |
| `iT_rel` / `iT_nrel` | InternalTranslate.lean:538/ | `iT n (^rel k R v) = iTR n k R v` 等 |
| `iT_verum` / `iT_falsum` | InternalTranslate.lean: | `iT n ^⊤ = ^⊤` |
| `iT_and` | InternalTranslate.lean:552 | `iT n (p ^⋏ q) = iT n p ^⋏ iT n q`（需 IsUFormula ℒₒᵣ p q） |
| `iT_or` | InternalTranslate.lean:556 | `iT n (p ^⋎ q) = iT n p ^⋎ iT n q` |
| `iT_all` / `iT_exs` | InternalTranslate.lean: | 量词层 +1 |
| `iT_quote` | InternalTranslate.lean:611 | 仅引号化：`iT 0 ⌜φ⌝ = ⌜arithTrln.translate φ⌝`（C-119） |
| `translateSeq` | SeqTranslate.lean | `∀ y, y ∈ translateSeq s ↔ ∃ x ∈ s, y = iT 0 x` |
| `isSemiformula_iT` | SeqTranslateFormula.lean:348 | `IsSemiformula ℒₛₑₜ n (iT n p)`（C-391 主定理） |
| `models_zfcTr_iff` / `models_zfcTr_iff'` | Z0Full.lean / Z0UniBridge.lean | V ⊧ zfcTr σ ↔ Provable ZFC ⌜translate σ⌝ |
| `zfcTr_sigma1` | Z0Full.lean | zfcTr σ 是 Σ1 句 |
| `ShCraigElim` / `bwd_of_shcraig_elim` | Z0UniBridge.lean | 归约链（C-390） |

## Foundation（1fb01b72，路径相对 Foundation/）

| 名字 | 路径 | 作用 |
|---|---|---|
| `Derivation.induction1` | FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:642 | 10 支推导归纳 |
| `internal_provable_iff_internal_derivable` | 同上 :939/947 | Provable T φ ↔ Derivable T (insert φ ∅) |
| `Derivable.wk` / `verum` / `and_m` / `or_m` / `cut` / `by_axL` | FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:792+ | LK 规则（sequent 层） |
| `sigma_one_complete` | FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean 末 | 算术理论的 Σ1 完全性 |
| `provable_internalize` | 同上 | 只对 ArithmeticTheory |
| `internalize_provability`（D1） | FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D1.lean:27 | T ⊢ φ → Provable T ⌜φ⌝ |
| `modus_ponens_sentence`（D2） | DerivabilityCondition/D2.lean:30 | Provable 层 MP |
| `Theory.craig` | FirstOrder/Arithmetic/Bootstrapping/Syntax/CraigTrick.lean | 用 choice 挑出的 Σ1 一致句 |
| `UformulaRec1.Construction.semiformula_result_induction` | FirstOrder/Arithmetic/Bootstrapping/... | 对 UformulaRec1 构造做 formula 层归纳（iT_neg 用它） |
| `IsUFormula.neg_neg` / `neg_and` / `neg_or` / `neg_all` / `neg_ex` | FirstOrder/... | 否定对合与 De Morgan |
''')

w("02-API与源码地址/Foundation地址.md", r'''# Foundation 源码地址（可访问网络时直接拉）

GitHub 仓库：`https://github.com/FormalizedFormalLogic/Foundation`
精确 commit：`1fb01b72de546e1b50821fd05b1314a8d958583f`（"add(FirstOrder/SetTheory): Transitive closure (#1035)"）
raw 基址：`https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/Foundation/`

关键模块（本机已验证返回 200）：

- `FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean`
  `https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean`
- `FirstOrder/Arithmetic/Bootstrapping/Syntax/CraigTrick.lean`
  `https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/CraigTrick.lean`
- `FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Typed.lean`
  `https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Typed.lean`
- `FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean`（含 induction1）
- `FirstOrder/Arithmetic/Bootstrapping/Syntax/Formula/Hierarchy.lean`（含 Sigma1 Hierarchy）

注意：本机的 308 个模块已全部复制进本包 `06-Foundation闭包/Foundation/`，**离线即可编译**；
只有需要对照最新上游或确认某行号时才用上面的 URL。
''')

w("04-编译与收据/BUILD.md", r'''# 编译与收据命令

## A. 增量编译（开发期）

工具：`.claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py`
（去掉 sandbox-exec 的本地变体；正式收据仍用包内冻结的 zfc_lean_check.py）。

```bash
cd /Volumes/D/HoTT_AI_HANDOFF_20260911
PKG=HoTT/formal/claude-cg001/godel-q-zfc-z0-full
python3 -B .claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py \
    $PKG GodelQ/ZFC/ShCraigElimNegLaw.lean
```
看 `exit code`；0 即通过，非 0 看 stdout/stderr 的报错行。缓存同目录 `devbuild_ns/godel-q-zfc-z0-full/`。

## B. 依赖顺序（编译单个文件前先编其 import 闭包）

Z0Full → SeqTranslate → SeqTranslateFormula → NegInvolution* → 你的新文件。
（`*` 号文件含 sorryAx，与本任务无关，编译它们只是因为它们在被依赖链里；不要把它们当源。）

## C. 正式收据（F-011）

```bash
python3 -B .claude/goals/CG-007-formalization-completion/tools/capture_run.py \
    --package HoTT/formal/claude-cg001/godel-q-zfc-z0-full \
    --run-id 2026MMDD-CG001-Z0-SHCRAIGELIM-01 \
    --proof-id MP-CG001-Z0-SHCRAIGELIM-001 \
    --claim-id CG001-C-NNN --expect ACCEPT \
    --source GodelQ/ZFC/Z0Full.lean --source GodelQ/ZFC/ShCraigElimNegLaw.lean \
    --source GodelQ/ZFC/ShCraigElim.lean \
    --scope "..."
```
然后用 `verify_cg001_run.py --rerun` 精确重放一致。注意：**含 sorry 的文件不能进收据源**
（zfc_lean_check.py 纯文本扫描未证标记会拒收）。

## D. 陷阱

- 中文注释里出现未证标记的英文词也会被驱动判为 FORBIDDEN_SOURCE_MARKER；写注释避开。
- 用 Python 写 .lean 比 zsh heredoc 稳（中文转义）。
- `#print axioms` 必须只剩 propext / Classical.choice / Quot.sound。
''')

w("07-修订说明/REVISION.md", r'''# 对 zfcTr-D3-plan.md 的独立评审（Codex 接管版，2026-10-11）

## 0. 直接回答：原计划对吗？

方向对，但“缺口形状”已被后续工作进一步收窄，且原计划 §5 的“经翻译的 Σ1 完全性移植（L1–L5，~1080 行）”
主攻路线已被证明**不必做**——真正剩下的是更窄的 `ShCraigElim` 归纳消去。

## 1. 与原计划的偏差

原计划把缺口写成“重做经翻译的 Σ1 完全性”（§5）。但 C-390（Z0UniBridge.lean）已把 Z0 完整形式
归约为 `ShCraigElim`，而 `ShCraigElim` 经 `bwd_of_shcraig_elim` 归约到原 `zfcTr_D3_internalize`。
即：缺口已收成“对 Sh.craig 的推导编码做结构归纳消去”，不必移植 Foundation 的 bold_sigma_one_complete。

## 2. 对三个接力误传的纠正（本机实测）

1. neg 律未编译过（含 sorry）—— 不是“已证”。见 STATUS.md。
2. Foundation 模块齐全（308 个），第三方 AI 的“缺 140 个”是无网络沙箱假象。
3. 八方向已闭合，只剩 ShCraigElim。

## 3. 修订后的最小路线

1. 修 ShCraigElimNegLaw.lean 的 and/or/all/exs 支（见 ROUTES.md §1）。
2. 填 induction_setup 的 8 个 sorry 支（hAnd/hOr 用 iT_and/iT_or + Derivable.and_m/or_m；
   hAxL/hCut 用 iT_neg；hAll/hExs/hShift 需照 iT_neg 写 iT_setShift/iT_substs1；
   axm 读 CraigTrick.lean）。
3. 接成无 sorry 的 ShCraigElim；Z0Blocked.lean 的 sorry 改为引用它。
4. 抓 F-011 收据、更新 形式化追踪/ 与矩阵。

## 4. 不要走的路

原计划 §5 的 ~1080 行 Σ1 完全性移植（已由 ShCraigElim 取代）；不要试图把 provable_internalize
推广到 ZFC（需要集合论语言的 Σ1 完全性，更难）。
''')

print("ALL DONE")
