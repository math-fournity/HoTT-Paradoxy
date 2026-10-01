# 命题与证据

**中文** · [Русский](CLAIMS-RU.md) · [Deutsch](CLAIMS-DE.md) · [Français](CLAIMS-FR.md) · [English](CLAIMS-EN.md)

> 本文件由 `dev` 上的 `scripts/release/build_main_release.py` 从提交 `d766ebd9` 生成，不在本分支修改。第 1、2 节逐字取自 `dev` 上共享证据矩阵 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 的两节（不含原标题行）；第 3 节逐字取自 `dev` 上的目标内索引草稿与 Claude 总索引；第 4 节由各运行的收据生成。文中 `formal/…`、`verification/runs/…` 指本分支 `HoTT/` 下的同名路径；其余过程文件的路径在 `dev` 上（见 README 第 6 节）。另有俄、德、法、英文译本（AI 翻译，以本中文版为准）；`CLAIMS.md` 与 `CLAIMS-ZH.md` 相同。

## 1. 罗素线与 UR：追问程序、邻近对照与截断对照

> 来源：`dev` 上 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 的“Claude CG-001 线：罗素线与 UR 的机器证据（追问程序、邻近对照、截断对照；2026-09-30）”一节。

> 授权：研究发起人 2026-09-30 在本机 Claude Code 会话中说“把所有该做的，全部做完，我认为我们要阶段性地收尾HoTT悖论查找工作了，因为我们很可能已经找到了。”写入者：Claude Code 本机会话 `eadb3381`（macOS，分支 main）。本节只追加，不改动其它各节。
> 工具链：Agda 2.8.0 + cubical 0.9，`--safe --cubical --guardedness`；macOS 记录 `formal/dedekind-omega-missile/TOOLCHAIN.json`，Linux 记录 `formal/cloud-opus-glm-audit/TOOLCHAIN.linux-x86_64.json`（C-77 至 C-80 的原运行）；Lean 4.34.0（C-80：Linux 记录 `formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN.linux-x86_64.json`，macOS 记录 `formal/claude-cg001/pedometer-ablation-lean/LEAN_TOOLCHAIN.json`）。
> 索引状态：各运行的 `index_status` 保持捕获时的值（`PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE`），`verification/PROOF_VERSION_CLOSURE.json` 属 integrator，本节未写；canonical 的 register→mark→freeze 待 integrator。目标内索引与精确重放：`.claude/goals/CG-001-targeted-overview/证据索引.md` §18–§23，核验 `.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --rerun`（复用 canonical 检查，只把矩阵索引检查换成目标内索引）。
> 编号约定：同上节，Opus 线的主张一律写带命名空间的 `CG001-C-NN`；`CG001-C-72` 已登记在上一节（Cloud-Opus 的 Linux 重放），本节不重复。本矩阵其它节里同号的 `C-71`、`C-75` 等是别的证明包的 claim，与本节无关。
> 读法：这批命题支撑两份社区审计稿（`docs/社区审计提交/02-罗素悖论的幽灵.md` 与 `03-HoTT的芝诺.md`）。研究发起人的判定与 UR 定义是判定，不是定理；本节不宣称 HoTT 不一致。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-HSET-UNIVERSE-001` | `CG001-C-71` | `formal/claude-cg001/hset-universe/HSetNotSet.agda` | `verification/runs/20260926-CG001-HSET-UNIVERSE-01/`；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记） |
| `MP-CG001-HSET-UNIVERSE-NEG-001` | `CG001-C-71`（负控制） | `formal/claude-cg001/hset-universe/WrongFlipSetTrivial.agda` | `verification/runs/20260926-CG001-HSET-UNIVERSE-NEG-01/`；exit 42，`false != true of type Bool` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-TOTALITY-ESCALATION-001` | `CG001-C-73` | `formal/claude-cg001/totality-escalation/TotalityEscalates.agda` | `verification/runs/20260926-CG001-TOTALITY-ESCALATION-01/`；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（精确上升只证 n = 0、1，一般 n 为来源 Kraus–Sattler 2015，见同包 `REVISIONS.md`；上界为库定理） |
| `MP-CG001-TOTALITY-ESCALATION-NEG-001` | `CG001-C-73`（负控制） | `formal/claude-cg001/totality-escalation/WrongRotateTrivial.agda` | `verification/runs/20260926-CG001-TOTALITY-ESCALATION-NEG-01/`；exit 42，`1 != 0 of type Nat` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-COPIES-OF-BOOL-001` | `CG001-C-74` | `formal/claude-cg001/totality-escalation/CopiesOfBool.agda`（命题全文 `CLAIM-C74.md`） | `verification/runs/20260926-CG001-COPIES-OF-BOOL-01/`；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（只涉及 Bool） |
| `MP-CG001-COPIES-OF-BOOL-NEG-001` | `CG001-C-74`（负控制） | `formal/claude-cg001/totality-escalation/WrongSwapStays.agda` | `verification/runs/20260926-CG001-COPIES-OF-BOOL-NEG-01/`；exit 42，`false != true of type Bool` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-UNIVERSE-QUESTIONING-001` | `CG001-C-75`、`CG001-C-76` | `formal/claude-cg001/universe-questioning/UniverseHasNoLevel.agda`（命题全文 `CLAIM.md`，范围修订 `REVISIONS.md`） | `verification/runs/20260926-CG001-UNIVERSE-QUESTIONING-01/`；exit 0，stderr 0 B；目标内精确重放一致（2026-09-30 补登入本草稿） | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（主定理经 Eilenberg–MacLane 空间用了高阶归纳类型，名称级证书见证据索引 §19 补注） |
| `MP-CG001-UNIVERSE-QUESTIONING-NEG-001` | `CG001-C-75`（负控制） | `formal/claude-cg001/universe-questioning/WrongSectionReadsZero.agda` | `verification/runs/20260926-CG001-UNIVERSE-QUESTIONING-NEG-01/`；exit 42，`1 != 0` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-QUESTIONING-DELAY-001` | `CG001-C-77`、`CG001-C-78`、`CG001-C-79` | `formal/claude-cg001/questioning-delay/QuestioningDelay.agda`（命题全文 `CLAIM.md`；导入 `pedometer-semantics` 与 `universe-questioning`） | `verification/runs/20260930-CG001-QUESTIONING-DELAY-01/`（Linux 工具链记录 `formal/cloud-opus-glm-audit/TOOLCHAIN.linux-x86_64.json`）；exit 0，stderr 0 B；目标内精确重放一致；macOS 跨平台重放 `verification/runs/20260930-CG001-QUESTIONING-DELAY-MACOS-01/`，归一化 stdout 与 Linux 逐行一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（罗素线 S6 的内部定理：对任意判定器，宇宙上的追问程序等于 never；读到现实执行仍需一致性，对任意判定器另需典范性） |
| `MP-CG001-QUESTIONING-DELAY-NEG-001` | `CG001-C-78`（负控制） | `formal/claude-cg001/questioning-delay/WrongUniverseAnswersEarly.agda` | `verification/runs/20260930-CG001-QUESTIONING-DELAY-NEG-01/`；exit 42，`nothing != just 1`；macOS 跨平台重放 `verification/runs/20260930-CG001-QUESTIONING-DELAY-MACOS-NEG-01/`，归一化 stdout 与 Linux 逐行一致 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-QUESTIONING-DELAY-NEG-002` | `CG001-C-79`（负控制） | `formal/claude-cg001/questioning-delay/WrongNaturalsSilent.agda` | `verification/runs/20260930-CG001-QUESTIONING-DELAY-NEG-02/`；exit 42，`just 1 != nothing`；macOS 跨平台重放 `verification/runs/20260930-CG001-QUESTIONING-DELAY-MACOS-NEG-02/`，归一化 stdout 与 Linux 逐行一致 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-QUESTIONING-DELAY-NEG-003` | `CG001-C-79`（负控制） | `formal/claude-cg001/questioning-delay/WrongSetsStopAtOne.agda` | `verification/runs/20260930-CG001-QUESTIONING-DELAY-NEG-03/`；exit 42，`nothing != just 1`；macOS 跨平台重放 `verification/runs/20260930-CG001-QUESTIONING-DELAY-MACOS-NEG-03/`，归一化 stdout 与 Linux 逐行一致 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-QUESTIONING-DELAY-NEG-004` | `CG001-C-78`（负控制） | `formal/claude-cg001/questioning-delay/WrongNeverByRefl.agda` | `verification/runs/20260930-CG001-QUESTIONING-DELAY-NEG-04/`；exit 42，`askFrom Type judgeU 1 != never`；macOS 跨平台重放 `verification/runs/20260930-CG001-QUESTIONING-DELAY-MACOS-NEG-04/`，归一化 stdout 与 Linux 逐行一致 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-QUESTIONING-DELAY-LEAN-001` | `CG001-C-80` | `formal/claude-cg001/questioning-delay-lean/QuestioningLean.lean`（**Lean 4.34.0**，Linux 记录 `formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN.linux-x86_64.json`） | `verification/runs/20260930-CG001-QUESTIONING-DELAY-LEAN-01/`；exit 0，九条定理零公理，`leanchecker --fresh` 通过；目标内精确重放一致；macOS 跨平台重放 `verification/runs/20260930-CG001-QUESTIONING-DELAY-LEAN-MACOS-01/`，归一化 stdout 与 Linux 逐行一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（Lean 行，事实世界中同一过程第 1 问停） |
| `MP-CG001-QUESTIONING-DELAY-LEAN-NEG-001` | `CG001-C-80`（负控制） | `formal/claude-cg001/questioning-delay-lean/WrongLeanUniverseSilent.lean` | `verification/runs/20260930-CG001-QUESTIONING-DELAY-LEAN-NEG-01/`；exit 1，`Not a definitional equality`（细化器拒绝）；macOS 跨平台重放 `verification/runs/20260930-CG001-QUESTIONING-DELAY-LEAN-MACOS-NEG-01/`，归一化 stdout 与 Linux 逐行一致 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-PRODUCT-QUESTIONING-001` | `CG001-C-81`、`CG001-C-82` | `formal/claude-cg001/product-questioning/ProductQuestioning.agda`（命题全文 `CLAIM.md`；导入 `questioning-delay`、`pedometer-semantics`、`universe-questioning`） | `verification/runs/20260930-CG001-PRODUCT-QUESTIONING-01/`（**macOS** 工具链记录 `formal/dedekind-omega-missile/TOOLCHAIN.json`）；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（C-78 的邻近对照：HoTT Book 例 8.8.6 的非宇宙乘积上，追问程序对任意判定器等于 never；同一乘积成员高度有上限时恰好第 2+b 问停；只在 macOS 捕获与重放） |
| `MP-CG001-PRODUCT-QUESTIONING-NEG-001` | `CG001-C-81`（负控制） | `formal/claude-cg001/product-questioning/WrongProductAnswersEarly.agda` | `verification/runs/20260930-CG001-PRODUCT-QUESTIONING-NEG-01/`；exit 42，`nothing != just 1` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-PRODUCT-QUESTIONING-NEG-002` | `CG001-C-81`（负控制） | `formal/claude-cg001/product-questioning/WrongProductNeverByRefl.agda` | `verification/runs/20260930-CG001-PRODUCT-QUESTIONING-NEG-02/`；exit 42，`askFrom Prod judgeProd 1 != never` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-PRODUCT-QUESTIONING-NEG-003` | `CG001-C-82`（负控制） | `formal/claude-cg001/product-questioning/WrongBoundedSilent.agda` | `verification/runs/20260930-CG001-PRODUCT-QUESTIONING-NEG-03/`；exit 42，`just 2 != nothing` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-PRODUCT-QUESTIONING-NEG-004` | `CG001-C-82`（负控制） | `formal/claude-cg001/product-questioning/WrongBoundedStopsEarly.agda` | `verification/runs/20260930-CG001-PRODUCT-QUESTIONING-NEG-04/`；exit 42，`nothing != just 1` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-TRUNCATION-QUESTIONING-001` | `CG001-C-83` | `formal/claude-cg001/truncation-questioning/TruncationQuestioning.agda`（命题全文 `CLAIM.md`；导入 `product-questioning`、`questioning-delay`、`pedometer-semantics`，经其导入 `universe-questioning`） | `verification/runs/20260930-CG001-TRUNCATION-QUESTIONING-01/`（**macOS** 工具链记录 `formal/dedekind-omega-missile/TOOLCHAIN.json`）；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（教科书消解的对照：对任意类型与判定器，追问程序在集合截断上第 1 问停，与 C-78、C-81 的 `never` 并列；代价：截断把宇宙里不同的自我认同合一，且不能解码回宇宙；只在 macOS 捕获与重放） |
| `MP-CG001-TRUNCATION-QUESTIONING-NEG-001` | `CG001-C-83`（负控制） | `formal/claude-cg001/truncation-questioning/WrongTruncSilent.agda` | `verification/runs/20260930-CG001-TRUNCATION-QUESTIONING-NEG-01/`；exit 42，`just 1 != nothing` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-TRUNCATION-QUESTIONING-NEG-002` | `CG001-C-83`（负控制） | `formal/claude-cg001/truncation-questioning/WrongNotEqTrivial.agda` | `verification/runs/20260930-CG001-TRUNCATION-QUESTIONING-NEG-02/`；exit 42，`false != true` | `NEGATIVE_CONTROL_REJECTED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-71 | `flipSet` 的第一分量为 `ua notEquiv`，`ua notEquiv ≢ refl`；`hSetNotSet : ¬ isSet (hSet ℓ-zero)` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260926-CG001-HSET-UNIVERSE-01`、`-NEG-01` | 只陈述集合宇宙这一层；不证明更高层 |
| CG001-C-73 | n 层落定者的总体在 n+1 层落定（库定理）；集合的总体不是集合、群胚的总体不是群胚（n = 0、1 精确）；集合总体的截断不能解码回去 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260926-CG001-TOTALITY-ESCALATION-01`、`-NEG-01` | 一般 n 由 CG001-C-76 与 Kraus–Sattler 重放（上节）给出，不在本行 |
| CG001-C-74 | 所有与 Bool 相同的类型的收集：按相同计数恰好一个，收集本身不是集合 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260926-CG001-COPIES-OF-BOOL-01`、`-NEG-01` | 有限实例；不涉及大小问题 |
| CG001-C-75 | 局部—整体环路原理；对 `K n = EM ℤ (1+n)` 有非平凡截面；`universeHasNoLevel : (m : ℕ) → ¬ isOfHLevel m (Type ℓ-zero)` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260926-CG001-UNIVERSE-QUESTIONING-01`、`-NEG-01` | 用了高阶归纳类型（名称级证书见上节 COPUS-R6-C01）；不证明没有高阶归纳类型时同样成立 |
| CG001-C-76 | 对一切 k，(1+k) 层落定者的总体不在 1+k 层落定（`gatheringNeverSettled`），配合库的上界恰好高一层；第 0 层的总体可缩 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260926-CG001-UNIVERSE-QUESTIONING-01` | CG001-C-73 一般 n 的机器证明；不陈述单个宇宙 |
| CG001-C-77 | 追问过程 Q 写成 C-55 的 Delay 程序并带判定器 `Judge C = (k : ℕ) → Dec (isOfHLevel (suc k) C)`：燃料方程只取决于事实；返回值可靠；停机当且仅当有某个有限层；`Q ≡ never` 当且仅当一层都没有；精确停机时刻（`exactHalt`、`silentUpTo`） | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | runs `20260930-CG001-QUESTIONING-DELAY-01`（Linux）、`-MACOS-01`（macOS） | `≡ never` 只经有限燃料的运行来读；读成现实执行需要理论一致性与对闭判定器的典范性 |
| CG001-C-78 | `universeQuestioningIsNever : (judge : Judge (Type ℓ-zero)) → question (Type ℓ-zero) judge ≡ never`；判定器存在且唯一；`kernelRuns1000`（`refl`）；问“有没有一层落定”的程序燃料 0 答否 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | runs `20260930-CG001-QUESTIONING-DELAY-01`、`-MACOS-01`；负控制 `-NEG-01`、`-NEG-04` 及其 `-MACOS-` 重放 | 不证明 HoTT 不一致；经 CG001-C-75 用了高阶归纳类型 |
| CG001-C-79 | 同一程序：ℕ、Bool 第 1 问停；h-层 1+n 的类型的目录（`Gathering n`）恰好第 1+n 问停，更少燃料得 `nothing`；各有判定器 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | runs `20260930-CG001-QUESTIONING-DELAY-01`、`-MACOS-01`；负控制 `-NEG-02`、`-NEG-03` 及其 `-MACOS-` 重放 | “第 k 问”指问数与燃料，不是时间 |
| CG001-C-80 | Lean 4（UIP）：同一组燃料方程写成有限燃料运行；对任意判定器，宇宙 `Type` 第 1 问停并返回 1；九条定理零公理 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | runs `20260930-CG001-QUESTIONING-DELAY-LEAN-01`（Linux）、`-LEAN-MACOS-01`（macOS）；负控制 `-LEAN-NEG-01`、`-LEAN-MACOS-NEG-01` | 集合层命题（Lean 相等有 UIP）；与 Agda 定义是按同一组方程的转写，不是跨系统的同一对象 |
| CG001-C-81 | `productHasNoLevel : (m : ℕ) → ¬ isOfHLevel m Prod`（`Prod = (n : ℕ) → K n`，HoTT Book 例 8.8.6）；对任意判定器 `question Prod judge ≡ never`；判定器存在且唯一；`productKernelRuns1000`（`refl`）；问“有没有一层”燃料 0 答否 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260930-CG001-PRODUCT-QUESTIONING-01`；负控制 `-NEG-01`、`-NEG-02` | 书中已知例子，不主张原创；只在 macOS 上捕获与重放；宇宙只作类型族的值域 |
| CG001-C-82 | `Bounded b = (n : ℕ) → K b` 在 h-层 3+b 落定、2+b 不落定；对任意判定器 `runFor (suc b) (question (Bounded b) judge) ≡ just (suc (suc b))`，更少燃料得 `nothing` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260930-CG001-PRODUCT-QUESTIONING-01`；负控制 `-NEG-03`、`-NEG-04` | 负控制只跑 b = 0；只在 macOS 上捕获与重放 |
| CG001-C-83 | 对任意类型与判定器，追问程序在集合截断 `∥ X ∥₂` 上燃料 0 返回 1；截断宇宙的判定器存在且唯一（`refl` 实跑）；与宇宙、乘积本身的 `never` 并列；`notEqNotRefl`、`truncCollapses : cong ∣_∣₂ notEq ≡ refl`、`noDecoding` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260930-CG001-TRUNCATION-QUESTIONING-01`；负控制 `-NEG-01`、`-NEG-02` | 不说截断错了；不裁定对截断发问与对宇宙发问是不是同一任务；只在 macOS 上捕获与重放 |

