# CG001-C-121、C-122、C-128：Z0 的内部化只差一条内部解释；其余前提与一条归约都是定理

> **证明包**：`MP-CG001-GODEL-Q-ZFC-Z0-FULL-001`。
>
> **目标包**：CG-007（`.claude/goals/CG-007-formalization-completion/`），单元 W8；本机 Codex 会话接手 Claude Opus 5.5 会话 d58e0c0d 中断的同一单元，2026-10-09。授权原话（2026-10-08）：“按照你的想法进行优先级安排，完成后续所有“形式化和机器证明”工作。”
>
> **理论变体**：同 `../godel-q-zfc-z0-translate/`：Lean 4（v4.34.0）加 Mathlib（`5ed29652`）与 Foundation（`1fb01b72`），经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。
>
> **身份**：机器证明（范围见 §4、§7、§8）。把 C-120 读成“𝗭𝗙𝗖 证明不了 Con(𝗭𝗙𝗖)”所差的最后一步，被固定成**一条**精确的 Lean 命题；C-128 再把这条命题在 `Type` 宇宙上归约到一条更窄的内部解释。除此之外的全部前提都是定理。D3 本身仍未证。

## 0. 位置

- C-120 已给出 `𝗭𝗙𝗖 ⊬ (Sh.craig.consistent)ᵗ`（不带前提）。这里的一致性句 `Sh.craig.consistent` 是 Foundation 用选择挑出的某个 Σ1 定义（包内补注见 `../godel-q-zfc-z0-translate/REVISIONS.md`），它在 𝗜𝚺₁ 内部与 Con(𝗭𝗙𝗖) 的关系无从推理。
- 本包换一条显式的路：把“𝗭𝗙𝗖 证明 x 的翻译”本身当作可证性谓词，即 `𝔅Z(x) := Provable 𝗭𝗙𝗼 (iT 0 x)`，作为 `Sh` 的 `Provability 𝗜𝚺₁ Sh`。它没有选择，逐字由 C-119 的内部翻译 `iT` 给出。
- 走 Foundation 的抽象第二定理（`ProvabilityAbstraction.con_unprovable`）。它要的条件逐条核对：D1、D2 成为定理；`𝗜𝚺₁ ⪯ Sh` 是 C-110；`Sh` 一致是 C-103；对角化是 Foundation 对 𝗜𝚺₁ 自带的；**只剩 D3**。
- D3 被固定成 `GodelQ/ZFC/Z0Blocked.lean` 的 `zfcTr_D3_internalize`，它带未证标记，因此不是本运行的编译源。`Z0Full.zfc_z0_full_of_D3_internalize` 表明：这条引理一旦成立，完整形式 `𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ` 立即随之成立，无需别的东西。

## 1. 精确命题（类型逐字见 `GodelQ/ZFC/Z0Full.lean`、`GodelQ/ZFC/Z0Blocked.lean`）

| 编号 | 定理 | 内容 |
|---|---|---|
| CG001-C-121 | `GodelQ.Z0Full.zfcTr` 及随之四条 | (1) `𝔅Z := TrProvable x := Provable 𝗭𝗙𝗼 (iT 0 x)` 是 `Provability 𝗜𝚺₁ Sh`，其 Σ1 公式 `trProv`；`V ⊧ zfcTr σ ↔ Provable 𝗭𝗙𝗼 ⌜σᵗ⌝`。(2) D1（`zfcTr.bew_def`，由 C-119 的 `iT_quote` 与 Foundation 的 `internalize_provability`）。(3) D2 = HBL2（`modus_ponens_sentence`）。(4) `𝗜𝚺₁ ⊢ zfcTr.con 🡘 (𝗭𝗙𝗖.consistent)`（一致性句在 𝗜𝚺₁ 中等价）。(5) `zfcTr σ` 是 𝚺₁ 句。(6) 正对照：D3 在标准模型 ℕ 中成立 |
| CG001-C-122 | `GodelQ.Z0Full.zfc_z0_full_of_D3_internalize` | 阻塞引理 `zfcTr_D3_internalize`（见 §4）一旦成立，`𝗭𝗙𝗼 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`，即 Z0 的完整形式 |
| CG001-C-128 | `GodelQ.Z0Bridge.zfcTr_D3_internalize_of_sigma1_bridge`、`zfc_z0_full_of_sigma1_bridge` | 若每个 `Type` 层的 𝗜𝚺₁ 模型都能把 Σ1 算术句的内部证明编码沿 `arithTrln` 变成 𝗭𝗙𝗖 证明编码，则该宇宙上的 D3 形状成立，并且 `𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`。见 §8 |

