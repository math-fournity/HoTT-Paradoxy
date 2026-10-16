# CG-007 交接说明（第二轮）：Z0 D3 攻坚包已就绪，缺口比上轮判断的小得多

> **身份**：`TASK_HANDOFF / GOAL_LOCAL / CANDIDATE_INTEGRATOR_RECEIPT`。本文件是 CG-007 目标包内的一份
> 工作交接，不是项目 current truth 的所有者；实时状态以 `形式化追踪/` 与各 `CLAIM.md` 为准。
> 上一轮交接是 `HANDOFF-TO-NEXT-SESSION.md`（2026-10-09，同一 Session）。
>
> **写出者**：Codex 会话 `01a120e6-4f37-79c0-8651-49996aaf6d9b`，2026-10-10 下午，
> 工作根 `/Users/aurolafly/.codex/worktrees/9276/HoTT_AI_HANDOFF_20260911`（**detached HEAD @ `770272ae`**；
> 主检出 `/Volumes/D/HoTT_AI_HANDOFF_20260911` **@ `dev` `87b65dfd`**）。
>
> **本轮用户指令**：读上一 AI（Claude Opus）的中断点；判断 `外部资料/zfcTr-D3-plan.md` 对不对；
> 写一份独立修订说明附在旁边；把"形式化与机器证明"推进到底，且必须 Cover 所有值得保留的
> 8 个 git worktree 方向；**给另一个 AI 建一个最小但完整的子目录**，专攻最后的数学证明。

## 0. 一分钟版本

**我没有证出 `zfcTr_D3_internalize`**（这是 Z0 完整形式的唯一缺口，Claude 停在这里）。
我这轮做的是：把缺口**缩小并重新定位**，把可用的零件**全部本机实测成可编译引理**，
做成一个可直接交给另一个 AI 的最小完整包。

**最重要的新事实（本机 Lean 实测）**：

> `(Sh.craig.standardProvability).HBL3` 由 `inferInstance` 直接合成成功。

也就是说 **Foundation 已经提供了 `Sh.craig` 的完整 D3**。上一轮交接（和
`外部资料/zfcTr-D3-plan-revision.md`）判断"三条路都通向同一件事、都绕不开 D3"，
因为它们都去攻 `Sh.Δ₁`——而正确入口是 **`Sh.craig`**（Craig 化后的 Sh），
它从 `Sh.RE`（C-119 已是 instance）自动得到 Δ1，且 D3 现成。

**缺口因此从"形式化 Σ1 完全性"缩小为一条句法等价**：

```lean
lemma keyE (σ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ zfcTr σ 🡘 provabilityPred Sh.craig σ
```

骨架文件 `Z0D3Skeleton.lean` 我本机编译通过（exit 0，唯一 warning 是 `gap` 的预期 sorry）。

## 1. 交付物（都在主检出 `/Volumes/D/HoTT_AI_HANDOFF_20260911/`）

| 路径 | 内容 |
|---|---|
| `Z0-D3-攻关包-最小完整版/` | **给另一个 AI 的包**（7 个子目录 + README + PLAN-REVISION） |
| `Z0-D3-攻关包-最小完整版/05-源码/Z0D3Skeleton.lean` | 本机实测 exit 0 的骨架，含 5 条已证引理 + 1 条标为 `gap` 的缺口 |
| `外部资料/Z0-D3-攻关包-最小完整版.zip` | 同上的 zip（834 KiB，217 文件），可直接发送 |
| `外部资料/zfcTr-D3-plan-revision.md` | **上一轮**另一位 Codex 会话写的修订（我没动它） |
| `Z0-D3-攻关包-最小完整版/PLAN-REVISION.md` | **我这轮**的修订说明，包含对上一轮的更正 + 本轮新事实 |

**全包结构**：