## 2. Cloud-Opus 的审计与补完：宇宙塔的一般 n、高阶归纳类型证书、GLM 线与跨平台重放

> 来源：`dev` 上 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 的“Cloud-Opus 审计并补完 GLM：GLM 线最终集成、一般 n（KS 5.9/5.10）与 HIT 名称级证书（2026-09-27）”一节。

> 授权：用户委托工作单 `GLM-5.3-Flash/审计请求/20260927-委托工作单-审计修正补完交付最终卷宗.md` §6（"`HoTT/CLAIM_EVIDENCE_MATRIX.md`（仅 D2 最终集成行）"）。写入者：Claude Code 云端会话（Cloud-Opus），分支 `claude/charming-pasteur-mvzlio`。
> 工具链：Agda v2.8.0 **Linux x86-64** release 资产 + cubical v0.9（与 `dedekind-omega-missile/TOOLCHAIN.json` 的 cubical 逐字节一致；Agda 为同一 release 的另一平台资产），记录 `formal/cloud-opus-glm-audit/TOOLCHAIN.linux-x86_64.json`。全部运行 `--safe --cubical --guardedness --ignore-interfaces`。
> 索引状态：运行 `index_status = PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE`；`verification/PROOF_VERSION_CLOSURE.json` 属 integrator，未写。目标内索引 `Cloud-Opus审计并补完GLM/证据索引.md`；核验 `Cloud-Opus审计并补完GLM/tools/verify_copus_run.py`（复用 canonical 检查并逐字节重放）。审计报告与卷宗：`Cloud-Opus审计并补完GLM/`。
> GLM 的原运行 `20260926-GLM-*` 保持原样（哈希锁定）；其 schema 非 canonical（见审计报告 R5），此处以 `20260927-COPUS-REPLAY-GLM-*` 为 canonical 副本。
> 编号约定：本节提到 Opus 的主张时一律写带命名空间的 `CG001-C-NN`（Opus CG-001 目标内索引 `.claude/goals/CG-001-targeted-overview/证据索引.md`）；本矩阵其它节里同号的 `C-63`、`C-71`、`C-75` 等是别的证明包的 claim，与本节无关。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-GLM-RUSSELL-IOTA-001` | `GLM-R1-C02`、`GLM-R1-C03` | `formal/glm-russell/iota-syntax/ArtificialEquationControl.agda`（+ `RealisticIotaSyntax.agda`） | `verification/runs/20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-01/`；exit 0 | `FORMAL_CHECKED_WITH_SCOPE`（GLM 证明，本会话 canonical 重放） |
| `MP-GLM-RUSSELL-IOTA-NEG-001` | `GLM-R1-C03` 负控制 | `formal/glm-russell/iota-syntax/WrongArtIsRefl.agda` | `verification/runs/20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-NEG-01/`；exit 42，`art i != boolTy` | `NEGATIVE_CONTROL_REJECTED`（只测 art ≢ refl，不测 C03 论证） |
| `MP-GLM-RUSSELL-IOTA-002` | `GLM-R1-C01` | `formal/glm-russell/iota-syntax/RealisticIotaSyntaxSet.agda` | `verification/runs/20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-02/`；exit 0 | `FORMAL_CHECKED_WITH_SCOPE` |
| `MP-GLM-RUSSELL-STALL-001` | `GLM-R2-C01`、`GLM-R2-C02` | `formal/glm-russell/universe-ascent-stall/AscentStallAtSets.agda` | `verification/runs/20260927-COPUS-REPLAY-GLM-ASCENT-STALL-01/`；exit 0 | `FORMAL_CHECKED_WITH_SCOPE / HIT_FREE_NAME_LEVEL (COPUS-R1-C02/C03)` |
| `MP-GLM-RUSSELL-GROUPOID-001` | `GLM-R3-C01` | `formal/glm-russell/groupoid-universe/NoHitGroupoidUniverse.agda` | `verification/runs/20260927-COPUS-REPLAY-GLM-GROUPOID-UNIVERSE-01/`；exit 0 | `FORMAL_CHECKED_WITH_SCOPE / HIT_FREE_NAME_LEVEL (COPUS-R1-C01) / KS_N1_FAITHFUL_REPLAY` |
| `MP-GLM-RUSSELL-GROUPOID-NEG-001` | `GLM-R3-C01` 原负控制 | `formal/glm-russell/groupoid-universe/WrongGroupoidWitness.agda` | `verification/runs/20260927-COPUS-REPLAY-GLM-GROUPOID-UNIVERSE-NEG-01/`；exit 42，`[NotInScope] true` | `REJECTED_BEFORE_TYPE_CHECKING / CONTROL_INVALID`（由 `MP-COPUS-GLM-FIX-NEG-001/002` 取代） |
| `MP-COPUS-KS-TOWER-001` | `COPUS-KS-C01`–`COPUS-KS-C05` | `formal/cloud-opus-glm-audit/ks-universe-tower/KSUniverseTower.agda`；本地 `CLAIM.md` | `verification/runs/20260927-COPUS-KS-UNIVERSE-TOWER-01/`；exit 0（72 s） | `MACHINE_PROVED_WITH_SCOPE / HIT_FREE_NAME_LEVEL (COPUS-R1-C05) / KNOWN_THEOREM_REPLAYED (Kraus–Sattler 2015)` |
| `MP-COPUS-KS-TOWER-NEG-001` | `COPUS-KS-C01` 负控制 | `formal/cloud-opus-glm-audit/ks-universe-tower/KSNegTrivialBase.agda` | `verification/runs/20260927-COPUS-KS-UNIVERSE-TOWER-NEG-01/`；exit 42，`false != true` | `NEGATIVE_CONTROL_REJECTED`（平凡基环） |
| `MP-COPUS-KS-TOWER-NEG-002` | `COPUS-KS-C01` 负控制 | `formal/cloud-opus-glm-audit/ks-universe-tower/KSNegOvershoot.agda` | `verification/runs/20260927-COPUS-KS-UNIVERSE-TOWER-NEG-02/`；exit 42 | `NEGATIVE_CONTROL_REJECTED`（证书层级精确，不越级） |
| `MP-COPUS-HITSCAN-001` | `COPUS-R1-C01`–`COPUS-R1-C03` | `formal/cloud-opus-glm-audit/hitscan/CertGLM.agda`（+ `HITScan.agda`） | `verification/runs/20260927-COPUS-HITSCAN-CERT-GLM-01/`；exit 0；stdout 含全部闭包 | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE`（名称级，边界见 hitscan/CLAIM.md） |
| `MP-COPUS-HITSCAN-002` | `COPUS-R1-C04`、`COPUS-R6-C01` | `formal/cloud-opus-glm-audit/hitscan/CertOpus.agda` | `verification/runs/20260927-COPUS-HITSCAN-CERT-OPUS-01/`；exit 0 | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` |
| `MP-COPUS-HITSCAN-003` | `COPUS-R1-C05` | `formal/cloud-opus-glm-audit/hitscan/CertKS.agda` | `verification/runs/20260927-COPUS-HITSCAN-CERT-KS-01/`；exit 0 | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` |
| `MP-COPUS-HITSCAN-004` | `COPUS-R1-C06` | `formal/cloud-opus-glm-audit/hitscan/CertC71.agda` | `verification/runs/20260927-COPUS-HITSCAN-CERT-OPUS-02/`；exit 0 | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` |
| `MP-COPUS-HITSCAN-NEG-001` | `COPUS-R1-C01` 扫描器负控制 | `formal/cloud-opus-glm-audit/hitscan/NegCertIota.agda` | `verification/runs/20260927-COPUS-HITSCAN-NEG-01/`；exit 42，点名 `Tm` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-COPUS-HITSCAN-NEG-002` | `COPUS-R6-C01` 扫描器负控制 | `formal/cloud-opus-glm-audit/hitscan/NegCertC75.agda` | `verification/runs/20260927-COPUS-HITSCAN-NEG-02/`；exit 42，点名 `HubAndSpoke, Susp, S¹, EM₁, EM₁-raw` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-COPUS-HITSCAN-NEG-003` | `COPUS-R1-C01` 扫描器负控制 | `formal/cloud-opus-glm-audit/hitscan/NegCertPT.agda` | `verification/runs/20260927-COPUS-HITSCAN-NEG-03/`；exit 42，点名 `∥_∥₁` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-COPUS-GLM-FIX-001` | `COPUS-GLM-FIX-C02a`、`COPUS-GLM-FIX-C02b` | `formal/cloud-opus-glm-audit/glm-repairs/IotaC02Faithful.agda` | `verification/runs/20260927-COPUS-GLM-REPAIR-01/`；exit 0 | `FORMAL_CHECKED_WITH_SCOPE / DECLARATION_PROOF_REPAIR` |
| `MP-COPUS-GLM-FIX-NEG-001` | `GLM-R3-C01` 修复负控制 | `formal/cloud-opus-glm-audit/glm-repairs/GroupoidNegFixed.agda` | `verification/runs/20260927-COPUS-GLM-REPAIR-NEG-01/`；exit 42，`false != true` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-COPUS-GLM-FIX-NEG-002` | `GLM-R3-C01` 近失控制 | `formal/cloud-opus-glm-audit/glm-repairs/GroupoidNegTrivialLoop.agda` | `verification/runs/20260927-COPUS-GLM-REPAIR-NEG-02/`；exit 42，`true != false` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-COPUS-GLM-FIX-NEG-003` | `GLM-R1-C03` 近失控制 | `formal/cloud-opus-glm-audit/glm-repairs/IotaC03NegTrivialInterp.agda` | `verification/runs/20260927-COPUS-GLM-REPAIR-NEG-03/`；exit 42 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-COPUS-Q7-001` | `COPUS-Q7-C01` | `formal/cloud-opus-glm-audit/glm-repairs/Q7AnnotatedReplay.agda` | `verification/runs/20260927-COPUS-GLM-REPAIR-Q7-01/`；exit 0 | `FORMAL_CHECKED_WITH_SCOPE` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| GLM-R1-C01 | `realisticIotaSyntaxIsASet : isSet Tm`（Tm：Bool 字面量 + cond + 两条 ι 路径构造子的玩具 HIT，Tm ≃ Bool） | `FORMAL_CHECKED_WITH_SCOPE` | run `20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-02` | 不是"理论自身的表述完全落定"；无替换/上下文/依赖；完整类型论语法未触及 |
| GLM-R1-C02 | 形式上只有 `valReflT/F : Path (Path Bool (val (cond (lit b) t s)) (val _)) refl refl`（端点定义性相等） | `FORMAL_CHECKED_WITH_SCOPE / DECLARATION_PROOF_RUPTURE` | run `20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-01` | **不**陈述"ι 路径构造子被解释为 refl"；该内容由 COPUS-GLM-FIX-C02a 陈述 |
| GLM-R1-C03 | `¬isSetTmA : ¬ isSet TmA`（加入一条被解释为 `ua not` 的人工等式后） | `FORMAL_CHECKED_WITH_SCOPE` | runs `20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-01`、`-NEG-01`、`20260927-COPUS-GLM-REPAIR-NEG-03` | 不证明"非落定必须人工注入" |
| GLM-R2-C01 | `universeLoopSpaceAtSetIsSet : ∀ {ℓ} (X : Type ℓ) (pX : isSet X) → isSet (Path (Type ℓ) X X)` | `FORMAL_CHECKED_WITH_SCOPE / HIT_FREE_NAME_LEVEL` | run `20260927-COPUS-REPLAY-GLM-ASCENT-STALL-01`；COPUS-R1-C02 | — |
| GLM-R2-C02 | `noLevel2AscentAtSets : ∀ {ℓ} (X : Type ℓ) (pX : isSet X) → isContr (Path (Path (Type ℓ) X X) refl refl)` | `FORMAL_CHECKED_WITH_SCOPE / HIT_FREE_NAME_LEVEL` | 同上；COPUS-R1-C03 | 不推出"HIT 对上升必要"（宇宙塔无 HIT 也上升：COPUS-KS-C01） |
| GLM-R3-C01 | `¬universeIsGroupoid : ¬ isOfHLevel 3 (Type (ℓ-suc ℓ-zero))` | `FORMAL_CHECKED_WITH_SCOPE / HIT_FREE_NAME_LEVEL / KS_N1_FAITHFUL_REPLAY` | runs `20260927-COPUS-REPLAY-GLM-GROUPOID-UNIVERSE-01`、`20260927-COPUS-GLM-REPAIR-NEG-01/02`、`20260927-COPUS-GLM-REPAIR-Q7-01`；COPUS-R1-C01 | 原负控制 `-NEG-01` 无效（作用域错误） |
| COPUS-KS-C01 | `KS-Theorem-5-9 : (n : ℕ) → ¬ isOfHLevel (2 + n) (Type (lvl n))`，`lvl zero = ℓ-zero`，`lvl (suc n) = ℓ-suc (lvl n)` | `MACHINE_PROVED_WITH_SCOPE / HIT_FREE_NAME_LEVEL` | run `20260927-COPUS-KS-UNIVERSE-TOWER-01`；负控制 `-NEG-01/02`；COPUS-R1-C05 | Kraus–Sattler 2015 的已知定理（重放，非新数学）；不证明任何固定宇宙无层 |
| COPUS-KS-C02 | `workOrderForm : (n : ℕ) → ¬ isOfHLevel (n + 2) (Type (iterSuc n ℓ-zero))`，`iterSuc zero ℓ = ℓ`，`iterSuc (suc n) ℓ = iterSuc n (ℓ-suc ℓ)` | `MACHINE_PROVED_WITH_SCOPE / HIT_FREE_NAME_LEVEL` | 同上 | 同上 |
| COPUS-KS-C03 | `KS-Theorem-5-10-U≤ : (n : ℕ) → isOfHLevel (3 + n) (T (lvl n) n) × ¬ isOfHLevel (2 + n) (T (lvl n) n)`，`T L k = TypeOfHLevel L (2 + k)` | `MACHINE_PROVED_WITH_SCOPE / HIT_FREE_NAME_LEVEL` | 同上 | — |
| COPUS-KS-C04 | `KS-Theorem-5-10-Loop : (n : ℕ) → isOfHLevel (3 + n) (Loop (lvl n) n) × ¬ isOfHLevel (2 + n) (Loop (lvl n) n)` | `MACHINE_PROVED_WITH_SCOPE / HIT_FREE_NAME_LEVEL` | 同上 | — |
| COPUS-KS-C05 | `step : (L : Level) (k : ℕ) → NT L k → NT (ℓ-suc L) (suc k)`（U_L^{≤k} 的非平凡 (k+1)-环 ⇒ U_{L+1}^{≤k+1} 的非平凡 (k+2)-环） | `MACHINE_PROVED_WITH_SCOPE` | 同上 | — |
| COPUS-R1-C01 | `Path (List Name) (hitsOf ¬universeIsGroupoid) []`、`Path Nat (sizeOf ¬universeIsGroupoid) 251` | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` | run `20260927-COPUS-HITSCAN-CERT-GLM-01`；负控制 `20260927-COPUS-HITSCAN-NEG-01/03` | 名称级闭包（反射所见）；不是"可在无 HIT 元理论中证明"的元定理 |
| COPUS-R1-C02 | `hitsOf universeLoopSpaceAtSetIsSet ≡ []`，`sizeOf ≡ 189` | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` | run `20260927-COPUS-HITSCAN-CERT-GLM-01` | 同上 |
| COPUS-R1-C03 | `hitsOf noLevel2AscentAtSets ≡ []`，`sizeOf ≡ 190` | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` | 同上 | 同上 |
| COPUS-R1-C04 | `hitsOf typeIsNotASet ≡ []`（Opus `CG001-C-63`），`sizeOf ≡ 101` | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` | run `20260927-COPUS-HITSCAN-CERT-OPUS-01` | 同上 |
| COPUS-R1-C05 | `hitsOf` 对 `KS-Theorem-5-9`、`workOrderForm`、`KS-Theorem-5-10-U≤`、`KS-Theorem-5-10-Loop` 均为 `[]`（363/364/363/364 名） | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` | run `20260927-COPUS-HITSCAN-CERT-KS-01` | 同上 |
| COPUS-R1-C06 | `hitsOf hSetNotSet ≡ []`（Opus `CG001-C-71`），`sizeOf ≡ 149` | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` | run `20260927-COPUS-HITSCAN-CERT-OPUS-02` | 同上 |
| COPUS-R6-C01 | `hitsOf localGlobal ≡ []`（Opus `CG001-C-75` 包的 local-global 桥），`sizeOf ≡ 201` | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` | run `20260927-COPUS-HITSCAN-CERT-OPUS-01`；负控制 `20260927-COPUS-HITSCAN-NEG-02`（`CG001-C-75` 主定理依赖 HIT） | 同上 |
| COPUS-GLM-FIX-C02a | `valBetaT-refl : (t s : Tm) → cong val (betaT t s) ≡ refl`、`valBetaF-refl`（证明为 refl） | `FORMAL_CHECKED_WITH_SCOPE` | run `20260927-COPUS-GLM-REPAIR-01` | 一阶 ι 玩具片段 |
| COPUS-GLM-FIX-C02b | `glmFormHoldsAtArt : Path (Path Type (f boolTy) (f boolTy)) refl refl` 且 `faithfulFormFailsAtArt : ¬ (cong f art ≡ refl)` | `FORMAL_CHECKED_WITH_SCOPE / RUPTURE_EXHIBIT` | 同上 | 只说明 GLM 原陈述形式不能区分真实与人工等式 |
| COPUS-Q7-C01 | GLM-R3-C01 各中间步骤的显式类型重述（`hlevel3≡isGroupoid`、`a-moves`、`fst-τ`、`τ≠refl-annotated`、`fst-FAM`、`eval-loopE`、`setOfSelfEquivs`、`Q7-theorem`） | `FORMAL_CHECKED_WITH_SCOPE` | run `20260927-COPUS-GLM-REPAIR-Q7-01` | 审计者读法的内核确认；不加新数学 |

