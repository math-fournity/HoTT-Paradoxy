# CG-007 交接（第四轮，2026-10-11，Codex 会话 9276）

> **接力链**：Claude Opus `d58e0c0d` → Codex `01a120e6` 第一轮 → Codex `01a120e6` 第二轮
> → **WorkBuddy 会话（`HANDOFF-2026-10-11-Z0D3-SESSION-3.md`，W9c 归位 + W8 第二层）**
> → **Codex 会话 9276（本文件，W8 第三层入口：宇宙多态桥 + `bwd` 归约）** → 你
>
> 本文件与 SESSION-3 是**并行会话**的两份交接，互不覆盖：SESSION-3 记 WorkBuddy 的第二层
> 公式保持性地基，本文件记 Codex 9276 的宇宙多态桥与收据。两份都要读。

## 位置与身份

- **主检出（canonical）**：`/Volumes/D/HoTT_AI_HANDOFF_20260911`，分支 `dev`。
  **每次动手前先 `git log --oneline -1`**——研究发起人会不定时把我的增量提交上去，
  我在本轮开始时 HEAD 是 `281ee5b4`，结束时已推进到 `273ac2e7`。
- **我的探测 worktree**：`/Users/aurolafly/.codex/worktrees/9276/HoTT_AI_HANDOFF_20260911`。
- **本轮我所有未提交增量都在主检出工作树里**（`git status` 可见）。
- **用户身份**：研究发起人。简体中文回答。

## 必读顺序

1. 本文件（第四轮交接）。
2. `.claude/goals/CG-007-formalization-completion/HANDOFF-2026-10-11-Z0D3-SESSION-3.md`
   （并行会话 WorkBuddy 的交接：W8 第二层公式保持性地基，9 条已证引理）。
3. `.claude/goals/CG-007-formalization-completion/W8-下一单元-V内部语法解释定理-规格.md`
   （研究发起人写的规格；追补在 §6/§7/§8）。
3. `.claude/goals/CG-007-formalization-completion/W8-第二层进展-公式保持性地基.md`。
4. `形式化追踪/01-有哥德尔路线/02-Z0-条件形式与剩余三步.md` 的**最后三节**。
5. `外部资料/zfcTr-D3-plan-review-3.md`（我本轮的独立评审）。
6. `外部资料/Z0-D3-补充包二-全量源码与缺口骨架/01-先读这个/START.md`。

## 一分钟状态

- **八方向覆盖**：已全部有 `dev` 上可重放收据（CG001-C-387 补上 dev-09 最后一缺口）。
- **Z0 影子形式 C-120**：无条件成立，不受本轮任何事影响。
- **Z0 完整形式**（读作 `ZFC ⊬ Con(ZFC)`）：**仍未证**，只差 `zfcTr_D3_internalize`。
- **本轮净进展**：D3 攻坚的**入口障碍已清除**，缺口从"第 2 层要做推导翻译"
  精确归约为**一条消去** `ShCraigElim`。**新收据 CG001-C-390**（主运行 + 负控制，双双精确重放）。

## 本轮做了什么（三件事）

### 1. 补包二：回应外部 AI 的反馈（`外部资料/Z0-D3-补充包二-全量源码与缺口骨架/`）

外部 AI 通读 `Z0-D3-攻关包-最小完整版` 后反馈三条可核实缺口（Foundation 只给 27/167 模块、
`source-manifest.json` 没进包、无 Lean 环境）。我逐条核对后建了补包二：

| 内容 | 数量/状态 |
|---|---|
| `02-Foundation全量源码/` | **308 个 .lean**（与 pinned 源树逐字节相同，`0 extra / 0 absent / 0 differ`） |
| `03-项目模块/` | 32 个 .lean + 两个 pin 文件 |
| `04-缺口骨架/` | 8 个文件（含**本机过核**的 `宇宙多态桥.lean`） |
| `05-收据与哈希/` | W8 manifest + stdout + RUN.json + `verify_package.py` |
| `06-源码地址.md` | Foundation 每处引用的 **pinned-commit 直链** |
| 自验 | 解压后 `python3 verify_package.py` → `RESULT: COMPLETE` |

