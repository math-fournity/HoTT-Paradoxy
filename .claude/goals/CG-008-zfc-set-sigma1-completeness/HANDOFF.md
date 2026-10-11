# CG-008 交接文档 · 2026-10-11（P2 结束态）

> 自包含。承接者读完本文件 + `GOAL.md` §3 的闭包表即可接手。
> 治理红线（F-011）不变：Foundation 只读；不碰 `sources/` 与 `private-audit/`；不 push `main`；不伪造收据。

---

## 0. 一句话诚实状态

**Z0 完整形式仍未机器证明；`Z0Blocked.lean:65` 的 `sorry` 仍在。**
2026-10-11 三轮：P1 建成集合语言内部演算工具层并把缺口**等价归约**成内部演算形状；
P2 建成 `Derivable` 编码层工具集、把缺口**定型**为集合语言的 `provable_internalize`
（进而改述为 **`zfcTr.HBL3`**），并证伪/归约了**六条**候选路线。
**归约与桥都是变换，不是证明。**

**P2 的净结论**：缺口**没有缩小**，但**定位精度大幅提高**，
且现在可以说明**为什么它不能被绕过**——两条剩余的路各被一条**数学必然**堵死
（`Sh.Δ₁` 不可能成立 = G1；`HBL3` 只在同语言时可陈述）。
补上缺口需要**扩展 Foundation 的抽象框架**（或为跨语言情形单开一条路），
而不是填实例或补桥。

---

## 1. 环境与工作根

- **工作根**：worktree `/Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911/dev-ef7e5239`
- **分支**：`workbuddy/dev-ef7e5239`；远端 `origin` = `https://github.com/mathfournity/HoTT-Paradoxy.git`
- **包根**：`HoTT/formal/claude-cg001/godel-q-zfc-z0-full/`
- **构建**（Bash cwd 不跨命令持久，**必须在同一条命令内 cd**）：

```bash
cd /Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911/dev-ef7e5239 && python3 -B .claude/goals/CG-008-zfc-set-sigma1-completeness/tools/build_z0.py --no-pin-check --package HoTT/formal/claude-cg001/godel-q-zfc-z0-full GodelQ/ZFC/<file>.lean
```

  本轮已把驱动与构建顺序从 `/tmp` 复制进仓库（`tools/` 下）：
  - `build_z0.py` — 驱动。**olean 缓存默认落在 `tools/../olean-cache/`**（本包内，已 gitignore），
    不再写 `/tmp`；可用环境变量 `Z0_BUILD_DIR` 覆盖。
  - `z0_build_order.txt`（探针用，26 文件，末位 `Z0Probe.lean`）
  - `z0_receipt_build_order.txt`（收据用，25 文件，不含 `Z0Probe`）
  - `prior-line-scaffolds/` — 先前 D3 攻坚线的试验脚手架（`compile_deps.sh`、`iter.sh`、
    `probe.py`、`LEANPATH`、`claim.py`、`neg.py`、`handoff.py`），逐字节保存，见其 README。

  不再依赖 `/tmp`。中间探针加 `--no-forbidden-check`；**收据文件不加**。
  **首次使用**（缓存为空）要按顺序跑完整依赖前缀，见 `z0_receipt_build_order.txt`；
  之后增量编译只跑目标文件即可。

  另：2026-10-10 的独立复核报告已从 `/tmp` 保存到 `audit/20261010-keyE缺口审计-独立复核.md`
  （该报告判定「缺口缩小到 `keyE`」是重新包装而非缩小，与本轮结论一致）。

- **正式收据**（带 pin 校验 + 禁用标记检查 + 精确重放）：

```bash
cd /Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911/dev-ef7e5239 && python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/2026-10-11-CG001-CG008-SET-INTERNAL-01 --rerun
```

---

## 2. 本轮产出（收据已过核）

**运行**：`2026-10-11-CG001-CG008-SET-INTERNAL-01`
**判词**：`KERNEL_ACCEPTED_WITH_SCOPE` / `PASS_WITH_SCOPE` / `replay: EXACT_EXIT_STDOUT_STDERR_MATCH`
**规模**：35 源文件、553 外部件（全部 pin 校验通过）、96.0 秒、stderr 0 B、exit 0
**公理**：全部报告只有 `propext` / `Classical.choice` / `Quot.sound`

