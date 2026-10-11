# CG-008 交接文档 · ZFC 的集合论 Σ₁ 完全性（Z0 完整形式闭合主线）

> 适用范围：接手工位 AI / 压缩恢复后的本会话。本文档与 `CG008_PROJECT.md`（立项书）、`GAP_CLOSURE_PLAN.md`（方案）、`CLAIM.md`、`HoTT/CLAIM_EVIDENCE_MATRIX.md` 配套，但**自包含**，可独立接管。
> 治理红线（F-011）：纯下游 `HoTT/formal/` 扩展；Foundation 源码只读、不碰 `sources/`；不动 `private-audit/`；不 push `main`；不伪造收据。

---

## 0. 一句话目标

闭合 Z0 完整形式

```
𝗭𝗙𝗖 ⊬ arithTrln.translate(𝗭𝗙𝗖.consistent)
```

其唯一实质缺口是阻塞引理 `zfcTr_D3_internalize` —— 即 **ZFC 内部化的集合论 Σ₁ 完全性 / Hilbert–Bernays–Löb 可导性条件 D3**。本轮（2026-10-11）已完成立项，并做出 Phase 0 的编译验证起步。

---

## 1. 项目背景与链路

- **CG-001**：在 real ZFC 上形式化哥德尔第二不完备定理 Z0：`ZFC ⊬ Con(ZFC)`。
- 完整形式经 Foundation 抽象第二定理 `ProvabilityAbstraction.con_unprovable` 可得；把"ZFC 证明某句的翻译"作为可证性谓词 `zfcTr`，需满足 D3 条件。
- 已建链路（全部在本包，编译 `rc=0`）：
  - `Z0Shadow.lean`：`Sh := {σ | 𝗭𝗙𝗖 ⊢ arithTrln.translate σ}`（ZFC 的算术影子），`Sh_provable_iff : Sh ⊢ σ ↔ 𝗭𝗙𝗖 ⊢ translate σ`。
  - `Z0Full.lean:60`：`zfcTr : Provability 𝗜𝚺₁ Sh`，`zfcTr σ = "𝗭𝗙𝗖 证明 translate σ"`。
  - `Z0Full.lean:103`：`zfc_z0_full [zfcTr.HBL3] : 𝗭𝗙𝗖 ⊬ translate(𝗭𝗙𝗖.consistent)`。
  - `Z0Full.lean:117`：`zfc_z0_full_of_D3_internalize` 把「`zfcTr_D3_internalize` 成立」作为显式前提，逐行走出完整 Z0。
- **结论**：只要机器证明 `zfcTr_D3_internalize` 并删去 `Z0Blocked.lean` 的 `sorry`，即得 Z0 完整形式的机器证明收据。

---

## 2. 精确缺口

`GodelQ/ZFC/Z0Blocked.lean:61-65`：

```lean
theorem zfcTr_D3_internalize {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (Z0Full.zfcTr τ)⌝ : V) := by
  sorry
```

含义：在 𝗜𝚺₁ 的**任意**模型 V 中，若"𝗭𝗙𝗖 证明了 τ 的翻译"成立，则"𝗭𝗙𝗖 证明了『𝗭𝗙𝗖 证明了 τ 的翻译』这句话的翻译"也成立。这正是 ZFC 可证性谓词的 **D3（反射原理 / Σ₁ 完全性的内部化）**，内部化版本。

等价形式（经 `Z0Full.lean` 的 `models_zfcTr_iff`）：`V ⊨ zfcTr τ → Provable 𝗭𝗙𝗖 (⌜translate(zfcTr τ)⌝)`。

---

## 3. 两条已证伪的廉价路线（不要再试）

