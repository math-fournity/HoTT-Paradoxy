# W8 下一单元：V 内部的语法解释定理（← 方向的精确任务规格）

> 状态：`SPECIFIED_NOT_STARTED`。2026-10-10 由 WorkBuddy 会话（Agent 模式）写下。
> 本文件只规定"要证什么、缺什么、按什么顺序做"，**不声称任何进展**。
> 依据：`形式化追踪/01-有哥德尔路线/02-Z0-条件形式与剩余三步.md` 的末两节、`HoTT/formal/claude-cg001/godel-q-zfc-z0-full/CLAIM.md` §4/§8。

## 1. 要证的命题

唯一目标（三者等价，任选其一作为入口）：

```lean
-- (a) 缺口本身
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V)

-- (b) C-128 的 bridge（(a) 由它 + sigma_one_complete 得到）
--     ∀ V σ, Σ1 σ → Provable 𝗜𝚺₁ ⌜σ⌝ → Provable 𝗭𝗙𝗖 ⌜σᵗ⌝

-- (c) keyE 的 ← 方向
--     𝗜𝚺₁ ⊢ provabilityPred Sh.craig σ 🡒 zfcTr σ
```

**(c) 是最容易陈述、也最容易卡住的**：它是"V 内部的语法解释定理"。

## 2. 为什么它绕不开（已核实的障碍）

| 现成工具 | 为什么不够 |
|---|---|
| `DirectInterpretation.of_provability`（`LK/Interpretation.lean:443`） | 经 `Theory.Proof.complete_on_eq_models` —— **完备性定理，语义**；不产生非标准 V 里的证明编码 |
| `WeakerThan.pbl` | 元层；搬不进非标准 V |
| `Derivable.of_ss`（`Syntax/Proof/Basic.lean:841`） | **只在同一语言内**弱化（`T.Δ₁Class ⊆ U.Δ₁Class`），ℒₒᵣ → ℒₛₜ 跨不过去 |
| `Derivation.sound`（`Syntax/Proof/Coding.lean:336`） | **只对 `d : ℕ`（标准）**成立；V 内部的 d 可能非标准 |
| `T.standardProvability.HBL3` | 只对 `ArithmeticTheory` + `𝗣𝗔⁻ ⪯ T`；`𝗭𝗙𝗖` 不是算术理论 |

## 3. 缺的零件（按依赖顺序）

**第 1 层：`arithTrln.translate` 的语法交换律**（Foundation 里只有语义版 `Model.eval_translate_iff` 等，没有语法版）

需要证明 `translate` 与下列运算交换（或给出其显式形状）：
`neg`、`⋏`、`⋎`、`∀¹`（→ 相对化到 `domain`）、`∃¹`、`subst`、`shift`、`free`、`setShift`、`Rew.emb`。

这一层是纯语法、与 𝗭𝗙𝗖 无关，可以独立做、独立验收。

**第 2 层：推导翻译函数**（V 内部，原始递归）

给出 `derivTranslate : V → V`，把一条 `Sh.craig` 推导编码送到一条 `𝗭𝗙𝗖` 推导编码，并证明：
`Derivation Sh.craig d → Derivation 𝗭𝗙𝗖 (derivTranslate d)`，且 `fstIdx` 被送到对应翻译。

规则逐个处理（规则集见 `Syntax/Proof/Basic.lean` 的 `axLGraph`、`verumIntroGraph`、`andIntroGraph`、`orIntroGraph`、`allIntroGraph`、`exsIntroGraph`、`wkRuleGraph`、`shiftRuleGraph`、`cutRuleGraph`、`axmGraph`）：
- `axm`：公理 `φ ∈ Sh.craig`。由 `mem_craig_codes_iff` 得 `φ = ρ.padding s` 且 `reWitness(s, ⌜ρ⌝)`，再由 `reWitness_spec` 与 `Sh.reCh` 的语义得 `zfcTr ρ`，即 V 手里**已有** `ρᵗ` 的一条 𝗭𝗙𝗖 推导；再用 `ρ.padding s = ρ ⋏ ⊤ ⋏ …` 在 𝗭𝗙𝗖 里把它接回来。**这是唯一用到 𝗭𝗙𝗖 的地方。**
- 逻辑规则：由第 1 层 + `domain_nonempty` / `func_defined` 两条 `arithTrln` 义务得到。

**第 3 层：组装**

`bridge` / `keyE←` / `zfcTr_D3_internalize`，然后接 `Z0Full.zfc_z0_full_of_D3_internalize`，最后按 `BUILD.md` 出正式收据（`capture_run.py`，含负控制）。

## 4. 已知的"看起来能省但省不掉"的坑

1. **`Sh.reCh` 不是 `trProv`**。实测：`Sh.reCh.val` 展开为 `mkSigma (codeOfREPred (Encodable.encode '' Sh))`，`trProv.val` 展开为 `mkSigma (∃¹ iTDef/[#0,↑0,#1] ⋏ (provable 𝗭𝗙𝗖)/[#0])`。两者**不是**同一个公式（`rfl` 失败），只是内容相同。所以第 2 层 `axm` 那一支要先补一条"`codeOfREPred` 的一般 V 表示引理"（`codeOfREPred_spec` 只在 ℕ 层）。
2. **不能只做 → 方向**。`zfcTr.HBL3` 需要两个方向；只做 → 只能得到 `zfcTr σ → □_{Sh.craig}(zfcTr σ)`，仍差 `□_{Sh.craig}(zfcTr σ) → zfcTr (zfcTr σ)`。
3. **不能把 `𝔅 := 𝗭𝗙𝗖.standardProvability` 搬到 `T₀ = 𝗜𝚺₁`**：`Provability T₀ T` 要求 `T₀ ⪯ T`，而 `⪯` 是同语言关系，`𝗜𝚺₁ ⪯ 𝗭𝗙𝗖` 类型不过。
4. **`Diagonalization 𝗭𝗙𝗖` 这条岔路已看过**：即便有，`𝔅 : Provability 𝗭𝗙𝗖 𝗭𝗙𝗖` 需要一条**集合论语言**的可证性公式，而 Foundation 的 `provabilityPred` 是算术公式（`Semisentence ℒₒᵣ 1`），套不上。

## 5. 环境与迭代

```bash
# 工作副本（不要直接改收据源）
cp -R <repo>/HoTT/formal/claude-cg001/godel-q-zfc-z0-full /tmp/d3build/src/
# 当前宿主不允许嵌套沙箱，用 devbuild.py 的无沙箱变体
python3 -B /tmp/d3build/devbuild_ns.py /tmp/d3build/src/godel-q-zfc-z0-full <模块…>
```
- Lean 4.34.0；Foundation 源码 `/Volumes/D/HoTT-toolchain-cache/foundation-src`（`1fb01b72`）；
  olean 在 `foundation-build-1fb01b72-v4.34.0/`**`lib/lean`**（不是 `.lake/build/lib/lean`）。
- 全链 24 模块冷启动约 60 s，增量几乎瞬时。模块清单见包内 `BUILD.md`。
- 探针文件（`GodelQ/ZFC/Probe*.lean`）**不进收据源**。

## 6. 停止条件

- 若第 1 层做完后第 2 层被证明不可行（例如规则翻译需要 𝗭𝗙𝗖 内的归纳而 𝗜𝚺₁ 供不起），
  照实写明卡点，把最小可续状态留在这个文件里，**不要**为了"完成"收窄命题。
- 无论做到哪一层，`C-120` 的影子形式（`𝗭𝗙𝗖 ⊬ (Sh.craig.consistent)ᵗ`）无条件成立，不受影响。
