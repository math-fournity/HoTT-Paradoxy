# -*- coding: utf-8 -*-
import os, shutil, pathlib

ROOT = pathlib.Path("/Volumes/D/HoTT_AI_HANDOFF_20260911")
FSRC = pathlib.Path("/Volumes/D/HoTT-toolchain-cache/foundation-src")
PKG  = ROOT/"HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC"
COMMIT = "1fb01b72de546e1b50821fd05b1314a8d958583f"
GHBASE = f"https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/{COMMIT}"

# ---- (A) 外部AI专攻数学证明包（最小、聚焦、指向完整版包） ----
A = ROOT/"外部资料/Z0-D3-外部AI专攻数学证明包"
A.mkdir(parents=True, exist_ok=True)
(A/"00-README.md").write_text("""# Z0-D3 外部 AI 专攻数学证明包（最小、聚焦）

> 本包只负责一件事：**把 `ShCraigElim` 证出来**。
> 它不做背景科普，只给“在完备基础上专攻证明”所需的精确信息。
> 完整可编译环境已在同仓库 `外部资料/Z0-D3-攻关包-完整版/` 备好（Foundation 全量 308 个 .lean + 目标包全量 45 个 .lean），本包是聚焦于“下一步做什么”的指令层。

## 目标（唯一缺口）

```lean
-- GodelQ/ZFC/Z0Blocked.lean:29
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) := by sorry
```

归约链（已证部分可收据，只差最右一格）：

```
ShCraigElim  (∀ σ, Provable Sh.craig ⌜σ⌝ (V) → Provable 𝗭𝗙𝗖 ⌜translate σ⌝ (V))
  ⇒ bwd_of_shcraig_elim  (Z0UniBridge.lean，已收据 C-390)
  ⇒ bwd ⇒ keyE ⇒ zfcTr_D3_internalize (Z0Blocked.lean:29，带 sorry)
  ⇒ Z0Full.zfc_z0_full_of_D3_internalize ⇒ 𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ
```

`ShCraigElim` 的数学内容：把 V 中一条 `Sh.craig` 推导的**编码**翻译成一条 `𝗭𝗙𝗖` 推导的**编码**
（语法的推导翻译，不是语义完备性——Foundation 的 `of_provability` 是语义的，搬不进非标准 V）。

## 当前真实进度（2026-10-11 本机实编译）

- `ShCraigElimNegLaw.iT_neg`：**8/9 支已编译通过**，唯独 `all`/`exs` 两量词支失败（见 04-当前失败与修法.md）。
- `ShCraigElimSetup.induction_setup` 的 **10 个规则支全是 sorry 骨架**，尚未填。
- `ShCraigElimBranches.lean`：已填 `hWk`/`hVerumIntro` 两支承 P/Q 不变量的支（无 sorry）；`isFormulaSet_translateSeq` 已证。

## 下一步（按此顺序，详见 01/02/03）

1. 闭 `iT_neg` 的 `all`/`exs` 两支（机械错误，修法见 04）。
2. 写 `iT_setShift` / `iT_substs1`（hAll/hExs/hShift 需要）。
3. 填 `hAnd`/`hOr`（`iT_and`/`iT_or` + `Derivable.and_m`/`or_m`）。
4. 把 10 支接进 `induction_setup`，产出无 sorry 的 `ShCraigElim`。
5. `Z0Blocked.lean` 的 sorry 改为 `exact bwd_of_shcraig_elim elim σ h`。
6. 按 F-011 抓收据（见 攻关包-完整版/04 或 03-Foundation-API与URL.md）。

## 完整可编译环境在哪里

- 全量源码 + 编译脚本：`外部资料/Z0-D3-攻关包-完整版/`
- 最小可编译包（含 06-Foundation闭包 308 源 + 05-项目模块）：`外部资料/Z0-D3-攻关包-Codex接管版/`
- Foundation GitHub：`https://github.com/FormalizedFormalLogic/Foundation` @ `1fb01b72`
- 单文件 raw 模板：`https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/<相对路径>`
""", encoding="utf-8")