| 路线 | 结果 | 证据 |
|---|---|---|
| **包内廉价传递**：从影子形式经 `Con(Sh.craig) ↔ Con(𝗭𝗙𝗖)` 桥梁推完整形式 | 坍缩为同一 D3 缺口；直接 `complete 𝗜𝚺₁` 静默回填 `sorryAx`，`cl_prover` 在 12M 心跳超时 | `Z0Final.lean`（诚实降格，仅 D3 链接条件定理 `zfc_z0_full_of_D3_cheap`，rc=0、无 `sorryAx`）；`verification/runs/2026-10-11-z0final-conditional/` |
| **`Sh.craig` 捷径**：Craig 技巧取 Sh 的 Δ₁ 公理化，套 Foundation 通用 `provable_D3` | `Sh.craig` 可证性谓词在非标准 V 中与 `Provable 𝗭𝗙𝗖` **估值发散**（`shInterp : 𝗭𝗙𝗖 ⊳ Sh` 仅语法可靠，未内部化进 𝗜𝚺₁），只能给 ZFC 的**外部** Σ₁ 完全性，闭不上内部化版 | `CraigTrick.lean:311`（`(T.craig).Δ₁`）、`:321-335`（`T.craig ⪯ T` 等）；`Z0Shadow.lean:40` 的 `shInterp` |

此外：`Theory.Δ₁ Sh` **不成立**（Sh 是 r.e./Σ₁ 而非 Δ₁），故"补 `Δ₁ Sh`"此路不通——`#check provable_D3 (T := Sh)` 报 `synthInstanceFailed: Theory.Δ₁ Sh`。

---

## 4. 本轮关键侦察结论（决定路线）

**CG-008 可纯下游闭合，无需改动 Foundation 本体。** Foundation 已内置闭合所需全部原语：

| 原语 | 位置 | 用途 |
|---|---|---|
| `setTheory_sigma₁_induction'` | `SetTheory/Basic/Hierarchy.lean` | **Lévy-Σ₁ 归纳原理**（算术版 `arithmetic_sigma₁_induction'` 的集合论对偶，正是 `D3.lean` 证明核心引擎） |
| `provable 𝗭𝗙𝗖 : 𝚺ᴬ₁.Semisentence 1` | `Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:556`（对任意理论 `T` 通用；本包 `Z0Full.lean:41` 已用） | ZFC 可证性谓词的 Σ₁ 半句 |
| `Proof 𝗭𝗙𝗖` 通用定义 `DerivationOf T d {φ}` | `Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:539` | 任意理论可证性关系 |
| `Theory.Δ₁ 𝗭𝗙𝗖` | 本包 `ZFCDelta1.lean:43`（已证：ZFC 公理集为算术 Δ₁） | ZFC 已满足 `Theory.Δ₁` 的"公理 Δ₁"要求 |
| `ProvablyProperOn.lévy_ofProperOn` | `SetTheory/Definability/Hierarchy.lean:57` | 借语义完全性证 Lévy-绝对性 |
| `FirstOrder.SetTheory.complete` | `SetTheory/Basic/Misc.lean:269` | 语义完全性 `T ⊢ φ ↔ ∀ M⊨T, M⊨φ` |
| 集合句编码 `⌜φ⌝`（`φ : Sentence ℒₛₑₜ`） | 通用 `Syntax` 报价记号（本包 `Z0Full.lean:80` 已用 `⌜(⊥ : Sentence ℒₛₑₜ)⌝`） | 把集合句编码为 ℕ⊂V 中的数 |

**故 CG-008 = 把 `D3.lean` 的算术机器平移到 Lévy 层级。** 工作量确定、治理零风险。

---

## 5. 已完成产物（本会话）

- **`CG008_PROJECT.md`**：立项书（缺口精确形状、两死路、分阶段方案 Phase 0–3、治理边界）。
- **`GodelQ/ZFC/ZFCSetSigma1.lean`**：Phase 0 锚点，**编译 `rc=0`、无 `sorry`/`admit`、无 `sorryAx`**（严格禁用标记检查通过）。已证：
  - `zfcProvable_iff_provable {ψ : SetTheorySentence} : Provable 𝗭𝗙𝗖 (⌜ψ⌝ : ℕ) ↔ 𝗭𝗙𝗖 ⊢ ψ`
    （源自 Foundation `D1.lean:40` 的 `@[simp] provable_iff_provable`，**注意其报价是 `⌜φ⌝ : ℕ` 标准模型，非任意 V**，且需 `[𝗭𝗙𝗖.Δ₁]`）。
  - `zfcProvable_arith_sigma1 {V} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] {ψ} : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 ((provable 𝗭𝗙𝗖).val/[⌜ψ⌝] : ArithmeticSentence)`
    （确认 `Provable 𝗭𝗙𝗖 (⌜ψ⌝)` 是算术 Σ₁——缺口两端的"Σ₁"半边已坐实）。
