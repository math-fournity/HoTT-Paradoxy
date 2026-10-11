# 交接文档 · CG-008（ZFC 的集合论 Σ₁ 完全性，Z0 唯一实质缺口的闭合主线）

> 编写时间：2026-10-11
> 上游目标：CG-001「ZFC 的哥德尔第二不完备定理 Z0：`𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)`」
> 适用对象：接手的 AI / 协作者（无需读过本会话历史，本文自包含）
> 关联文档（同目录）：`CG008_PROJECT.md`（立项书）、`GAP_CLOSURE_PLAN.md`（方案演进）、`CLAIM.md`（索赔全文）、`Z0Blocked.lean`（缺口本体）

---

## 0. 一句话目标

把 Z0 完整形式 `𝗭𝗙𝗖 ⊬ arithTrln.translate(𝗭𝗙𝗖.consistent)` 从"条件定理"升级为**机器证明收据**，方法是形式化 ZFC 的**内部化集合论 Σ₁ 完全性**（CG-008），从而消除 `Z0Blocked.lean` 里 `zfcTr_D3_internalize` 的 `sorry`。

---

## 1. 当前精确状态（已核实）

| 项 | 状态 | 位置 |
|---|---|---|
| Z0 完整形式 | **未证**（缺口保留 `sorry`） | `GodelQ/ZFC/Z0Blocked.lean:61-65` |
| 接收端（缺口一旦证毕即出 Z0） | 已就绪，无 `sorry` | `GodelQ/ZFC/Z0Full.lean:117` `zfc_z0_full_of_D3_internalize` → `:103` `zfc_z0_full` |
| 两条廉价路线 | **已证伪**（坍缩为同一 D3 缺口） | `Z0Final.lean`（条件定理 `zfc_z0_full_of_D3_cheap`，rc=0 无 `sorryAx`）、`verification/runs/2026-10-11-z0final-conditional/` |
| CG-008 立项 | 已完成 | `CG008_PROJECT.md` |
| Phase 0 基础设施锚点 | **编译通过 rc=0、无未证标记、无 `sorryAx`** | `GodelQ/ZFC/ZFCSetSigma1.lean` |
| 证据登记 | 已登记 | `HoTT/CLAIM_EVIDENCE_MATRIX.md` 行 `MP-CG001-GODEL-Q-ZFC-Z0-CG008-001` |

**缺口本体**（`Z0Blocked.lean:61-65`，逐字）：
```lean
theorem zfcTr_D3_internalize {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (Z0Full.zfcTr τ)⌝ : V) := by
  sorry
```
语义：在 𝗜𝚺₁ 的任意模型 V 中，若「𝗭𝗙𝗖 证明了 τ 的翻译」成立，则「𝗭𝗙𝗖 证明了『𝗭𝗙𝗖 证明了 τ 的翻译』这句话的翻译」也成立——即 ZFC 可证性谓词的 **D3（希尔伯特-伯奈斯-勒布可导性条件）/ Σ₁ 完全性内部化**。

---

## 2. 为什么是这条路（两条已证伪的廉价路线）

1. **包内廉价传递**：从已证影子形式 `zfc_z0` 经 `Con(Sh.craig) ↔ Con(𝗭𝗙𝗖)` 桥梁推完整形式。
   - 直接 `complete 𝗜𝚺₁` 证桥梁 → Lean 静默回填 `sorryAx`（桥梁不可证）；
   - 以桥梁为前提的条件定理 `cl_prover` 在 12M 心跳下确定性超时。
   - 两条都坍缩为同一 D3 / `Theory.Δ₁ Sh` 缺口。
2. **`Sh.craig` 捷径**：经 Craig 技巧取 `Sh` 的 Δ₁ 公理化套用 Foundation 通用 `provable_D3`。
   - `Sh.craig` 的可证性谓词在非标准 V 中与 `Provable 𝗭𝗙𝗖` **估值发散**（`shInterp : 𝗭𝗙𝗖 ⊳ Sh` 仅语法可靠，未内部化进 𝗜𝚺₁），只能给 ZFC 的**外部** Σ₁ 完全性，闭不上内部化版。
   - 且 `Sh := {σ | 𝗭𝗙𝗖 ⊢ arithTrln.translate σ}` 本身只是 Σ₁（r.e.）而非 Δ₁，故 `Theory.Δ₁ Sh` 实例**不存在**（`#check provable_D3 (T := Sh)` → `synthInstanceFailed: Theory.Δ₁ Sh`）。

