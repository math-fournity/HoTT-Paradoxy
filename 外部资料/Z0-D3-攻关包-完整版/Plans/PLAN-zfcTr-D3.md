# zfcTr_D3_internalize 证明攻坚方案

> **性质**：攻坚方案（PLAN），不是证明。本文中的引理陈述是**待证目标**，
> 不得当作已证定理引用。最终交付必须满足 §8 验收标准。
>
> 背景：HoTT-Paradoxy `dev` 分支，包
> `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/`（MP-CG001-GODEL-Q-ZFC-Z0-FULL-001）。
> 完整形式 `𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ` 只差这一条引理
> （见包内 `CLAIM.md` §4、`GodelQ/ZFC/Z0Blocked.lean`）。

---

## 1. 目标命题（逐字）

文件 `GodelQ/ZFC/Z0Blocked.lean`：

```lean
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V))
```

读作：ZFC 证明了 τ 的翻译，则 ZFC 也证明"ZFC 证明了 τ 的翻译"这句话的翻译。
其中 `zfcTr τ := trProv.val/[⌜τ⌝]`，`trProv := "x. ∃ y, !iTDef y 0 x ∧ !(provable 𝗭𝗙𝗖) y"`（Σ₁ 公式）。

## 2. 已有什么（全部是定理，可直接用）

| 工具 | 位置 | 内容 |
|---|---|---|
| D1 `internalize_provability` | Foundation `.../Bootstrapping/DerivabilityCondition/D1.lean:27` | `T ⊢ φ → Provable T ⌜φ⌝`（引用推导再内化） |
| D2 `modus_ponens_sentence` | Foundation `.../DerivabilityCondition/D2.lean:30` | `Provable` 层面的 MP |
| `sigma_one_complete` | Foundation `.../DerivabilityCondition/D3.lean` 末 | 对**算术理论**的形式化 Σ₁ 完全性：`V ⊧ σ → Provable T ⌜σ⌝` |
| `provable_internalize` | 同上文件末 | `Provable T ⌜σ⌝ → Provable T ⌜provabilityPred T σ⌝`，但**只对 `T : ArithmeticTheory`** |
| `iT_quote` | 包内 `GodelQ/ZFC/InternalTranslate.lean:611` | `iT 0 ⌜φ⌝ = ⌜arithTrln.translate φ⌝`（C-119） |
| `models_zfcTr_iff`, `zfcTr_sigma1` | 包内 `GodelQ/ZFC/Z0Full.lean` | `V ⊧ zfcTr σ ↔ Provable 𝗭𝗙𝗖 ⌜σᵗ⌝`；`zfcTr σ` 是 Σ₁ 句 |
| C-128 归约 `zfcTr_D3_internalize_of_sigma1_bridge` | 包内 `GodelQ/ZFC/Z0Bridge.lean` | D3 ⇐ 下面的 bridge 前提（已证） |

`Provable` 的定义（`Foundation/.../Syntax/Proof/Basic.lean:541`）：
```lean
def Provable (φ : V) : Prop := ∃ d, Proof T d φ
```
是**外部**的存在量词：V 中存在一个推导编码。

## 3. 缺口精确形状：bridge（C-128 的前提）

```lean
bridge : ∀ {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] {σ : ArithmeticSentence},
  ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ → Provable 𝗜𝚺₁ (⌜σ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)
```

**关键简化**（本方案的核心观察）：C-128 实际只把 bridge 用在 `σ := zfcTr τ` 上，
而此时输入的 `Provable 𝗜𝚺₁ ⌜σ⌝` 是由 `hv : V ⊧ zfcTr τ` 经 `sigma_one_complete` 得到的。
既然 `sigma_one_complete`（真 ⇒ 内部编码）已有，bridge 的输入可以直接取更强的
`V ⊧ σ`，得到**更弱、更容易**的待证目标：

```lean
-- Bridge′（最小缺口）
theorem bridge_sigma1_translate
    {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    {σ : ArithmeticSentence} (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ)
    (hv : V↓[ℒₒᵣ] ⊧ σ) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)
```

它蕴涵原引理（替换版 Z0Bridge，三行）：

```lean
theorem zfcTr_D3_internalize_of_bridge'
    (bridge : ∀ {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] {σ : ArithmeticSentence},
      ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ → V↓[ℒₒᵣ] ⊧ σ → Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V))
    {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence) (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) :=
  bridge (zfcTr_sigma1 τ) ((models_zfcTr_iff V τ).mpr h)
```

之后 `zfc_z0_full_of_D3_internalize`（Z0Full.lean，已证）直接给出
`𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`，无需其他东西。

## 4. 为什么现有工具填不上这个缺口