- 运行日志 `HoTT/verification/runs/2026-10-11-cg008/`（`build.log` / `build-strict.log`）。
- 证据矩阵行 `MP-CG001-GODEL-Q-ZFC-Z0-CG008-001`（`CG008_PROJECT_ESTABLISHED / PHASE0_ANCHOR_COMPILED_CLEAN`）。
- `GAP_CLOSURE_PLAN.md` §0、`CLAIM_EVIDENCE_MATRIX.md` 同步更新。

---

## 6. 构建 / 验证命令（关键环境提示）

- 构建驱动 `/tmp/build_z0.py`（本地 drop-in，钉扎工具链、去 sandbox-exec；其 `FORBIDDEN` 检查拒绝 `sorry`/`admit`/`unsafe` 等，除非 `--no-forbidden-check`）。
- Foundation 缓存库根：`/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0`（Foundation 源码只读镜像：`/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/`）。
- 工具链钉扎见包内 `LEAN_TOOLCHAIN.json` / `MATHLIB_CLOSURE.json`；Lean 4 core v4.34.0。

⚠️ **本环境 Bash 的 cwd 不跨命令持久**——必须在同一命令内 `cd` 到包根：

```bash
cd /Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911/dev-ef7e5239/HoTT/formal/claude-cg001/godel-q-zfc-z0-full && python3 /tmp/build_z0.py --no-pin-check --package . GodelQ/ZFC/ZFCSetSigma1.lean
```

- 收据文件须无 `sorry`/`admit`；带 `sorry` 的中间文件编译须加 `--no-forbidden-check` 且**不得称为收据**。
- 编译可能较慢（Foundation 缓存导入）；分阶段小文件增量编译，避免一次性大编译。

---

## 7. 剩余实质工作（下一个 AI 的发力点）

### Phase 0.1 · `set_sigma_one_complete`（核心难点）
仿 `D3.lean:82-173` 的 `bold_sigma_one_complete` / `sigma_one_complete`，但层级换 Lévy（`ℬ[∈, ℒₛₑₜ].Hierarchy 𝚺 1`），归纳引擎用 `setTheory_sigma₁_induction'`。目标：

```lean
theorem set_sigma_one_complete {ψ : SetTheorySentence}
    (hp : ℬ[∈, ℒₛₑₜ].Hierarchy 𝚺 1 ψ)
    (hV : V↓[ℒₛₑₜ] ⊧ ψ) : Provable 𝗭𝗙𝗖 (⌜ψ⌝ : V) := by
  apply Bounding.Hierarchy.setTheory_sigma₁_induction' hp
  -- 十个构造情形：verum/falsum/eq/neq/mem/nmem/and/or/ball/exs
```

- **🔴 关键风险 / 开放点**：算术版 `bold_sigma_one_complete` 借**局部** `term_complete`（`D3.lean:45-78`）把项求值搬进 `T.internalize V ⊢ ...`。集合论对偶需要**集合论项求值完全性**引理（把 `V ⊨ t` 推出 `𝗭𝗙𝗖 ⊢ t = 值`）。已 `grep` 确认 Foundation `SetTheory/` 下**无** `term_complete` / 集合论项求值 API，故需在本文件**自建**（仿 `D3.lean:45` 样板，针对闭句情形可绕过项求值、仅对公式结构归纳——这是首选降级路径，须先验证）。
- 另一开放点：`set_sigma_one_complete` 的前提取 `V↓[ℒₛₑₜ] ⊧ ψ` 要求 V 为 `SetStructure`；而 D3 内部化须在所有 `V ⊨ 𝗜𝚺₁`（算术模型）成立。需借 `arithTrln` 保真性把"算术模型求值集合句"桥接到 `SetStructure` 语义（复用本包 `Effective.lean` / `InternalTranslate.lean` 的 `arithInterp` 结果）。

### Phase 0.2 · `set_provable_internalize`
仿 `D3.lean:175` 的 `provable_internalize`：

