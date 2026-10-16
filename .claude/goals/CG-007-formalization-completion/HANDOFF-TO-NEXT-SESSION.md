# CG-007 交接说明：给下一个 Session 的自己

> **身份**：`TASK_HANDOFF / GOAL_LOCAL / CANDIDATE_INTEGRATOR_RECEIPT`。本文件是 CG-007 目标包内的一份工作交接，不是项目 current truth 的所有者；实时状态以 `形式化追踪/` 与各 `CLAIM.md` 为准。
>
> **写出者**：Codex 会话 `01a120e6-4f37-79c0-8651-49996aaf6d9b`，2026-10-09，工作根 `/Users/aurolafly/.codex/worktrees/9276/HoTT_AI_HANDOFF_20260911`（detached HEAD @ `770272ae`；主检出 `/Volumes/D/HoTT_AI_HANDOFF_20260911` @ `dev` `1c113550`）。
>
> **接续对象**：Claude Opus 5.5 会话 `d58e0c0d-fdab-467e-aa11-6f0151221e2e`（2026-10-08 起，两次压缩）。

## 0. 一分钟版本

两条路线（R-无 / R-合）的机器证明都已完成并收据化。Z0（有哥德尔路线的最后一件）现在**只剩一条 Lean 引理**。八个 git worktree 方向的形式化覆盖已补齐。**W9 的 `main` 发布需要研究发起人授权，我没有动。**

## 1. 你必须先读的（按顺序，索引不替代实物）

1. 根 `AGENTS.md`——尤其「形式化与机器证明追踪」节（2026-10-09 新增）：入口、三条编号空间、F-011 五步完成判据、未证明内容处置范式。
2. `形式化追踪/README.md` 总览 → 该线 README → 相关节文件。**这是“做到哪了、下一步、为什么停”的唯一入口。**
3. `.claude/goals/CG-007-formalization-completion/GOAL.md`、`方案.md`、`STATE.json`（`phase` 现为 `W8→W9`，`next_action` 写着 W9 剩项）、`工作台.md` §6（我这次接手的判定与最小可续状态三选一）。
4. 本文件 §3 列的三个关键 `CLAIM.md`。

## 2. 这一轮做完了什么（都有收据）

| 单元 | 编号 | 收据 |
|---|---|---|
| W8 Z0 内部化 | CG001-C-121、C-122 | `HoTT/verification/runs/20261009-CG001-GODEL-Q-ZFC-Z0-FULL-01/`（exit 0，stderr 0 B，71.7 s，112 条公理报告只有三条标准公理；`verify_cg001_run.py --rerun` → `PASS_WITH_SCOPE / EXACT_EXIT_STDOUT_STDERR_MATCH`） |
| 八方向覆盖 | CG001-C-123–C-126 | `.../20261009-CG001-BRANCH-FORMALIZATION-COVERAGE-06/`（16 正源，165 条无公理报告）与 `-NEG-02/`（2 负控制在预定点被拒） |

索引位置：CG-001 目标 `证据索引.md` §35、§36；共享矩阵 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 末两节；`形式化追踪/` 的 01 章、02 节、05 章、总览、`99-更新日志.md`；终局报告 `docs/ZFC时间维度观察力不完备-哥德尔式Q终局报告-20261008.md` §12。

## 3. 三条你现在就得知道的事实

**(1) W8 的缺口是一条精确引理，不是“还差证明的翻译”这种笼统说法。**

`HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/Z0Blocked.lean:zfcTr_D3_internalize`：

```lean
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗸 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗸 (⌜arithTrln.translate (zfcTr τ)⌝ : V)
```

读作：“𝗭𝗙𝗸 证明了 τ 的翻译，就能证明‘𝗭𝗙𝗸 证明了 τ 的翻译’这句话的翻译。”这就是 D3（经翻译的形式化 Σ1 完全性）在显式谓词 `𝔅Z(x) := Provable 𝗭𝗙𝗸 (iT 0 x)` 下的形状。

