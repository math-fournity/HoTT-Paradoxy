# CG-007「Z0 完整形式」——给下一个 Session 的接手提示词

> 写出者：WorkBuddy 会话（第三轮接手复核），2026-10-11 01:2x。
> 我这一轮**没有证出新命题**（详见 §11）。本提示词的目标不是转述我的成果，而是把你准确放到
> 当前真正的战场上，并把我核到的"基线已过期"这个陷阱提前拆掉。

---

## 0. 你是谁、在哪、第一件事（最重要，先读完这一节再动手）

你是 CG-007（"Z0 完整形式"：把 𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖) 做到机器证明）的下一个工作单元。
用户是研究发起人，简体中文回答，回答要诚实、区分"已证 / 已读码 / 我判断"。

你的工作目录（cwd）是：

```
/Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911/dev-4d788035
分支 workbuddy/dev-4d788035，HEAD 87b65dfd
```

**⚠️ 这个 cwd 已经过期 13 个提交，不要在这里直接开工。**

canonical 工作根是 **`/Volumes/D/HoTT_AI_HANDOFF_20260911`**（分支 `dev`，我核到时 HEAD = `273ac2e7`）。
更要紧的是：**并行会话的大量增量还躺在那个工作树里、从未提交**——`GodelQ/ZFC/Z0UniBridge.lean`、
`Z0Layer1.lean`、`Z0Layer1Emb.lean`、`SeqTranslateFormula.lean` 的改动、4 组运行收据目录、
`tools/`（`devbuild.py` / `lean_probe.py` / `devbuild_ns.py`）、以及两份新交接
（`HANDOFF-2026-10-11-Z0D3-SESSION-3.md`、`HANDOFF-2026-10-11-Z0D3-SESSION-4.md`）。
**这些文件不在任何 commit 里**——你若在 `dev-4d788035` 这个 worktree 里工作，会完全看不到它们，
从而在错误的基线上重复劳动。

所以第一件事，无条件执行：

```bash
cd /Volumes/D/HoTT_AI_HANDOFF_20260911
git log --oneline -1      # 先看 HEAD 有没有又动过（研究发起人会不定时把增量提交上去）
git status --short        # 看并行会话的未提交增量还在不在（在 = 你必须以工作树为准，不要 reset）
```

若你必须留在 `dev-4d788035`：先 `git merge --ff-only dev`（`dev` 是同一仓库的本地 ref，
可 fast-forward 到 `273ac2e7`），但这**仍然拿不到未提交文件**，所以结论还是去主检出。

---

## 1. 一分钟状态

| 项 | 状态 |
|---|---|
| 八方向 worktree 形式化覆盖 | **已全部有 `dev` 上可重放的收据**（dev-09 缺口由 CG001-C-387 补上） |
| Z0 **影子**形式 C-120（`Sh ⊬ Sh.craig.consistent`） | **无条件成立**，不受任何未完成项影响 |
| Z0 **完整**形式（`𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`） | **仍未证**。只差一条引理 |
| 唯一缺口 | `ShCraigElim` / `internalized_of_provability`（精确形状见 §4） |
| 已证的可复用机制 | ① `Sh.craig` 的完整 D3（`(Sh.craig.standardProvability).HBL3 := inferInstance`）；② 宇宙多态桥 `models_zfcTr_iff'` + `bwd_of_shcraig_elim`（CG001-C-390） |
| 最新编号 | `dev` 共享 `C-NNN` 下一个 **C-391**；Claude 线 `CG001-C-NNN` 下一个 **C-391** |

---

## 2. 必读顺序（按此顺序，别跳）

1. `/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/goals/CG-007-formalization-completion/HANDOFF-2026-10-11-Z0D3-SESSION-4.md`
   （**最新**，Codex 9276：宇宙多态桥 + `bwd` 归约 + 新收据 CG001-C-390 + 两条路径）
2. 同目录 `HANDOFF-2026-10-11-Z0D3-SESSION-3.md`
   （**并行会话** WorkBuddy：W9c 归位 + W8 第二层公式保持性地基，9 条已证引理）
   —— 这两份是**并行会话的两份交接，互不覆盖，都要读**。