| 文件 | 内容 | 可进收据 |
|---|---|---|
| `GodelQ/ZFC/ZFCSetInternal.lean` | 集合语言内部演算 13 条 + 引号求值 2 条 | ✅ |
| `GodelQ/ZFC/CG008Reduce.lean` | 缺口 → 内部演算形状的**等价归约**（4 条定理） | ✅ |
| `GodelQ/ZFC/CG008SetComplete.lean` | Σ₁ 归纳的层次分析 | ✅ |
| `GodelQ/ZFC/CG008SetAll.lean` | 全称引入 / 全称消去 / Lévy 有界全称引入 / 成员等号替换 | ✅ |
| `GodelQ/ZFC/CG008Raw.lean` | typed ↔ 编码层的双向桥 | ✅ |
| `GodelQ/ZFC/CG008RawSigma1.lean` | 17 条 typed 引理下沉为 14 条 `d_*` | ✅ |
| `GodelQ/ZFC/CG008GapShape.lean` | 缺口的六步等价链（记录文件） | ✅ |
| `GodelQ/ZFC/CG008ProofToProvable.lean` | 缺口「平凡一半」的机器化 | ✅ |
| `GodelQ/ZFC/CG008SetProvInt.lean` | 算术 `provable_internalize` 路线的逐步核对 | ✅ |
| `GodelQ/ZFC/CG008SetSigma1Complete.lean` | 缺口 = 集合语言 `provable_internalize` 的定型 | ✅ |
| `GodelQ/ZFC/CG008Sigma1.lean` | 十情形工具清单 | 探针 |
| `GodelQ/ZFC/CG008MemCase.lean` | 剩余障碍的精确分析 | 探针 |
| `GodelQ/ZFC/CG008Probe1–12.lean` | 逐条查实的编译探针（4、11、12 是三条证伪） | 探针（非收据） |

**运行**：`2026-10-11-CG001-CG008-SET-INTERNAL-01`（P1）与
`2026-10-11-CG001-CG008-DERIVABLE-LAYER-01`（P2），均 `KERNEL_ACCEPTED_WITH_SCOPE`
/ `PASS_WITH_SCOPE` / `replay: EXACT_EXIT_STDOUT_STDERR_MATCH`。

---

## 3. 本轮三个实质结论

### 3.1 交接单的头号障碍被解除（原判过强）

`CG008_HANDOFF_2026-10-11.md` §4.2 与 `CG008_PROJECT.md` §5 都把
「集合语言的内部化演算辅助（`eq_refl`/`eq_symm`/`subst_eq`/`K_intro`/`ball_intro`/`bexs_intro`/`ball_replace`）
在 Foundation 里只为 `Term V ℒₒᵣ` 定义，需自建」列为头号风险。**该判断过强。**

读 `EquationalTheory.lean:36-70` 可见那套证明只依赖三样：
`complete`（模型→元层推导）、`internal_provable_of_outer_provable`（`D1.lean:32`）、
`TProof.specialize!`（`Typed.lean:462`）。后两者**只要求 `T : Theory L` + `[T.Δ₁]`**，与 `L` 无关；
`K_intro`/`A_intro_left`/`A_intro_right`/`TProof.exs!` 来自 `Entailment.Minimal` 的
`InternalTheory V L` 实例，同样通用。唯一 ℒₒᵣ 专属的只有两处：
`complete` 的来源（换 `SetTheory.complete`，`Misc.lean:269`）与等式记号 `≐`。

**结论**：不是从零发明十情形，是**换 API 来源**。

### 3.2 §4 第 2 步的陈述有类型缺陷

§4 写的 `set_sigma_one_complete` 前提取 `V↓[ℒₛₑₜ] ⊧ ψ`，但缺口的 `V` 只有 `[V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]`。
探针 `CG008Probe3.lean` 查实：`SetStructure V` 在此上下文**能被 `infer_instance` 合成、不报错**，
但合成到的是 `Arithmetic/Exponential/Bit.lean:28` 的比特编码 `Membership` 实例——
会**静默**给出语义错误的引理。

**对照**：英文原版交接（GUI 导出第 1518 行起）写的是
`set_sigma_one_complete {V} [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖] …`——
带 `[V↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖]`。中文版 §4 丢掉了它，而它正是关键。

### 3.3 真正的剩余障碍是 `hMem` / `hNMem`（**最重要**）

`CG008Sigma1.lean` 逐条核对 `setTheory_sigma₁_induction'` 的十情形：