**核对结论**：它的结构审计与两条数学更正（Δ1 不可判定论证更强、CraigTrick 不需要
证明长度的界）**全部成立已采纳**；它的 D2 修正（`intro hp; exact hp` 是 tactic 层失败）
**经本机两探针证实**；它估的缺口规模**偏大**（它无法运行 `inferInstance`）。

### 2. 独立评审原计划（`外部资料/zfcTr-D3-plan-review-3.md`）

结论：**方向对、缺口定位错、工作量估计错**。

- §3 Bridge′ 弱化与 §4 对 `of_provability` 的否定：**正确**
  （[实测] 全量 308 源 grep 确认不存在内化版本）；
- §5.1 的 L1–L5 分解：**不必做**（Foundation 已提供 `Sh.craig` 的 D3，`inferInstance` 即得）；
- §5.1 L3 量词方向与 §7.3 环境描述：**确为错**（采纳第二位 AI 的更正）。

### 3. **证明推进：宇宙层级障碍清除 + `bwd` 归约**（新收据 CG001-C-390）

新文件 `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/Z0UniBridge.lean`：

```lean
-- ① 宇宙多态版（项目自带的 models_zfcTr_iff 锁在 V : Type，目标定理要 V : Type*）
lemma models_zfcTr_iff' {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (σ : ArithmeticSentence) :
    (V ↓[ℒₒᵣ] ⊧ zfcTr σ) ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V) := by
  rw [zfcTr_def, ← trProvable_quote]
  simp [models_iff]

-- ② bwd 归约为一条消去
abbrev ShCraigElim (V : Type*) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] : Prop :=
  ∀ (σ : ArithmeticSentence),
    Provable Sh.craig (⌜σ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)

lemma bwd_of_shcraig_elim (elim : ShCraigElim V) (σ)
    (h : V ↓[ℒₒᵣ] ⊧ ↑(provabilityPred (Theory.craig Sh) (zfcTr σ))) :
    V ↓[ℒₒᵣ] ⊧ ↑(zfcTr (zfcTr σ))
```

**为什么这一步重要**：在它之前，任何人想证 `bwd` 都会先在
`rw [models_zfcTr_iff]` 上撞宇宙层级错误（本机实测，`Semantics.Models.{u_1+1,0}` 对 `{1,0}`）。
两轮修订都提到过这个差异，但**没人实际处理**。现在它没了。

**收据**（双双 `--rerun` 精确重放）：

| run | 结果 |
|---|---|
| `20261011-CG001-Z0-UNIBRIDGE-01` | exit 0，stderr 0 B，2 条公理报告只有三条标准公理，`PASS_WITH_SCOPE` |
| `20261011-CG001-Z0-UNIBRIDGE-NEG-01` | exit 1，内核类型不匹配，`NEGATIVE_CONTROL_REJECTED_AS_EXPECTED` |

## 唯一剩下的缺口（精确形状）

```lean
-- 就是 ShCraigElim，展开后：
lemma internalized_of_provability {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (σ : ArithmeticSentence)
    (h : Provable Sh.craig (⌜σ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)
```

数学内容：**在 V 内对任意（可能非标准的）Tait 推导归纳，把每条规则翻成 𝗭𝗙𝗖 推导**。

**为什么绕不开**：Foundation 的 `of_provability`（`LK/Interpretation.lean:443`）
第一行就是 `apply Theory.Proof.complete_on_eq_models`——**完备性定理，语义**，
产出元层推导，不产生 V 内证明编码。本机全量 grep 308 个源文件确认**不存在内化版本**。

**两条路径**（都不必重做 Σ1 完全性）：

1. **逐规则消去**：对 `Sh.craig` 推导结构（`Proof/Basic.lean:412` 的 10 条规则）做 V 内归纳。
   `axm` 支是唯一用到 𝗭𝗙𝗖 的地方（由 `mem_craig_codes_iff` 拿 `p = ρ.padding k` 且
   `reWitness(k, ⌜ρ⌝)`，再由 `Sh.reCh` 的语义得 `ρᵗ` 的 𝗭𝗙𝗖 推导）；
   其余 9 条逻辑规则靠第 1 层的语法交换律 + `arithTrln` 的 `domain_nonempty`/`func_defined`。
   **注意**：`Derivable.of_ss`（`Proof/Basic.lean:841`）只在**同一语言内**弱化，
   ℒₒᵣ → ℒₛₑₜ 跨不过去。
