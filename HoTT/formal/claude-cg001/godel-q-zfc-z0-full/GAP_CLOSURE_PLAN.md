# CG-008（提案）· Z0 阻塞引理 `zfcTr_D3_internalize` 的闭合方案

> 状态：**已立项（方向 B）/ 非证明收据**。用户已选 (B) 真正构建集合论 Σ₁ 完全性以闭合 Z0。本文件不声称任何机器证明；它把"如何闭合 Z0 唯一缺口"固定成一份可执行工作单元规格（CG-008）。
> 关联：CG-007（`zfcTr_D3_internalize` 实证确认为实缺口，见 `HoTT/verification/runs/20261010-CG001-Z0-D3-GAP-DIAGNOSTIC-01/`）。

---

## 0. 结论速览

- **Z0 完整形式 `𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)` 在当前 Foundation（commit `1fb01b72`）下不可证。**
- 唯一缺口 = 阻塞引理 `zfcTr_D3_internalize`（`GodelQ/ZFC/Z0Blocked.lean:61-65`，带精确 `sorry` 命题）。
- 缺口本质：**ZFC 的集合论 Σ₁ 完全性 / Hilbert–Bernays–Löb 可导性条件 D3**（针对集合论语义下的可证性谓词 `Provable 𝗭𝗙𝗖 (φ : V)`）。经 `GodelQ/Probe_d3final.lean` 精确到 **`Theory.Δ₁ Sh` 实例缺失**：`#check Theory.Δ₁ Sh` 类存在（`Type`），但 `#check provable_D3 (T := Sh)` 报 `synthInstanceFailed: Theory.Δ₁ Sh`；经 `Sh_provable_iff`（`zfcTr σ ↔ provabilityPred Sh σ`）该实例正是 `zfcTr_D3_internalize` 所归约到的内容——即 ZFC 的 Σ₁ 完全性，Foundation（commit `1fb01b72`）尚未形式化。
- **现有 Foundation API 关不上**（已实证证伪三条路线，见诊断运行）。闭合它需要为 ZFC 的形式化可证性谓词补出"集合论版本的 Σ₁ 完全性"。
- **「包内廉价传递」路线已证伪（2026-10-11）**：尝试从已证影子形式 `zfc_z0` 经 `Con(Sh.craig) ↔ Con(𝗭𝗙𝗖)` 等价桥梁直接推出完整形式。直接 `complete 𝗜𝚺₁` 证明桥梁静默回填 `sorryAx`；以桥梁为前提的条件定理 `cl_prover` 在 12M 心跳下仍超时。两条都坍缩为同一 D3 / `Theory.Δ₁ Sh` 缺口，不能闭合 Z0。诚实收尾见 `GodelQ/ZFC/Z0Final.lean` 与 `CLAIM.md §4.1.2`。**CG-008 仍是唯一真实闭合路径。**
- 好消息：Foundation **已有**闭合所需的底层积木（Lévy 层级 `𝚺ᴸ₁`、通用 `Proof` 谓词、集合论模型与一致性），缺的只是"把 Σ₁ 完全性定理在集合论一侧正式化"这一层。
- **2026-10-11 续：CG-008 已正式立项**——立项书 `CG008_PROJECT.md` 锁定缺口精确形状、分阶段方案（Phase 0 `set_sigma_one_complete`/`set_provable_internalize` → Phase 1 `zfcTr_D3_internalize` → Phase 2 替换 `Z0Blocked.lean` 的 `sorry` 闭合 Z0 → Phase 3 收据登记）与治理边界（F-011：纯下游 `HoTT/formal/`，不改 Foundation 本体）。Phase 0 基础设施锚点 `GodelQ/ZFC/ZFCSetSigma1.lean` 已编译 **rc=0、无未证标记、无 `sorryAx`**，证明 `zfcProvable_iff_provable`（`𝗭𝗙𝗖 ⊢ ψ ↔ Provable 𝗭𝗙𝗖 (⌜ψ⌝ : ℕ)`，源自 Foundation `provable_iff_provable`）与 `zfcProvable_arith_sigma1`（ZFC 集合句可证性为算术 Σ₁）。侦察修正：Foundation 已内置 `setTheory_sigma₁_induction'`（Lévy-Σ₁ 归纳，算术版对偶）、通用 `provable 𝗭𝗙𝗖`、集合句 `⌜φ⌝` 编码，故 CG-008 **可纯下游闭合，无需改 Foundation**；剩余实质工作为 `set_sigma_one_complete`（需把 `D3.lean:45` 的本地 `term_complete` 平移为集合论项求值完全性）。