`Sh_z0_full`、`zfc_z0_full` 是 C-122 在 D3 作为实例给出时的两个特例，与 C-122 同一次编译。

## 2. 证明

- **𝔅Z 的构造**：`trProv : 𝚺ᴬ₁.Semisentence 1 := “x. ∃ y, !iTDef y 0 x ∧ !(provable 𝗭𝗙𝗼) y”`。`𝚺ᴬ₁-Predicate (TrProvable : V → Prop) via trProv` 由 `iT_quote`（C-119）给出：`iT 0 ⌜σ⌝ = ⌜σᵗ⌝`。
- **D1**：`Sh ⊢ σ → 𝗜𝚺₁ ⊢ zfcTr σ`。经完备性化为每个 𝗜𝚺₁ 模型 V 中 `V ⊧ zfcTr σ ↔ Provable 𝗭𝗙𝗼 ⌜σᵗ⌝`，再由 Foundation 的 `internalize_provability` 从 `𝗭𝗙𝗼 ⊢ σᵗ` 得到。
- **D2**：`𝗜𝚺₁ ⊢ zfcTr (σ 🡒 τ) 🡒 zfcTr σ 🡒 zfcTr τ`。同样经完备性，两侧都用 `models_zfcTr_iff` 化成 `Provable 𝗭𝗙𝗼`，再用 Foundation 的 `modus_ponens_sentence`。
- **一致性句等价**：`zfcTr.con = ∼zfcTr ⊥`，而 `zfcTr ⊥ = Provable 𝗭𝗙𝗼 (iT 0 ⌜⊥⌝)`；`iT 0 ⌜⊥⌝ = ⌜⊥⌝` 由 `iT_quote` 与 `⊥` 的翻译。所以 `zfcTr.con` 与 Foundation 的 `𝗭𝗙𝗖.consistent` 在每个模型中都等价于 `¬ Provable 𝗭𝗙𝗼 ⌜⊥⌝`。
- **`zfcTr σ` 是 Σ1 句**：`trProv` 由 `mkSigma` 给出，`/[⌜σ⌝]` 保持层级（`Bounding.Hierarchy.rew`）。
- **正对照**：D3 在 ℕ 中成立，因为真的 Σ1 句子被 𝗭𝗙𝗼 证明（D1）加上 `Sh ⊢ σ ↔ 𝗭𝗙𝗼 ⊢ σᵗ`。
- **完整形式**：`con_unprovable (𝔅 := zfcTr)` 需要 `[zfcTr.HBL]`（= HBL2 + HBL3）与 `Sh` 一致。HBL2 是定理；HBL3 由阻塞引理在模型层逐点给出（`zfc_z0_full_of_D3_internalize` 的证明）。

## 3. 负控制

本包没有负控制运行：正结果全部以一条显式前提为条件，D3 的正对照已在同一运行中机器核对。阻塞引理本身不进入收据源，因此不存在“应当被拒绝而未拒绝”的目标。这与 CG-007 其它单元（每个单元都有至少一个负控制）不同，记在此处。

## 4. 还差什么：唯一阻塞引理

`GodelQ/ZFC/Z0Blocked.lean:zfcTr_D3_internalize`，逐字为：

```lean
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗼 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗼 (⌜arithTrln.translate (zfcTr τ)⌝ : V)
```

读作：**“𝗭𝗙𝗖 证明了 τ 的翻译，那么 𝗭𝗙𝗼 也能证明‘𝗭𝗙𝗼 证明了 τ 的翻译’这句话的翻译。”** 这就是 Hilbert–Bernays 条件 D3 在这个显式谓词下的形状，即**经翻译的形式化 Σ1 完全性**。

