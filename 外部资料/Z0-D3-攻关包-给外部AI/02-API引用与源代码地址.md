# API 引用与源代码地址（可联网 `curl` 复现）

本文件给"差什么"里每个关键 API 两样东西：
1. **本地路径**（本机 `/Volumes/D/HoTT-toolchain-cache/foundation-src/` 下，逐字可用）；
2. **GitHub 原始地址**（联网机器 `curl -O` 即可取得，已实测返回 200）。

地址模板（commit 固定 `1fb01b72de546e1b50821fd05b1314a8d958583f`）：

```
https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/Foundation/<相对路径>.lean
```

完整 167 个依赖模块的逐行清单见同目录 `Foundation_modules_urls.txt`
（相对路径逐行见 `Foundation_fetch_list.txt`）。

---

## §0 仓库与 commit

- 仓库：`https://github.com/FormalizedFormalLogic/Foundation`
- 固定 commit：`1fb01b72de546e1b50821fd05b1314a8d958583f`
- 本机全量源码（308 个 `.lean`）：`/Volumes/D/HoTT-toolchain-cache/foundation-src/`
- 本机全量构建（1893 模块 olean）：`/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean`

---

## §1 归纳原理与推导规则（填 10 支的核心）

| API | 本地路径 | GitHub 地址 |
|---|---|---|
| `Derivation.induction1`（10 规则支归纳） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:642` | `…/Proof/Basic.lean` |
| `axL` / `verumIntro` / `andIntro` / `orIntro` / `allIntro` / `exsIntro` / `wkRule` / `shiftRule` / `cutRule` / `axm`（推导构造子） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:143-161` | `…/Proof/Basic.lean` |
| `fstIdx_*`（`fstIdx axL` 等结论 sequent 取出） | 同上 `Basic.lean` | `…/Proof/Basic.lean` |
| `Derivable.wk`（弱化规则） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean`（搜 `def wk` / `theorem wk`） | `…/Proof/Basic.lean` |
| `Derivable.verum` | 同 `Basic.lean` | `…/Proof/Basic.lean` |

## §2 公式递归与 `neg` 相容（模板）

| API | 本地路径 | GitHub 地址 |
|---|---|---|
| `UformulaRec1.Construction.semiformula_result_induction`（一般公式归纳原理，**你写 `iT_setShift`/`iT_substs1` 要照抄这个**） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Formula/Functions.lean:528` 起 | `…/Syntax/Formula/Functions.lean` |
| `IsUFormula.neg_neg`（码层面对合 `neg (neg x) = x`；`ShCraigElimNegLaw.lean` 已用） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Formula/Functions.lean:127` | `…/Syntax/Formula/Functions.lean` |
| `neg_verum` / `neg_falsum` / `neg_rel` / `neg_nrel` / `neg_and` / `neg_or` / `neg_all` / `neg_ex`（`neg` 的逐构造子展开） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Formula/Functions.lean` | `…/Syntax/Formula/Functions.lean` |
| 本项目已证的 `iT_neg`（**现成模板，9 支全填无 sorry**） | `HoTT/.../godel-q-zfc-z0-full/GodelQ/ZFC/ShCraigElimNegLaw.lean` | 仓库内（非 Foundation） |

## §3 本项目已证、可直接调用的 `iT` 相容引理

这些都在 `HoTT/.../godel-q-zfc-z0-full/GodelQ/ZFC/` 下，已编译无 sorry：

| 引理 | 文件 | 形状 |
|---|---|---|
| `iT_quote` | `InternalTranslate.lean:611` | `iT 0 ⌜φ⌝ = ⌜arithTrln.translate φ⌝`（仅引号化公式） |
| `iT_rel` / `iT_nrel` | `InternalTranslate.lean` | 原子级 `rel`/`nrel` 翻译 |
| `iT_verum` / `iT_falsum` | `InternalTranslate.lean` | 真假不动 |
| `iT_and` / `iT_or` | `InternalTranslate.lean` | `iT (p⋏q) = iT p ⋏ iT q` |
| `iT_neg`（一般） | `ShCraigElimNegLaw.lean` | `iT n (neg p) = neg (iT n p)`（V 内任意码） |
| `isSemiformula_iT` | `SeqTranslateFormula.lean` | `IsSemiformula (iT n p)` |
| `isSemiformula_iTR` | `SeqTranslateFormula.lean` | 原子翻译的 `IsUFormula` |
| `translateSeq_mono` / `mem_translateSeq_iff` / `translateSeq_insert` | `SeqTranslate.lean` | sequent 翻译性质 |