3. 同目录 `W8-下一单元-V内部语法解释定理-规格.md`（**研究发起人自己写的规格**，追补在 §6/§7/§8）
4. 同目录 `W8-第二层进展-公式保持性地基.md`
5. `形式化追踪/01-有哥德尔路线/02-Z0-条件形式与剩余三步.md` 的**最后三节**
6. `外部资料/zfcTr-D3-plan-review-3.md`（本轮独立评审：方向对、缺口定位错、工作量估计错）
7. `外部资料/Z0-D3-补充包二-全量源码与缺口骨架/01-先读这个/START.md`
8. `HoTT/CLAIM_EVIDENCE_MATRIX.md` 与 `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/CLAIM.md` 的 Z0 各节

---

## 3. 项目治理的强制启动闭包（**我这一轮没做，你必须做**）

这个 repo 有比一般项目重得多的启动纪律，写在根 `AGENTS.md`。任何项目 Session（含机械任务）
都必须先完成：

1. 读根 `AGENTS.md`、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md`。
2. 读 `.codex/skills/hott-local-session-governance/SKILL.md`、`.codex/cognition/TASK_ROUTING.md`、
   `.codex/cognition/LOAD_SET.json`、`.codex/cognition/PROTOCOL.md`、
   `.codex/skills/SKILL_ROLES.json`、`.codex/research/hott/STATE.json`。
3. **全文**读单体 `最高指示.md`（83 KB），按 §0A 确定上下文角色（本任务应为
   `RESEARCH_GENERATION`，路由见 `TASK_ROUTING.md` 的"其它 HoTT 理论研究"行）。
4. **按固定顺序全文**读四件套：`核心认知.md` → `方向追踪.md` → `全景视野.md` → `扩展认知.md`。
   注意后三件是**索引 + 全部 shard**，缺一片即未完成加载（合计约 474 KB，需要容量）。
5. 若四件套/最高指示缺件、截断、hash 不符 → 停为 `BLOCKED_FULL_SET_COGNITION`，不要用摘要补洞。

**我这一轮明确没有做 3、4**（只读了 `TASK_ROUTING.md`、治理 SKILL 和 `方向追踪.md` 的索引），
因此我把自己限制在有界的**形式化工程核对**，**没有对用户的悖论观／数学哲学作任何判断**。
你要继续做形式化，请先把 3、4 补齐——这个项目的验收会看这一条。

另：`AGENTS.md` 的 **`MATH_PROOF_BEFORE_DELIVERY_V1`（F-011 门禁）**要求——在把任何数学命题
当"已成立的数学结论"交付之前，必须有与精确命题相称的机器证明与运行收据，并在
`HoTT/CLAIM_EVIDENCE_MATRIX.md` 建立索引行。**做不到就不得用"已证明"措辞**，
必须标 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` 之类。这条是硬门禁。

---

## 4. 唯一剩下的缺口（精确形状）

```lean
-- 就是 ShCraigElim，展开后：
lemma internalized_of_provability {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (σ : ArithmeticSentence)
    (h : Provable Sh.craig (⌜σ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)
```

数学内容：**在 V 内对任意（可能非标准的）Tait 推导做归纳，把每条规则翻成 𝗭𝗙𝗖 推导**。

**为什么绕不开**：Foundation 的 `DirectInterpretation.of_provability`
（`Foundation/FirstOrder/LK/Interpretation.lean:443`）第一行就是
`apply Theory.Proof.complete_on_eq_models`——**完备性定理、语义**，产出元层推导，
不产生 V 内的证明编码。上一轮做了**全量 308 个源文件的 grep，确认不存在内化版本**。

**为什么它一旦成立就完事**（组装链，零件都已就位）：

```
internalized_of_provability
  → ShCraigElim V
  → bwd_of_shcraig_elim (elim : ShCraigElim V)          -- 已证，CG001-C-390
  → keyE 的 ← 方向
  → keyE : 𝗜𝚺₁ ⊢ zfcTr σ 🡘 provabilityPred Sh.craig σ
  → zfcTr.HBL3 (D3)
  → Z0Full.zfc_z0_full [zfcTr.HBL3]                     -- 已证
  → 𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)          -- 完整形式
```

---