- Foundation 对算术理论的 D3 有完整机器证明（`Bootstrapping/DerivabilityCondition/D3.lean`，179 行，加 `PeanoMinus`/`EquationalTheory` 共约 1080 行）；它服务的是 `T.standardProvability`（谓词 `Provable T ⌜σ⌝`，T 是算术理论）。本处谓词是 `Provable 𝗭𝗙𝗼 (iT 0 x)`，作用对象是**翻译后**的公式，不能直接套用。
- 需要的这一步在数学上是“证明的内部翻译”：给出一个 𝗜𝚺₁ 内的证明搜索，把一条 𝗭𝗙𝗼 证明变成“𝗭𝗙𝗼 证明这句话”的 𝗭𝗙𝗼 证明。Foundation 的 `LK/Interpretation.lean:443 of_provability`（`U ⊢ σ → T ⊢ π.translate σ`）是用**完备性定理**证明的语义证明，其中没有可搬进 𝗜𝚺₁ 的语法翻译。
- 因此这条引理是实的、可交给下一个工作单元或外部复核的精确缺口。它不是措辞问题：把 D3 写成别的形式也绕不过同一内容。
- C-128 不取消这条缺口。它只证明：在 `Type` 宇宙上，缺口可以再收成“Σ1 算术证明编码沿 `arithTrln` 变成 𝗭𝗙𝗖 证明编码”。`Z0Blocked` 的 `Type*` 陈述比 C-122 实际消费的前提更强，C-128 不对它作声称。

### 4.1 实证确认（2026-10-10 机器检验）：缺口为实，且现有 Foundation API 关不上

本包在 2026-10-10 用本地驱动（去掉 `zfc_lean_check.py` 的 `sandbox-exec`，本环境禁止它；其余钉扎与禁用标记检查保留）对缺口做了两次机器检验：

1. **基线重放（exit 0）**：把本包除 `Z0Blocked.lean`（`sorry`）与 `Z0Probe.lean`（既有错误）外的 25 个收据文件编译，全部 rc=0，`PINNED_INPUT_OK modules=1893`。这说明 Z0 装置中除 D3 之外的全部内容都在钉扎的 Foundation/Mathlib 上机器检验通过；缺口是孤立的，不是别处的连带错误（本地重放了 2026-10-09 收据 `20261009-CG001-GODEL-Q-ZFC-Z0-FULL-01` 的源集）。
2. **探针尝试（exit 1）**：新增诊断文件 `GodelQ/ZFC/Z0D3Attempt.lean`，直接 `exact internalize_provability (V := V) h` 试图关闭缺口，在 53 行得到类型不匹配：参数 `h` 的类型是 `Provable 𝗭𝗙𝗖 ⌜arithTrln.translate τ⌝`（前提句），但 `internalize_provability` 要的是 `𝗭𝗙𝗖 ⊢ arithTrln.translate (↑zfcTr τ)`（结论句）。前提句 `translate τ` 与结论句 `translate (zfcTr τ)` 是**两句不同的句子**；`internalize_provability {φ} : T ⊢ φ → Provable T ⌜φ⌝`（`D1.lean:27`，对一般 `T : Theory L` 且 `[T.Δ₁]`，故 ZFC 也满足）只能把**同一句** φ 重写，无法合成“包裹了 `iTDef` + `provable 𝗭𝗙𝗖`”的结论句。

**被证伪的路线**（已用 Foundation 源码逐字核对）：

- `provable_D3`（`StandardProvability.lean:71`）位于 `section arithmetic`（`variable {T U : ArithmeticTheory}`，第 60 行），要求 `T : ArithmeticTheory`；`𝗭𝗙𝗖` 是 `Theory ℒₛₑₜ`（集合论），故 `provable_D3 (T := 𝗭𝗙𝗖)` 是**类型错误**。先前“用 standardProvability 的 D3 经桥接关闭缺口”的假设被证伪。
- `sigma_one_complete`（`D3.lean:170`）与 `provable_sigma_one_complete`（`StandardProvability.lean:64`）只对**算术理论**定义；Foundation 没有集合论版本的 Σ1 完全性。
- `Z0Bridge.lean` 的 `bridge` 前提（C-128）本身就是同一个“内部化 Σ1 完全性”缺口的再收窄，并未给出证明。

**结论**：缺口为**实**——它是 ZFC 的**内部化 Σ1 完全性 / HB-Löb 可导性条件 D3**（针对集合论可证性谓词 `Provable 𝗭𝗙𝗖 (iT 0 x)`）。它在数学上很可能可形式化（需要在 Foundation 中补出集合论可证性谓词的 Σ1 完全性），但**无法靠复用现有 Foundation API 完成**。因此本包不产出机器证明，不把 `𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)` 作为已证数学结论交付。诊断证据见 `HoTT/verification/runs/20261010-CG001-Z0-D3-GAP-DIAGNOSTIC-01/`。