### 终局轮追加（2026-09-27）

> 写终局判词（`Cloud-Opus审计并补完GLM/14-罗素面终局判词.md`）之后追加。原为暂存区的一行类型检查，按用户"全部代码入库"的要求入库并按 F-011 捕获。同一授权（委托工作单 §6，D2 最终集成行）。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-COPUS-KS-TOWER-002` | `COPUS-KS-C06` | `formal/cloud-opus-glm-audit/ks-universe-tower/CatalogOfSetsTwoSteps.agda` | `verification/runs/20260927-COPUS-KS-CATALOG-OF-SETS-01/`；exit 0（73 s） | `MACHINE_PROVED_WITH_SCOPE`（KS 5.10 在 n = 0 的实例；无 HIT 见 COPUS-R1-C05） |
| `MP-COPUS-KS-TOWER-NEG-003` | `COPUS-KS-C06` 负控制 | `formal/cloud-opus-glm-audit/ks-universe-tower/KSNegCatalogOfSetsIsSet.agda` | `verification/runs/20260927-COPUS-KS-CATALOG-OF-SETS-NEG-01/`；exit 42，`[UnequalTerms]` | `NEGATIVE_CONTROL_REJECTED`（3 层读不成 2 层） |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| COPUS-KS-C06 | `catalogOfSetsTwoSteps : isOfHLevel 3 (hSet ℓ-zero) × (¬ isSet (hSet ℓ-zero))` | `MACHINE_PROVED_WITH_SCOPE` | run `20260927-COPUS-KS-CATALOG-OF-SETS-01`；负控制 `-NEG-01` | 只关于装集合的目录 `hSet ℓ-zero`；"追问两步就停"是对两个分量的读法 |

#### Lean 对照 `CG001-C-72` 的 Linux 重放（2026-09-27）

> Opus 的 UIP 世界对照（`CG001-C-72`，原运行在 macOS）。本会话用 Lean 4.34.0 的 Linux release 资产重放；它与 Opus 的工具链同一源码 commit `293d5d0c0c3f3dded4688b3ccd6a33939ac5102b`，`Init.olean`、`Init/Prelude.olean` 两平台逐字节相同。工具链记录 `formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN.linux-x86_64.json`；驱动沿用 CG-001 的 `lean_check.py`，未改动。首次捕获因漏解 `Init.olean.server` 失败，已整体留档于 `Cloud-Opus审计并补完GLM/附件/失败捕获-20260927-Lean缺Init配套文件/`。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-UNIVERSE-SET-LEAN-001` | `CG001-C-72` | `formal/claude-cg001/universe-set-lean/UniverseIsSet.lean` | `verification/runs/20260927-COPUS-REPLAY-CG001-UNIVERSE-SET-LEAN-01/`；exit 0；stdout 与原运行逐字节相同 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_BYTE_IDENTICAL_REPLAY`（Lean 4，UIP；不是 HoTT 命题） |
| `MP-CG001-UNIVERSE-SET-LEAN-NEG-001` | `CG001-C-72` 负控制 | `formal/claude-cg001/universe-set-lean/WrongCastFlips.lean` | `verification/runs/20260927-COPUS-REPLAY-CG001-UNIVERSE-SET-LEAN-NEG-01/`；exit 1，拒绝在目标文件第 11 行 | `NEGATIVE_CONTROL_REJECTED`（细化阶段：`cast p true` 不定义性等于 `false`） |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-72 | `theorem universeIsSet {A B : Type} (p q : A = B) : p = q := rfl`；`castIsId`、`noFlip`（均不依赖公理） | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-UNIVERSE-SET-LEAN-01`、`20260927-COPUS-REPLAY-CG001-UNIVERSE-SET-LEAN-01`；负控制 `-NEG-01` 两份 | UIP 类型论中的命题，不是 HoTT 命题；在终局判词中只作粗粒度对照（同时压平了高阶结构） |

