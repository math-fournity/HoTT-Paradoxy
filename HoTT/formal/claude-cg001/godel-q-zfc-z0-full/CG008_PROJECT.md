# CG-008 立项书 · ZFC 的集合论 Σ₁ 完全性（Z0 唯一实质缺口的闭合主线）

> 关联任务：CG-001「ZFC 的哥德尔第二不完备定理 Z0：`𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)`」
> 关联文件：`GodelQ/ZFC/Z0Blocked.lean`（阻塞引理 `zfcTr_D3_internalize`，当前以 `sorry` 精确标注）、
> `GodelQ/ZFC/Z0Full.lean`（`zfc_z0_full_of_D3_internalize` 已就绪，只待该引理）、
> `GAP_CLOSURE_PLAN.md` §3.6（2026-10-11 廉价传递路线证伪结论）。
>
> 治理边界（F-011）：本立项 **纯属下游 `HoTT/formal/` 扩展**。Foundation 只读（位于
> `/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/`），**不修改** `sources/`；
> 不碰 `private-audit/`；不推 `main`；不伪造收据。源在 `HoTT/formal/`，运行记录在
> `HoTT/verification/runs/`，索引在 `HoTT/CLAIM_EVIDENCE_MATRIX.md`。

---

## 0. 一句话结论

Z0 完整形式 `𝗭𝗙𝗖 ⊬ arithTrln.translate(𝗭𝗙𝗖.consistent)` 唯一未闭合的实质步骤，是
`Z0Blocked.lean` 中的阻塞引理 `zfcTr_D3_internalize`——它等价于 **ZFC 内部化的集合论 Σ₁ 完全性**
（即集合论可证性谓词的 D3 可导性条件）。**经本轮侦察确认，Foundation 已提供闭合此缺口所需的全部下游原语**
（`setTheory_sigma₁_induction'`、`provable 𝗭𝗙𝗖`、`Theory.Δ₁ 𝗭𝗙𝗖`、集合句 `⌜φ⌝` 编码、`FirstOrder.SetTheory.complete`），
故 CG-008 可在 `HoTT/formal/` 内全程完成，**无需改动 Foundation**。

---

## 1. 缺口的精确形状（已用机器侦察坐实）

### 1.1 阻塞引理

`GodelQ/ZFC/Z0Blocked.lean:61-65`：

```lean
theorem zfcTr_D3_internalize {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (Z0Full.zfcTr τ)⌝ : V) := by
  sorry
```

含义：在 𝗜𝚺₁ 的**任意**模型 V 中，若「𝗭𝗙𝗖 证明了 τ 的翻译」成立，则「𝗭𝗙𝗖 证明了『𝗭𝗙𝗖 证明了 τ 的翻译』这句话的翻译」也成立。
这正是 ZFC 可证性谓词的 **D3（反射原理 / Σ₁ 完全性的内部化）**。

### 1.2 下游已就绪的接收端

`GodelQ/ZFC/Z0Full.lean:117-134` 的 `zfc_z0_full_of_D3_internalize` 已经把「`zfcTr_D3_internalize` 成立」
作为显式前提，并逐行走出完整 Z0（`zfc_z0_full`，见 `Z0Full.lean:103`）。一旦 `zfcTr_D3_internalize`
被机器证明，删去 `Z0Blocked.lean` 的 `sorry` 即得到无未证标记的 Z0 收据。

### 1.3 两条已被证伪的廉价路线（不再尝试）

| 路线 | 结论 | 证据 |
|---|---|---|
| **包内廉价传递**：用 `complete 𝗜𝚺₁` 把 `zfcTr` 桥接到 `zfc_z0_full` | 坍缩为同一个 D3 缺口；诚实保留为条件定理 `zfc_z0_full_of_D3_cheap`（无 `sorryAx`，见 `Z0Final.lean`），但**不计入收据** | `verification/runs/2026-10-11-z0final-conditional/`（build1/2 在 200k/12M heartbeats 超时，build3 `rc=0`，`#print axioms` 仅 `propext/Classical.choice/Quot.sound`）；`CLAIM.md` §4.1.2 |
| **`Sh.craig` 捷径**：经 Craig 技巧取 `Sh` 的 Δ₁ 公理化，套用 Foundation 通用 `provable_D3` | `Sh.craig` 的可证性谓词在非标准 V 中与 `Provable 𝗭𝗙𝗖` **估值发散**（`shInterp : 𝗭𝗙𝗖 ⊳ Sh` 仅语法可靠，未内部化进 𝗜𝚺₁），只能给 ZFC 的**外部** Σ₁ 完全性，闭不上内部化版的 `zfcTr_D3_internalize` | `CraigTrick.lean:311`（`(T.craig).Δ₁`）、`:321-335`（`T.craig ⪯ T` / `T ⪯ T.craig` / `T ≊ T.craig`）；`Z0Shadow.lean:40` 的 `shInterp` |