### 4.1.1 补充（2026-10-11）：缺口精确到缺失的 `Theory.Δ₁ Sh` 实例 + 诚实降格重验证

- **决定性探针 `GodelQ/Probe_d3final.lean`**（`#check Theory.Δ₁ Sh` vs `#check provable_D3 (T := Sh)`）：前者给出 `Theory.Δ₁ Sh : Type`（类**存在**），后者报 `error(lean.synthInstanceFailed): failed to synthesize instance of type class Theory.Δ₁ Sh`。说明 `zfcTr_D3_internalize` 经 `Sh_provable_iff`（`zfcTr σ ↔ provabilityPred Sh σ`）归约为 `provable_D3 (T := Sh)`，而该定理要求 `[Theory.Δ₁ Sh]`——即 **ZFC 的 Σ₁ 完全性**，在 Foundation（commit `1fb01b72`）中尚未形式化。这是 Z0 缺口的**精确 API 层定位**（CG-008 核心内容），不是措辞问题。
- **诚实降格重验证（2026-10-11，本地驱动 `/tmp/build_z0.py`，去 sandbox-exec，保留钉扎与禁用标记检查）**：
  - `GodelQ/ZFC/Z0Blocked.lean`（含精确 `sorry` 命题、禁用标记检查）：`## lean ... (rc=0)` + `warning: declaration uses 'sorry'`——精确命题类型可检查、缺口良定义；
  - `GodelQ/ZFC/Z0Full.lean` / `GodelQ/ZFC/Z0Bridge.lean`（**启用**禁用标记检查，须无 `sorry`）：均 `rc=0`、无 `sorry`——收据文件干净，降格未给装置引入新错误。
  - 捕获见 `HoTT/verification/runs/20261010-CG001-Z0-D3-GAP-DIAGNOSTIC-01/`（`stdout_reverify_Z0Bridge.txt` / `stdout_reverify_Z0Blocked.txt` / `stdout_probe_d3final.txt`）。
- **状态不变**：不产出 Z0 机器证明收据；`zfcTr_D3_internalize` 保留 `sorry`；闭合需 CG-008 形式化 `Δ₁ Sh`（集合论 Σ₁ 完全性）或 `Z0Bridge.bridge`。

### 4.1.2 补充（2026-10-11）：包内廉价传递尝试——坍缩为同一 D3 缺口，已诚实降格

按前期方向评估，尝试「包内廉价传递」：从已无条件证明的影子形式
`zfc_z0 : 𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val)`
经一致性等价桥梁 `𝗜𝚺₁ ⊢ Sh.craig.consistent.val ↔ 𝗭𝗙𝗖.consistent`
推出完整形式 `𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`，不碰 Foundation 本体。

两次机器检验（本地驱动 `/tmp/build_z0.py`，去 sandbox-exec，保留钉扎与禁用标记检查）：

1. **直接尝试（已证伪）**：用 `complete 𝗜𝚺₁` 证明该桥梁。Lean 无法闭合目标，
   静默以 `sorry` 回填，`#print axioms` 报 `sorryAx`（2026-10-11 早期会话实测）。
   桥梁不可证——它等于 ZFC 的 Σ₁ 内部化 / D3（`Theory.Δ₁ Sh` 缺失）。
2. **条件形式尝试（诚实降格）**：把桥梁作为显式前提写 `zfc_z0_full_of_bridge`，
   主体需 `cl_prover [e, hSh]` 在 `Sh` 内由 `Sh ⊢ (A ↔ B)`、`Sh ⊢ B` 推 `Sh ⊢ A`；
   因 `e` 是经 `WeakerThan.pbl` 包裹的**抽象**前提，`cl_prover` 在 12 000 000
   心跳预算下仍确定性超时（`build2.log`）。该条件定理数学正确，但当前 Foundation
   的 `cl_prover` 对抽象等价比无法在合理预算内闭合。