#### 芝诺线（Opus 的 A7：无穷相干）的 Linux 重放（2026-09-27）

> 为 `docs/社区审计提交/01-芝诺悖论的幽灵.md` 捕获。Agda v2.8.0 Linux 资产 + cubical v0.9（逐字节一致）；Lean 4.34.0 Linux 资产（与原工具链同一源码 commit）。Opus 的原运行 `20260926-CG001-*` 保持原样。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-SST-FINITE-LEVELS-001` | `CG001-C-62` | `formal/claude-cg001/sst-finite-levels/SSTLevels.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-SST-FINITE-LEVELS-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-SST-FINITE-LEVELS-NEG-001` | `CG001-C-62` 负控制 | `formal/claude-cg001/sst-finite-levels/WrongFace.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-SST-FINITE-LEVELS-NEG-01/`；exit 42，`UnequalTerms` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-WILD-SST-001` | `CG001-C-64` | `formal/claude-cg001/wild-sst/WildSST.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-WILD-SST-NEG-001` | `CG001-C-64` 负控制 | `formal/claude-cg001/wild-sst/WrongSpinCoherent.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-NEG-01/`；exit 42，`UnequalTerms` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-WILD-SST-LEAN-001` | `CG001-C-65` | `formal/claude-cg001/wild-sst-lean/WildSSTUIP.lean` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-LEAN-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-WILD-SST-LEAN-NEG-001` | `CG001-C-65` 负控制 | `formal/claude-cg001/wild-sst-lean/WrongRoute.lean` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-LEAN-NEG-01/`；exit 1，`ELABORATION_ERROR_IN_TARGET` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-WILD-SST2-001` | `CG001-C-66` | `formal/claude-cg001/wild-sst/WildSST2.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST2-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-WILD-SST2-NEG-001` | `CG001-C-66` 负控制 | `formal/claude-cg001/wild-sst/WrongSurfTrivial.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST2-NEG-01/`；exit 42，`UnequalTerms` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-SELF-INTERPRETATION-001` | `CG001-C-67` | `formal/claude-cg001/self-interpretation/SelfInterpretation.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-SELF-INTERPRETATION-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-SELF-INTERPRETATION-NEG-001` | `CG001-C-67` 负控制 | `formal/claude-cg001/self-interpretation/WrongFlipIsIdentity.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-SELF-INTERPRETATION-NEG-01/`；exit 42，`UnequalTerms` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-WILD-SST-P4-001` | `CG001-C-68` | `formal/claude-cg001/wild-sst/WildSSTP4Flat.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-P4-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-WILD-SST-P4-NEG-001` | `CG001-C-68` 负控制 | `formal/claude-cg001/wild-sst/WrongSurfMoveTrivial.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-P4-NEG-01/`；exit 42，`UnequalTerms` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-WINDING-COCYCLE-001` | `CG001-C-69` | `formal/claude-cg001/wild-sst/WindingCocycle.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WINDING-COCYCLE-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-WINDING-COCYCLE-NEG-001` | `CG001-C-69` 负控制 | `formal/claude-cg001/wild-sst/WrongSpinWCocycle.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WINDING-COCYCLE-NEG-01/`；exit 42，`UnequalTerms` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-WILD-SST-LEVELS-001` | `CG001-C-70` | `formal/claude-cg001/wild-sst/WildSSTP4Levels.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-LEVELS-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-WILD-SST-LEVELS-NEG-001` | `CG001-C-70` 负控制 | `formal/claude-cg001/wild-sst/WrongS2Groupoid.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-LEVELS-NEG-01/`；exit 42，`UnequalTerms` | `NEGATIVE_CONTROL_REJECTED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-62 | `SST≤0 … SST≤5 : Type₁` 与平凡居民（外部生成器逐层打印） | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-SST-FINITE-LEVELS-01`、`20260927-COPUS-REPLAY-CG001-SST-FINITE-LEVELS-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |
| CG001-C-64 | `WildSST`、`Coh₂`、`setsCohere`；`spin`：两条路线绕 1 圈与 2 圈，`spinIncoherent : ¬ Coh₂ spin` | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-WILD-SST-01`、`20260927-COPUS-REPLAY-CG001-WILD-SST-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |
| CG001-C-65 | Lean 4（UIP）：`theorem coh2 (S : WildSST) : Coh2 S := fun _ _ _ _ _ _ _ => rfl` | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-WILD-SST-LEAN-01`、`20260927-COPUS-REPLAY-CG001-WILD-SST-LEAN-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |
| CG001-C-66 | `surf≢refl`；`flat` 上两个不同的六边形填充；`Deg₃` 对一个成立、对另一个不成立 | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-WILD-SST2-01`、`20260927-COPUS-REPLAY-CG001-WILD-SST2-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |
| CG001-C-67 | 玩具语法自解释两难：`faithful∞`、`syntax∞IsNotASet`、`noFaithfulForFacts` | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-SELF-INTERPRETATION-01`、`20260927-COPUS-REPLAY-CG001-SELF-INTERPRETATION-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |
| CG001-C-68 | 一般第二级相干 `Coh₃`（P₄）：`notCoh₃ : ¬ Coh₃ flatSurfᵢ`、`coh₃Trivial : Coh₃ flatTrivialᵢ` | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-WILD-SST-P4-01`、`20260927-COPUS-REPLAY-CG001-WILD-SST-P4-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |
| CG001-C-69 | 圆周值结构上 `Coh₂` ⇔ 绕数上闭链方程；`spinW` 不相干、`uniformW` 相干 | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-WINDING-COCYCLE-01`、`20260927-COPUS-REPLAY-CG001-WINDING-COCYCLE-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |
| CG001-C-70 | 集合 ⇒ `Coh₂ᵢ`；群胚 ⇒ `Coh₂ᵢ` 为命题且 `Coh₃` 成立；`flatS¹` 数据唯一 | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-WILD-SST-LEVELS-01`、`20260927-COPUS-REPLAY-CG001-WILD-SST-LEVELS-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |

#### 自查轮追加：Lean 对照的补充控制（2026-09-27）

> 用户要求对本会话后来的工作做声明层与证明层的自查。查出 Opus 的 `CG001-C-65` 负控制 `WrongRoute.lean` 注释声称检验"首尾记账、内核拒绝"，实际报错落在一步的参数上、由细化器报出；`CG001-C-72` 负控制的注释也把细化器拒绝写成 "KERNEL_REJECTED"。两个主定理不受影响。补上的控制见 `formal/cloud-opus-glm-audit/lean-controls/CLAIM.md`；原包只增不改的说明 `formal/claude-cg001/wild-sst-lean/REVISIONS.md`、`formal/claude-cg001/universe-set-lean/REVISIONS.md`。工具链记录 `formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN_META.linux-x86_64.json`。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-COPUS-LEAN-C65-ENDPOINT-NEG-001` | `CG001-C-65` 首尾负控制 | `formal/cloud-opus-glm-audit/lean-controls/WrongRouteEndpoint.lean` | `verification/runs/20260927-COPUS-LEAN-C65-ENDPOINT-NEG-01/`；exit 1，`ELABORATION_ERROR_IN_TARGET` | `NEGATIVE_CONTROL_REJECTED`（细化器在第二、三步的接口处拒绝） |
| `MP-COPUS-LEAN-C65-KERNEL-001` | `COPUS-LEAN-C01` | `formal/cloud-opus-glm-audit/lean-controls/KernelRoute.lean` | `verification/runs/20260927-COPUS-LEAN-C65-KERNEL-01/`；exit 0（含 `leanchecker --fresh`） | `KERNEL_ACCEPTED_WITH_SCOPE`（经 `Lean.addDecl` 由内核接受；Lean 4，UIP） |
| `MP-COPUS-LEAN-C65-KERNEL-NEG-001` | `COPUS-LEAN-C01` 负控制 | `formal/cloud-opus-glm-audit/lean-controls/KernelRouteEndpoint.lean` | `verification/runs/20260927-COPUS-LEAN-C65-KERNEL-NEG-01/`；exit 1，`KERNEL_ERROR_IN_TARGET` | `NEGATIVE_CONTROL_REJECTED`（内核本身：`(kernel) application type mismatch`） |
| `MP-COPUS-LEAN-C72-KERNEL-001` | `COPUS-LEAN-C02` | `formal/cloud-opus-glm-audit/lean-controls/KernelCast.lean` | `verification/runs/20260927-COPUS-LEAN-C72-KERNEL-01/`；exit 0（含 `leanchecker --fresh`） | `KERNEL_ACCEPTED_WITH_SCOPE`（经 `Lean.addDecl` 由内核接受；Lean 4，UIP） |
| `MP-COPUS-LEAN-C72-KERNEL-NEG-001` | `COPUS-LEAN-C02` 负控制 | `formal/cloud-opus-glm-audit/lean-controls/KernelCastFlips.lean` | `verification/runs/20260927-COPUS-LEAN-C72-KERNEL-NEG-01/`；exit 1，`KERNEL_ERROR_IN_TARGET` | `NEGATIVE_CONTROL_REJECTED`（内核本身：`(kernel) declaration type mismatch`） |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| COPUS-LEAN-C01 | `kernelRouteA`：陈述取自 `routeA`、证明项为显式首尾的 `Eq.trans stepOne (Eq.trans stepTwo stepThree)`，经 `Lean.addDecl` 交给内核而被接受；`kernelRouteA_states_routeA : @kernelRouteA = @routeA := rfl`；均不依赖公理 | `MACHINE_PROVED_WITH_SCOPE` | run `20260927-COPUS-LEAN-C65-KERNEL-01`；负控制 `20260927-COPUS-LEAN-C65-KERNEL-NEG-01`、`20260927-COPUS-LEAN-C65-ENDPOINT-NEG-01` | UIP 类型论中的命题；不给 `CG001-C-65` 增加新数学；负控制不证明 Lean 内核一般可靠 |
| COPUS-LEAN-C02 | `kernelCastIsId : ∀ (p : Bool = Bool), cast p true = true`（证明项 `fun p => Eq.refl true`，经 `Lean.addDecl` 交给内核）被接受；`kernelCastIsId_states_castIsId : @kernelCastIsId = fun p => castIsId p true := rfl` | `MACHINE_PROVED_WITH_SCOPE` | run `20260927-COPUS-LEAN-C72-KERNEL-01`；负控制 `20260927-COPUS-LEAN-C72-KERNEL-NEG-01` | UIP 类型论中的命题，不是 HoTT 命题 |

