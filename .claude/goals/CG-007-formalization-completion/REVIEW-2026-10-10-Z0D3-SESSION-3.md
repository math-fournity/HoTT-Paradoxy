# CG-007 复核（第三轮接手）：对 SESSION-2 交接的独立核对 + 缺口再定位

> **身份**：`TASK_RECEIPT / INDEPENDENT_REVIEW / CANDIDATE_ANALYSIS`。本文件是 CG-007 目标包内的一份
> 复核记录，**不是项目 current truth 的所有者**；实时状态以 `dev` 上的 `形式化追踪/`、`HoTT/CLAIM_EVIDENCE_MATRIX.md`
> 与各 `CLAIM.md` 为准。
>
> **写出者**：WorkBuddy 会话（2026-10-10 下午），工作根
> `/Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911/dev-4d788035`
> （分支 `workbuddy/dev-4d788035` @ `87b65dfd`）。
>
> **被审对象**：`HANDOFF-2026-10-10-Z0D3-SESSION-2.md`（Codex 会话 `01a120e6`，2026-10-10 15:09，
> 写于 detached HEAD worktree `/Users/aurolafly/.codex/worktrees/9276` @ `770272ae`）。

## 0. 本轮的认知加载边界（必须先说）

本轮**没有**完整加载四件套：`核心认知.md`（711 行）与 `方向追踪 / 全景视野 / 扩展认知` 的
全部索引＋分片（合计约 474 KB）本轮未读；`最高指示.md`（83 KB）本轮未全文重读；只实际读了
`方向追踪.md` 的索引、`TASK_ROUTING.md`、`hott-local-session-governance/SKILL.md` 与根 `AGENTS.md` 的
相关节。

因此本轮**只做有界的形式化工程核对（bounded formal-engineering pass），不产出任何 core 语义判断、
不对用户的悖论观／数学哲学作任何评价**。按 `BLOCKED_FULL_SET_COGNITION` 的处置顺序，
本轮停止在"不依赖四件套即可判定的事实层"，并把缺口照实登记在此。若研究发起人要求本轮进入
语义／方向层，须先完成四件套与最高指示的全文加载。

## 1. 交接报告的逐条核对

| # | 交接中的声称 | 我核到的实际 | 判定 |
|---|---|---|---|
| 1 | `Z0D3Skeleton.lean` 本机 exit 0，唯一 warning 是 `gap` 的 sorry | **成立**。我在 dev tip `87b65dfd` 上独立重放：Lean 4.34.0、24 个模块增量全 skip、`Z0D3Skeleton.lean` 单独编译 1.4 s、exit 0、唯一输出 `line 82: warning: declaration uses 'sorry'` | ✅ 独立重放通过 |
| 2 | `(Sh.craig.standardProvability).HBL3 := inferInstance` 可合成 | **成立**（同一份编译里通过） | ✅ |
| 3 | `Sh.craig.Δ₁`、`𝗣𝗔⁻ ⪯ Sh.craig`、`Sh.craig ⪯ Sh`、`Sh ⪯ Sh.craig` 均 `inferInstance` | **成立** | ✅ |
| 4 | 包体量"3.6 M、217 文件"、zip "834 KiB、217 文件" | 成立：`du -sh` = 3.6 M；包内 217 文件（Foundation **169** 个 `.lean` ＋ 项目模块 27）；zip 853 696 B（= 833 KiB），内 217 文件。仅"167 个 Foundation 模块"应更正为 **169** | ✅（一处数字更正） |
| 5 | 交付物"都在主检出 `/Volumes/D/...`" | **部分不成立**：`HANDOFF-2026-10-10-Z0D3-SESSION-2.md` 写在了 9276 worktree，不在主检出（主检出直到 15:52 的 W9c 提交才把它带回来） | ⚠️ 位置描述有误 |
| 6 | "本轮未提交任何 Git" | **已被时间推翻**：主检出 `dev` 于 **2026-10-10 15:52:21** 落在 `dbebffe3`（W9c），把 10-10 那一轮的工作带回了 `dev` | ⚠️ 已过期（见 §2） |
| 7 | 下一步 C：救 dev-09 的 `external-foundation-incompleteness` | **已完成**（在 W9c 里）：`HoTT/formal/claude-cg001/external-foundation-incompleteness/` + 运行 `20261010-CG001-FFL-INCOMPLETENESS-R3-REPLAY-01` 与 `-NEG-01`，登记为 **CG001-C-387** | ✅ 已由他人完成 |
| 8 | `形式化追踪/99-更新日志.md` 与 `01-有哥德尔路线/02-...` 已追加本轮 | `02-Z0-条件形式与剩余三步.md` **确已追加**（mtime 10-10 15:49，含 keyE／非标准 V 段）；`99-更新日志.md` 今日确有 2 处 `2026-10-10` 行（由 W9c 带入） | ✅ |