结论：廉价传递**不能**闭合 Z0，与 D3 / `Theory.Δ₁ Sh` 同一缺口；不保留任何伪造收据。
诚实处置：`GodelQ/ZFC/Z0Final.lean` 现仅含 D3 链接条件定理 `zfc_z0_full_of_D3_cheap`
（编译 rc=0，`#print axioms` 仅 `[propext, Classical.choice, Quot.sound]`，无 `sorryAx`），
文件头注释完整记录上述负结果。证据见 `HoTT/verification/runs/2026-10-11-z0final-conditional/`
（build1–build3.log：build1/build2 = 条件尝试 cl_prover 超时且无 sorryAx；build3 = 精简后 rc=0 干净编译）。

**状态不变**：不产出 Z0 机器证明收据；完整形式仍阻塞于 CG-008（集合论 Σ₁ 完全性）。

### 4.1.3 补充（2026-10-11，Claude 会话 77d1ad24，worktree `dev-ef7e5239`）：缺口改述为 `HBL3`，并证明它**不可能**靠补实例绕过

§4.1.1 把缺口定位为「缺失的 `Theory.Δ₁ Sh` 实例」。**方向正确，但那条路不可能走通**——
本轮机器查实了为什么。三条实质结果：

**（一）缺口 = `zfcTr.HBL3`。** Foundation 有抽象可证性框架
（`Incompleteness/ProvabilityAbstraction/Basic.lean:25-93`）：

```lean
structure Provability (T₀ : Theory L₀) (T : Theory L) where
  prov : Semisentence L₀ 1
  bew_def {σ} : T ⊢ σ → T₀ ⊢ prov/[⌜σ⌝]                        -- D1
class HBL3 (𝔅 : Provability T₀ T) where
  D3 {σ : Sentence L} : T₀ ⊢ 𝔅 σ 🡒 𝔅 (𝔅 σ)                    -- ← 缺口
instance [∀ σ, 𝔅.FormalizedCompleteOn (𝔅 σ)] : 𝔅.HBL3 := ⟨by simp⟩
```

`zfcTr : Provability 𝗜𝚺₁ Sh` 已建成（`Z0Full.lean:60`，带 D1），
`HBL3.D3` 经 `models_zfcTr_iff` 展开**正是** `zfcTr_D3_internalize`。
故缺口 = 建成 `∀ σ, zfcTr.FormalizedCompleteOn (zfcTr σ)`。
证据：`GodelQ/ZFC/CG008HBL3.lean`、`CG008Final.lean`。

**（二）`Sh.Δ₁` 不可能成立——这是 G1 的必然，不是缺实例。**
`Δ₁` 的字段（`Bootstrapping/Syntax/Theory.lean:16`）含
`mem_iff : ∀ φ, ℕ ⊧/![⌜φ⌝] ch.val ↔ ∃ σ ∈ T, φ = σ`——**双向**，要精确刻画公理集。
而 `Sh := {σ | 𝗭𝗙𝗖 ⊢ arithTrln.translate σ}` 的「公理」是 𝗭𝗙𝗖 的**定理**，
其成员判定是 Σ₁（`provable 𝗭𝗙𝗖`）、补是 Π₁。
**若 `Sh.Δ₁` 成立 ⇒ 𝗭𝗙𝗖 定理集递归 ⇒ 与 G1 矛盾。**
证据：`GodelQ/ZFC/CG008Delta1Wall.lean`。

**（三）跨语言墙：两条路各堵一半，堵的是同一件事。**

| 路 | 结构 | 语言 | `Δ₁` | `HBL3` |
|---|---|---|---|---|
| 1 | `zfcTr : Provability 𝗜𝚺₁ Sh` | 同（`ℒₒᵣ`） | ❌ 不可能（见上） | ✅ 可陈述（缺口所在） |
| 2 | `𝗭𝗙𝗖.standardProvability : Provability 𝗜𝚺₁ 𝗭𝗙𝗖` | 跨（`ℒₒᵣ`/`ℒₛₑₜ`） | ✅ 有 | ❌ **不可陈述** |

路 2 的结构**能建成**（`Provability` 是多语言的；`ℒₒᵣ` 对任意 `Encodable` 有
`GödelNumber`；`LORDefinable ℒₛₑₜ` 与 `𝗭𝗙𝗖.Δ₁` 都合成成功），
但 `HBL3.D3` 要 `𝔅 σ : Sentence L`，而 `𝔅.pr : Sentence L → Sentence L₀`
⇒ **`HBL3` 只在 `L = L₀` 时可陈述**（`HBL2` **是**多语言的——两边都落在 `L₀`——
两者是独立的类，不可混同）。证据：`CG008Probe17-20.lean`。