## 3. 芝诺线、Delay 语义与共用对照

> 这些命题的行在 `dev` 上的目标内索引里（`.claude/goals/CG-001-targeted-overview/relay.md` 的 R1 草稿），尚未登记进共享矩阵；每个运行另有逐字节重放的输出，在 `dev` 上的 `.claude/goals/CG-001-targeted-overview/verification/`。命题全文与禁止外推以各包的 `CLAIM.md` 为准。

### 3.1 证明包与运行（逐字）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-PEDOMETER-SEMANTICS-001` | `CG001-C-55`、`CG001-C-56` | `formal/claude-cg001/pedometer-semantics/PedometerSemantics.agda`（命题全文 `CLAIM.md`） | `verification/runs/20260925-CG001-PEDOMETER-SEMANTICS-01/`；exit 0，stderr 0 B，零警告；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记） |
| `MP-CG001-PEDOMETER-SEMANTICS-NEG-001` | `CG001-C-55`（负控制） | `formal/claude-cg001/pedometer-semantics/WrongPRevHalts.agda` | `verification/runs/20260925-CG001-PEDOMETER-SEMANTICS-NEG-01/`；exit 42，`nothing != just 1` | `KERNEL_REJECTED_AS_EXPECTED` |
| `MP-CG001-PEDOMETER-SEMANTICS-NEG-002` | `CG001-C-56`（负控制） | `formal/claude-cg001/pedometer-semantics/WrongReverseFixesGo.agda` | `verification/runs/20260925-CG001-PEDOMETER-SEMANTICS-NEG-02/`；exit 42，`back (~ i) != go i` | `KERNEL_REJECTED_AS_EXPECTED` |
| `MP-CG001-DELAY-MONAD-001` | `CG001-C-59` | `formal/claude-cg001/pedometer-semantics/DelayMonad.agda`（导入 `PedometerSemantics.agda`；命题全文 `CLAIM-C59.md`） | `verification/runs/20260925-CG001-DELAY-MONAD-01/`；exit 0，stderr 0 B，零警告；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记） |
| `MP-CG001-DELAY-MONAD-NEG-001` | `CG001-C-59`（负控制） | `formal/claude-cg001/pedometer-semantics/WrongNeverBindRefl.agda` | `verification/runs/20260925-CG001-DELAY-MONAD-NEG-01/`；exit 42，`bind never f != never of type Delay B` | `KERNEL_REJECTED_AS_EXPECTED` |
| `MP-CG001-SST-FINITE-LEVELS-001` | `CG001-C-62` | `formal/claude-cg001/sst-finite-levels/SSTLevels.agda`（由同目录 `gen_sst.py 5` 生成） | `verification/runs/20260926-CG001-SST-FINITE-LEVELS-01/`；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记） |
| `MP-CG001-SST-FINITE-LEVELS-NEG-001` | `CG001-C-62`（负控制） | `formal/claude-cg001/sst-finite-levels/WrongFace.agda` | `verification/runs/20260926-CG001-SST-FINITE-LEVELS-NEG-01/`；exit 42，`x2 != x3 of type A0` | `KERNEL_REJECTED_AS_EXPECTED` |
| `MP-CG001-UIP-ESCAPE-001` | `CG001-C-63` | `formal/claude-cg001/uip-escape/UIPEscape.agda` | `verification/runs/20260926-CG001-UIP-ESCAPE-01/`；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记） |
| `MP-CG001-UIP-ESCAPE-NEG-001` | `CG001-C-63`（负控制） | `formal/claude-cg001/uip-escape/WrongTransport.agda` | `verification/runs/20260926-CG001-UIP-ESCAPE-NEG-01/`；exit 42，`false != true of type Bool` | `KERNEL_REJECTED_AS_EXPECTED` |
| `MP-CG001-WILD-SST-001` | `CG001-C-64` | `formal/claude-cg001/wild-sst/WildSST.agda` | `verification/runs/20260926-CG001-WILD-SST-01/`；exit 0，stderr 0 B，零警告；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记） |
| `MP-CG001-WILD-SST-NEG-001` | `CG001-C-64`（负控制） | `formal/claude-cg001/wild-sst/WrongSpinCoherent.agda` | `verification/runs/20260926-CG001-WILD-SST-NEG-01/`；exit 42，`1 != 2 of type Nat` | `KERNEL_REJECTED_AS_EXPECTED` |
| `MP-CG001-WILD-SST-LEAN-001` | `CG001-C-65` | `formal/claude-cg001/wild-sst-lean/WildSSTUIP.lean`（**Lean 4.34.0**） | `verification/runs/20260926-CG001-WILD-SST-LEAN-01/`；exit 0，4 条定理零公理，`leanchecker --fresh` 通过；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记；Lean 行） |
| `MP-CG001-WILD-SST-LEAN-NEG-001` | `CG001-C-65`（负控制） | `formal/claude-cg001/wild-sst-lean/WrongRoute.lean` | `verification/runs/20260926-CG001-WILD-SST-LEAN-NEG-01/`；exit 1，“Application type mismatch” | `KERNEL_REJECTED_AS_EXPECTED` |
| `MP-CG001-WILD-SST2-001` | `CG001-C-66` | `formal/claude-cg001/wild-sst/WildSST2.agda`（导入 `WildSST.agda`；命题全文 `CLAIM-C66.md`；辅助 `p4_faces.py` 与输出） | `verification/runs/20260926-CG001-WILD-SST2-01/`；exit 0，stderr 0 B，零警告；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记；“一般 P₄ 化为 Deg₃”为手推，勿登记为机器证明） |
| `MP-CG001-WILD-SST2-NEG-001` | `CG001-C-66`（负控制） | `formal/claude-cg001/wild-sst/WrongSurfTrivial.agda` | `verification/runs/20260926-CG001-WILD-SST2-NEG-01/`；exit 42，`negsuc zero != pos 0 of type ℤ` | `KERNEL_REJECTED_AS_EXPECTED` |
| `MP-CG001-SELF-INTERPRETATION-001` | `CG001-C-67` | `formal/claude-cg001/self-interpretation/SelfInterpretation.agda` | `verification/runs/20260926-CG001-SELF-INTERPRETATION-01/`；exit 0，stderr 0 B，零警告；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记） |
| `MP-CG001-SELF-INTERPRETATION-NEG-001` | `CG001-C-67`（负控制） | `formal/claude-cg001/self-interpretation/WrongFlipIsIdentity.agda` | `verification/runs/20260926-CG001-SELF-INTERPRETATION-NEG-01/`；exit 42，`x != x₁ of type Bool` | `KERNEL_REJECTED_AS_EXPECTED` |
| `MP-CG001-WILD-SST-P4-001` | `CG001-C-68` | `formal/claude-cg001/wild-sst/WildSSTP4Flat.agda`（导入 `WildSSTP4.agda`；二者由 `gen_p4.py` 生成；命题全文 `CLAIM-C68.md`；结构清单 `P4_STRUCTURE.txt`） | `verification/runs/20260926-CG001-WILD-SST-P4-01/`；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记；取代 C-66 的手推一步） |
| `MP-CG001-WILD-SST-P4-NEG-001` | `CG001-C-68`（负控制） | `formal/claude-cg001/wild-sst/WrongSurfMoveTrivial.agda` | `verification/runs/20260926-CG001-WILD-SST-P4-NEG-01/`；exit 42，面不是 `refl`（`i ∨ ~ i != (~ i₁ ∨ i₁) ∨ ~ i ∨ i of type I`） | `KERNEL_REJECTED_AS_EXPECTED` |
| `MP-CG001-WINDING-COCYCLE-001` | `CG001-C-69` | `formal/claude-cg001/wild-sst/WindingCocycle.agda`（命题全文 `CLAIM-C69.md`；辅助 `p3_routes.py` 与输出） | `verification/runs/20260926-CG001-WINDING-COCYCLE-01/`；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记） |
| `MP-CG001-WINDING-COCYCLE-NEG-001` | `CG001-C-69`（负控制） | `formal/claude-cg001/wild-sst/WrongSpinWCocycle.agda` | `verification/runs/20260926-CG001-WINDING-COCYCLE-NEG-01/`；exit 42，`1 != 2 of type ℕ` | `KERNEL_REJECTED_AS_EXPECTED` |
| `MP-CG001-WILD-SST-LEVELS-001` | `CG001-C-70` | `formal/claude-cg001/wild-sst/WildSSTP4Levels.agda`（命题全文 `CLAIM-C70.md`） | `verification/runs/20260926-CG001-WILD-SST-LEVELS-01/`；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记；一般的 t+1 规律为元层论证，勿登记为机器定理） |
| `MP-CG001-WILD-SST-LEVELS-NEG-001` | `CG001-C-70`（负控制） | `formal/claude-cg001/wild-sst/WrongS2Groupoid.agda` | `verification/runs/20260926-CG001-WILD-SST-LEVELS-NEG-01/`；exit 42，`S² !=< S¹` | `KERNEL_REJECTED_AS_EXPECTED` |
| `MP-CG001-UNIVERSE-SET-LEAN-001` | `CG001-C-72` | `formal/claude-cg001/universe-set-lean/UniverseIsSet.lean`（**Lean 4.34.0**） | `verification/runs/20260926-CG001-UNIVERSE-SET-LEAN-01/`；exit 0，3 条定理零公理，`leanchecker --fresh` 通过；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记；Lean 行，UIP 类型论中的对照） |
| `MP-CG001-UNIVERSE-SET-LEAN-NEG-001` | `CG001-C-72`（负控制） | `formal/claude-cg001/universe-set-lean/WrongCastFlips.lean` | `verification/runs/20260926-CG001-UNIVERSE-SET-LEAN-NEG-01/`；exit 1，Type mismatch | `KERNEL_REJECTED_AS_EXPECTED` |

