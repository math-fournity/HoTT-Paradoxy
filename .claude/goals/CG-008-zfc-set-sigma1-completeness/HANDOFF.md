# CG-008 交接文档 · 2026-10-12（P3 结束态）

> 自包含。承接者读完本文件 + `GOAL.md` §3 的闭包表即可接手。
> 治理红线（F-011）不变：Foundation 只读；不碰 `sources/` 与 `private-audit/`；不 push `main`；不伪造收据。
> **本分支不得合并到原 repo 的 `dev`**（研究发起人 2026-10-11 明令）。

---

## P3 增量（2026-10-12，本轮）

**一句话**：把「缺口是什么」推进到「缺口**具体要造什么**」——
所有路线都归约到**同一条内部桥**，而它需要一件 Foundation 里**不存在**的东西：
**语法可计算的证明翻译**（从 𝗜𝚺₁ 推导到 𝗭𝗙𝗖 推导）。

**四条语言无关的机制全部排除**（各有确切原因，不要再试）：

| 机制 | 为什么不通 |
|---|---|
| `derivable_quote`（D1 引擎） | **方向相反**：元层推导 ⟹ 内部码；缺口要内部 ⟹ 内部 |
| `T.craig.Δ₁` | `Sh.craig` **有** `Δ₁`（`CraigTrick.lean:311`），`provable_D3` 可用；但结论句是 `provable Sh.craig`，与 `zfcTr` 的桥**等价于缺口** |
| `unprovable_flon`（抽象 G2） | 只需**单句** `FormalizedCompleteOn 𝐉`，但结论是 `flon`（形式化不矛盾律）**不是**一致性句；且 `Refutability.lean` 在 pinned build 里**未构建** |
| `rosser_internalize` | 语言无关且内嵌 `Proof T`，但方向是**元层 ⟹ 内部**，与 D1 同形 |

**一处自我更正**（`CG008Correction.lean`）：先前说「集合语义不在缺口的路径上」**过强**。
缺口的**陈述**确实纯算术（V 是 `𝗜𝚺₁` 模型，两句都是 `Provable 𝗭𝗙𝗖 (⌜·⌝ : V)`），
但 D3 的标准证法要**形式化 Σ₁ 完全性**，其算术版靠 `term_complete` + `toNumVec`
把 V 的元素代换成**数字项**；`ℒₛₑₜ` 无常项使这一步无对偶。
**故 P1 的 `hMem`/`hNMem` 分析是对的，它就是缺口的真正难点。**

**缺口的三种更精确形式**（本轮新得）：

1. **最具体**：`derivation 𝗭𝗙𝗖` 是**语言无关的 Δ₁ 不动点**（`Basic.lean:543`，只需 `[T.Δ₁]`），
   故缺口 = **在 𝗜𝚺₁ 内对 `derivation 𝗭𝗙𝗖` 做归纳**；
   `Fixpoint.induction` 是其**元层**版，Foundation 无内部版。
2. **最锐利**：对算术理论 `T`，D3 **是** Σ₁ 完全性的推论（取 `σ := □σ₀`，而 `□σ₀` 是 Σ₁）；
   缺口缺的**不是 D3 本身**，而是**跨语言可证性谓词的 Σ₁ 完全性**。
3. **前提最弱**：抽象 G2 的 `con_unprovable` 依赖链只在**一个句子** `𝐆 := gödel 𝔅` 上
   使用 `D3`，故 Z0 只需**一条实例**而非整族 `HBL3`（`CG008SingleD3.lean`）。

**但单句实例经 `provable_sigma_one_complete (T := 𝗜𝚺₁)` 归约到同一条内部桥**
（`CG008SingleD3Attack.lean`）。**前提确实减弱，要建的东西没变。**

**那条桥的解剖**（`CG008BridgeAnatomy.lean`）：

```
桥：𝗜𝚺₁ ⊢ provabilityPred 𝗜𝚺₁ ψ 🡒 zfcTr ψ
展开：∃ d : V, Proof 𝗜𝚺₁ d ⌜ψ⌝  ⟹  ∃ d' : V, Proof 𝗭𝗙𝗖 d' ⌜translate ψ⌝
```