---

## 1. 缺口的精确形式

```lean
theorem zfcTr_D3_internalize {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V)
```

- `zfcTr τ` = "∃ y, iTDef y 0 code(τ) ∧ provable 𝗭𝗙𝗖 y"——即"`𝗭𝗙𝗖` 证明 `translate τ`"的内部化。
- 前提句 `arithTrln.translate τ` 与结论句 `arithTrln.translate (zfcTr τ)` 是**两句不同的句子**；前者是算术句的集合论翻译，后者是该翻译"可证"的 Σ₁ 内部化。
- 因此缺口 = 从"`𝗭𝗙𝗖 ⊢ φ`"（φ 为 Σ₁ 集合论句）推出"`𝗭𝗙𝗖 ⊢ Pr_𝗭𝗙𝗖(⌜φ⌝)`"——这正是 **D3 / Σ₁ 完全性**。

---

## 2. 为何现有 API 关不上（已实证）

| 路线 | 位置 | 结果 |
|---|---|---|
| `internalize_provability` | `.../DerivabilityCondition/D1.lean:27` | 只对**同一句** φ 改写（`T ⊢ φ → Provable T ⌜φ⌝`），无法合成"被包裹的可证性句"。探针编译失败（`Z0D3Attempt.lean:53` 类型不匹配）。 |
| `provable_D3` / `provable_sigma_one_complete` | `.../Incompleteness/StandardProvability.lean:71/64` | 位于 `section arithmetic`，要求 `T : ArithmeticTheory`。`𝗭𝗙𝗖` 是 `Theory ℒₛₑₜ`，类型错误。 |
| `Z0Bridge.bridge`（C-128） | `Z0Bridge.lean` | 该前提本身即同一内部化 Σ₁ 完全性缺口，只是再收窄，不提供证明。 |

补充侦察：`grep "sigma_one_complete"` 在 `Foundation/FirstOrder/SetTheory` 与 `LK` 下**零命中**；`Foundation/FirstOrder/SetTheory/` 共 27 个文件，覆盖模型/递归/可定义性/序数，**无任何可导性条件或 Σ₁ 完全性**。算术侧（`Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean`）独占全部 D1/D2/D3 机械。

---

## 3. 已有可复用的 Foundation 积木（关键，使方案非空想）

1. **Lévy 层级（集合论 Σ₁）** —— `Foundation/FirstOrder/SetTheory/Definability/Hierarchy.lean`
   - `abbrev lévy := @Bounding.HierarchySymbol.mk _ ℬ[∈, ℒₛₑₜ]`；记号 `𝚺ᴸ₀ / 𝚺ᴸ₁ / 𝚫ᴸ₁` 等。
   - 即"集合论语言的 Σ₁ 公式"已有定义，对标算术侧的 `ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1`。

2. **通用证明谓词** —— `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:539`
   - `def Proof (d φ : V) : Prop := DerivationOf T d {φ}`（对任意 `Theory L`）。
   - 算术侧 `provable : 𝚺ᴬ₁.Semisentence 1`（同文件 :556）是可证性谓词的 Σ₁ 编码；集合论侧需其 **Lévy-Σ₁ 对应物** `provableZFC : 𝚺ᴸ₁.Semisentence 1`。

3. **集合论模型与一致性** —— `SetTheory/Universe.lean`（ZFC 的 `Universe` 模型、`zfc_consistent`）、`ZF/Model.lean`（`𝗭𝗙 ⊨ → 𝗭𝗙𝗖 ⊨`）。

4. **Σ₁ 完全性的算术模板** —— `D3.lean` 的 `bold_sigma_one_complete`（:82）通过 `Bounding.Hierarchy.arithmetic_sigma₁_induction'` 证得：真 Σ₁ 算术句可证。集合论侧需对应的 **Σᴸ₁ 归纳 / Σᴸ₁ 收集-分离** 论证（ZFC 的 Σ₁-collection + Σ₁-separation 给出 Σ₁-正确性）。

---

### 3.5 2026-10-11 深度侦察结论（缺口已确认在「基础设施层」，非语法路线）