```lean
theorem set_provable_internalize {ψ : SetTheorySentence}
    (h : Provable 𝗭𝗙𝗖 (⌜ψ⌝ : V)) : Provable 𝗭𝗙𝗖 (⌜provabilityPredZFC ψ⌝ : V) := ...
```
其中 `provabilityPredZFC ψ := (provable 𝗭𝗙𝗖).val/[⌜ψ⌝]`。

### Phase 1 · 闭合 `zfcTr_D3_internalize`
在 `ZFCSetSigma1.lean`（或新版 `Z0Blocked.lean`）中用 `models_zfcTr_iff`（`Z0Full.lean:67`）+ 翻译保真性，把 Phase 0.2 实例化到 `ψ := arithTrln.translate τ` 与 `ψ := arithTrln.translate (zfcTr τ)`，推出无 `sorry` 的 `zfcTr_D3_internalize`。

### Phase 2 · 闭合 Z0（无未证标记）
用 Phase 1 结果替换 `Z0Blocked.lean:65` 的 `sorry`；`zfc_z0_full_of_D3_internalize`（`Z0Full.lean:117`）即无额外前提成立，`zfc_z0_full`（`Z0Full.lean:103`）即完整形式。

### Phase 3 · 收据与登记
全包编译 `rc=0`；对 `Z0Blocked.lean` / `Z0Full.lean` 跑 `#print axioms`，确认仅 `propext / Classical.choice / Quot.sound`。在 `CLAIM_EVIDENCE_MATRIX.md` 将 `MP-CG001-GODEL-Q-ZFC-Z0-CG008-001` 判词升级为 `MACHINE_PROVED`；更新 `CLAIM.md` 与 `GAP_CLOSURE_PLAN.md`；运行记录写入 `HoTT/verification/runs/2026-10-11-cg008/`（含 `RUN.json`、`stdout.txt`、`stderr.txt`、`source-manifest.json`，遵循 `AGENTS.md` 的 MATH_PROOF_BEFORE_DELIVERY 门禁）。

---

## 8. 必读文件索引

**本包**（`HoTT/formal/claude-cg001/godel-q-zfc-z0-full/`）：
- `GodelQ/ZFC/Z0Blocked.lean`（缺口 + `sorry`）
- `GodelQ/ZFC/Z0Full.lean`（`zfcTr`、`zfc_z0_full`、`zfc_z0_full_of_D3_internalize`）
- `GodelQ/ZFC/Z0Shadow.lean`（`Sh`、`Sh_provable_iff`）
- `GodelQ/ZFC/ZFCDelta1.lean`（`ZFC.delta1`）
- `GodelQ/ZFC/ZFCSetSigma1.lean`（Phase 0 锚点，起步点）
- `CG008_PROJECT.md`、`GAP_CLOSURE_PLAN.md`、`CLAIM.md`

**Foundation 源码（只读）**（`/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/`）：
- `Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean`（`sigma_one_complete :170`、`provable_internalize :175`、前置 `:34`）
- `Arithmetic/Bootstrapping/DerivabilityCondition/D1.lean`（`provable_iff_provable :40`，报价 `: ℕ`）
- `Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean`（`Proof :539`、`provable :556`、`Provable.defined :608`）
- `Arithmetic/Bootstrapping/Syntax/Theory.lean`（`class Δ₁ :16`）
- `SetTheory/Basic/Hierarchy.lean`（`setTheory_sigma₁_induction'`）
- `SetTheory/Definability/Hierarchy.lean`（`lévy`、`ProvablyProperOn.lévy_ofProperOn`）
- `SetTheory/Basic/Misc.lean`（`complete :269`）

**记忆日志**：`.workbuddy-ai/memory/2026-10-11.md`（含环境提示与侦察修正记录）。

---

## 9. 当前诚实状态

- Z0 完整形式 **仍未机器证明**（`Z0Blocked.lean` 的 `sorry` 仍在）；未伪造收据、未 push `main`、未碰 `sources/`/`private-audit/`。
- CG-008 **已立项**；Phase 0 锚点 **已编译干净**（无 `sorry`/`admit`）。
- 下一步是 **Phase 0.1 `set_sigma_one_complete`**（含自建集合论项求值完全性这一关键子任务）。