**它为什么是实的缺口**：Foundation 的 `LK/Interpretation.lean:443 of_provability`（`U ⊢ σ → T ⊢ π.translate σ`）用**完备性定理**证明，是语义证明，没有可搬进 𝗜𝚺₁ 的语法证明翻译。Foundation 自己对算术理论的 D3 是完整机器证明（`DerivabilityCondition/{EquationalTheory,PeanoMinus,D3}.lean` 共 997 行），但它的谓词 `Provable T ⌜σ⌝` 作用在项上、T 是算术理论；这里谓词作用在**翻译后**的公式上。换成别的 D3 写法也绕不过同一内容。

**已就绪的正反两面**：`Z0Full.zfc_z0_full_of_D3_internalize`（无未证标记，已过核）表明引理一旦成立完整形式立即随之成立；`zfcTr_D3_standard` 是 D3 在标准模型 ℕ 中成立的正对照（同一运行内机器核对）。

**(2) 覆盖包不走 `PROOF_VERSION_CLOSURE` registry，这是判定不是遗漏。**

`scripts/audit/proof_claim_ids.py` 的 `CLAIM_ID` 模式只接受 `C-NNN`；`mark_proof_run_indexed.py` 因此拒绝 `CG001-C-123..C-126`。覆盖包沿用 CG-007 全线路线（CG-001 证据索引 + 共享矩阵），`RUN.json` 的 `index_status` 是 `PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE`，与 `20261009-CG001-GODEL-Q-ZFC-Z0-FULL-01` 等一致。我曾尝试登记 registry 并把 `PROOF_VERSION_CLOSURE.json` 改了序列化格式，**已用 `git show HEAD:<path>` 精确还原**（`git diff` 为空）。完整理由写在 `HoTT/formal/branch-formalization-coverage/CLAIM.md` §6。

**(3) 五条“不要重复”的边界。**

- `audit/20261008-八线掌握度与路线保全审计-ZCode.md` 是他人的未提交文件，CG-007 工作台 §2 既有约定“不动不提交”。
- `HoTT/verification/runs/20261009-CG001-BRANCH-FORMALIZATION-COVERAGE-01/02/03/04/05` 与 `-NEG-01` 是驱动修正期的失败或不完整尝试，**不是结论证据**；判据以 `-06` 与 `-NEG-02` 为准（CLAIM §3 列了每次失败的起因）。
- 各分支包的文件一字不改（`HoTT/CLAIM_NAMESPACE_LEDGER.md` §2）；分支命题一律 `D0x-C-NNN`。
- `Z0Blocked.lean` 带未证标记，因此驱动与双重校验器都会拒收它为收据源——这是设计，不是疏漏。
- `sources/` 只读；`private-audit/` 只读；不恢复研究发起人移走的目录。

## 4. 三条可走的下一步，按我的判断排序

### A. 攻 D3（最有判别力，Z0 完整形式的最后一道门）

- 读 `/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/`：`EquationalTheory.lean`（547 行）、`PeanoMinus.lean`（271 行）、`D3.lean`（179 行，含 `term_complete`、`bold_sigma_one_complete`、`sigma_one_complete`）。
- 目标：判断 `bold_sigma_one_complete` 沿公式结构归纳的路线，能否把“真的 Σ1 句子有 𝗭𝗙𝗸 证明”搬到翻译后的公式上。
- 若走不通：不要硬凑。把已尝试的分支、卡住的具体引理写进 `Z0Blocked.lean` 的 docstring 与 `CLAIM.md` §4，保持 `SOURCE_REPORTED_NOT_REPLAYED` 式的诚实，转 B 或 C。
- 工作副本的重建方法：`godel-q-zfc-z0-translate` 的 23 个模块编译次序在 `.claude/goals/CG-007-formalization-completion/tools/` 之外的历史 scratchpad（`w8_chain.txt`）；新建包时复制 `godel-q-zfc-z0-translate/GodelQ/` 的 21 个依赖模块（`cmp` 逐个核对）再跑 `make_pins.py`。