**结论**：ZFC 的可证性谓词把 `ℒₛₑₜ` 句映到 `ℒₒᵣ` 句；这个跨语言性要么让 `Δ₁` 丢失，
要么让 `HBL3` 无法陈述。**补上缺口需要扩展 Foundation 的抽象框架**
（或为跨语言情形单开一条路），**不是填一个 `Δ₁` 实例，也不是补一座报价桥**。
本轮已把那个待补的位置**定义**出来：`GodelQ/ZFC/CG008CrossLanguage.lean` 的
`CrossLanguageD3`（`∀ σ, T₀ ⊢ 𝔅 σ 🡒 𝔅' σ`，`𝔅' : Sentence L → Sentence L₀`），
缺口是它的一个实例（`gap_is_cross_language_D3`）。

**同时排除的其余路线**：Σ₁ 绝对性把 V 真降到 ℕ（方向反了，`sigma_one_upward` 沿
`natCastEmbedding : ℕ ↪ₛ V`，`CG008Probe12.lean`）；`SoundOnHierarchy` 桥
（定义在 `ArithmeticTheory` 上且方向相反，`CG008Probe11.lean`）；
把 `sigma_one_provable_of_models` 的 `T` 换成 `𝗭𝗙𝗖`（归约回缺口本身，`CG008Probe21.lean`）。
另**纠正**一处先前的自我误述：缺口是 **D3**（`□σ → □□σ`），
**不是** Σ₁ 完全性（`σ → □σ`）——后者对任意 σ 可证会推出 `Con`，矛盾
（`CG008Probe13.lean`）。

**收据**：`HoTT/verification/runs/2026-10-11-CG001-CG008-HBL3-LOCATION-01`、
`...-CROSS-LANGUAGE-WALL-01`、`...-DELTA1-NECESSITY-01`，三者均
`KERNEL_ACCEPTED_WITH_SCOPE` / `PASS_WITH_SCOPE` / `replay: EXACT_EXIT_STDOUT_STDERR_MATCH`。

**状态不变**：`zfcTr_D3_internalize` 仍未证；`Z0Blocked.lean:65` 的 `sorry` 仍在；
缺口**没有缩小**，但已能说明**它为何绕不开**。

## 5. 文件

- 新文件：
  - `GodelQ/ZFC/Z0Full.lean`（𝔅Z、D1、D2、一致性句等价、Σ1 层级、正对照、完整形式的条件形式）；
  - `GodelQ/ZFC/Z0Blocked.lean`（唯一阻塞引理，带未证标记，**不是**任何运行的编译源）；
  - `GodelQ/ZFC/Z0Bridge.lean`（C-128 的条件归约；是归约运行的编译源，不导入 `Z0Blocked.lean`）；
  - `GodelQ/ZFC/Z0Final.lean`（2026-10-11 廉价传递诚实收尾：仅含 D3 链接条件定理 `zfc_z0_full_of_D3_cheap`，编译 rc=0、无 `sorryAx`；文件头记录「包内廉价传递坍缩为 D3」的负结果）。
- 21 个依赖模块逐字节复制自 `../godel-q-zfc-z0-translate/GodelQ/`（复制时逐个 `cmp` 核对过）。

## 6. 运行

见 `README.md` 的运行表与 CG-001 证据索引 §35。捕获工具：`.claude/goals/CG-007-formalization-completion/tools/capture_run.py`（驱动 `zfc_lean_check.py` 原样复用）。

## 7. 禁止外推