1. **`of_provability` 是语义的**（`Foundation/FirstOrder/LK/Interpretation.lean:443`）：
   ```lean
   lemma of_provability {σ : Sentence L₂} (h : U ⊢ σ) : T ⊢ π.translate σ := by
     apply Theory.Proof.complete_on_eq_models.{_, 0}   -- ← 完备性定理
     intro M _ _ _ hT
     exact Model.translate_iff.mpr <| models_of_provable (π.model_models_theory hT) h
   ```
   它经由"所有模型都满足"得到 `⊢`，**没有给出证明编码上的可计算函数**，
   因此没有任何东西可搬进 𝗜𝚺₁ 去处理 V 内部（可能非标准）的证明编码。
   注意 `DirectInterpretation.interpret_theory`（同文件 :407）只对**公理**
   `∀ φ ∈ U, T ⊢ trln.translate φ` 成立，不覆盖任意定理。

2. **`provable_internalize` 只对算术理论**：`variable (T : ArithmeticTheory)`，
   ZFC 不是算术理论，不能直接套用。

3. **`sigma_one_complete` 给错理论的编码**：它给出 `Provable 𝗜𝚺₁`（V 内部的
   算术证明编码），而我们要的是 `Provable 𝗭𝗙𝗖` 编码。两种编码之间没有现成的桥。

## 5. 主攻路线：经翻译的 Δ₀ 完全性（最小 Σ₁ 步骤）

**数学思想**：不去翻译任意的 𝗜𝚺₁ 证明（那需要形式化的解释定理，大工程），
而是利用 bridge′ 的输入是**真**的 Σ₁ 句这一事实，走 Δ₀ 完全性：

- σ 是 Σ₁，V ⊧ σ ⇒ 取内证人 `w : V` 使 `V ⊧ θ(w)`，其中 `σ = ∃x θ(x)`，θ 是 Δ₀。
- **Δ₀ 句子是可判定的**：θ(w) 为真 ⇒ 沿翻译在 ZFC 中可证，且证明从
  (⌜θ⌝, w) **一致可计算**（对 θ 的结构做外部归纳；θ 是标准公式）。
- 最后一次 ∃-引入得到 `Provable 𝗭𝗙𝗖 ⌜translate σ⌝`。

这正是 Foundation 的 `bold_sigma_one_complete`
（`.../DerivabilityCondition/D3.lean`，对 Hierarchy 的归纳证明形式化 Σ₁ 完全性）
**移植到翻译目标**的结果：把那里的目标 `T.internalize V ⊢ ⌜φ⌝`（T 算术）
换成 `Provable 𝗭𝗙𝗖 ⌜translate φ⌝`，把那里的 numeral/项引理换成翻译版。
`bold_sigma_one_complete` 的证明结构（`term_complete`、`numeral_add/mul/lt`、
`ball_intro` 处理有界量词的内归纳）可逐段对照移植——这是本方案要求精读它的原因。

### 5.1 引理分解（按依赖顺序）

**L1（翻译的原子完全性）**。对 numeral `𝕹 m`、`𝕹 n`：
真原子句 `𝕹 m ≐ 𝕹 n`、`𝕹 m <' 𝕹 n` 的翻译是 ZFC 定理，且证明编码
在 IΣ₁ 内关于 (m, n) 一致可得。基础：`arithTrln` 把算术解释在 ω 上
（`GodelQ/ZFC/ArithInterp.lean:68` 的 `DirectTranslation`），ZFC 证明 ω 满足
足够的算术（Q 的翻译实例由已有的 `interpret_theory` 对公理给出）。

**L2（翻译的项求值）**。`term_complete` 的翻译版：
`Provable 𝗭𝗙𝗖 ⌜translate( t[w̅] ≐ 𝕹(t.valb w) )⌝`，
对项 t 做外部归纳，用 L1 处理 `+`、`×` 的 numeral 运算。

**L3（Δ₀ 完全性，核心）**。
```lean
lemma delta0_translate_complete {V} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    {θ : ...} (hθ : Δ₀ θ) {w} (hw : V ⊧ θ(w)) :
    Provable 𝗭𝗙𝗖 (⌜(arithTrln.translate θ)(𝕹 w)⌝ : V)
```
对**标准**公式 θ 做外部结构归纳：
- 原子：L1+L2；
- `∧ ∨ → ¬`：命题步骤，翻译与连接词可交换（直接翻译的定义），用 D2 的
  `modus_ponens_sentence` 做内部 MP；
- 有界 `∃x<t`：由内证人 `u < t(w)`、`V ⊧ θ₁(u)`，经 IH 得编码，
  再一次有界 ∃-引入（需 ZFC ⊢ 𝕹 u ∈ ω，numeral 引理）；
- 有界 `∀x<t`：设 `b := t(w) : V`（可能非标准），在 IΣ₁ 内对 `u ≤ b`
  做 Σ₁ 归纳，证 `∀ u ≤ b, Provable 𝗭𝗙𝗖 ⌜∀x∈ω (x < 𝕹 u → translate θ₁)⌝`。
  这是对照 `bold_sigma_one_complete` 的 `hBall` 情形（`ball_intro`）最需要
  小心的一步：归纳谓词是关于证明编码存在的 Σ₁ 命题，IΣ₁ 的 Σ₁ 归纳恰好够用。