---

## 10. 给接手工位 AI 的速记

1. 读 `CG008_PROJECT.md` + 本文件 §1–§4，理解缺口与死路。
2. 读 `D3.lean`（`sigma_one_complete`/`provable_internalize` 全文）与 `SetTheory/Basic/Hierarchy.lean`（`setTheory_sigma₁_induction'` 签名）。
3. 在 `ZFCSetSigma1.lean` 内建 `set_sigma_one_complete`：先确认 `setTheory_sigma₁_induction'` 的调用方式，再处理集合论项求值（优先尝试"闭句仅对公式结构归纳"降级路径）。
4. 增量编译（§6 命令），禁止 `sorry` 进收据。
5. 按 §7 Phase 1→3 推进，最终更新证据矩阵与文档。

---

## 11. 本轮续作侦察补充（2026-10-11 续 · 已读 Foundation 源码）

> 以下为接续 AI 在本会话下半段读 `D3.lean` / `D1.lean` / `Typed.lean` / `SetTheory/Basic/Hierarchy.lean` 后修正的精确路线。**没有改变治理边界（仍纯下游、不改 Foundation）**，但把 Phase 0.1 的"怎么做"从模糊缩小到可机械执行。

### 11.1 算术模板已彻底读懂（`D3.lean` 全文）

算术 `provable_internalize`（`D3.lean:175-178`）证明：
```
Provable T (⌜σ⌝ : V) → Provable T (⌜provabilityPred T σ⌝ : V)
  := by simpa [models_iff] using sigma_one_complete (σ := provabilityPred T σ) (by simp)
```
依赖两条：
1. `sigma_one_complete {σ} (hσ : Hierarchy 𝚺1 σ) : V↓[ℒₒᵣ] ⊧ σ → Provable T (⌜σ⌝ : V)`
   （`D3.lean:170`），其内部 `bold_sigma_one_complete`（`D3.lean:82`）靠
   `Bounding.Hierarchy.arithmetic_sigma₁_induction'` + 本地 `term_complete`（`D3.lean:45`，算术项求值）
   把公式结构归纳成 `T.internalize V ⊢ ⌜σ⌝`，再经 `tprovable_iff_provable` 转 `Provable T`。
2. `tprovable_iff_provable`（`Typed.lean:168`）**对任意 `Theory L` + `[T.Δ₁]` 通用**：
   `T.internalize V ⊢ ⌜φ⌝ ↔ Provable T (⌜φ⌝ : V)`。

### 11.2 决定性事实（决定 Phase 0.1 能不能机械平移）

- **`tprovable_iff_provable` 是通用的** → `𝗭𝗙𝗖.internalize V ⊢ ⌜ψ⌝ ↔ Provable 𝗭𝗙𝗖 (⌜ψ⌝ : V)` 对 ZFC 成立
  （`grep` 在 `Foundation/FirstOrder/` 下找不到 `def internalize`，说明 `internalize` 是某个类的通用投影，
  ZFC 作为 `Theory ℒₛₑₜ` 且 `[𝗭𝗙𝗖.Δ₁]` 已证（`ZFCDelta1.lean:43`），故可直接用）。
- **Foundation `SetTheory/` 目录下没有自己的 `internalize` / `Provable` / `tprovable_iff_provable`** →
  集合论版的 `set_sigma_one_complete` **必须在本包自建**（不能复用 Foundation 现成集合版），但结尾的
  `tprovable_iff_provable` 转换可直接复用通用版。
- **算术 `provable_internalize` 不能直接实例化到 ZFC 输出**：它形为
  `Provable T (...) → Provable T (...)`，`T` 必须是 `ArithmeticTheory`，输出理论也是算术的，
  而缺口要的是 `Provable 𝗭𝗙𝗖 (...)`（集合论输出）。所以**集合论版 `set_provable_internalize` 是刚需**，
  不能指望调一个算术引理就出来。

### 11.3 缺口的精确等价（关键简化）