### 3.2 命题一句话（逐字）

| 命题 | 一句话 | 包 |
|---|---|---|
| `CG001-C-55` | 停机过程作为程序（Delay 单子）：无见证即等于 `never`；P-rev 与随身即运输的规格下，“多走 2 步就停”的程序等于 `never`（任意类型、路径、族）；在 C-50、C-51、列表三种规格下同一程序一步收敛 | pedometer-semantics |
| `CG001-C-56` | 方向是一种选择：C-50 的地点类型有固定两镇的对合自等价，把 `go` 送到 `sym back`、`back` 送到 `sym go`，经它携带的计数沿 `go` 为 −1、沿 `sym go` 为 +1 | pedometer-semantics |
| `CG001-C-59` | C-55 所用 `Delay` 的单子结构（导入同一类型）：`return`、`bind` 与三条单子律为路径；`never` 为 `bind` 的左零元、不等于任何 `return a`；`d ≡ never` 当且仅当对一切燃料 `runFor n d ≡ nothing`；纯后续映射有限观察；P-rev 规格的停机程序对一切燃料返回 `nothing`、接任何后续都等于 `never`，另三种规格下“停下后报告计数加一”在燃料 1 报出 2 | pedometer-semantics（`CLAIM-C59.md`） |
| `CG001-C-62` | 外部程序对 n = 0..5 逐层打印 n 截断半单纯类型的类型（第 m 层 2^{m+1} − 2 个面参数），Cubical Agda 逐层接受并各有平凡居民；不涉及理论内部的统一族 F : ℕ → U（开放问题） | sst-finite-levels |
| `CG001-C-63` | `ua notEquiv ≠ refl`，宇宙不是集合；集合之上沿任意两条证明的搬运相等；宇宙之上沿 `ua notEquiv` 与 `refl` 的搬运在 `true` 处不同 | uip-escape |
| `CG001-C-64` | 预层式半单纯结构 WildSST 与六边形相干 Coh₂：各层都是集合则 Coh₂ 成立；实例 spin（各层 S¹、面映射为恒等、一条恒等式取 rotLoop）满足全部面恒等式，但两条路线绕 1 圈与 2 圈，¬ Coh₂ spin | wild-sst |
| `CG001-C-65` | 同一预层式定义在 Lean 4（UIP）中：coh2 : ∀ S, Coh2 S 由 rfl 成立，零公理 | wild-sst-lean |
| `CG001-C-66` | 第二级：Hopf 族把 surf 搬运成绕数 −1 的环，surf ≠ refl；退化结构 flat 上两个不同的六边形填充；Deg₃ 对全 refl 成立、对 surf 填充在 (0,0,0,1) 不成立（“一般 P₄ 化为 Deg₃”为手推加 p4_faces.py 核对） | wild-sst（`CLAIM-C66.md`） |
| `CG001-C-67` | HoTT 吃掉自己的缩影：玩具语法不截断时忠实解释进宇宙存在而语法不是集合；截断成集合时可解释进 hProp，但没有函数进单价宇宙把 swap 送到翻转 | self-interpretation |
| `CG001-C-68` | 一般的第二级相干 `Coh₃`（P₄）由生成器写成类型，两个半球 6 步与 8 步划分全部 14 个面；在 C-66 的 flat 上，surf 填充违反 `Coh₃`，全 `refl` 满足（取代 C-66 的手推） | wild-sst（`CLAIM-C68.md`） |
| `CG001-C-69` | 圆周值结构（面映射为恒等、恒等式为绕数 w 的环）上，`Coh₂` 与绕数上闭链方程互推；`spinW`、`levelW` 不相干，`uniformW` 相干 | wild-sst（`CLAIM-C69.md`） |
| `CG001-C-70` | 各层是集合则 `Coh₂ᵢ` 成立；各层是群胚则 `Coh₂ᵢ` 是命题、`Coh₃` 对任何六边形数据成立；圆周上的 flat 形状六边形数据唯一且满足 `Coh₃` | wild-sst（`CLAIM-C70.md`） |
| `CG001-C-72` | Lean 4（UIP）中宇宙是集合；沿 `Bool = Bool` 的 cast 是恒等；Bool 的自认同不能把 `true` 送到 `false` | universe-set-lean |