---

## 2. 为什么「构建 ZFC 的 Σ₁ 完全性」是对的，且是集合论版而非算术版

### 2.1 Foundation 已有「算术」Σ₁ 完全性，但键不到我们的句上

`Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean`：

- 前置（`D3.lean:34`）：`variable (T : ArithmeticTheory) [Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T]`
- `sigma_one_complete`（`D3.lean:170`）：`ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ → V↓[ℒₒᵣ] ⊧ σ → Provable T (⌜σ⌝ : V)`
- `provable_internalize`（`D3.lean:175`）：`Provable T (⌜σ⌝ : V) → Provable T (⌜provabilityPred T σ⌝ : V)`

关键限制：`T` 必须是 **`ArithmeticTheory`**，且 `σ` 是 **`ArithmeticSentence`**。`provable_internalize` 的
`σ` 取算术句。而 `zfcTr_D3_internalize` 的两边都是 `Provable 𝗭𝗙𝗖` 作用在**集合语言句**的编码上
（`⌜arithTrln.translate τ⌝`、`⌜arithTrln.translate (zfcTr τ)⌝`），不是算术句。因此**算术 D3 不能直接实例化**到本缺口。

### 2.2 `Sh` 拿不到 `Theory.Δ₁`，所以「让 Sh 变 Δ₁」此路不通

`Z0Blocked.lean:30` 已点明：Foundation 通用 `provable_D3` 若能以 `T = Sh` 调用，即可直接给出
`𝗜𝚺₁ ⊢ provabilityPred Sh σ 🡒 provabilityPred Sh (provabilityPred Sh σ)`，而 `zfcTr σ ↔ provabilityPred Sh σ`
（经 `Sh_provable_iff`，见 `Z0Shadow.lean:45`）。但 `[Theory.Δ₁ Sh]` **不成立**——`Sh` 是 r.e.（Σ₁）而非 Δ₁，
`#check Theory.Δ₁ Sh` 合成失败（见 `Z0Blocked.lean:32`）。`Sh.craig` 虽 Δ₁ 却估值发散（§1.3）。
故「补 `Δ₁ Sh`」是死胡同，真正要做的是**直接证明 `Provable 𝗭𝗙𝗖` 的集合论 D3**。

### 2.3 集合论 Σ₁ 完全性在 Foundation 中「差最后一块拼图」

Foundation 已具备（全部为只读可用原语）：

| 原语 | 位置 | 用途 |
|---|---|---|
| `setTheory_sigma₁_induction'` | `SetTheory/Basic/Hierarchy.lean` | **Lévy-Σ₁ 归纳原理**（算术版 `arithmetic_sigma₁_induction'` 的集合论对偶，正是 `D3.lean` 证明的核心引擎） |
| `provable 𝗭𝗙𝗖 : 𝚺ᴬ₁.Semisentence 1` | `Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:556`（对**任意**理论 `T` 通用，已在本包 `Z0Full.lean:41` 成功使用） | ZFC 可证性谓词的 Σ₁ 半句 |
| `Proof 𝗭𝗙𝗖` 通用定义 `DerivationOf T d {φ}` | `Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:539` | 任意理论的可证性关系 |
| `Theory.Δ₁ 𝗭𝗙𝗖` | `GodelQ/ZFC/ZFCDelta1.lean:43`（已证：ZFC 公理集为算术 Δ₁） | ZFC 已满足 `Theory.Δ₁` 的「公理 Δ₁」要求 |
| `ProvablyProperOn.lévy_ofProperOn` | `SetTheory/Definability/Hierarchy.lean:57` | 借语义完全性证 Lévy-绝对性 |
| `FirstOrder.SetTheory.complete` | `SetTheory/Basic/Misc.lean:269` | 语义完全性 `T ⊢ φ ↔ ∀ M⊨T, M⊨φ` |
| 集合句编码 `⌜φ⌝`（`φ : Sentence ℒₛₑₜ`） | 通用 `Syntax` 报价记号（本包 `Z0Full.lean:80` 已用 `⌜(⊥ : Sentence ℒₛₑₜ)⌝`） | 把集合句编码为 ℕ⊂V 中的数 |