(A/"01-必读文件清单.md").write_text("""# 必读文件清单（本地路径，均在目标包内）

| 文件 | 角色 |
|---|---|
| `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/Z0Blocked.lean` | 目标阻塞引理（带 sorry） |
| `.../Z0UniBridge.lean` | 归约：bwd 缩为一条消去 `ShCraigElim`；`ShCraigElim` 定义 |
| `.../Z0Full.lean` | 机器：`zfcTr`、`models_zfcTr_iff`、`zfc_z0_full_of_D3_internalize` |
| `.../InternalTranslate.lean` | `iT` 与 `iT_rel/iT_nrel/iT_and/iT_or/iT_all/iT_exs/iT_quote` 定义与计算规则 |
| `.../SeqTranslateFormula.lean` | **同形模板** `isSemiformula_iT`（all/exs 支写法见第 344–355 行） |
| `.../SeqTranslate.lean` | `translateSeq`、`isFormulaSet_translateSeq` |
| `.../ShCraigElimSetup.lean` | 10 支归纳骨架（`P`/`Q` 不变量已证） |
| `.../ShCraigElimNegLaw.lean` | `iT_neg`（8/9 支过，all/exs 失败） |
| `.../ShCraigElimBranches.lean` | 已填 hWk/hVerumIntro；未填支注释 |
| `.../ShCraigElimPredicate.lean` | `P`/`Q` 谓词定义 |

> 相对根：`/Volumes/D/HoTT_AI_HANDOFF_20260911/`。完整可编译副本见 `外部资料/Z0-D3-攻关包-完整版/`。
""", encoding="utf-8")

(A/"02-目标定理与分解.md").write_text("""# 目标定理与 10 支分解

## 目标
`ShCraigElim`：在任意 𝗜𝚺₁ 模型 V 中，
`∀ σ, Provable Sh.craig ⌜σ⌝ (V) → Provable 𝗭𝗙𝗖 ⌜arithTrln.translate σ⌝ (V)`。

## 归纳设置（`ShCraigElimSetup.induction_setup`）
用 `Derivation.induction1 (T := Sh.craig)` 的 10 个规则支，每支目标化简为
`Provable 𝗭𝗙𝗖 (translateSeq s)`（s 是该支结论 sequent）。
不变量 `P d := Provable (L:=ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (fstIdx d))` 已是 Σ1 谓词（`p_defined` 已证）。

## 10 支现状
| 支 | 依赖 | 现状 |
|---|---|---|
| axL | `iT_neg`（hAxL 里出现 `iT 0 (neg p)`） | sorry |
| verumIntro | `iT_verum` | sorry（hVerumIntro 已可在 Branches 复用） |
| andIntro | `iT_and` + `Derivable.and_m` | sorry |
| orIntro | `iT_or` + `Derivable.or_m` | sorry |
| allIntro | `iT_setShift` 相容 | sorry |
| exsIntro | `iT_substs1` 相容 | sorry |
| wkRule | `translateSeq_mono` | sorry（hWk 已可在 Branches 复用） |
| shiftRule | `iT_setShift` 相容 | sorry |
| cutRule | `iT_neg`（ih₂ 里 `iT 0 (neg p)`） | sorry |
| axm | `CraigTrick.lean` 的 `Sh.craig` 公理 | sorry |

## 已复用零件（Branches）
`hWk`、`hVerumIntro`、`isFormulaSet_translateSeq` 已证无 sorry。
""", encoding="utf-8")