## 2. 本轮发现的关键新事实：仓库已经动过，交接里的"基线"已经过期

三个根的当前位置（我开工时实测）：

| 根 | 分支 / HEAD | 相对 `dev` |
|---|---|---|
| 主检出 `/Volumes/D/HoTT_AI_HANDOFF_20260911` | `dev` @ **`dbebffe3`**（10-10 15:52:21，W9c） | — |
| 我的 worktree `dev-4d788035` | `workbuddy/dev-4d788035` @ `87b65dfd` | **落后 1 个提交** |
| 交接写出方的 worktree `9276` | detached @ `770272ae` | **落后 4 个提交** |

`dbebffe3` 的提交信息明确写了：10-10 那一轮是在 `770272ae` 这个已被 `dev` 越过的基线上工作的，
且它对 `99-更新日志` / `05-分支上的形式包/README` / `CLAIM_EVIDENCE_MATRIX` / `证据索引` 的改动是
**同名节整体替换**，整体搬运会删掉 CG001-C-127 的节并回退 W9 的 run 号修正；W9c 因此以 `dev` 的文件
为底、只插入增量。

**给下一个接手者的硬提醒**：不要再把 `9276` 或 `87b65dfd` 当作工作基线。W9c 自己也说
`Z0-D3-攻关包-最小完整版/` 与 `外部资料/` 是**故意留作未跟踪**的——所以攻关卡包至今不在 Git 里。

## 3. 我对缺口的再定位（比 `keyE` 更干净的一层）

交接把缺口定为

```lean
keyE (σ : ArithmeticSentence) : 𝗜𝚺₁ ⊢ zfcTr σ 🡘 provabilityPred Sh.craig σ
```

我读完 `Z0Full.lean`、`Z0Blocked.lean`、Foundation 的
`Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean`（179 行）与
`Arithmetic/Bootstrapping/Syntax/CraigTrick.lean`、`LK/Interpretation.lean:443` 之后，认为
**真正的最小充分条件是下面这一条，而不是 `keyE`**：

```lean
-- zfc_sigma1_complete：ZFC 经翻译的形式化 Σ1 完全性
zfc_sigma1_complete :
    ∀ (τ : ArithmeticSentence), ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 τ → 𝗜𝚺₁ ⊢ τ 🡒 zfcTr τ
```

理由（逐行可对）：

1. `zfcTr.HBL3` 要的是 `𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr (zfcTr σ)`。
2. `zfcTr σ` 是 Σ1（`Z0Full.zfcTr_sigma1`，已证）。
3. 取 `τ := zfcTr σ`，`zfc_sigma1_complete` 直接给出
   `𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr (zfcTr σ)`——**一步到位**，不需要 `Provability.ext`、
   不需要先绕 `Sh.craig`、也不需要 Iff（只要 `🡒`）。
4. 因此 `zfc_sigma1_complete → zfcTr.HBL3 → zfc_z0_full`（`Z0Full.zfc_z0_full` 已证），
   完整形式 `𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)` 立即成立。

`keyE` 只是拿到 `zfc_sigma1_complete` 的**一条**路径：
`provable_sigma_one_complete (T := Sh.craig)` 给 `𝗜𝚺₁ ⊢ τ 🡒 provabilityPred Sh.craig τ`，
再用 `keyE` 的 `provabilityPred Sh.craig τ 🡒 zfcTr τ` 那一半接上。
**注意 D3 只需要 `keyE` 在 `τ = zfcTr σ` 这一族上的实例、且只需要 `🡒` 方向**——
比交接写的"一条句法等价（Iff、全部 σ）"要弱。这是本轮给出的第一处收缩。

## 4. 真正的障碍在哪（我把定位再下沉了一层）

`zfc_sigma1_complete` 也就是"在 𝗜𝚺₁ 的每个模型 V 里，`V ⊧ τ`（τ 为 Σ1）⟹
`Provable 𝗭𝗙𝗖 ⌜translate τ⌝`"。而 `Provable 𝗭𝗙𝗖 ⌜translate τ⌝` 说的是
**集合论语言里的**可证性。Foundation 的 `sigma_one_complete` 只对**算术理论** `T` 成立
（`D3.lean:170`，前提 `[Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T]`），对 `T := 𝗭𝗙𝗖` 不适用。