**L4（∃-引入与量词相对化）**。
`translate (∃x θ) = ∃x∈ω translate θ`（直接翻译定义，应已有或易证），
由 L3 的编码经 ∃-引入得 `Provable 𝗭𝗙𝗖 ⌜translate (∃x θ)⌝`。

**L5（组装 Bridge′）**。σ Σ₁ 取范式 `∃x θ`（Δ₀ θ；Foundation 应有 Σ₁ 范式，
或直接对 `ℬ.Hierarchy 𝚺 1` 做归纳如 `bold_sigma_one_complete` 那样），
由 `hv : V ⊧ σ` 取内证人 w，L3+L4 即得。

### 5.2 每步要查的精确位置

- `bold_sigma_one_complete` 证明全文：Foundation `.../DerivabilityCondition/D3.lean`
 （179 行；连同 `PeanoMinus`/`EquationalTheory` 约 1080 行支撑）——**逐行精读**，
  它是 L3 的模板。
- `numeral_add/mul/lt/ne/nlt`、`term_complete`：同文件 —— 需写 ZFC/翻译版（L1/L2）。
- `tprovable_tquote_iff_provable_quote`：在 `Provable` 与 `T.internalize V ⊢`
  之间转换（D2 的证明展示了用法）。
- `iT_quote`（InternalTranslate.lean:611）：编码层 `iT 0 ⌜φ⌝ = ⌜translate φ⌝`，
  用于把内部翻译的编码与外部 `translate` 对齐。
- `arithTrln` 定义：`GodelQ/ZFC/ArithInterp.lean:68`（`DirectTranslation 𝗭𝗙𝗖 ℒₒᵣ`）；
  注意 z0-full 包用的是自己包内的版本，不要混用其他包的同名定义。

## 6. 备选路线（若 5.1 卡住）

**R-备：形式化语法解释定理**。定义从 𝗜𝚺₁ 推导编码到 ZFC 推导编码的可计算
翻译函数 F，在 IΣ₁ 内证其正确性（对推导结构的内归纳），然后 bridge 的原形式
（`Provable 𝗜𝚺₁` 输入）直接可得。这是更 general 的定理，但工作量显著更大
（要处理 𝗜𝚺₁ 归纳规则的翻译：ZFC 用 ω 上的归纳模拟），只建议在 Δ₀ 路线被证
伪不可行时启用。

**不建议的路线**：
- 试图把 `provable_internalize` 推广到 ZFC：需要集合论语言的 Σ₁ 完全性，
  比本方案更难。
- 在 ZFC 内证 `Prov_ZFC(⌜τᵗ⌝) ↔ (𝔅τ)ᵗ` 再用 D2：同样需要翻译与可证性谓词
  可交换的内部证明，难度不低于本方案。

## 7. 给执行 AI 的起点与环境

1. **起点文件**：先读 `GodelQ/ZFC/Z0Blocked.lean`（目标）、`GodelQ/ZFC/Z0Bridge.lean`
   （归约思想）、`GodelQ/ZFC/Z0Full.lean`（`zfcTr`、`models_zfcTr_iff`），
   再读 Foundation `.../DerivabilityCondition/D3.lean` 全文。
2. **工具链 pin**（`LEAN_TOOLCHAIN.json` / `MATHLIB_CLOSURE.json`）：
   Lean 4.34.0（commit `293d5d0c`）、Mathlib `5ed29652`、Foundation `1fb01b72`。
   新引理必须在此外部环境编译，**不得修改** Foundation/Mathlib 源码。
3. **已备好的 90% 环境**：本机 `~/workspace/toolchain-cache/` 有精确版 Lean、
   Mathlib 全量 8908 olean、Foundation 137/181 模块 olean、移植版顺序编译脚本
   `build_foundation.py`。内存 ≥16G 的机器上一条命令可复现完整环境；
   当前唯一已知障碍是 `...Bootstrapping.Syntax.Term.Basic` 在 8G 机器上 OOM
   （内存墙，与数学无关）。
4. **只能加文件**：新引理写成包内新文件（如 `GodelQ/ZFC/Z0BridgeDelta0.lean`），
   按包内既有顺序加入编译驱动；**不得**把带 `sorry` 的文件列入收据源。

## 8. 验收标准（F-011 门禁，执行 AI 必须满足）

1. 精确命题（Bridge′ 及组装后的 `zfcTr_D3_internalize`）落源码，无 `sorry`；
2. `#print axioms` 仅含 `propext`、`Classical.choice`、`Quot.sound`；
3. 正运行（24+新增文件顺序编译 exit 0）+ 至少一个负控制（内核应拒绝的变体）；
4. 正式 run receipt（`verify_cg001_run.py --rerun` 通过）；
5. 更新 CG-001 证据索引、`HoTT/CLAIM_EVIDENCE_MATRIX.md`、`形式化追踪/`。