| 情形 | 工具 | 现状 |
|---|---|---|
| `hVerum` / `hFalsum` | `Minimal.verum`；语义前提为假 | ✅ |
| `hEQ` / `hNEQ` | `set_eq_refl`/`set_eq_symm`/`set_ne_symm` | ◐ 只对闭项 |
| **`hMem` / `hNMem`** | **——** | **❓ 缺** |
| `hAnd` / `hOr` | `set_K_intro` / `set_A_intro_left/right` | ✅ |
| `hBall` | `set_ball_intro` | ✅ 本轮补上 |
| `hExs` | `set_exs_intro` | ✅ |

**为什么它是障碍**：算术版 `bold_sigma_one_complete`（`D3.lean:82`）的 `P`（`revert w` 之后）是
`fun n φ ↦ ∀ w, V ⊧/w φ → T.internalize V ⊢ (toNumVec w ⤔ ⌜φ⌝)`——
**带语义前提**，且结论用 `toNumVec w ⤔ ⌜φ⌝` 把自由变量代换成**数字项**，落回闭句层。

**`ℒₛₑₜ` 没有常项与函数符号**（已用 `IsEmpty ((ℒₛₑₜ).Func 0)` 机器确认），
所以「把自由变量的值命名成项」这一步**在集合语言里没有对偶**。
这是集合版比算术版**实质更难**的地方。

---

## 4. 下一步（按可行性排序）

**缺口的最终形状**（本轮定型，详见 `GodelQ/ZFC/CG008GapShape.lean` 的六步链）：
它是**集合语言的 `provable_internalize`**——与算术版 `D3.lean:175` 逐字同形，
只差 `T : ArithmeticTheory` → `T = 𝗭𝗙𝗖 : Theory ℒₛₑₜ`；
最终落在 **V 内部对 Δ₁ 谓词 `Derivation` 的完全性**。

**下一步候选**：
1. **在 `Derivable` 编码层做**（`CG008Raw.lean` 的发现）：该层**没有「自由变量」概念**，
   所以算术版 `toNumVec` 的障碍在那里可能不存在。
   `CG008RawSigma1.lean` 的 14 条 `d_*` 已是该层的工具集。
2. 若卡住，照实降格：把「需要集合语言 Σ₁ 完全性」写成精确的显式前提定理（仿 `Z0Bridge.lean`），
   写明卡点，不伪造收据。

**已排除的路（都有编译实证，不要重试）**：

| 路 | 为什么不行 | 证据 |
|---|---|---|
| 内部蕴含句 `⌜translate τ 🡒 translate (zfcTr τ)⌝` + modus ponens | 那**正是反射原理**，即哥德尔第二定理的内容，循环 | `CG008Probe4.lean` |
| 载体重接到标准模型（把 `: V` 改写成 `: ℕ`） | 类型错误——Gödel 报价把载体类型编码进结果值 | `Z0Probe6/7.lean` |
| `Sh.craig` / `Δ₁ Sh` 捷径 | `Sh.Δ₁` **不可能**成立（见下） | `Z0D3Attempt.lean` |
| 廉价传递 `Con(Sh.craig) ↔ Con(𝗭𝗙𝗖)` | 坍缩为同一 D3 缺口 | `Z0Final.lean` |
| **Σ₁ 绝对性把 V 真降到 ℕ** | **方向反了**——`sigma_one_upward` 沿 `ι : M ↪ₛ N`，而 `natCastEmbedding : ℕ ↪ₛ V`；Σ₁ 只**向上**绝对 | `CG008Probe12.lean` |
| `SoundOnHierarchy` 桥（`Absoluteness.lean:121-152`） | 定义在 `ArithmeticTheory` 上，且那是**反方向**（真⟹可证，靠可靠性） | `CG008Probe11.lean` |
| **借 `standardProvability` 白送的 `HBL3`** | `Sh` 无 `Δ₁`；且 `Sh.standardProvability` **连提及都不行** | `CG008Probe15.lean` |
| **走 `𝗭𝗙𝗖.standardProvability : Provability 𝗜𝚺₁ 𝗭𝗙𝗖`** | 结构**能建成**（`LORDefinable ℒₛₑₜ` 与 `𝗭𝗙𝗖.Δ₁` 都有），但 `HBL3` **连陈述都不行**：`D3` 要 `𝔅 σ : Sentence L`，而 `𝔅.pr : Sentence L → Sentence L₀` | `CG008Probe17-20.lean` |
| **把 `sigma_one_provable_of_models` 的 `T` 换成 `𝗭𝗙𝗖`** | 归约回缺口本身（该引理要 `T : ArithmeticTheory`，且证明依赖 `term_complete`/`toNumVec`，`ℒₛₑₜ` 无常项） | `CG008Probe21.lean` |

**两条数学必然**（不是工程缺口，不要试图「补实例」）：