## 4. 运行清单

| 运行 | 证明 | 命题 | 证明器 | 记录的结局 | 单元 |
|---|---|---|---|---|---|
| `20260925-CG001-DELAY-MONAD-01` | `MP-CG001-DELAY-MONAD-001` | CG001-C-59 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260925-CG001-DELAY-MONAD-NEG-01` | `MP-CG001-DELAY-MONAD-NEG-001` | CG001-C-59 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260925-CG001-PEDOMETER-SEMANTICS-01` | `MP-CG001-PEDOMETER-SEMANTICS-001` | CG001-C-55、CG001-C-56 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260925-CG001-PEDOMETER-SEMANTICS-NEG-01` | `MP-CG001-PEDOMETER-SEMANTICS-NEG-001` | CG001-C-55 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260925-CG001-PEDOMETER-SEMANTICS-NEG-02` | `MP-CG001-PEDOMETER-SEMANTICS-NEG-002` | CG001-C-56 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260926-CG001-COPIES-OF-BOOL-01` | `MP-CG001-COPIES-OF-BOOL-001` | CG001-C-74 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260926-CG001-COPIES-OF-BOOL-NEG-01` | `MP-CG001-COPIES-OF-BOOL-NEG-001` | CG001-C-74 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260926-CG001-HSET-UNIVERSE-01` | `MP-CG001-HSET-UNIVERSE-001` | CG001-C-71 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR、A7 |
| `20260926-CG001-HSET-UNIVERSE-NEG-01` | `MP-CG001-HSET-UNIVERSE-NEG-001` | CG001-C-71 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR、A7 |
| `20260926-CG001-SELF-INTERPRETATION-01` | `MP-CG001-SELF-INTERPRETATION-001` | CG001-C-67 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260926-CG001-SELF-INTERPRETATION-NEG-01` | `MP-CG001-SELF-INTERPRETATION-NEG-001` | CG001-C-67 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | A7 |
| `20260926-CG001-SST-FINITE-LEVELS-01` | `MP-CG001-SST-FINITE-LEVELS-001` | CG001-C-62 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260926-CG001-SST-FINITE-LEVELS-NEG-01` | `MP-CG001-SST-FINITE-LEVELS-NEG-001` | CG001-C-62 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | A7 |
| `20260926-CG001-TOTALITY-ESCALATION-01` | `MP-CG001-TOTALITY-ESCALATION-001` | CG001-C-73 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260926-CG001-TOTALITY-ESCALATION-NEG-01` | `MP-CG001-TOTALITY-ESCALATION-NEG-001` | CG001-C-73 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260926-CG001-UIP-ESCAPE-01` | `MP-CG001-UIP-ESCAPE-001` | CG001-C-63 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR、A7 |
| `20260926-CG001-UIP-ESCAPE-NEG-01` | `MP-CG001-UIP-ESCAPE-NEG-001` | CG001-C-63 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR、A7 |
| `20260926-CG001-UNIVERSE-QUESTIONING-01` | `MP-CG001-UNIVERSE-QUESTIONING-001` | CG001-C-75、CG001-C-76 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260926-CG001-UNIVERSE-QUESTIONING-NEG-01` | `MP-CG001-UNIVERSE-QUESTIONING-NEG-001` | CG001-C-75 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260926-CG001-UNIVERSE-SET-LEAN-01` | `MP-CG001-UNIVERSE-SET-LEAN-001` | CG001-C-72 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR、A7 |
| `20260926-CG001-UNIVERSE-SET-LEAN-NEG-01` | `MP-CG001-UNIVERSE-SET-LEAN-NEG-001` | CG001-C-72 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | UR、A7 |
| `20260926-CG001-WILD-SST-01` | `MP-CG001-WILD-SST-001` | CG001-C-64 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260926-CG001-WILD-SST-LEAN-01` | `MP-CG001-WILD-SST-LEAN-001` | CG001-C-65 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260926-CG001-WILD-SST-LEAN-NEG-01` | `MP-CG001-WILD-SST-LEAN-NEG-001` | CG001-C-65 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | A7 |
| `20260926-CG001-WILD-SST-LEVELS-01` | `MP-CG001-WILD-SST-LEVELS-001` | CG001-C-70 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260926-CG001-WILD-SST-LEVELS-NEG-01` | `MP-CG001-WILD-SST-LEVELS-NEG-001` | CG001-C-70 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | A7 |
| `20260926-CG001-WILD-SST-NEG-01` | `MP-CG001-WILD-SST-NEG-001` | CG001-C-64 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | A7 |
| `20260926-CG001-WILD-SST-P4-01` | `MP-CG001-WILD-SST-P4-001` | CG001-C-68 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260926-CG001-WILD-SST-P4-NEG-01` | `MP-CG001-WILD-SST-P4-NEG-001` | CG001-C-68 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | A7 |
| `20260926-CG001-WILD-SST2-01` | `MP-CG001-WILD-SST2-001` | CG001-C-66 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260926-CG001-WILD-SST2-NEG-01` | `MP-CG001-WILD-SST2-NEG-001` | CG001-C-66 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | A7 |
| `20260926-CG001-WINDING-COCYCLE-01` | `MP-CG001-WINDING-COCYCLE-001` | CG001-C-69 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260926-CG001-WINDING-COCYCLE-NEG-01` | `MP-CG001-WINDING-COCYCLE-NEG-001` | CG001-C-69 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | A7 |
| `20260926-GLM-ASCENT-STALL-01` | `MP-GLM-RUSSELL-STALL-001` | GLM-R2-C01、GLM-R2-C02 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260926-GLM-GROUPOID-UNIVERSE-01` | `MP-GLM-RUSSELL-GROUPOID-001` | GLM-R3-C01 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260926-GLM-GROUPOID-UNIVERSE-NEG-01` | `MP-GLM-RUSSELL-GROUPOID-NEG-001` | GLM-R3-C01 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED_AS_EXPECTED` | UR |
| `20260926-GLM-IOTA-SYNTAX-01` | `MP-GLM-RUSSELL-IOTA-001` | GLM-R1-C02、GLM-R1-C03 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260926-GLM-IOTA-SYNTAX-02` | `MP-GLM-RUSSELL-IOTA-002` | GLM-R1-C01 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260926-GLM-IOTA-SYNTAX-NEG-01` | `MP-GLM-RUSSELL-IOTA-NEG-001` | GLM-R1-C03 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED_AS_EXPECTED` | UR |
| `20260927-COPUS-GLM-REPAIR-01` | `MP-COPUS-GLM-FIX-001` | COPUS-GLM-FIX-C02a、COPUS-GLM-FIX-C02b | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260927-COPUS-GLM-REPAIR-NEG-01` | `MP-COPUS-GLM-FIX-NEG-001` | GLM-R3-C01 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260927-COPUS-GLM-REPAIR-NEG-02` | `MP-COPUS-GLM-FIX-NEG-002` | GLM-R3-C01 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260927-COPUS-GLM-REPAIR-NEG-03` | `MP-COPUS-GLM-FIX-NEG-003` | GLM-R1-C03 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260927-COPUS-GLM-REPAIR-Q7-01` | `MP-COPUS-Q7-001` | COPUS-Q7-C01 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260927-COPUS-HITSCAN-CERT-GLM-01` | `MP-COPUS-HITSCAN-001` | COPUS-R1-C01、COPUS-R1-C02、COPUS-R1-C03 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260927-COPUS-HITSCAN-CERT-KS-01` | `MP-COPUS-HITSCAN-003` | COPUS-R1-C05 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260927-COPUS-HITSCAN-CERT-OPUS-01` | `MP-COPUS-HITSCAN-002` | COPUS-R1-C04、COPUS-R6-C01 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260927-COPUS-HITSCAN-CERT-OPUS-02` | `MP-COPUS-HITSCAN-004` | COPUS-R1-C06 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260927-COPUS-HITSCAN-NEG-01` | `MP-COPUS-HITSCAN-NEG-001` | COPUS-R1-C01 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260927-COPUS-HITSCAN-NEG-02` | `MP-COPUS-HITSCAN-NEG-002` | COPUS-R6-C01 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260927-COPUS-HITSCAN-NEG-03` | `MP-COPUS-HITSCAN-NEG-003` | COPUS-R1-C01 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260927-COPUS-KS-CATALOG-OF-SETS-01` | `MP-COPUS-KS-TOWER-002` | COPUS-KS-C06 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260927-COPUS-KS-CATALOG-OF-SETS-NEG-01` | `MP-COPUS-KS-TOWER-NEG-003` | COPUS-KS-C06 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260927-COPUS-KS-UNIVERSE-TOWER-01` | `MP-COPUS-KS-TOWER-001` | COPUS-KS-C01、COPUS-KS-C02、COPUS-KS-C03、COPUS-KS-C04、COPUS-KS-C05 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260927-COPUS-KS-UNIVERSE-TOWER-NEG-01` | `MP-COPUS-KS-TOWER-NEG-001` | COPUS-KS-C01 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260927-COPUS-KS-UNIVERSE-TOWER-NEG-02` | `MP-COPUS-KS-TOWER-NEG-002` | COPUS-KS-C01 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260927-COPUS-LEAN-C65-ENDPOINT-NEG-01` | `MP-COPUS-LEAN-C65-ENDPOINT-NEG-001` | CG001-C-65 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | A7 |
| `20260927-COPUS-LEAN-C65-KERNEL-01` | `MP-COPUS-LEAN-C65-KERNEL-001` | COPUS-LEAN-C01 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260927-COPUS-LEAN-C65-KERNEL-NEG-01` | `MP-COPUS-LEAN-C65-KERNEL-NEG-001` | COPUS-LEAN-C01 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | A7 |
| `20260927-COPUS-LEAN-C72-KERNEL-01` | `MP-COPUS-LEAN-C72-KERNEL-001` | COPUS-LEAN-C02 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR、A7 |
| `20260927-COPUS-LEAN-C72-KERNEL-NEG-01` | `MP-COPUS-LEAN-C72-KERNEL-NEG-001` | COPUS-LEAN-C02 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | UR、A7 |
| `20260927-COPUS-REPLAY-CG001-SELF-INTERPRETATION-01` | `MP-CG001-SELF-INTERPRETATION-001` | CG001-C-67 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260927-COPUS-REPLAY-CG001-SELF-INTERPRETATION-NEG-01` | `MP-CG001-SELF-INTERPRETATION-NEG-001` | CG001-C-67 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | A7 |
| `20260927-COPUS-REPLAY-CG001-SST-FINITE-LEVELS-01` | `MP-CG001-SST-FINITE-LEVELS-001` | CG001-C-62 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260927-COPUS-REPLAY-CG001-SST-FINITE-LEVELS-NEG-01` | `MP-CG001-SST-FINITE-LEVELS-NEG-001` | CG001-C-62 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | A7 |
| `20260927-COPUS-REPLAY-CG001-UNIVERSE-SET-LEAN-01` | `MP-CG001-UNIVERSE-SET-LEAN-001` | CG001-C-72 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR、A7 |
| `20260927-COPUS-REPLAY-CG001-UNIVERSE-SET-LEAN-NEG-01` | `MP-CG001-UNIVERSE-SET-LEAN-NEG-001` | CG001-C-72 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | UR、A7 |
| `20260927-COPUS-REPLAY-CG001-WILD-SST-01` | `MP-CG001-WILD-SST-001` | CG001-C-64 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260927-COPUS-REPLAY-CG001-WILD-SST-LEAN-01` | `MP-CG001-WILD-SST-LEAN-001` | CG001-C-65 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260927-COPUS-REPLAY-CG001-WILD-SST-LEAN-NEG-01` | `MP-CG001-WILD-SST-LEAN-NEG-001` | CG001-C-65 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | A7 |
| `20260927-COPUS-REPLAY-CG001-WILD-SST-LEVELS-01` | `MP-CG001-WILD-SST-LEVELS-001` | CG001-C-70 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260927-COPUS-REPLAY-CG001-WILD-SST-LEVELS-NEG-01` | `MP-CG001-WILD-SST-LEVELS-NEG-001` | CG001-C-70 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | A7 |
| `20260927-COPUS-REPLAY-CG001-WILD-SST-NEG-01` | `MP-CG001-WILD-SST-NEG-001` | CG001-C-64 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | A7 |
| `20260927-COPUS-REPLAY-CG001-WILD-SST-P4-01` | `MP-CG001-WILD-SST-P4-001` | CG001-C-68 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260927-COPUS-REPLAY-CG001-WILD-SST-P4-NEG-01` | `MP-CG001-WILD-SST-P4-NEG-001` | CG001-C-68 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | A7 |
| `20260927-COPUS-REPLAY-CG001-WILD-SST2-01` | `MP-CG001-WILD-SST2-001` | CG001-C-66 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260927-COPUS-REPLAY-CG001-WILD-SST2-NEG-01` | `MP-CG001-WILD-SST2-NEG-001` | CG001-C-66 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | A7 |
| `20260927-COPUS-REPLAY-CG001-WINDING-COCYCLE-01` | `MP-CG001-WINDING-COCYCLE-001` | CG001-C-69 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | A7 |
| `20260927-COPUS-REPLAY-CG001-WINDING-COCYCLE-NEG-01` | `MP-CG001-WINDING-COCYCLE-NEG-001` | CG001-C-69 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | A7 |
| `20260927-COPUS-REPLAY-GLM-ASCENT-STALL-01` | `MP-GLM-RUSSELL-STALL-001` | GLM-R2-C01、GLM-R2-C02 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260927-COPUS-REPLAY-GLM-GROUPOID-UNIVERSE-01` | `MP-GLM-RUSSELL-GROUPOID-001` | GLM-R3-C01 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260927-COPUS-REPLAY-GLM-GROUPOID-UNIVERSE-NEG-01` | `MP-GLM-RUSSELL-GROUPOID-NEG-001` | GLM-R3-C01 | Cubical Agda | 被拒（预期），exit 42，`REJECTED_BEFORE_TYPE_CHECKING` | UR |
| `20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-01` | `MP-GLM-RUSSELL-IOTA-001` | GLM-R1-C02、GLM-R1-C03 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-02` | `MP-GLM-RUSSELL-IOTA-002` | GLM-R1-C01 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-NEG-01` | `MP-GLM-RUSSELL-IOTA-NEG-001` | GLM-R1-C03 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260930-CG001-PRODUCT-QUESTIONING-01` | `MP-CG001-PRODUCT-QUESTIONING-001` | CG001-C-81、CG001-C-82 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260930-CG001-PRODUCT-QUESTIONING-NEG-01` | `MP-CG001-PRODUCT-QUESTIONING-NEG-001` | CG001-C-81 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260930-CG001-PRODUCT-QUESTIONING-NEG-02` | `MP-CG001-PRODUCT-QUESTIONING-NEG-002` | CG001-C-81 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260930-CG001-PRODUCT-QUESTIONING-NEG-03` | `MP-CG001-PRODUCT-QUESTIONING-NEG-003` | CG001-C-82 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260930-CG001-PRODUCT-QUESTIONING-NEG-04` | `MP-CG001-PRODUCT-QUESTIONING-NEG-004` | CG001-C-82 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260930-CG001-QUESTIONING-DELAY-01` | `MP-CG001-QUESTIONING-DELAY-001` | CG001-C-77、CG001-C-78、CG001-C-79 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260930-CG001-QUESTIONING-DELAY-LEAN-01` | `MP-CG001-QUESTIONING-DELAY-LEAN-001` | CG001-C-80 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260930-CG001-QUESTIONING-DELAY-LEAN-MACOS-01` | `MP-CG001-QUESTIONING-DELAY-LEAN-001` | CG001-C-80 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260930-CG001-QUESTIONING-DELAY-LEAN-MACOS-NEG-01` | `MP-CG001-QUESTIONING-DELAY-LEAN-NEG-001` | CG001-C-80 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | UR |
| `20260930-CG001-QUESTIONING-DELAY-LEAN-NEG-01` | `MP-CG001-QUESTIONING-DELAY-LEAN-NEG-001` | CG001-C-80 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | UR |
| `20260930-CG001-QUESTIONING-DELAY-MACOS-01` | `MP-CG001-QUESTIONING-DELAY-001` | CG001-C-77、CG001-C-78、CG001-C-79 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260930-CG001-QUESTIONING-DELAY-MACOS-NEG-01` | `MP-CG001-QUESTIONING-DELAY-NEG-001` | CG001-C-78 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260930-CG001-QUESTIONING-DELAY-MACOS-NEG-02` | `MP-CG001-QUESTIONING-DELAY-NEG-002` | CG001-C-79 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260930-CG001-QUESTIONING-DELAY-MACOS-NEG-03` | `MP-CG001-QUESTIONING-DELAY-NEG-003` | CG001-C-79 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260930-CG001-QUESTIONING-DELAY-MACOS-NEG-04` | `MP-CG001-QUESTIONING-DELAY-NEG-004` | CG001-C-78 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260930-CG001-QUESTIONING-DELAY-NEG-01` | `MP-CG001-QUESTIONING-DELAY-NEG-001` | CG001-C-78 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260930-CG001-QUESTIONING-DELAY-NEG-02` | `MP-CG001-QUESTIONING-DELAY-NEG-002` | CG001-C-79 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260930-CG001-QUESTIONING-DELAY-NEG-03` | `MP-CG001-QUESTIONING-DELAY-NEG-003` | CG001-C-79 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260930-CG001-QUESTIONING-DELAY-NEG-04` | `MP-CG001-QUESTIONING-DELAY-NEG-004` | CG001-C-78 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260930-CG001-TRUNCATION-QUESTIONING-01` | `MP-CG001-TRUNCATION-QUESTIONING-001` | CG001-C-83 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20260930-CG001-TRUNCATION-QUESTIONING-NEG-01` | `MP-CG001-TRUNCATION-QUESTIONING-NEG-001` | CG001-C-83 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20260930-CG001-TRUNCATION-QUESTIONING-NEG-02` | `MP-CG001-TRUNCATION-QUESTIONING-NEG-002` | CG001-C-83 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