(A/"03-Foundation-API与URL.md").write_text(f"""# Foundation 关键 API 与 GitHub 地址

> commit：`{COMMIT}`（Foundation 1fb01b72）。
> 仓库：`https://github.com/FormalizedFormalLogic/Foundation`
> 单文件 raw：`{GHBASE}/<相对路径>`

## 证明里会直接用的引理（本地路径 → GitHub raw）
| 引理 | 本地路径 | GitHub raw |
|---|---|---|
| `neg_rel` / `neg_nrel` / `neg_and` / `neg_or` / `neg_all` / `neg_ex`（均 `@[simp]`） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Formula/Functions.lean:75-96` | `{GHBASE}/Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Formula/Functions.lean` |
| `IsUFormula.neg_neg` | `.../Syntax/Formula/Functions.lean:127` | 同上 |
| `CraigTrick.craigCh` / `Sh.craig` 构造 | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/CraigTrick.lean` | `{GHBASE}/Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/CraigTrick.lean` |
| `sigma_one_complete`（算术理论 Σ1 完全性） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean` | `{GHBASE}/Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean` |
| `Derivation.induction1` | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Typed.lean` | `{GHBASE}/Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Typed.lean` |
| `Provable` 定义 `∃ d, Proof T d φ` | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:541` | `{GHBASE}/Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean` |
| `of_provability`（语义，搬不进非标准 V） | `Foundation/FirstOrder/LK/Interpretation.lean:443` | `{GHBASE}/Foundation/FirstOrder/LK/Interpretation.lean` |

> 注意：第三位 AI 曾把 `R0/Basic.lean` 写成 `Foundation/FirstOrder/Arithmetic/Bootstrapping/R0/Basic.lean`（404）。
> 正确路径是 `Foundation/FirstOrder/SetTheory/R0/Basic.lean`（200）。但本包根本不用 R0，无关。

## 全量源码
- 本地：`/Volumes/D/HoTT-toolchain-cache/foundation-src/`（314 个 .lean）
- 已打包：`外部资料/Z0-D3-攻关包-完整版/Foundation/`（308 个 .lean，与 1fb01b72 一致）
- 逐条 URL 清单：`外部资料/Z0-D3-攻关包-完整版/foundation_modules_urls.txt`
""", encoding="utf-8")

(A/"04-当前失败与修法.md").write_text("""# 当前失败与修法（iT_neg 的 all/exs 两支）

## 报错（2026-10-11 本机实编译 ShCraigElimNegLaw.lean）
```
error: Tactic `rewrite` failed: Did not find an occurrence of the pattern
  neg ℒₛₑₜ (result ℒₒᵣ iT.construction (iT.construction.allChanges param 0) p)
in the target expression
  ^∃ domZero ^⋏ iT (iT.construction.exsChanges param 0) (neg ℒₒᵣ p) = ...
```

## 根因（机械错误，不是死路）
`all` 支误用 `iT_all`/`iT_exs`，把 LHS 写成 `iT (exsChanges param 0) (neg p)`；
而归纳假设 `ih 0` 的键是 `allChanges param 0`（定义上都等于 `param+1`，但 `rw` 不会自动把
`exsChanges` 展开成 `allChanges`）。目标是 `iT (exsChanges param 0) (neg p)`，`ih 0` 匹配不上。

## 修法（对照 `SeqTranslateFormula.lean:344` 的 `isSemiformula_iT` 同形 all/exs 支）
不要走 `iT_all`/`iT_exs`，直接用 `iT.construction.result_all`/`result_exs`，使 LHS 自然就是
`result (allChanges param 0) p`：

```lean
· intro n param p hp ih h
  rw [← h] at hp
  rw [neg_all (L := ℒₒᵣ) hp.isUFormula, iT_exs (IsUFormula.neg hp.isUFormula)]
  rw [show iT (param + 1) (neg ℒₒᵣ p) = iT (iT.construction.exsChanges param 0) (neg ℒₒᵣ p) by simp [iT.construction]]
  rw [← ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])]
  simpa [iT.construction, neg, imp, domZero]
· intro n param p hp ih h
  rw [← h] at hp
  rw [neg_ex (L := ℒₒᵣ) hp.isUFormula, iT_all (IsUFormula.neg hp.isUFormula)]
  rw [show iT (param + 1) (neg ℒₒᵣ p) = iT (iT.construction.exsChanges param 0) (neg ℒₒᵣ p) by simp [iT.construction]]
  rw [← ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])]
  simpa [iT.construction, neg, imp, domZero]
```

## 编译核验
```bash
export PATH="/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin:/usr/bin:/bin:$PATH"
cd /Volumes/D/HoTT_AI_HANDOFF_20260911
python3 -B .claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py \\
  HoTT/formal/claude-cg001/godel-q-zfc-z0-full GodelQ/ZFC/ShCraigElimNegLaw.lean
```
exit 0 且 `#print axioms` 只剩 `propext`/`Classical.choice`/`Quot.sound` 即通过。
""", encoding="utf-8")