1. **`Sh.Δ₁` 不可能成立**——`Δ₁` 的 `mem_iff` 要精确刻画公理集；
   而 `Sh` 的「公理」是 𝗭𝗙𝗖 的**定理**，其成员判定是 Σ₁、补是 Π₁。
   若 `Sh.Δ₁` 成立 ⇒ 𝗭𝗙𝗖 定理集递归 ⇒ **与 G1 矛盾**。（`CG008Delta1Wall.lean`）
2. **`HBL3` 只在 `L = L₀` 时可陈述**——`D3 : T₀ ⊢ 𝔅 σ 🡒 𝔅 (𝔅 σ)` 要
   `𝔅 σ : Sentence L`，而 `𝔅.pr : Sentence L → Sentence L₀`。
   注意 `HBL2` **是**多语言的（两边都落在 `L₀`），两者是独立的类，不可混同。
   （`CG008Probe20.lean`）

**跨语言墙的最终形式**：ZFC 的可证性谓词把 `ℒₛₑₜ` 句映到 `ℒₒᵣ` 句。
这个跨语言性要么让 `Δ₁` 丢失（走 `zfcTr : Provability 𝗜𝚺₁ Sh` 那条路），
要么让 `HBL3` 无法陈述（走 `𝗭𝗙𝗖.standardProvability` 那条路）。

**已解除的障碍**（原判为卡点，实为换 API 来源）：
- 集合语言的内部化演算辅助（`ZFCSetInternal.lean`）；
- 集合语言的全称引入（`CG008SetAll.lean`）。

**纠一处误诊**：`Z0Blocked.lean` 文档第 16-18 行否定的 `zfcTr_D3_syntactic`
**不是**缺口的形状——缺口前提是「V 内部**有一条推导**」（Σ₁ 完全性），
不是「该句为真」（反射原理）。这个区分是缺口不循环的原因（`CG008SetSigma1Complete.lean`）。
（第二轮又进一步改述为 **`zfcTr.HBL3`**，见 `CG008HBL3.lean`。）

---

## 5. 闭包（恢复时用 Read 重读）

```goal-x-closure
# 路径 | 用途
最高指示-Claude版.md | 操作指令
CG008_HANDOFF_2026-10-11.md | 上一轮交接（包内根目录）
GodelQ/ZFC/CG008GapShape.lean | **缺口的六步等价链与本轮已排除的路（先读这个）**
CG008_HANDOFF.md | 立项交接（包内根目录）
CG008_PROJECT.md | 立项书（包内根目录）
GodelQ/ZFC/Z0Blocked.lean | 待消除的精确 sorry（第 65 行）
GodelQ/ZFC/Z0Full.lean | zfcTr、models_zfcTr_iff:67、zfc_z0_full_of_D3_internalize:117
GodelQ/ZFC/ZFCSetInternal.lean | 本轮建成：集合语言内部演算层
GodelQ/ZFC/CG008Reduce.lean | 本轮建成：缺口 → 内部形状的等价归约
GodelQ/ZFC/CG008SetAll.lean | 本轮建成：全称引入与 Lévy 有界全称引入
GodelQ/ZFC/CG008MemCase.lean | 本轮建成：剩余障碍的精确分析
GodelQ/ZFC/CG008Sigma1.lean | 十情形工具清单
GodelQ/ZFC/InternalTranslate.lean | iT_quote:611
GodelQ/ZFC/ZFCDelta1.lean | [𝗭𝗙𝗖.Δ₁] 已证
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean | 要平移的算术机器
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/SetTheory/Basic/Hierarchy.lean | setTheory_sigma₁_induction':63（十情形）
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/SetTheory/Basic/Misc.lean | SetTheory.complete:269
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Typed.lean | tprovable_iff_provable:168、TProof.all!:489
.claude/goals/CG-008-zfc-set-sigma1-completeness/工作台.md | 本目标包的完整决策与翻查记录
形式化追踪/README.md | 各线现状总览
形式化追踪/01-有哥德尔路线/02-Z0-条件形式与剩余三步.md | Z0 的状态与剩余步骤
```

---

## 6. 治理

- 提交按**精确路径**；推送 `dev` 分支（本 worktree 分支 `workbuddy/dev-ef7e5239`）。
- 不 push `main`；不伪造收据；删除只进废纸篓；不调用 Agent 工具。
- 共享文件（`CLAIM_EVIDENCE_MATRIX.md`、`形式化追踪/`、`.claude/总索引*`）已按最小改动更新。