**唯一缺失**：把上述原语组装成「`Provable 𝗭𝗙𝗖` 的集合论 Σ₁ 完全性 + D3 内部化」的下游模块。
这就是 CG-008 的实质工作量，且全部落在 `HoTT/formal/` 内。

---

## 3. 分阶段实施方案

> 每阶段产物均为独立 `.lean` 文件，用 `/tmp/build_z0.py --no-forbidden-check --no-pin-check --package . <file>`
> 增量编译验证；最终收据文件**不得含 `sorry`/`admit`**。运行记录写入 `HoTT/verification/runs/2026-10-11-cg008/`。

### Phase 0 · 集合论 Σ₁ 完全性基础设施

新建 `GodelQ/ZFC/ZFCSetSigma1.lean`：

- **0.1 集合论 Σ₁ 完全性定理**（仿 `D3.lean:162-173` 的 `sigma_one_provable_of_models` / `sigma_one_complete`，
  但层级换成 Lévy）：

  ```lean
  theorem set_sigma_one_complete {ψ : SetTheorySentence}
      (hp : ℬ[∈, ℒₛₑₜ].Hierarchy 𝚺 1 ψ)
      (hV : V↓[ℒₛₑₜ] ⊧ ψ) : Provable 𝗭𝗙𝗖 (⌜ψ⌝ : V) := by
    apply Bounding.Hierarchy.setTheory_sigma₁_induction' hp
    -- 十个构造情形：verum/falsum/eq/neq/mem/nmem/and/or/ball/exs
    -- 其中 ball 情形即 Lévy 有界全称 ∀¹[“#0 ∈ t”] φ，是 Σ₁ 的构成方式；
    -- exs 情形取 V 中的见证，用 IH + ZFC 的 ∃-引入。
  ```

  **开放技术风险（Phase 0.1 的关键不确定点，须先查实）**：算术版 `bold_sigma_one_complete`
  借 `term_complete` 把项求值搬进 `T.internalize V ⊢ ...`。集合论对偶需要集合论项求值的完全性
  引理（把 `V ⊨ t` 推出 `𝗭𝗙𝗖 ⊢ t = 值`）。若 Foundation 未直接提供，需仿 `D3.lean:45` 的
  `term_complete` 在集合论侧自建，或证明对**闭句**（`ξ` 为空）情形可绕过项求值、仅对公式结构归纳。
  **这一查证是 Phase 0 的第一步、也是本立项的头号不确定性**，须在写证明前用 `grep`/读数确认。

- **0.2 集合论 D3 内部化**（仿 `D3.lean:175` 的 `provable_internalize`）：

  ```lean
  theorem set_provable_internalize {ψ : SetTheorySentence}
      (h : Provable 𝗭𝗙𝗖 (⌜ψ⌝ : V)) : Provable 𝗭𝗙𝗖 (⌜provabilityPredZFC ψ⌝ : V) := by
    apply set_sigma_one_complete (V := V) (ψ := provabilityPredZFC ψ) (by simp)
    -- 其中 provabilityPredZFC ψ := (provable 𝗭𝗙𝗖).val/[⌜ψ⌝]
  ```

### Phase 1 · 从集合论 D3 走到 `zfcTr_D3_internalize`

在 `ZFCSetSigma1.lean`（或 `Z0Blocked.lean` 的新版）中：