**要在 V 内把 `d` 变成 `d'`——即语法可计算的证明翻译。**
而 `paInterp`（`PAModel.lean:246`）的 `interpret_theory` **走 `SetTheory.complete`**
（完备性定理，语义论证），只给**元层**结论，**不产生 V 内的编码**。
`of_provability` 同理（`CG008InterpretationWall.lean`）。

**所以缺口要的是**：一个语法可计算的证明翻译（𝗜𝚺₁ 推导 ⟹ 𝗭𝗙𝗖 推导）。
**Foundation 里没有——算术侧没有，集合侧也没有。**

**本轮收据**：`2026-10-12-CG001-CG008-MECHANISM-SURVEY-01`（74 源，`KERNEL_ACCEPTED_WITH_SCOPE`
/ `PASS_WITH_SCOPE` / `replay: EXACT_EXIT_STDOUT_STDERR_MATCH`）；证据索引 §45。

---

# （以下为 2026-10-11 P2 结束态，保留）

> 自包含。承接者读完本文件 + `GOAL.md` §3 的闭包表即可接手。
> 治理红线（F-011）不变：Foundation 只读；不碰 `sources/` 与 `private-audit/`；不 push `main`；不伪造收据。

---

## 0. 一句话诚实状态

**Z0 完整形式仍未机器证明；`Z0Blocked.lean:65` 的 `sorry` 仍在。**
2026-10-11 共五轮：P1 建成集合语言内部演算工具层并把缺口**等价归约**成内部演算形状；
P2 四轮建成 `Derivable` 编码层工具集、把缺口**定型**为集合语言的 `provable_internalize`
并进一步改述为 **`zfcTr.HBL3`**、**证明它不可能靠补实例绕过**、
最后把待补位置**定义**出来（`CrossLanguageD3`）。
**归约、桥、定义都是变换，不是证明。**

**P2 的净结论**：缺口**没有缩小**，但**定位精度大幅提高**，
且现在可以说明**为什么它不能被绕过**——两条剩余的路各被一条**数学必然**堵死
（`Sh.Δ₁` 不可能成立 = G1；`HBL3` 只在同语言时可陈述）。
补上缺口需要**扩展 Foundation 的抽象框架**（或为跨语言情形单开一条路），
而不是填实例或补桥。

**本轮也纠正了 `CLAIM.md` §4.1.1**：它把缺口定位为「缺失的 `Theory.Δ₁ Sh` 实例」——
方向对，但那条路**不可能**走通（新增 §4.1.3 说明原因）。

---

## 0.5 给承接者的第一条命令

```bash
cd /Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911/dev-ef7e5239 && git log --oneline -5 && git status --short
```