结论：必须**直接形式化 `Provable 𝗭𝗙𝗖` 的集合论 Σ₁ 完全性**，别无捷径。

---

## 3. 可行性判定（关键，决定治理边界）

对 Foundation 源码（只读，位于 `/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/`）逐文件核对，**CG-008 可纯下游（`HoTT/formal/`）闭合，无需改动 Foundation 本体**：

| Foundation 已提供的积木 | 位置 | 用途 |
|---|---|---|
| `setTheory_sigma₁_induction'` | `SetTheory/Basic/Hierarchy.lean` | **Lévy-Σ₁ 归纳原理**（算术版 `arithmetic_sigma₁_induction'` 的集合论对偶，正是 `D3.lean` 证明核心引擎） |
| `provable 𝗭𝗙𝗖 : 𝚺ᴬ₁.Semisentence 1` | `Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:556`（对任意理论 `T` 通用，本包 `Z0Full.lean:41` 已成功使用） | ZFC 可证性谓词的 Σ₁ 半句 |
| `Proof 𝗭𝗙𝗖` 通用定义 `DerivationOf T d {φ}` | `Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:539` | 任意理论的可证性关系 |
| `Theory.Δ₁ 𝗭𝗙𝗖` | 本包 `GodelQ/ZFC/ZFCDelta1.lean:43`（已证：ZFC 公理集为算术 Δ₁） | 满足 `D3` 的「公理 Δ₁」前提 |
| 集合句编码 `⌜φ⌝`（`φ : Sentence ℒₛₑₜ`） | 通用 `Syntax` 报价记号（本包 `Z0Full.lean:80` 已用 `⌜(⊥ : Sentence ℒₛₑₜ)⌝`） | 把集合句编码为 ℕ⊂V 中的数 |
| `FirstOrder.SetTheory.complete` | `SetTheory/Basic/Misc.lean:269` | 语义完全性 `T ⊢ φ ↔ ∀ M⊨T, M⊨φ` |
| `ProvablyProperOn.lévy_ofProperOn` | `SetTheory/Definability/Hierarchy.lean:57` | 借语义完全性证 Lévy-绝对性 |
| `setTheory_sigma₁_induction'` 的兄弟 `arithmetic_sigma₁_induction'` | （算术侧，作模板） | 证明结构模板 |

**唯一缺的、须在本包自建的**：把 `D3.lean` 的算术机器（`bold_sigma_one_complete` + `term_complete`）平移到 Lévy 层级。其中 `term_complete`（算术项求值完全性，`D3.lean:45-78`，**在 `D3.lean` 内部本地定义**）没有集合论版，需在 Phase 0.1 文件内仿建集合论项求值完全性。

> 治理（F-011，已被本会话全程遵守）：**不改 Foundation 本体、不碰 `sources/`、不碰 `private-audit/`、不推 `main`、不伪造收据**（任何含 `sorry` 的文件不进入最终收据，`#print axioms` 须仅含 `propext`/`Classical.choice`/`Quot.sound`）。

---

## 4. 文件清单（含 path 与职责）

包根：`HoTT/formal/claude-cg001/godel-q-zfc-z0-full/`（相对仓库根 `dev-ef7e5239/`）