## 5. 两条路径（**都不必重做 Σ1 完全性**）

**路径 2 建议先试**（因为 `zfcTr τ` 是 Σ1 句，不必处理任意推导）：

1. **逐规则消去**：对 `Sh.craig` 的推导结构（`Proof/Basic.lean:412` 的 10 条规则）做 V 内归纳。
   - `axm` 支是唯一用到 𝗭𝗙𝗖 的地方：由 `mem_craig_codes_iff` 拿 `p = ρ.padding k` 且
     `reWitness(k, ⌜ρ⌝)`，再由 `Sh.reCh` 的语义得 `ρᵗ` 的 𝗭𝗙𝗖 推导。
   - 其余 9 条逻辑规则靠第 1 层的语法交换律 + `arithTrln` 的 `domain_nonempty` / `func_defined`。
   - **注意**：`Derivable.of_ss`（`Proof/Basic.lean:841`）只在**同一语言内**弱化，
     ℒₒᵣ → ℒₛₑₜ **跨不过去**。

2. **只对标准 Σ1 句重走 Σ1 完全性归纳**：不做任意推导的闭包，用
   `bold_sigma_one_complete`（`D3.lean:82`）的结构，把目标从 `T.internalize V ⊢ ⌜φ⌝`
   换成 `Provable 𝗭𝗙𝗖 ⌜translate φ⌝`，把 numeral／项引理换成翻译版。

**独立佐证**：我这一轮从另一条线（读 `Z0Full.lean` / `Z0Blocked.lean` / `D3.lean` /
`CraigTrick.lean` / `Interpretation.lean`）也收敛到同一个目标，我当时把它写成

```lean
zfc_sigma1_complete : ∀ (τ : ArithmeticSentence), ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 τ → 𝗜𝚺₁ ⊢ τ 🡒 zfcTr τ
```

并注意到：取 `τ := zfcTr σ`（`zfcTr_sigma1` 已证 `zfcTr σ` 是 Σ1）**一步**就给
`zfcTr.HBL3`，不需要 Iff、不需要 `Provability.ext`。也就是说 **D3 只用到 `keyE` 在
`τ = zfcTr σ` 这一族上的 `🡒` 方向**，比"全部 σ 的双向 Iff"要弱。
（这与 SESSION-4 的路径 2 是同一件事的两个说法，可互相校验。）

---

## 6. 已排除的路（别重复）

1. `Sh.Δ₁` 取 `ch := trProv`：`mkDelta trProv (∼trProv)` 要求 `trProv ↔ ¬trProv`，
   在 `trProv` 有确定真值的模型里为假。Π1 那半必须是**等价**公式，不是否定。
2. 给 `Provable 𝗭𝗙𝗜 x` 找有界形式 `∃ d < x`：对 `Sh` 这样的界**不存在**（否则 `Sh` 可判定）。
3. `provable_D3 (T := Sh)`：需 `Sh.Δ₁`，循环。**正解是 `T := Sh.craig`。**
4. `T := Sh.craig` 直接套 `provable_internalize` 得目标：它给的是
   `Sh.craig ⊢ provabilityPred Sh.craig σ`，理论不对，还要翻译回 𝗭𝗙𝗖，更难。
5. 把 `Provable 𝗭𝗙𝗜 ⌜σᵗ⌝ (V)` 当元层 `𝗭𝗙𝗜 ⊢ σᵗ` 用：`Provable.sound` 只在 ℕ 层；
   非标准 V 下推导编码 `d` 可能非标准。这是 D3 的数学核心。
6. 从零移植 Foundation 那 997 行 PA⁻ 机器来"重做 D3"：**不必**——Foundation 已对
   `Sh.craig` 提供完整 D3，`inferInstance` 即得。
7. 想跳过宇宙层级：`rw [models_zfcTr_iff]` 会撞
   `Semantics.Models.{u_1+1,0}` 对 `{1,0}` 的错误。**用已证的
   `Z0UniBridge.models_zfcTr_iff'`（`V : Type*` 版），别自己重撞。**

---

## 7. 环境（完整可用，**别信任何"环境缺失／OOM"的历史描述**）