1. 不声称“𝗭𝗙𝗼 ⊬ Con(𝗭𝗙𝗼)”已证：完整形式以 §4 的阻塞引理为显式前提。已证且不带前提的仍是 C-120 的影子形式（`𝗭𝗙𝗼 ⊬ (Sh.craig.consistent)ᵗ`）。
2. 不推出 ZFC ⊢ ⊥。
3. `Sh` 的一致性来自 Lean 元层的 `Universe` 模型（C-103），不是 𝗭𝗙𝗼 内部可证的事。
4. `iT_quote` 与 `models_zfcTr_iff` 是对每个具体算术公式成立的元层定理（在 𝗜𝚺₁ 的每个模型中），不是 𝗜𝚺₁ 内部对“所有公式编码”的一句断言。
5. D3 在 ℕ 中成立是正对照，不证明它在任意（含非标准）𝗜𝚺₁ 模型中成立。
6. C-128 是条件归约。它不证明 D3，不证明 `Z0Blocked` 的 `Type*` 陈述，也不把 `𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)` 提升为无条件定理。Foundation 的 `sigma_one_complete` 只给出 𝗜𝚺₁ 内部的算术证明编码；沿 `arithTrln` 把它变成 𝗭𝗙𝗖 证明编码仍是未证前提。

## 8. CG001-C-128：把 D3 收成一条内部解释（条件归约，不是 D3 的证明）

> **证明包**：`MP-CG001-GODEL-Q-ZFC-Z0-BRIDGE-001`。类型逐字见 `GodelQ/ZFC/Z0Bridge.lean`。

`zfcTr_D3_internalize_of_sigma1_bridge` 的前提 `bridge` 是：对每个 `Type` 层的 𝗜𝚺₁ 模型 V、每个 Σ1 算术句 σ，若 V 内部有 `Provable 𝗜𝚺₁ ⌜σ⌝`，则 V 内部有 `Provable 𝗭𝗙𝗖 ⌜arithTrln.translate σ⌝`。

在这个前提下：

1. `zfcTr τ` 已是 Σ1 句（C-121 的 `zfcTr_sigma1`），而且假设 `Provable 𝗭𝗙𝗖 ⌜translate τ⌝` 正好是 `V ⊧ zfcTr τ`；
2. Foundation 的 `sigma_one_complete` 因此给出 `Provable 𝗜𝚺₁ ⌜zfcTr τ⌝`，这是 V 内部的算术证明编码；
3. `bridge` 把这个编码变成 `Provable 𝗭𝗙𝗖 ⌜translate (zfcTr τ)⌝`。

`zfc_z0_full_of_sigma1_bridge` 把上面的逐点结论喂给 C-122 的 `zfc_z0_full_of_D3_internalize`，得到同一条完整形式：`𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`。

这不是 D3 的证明。Foundation 的 `DirectInterpretation.of_provability` 只把外部推导经完备性变成另一条外部推导，不产生非标准模型 V 里的证明编码，所以填不上 `bridge`。`Z0Blocked.lean` 仍带未证标记，并且不进入本运行的源清单。

## 9. CG-008（2026-10-11，worktree `dev-ef7e5239`）：头号障碍解除 + 路线陈述缺陷

> **证明包**：`MP-CG001-GODEL-Q-ZFC-Z0-CG008-001`（状态仍为 OPEN / 未证）。
> **目标包**：`.claude/goals/CG-008-zfc-set-sigma1-completeness/`。

### 9.1 已解除：集合语言的内部化演算辅助（原判为「最可能卡住的一步」）

`CG008_HANDOFF_2026-10-11.md` §4.2 与 `CG008_PROJECT.md` §5 风险登记都把
「集合语言的内部化演算辅助（`eq_refl`/`eq_symm`/`subst_eq`/`K_intro`/`ball_intro`/`bexs_intro`/`ball_replace`）
在 Foundation 里只为 `Term V ℒₒᵣ` 定义，需自建」列为 §4 路线的头号风险。**该判断过强。**

读 `EquationalTheory.lean:36-70` 可见那套证明只依赖三样：`complete`（模型→元层推导）、
`internal_provable_of_outer_provable`（`D1.lean:32`）、`TProof.specialize!`（`Typed.lean:462`）。
后两者**只要求 `T : Theory L` + `[T.Δ₁]`**，与 `L` 无关；`K_intro`/`A_intro_left`/`A_intro_right`/
`TProof.exs!` 来自 `Entailment.Minimal` 的 `InternalTheory V L` 实例，同样通用。
唯一 ℒₒᵣ 专属的只有两处：`complete` 的来源（换 `SetTheory.complete`，`Misc.lean:269`）
与等式记号 `≐`（硬接线 `ℒₒᵣ`；集合语言写 `Semiformula.rel Language.Eq.eq ![t, u]`）。