### B. W9 收尾（需研究发起人授权，你不应独自推进 `main`）

- 终局报告 §12 我已补写；剩四种 CLAIMS 译文更新、`main` 由 `scripts/release/build_main_release.py` 从 `dev` 生成（父提交 `f3127701`）、推送并回读远端。**推送与发布以研究发起人的授权为准。**
- 关包前：更新 `STATE.json`（`status`、`phase`、`next_action`）、`LOG.md` 追加一行、`工作台.md`。

### C. 把 `external-foundation-incompleteness` 救成活收据

- dev-09 的 D09-C-369 现在 `SOURCE_REPORTED_NOT_REPLAYED`，只因它的运行依赖一个已不存在的 `/tmp` Foundation 检出。
- 本机已有 `/Volumes/D/HoTT-toolchain-cache/foundation-src`（`1fb01b72`）与 `foundation-build-1fb01b72-v4.34.0`；若该分支包的源码能在这一版上编译，就是一份新的 `dev` 收据。先读它的 `CLAIM.md` 与运行记录，确认版本差异是否改变命题。

## 5. 工具与陷阱（我这次踩过的）

- **先写索引行，再校验**：`verify_cg001_run.py --rerun` 在 CG-001 证据索引里找不到 proof/run/claim 的行就报 `GOAL_INDEX_ROW_COUNT`。
- **`sorry` 不能出现在收据源里**：`zfc_lean_check.py` 与双重校验器都按整文件查禁词。注意分支源在英文散文里会出现 "admit" 一词而非 Lean tactic；我的 `capture_branch_run.py` 先剔除注释体再查，`verify_cg001_run.py` 不剔，所以含该词的源不能走 CG001 校验线（见 §3(2)）。
- **`Semantics.Iff.models_iff` 不存在**：真名 `Foundation.Logic.Semantics.models_iff`，是 namespace 外的 simproc 引理，`rw` 匹配不到包装过的 `Realize`，用 `simpa`。
- **`modus_ponens_sentence` 要显式给理论参数**，否则 `LORDefinable` 实例 stuck。
- **多源收据**：`capture_branch_run.py` 的 `cwd` 是 `<package>/GodelQ`，源路径用裸文件名；分支源里的根级 `import MetaSubtheoryAudit` 要求依赖模块的 olean 落在 LEAN_PATH 根。
- **registry 的 JSON 序列化格式**：`PROOF_VERSION_CLOSURE.json` 不是 `sort_keys=True, indent=2`；改它必须用 `git show HEAD:<path>` 还原而不是手写。

## 6. 授权与边界

- 研究发起人 2026-10-07：“这个 repo 全部的分支和 git worktree，现在由你全面接手了，你就是‘最后的AI’，所以你认为应该做的，都可以做，我全面授权你。”“你要综合所有之前的AI的所有工作，推进到完全的形式化和机器证明的完成。”
- 2026-10-08：“按照你的想法进行优先级安排，完成后续所有‘形式化和机器证明’工作。”
- 本轮（2026-10-09）：“按照你的想法，推进工作，直至‘形式化与机器化’彻底完成，而且必须 Cover 所有值得保留的 8 个当初的 git worktree 留下的工作方向。”
- **没有授权的**：`main` 推送与发布、tag、Sub Agent（2026-09-17 禁令仍有效；P-DAG 2026-10-08 起暂停）、碰他人未提交文件、改 `sources/` 与 `private-audit/`。

## 7. 我这轮的主观判断（供你校验，不是结论）

- Z0 的完整形式在数学上不 surprising，卡的是 Foundation 的 `of_provability` 恰好是语义证明这一实现事实。若下一个 Session 愿意投入，读通那 997 行是最直接的路径；若不愿，把 B/c 做掉也同样推进父目标。
- 八方向覆盖的真正价值不在“又多 16 个 PASS”，而在于 `dev` 现在能回答“这八个方向各自到底有没有可重放的形式资产、缺的是什么”——这是一个此前不存在的查询能力。