## §4 你还需要的（未证，核心难点）

下面这些**尚不存在**，是你真正的证明工作（`iT_neg` 是模板）：

```lean
-- 模板形状（来自 iT_neg）：
theorem iT_setShift {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT (n+1) (setShift ℒₒᵣ p) = setShift ℒₛₑₜ (iT n p) := by
  apply UformulaRec1.Construction.semiformula_result_induction (c := iT.construction) ...

theorem iT_substs1 {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT (n+1) (substs1 ℒₒᵣ p t) = substs1 ℒₛₑₜ (iT n p) (translateTerm t) := by
  ...
```

`setShift` / `substs1` / `IsUFormula` 版本的展开引理（`setShift_and` 等）在 Foundation
`Formula/Functions.lean` 与 `Negation.construction` 附近；`translateTerm`（项翻译）在本项目
`InternalTranslate.lean` 里（搜 `iTE` / 项翻译）。按 §2 的递归原理照 `iT_neg` 写即可。

## §5 `of_provability`（为什么不能照搬）

| API | 本地路径 | GitHub 地址 |
|---|---|---|
| `DirectInterpretation.of_provability`（`U ⊢ σ → T ⊢ π.translate σ`，**语义证明**，搬不进 𝗜𝚺₁） | `Foundation/FirstOrder/LK/Interpretation.lean:443` | `…/LK/Interpretation.lean` |
| `DirectInterpretation.interpret_theory`（只对公理成立，不覆盖任意定理） | `Foundation/FirstOrder/LK/Interpretation.lean:407` | `…/LK/Interpretation.lean` |

## §6 配套 Foundation 不完全性 / D3 参考

| API | 本地路径 | GitHub 地址 |
|---|---|---|
| `sigma_one_complete` / `bold_sigma_one_complete`（算术理论的 Σ1 完全性；本缺口**已被收窄**，无需移植） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean` | `…/DerivabilityCondition/D3.lean` |
| `provable_internalize`（仅对 `ArithmeticTheory`） | 同上 `D3.lean` | `…/DerivabilityCondition/D3.lean` |
| `DerivabilityCondition.D1`（`internalize_provability`） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D1.lean` | `…/DerivabilityCondition/D1.lean` |
| `DerivabilityCondition.D2`（`modus_ponens_sentence`） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D2.lean` | `…/DerivabilityCondition/D2.lean` |
| `CraigTrick`（Foundation 的 Craig 填充，`Sh.craig` 由此来） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/CraigTrick.lean` | `…/Syntax/CraigTrick.lean` |
| `R0/Basic`（`bold_sigma_one_completeness` 模板位置） | `Foundation/FirstOrder/Arithmetic/R0/Basic.lean` | `…/Arithmetic/R0/Basic.lean` |

## §7 目标包内关键文件（你要改的）

| 文件 | 角色 |
|---|---|
| `GodelQ/ZFC/ShCraigElimSetup.lean` | 归纳设置 + 不变量 Σ1 谓词；10 支骨架（`sorry` 待填） |
| `GodelQ/ZFC/ShCraigElimBranches.lean` | 已填 `hWk`/`hVerumIntro`；待填 `hAnd`/`hOr` 等 |
| `GodelQ/ZFC/SeqTranslate.lean` | `translateSeq` 定义与性质（10 支的公共前置） |
| `GodelQ/ZFC/SeqTranslateFormula.lean` | `isSemiformula_iT` 等（已证） |
| `GodelQ/ZFC/ShCraigElimNegLaw.lean` | `iT_neg` 一般版本（你的模板） |
| `GodelQ/ZFC/InternalTranslate.lean` | `iT` 定义、`iT_*` 相容引理、`iTE` 项翻译 |
| `GodelQ/ZFC/Z0UniBridge.lean` | 归约 `ShCraigElim → bwd`（已收据） |
| `GodelQ/ZFC/Z0Blocked.lean` | 原阻塞引理（带 `sorry`，证完 `ShCraigElim` 后此 sorry 可消除） |
| `GodelQ/ZFC/Z0Full.lean` | `zfcTr`、`models_zfcTr_iff`、`zfc_z0_full_of_D3_internalize`（已收据） |