对 Foundation 源码（`/Volumes/D/HoTT-toolchain-cache/foundation-src`，commit `1fb01b72`）逐文件核对后，确认：

- **算术侧**：`provable : 𝚺ᴬ₁.Semisentence 1`（`Bootstrapping/Syntax/Proof/Basic.lean:556`）仅服务**算术理论**；**不存在**对集合论证明谓词的算术编码（即没有把「𝗭𝗙𝗖 ⊢ φ」写成算术 Δ₁ 公式的机制）。
- **集合论侧**：`SetTheory/Definability/Hierarchy.lean` 有 Lévy 层级 `𝚺ᴸ₁` 与有界量化 `lévy_ball`/`lévy_bexs`；`Recursion/Seq.lean` 有 `sigmaOne_skolem`（Σ₁ 关系）；`Universe.lean` 有 `zfc_consistent`。但 `SetTheory/` 下 **`grep sigma_one_complete` / `D3` / 可导性条件 = 零命中**；`Proof 𝗭𝗙𝗖` **不是** `𝚺ᴸ₁` 可表示的（没有 `provableZFC : 𝚺ᴸ₁.Semisentence 1`），也**没有集合论的 Σ₁ 完全性**（真 Σ₁ 句 → 在 𝗭𝗙𝗖 中可证）。
- 存在 `FirstOrder.SetTheory.complete`（完备性定理），但完备性 ≠ Σ₁ 完全性；后者需要 Σ₁-collection/separation 的内部论证，Foundation 未形式化。

**结论**：`zfcTr_D3_internalize` 的闭合，无论走「算术 Δ₁ 实例 `Theory.Δ₁ Sh`」（需对集合论可证性做算术化）还是走「集合论 Σ₁ 完全性 / `set_provable_internalize`」（需把 `Proof 𝗭𝗙𝗖` 表成 `𝚺ᴸ₁` 并证 ZFC 的 Σ₁ 完全性），都**依赖 Foundation 当前缺失的基础设施**。这正是 CG-008 的实质工作量。

> **治理闸门（F-011 / sources 边界）**：阶段 0/1 若要补出「集合论证明谓词的 Δ₀/Lévy-Σ₁ 可表示性」与「ZFC 的 Σ₁ 完全性」，很可能**需要改动 Foundation 本体**（新增集合论 Σ₁ 归纳/收集-分离原理），超出本仓库 `sources/` 边界，须走上游贡献或本地 fork，并需**单独授权**。纯下游 `HoTT/formal/` 扩展只能在「Foundation 已提供 set-theoretic Σ₁ 完全性」的假设下推进；当前该假设不成立。

### 3.6 2026-10-11 深度侦察结论（廉价传递路线已证伪，CG-008 仍是唯一路径）

针对「包内廉价传递」——从已无条件证明的影子形式 `zfc_z0 : 𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val)` 经一致性等价桥梁 `𝗜𝚺₁ ⊢ Sh.craig.consistent.val ↔ 𝗭𝗙𝗖.consistent` 推出完整形式 `𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`——做了两次机器检验（本地驱动 `/tmp/build_z0.py`，去 sandbox-exec，保留钉扎与禁用标记检查）：

1. **直接尝试**：`complete 𝗜𝚺₁` 证明桥梁。Lean 无法闭合目标，静默回填 `sorry`，`#print axioms` 报 `sorryAx`。桥梁在当前 Foundation 不可证。
2. **条件形式尝试**：以桥梁为显式前提写 `zfc_z0_full_of_bridge`，主体 `cl_prover [e, hSh]`（`e` 为经 `WeakerThan.pbl` 包裹的抽象前提）。`cl_prover` 在 12 000 000 心跳预算下仍确定性超时——该条件定理数学正确，但 `cl_prover` 对抽象等价比无法在合理预算内闭合。

**结论**：廉价传递与 D3 / `Theory.Δ₁ Sh` 是**同一缺口**（把两估值化可证性谓词在非标准模型中等同 = ZFC 的 Σ₁ 内部化）。它**不能**闭合 Z0，也不引入任何伪造收据。诚实处置：
- `GodelQ/ZFC/Z0Final.lean` 现仅含 D3 链接条件定理 `zfc_z0_full_of_D3_cheap`（编译 rc=0，仅 `[propext, Classical.choice, Quot.sound]`，无 `sorryAx`），文件头完整记录负结果；
- 证据见 `HoTT/verification/runs/2026-10-11-z0final-conditional/`（build1–build3.log）。