跨语言的唯一桥梁是 `shInterp : 𝗭𝗙𝗖 ⊳ Sh`（`Z0Shadow.lean:40`）。我确认了它的性质：

- `DirectInterpretation.of_provability`（`LK/Interpretation.lean:443-448`）是**语义的**——
  证明体是 `apply Theory.Proof.complete_on_eq_models` + `π.model_models_theory`，
  **不是**一个可搬进 𝗜𝚺₁ 的语法证明翻译函数。
- 反过来看 Craig 那一侧是**好消息**：`CraigTrick.lean:321-332` 里的
  `T.craig ⪯ T` 与 `T ⪯ T.craig` 都是**语法的**（`WeakerThan.ofAxm!` + 显式 `mdp` 推导），
  不是靠完备性。Craig 轴是可内部化的那一半。

所以本轮的定位是：

> **缺口 = 把 `shInterp` 这个直接解释的"证明翻译"在 𝗜𝚺₁ 内部语法化。**
> 精确形状：`∀ V [V ⊧* 𝗜𝚺₁] (σ), Provable Sh.craig ⌜σ⌝ → Provable 𝗭𝗙𝗖 ⌜arithTrln.translate σ⌝`
> （这就是 `keyE` 的 `provabilityPred Sh.craig σ 🡒 zfcTr σ` 那一半；另一半同理）。
> 它一旦成立，`zfc_sigma1_complete` 成立，D3 成立，完整形式成立。

这与交接 §7 的判断一致（"非标准 V 下的推导消去，不是 Lean 工程问题"），但把
"要做的那件事"从"一条句法等价"进一步指到了"内部化一条跨语言证明翻译"。
**我不认为这比前几轮估计的 1080 行更便宜**：1080 行那个估计针对的是"移植
`bold_sigma_one_complete`"，而内部化 `of_provability` 是另一件事，量级我不敢下断言，
只敢说：交接"缺口比之前所有 AI 判断的小得多"这句**只对"入口纠错"那部分成立**
（`Sh.craig` 确实免掉了移植 D3 的工作），**对剩余工作量本身不成立**。

## 5. 本轮没有证出新东西

- 没有证出 `zfcTr_D3_internalize`、没有证出 `keyE`、没有证出 `zfc_sigma1_complete`。
- 因此按 F-011 门禁：**本轮无新收据**，没有运行 `capture_run.py`。
- 本轮唯一机器跑过的是重放：`Z0D3Skeleton.lean` 在 dev tip 上 exit 0（见 §1.1）。
  它含 `sorry`，按既有规则不能进收据源。

## 6. 环境补充（我踩到的、交接没写的）

- **本机 `/usr/bin/sandbox-exec` 在我这层沙箱里被拒**（`sandbox_apply: Operation not permitted`）。
  `devbuild.py` 因此整条失败（exit 71）。绕过办法：不用 `sandbox-exec`，直接设置
  `LEAN_PATH=<build> + MATHLIB_CLOSURE.json 的 lean_path` 与 `HOME=<build>`，调用
  `/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean -DautoImplicit=false -R . -o … -i … <rel>`。
  单模块 1.4 s、24 模块全 skip 时约 7 s。
- 交接说的增量缓存 `/tmp/d3build/devbuild/` 仍然有效（我这轮命中了 24/24 skip）。

## 7. 我建议的下一步（需研究发起人先确认方向）

1. **先把基线对齐**：在 `dev` @ `dbebffe3` 上开新 worktree，不要再在 `87b65dfd` 或 `9276` 上工作。
2. **`Z0D3Skeleton.lean` 目前不在 Git 里**（W9c 故意留未跟踪）。要么把它收进
   `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/` 提交，要么明确继续留在外面。
   需要发起人一句话。
3. 攻 `zfc_sigma1_complete`（而不是直接攻 `keyE` 的 Iff 版）：先只做
   `τ = zfcTr σ` 这一族的单向 `🡒`。若这条路也卡住，按既有范式把精确 Lean 命题写回
   `Z0Blocked.lean`，`CLAIM.md` §4 说明，保持诚实——父目标不受影响（C-120 影子形式已无条件成立）。
4. 若发起人要我在语义／方向层继续，先授权我做完整认知加载（四件套 + 最高指示），本轮我刻意没做。

## 8. 授权与边界

- 本轮我只做了只读核对与一次重放编译；**没有提交 Git、没有推 `main`、没有碰 `sources/` 与
  `private-audit/`、没有动主检出里用户未提交的 `外部资料/`**。
- 我在自己的 worktree 里新增了 2 个文件：本文件，以及
  `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/Z0D3Skeleton.lean`（重放用副本）。
  两者都**未提交**。