```
Z0-D3-攻关包-最小完整版/
├── README.md                    总入口
├── PLAN-REVISION.md             我对原计划与上一轮修订的更正
├── 01-先读这个/START.md          60 秒版
├── 02-目标命题/                  GOAL.md + Z0Blocked.lean(已修 open) + Z0Full.lean
├── 03-可用的已证引理/API.md      逐条标"实测/读码"
├── 04-攻坚路线/ROUTES.md         三条路线，含两条我判定为死路的
├── 05-源码/                      Foundation 167 模块 + 项目 27 模块 + 骨架 + BUILD.md + devbuild_min.py
├── 06-复现环境/ENV.md            本机路径、GitHub URL、无构建树时怎么办
└── 07-收据/                      W8 运行元数据
```

## 2. 我这轮实测确定成立的东西（`Z0D3Skeleton.lean`，exit 0）

| 引理/事实 | 状态 |
|---|---|
| `(Sh.craig : ArithmeticTheory).Δ₁ := inferInstance` | ✅ 编译通过 |
| `𝗣𝗔⁻ ⪯ Sh.craig := inferInstance` | ✅ |
| `Sh.craig ⪯ Sh` / `Sh ⪯ Sh.craig` | ✅（后接成 `shCraig_iff`，五行的 `weakerThan_iff.mp`） |
| `(Sh.craig.standardProvability).HBL3 := inferInstance` | ✅ **本轮核心发现** |
| `Provable Sh.craig ⌜σ⌝ ↔ Sh.craig ⊢ σ` | ❌ 对非标准 V 不成立（这正是 D3 的数学核心） |
| `V ⊧ provabilityPred Sh.craig σ ↔ Provable Sh.craig ⌜σ⌝` | ✅ 已证 |
| `step1 : V ⊧ zfcTr σ → Provable Sh.craig ⌜zfcTr σ⌝` | ✅ 一行，`sigma_one_complete (T := Sh.craig)` |

## 3. 我试过并判定走不通的（下一代不要重复）

1. **`Sh.Δ₁` 取 `ch := trProv`**：`mkDelta trProv (∼trProv)` 要求 `trProv ↔ ¬trProv`，
   在 trProv 有确定真值的模型中为假。Π1 那半必须是**等价**公式，不是否定。
2. **给 `Provable 𝗭𝗙𝗜 x` 找有界形式 `∃ d < x, ...`**：对 Sh 这样的界**不存在**
   （否则 Sh 可判定）。照这个走的人会找一个既不存在、也不是障碍的东西。
3. **`provable_D3 (T := Sh)`**：需 `Sh.Δ₁`，循环。**正解是 `T := Sh.craig`。**
4. **`T := Sh.craig` 但直接套 `provable_internalize` 得目标**：
   它给 `Sh.craig ⊢ provabilityPred Sh.craig σ`，理论不对，还要翻译回 ZFC，更难。
5. **把 `Provable 𝗭𝗙𝗂 ⌜σᵗ⌝ (V)` 当元层 `𝗭𝗙́ ⊢ σᵗ` 用**：`Provable.sound` 只在 ℕ 层。
   非标准 V 下推导编码 `d` 可能非标准，这一步是 D3 的数学核心，我不认为能绕过。

## 4. 下一步（按我的判断排序）

### A. 攻 `keyE`（最有判别力，Z0 完整形式的最后一道门）

- 读 `05-源码/Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean`
  **全文**（179 行）。不是移植它，是看它怎么把 `V ⊧ σ` 变成 `T.internalize V ⊢ ⌜σ⌝`——
  `keyE` 需要的正是"跨理论的这一步"。
- 先试**单向** `𝗜𝚺₁ ⊢ zfcTr σ 🡒 provabilityPred Sh.craig σ`
  （配 `Provability.mono'` 可能就够 D3 用）。单向比 Iff 容易得多，值得先花两小时。
- 组装路径（零件都在 `API.md`）：
  `keyE` → `Provability.ext` → `zfcTr.HBL3` → `Z0Full.zfc_z0_full_of_D3_internalize` → 完整形式。