> **治理结论**：CG-008（集合论 Σ₁ 完全性）仍是 Z0 完整形式唯一真实的闭合路径；廉价传递作为「不碰 Foundation 本体的捷径」已被证伪，不再作为候选方案。

## 4. 闭合方案（分阶段，每阶段机器可检验）

> 放置位置：作为 **下游扩展** 建在 `HoTT/formal/claude-cg001/`（而非改动上游缓存 `foundation-src`）。受 F-011 门禁约束：源码入 `HoTT/formal/`，运行入 `HoTT/verification/runs/`，索引入 `CLAIM_EVIDENCE_MATRIX.md`；不 push `main`、不碰 `sources/`/`private-audit/`。

### 阶段 0 — 集合论可证性谓词的 Σᴸ₁ 编码
- 定义 `provableZFC : 𝚺ᴸ₁.Semisentence 1`（对标 `provable : 𝚺ᴬ₁.Semisentence 1`），把 `Proof 𝗭𝗙𝗖 d (φ : V)` 编码为 Lévy-Σ₁ 公式。
- 依赖：`Proof` 谓词（已有）、`𝚺ᴸ₁` 层级（已有）。
- 里程碑：`provableZFC` 良类型，且 `Provable 𝗭𝗙𝗖 φ ↔ V ⊧ provableZFC(⌜φ⌝)` 的双向等价（可证 = 真）。

### 阶段 1 — ZFC 的 Σᴸ₁ 完全性
- 定理（对标 `bold_sigma_one_complete`）：`∀ φ : 𝚺ᴸ₁ sentence, V↓[ℒₛₑₜ] ⊧ φ → Provable 𝗭𝗙𝗖 ⌜φ⌝`。
- 论证骨架：Σᴸ₁ 句绝对、ZFC 的 Σ₁-collection / Σ₁-separation 推出 Σ₁-正确性。
- 里程碑：`set_sigma_one_complete` 编译通过（这是整个方案的核心难度点）。

### 阶段 2 — ZFC 的可导性条件 D3
- `set_provable_internalize`（对标 `D3.lean:175` `provable_internalize`）：`Provable 𝗭𝗙𝗖 ⌜φ⌝ → Provable 𝗭𝗙𝗖 ⌜provableZFC φ⌝`，由阶段 1 + `provableZFC` 为 Σᴸ₁ 推出。

### 阶段 3 — 闭合原缺口 + 完整 Z0
- 以 `set_provable_internalize` 实例化得到 `zfcTr_D3_internalize`，消除 `Z0Blocked.lean` 的 `sorry`。
- 经 `Z0Full.zfc_z0_full_of_D3_internalize` 推出完整 Z0：`𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)`。
- 生成真实机器证明收据（`MACHINE_PROVED`，替换 `Z0Blocked.lean` 的 `sorry` 源，重跑 `zfc_lean_check.py`）。

---

## 5. 工作量与风险评估

- **规模**：阶段 1（Σᴸ₁ 完全性）是论文级形式化子工程，需对 ZFC 的 Σ₁ 集合论公理逐一建立可定义性/可证性论证；其余阶段为相对机械的翻译。整体远超单次会话范围，建议作为独立工作单元（CG-008）立项，并评估为"多周"量级。
- **风险**：
  - 上游 `foundation-src` 是钉扎缓存；若阶段 0/1 需要改动 Foundation 本体（如新增集合论 Σ₁ 归纳原理），须走上游贡献或本地 fork，不在本仓库 `sources/` 边界内——需单独授权。
  - 若发现 ZFC 的 Σᴸ₁ 完全性在 Foundation 既有公理下无法推出（极不可能，但属形式化风险），则 Z0 在该基础下本质不可证，应降级为 `CONJECTURE` 永久保留。

## 6. 请求的决定

请授权方向（二选一）：

- **(A) 诚实收尾**：维持 `Z0Blocked.lean` 的 `sorry` 与 `CONJECTURE` 状态，Z0 标记为"基础下未证、缺口已精确定位"。不进入上游扩展。
- **(B) 立项 CG-008**：按第 4 节分阶段真正构建集合论 Σ₁ 完全性 / D3，闭合缺口并产出机器证明收据。需明确：(B1) 仅在下游 `HoTT/formal/` 建扩展，还是 (B2) 同时向上游 Foundation 贡献。
