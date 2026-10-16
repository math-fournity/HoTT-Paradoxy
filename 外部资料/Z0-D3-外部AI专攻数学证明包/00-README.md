# Z0-D3 外部 AI 专攻数学证明包（最小、聚焦）

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