工作树应干净、HEAD 应等于 `origin/workbuddy/dev-ef7e5239`。
本分支**不得合并到原 repo 的 `dev`**（研究发起人 2026-10-11 明令）。

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
cd /Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911/dev-ef7e5239 && python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/2026-10-11-CG001-CG008-CROSSLANG-DEF-01 --rerun
```

  （把 `--run-dir` 换成下面 §2 表中任一运行名即可核对该轮。）

---

## 2. 五轮产出（收据全部过核）

**五份收据，判词一律** `KERNEL_ACCEPTED_WITH_SCOPE` / `PASS_WITH_SCOPE` /
`replay: EXACT_EXIT_STDOUT_STDERR_MATCH`；**外部件 553 项全部 pin 校验通过**；
**stderr 0 B、exit 0**；**公理只有 `propext` / `Classical.choice` / `Quot.sound`**。

| # | 运行 | 源 | 内容 |
|---|---|---|---|
| P1 | `2026-10-11-CG001-CG008-SET-INTERNAL-01` | 35 | 集合语言内部演算层 + 缺口等价归约 |
| P2.1 | `2026-10-11-CG001-CG008-DERIVABLE-LAYER-01` | 46 | `Derivable` 编码层工具集 + 缺口定型 |
| P2.2 | `2026-10-11-CG001-CG008-HBL3-LOCATION-01` | 52 | 缺口 = `zfcTr.HBL3`；卡点定位 |
| P2.3 | `2026-10-11-CG001-CG008-CROSS-LANGUAGE-WALL-01` | 58 | 跨语言墙：两条路各堵一半 |
| P2.4 | `2026-10-11-CG001-CG008-DELTA1-NECESSITY-01` | 60 | 两条数学必然（`Sh.Δ₁` 不可能 = G1） |
| P2.5 | `2026-10-11-CG001-CG008-CROSSLANG-DEF-01` | 62 | `CrossLanguageD3` 定义 + 解释墙 |

证据索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §39–§44。

### 2.1 P1 的文件（集合语言工具层）

**运行**：`2026-10-11-CG001-CG008-SET-INTERNAL-01`
**规模**：35 源文件、553 外部件（全部 pin 校验通过）、96.0 秒、stderr 0 B、exit 0

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
| **`GodelQ/ZFC/CG008HBL3.lean`** | **缺口 = `zfcTr.HBL3`**；充分条件 `FormalizedCompleteOn` | ✅ |
| **`GodelQ/ZFC/CG008HBL3Test.lean`** | D1 前提在元层、D3 在系统内；`Provable.complete` 硬编码 ℕ | ✅ |
| **`GodelQ/ZFC/CG008Final.lean`** | 三重等价形状 + 卡点 + 诚实降格（**先读这个**） | ✅ |
| **`GodelQ/ZFC/CG008Delta1Wall.lean`** | **`Sh.Δ₁` 不可能成立 = G1 的必然** | ✅ |
| **`GodelQ/ZFC/CG008CrossLanguage.lean`** | **`CrossLanguageD3` 定义**（待补的位置） | ✅ |
| **`GodelQ/ZFC/CG008InterpretationWall.lean`** | 解释墙：`of_provability` 走完备性，给不出系统内编码 | ✅ |
| `GodelQ/ZFC/CG008Sigma1.lean` | 十情形工具清单 | 探针 |
| `GodelQ/ZFC/CG008MemCase.lean` | 剩余障碍的精确分析 | 探针 |
| `GodelQ/ZFC/CG008Probe1–21.lean` | 逐条查实的编译探针（4、11、12、15、20、21 是证伪/归约） | 探针（非收据） |

---

## 3. P1 的三个实质结论

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

**P2 的后续工作表明：§3.3 的 `hMem`/`hNMem` 障碍不是最终障碍**——
P2 换了一条通道（`Derivable` 编码层，没有「自由变量」概念），
并把缺口定型为 `zfcTr.HBL3`，从而绕开了十情形的框架。见下面 §3.5。

### 3.4 P2 的第一项实质结论：缺口是 **D3**，不是 Σ₁ 完全性

先前的记录（含 `Z0Blocked.lean` 文档第 16-18 行）把缺口说成「反射原理，不可能」。
**那个判断针对的句子不是缺口**。缺口的前提是
「V 内部**有一条推导**」（`Provable`），不是「该句为真」。
从「推导存在」到「可证性句可证」是 **Σ₁ 完全性**，不是**反射原理**。

进一步：缺口也不是「𝗭𝗙𝗖 证明自己的 Σ₁ 完全性」（那会推出 `Con`，矛盾），
而是 **HBL 的 D3**（`□σ → □□σ`）——对 Σ₁ 可证性谓词它是**真的且可证的**。
区别在于 D3 ≠ Σ₁ 完全性。见 `CG008SetSigma1Complete.lean`、`CG008Probe13.lean`。

### 3.5 P2 的最终结论：跨语言墙

**缺口 = `zfcTr.HBL3`**（`CG008HBL3.lean`）。Foundation 已给充分条件实例
`[∀ σ, 𝔅.FormalizedCompleteOn (𝔅 σ)] → 𝔅.HBL3`，故缺口 = 建成
`∀ σ, zfcTr.FormalizedCompleteOn (zfcTr σ)`。

**它不白送**，因为 D1 与 D3 的前提在**不同的层**：

| | D1（已建成） | D3（缺口） |
|---|---|---|
| 前提位置 | **元层**（`Sh ⊢ σ`） | **系统内**（`zfcTr σ`，即 `V ⊨ zfcTr σ`） |
| 桥 | `internalize_provability` 白送 | ❌ 无 |

唯一的回程桥 `Provable.complete`（`D1.lean:35`）把 `ℕ` **硬编码**，无 `V ⊨ 𝗜𝚺₁` 版本。

**两条路各堵一半，堵的是同一件事**：

| 路 | 结构 | 语言 | `Δ₁` | `HBL3` |
|---|---|---|---|---|
| 1 | `zfcTr : Provability 𝗜𝚺₁ Sh` | 同（`ℒₒᵣ`） | ❌ **不可能** | ✅ 可陈述（缺口所在） |
| 2 | `𝗭𝗙𝗖.standardProvability : Provability 𝗜𝚺₁ 𝗭𝗙𝗖` | 跨 | ✅ 有 | ❌ **不可陈述** |

- 路 1 的 `Δ₁` **不可能**成立：`Δ₁` 的 `mem_iff` 要精确刻画公理集，
  而 `Sh` 的「公理」是 𝗭𝗙𝗖 的**定理**（成员判定 Σ₁、补 Π₁）；
  若 `Sh.Δ₁` 成立 ⇒ 𝗭𝗙𝗖 定理集递归 ⇒ **与 G1 矛盾**（`CG008Delta1Wall.lean`）。
- 路 2 的 `HBL3` **不可陈述**：`D3` 要 `𝔅 σ : Sentence L`，而 `𝔅.pr : Sentence L → Sentence L₀`
  （`HBL2` **是**多语言的，两者独立）。（`CG008Probe17-20.lean`）

**根本原因**：ZFC 的可证性谓词把 `ℒₛₑₜ` 句映到 `ℒₒᵣ` 句。

**解释墙**（`CG008InterpretationWall.lean`）：`of_provability`（`LK/Interpretation.lean:443`）
的证明走**完备性**（`complete_on_eq_models`）——**语义论证，不构造证明对象**；
而缺口要 **𝗜𝚺₁ 内部的证明**（展开后需 V 内部的证明编码 `d`）。

**待补位置已定义**：`CG008CrossLanguage.CrossLanguageD3`
（`∀ σ, T₀ ⊢ 𝔅 σ 🡒 𝔅' σ`，`𝔅' : Sentence L → Sentence L₀`），
缺口是它的一个实例（`gap_is_cross_language_D3`）。

---

## 4. 下一步（P2 结束态）

**缺口的三重等价形状**（详见 `GodelQ/ZFC/CG008Final.lean`）：

| # | 形状 | 出处 |
|---|---|---|
| 1 | `Provable 𝗭𝗙𝗖 ⌜translate τ⌝ → Provable 𝗭𝗙𝗖 ⌜translate (zfcTr τ)⌝` | `Z0Blocked.lean:61-65` |
| 2 | 集合语言的 `provable_internalize`（与 `D3.lean:175` 逐字同形，只差 `T : ArithmeticTheory` → `𝗭𝗙𝗖 : Theory ℒₛₑₜ`） | `CG008GapShape.lean` |
| 3 | **`zfcTr.HBL3`**，即 `∀ σ, 𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr (zfcTr σ)` | `CG008HBL3.lean` |

**下一步候选（按建议顺序）**：

1. **主路——扩展框架**：Foundation 的抽象框架是为**同语言**情形设计的
   （`HBL3` 只在 `L = L₀` 时可陈述）。缺口需要的是它的**跨语言推广**，
   而那个位置**已经定义好**：`CG008CrossLanguage.CrossLanguageD3`。
   承接者应判断：是给 Foundation 加一条跨语言的路，
   还是在 `HoTT/formal/` 侧自建（后者不碰 Foundation，符合 F-011）。
2. **备路——照实降格**：若研究发起人裁定不扩展框架，把缺口作为**显式前提**交付。
   `Z0Bridge.lean` 的 `zfc_z0_full_of_sigma1_bridge` 已备好这个归约：
   前提一旦给出，`zfc_z0_full_of_D3_internalize` 立即闭合 Z0。
3. **已排除，不要重试**：见下表。

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
GodelQ/ZFC/CG008BridgeAnatomy.lean | **P3 先读这个**：所有路线归约到的那条桥 + 它要造什么
GodelQ/ZFC/CG008SingleD3.lean | P3：抽象 G2 只需单句 D3（前提最弱形式）
GodelQ/ZFC/CG008Correction.lean | P3：更正我自己的过强说法——P1 的障碍就是缺口难点
GodelQ/ZFC/CG008Final.lean | 三重等价形状 + 卡点 + 为什么绕不开
GodelQ/ZFC/CG008CrossLanguage.lean | **待补的位置**：CrossLanguageD3 的定义
GodelQ/ZFC/CG008Delta1Wall.lean | Sh.Δ₁ 不可能成立 = G1（不要再试补 Δ₁ 实例）
GodelQ/ZFC/CG008InterpretationWall.lean | of_provability 走完备性，给不出系统内编码
GodelQ/ZFC/CG008HBL3.lean | 缺口 = zfcTr.HBL3；充分条件 FormalizedCompleteOn
GodelQ/ZFC/CG008GapShape.lean | 缺口的六步等价链与已排除的路
GodelQ/ZFC/Z0Blocked.lean | 待消除的精确 sorry（第 65 行）
GodelQ/ZFC/Z0Full.lean | zfcTr:35、models_zfcTr_iff:67、zfc_z0_full_of_D3_internalize:117
GodelQ/ZFC/Z0Bridge.lean | 备路：把缺口收成显式前提 bridge 的归约
GodelQ/ZFC/InternalTranslate.lean | iT_quote:611
GodelQ/ZFC/ZFCDelta1.lean | [𝗭𝗙𝗖.Δ₁] 已证
CG008_HANDOFF.md | 立项交接（包内根目录）
CG008_PROJECT.md | 立项书（包内根目录）
CLAIM.md | 本包声明；§4.1.3 是本轮的更正
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/Incompleteness/ProvabilityAbstraction/Basic.lean | 抽象框架：Provability:25、HBL2:56、HBL3:62、FormalizedCompleteOn:87
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/Incompleteness/StandardProvability.lean | provable_D1:33、provable_D2:37、provable_D3:71、standardProvability:42、HBL3 实例:90
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Theory.lean | Δ₁ 的定义:16（mem_iff 双向）
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D1.lean | internalize_provability:27、Provable.complete:35（硬编码 ℕ）
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean | 要平移的算术机器；sigma_one_provable_of_models:162、provable_internalize:175
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/LK/Interpretation.lean | of_provability:443（走完备性）
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/SetTheory/Basic/Misc.lean | SetTheory.complete:269
.claude/goals/CG-008-zfc-set-sigma1-completeness/工作台.md | 本目标包的完整决策、事故与翻查记录
形式化追踪/README.md | 各线现状总览
形式化追踪/01-有哥德尔路线/02-Z0-条件形式与剩余三步.md | Z0 的状态与剩余步骤
```

---

## 6. 治理

- 提交按**精确路径**；推送本 worktree 分支 `workbuddy/dev-ef7e5239`。
- **不得合并到原 repo 的 `dev`**（研究发起人 2026-10-11 明令）；不 push `main`；不伪造收据；不调用 Agent 工具。
- **删除只进废纸篓，且用绝对路径 `~/bin/rm-trash`**（Bash 工具的 shell 未必加载 zsh alias，
  别名不在时 `rm` 会真删）。**删任何路径前先 `ls` 它**——
  本会话曾因把 `HoTT` 误写成 `HoTt` 后 `rm -rf HoTt` 而删掉整棵树
  （macOS 大小写不敏感，两者是同一路径）；已从废纸篓与 git 全部恢复，详见工作台 §2.5。
- 共享文件（`CLAIM.md`、`形式化追踪/`、`.claude/总索引*`、证据索引）已按最小改动更新。
  `CLAIM_EVIDENCE_MATRIX.md` 未从本 worktree 更新（见证据索引各轮的
  `shared_matrix_index: NOT_INDEXED_RELAY_DRAFT_ONLY`）。