**成果**：新文件 `GodelQ/ZFC/ZFCSetInternal.lean`，编译 `rc=0`，过 FORBIDDEN 检查（可进入收据）。
含 13 条可复用引理：`set_outer_to_internal`、`set_complete_of_models`、`set_eq_refl`、
`set_eq_symm`、`set_ne_symm`、`set_eq_uniform_trans`、`set_eq_trans`、`set_subst_eq`、
`set_subst_mem`、`set_K_intro`、`set_A_intro_left`、`set_A_intro_right`、`set_exs_intro`，
外加引号求值辅助 `eval_quote_mem`、`eval_quote_eq`。

**写法要点**（编译实证）：`TProof.specialize!` 的结果形状是
`Semiformula.subst w (⌜σ⌝ : Semiformula V L n)`；要让 `simpa` 化到 `setEq t u` 的具体形状，
必须给中间 `have` 显式的 **typed** 类型标注（`∀¹ (setEq …) : Semiformula V ℒₛₑₜ k`），
否则 Lean 把 `⌜σ⌝` elaborate 成 untyped 的 `FirstOrder.Semiformula`，`simpa` 接不上。

### 9.2 新发现：§4 第 2 步的 `set_sigma_one_complete` 陈述有类型缺陷

§4 写的 `set_sigma_one_complete {ψ} (hp : Hierarchy 𝚺 1 ψ) (hV : V↓[ℒₛₑₜ] ⊧ ψ) : …`
前提取 `V↓[ℒₛₑₜ] ⊧ ψ`，但缺口的 `V` 只有 `[V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]`（**算术**模型）。
探针 `GodelQ/ZFC/CG008Probe3.lean`（`rc=0`）查实：

- `SetStructure V` 在这个上下文里**能被 `infer_instance` 合成**——所以**不报错**；
- 但它合成到的是 `Arithmetic/Exponential/Bit.lean:28` 的
  `instance : Membership V V := ⟨fun a i ↦ Bit i a⟩`（**二进制编码**，不是集合成员关系）。

即拿 `SetStructure V` 去实例化 `V↓[ℒₛₑₜ] ⊧ ψ` 会得到**语义错误**的引理，且静默成功。
**对照**：英文原版交接（GUI 导出第 1518 行起）写的是
`set_sigma_one_complete {V} [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖] …`——
带 `[V↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖]`。中文版 §4 丢掉了这个假设，而它正是关键：
Σ₁ 完全性要的是「V 是 ZFC 的模型」。

### 9.3 缺口的精确形状（本轮定型）

`models_zfcTr_iff`（是 **↔**）给出缺口等价于：对任意 `V ⊨ 𝗜𝚺₁`，
`Provable 𝗭𝗙𝗖 (⌜translate τ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜translate (zfcTr τ)⌝ : V)`。

两端都在 `Provable 𝗭𝗙𝗖 (⌜·⌝ : V)` 这一侧，说的是「V 内部有一个编码为 V 元素的 𝗭𝗙𝗖 推导」
（`Provable T φ := ∃ d : V, Proof T d φ`，见证在 V 里），**与 `V↓[ℒₛₑₜ] ⊧ ·` 无关**。
所以要在 V 的**内部演算层**做，不能在 V 的集合语义里做。

两条已知的失败出口（均有编译实证）：
1. **外部提取**：把 V 内部推导降成元层 `𝗭𝗙𝗖 ⊢ translate τ`——被载体墙挡住
   （`Z0Probe7.lean`：`𝗭𝗙𝗖.internalize V ⊢ ⌜σ⌝` 不能改写成 `𝗭𝗙𝗖.internalize ℕ ⊢ ⌜σ⌝`）。
2. **集合语义**：用 `V↓[ℒₛₑₜ] ⊧ ψ` 走 `set_sigma_one_complete`——V 不是 `SetStructure` 模型
   （§9.2），且强制实例化会用错的 `∈`。

**仍未证**。下一步需要的是 V 内部的 ZFC Σ₁ 完全性（在 `Provable` 的内部演算层构造证明码），
而非语义层的完全性。Foundation 的 `Bootstrapping/` 目录下**没有**任何内部化解释机制
（已用 `grep -rln "Interpretation\|interpret" FirstOrder/Arithmetic/Bootstrapping/` 确认为空），
这是 CG-008 的实质工作量。