经 `models_zfcTr_iff`（`Z0Full.lean:67`）：
```
Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)  ↔  V↓[ℒₒᵣ] ⊧ zfcTr τ
Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V)  ↔  V↓[ℒₒᵣ] ⊧ zfcTr (zfcTr τ)
```
（`Z0Full.lean` 已证 `zfcTr τ` 是算术 Σ₁ 句：`zfcTr_sigma1`）。
**故 `zfcTr_D3_internalize` 等价于 D3 对谓词 `zfcTr`：**
```
V↓[ℒₒᵣ] ⊧ zfcTr τ  →  V↓[ℒₒᵣ] ⊧ zfcTr (zfcTr τ)      （对所有 V ⊨ 𝗜𝚺₁）
```

### 11.4 Phase 0.1 可执行骨架（落 `ZFCSetSigma1.lean`）

```lean
-- 集合论项求值完全性（Foundation 无现成，仿 D3.lean:45 本地自建；
-- 因目标句都是 arithTrln.translate α 的翻译，项求值可借 arithTrln + eval_numeralF_iff
-- 还原到算术 term_complete，不必对通用集合项全做）
theorem set_term_complete {n} (t : ClosedSemiterm ℒₛₑₜ n) (w : Fin n → V)
    (h : V↓[ℒₒᵣ] ⊧ arithTrln.translate (term_as_arith t)) :
    𝗭𝗙𝗖.internalize V ⊢ (w ⤕ ⌜t⌝) ≐ ⌜t.valb w⌝ := ...

-- 集合论 Σ₁ 完全性（仿 bold_sigma_one_complete，归纳引擎换 setTheory_sigma₁_induction'）
theorem set_sigma_one_complete {ψ : SetTheorySentence}
    (hp : ℬ[∈, ℒₛₑₜ].Hierarchy 𝚺 1 ψ)
    (hV : V↓[ℒₛₑₜ] ⊧ ψ) : Provable 𝗭𝗙𝗖 (⌜ψ⌝ : V) := by
  apply (tprovable_iff_provable (T := 𝗭𝗙𝗖)).mpr
  apply Bounding.Hierarchy.setTheory_sigma₁_induction' hp
  -- 十个构造情形：verum/falsum/eq/neq/mem/nmem/and/or/ball/exs
  -- 每情形借 arithTrln 保真性 + eval_numeralF_iff（本包 NumeralSemantics.lean:30）+
  --   算术 numeral_* / term_complete 归约到 𝗭𝗙𝗖.internalize V ⊢ ...

-- 集合论内部化 D3（仿 provable_internalize）
theorem set_provable_internalize {ψ : SetTheorySentence}
    (h : Provable 𝗭𝗙𝗖 (⌜ψ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate ((provable 𝗭𝗙𝗖).val/[⌜ψ⌝])⌝ : V) := by
  simpa [models_iff] using set_sigma_one_complete (ψ := ...) (by simp)
```

### 11.5 闭合 `zfcTr_D3_internalize`（Phase 1）的精确配方

在 `V ⊨ 𝗜𝚺₁` 下，用 `set_provable_internalize`（ψ := `arithTrln.translate τ`）得
`Provable 𝗭𝗙𝗖 (⌜provabilityPredZFC (arithTrln.translate τ)⌝ : V)`；
再用 `iT_quote` 证明 `arithTrln.translate (zfcTr τ)` 与 `provabilityPredZFC (arithTrln.translate τ)`
在 ZFC 内可证等价（`zfcTr τ` 用 `iTDef y 0 ⌜τ⌝` 编码"翻译句"，与"直接码 `⌜arithTrln.translate τ⌝`"经
`iT_quote` 等价），由等价 + `Provable 𝗭𝗙𝗖` 的替换闭包得结论 `Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V)`。
替换 `Z0Blocked.lean:65` 的 `sorry` 即得无未证标记收据，Phase 2/3 走 `zfc_z0_full_of_D3_internalize` → `zfc_z0_full`。

### 11.6 诚实状态（本续作未编译任何新证明）

- 仅做了 Foundation 源码阅读与路线精化；**未新增任何编译通过的 Lean 证明**，`Z0Blocked.lean` 的 `sorry` 仍在。
- 下一步由接手工位 AI 按 §11.4–§11.5 落地，`/tmp/build_z0.py` 增量编译验证（§6 命令），严禁 `sorry` 进收据。