- `CG008_PROJECT.md` — **立项书**：缺口精确形状、两条死路、Phase 0→3 分步、治理边界。
- `GAP_CLOSURE_PLAN.md` — 方案演进（§0 结论、§3.6 侦察结论）。
- `CLAIM.md` — 索赔全文与状态。
- `HANDOFF_CG008.md` — 本交接文档。
- `GodelQ/ZFC/Z0Blocked.lean` — **缺口本体**（`zfcTr_D3_internalize` 的 `sorry`）。
- `GodelQ/ZFC/Z0Full.lean` — `zfcTr` 定义、D1/D2、`zfc_z0_full`、`zfc_z0_full_of_D3_internalize`（接收端）。
- `GodelQ/ZFC/ZFCDelta1.lean` — `ZFC.delta1`（已证 `Theory.Δ₁ 𝗭𝗙𝗖`）。
- `GodelQ/ZFC/Z0Shadow.lean` — `Sh` 定义、`Sh_provable_iff`、`shInterp`。
- `GodelQ/ZFC/Z0PA.lean` — `ISigma1_le_Sh : 𝗜𝚺₁ ⪯ Sh` 等。
- `GodelQ/ZFC/Z0Final.lean` — 诚实降级的 D3 条件定理（无 `sorryAx`）。
- `GodelQ/ZFC/ZFCSetSigma1.lean` — **Phase 0 锚点（已编译 rc=0）**：`zfcProvable_iff_provable`、`zfcProvable_arith_sigma1`。**Phase 0.1 应在此文件内继续添加 `set_sigma_one_complete` 等。**
- `HoTT/verification/runs/2026-10-11-cg008/` — 本回合构建日志（`build.log` / `build-strict.log`，均 rc=0）。
- `HoTT/CLAIM_EVIDENCE_MATRIX.md` — 证据索引（行 `MP-CG001-GODEL-Q-ZFC-Z0-CG008-001`）。

仓库根：`/Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911/dev-ef7e5239/`

---

## 5. 下一步：Phase 0.1 `set_sigma_one_complete`（真正的发力点）

在 `GodelQ/ZFC/ZFCSetSigma1.lean` 内新增，仿 `D3.lean` 的结构：

**5.1 目标引理（签名待 Phase 1 桥接微调，先按下述写）**
```lean
-- 集合论 Σ₁ 完全性：真（在 V 中满足）的 Lévy-Σ₁ 集合句，ZFC 可证
theorem set_sigma_one_complete {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    {ψ : SetTheorySentence} (hp : ℬ[∈, ℒₛₑₜ].Hierarchy 𝚺 1 ψ)
    (hV : V↓[ℒₛₑₜ] ⊧ ψ) : Provable 𝗭𝗙𝗖 (⌜ψ⌝ : V) := by
  apply Bounding.Hierarchy.setTheory_sigma₁_induction' hp
  -- 十个构造情形：verum/falsum/eq/neq/mem/nmem/and/or/ball/exs
```
> 注：`V↓[ℒₛₑₜ] ⊧ ψ` 需要 `[SetStructure V]` 之类的实例；若与 `[V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]` 在同一 `V` 上冲突，可参考 `Z0Full.lean` 用 `arithTrln` 翻译保真性把「V ⊨ 算术句」桥接为「V ⊧ 集合句」。这是 Phase 1 的桥接难点，Phase 0.1 可先对「闭句 / 经翻译的算术句」情形推进。

**5.2 集合论项求值完全性（最大的自建块）**
`D3.lean:45-78` 的本地 `term_complete` 证明 `T.internalize V ⊢ (toNumVec w ⤔ ⌜t⌝) ≐ 𝕹(t.valb w)`，即「项在 V 中的值 = 其在 T 中的 numeral」。集合论侧需要类似引理：对集合论语义下的项 t，证明 `𝗭𝗙𝗖 ⊢ ⌜t⌝ ≐ value_of_t_in_V`。Foundation 未直接提供，须在本文件用集合论项求值 API 自建（先 `grep` 确认 Foundation 是否已有 `SetTheory` 项求值相关 `eval`/`Term.val`/`numeral` 引理，避免重复造轮）。

**5.3 集合论 D3 内部化（仿 `D3.lean:175` `provable_internalize`）**
```lean
theorem set_provable_internalize {V} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    {ψ : SetTheorySentence} (h : Provable 𝗭𝗙𝗖 (⌜ψ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜provabilityPredZFC ψ⌝ : V) := ...
-- 其中 provabilityPredZFC ψ := (provable 𝗭𝗙𝗖).val/[⌜ψ⌝]
```

**5.4 Phase 1 → 2 → 3**（见 `CG008_PROJECT.md` §3）
- Phase 1：用 `set_provable_internalize` + `Z0Full.models_zfcTr_iff` + 翻译保真性，推出 `zfcTr_D3_internalize`（替换 `Z0Blocked.lean:65` 的 `sorry`）。
- Phase 2：`zfc_z0_full_of_D3_internalize` 立即给出无额外前提的 `zfc_z0_full`（Z0 完整形式）。
- Phase 3：全包编译 rc=0、`#print axioms` 仅标准三条；更新 `CLAIM_EVIDENCE_MATRIX.md` 行判词为 `MACHINE_PROVED`；更新 `CLAIM.md`/`GAP_CLOSURE_PLAN.md` 状态。