2. **只对标准 Σ1 句重走 Σ1 完全性归纳**：不做任意推导的闭包，用
   `bold_sigma_one_complete`（`D3.lean:82`）的结构，把目标从 `T.internalize V ⊢ ⌜φ⌝`
   换成 `Provable 𝗭𝗙𝗖 ⌜translate φ⌝`，把 numeral/项引理换成翻译版。
   路径 2 对 `bwd` 的实例够用（因为 `zfcTr τ` 是 Σ1 句）。**建议先试路径 2。**

## 环境（完整可用，别信任何"环境缺失/OOM"的历史描述）

```
Lean 4.34.0      /Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0
Foundation 源码  /Volumes/D/HoTT-toolchain-cache/foundation-src（308 个 .lean）
Foundation 构建  /Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean（2500 olean）
Mathlib          /Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-*
```

**工具全部在 repo 内**（`T=.claude/goals/CG-007-formalization-completion/tools`），
不再有 `/tmp` 依赖。说明见该目录的 `README.md`：

```bash
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

## 陷阱（本轮踩过，别重复）

1. **`capture_run.py` 的 `--source` 顺序必须是真实的 import 拓扑序**。
   我第一版把 `SeqTranslate.lean` 放在 `InternalTranslate.lean` 前面，
   运行失败（`object file ... does not exist`），run 目录被占用后要先删才能重跑。
   **正确顺序见 `Z0UniBridge.lean` 的 25 个依赖**（我上面 capture 命令里的顺序是对的）。
2. **`verify_cg001_run.py` 把 `sorry` 当源清单硬禁**：含未证标记的文件连"拒绝型"
   收据都进不了。要收据就得证完，或隔离到不进源清单的文件。
3. **先写索引行再校验**（否则 `GOAL_INDEX_ROW_COUNT`），且索引行必须是**裸 claim id**
   （我第一段写 `C-387（＝…）` 匹配不上）。
4. **改共享物理文档前先 `git -C /Volumes/D/... diff dev -- <file>`**，
   否则会顶掉别人的节。
5. **Lean 源码里嵌中文注释会让某些 zsh heredoc 的转义坏掉**——用 Python 写 `.lean` 更稳。
   本轮的 `Z0UniBridge.lean`/`WrongZ0UniBridge.lean` 都是用 Python 脚本写的。
6. **`abbrev` 里的 `V` 需要显式 binder**：`lemma foo (elim : ShCraigElim V)` 在
   `variable {V : Type*}` 作用域**之外**时 `V` 不可见，要写
   `lemma foo {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (elim : ShCraigElim V)`。

## 编号空间

- `C-NNN`（`dev` 共享）：下一个从 **C-391** 起（本轮用了 C-390）。
- `CG001-C-NNN`（Claude 线）：本轮到 **C-390**，下一个 **C-391**。
- `D0x-C-NNN`（分支）：只读，不改号。

## 授权与边界（未变）

- 2026-10-07/08/09/10 + "继续推进" 多段授权仍有效。
- **没有**授权：`main` 推送与发布、tag、Sub Agent、碰他人未提交文件、
  改 `sources/` 与 `private-audit/`。

## 我的判断（供校验）

- **本轮是净推进，不是结案**。`ShCraigElim` 未证，`zfcTr_D3_internalize` 未证。
- **但入口比之前干净得多**：宇宙层级障碍没了，`bwd` 归约成了可传递的一条 `Prop`，
  收据齐全，补包二能让任何外部 AI 在**可编译环境**里工作。
- **路径 2 比路径 1 更可能先出结果**（因为 `zfcTr τ` 是 Σ1 句，不必处理任意推导）。
- 若两条路径都卡住：写精确 Lean 命题回 `Z0Blocked.lean`，在 `CLAIM.md` §4 说明
  为什么是实的缺口。**父目标不受影响——C-120 影子形式已无条件成立。**