```
Lean 4.34.0       /Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0
Foundation 源码   /Volumes/D/HoTT-toolchain-cache/foundation-src            (308 个 .lean)
Foundation 构建   /Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean
Mathlib           /Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed29652...
```

工具**已全部收进 repo**（`T=.claude/goals/CG-007-formalization-completion/tools`），
不再依赖 `/tmp`；说明见该目录 `README.md`：

```bash
cd /Volumes/D/HoTT_AI_HANDOFF_20260911
PKG=HoTT/formal/claude-cg001/godel-q-zfc-z0-full
T=.claude/goals/CG-007-formalization-completion/tools

# 迭代编译（缓存默认 <repo>/.cg007-build/，已 gitignore；24 模块约 27 秒，增量几乎瞬时）
python3 -B $T/devbuild.py $PKG <模块列表，按 import 拓扑序>

# 单文件探针（验证一条引理能否 elaborate，几秒出结果）
python3 -B $T/lean_probe.py $PKG <probe.lean>

# 收据与校验
python3 -B $T/capture_run.py --package $PKG --run-id ... --proof-id ... \
    --claim-id ... --expect ACCEPT|REJECT --source ... --scope "..." [--non-goal "..."]
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py \
    --run-dir <dir> --rerun [--expect-rejected]
```

**环境陷阱（我实测，可能只影响某些宿主）**：旧脚本 `/tmp/d3build/devbuild.py` 用
`/usr/bin/sandbox-exec`，在我的沙箱里被拒（`sandbox_apply: Operation not permitted`，exit 71）。
**仓库内的 `$T/devbuild.py` 不用 sandbox-exec**，所以优先用它；若仍被拒，用 `devbuild_ns.py`，
或手工：设 `LEAN_PATH=<build>:<MATHLIB_CLOSURE.json 的 lean_path>`、`HOME=<build>`，然后
`lean -DautoImplicit=false -R . -o … -i … <rel>`（单模块约 1.4 s）。

---

## 8. 陷阱（前两轮踩过，别重复）

1. **`capture_run.py` 的 `--source` 顺序必须是真实的 import 拓扑序。** 顺序错会报
   `object file ... does not exist`，run 目录被占用后要先删才能重跑。正确顺序见
   `Z0UniBridge.lean` 的 25 个依赖。
2. **`verify_cg001_run.py` 把 `sorry` 当源清单硬禁**：含未证标记的文件连"拒绝型"收据都进不了。
   要收据就得证完，或把带 sorry 的文件隔离出源清单。
3. **先写索引行再校验**（否则 `GOAL_INDEX_ROW_COUNT`），且索引行必须是**裸 claim id**
   （写成 `C-387（＝…）` 匹配不上）。
4. **改共享物理文档前先 `git -C /Volumes/D/... diff dev -- <file>`**，否则会顶掉别人的节。
5. **Lean 源码里嵌中文注释会让某些 zsh heredoc 转义坏掉**——用 Python 脚本写 `.lean` 更稳。
6. **`abbrev` 里的 `V` 需要显式 binder**：在 `variable {V : Type*}` 作用域**之外**时
   `V` 不可见，要写 `lemma foo {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (elim : ShCraigElim V)`。
7. `Jeroslow.lean` 不在本地构建树的导入闭包里，要用得先补编译。
8. `sigma_one_complete` 的限定名是
   `FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.sigma_one_complete`
   （`D3.lean` 里 namespace 重开了 `Arithmetic`）。
9. `noncomputable` 传染：`(Sh.craig).Δ₁` 非计算，用到它的 `example` 要标 `noncomputable`，
   但 `theorem` 不能标。模块文档注释必须在 `import` 之后。

---

## 9. 授权与边界（未变）

- 有效授权：2026-10-07 / 10-08 / 10-09 / 10-10 及"继续推进"多段授权。
- **没有授权**：`main` 推送与发布、打 tag、起 Sub Agent、碰他人未提交文件、
  改 `sources/` 与 `private-audit/`。
- 主检出 `/Volumes/D/...` 里有研究发起人未提交的 `外部资料/` 和
  `Z0-D3-攻关包-最小完整版/`（含 zip）——**别动**。