---

## 6. 构建与验证工具链（必读，否则会卡）

- 构建驱动：`/tmp/build_z0.py`（本地、去 sandbox-exec，钉扎 + 禁用标记检查）。
- **关键环境坑**：本机 Bash 的 cwd **不跨命令持久**。每次构建必须在同一命令内 `cd` 到包根：
  ```bash
  cd /Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911/dev-ef7e5239/HoTT/formal/claude-cg001/godel-q-zfc-z0-full && \
  python3 /tmp/build_z0.py --no-pin-check --package . GodelQ/ZFC/ZFCSetSigma1.lean
  ```
- 收据文件（最终要交付的）**不要**加 `--no-forbidden-check`，让禁用标记闸门运行（含 `sorry`/`admit`/`native_decide`/`unsafe` 会直接判 FAIL）。WIP 脚手架（含 `sorry`）才临时加 `--no-forbidden-check` 仅做类型检查。
- 钉扎可能因 Foundation oleans 变动而需 `--no-pin-check`（本会话一直这么用）。
- 编译可能慢（导入 Foundation + Mathlib 闭包）；一次性大文件易触发长心跳。建议**每阶段一个小文件增量编译**。

---

## 7. Lean API 踩坑记录（省下数小时）

- `⌜ψ⌝` 报价：做类型类 `GödelQuote SetTheorySentence V` 合成，需要 `[V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]` 实例在作用域；否则报 `synthInstanceFailed: GödelQuote SetTheorySentence V`。
- `provable_iff_provable`（`D1.lean:40`）的报价是**标准模型** `⌜φ⌝ : ℕ`，不是任意 `V`——写 `⌜ψ⌝ : ℕ`。
- `provable 𝗭𝗙𝗖` 是 `𝚺ᴬ₁`（算术）半句；把它作用在集合句编码 `⌜ψ⌝` 上得到的是**算术 Σ₁** 陈述（因为编码是数）。这正是 Phase 0 锚点 `zfcProvable_arith_sigma1` 已证的事实。
- 算术 D3（`sigma_one_complete` / `provable_internalize`）键在 `T : ArithmeticTheory` 且 `σ : ArithmeticSentence`；缺口句是**集合句**，故算术 D3 **不能直接套用**——必须建集合论版。
- `Theory.Δ₁` 类是算术味的（`ch : 𝚫ᴬ₁.Semisentence 1` + `isDelta1 : ch.ProvablyProperOn 𝗜𝚺₁`），`ZFC.delta1` 满足的是「公理集 Δ₁」，不等于「定理集 Δ₁」。

---

## 8. 完成判据（Done = 真收据）

1. `GodelQ/ZFC/Z0Blocked.lean` 的 `zfcTr_D3_internalize` **无 `sorry`** 编译通过。
2. `python3 /tmp/build_z0.py --no-pin-check --package . GodelQ/ZFC/Z0Blocked.lean` 与 `Z0Full.lean` 均 rc=0，且 `#print axioms` 仅 `[propext, Classical.choice, Quot.sound]`。
3. `zfc_z0_full`（Z0 完整形式）在**无额外前提**下成立。
4. `HoTT/CLAIM_EVIDENCE_MATRIX.md` 对应行判词改为 `MACHINE_PROVED`；`CLAIM.md` 状态更新为「Z0 完整形式已机器证明」。
5. 全过程不改 Foundation 本体、不碰 `sources/`/`private-audit/`、不推 `main`、不伪造收据。

---

## 9. 开放风险

- **集合论项求值完全性**（§5.2）：Foundation 是否已有现成引理未知，须先 `grep` 确认；若没有，自建量不小。
- **Phase 1 的「V ⊨ 𝗜𝚺₁ 求值集合句」桥接**：需复用本包 `Effective.lean` / `InternalTranslate.lean` 的 `arithInterp` 保真性，签名可能要微调。
- 编译长心跳：分阶段小文件增量验证。

---

## 10. 给接手 AI 的提示词

见本仓库同层对话中用户索取的那段「代码块提示词」（亦可在 `CG008_PROJECT.md` §3 找到方案原文）。直接把它粘给下一个 AI 会话即可，本文档是其完整背景。