- **卡住就写清楚卡在哪一条**，不要留 `sorry` 冒充完成。CG-007 的既有范式
  （`Z0Blocked.lean` 带未证标记 + `CLAIM.md` §4 说明）就是干这个的。

### B. W9 收尾（需研究发起人授权，你不应独自推进 `main`）

终局报告 §12 已补写（上一轮做的）。剩四种 CLAIMS 译文更新、`main` 由
`scripts/release/build_main_release.py` 从 `dev` 生成（父提交 `f3127701`）、推送并回读远端。

### C. 把 `external-foundation-incompleteness` 救成活收据

dev-09 的 D09-C-369 现在 `SOURCE_REPORTED_NOT_REPLAYED`。
但注意：**它的 Foundation pin 是 `f3972f42`**，而本机构建树是 `1fb01b72`
（`f3972f42` 正是 `1fb01b72` 的父提交，差一个 `Transitive closure (#1035)`）。
`TOOLCHAIN.json` 还钉了 `lakefile.toml`/`lake-manifest.json`/`lean-toolchain` 三个 SHA-256。
先核这三件与 `f3972f42` 是否一致，再决定能否用 `1fb01b72` 的 olean 重放。

## 5. 环境与陷阱（我这轮踩过的）

- **本机 Lean 环境完整可用**：`/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0`
  （1893 模块）+ `astra-real-geometry-v4.34.0`（Mathlib `5ed29652`）。
  `/tmp/d3build/devbuild/` 有增量缓存——**24 个模块编译只要 18 秒**（冷启动约 60 秒）。
  别信任何说"环境是 90% 好的""某模块会 OOM"的历史描述，直接跑。
- **`Jeroslow.lean` 不在本地构建树的导入闭包里**（只在 `Incompleteness/` 下选了 9 个模块）。
  要用它得先补编译，别假设它在。
- **`sigma_one_complete` 的正确限定名**是
  `FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.sigma_one_complete`
  （`D3.lean` 里 namespace 重开了 `Arithmetic`，直接 `#check @sigma_one_complete` 找不到）。
  `Bootstrapping.Arithmetic.sigma_one_complete` 在打开的 namespace 下可用。
- **`arithTrln.translate` 需要 `open ... GodelQ.ZFCArith`** 且 `translate` 是 `LogicalConnective.Hom`。
- **`noncomputable` 传染**：`(Sh.craig).Δ₁` 是非计算的，用到它的 `example` 必须标 `noncomputable`，
  但 `theorem` 不能标（Lean 会报 "‘theorem’ subsumes ‘noncomputable’"）。
- **模块文档注释必须在 `import` 之后**，否则 `invalid 'import' command`。
- **收据工具拒 `sorry`**：`capture_run.py` 按整文件查禁词，所以 `Z0Blocked.lean`
  （带 sorry）和含 "admit" 英文散文的分支源都不能进收据源。

## 6. 授权与边界（未变）

- 2026-10-07 / 10-08 / 10-09 的三段全面授权仍然有效（见上一轮交接 §6）。
- **没有授权的**：`main` 推送与发布、tag、Sub Agent、碰他人未提交文件、改 `sources/` 与 `private-audit/`。
- 主检出 `/Volumes/D/...` 有用户未提交的 `外部资料/` 内容（我 pack 时的源），**我没动它们**。
  本轮我唯一的新增是 `Z0-D3-攻关包-最小完整版/` 和它的 zip，都在主检出、未提交。

## 7. 我这轮的主观判断（供你校验，不是结论）

- **缺口比之前所有 AI 判断的小得多。**"读通 Foundation 那 997 行 PA⁻ 机器再移植"
  这个建议（上一轮交接 §4A）是**过度悲观**的：那 997 行的产物已经由 Foundation 机器证明完，
  我只需 `inferInstance`。真正要做的只剩一条句法等价。
- **但我不假装它容易。** `keyE` 的两个方向都撞同一个问题：非标准 V 下的推导消去。
  这是 D3 的数学核心，不是 Lean 工程问题。