- 改共享文档（`99-更新日志.md`、`CLAIM_EVIDENCE_MATRIX.md`、`证据索引.md`、
  两个 `README.md`）时**只插入增量、以 `dev` 的文件为底**，因为历史上有人用"同名节整体替换"
  导致回退了 CG001-C-127 的节和 W9 的 run 号修正。

---

## 10. 交付与诚实要求

- 证完 `internalized_of_provability` 后：跑 `capture_run.py` 出主运行 + 负控制，
  `verify_cg001_run.py --rerun` 精确重放，写 `CLAIM.md` + `HoTT/CLAIM_EVIDENCE_MATRIX.md`
  索引行，编号从 **C-391 / CG001-C-391** 起。
- **证不出来也要交**：把卡点写成精确 Lean 命题放回 `Z0Blocked.lean`，在 `CLAIM.md` §4
  说明它为什么是实的缺口。**绝不留 `sorry` 冒充完成，绝不改定理类型，绝不加
  `axiom` / `native_decide` / `unsafe` / `opaque` / `debug.skipKernelTC`。**
- 最终回答必须能让人分清：哪些是**已证（有收据）**、哪些是**已读码**、哪些是**我的判断**。
  父目标不受影响——C-120 的影子形式已无条件成立，缺口的未完成不使项目失败。

---

## 11. 上一轮（WorkBuddy 第三轮接手）留下的增量——**我什么都没证出来**

诚实交代：我这一轮只做了**只读核对 + 一次重放编译**，**没有证出任何新命题，没有新收据**。
仍然有效的只有下面几条，读一读能省你时间：

1. **独立重放通过**：`Z0D3Skeleton.lean`（SESSION-2 交付）在 `dev` tip `87b65dfd` 上编译
   **exit 0**，唯一输出是第 82 行 `declaration uses 'sorry'`。核心声称
   `(Sh.craig.standardProvability).HBL3 := inferInstance` **成立**（已由后轮独立确认）。
2. **数字更正**：`Z0-D3-攻关包-最小完整版/` 里 Foundation 模块是 **169** 个 `.lean`
   （SESSION-2 交接写的 167 不对）；包内共 217 文件、3.6 M；zip 853 696 B（833 KiB）。
   （注意：后来的"补包二"用的是**全量 308 个**源文件，口径不同，别混。）
3. **缺口再定位**：见 §5 末尾的 `zfc_sigma1_complete` 说法——与 SESSION-4 的路径 2 收敛。
4. **环境陷阱**：见 §7 的 sandbox-exec 一条。
5. **`Z0D3Skeleton.lean` 至今不在 Git 里**（我核过 `git ls-tree -r dev | grep Z0D3Skeleton` = 空；
   W9c 的提交信息说 `Z0-D3-攻关包-最小完整版/` 与 `外部资料/` 是故意留未跟踪的）。
   你要用它，得自己去包里取；要不要入库请先问研究发起人。
6. 我写的一份复核记录（**不在 `dev` 里**，在我的 worktree 内，未提交）：
   `/Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911/dev-4d788035/.claude/goals/CG-007-formalization-completion/REVIEW-2026-10-10-Z0D3-SESSION-3.md`
   —— 内容已基本被 SESSION-3 / SESSION-4 覆盖，可只看它的 §1（逐条核对表）与 §2（基线问题）。

---

## 12. 建议的第一步动作（可照抄）

```bash
cd /Volumes/D/HoTT_AI_HANDOFF_20260911
git log --oneline -1 && git status --short | head -40

# 读三份交接 + 规格
less .claude/goals/CG-007-formalization-completion/HANDOFF-2026-10-11-Z0D3-SESSION-4.md
less .claude/goals/CG-007-formalization-completion/HANDOFF-2026-10-11-Z0D3-SESSION-3.md
less .claude/goals/CG-007-formalization-completion/W8-下一单元-V内部语法解释定理-规格.md

# 走治理闭包（§3），然后
PKG=HoTT/formal/claude-cg001/godel-q-zfc-z0-full
T=.claude/goals/CG-007-formalization-completion/tools
python3 -B $T/devbuild.py $PKG <按 import 拓扑序的模块列表>   # 先确认基线能编译
```

然后攻 `internalized_of_provability`，**先试路径 2**。