- 利用 `Z0Full.lean` 已有的 `models_zfcTr_iff`（`V ⊨ zfcTr τ ↔ Provable 𝗭𝗙𝗖 (⌜translate τ⌝)`）与
  翻译保真性（`arithInterp` / `eval_numeralF_iff` / `internalize_provability`），把 Phase 0.2 的
  `set_provable_internalize` 实例化到 `ψ := arithTrln.translate τ` 与 `ψ := arithTrln.translate (zfcTr τ)`，
  推出：

  ```lean
  theorem zfcTr_D3_internalize {V} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
      (τ : ArithmeticSentence)
      (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (Z0Full.zfcTr τ)⌝ : V) := by
    -- 经 Phase 0.2 + 翻译保真性 + models_zfcTr_iff，无 sorry
  ```

  此处须处理「V ⊨ 𝗜𝚺₁（算术模型）如何求值集合句」的桥接：对任意 V ⊨ 𝗜𝚺₁，
  `V ⊨ arithTrln.translate σ` 由算术语义经翻译定义；而 `set_sigma_one_complete` 的前提取
  `V↓[ℒₛₑₜ] ⊧ ψ`。两者通过 `arithTrln` 的保真性（`translate` 把算术真值搬为集合真值）衔接——
  此衔接引理需在 Phase 1 显式补全（可能复用本包 `Effective.lean` / `InternalTranslate.lean` 已有结果）。

### Phase 2 · 闭合 Z0（无未证标记）

- 用 Phase 1 的 `zfcTr_D3_internalize` 替换 `Z0Blocked.lean:65` 的 `sorry`，使
  `zfc_z0_full_of_D3_internalize`（`Z0Full.lean:117`）在**无额外前提**下成立；
- 其结论 `zfc_z0_full`（`Z0Full.lean:103`）即 `𝗭𝗙𝗖 ⊬ arithTrln.translate(𝗭𝗙𝗖.consistent)` —— Z0 完整形式。

### Phase 3 · 收据与登记

- 全包编译（`/tmp/build_z0.py`）`rc=0`，对 `Z0Blocked.lean` 与 `Z0Full.lean` 跑 `#print axioms`，
  确认无 `sorryAx`；
- 在 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 新增行：
  `MP-CG001-GODEL-Q-ZFC-Z0-CG008-001 | CG001-C-122（CG-008 闭合，Z0 完整形式机器证明）| formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/Z0Blocked.lean + Z0Full.lean | verification/runs/2026-10-11-cg008/ | MACHINE_PROVED`；
- 更新 `CLAIM.md` 状态为「Z0 完整形式已机器证明」，更新 `GAP_CLOSURE_PLAN.md` §0 与 §3.6 标记 CG-008 完成。

---

## 4. 治理与合规（F-011）

- **纯下游**：所有新增/修改文件位于 `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/`；Foundation 只读。
- **不碰红线**：不动 `sources/`、不动 `private-audit/`、不推 `main`。
- **不伪造收据**：任何含 `sorry` 的中间文件**不**进入最终收据；`#print axioms` 须仅含
  `propext` / `Classical.choice` / `Quot.sound`（与 `Z0Final.lean` 既有零-`sorryAx` 记录一致）。
- **可复现**：运行记录落 `HoTT/verification/runs/2026-10-11-cg008/`；工具链由 `LEAN_TOOLCHAIN.json` 固定。

---

## 5. 风险登记

| 风险 | 等级 | 缓解 |
|---|---|---|
| Phase 0.1 缺集合论项求值完全性引理，需自建 | 中 | 先 `grep` 确认 Foundation 是否已有；按 `D3.lean:45` `term_complete` 样板在集合论侧补建，仅对闭句情形可绕过 |
| Phase 1 的「V ⊨ 𝗜𝚺₁ 求值集合句」桥接缺引理 | 中 | 复用本包 `Effective.lean`/`InternalTranslate.lean` 的 `arithInterp` 保真性结果 |
| 编译 heartbeats 超时（前次曾达 12M） | 低-中 | 分阶段小文件增量编译；每阶段单独验证，避免一次性大编译 |
| 误判「算术 D3 可直接套用」 | 已排除 | §2.1 已论证 `σ` 须为算术句，而缺口句是集合句，故不可直接套 |

---

## 6. 本轮侦察坐实的「好消息」

与 `GAP_CLOSURE_PLAN.md` §3.6 的旧判断（「CG-008 = 从零构建集合论 Σ₁ 完全性」）相比，本轮进一步确认：
Foundation **已内置** `setTheory_sigma₁_induction'`（Lévy-Σ₁ 归纳，算术版的对偶）与通用
`provable 𝗭𝗙𝗖`、以及 `Theory.Δ₁ 𝗭𝗙𝗖`。因此 CG-008 不是「发明新数学」，而是**把 `D3.lean` 的算术机器
平移到 Lévy 层级**——工作量确定但可行，且全程在下游 `HoTT/formal/` 内完成，治理上零风险。