- **若 `keyE` 也卡住**，诚实的结论是：把它写成精确 Lean 命题放回 `Z0Blocked.lean`，
  在 `CLAIM.md` §4 说明它为什么是实的缺口，保持 `SOURCE_REPORTED_NOT_REPLAYED` 式的诚实。
  父目标（Z0 的影子形式 C-120 已无条件成立）不受影响。

---

## 9. 第三段（2026-10-11）：D3 攻坚第 1 层过半，`emb` 部分完成

### 9.1 新收据（两条，均可 `--rerun` 精确重放）

| run | 源 | 结果 |
|---|---|---|
| `20261010-CG001-Z0-LAYER1-TRANSLATE-COMMUTATION-01` | `GodelQ/ZFC/Z0Layer1.lean`（七条交换律）+ 24 个依赖模块 | exit 0，7 条公理报告只有 `[propext, Classical.choice, Quot.sound]`；`--rerun` `PASS_WITH_SCOPE / EXACT_EXIT_STDOUT_STDERR_MATCH` |
| `20261010-CG001-Z0-LAYER1-TRANSLATE-COMMUTATION-NEG-01` | 加 `GodelQ/ZFC/WrongZ0Layer1Overclaim.lean` | exit 1，内核**类型不匹配**；`--rerun --expect-rejected` `NEGATIVE_CONTROL_REJECTED_AS_EXPECTED` |

编号 `CG001-C-388`。负控制的原文错误信息见 `形式化追踪/01-有哥德尔路线/02-Z0-条件形式与剩余三步.md`
末节——它钉住"第 1 层不含可证性谓词信息"。

### 9.2 阶段结论：规格 §3 第 1 层 11 项，7 项免费、1 项部分、3 项未开始

- 免费 7 项：`neg ⋏ ⋎`（HomClass 实例）、`∀¹ ∃¹ rel nrel`（Foundation `rfl` 引理）。
  规格把这一层列为"纯语法、可独立做独立验收"是对的，但它低估了现成程度。
- `emb` 部分（`CG001-C-389`）：`emb_term`、`emb_vec` 已证；`emb_id` 8 例中 6 例已证；
  `all`/`exs` 未证，卡点是 `Semiformula.rew Rew.emb (∀¹ φ)` 不归约成 `Rewriting.app` 形式，
  因此 `Rewriting.app_all` 匹配不上（配 `Rew.q_emb` 应有戏，我没试完）。
- `subst`/`shift`/`free`/`setShift` 未开始。

### 9.3 一条重要机制事实（影响你如何安排 `emb` 的收据）

`verify_cg001_run.py` 把 `sorry` 当作**源清单硬禁**——含未证标记的文件不但不能当正源，
连"驱动拒绝型"的负收据也进不了（我试过，校验层报 `LEAN_FORBIDDEN_MARKER`）。
所以 `emb` 的已证部分目前**只在开发构建中有证据**。要么证完 `all`/`exs`，
要么接受它暂无收据（我已把 `emb_id` 拆到 `Z0Layer1Emb.lean`，让无未证标记的
`Z0Layer1.lean` 保住 C-388 的收据）。

### 9.4 文件清单（主检出 `/Volumes/D/...`，未提交）

- `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/Z0Layer1.lean`（七条，无未证标记）
- `.../GodelQ/ZFC/Z0Layer1Emb.lean`（`emb` 部分，带未证标记）
- `.../GodelQ/ZFC/WrongZ0Layer1Overclaim.lean`（负控制）
- `.../CLAIM-Z0-LAYER1.md`（命题全文）
- `HoTT/verification/runs/20261010-CG001-Z0-LAYER1-TRANSLATE-COMMUTATION-01/` 与 `-NEG-01/`
- `.claude/goals/CG-001-targeted-overview/证据索引.md` §38/§38b、`HoTT/CLAIM_EVIDENCE_MATRIX.md`
  的 W8-L1 节、`形式化追踪/` 的 01 章末节与 99 日志、W8 规格的 `emb` 小节