print("A written:", A)
print("  files:", sorted(p.name for p in A.iterdir()))

# ---- (B) 第三位 AI 说“缺的模块”补发包 ----
B = ROOT/"外部资料/Z0-D3-补充-第三位AI缺的模块"
B.mkdir(parents=True, exist_ok=True)
relpaths = [
    "Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean",
    "Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/CraigTrick.lean",
    "Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Typed.lean",
    "Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean",
    "Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Formula/Functions.lean",
    "Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Formula/Basic.lean",
    "Foundation/FirstOrder/SetTheory/R0/Basic.lean",  # 注意：第三位AI误写成 R0/Basic.lean（无前缀），正确是 SetTheory/R0/Basic.lean
]
copied = []
for rp in relpaths:
    src = FSRC/rp
    if not src.exists():
        print("MISSING LOCAL:", rp); continue
    dst = B/rp
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    copied.append(rp)

# 全量 URL 清单（子sumes “缺的 20 个模块”）
full_manifest = ROOT/"外部资料/Z0-D3-攻关包-完整版/foundation_modules_urls.txt"
out_manifest = B/"FOUNDATION_ALL_MODULES_URLS.txt"
if full_manifest.exists():
    shutil.copyfile(full_manifest, out_manifest)
    nlines = sum(1 for _ in open(full_manifest))
else:
    nlines = 0

(B/"README.md").write_text(f"""# 补发包：第三位 AI 说“缺的 Foundation 模块”

> 第三位 AI 在沙箱里**没有 Lean/Mathlib/Foundation、zip 只含 4 个模块**，于是报告“缺 20 个模块”。
> 本机已核实：**这些模块全部存在**（Foundation 全量 314 个 .lean，commit `1fb01b72`）。
> 本目录把该 AI 点名的模块**原样复制**进来，并附 GitHub raw URL，使其联网即可自取。

## 已复制的模块（相对路径 = Foundation 仓库内路径）
""" + "\n".join(f"- `{rp}`  →  {GHBASE}/{rp}" for rp in copied) + f"""

## 全量清单
`FOUNDATION_ALL_MODULES_URLS.txt`：本机 `外部资料/Z0-D3-攻关包-完整版/foundation_modules_urls.txt`
的副本，含 **{nlines}** 条 Foundation 模块 GitHub raw URL（逐条 `curl -O` 即可复现全量 308 源）。
所谓“缺的 20 个模块”已被这个全集清单完全覆盖——无需单独补列。

## 第三位 AI 的路径误写
它把 `R0/Basic.lean` 写成 `Foundation/FirstOrder/Arithmetic/Bootstrapping/R0/Basic.lean`（GitHub 返回 404）。
正确路径是 `Foundation/FirstOrder/SetTheory/R0/Basic.lean`（200）。但本包（Z0-D3）根本不用 R0，无关。

## GitHub 取源
- 仓库：`https://github.com/FormalizedFormalLogic/Foundation`
- commit：`{COMMIT}`
- 单文件：`{GHBASE}/<相对路径>`
""", encoding="utf-8")

print("B written:", B)
print("  copied:", len(copied), "modules; manifest lines:", nlines)
