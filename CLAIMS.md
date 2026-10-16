# 命题与证据

**中文** · [Русский](CLAIMS-RU.md) · [Deutsch](CLAIMS-DE.md) · [Français](CLAIMS-FR.md) · [English](CLAIMS-EN.md)

> 本文件由 `dev` 上的 `scripts/release/build_main_release.py` 从提交 `99865e92` 生成，不在本分支修改。第 1、2 节逐字取自 `dev` 上共享证据矩阵 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 的两节（不含原标题行）；第 3 节逐字取自 `dev` 上的目标内索引草稿与 Claude 总索引；第 4 节（ZFC 一侧）逐字取自共享证据矩阵中各包的行与 Claude 总索引；第 5 节由各运行的收据生成。文中 `formal/…`、`verification/runs/…` 指本分支 `HoTT/` 下的同名路径；其余过程文件的路径在 `dev` 上（`RELEASE-MANIFEST.json` 的 `paths_mentioned_but_on_dev` 列出了正文提到的那些）。另有俄、德、法、英文译本（AI 翻译，以本中文版为准）；`CLAIMS.md` 与 `CLAIMS-ZH.md` 相同。

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
| `MP-ZFC-HOTT-OBSERVATION-BRIDGE-001` | `C-357` | `formal/claude-cg001/observation-completion-bridge/ObservationCompletionBridge.agda`（命题全文 `CLAIM.md`；复用C-78/C-83的固定Cubical Agda依赖） | `verification/runs/20261003-CG001-ZFC-HOTT-OBSERVATION-BRIDGE-02/`；macOS Agda 2.8.0 + cubical 0.9；exit 0，stderr 0 B；由统一捕获器记录全部本地导入根和12个固定源码文件 | `KERNEL_ACCEPTED_WITH_SCOPE`：原universe Q为`never`、截断Q第一步停、且无统一section三项的联合控制；不构成ZFC模型／验收定理。 |
| `MP-ZFC-HOTT-OBSERVATION-BRIDGE-NEG-001` | `C-357`（负控制） | `formal/claude-cg001/observation-completion-bridge/WrongObservationCompletionBridge.agda` | `verification/runs/20261003-CG001-ZFC-HOTT-OBSERVATION-BRIDGE-NEG-02/`；exit 42，`Bool != A` | `NEGATIVE_CONTROL_REJECTED`：同层常值Bool不能承担每个原universe元素的统一恢复。 |
| `MP-ZFC-HOTT-COMPLETION-REFLECTION-001` | `C-358` | `formal/claude-cg001/completion-reflection-failure/CompletionReflectionFailure.agda`（命题全文 `CLAIM.md`；复用固定C-78/C-83过程） | `verification/runs/20261003-CG001-ZFC-HOTT-COMPLETION-REFLECTION-04/`；macOS Agda 2.8.0 + cubical 0.9；exit 0，stderr 0 B；统一捕获器固定6个本地导入根和11个源码文件 | `KERNEL_ACCEPTED_WITH_SCOPE`：截断Q在第一步完成，不能推出原universe Q存在有限halt witness；不构成ZFC模型／验收定理。 |
| `MP-ZFC-HOTT-COMPLETION-REFLECTION-NEG-001` | `C-358`（负控制） | `formal/claude-cg001/completion-reflection-failure/WrongCompletionReflection.agda` | `verification/runs/20261003-CG001-ZFC-HOTT-COMPLETION-REFLECTION-NEG-03/`；exit 42，`nothing != just 1` | `NEGATIVE_CONTROL_REJECTED`：伪造的原Q fuel-0 halt不由截断完成推出。 |

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
| C-357 | 固定原universe的逐层Q满足`question (Type ℓ-zero) judgeU ≡ never`；其集合截断`TU`上的同一Q满足`runFor 0 (question TU judgeTU) ≡ just 1`；并且不存在统一`g : TU → Type ℓ-zero`使所有`A`满足`g ∣A∣₂ ≡ A`。三项由`coarseCompletionCreatesNoRestoration`同一Cubical Agda命题联结。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `MP-ZFC-HOTT-OBSERVATION-BRIDGE-001` / `20261003-CG001-ZFC-HOTT-OBSERVATION-BRIDGE-02`；负控制 `MP-ZFC-HOTT-OBSERVATION-BRIDGE-NEG-001` / `-NEG-02` | 证明固定HoTT Q上的粗完成观察与无统一恢复控制；不形式化ZFC、单纯集模型、模型验收或AcceptanceContract，不说截断错误，也不证明ZFC时间观察力不完备、HoTT不一致或UR现实判词。 |
| C-358 | 定义`CompletionReflectsOriginalHalting = (runFor 0 (question TU judgeTU) ≡ just 1) → Questioning.Halts (Type ℓ-zero) judgeU`。`coarseCompletionDoesNotReflectOriginalHalting`证明其否定：截断版阶段一完成不能推出原Q有有限halt witness。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `MP-ZFC-HOTT-COMPLETION-REFLECTION-001` / `20261003-CG001-ZFC-HOTT-COMPLETION-REFLECTION-04`；负控制 `MP-ZFC-HOTT-COMPLETION-REFLECTION-NEG-001` / `-NEG-03` | 证明固定HoTT Q上的完成反射失败；不裁定两个问题是否同一任务，不形式化ZFC／模型／AcceptanceContract，也不证明ZFC时间观察力不完备、HoTT不一致或UR现实判词。 |

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

## 4. ZFC-1 一侧：缺的门 Q、两次选择与 A、芝诺与圆环、B 的两个成因、哥德尔一路

> 研究发起人 2026-10-04 放在 `main` 文首的“ZFC Failure”与 2026-10-14 的表述，逐句对照见 `docs/ZFC-1的问题-原话逐句对照与机器证明-20261015.md`。4.1 的行逐字取自 `dev` 上 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 中各包所在的节；4.2 的行逐字取自 `dev` 上的 Claude 总索引。命题全文与禁止外推以各包的 `CLAIM.md` 为准。用到 Foundation 的 𝗭𝗙𝗖 的命题，说的是 Foundation 库里形式化的 𝗭𝗙𝗖。

### 4.1 证明包与运行（逐字）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-GODEL-Q-001` | `CG001-C-84`–`CG001-C-94` | `formal/claude-cg001/godel-q/GodelQ/`：`ProcessObservation`、`EffectiveTheory`、`GodelZenoRunner`、`ProvabilityLogic`、`OmegaQuestion`、`Qualification`（按序编译；命题全文 `CLAIM.md`） | `verification/runs/20261007-CG001-GODEL-Q-01/`；exit 0，stderr 0 B；公理只有 propext、Classical.choice、Quot.sound（C-92 无公理）；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-GODEL-Q-NEG-CONSISTENCY-001` | `CG001-C-90`（负控制） | `formal/claude-cg001/godel-q/GodelQ/Negative/WrongTheoryWithoutConsistency.lean` | `verification/runs/20261007-CG001-GODEL-Q-NEG-CONSISTENCY-01/`；exit 1，`consistent` 字段的目标 `False` 无法关闭 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-GODEL-Q-NEG-EFFECTIVENESS-001` | `CG001-C-90`（负控制） | `formal/claude-cg001/godel-q/GodelQ/Negative/WrongBargainWithoutEffectiveness.lean` | `verification/runs/20261007-CG001-GODEL-Q-NEG-EFFECTIVENESS-01/`；exit 1，`re_never` 无法关闭 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-GODEL-Q-NEG-GODEL-II-001` | `CG001-C-92`（负控制） | `formal/claude-cg001/godel-q/GodelQ/Negative/WrongConsistencyProvable.lean` | `verification/runs/20261007-CG001-GODEL-Q-NEG-GODEL-II-01/`；exit 1，目标化简为 `False` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-GODEL-Q-NEG-SOUNDNESS-001` | `CG001-C-85`（负控制） | `formal/claude-cg001/godel-q/GodelQ/Negative/WrongEscapeWithoutSoundness.lean` | `verification/runs/20261007-CG001-GODEL-Q-NEG-SOUNDNESS-01/`；exit 1，`sound` 字段的目标 `¬ Done e` 无法关闭 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-GODEL-Q-ZFC-001` | `CG001-C-95`–`CG001-C-102` | `formal/claude-cg001/godel-q-zfc/GodelQ/`：CG-005 的三个模块（逐字节复制）、`FoundationArith.lean`、`ZFC/` 下 14 个模块与 `ZFC/Qualification.lean`（按序编译；命题全文 `CLAIM.md`） | `verification/runs/20261008-CG001-GODEL-Q-ZFC-01/`；exit 0，stderr 0 B，约 41 秒；85 条公理报告全为三条标准公理；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-GODEL-Q-ZFC-NEG-CONSISTENCY-001` | `CG001-C-99`（负控制） | `formal/claude-cg001/godel-q-zfc/GodelQ/Negative/WrongConsistencyWithBot.lean` | `verification/runs/20261008-CG001-GODEL-Q-ZFC-NEG-CONSISTENCY-01/`；exit 1，`Entailment.Consistent (insert ⊥ 𝗭𝗙𝗖)` 找不到 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-GODEL-Q-ZFC-NEG-DELTA1-001` | `CG001-C-97`（负控制） | `formal/claude-cg001/godel-q-zfc/GodelQ/Negative/WrongREWithoutDelta1.lean` | `verification/runs/20261008-CG001-GODEL-Q-ZFC-NEG-DELTA1-01/`；exit 1，`Theory.Δ₁ trueInUniverse` 找不到 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-GODEL-Q-ZFC-NEG-SOUNDNESS-001` | `CG001-C-100`（负控制） | `formal/claude-cg001/godel-q-zfc/GodelQ/Negative/WrongSoundnessWithoutModel.lean` | `verification/runs/20261008-CG001-GODEL-Q-ZFC-NEG-SOUNDNESS-01/`；exit 1，模型实例 `Universe↓[ℒₛₑₜ] ⊧* insert (haltsS ΦH a) 𝗭𝗙𝗖` 找不到 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-GODEL-Q-ZFC-TURING-001` | `CG001-C-104`、`CG001-C-105` | `formal/claude-cg001/godel-q-zfc-turing/GodelQ/Turing.lean`、`ZFC/TuringZFC.lean`、`ZFC/QualificationTuring.lean`（加 16 个与 `godel-q-zfc` 逐字节相同的依赖模块；命题全文 `CLAIM.md`） | `verification/runs/20261008-CG001-GODEL-Q-ZFC-TURING-01/`；exit 0，stderr 0 B；87 条公理报告只有三条标准公理；依赖检查两行通过；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-GODEL-Q-ZFC-TURING-NEG-TRUTH-001` | `CG001-C-104`（负控制） | `formal/claude-cg001/godel-q-zfc-turing/GodelQ/Negative/WrongTuringWithTruthObserver.lean` | `verification/runs/20261008-CG001-GODEL-Q-ZFC-TURING-NEG-TRUTH-01/`；exit 1，`re` 字段处被拒 | `NEGATIVE_CONTROL_REJECTED`：可靠但不可枚举的真理观察者没有漏点，“可枚举”这一前提确实被用到 |
| `MP-CG001-ZENO-DENSITY-ATTAINMENT-001` | `CG001-C-106`、`CG001-C-107`、`CG001-C-108` | `formal/claude-cg001/zeno-density-attainment/GodelQ/Zeno/Attainment.lean`、`Runners.lean`、`QualificationZeno.lean`（命题全文 `CLAIM.md`） | `verification/runs/20261008-CG001-ZENO-DENSITY-ATTAINMENT-01/`；exit 0，stderr 0 B；22 条公理报告只有三条标准公理；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-ZENO-DENSITY-ATTAINMENT-NEG-DENSE-001` | `CG001-C-106`（负控制） | `formal/claude-cg001/zeno-density-attainment/GodelQ/Negative/WrongDenseAttains.lean` | `verification/runs/20261008-CG001-ZENO-DENSITY-ATTAINMENT-NEG-DENSE-01/`；exit 1，`Isolated (1 : ℝ)` 无法证明 | `NEGATIVE_CONTROL_REJECTED`：“终点孤立”这一前提确实被用到 |
| `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-001` | `CG001-C-117`、`CG001-C-118` | `formal/claude-cg001/godel-q-zfc-runner-arrival/GodelQ/ZFC/ArrivalArith.lean`、`ArrivalZFC.lean`、`QualificationArrival.lean`（加 21 个逐字节复制的依赖模块；命题全文 `CLAIM.md`） | `verification/runs/20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-01/`；exit 0，stderr 0 B；139 条公理报告只有三条标准公理；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-001` | `CG001-C-118`（负控制） | `formal/claude-cg001/godel-q-zfc-runner-arrival/GodelQ/Negative/WrongArrivalOldPhi.lean` | `verification/runs/20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-01/`；exit 1 | `NEGATIVE_CONTROL_REJECTED`：等价依赖到达句与停机公式来自同一个 `stopF` |
| `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-002` | `CG001-C-118`（负控制） | `formal/claude-cg001/godel-q-zfc-runner-arrival/GodelQ/Negative/WrongHaltingRunnerArrives.lean` | `verification/runs/20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-02/`；exit 1 | `NEGATIVE_CONTROL_REJECTED`：到达句区分停与不停 |
| `MP-CG001-IDEA-T-C6-P-001` | `CG001-C-114`、`CG001-C-115`、`CG001-C-116` | `formal/claude-cg001/idea-t-c6-p/GodelQ/IdeaT.lean`、`C6Review.lean`、`PTwoSides.lean`、`QualificationW7.lean`（加 20 个逐字节复制的依赖模块；命题全文 `CLAIM.md`） | `verification/runs/20261009-CG001-IDEA-T-C6-P-01/`；exit 0，stderr 0 B；144 条公理报告只有三条标准公理；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-IDEA-T-C6-P-NEG-001` | `CG001-C-114`（负控制） | `formal/claude-cg001/idea-t-c6-p/GodelQ/Negative/WrongLimitDecoder.lean` | `verification/runs/20261009-CG001-IDEA-T-C6-P-NEG-01/`；exit 1 | `NEGATIVE_CONTROL_REJECTED`：接口上的碰撞确实被用到 |
| `MP-CG001-IDEA-T-C6-P-NEG-002` | `CG001-C-115`（负控制） | `formal/claude-cg001/idea-t-c6-p/GodelQ/Negative/WrongCompleteReview.lean` | `verification/runs/20261009-CG001-IDEA-T-C6-P-NEG-02/`；exit 1 | `NEGATIVE_CONTROL_REJECTED`：有效性确实被用到 |
| `MP-CG001-IDEA-T-C6-P-NEG-003` | `CG001-C-116`（负控制） | `formal/claude-cg001/idea-t-c6-p/GodelQ/Negative/WrongRealP1.lean` | `verification/runs/20261009-CG001-IDEA-T-C6-P-NEG-03/`；exit 1 | `NEGATIVE_CONTROL_REJECTED`：语义 P₁ 的成立确实依赖量子化 |
| `MP-CG001-SAME-Q-UNIVALENT-001` | `CG001-C-112`、`CG001-C-113` | `formal/claude-cg001/same-q-univalent/SameQ.agda`（导入 `pedometer-semantics`、`questioning-delay`、`truncation-questioning`、`product-questioning`、`universe-questioning`；命题全文 `CLAIM.md`） | `verification/runs/20261009-CG001-SAME-Q-UNIVALENT-01/`；exit 0；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-SAME-Q-UNIVALENT-NEG-001` | `CG001-C-113`（负控制） | `formal/claude-cg001/same-q-univalent/WrongH0Settles.agda` | `verification/runs/20261009-CG001-SAME-Q-UNIVALENT-NEG-01/`；exit 42，`nothing != just 1` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-SAME-Q-UNIVALENT-NEG-002` | `CG001-C-113`（负控制） | `formal/claude-cg001/same-q-univalent/WrongTruncUnsettled.agda` | `verification/runs/20261009-CG001-SAME-Q-UNIVALENT-NEG-02/`；exit 42，`true != false` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-SAME-Q-UNIVALENT-NEG-003` | `CG001-C-112`（负控制） | `formal/claude-cg001/same-q-univalent/WrongRunnerWithoutMonotone.agda` | `verification/runs/20261009-CG001-SAME-Q-UNIVALENT-NEG-03/`；exit 42，`alt k != not (alt k)` | `NEGATIVE_CONTROL_REJECTED`：单调前提确实被用到 |
| `MP-CG001-GODEL-Q-ZFC-Z0-SIGMA1-001` | `CG001-C-413`–`CG001-C-417` | `formal/claude-cg001/godel-q-zfc-z0-sigma1/GodelQ/ZFC/`：`SetNum.lean`、`SetNumArith.lean`（数字层）、`TransTyped.lean`、`TransTerm.lean`（`term_ve`）、`TransBall.lean`（`ball_merge`）、`TransSigma1.lean`（`tr_sigma1_complete`）、`Z0D3.lean`（`zfcTr_D3`、`zfc_z0_unconditional`） | `verification/runs/20261014-CG001-GODEL-Q-ZFC-Z0-SIGMA1-01/`；exit 0，stderr 0 B，110 秒；138 条公理报告只有三条标准公理；`--rerun` `PASS_WITH_SCOPE` / `EXACT_EXIT_STDOUT_STDERR_MATCH` | `KERNEL_ACCEPTED_WITH_SCOPE` |
| `MP-CG001-GODEL-Q-ZFC-Z0-SIGMA1-NEG-BALL-001` | `CG001-C-415`（负控制） | 同目录 `GodelQ/Negative/BallMergeOffByOne.lean` | `verification/runs/20261014-CG001-GODEL-Q-ZFC-Z0-SIGMA1-NEG-BALL-01/`；exit 1，`key b le_rfl` 给出关于 N_b 的结论，与要求的 N_{b+1} 不符 | `NEGATIVE_CONTROL_REJECTED`：合并的界由前提逐一支撑 |
| `MP-CG001-HALTING-WITHOUT-LEM-001` | `CG001-C-422` | `formal/claude-cg001/halting-without-lem/GodelQ/Diagonal/`：`Core.lean`（只用 Lean 内核：`no_liar`、`no_never_recognizer`、`no_decider`、`recognizer_without_flip`）、`MathlibCodes.lean`（`code_flip`、`turing_codes`）、`QualificationDiag.lean`（命题对照与公理审计） | `verification/runs/20261014-CG001-HALTING-WITHOUT-LEM-01/`；exit 0，stderr 0 B；`qual_C422` 不依赖任何公理；审计 5 条“不依赖”、4 条对照“依赖”全部通过；`--rerun` `PASS_WITH_SCOPE` / `EXACT_EXIT_STDOUT_STDERR_MATCH` | `KERNEL_ACCEPTED_WITH_SCOPE` |
| `MP-CG001-HALTING-WITHOUT-LEM-NEG-001` | `CG001-C-422`（负控制） | 同目录 `GodelQ/Negative/WrongRecognizerWithoutFlip.lean` | `verification/runs/20261014-CG001-HALTING-WITHOUT-LEM-NEG-FLIP-01/`；exit 1，`hd d d` 是 `True ↔ ¬False`，不是 `P ↔ ¬P` | `NEGATIVE_CONTROL_REJECTED`：翻转程序是用到的前提 |
| `MP-CG001-TWO-CHOICES-LPO-001` | `CG001-C-418`–`CG001-C-421` | `formal/claude-cg001/two-choices-lpo/GodelQ/TwoChoices/`：`Core.lean`（只用 Lean 内核：`limBit_iff_lpo`、`natBMC_iff_lpo`、`unbounded_settling_false`、芝诺读数）、`Machines.lean`（`no_computable_settling_point`、`no_computable_final_value`、`lpo_classical`、`computability_differs`）、`Rational.lean`（`zenoReading_eq_floor`、`zenoQ_cauchy`）、`QualificationTC.lean`（命题对照与公理审计） | `verification/runs/20261014-CG001-TWO-CHOICES-LPO-01/`；exit 0，stderr 0 B，8 秒；`qual_C418`、`qual_C419` 只用 `propext`、`Quot.sound`；审计 12 条“不依赖 `Classical.choice`”、5 条对照“依赖”全部通过；`--rerun` `PASS_WITH_SCOPE` / `EXACT_EXIT_STDOUT_STDERR_MATCH` | `KERNEL_ACCEPTED_WITH_SCOPE` |
| `MP-CG001-TWO-CHOICES-LPO-NEG-001` | `CG001-C-418`（负控制） | 同目录 `GodelQ/Negative/WrongLPOForFree.lean` | `verification/runs/20261014-CG001-TWO-CHOICES-LPO-NEG-FREE-01/`；exit 1，审计报出 `lpo_for_free` 依赖 `Classical.choice` | `NEGATIVE_CONTROL_REJECTED`：审计不是空的 |
| `MP-CG001-TWO-CHOICES-LPO-NEG-003` | `CG001-C-420`（负控制） | 同目录 `GodelQ/Negative/WrongComputableSettling.lean` | `verification/runs/20261014-CG001-TWO-CHOICES-LPO-NEG-SETTLING-01/`；exit 1，`DoneBy e m ↔ DoneBy e 0` 未解 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-TWO-CHOICES-LPO-NEG-002` | `CG001-C-418`（负控制） | 同目录 `GodelQ/Negative/WrongSettlingUnbounded.lean` | `verification/runs/20261014-CG001-TWO-CHOICES-LPO-NEG-UNBOUNDED-01/`；exit 1，`omega` 证不出上界 | `NEGATIVE_CONTROL_REJECTED`：“有界”是用到的前提 |
| `MP-CG001-A-UNIVALENCE-B-001` | `CG001-C-430` | `formal/claude-cg001/a-univalence-b/AUnivalenceB.agda`（`UnivalentCollection.localGlobal`、`noFiniteLevel`、`neverWithBoth`、`boundedSettles`、`haltsWithBound`、`factStopsAtOne`、`neverNeedsUnbounded`、`neverNeedsStructure`、`universeNever`、`gatheringUnivalent`、`numberedNotUnivalent`、`pairedNever`、`qual-C430`；导入 `questioning-delay`、`pedometer-semantics`、`universe-questioning`） | `verification/runs/20261015-CG001-A-UNIVALENCE-B-01/`（macOS 工具链记录 `formal/dedekind-omega-missile/TOOLCHAIN.json`）；exit 0，stderr 0 B；`--rerun` `PASS_WITH_SCOPE` / `EXACT_EXIT_STDOUT_STDERR_MATCH` | `KERNEL_ACCEPTED_WITH_SCOPE` |
| `MP-CG001-A-UNIVALENCE-B-NEG-001` | `CG001-C-430`（负控制） | 同目录 `WrongFactNever.agda` | `verification/runs/20261015-CG001-A-UNIVALENCE-B-NEG-01/`；exit 42，`just 1 != nothing` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-A-UNIVALENCE-B-NEG-002` | `CG001-C-430`（负控制） | 同目录 `WrongBoundedNever.agda` | `verification/runs/20261015-CG001-A-UNIVALENCE-B-NEG-02/`；exit 42，`just 2 != nothing` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-A-UNIVALENCE-B-NEG-003` | `CG001-C-430`（负控制） | 同目录 `WrongBWithoutUnivalence.agda` | `verification/runs/20261015-CG001-A-UNIVALENCE-B-NEG-03/`；exit 42，恒等等价不是单价性要的映射 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-CIRCLE-PARADOX-001` | `CG001-C-424` | `formal/claude-cg001/circle-paradox/GodelQ/Circle/CircleParadox.lean`（`one_step`、`farEnd_arrives`、`closing_never_attains`、`θ_eq_zenoSeq`、`range_bend_ne`、`range_bend_one`、`gap_infinite`、`zero_not_isolated`、`discrete_closing_attains`、`discreteGap_reaches_one`）、`QualificationCircle.lean` | `verification/runs/20261015-CG001-CIRCLE-PARADOX-01/`；exit 0，stderr 0 B；20 条公理报告只有三条标准公理；`--rerun` `PASS_WITH_SCOPE` / `EXACT_EXIT_STDOUT_STDERR_MATCH` | `KERNEL_ACCEPTED_WITH_SCOPE` |
| `MP-CG001-CIRCLE-PARADOX-NEG-001` | `CG001-C-424`（负控制） | 同目录 `GodelQ/Negative/WrongFiniteClosing.lean` | `verification/runs/20261015-CG001-CIRCLE-PARADOX-NEG-CLOSE-01/`；exit 1，`↑1 − ↑2⁻¹ = 0` 未解 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-RUNNER-ARRIVAL-RATIONAL-001` | `CG001-C-428` | `formal/claude-cg001/runner-arrival-rational/GodelQ/ZFC/ArrivalRational.lean`（`arrRat_iff_arr`、`zfc_arrRat_iff_arr`、`zfc_arrRat_iff_never`、`universe_arrRatS_iff`、`zfc_runner_rat`、`zfc_arriveRatC`、`arrRat_encode_rat`、`arriveRatC_nat`）、`QualificationArrivalRational.lean`；23 个模块逐字节复制自 `godel-q-zfc-runner-arrival` | `verification/runs/20261015-CG001-RUNNER-ARRIVAL-RATIONAL-01/`；exit 0，stderr 0 B；144 条公理报告只有三条标准公理；`--rerun` `PASS_WITH_SCOPE` / `EXACT_EXIT_STDOUT_STDERR_MATCH` | `KERNEL_ACCEPTED_WITH_SCOPE` |
| `MP-CG001-RUNNER-ARRIVAL-RATIONAL-NEG-001` | `CG001-C-428`（负控制） | 同目录 `GodelQ/Negative/WrongRationalStepZero.lean` | `verification/runs/20261015-CG001-RUNNER-ARRIVAL-RATIONAL-NEG-STEP-01/`；exit 1，需要 `q ≤ n`，只有 `0 ≤ n` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-TERMINATION-GATE-001` | `CG001-C-431` | `formal/claude-cg001/termination-gate/GodelQ/Gate/Core.lean`、`QualificationGate.lean`（`ungated_proves_false`、`ungated_proves_anything`、`ungated_data_empty`、`gated_has_solution`、`qual_C431`） | `verification/runs/20261015-CG001-TERMINATION-GATE-01/`；exit 0，stderr 0 B；审计公理清单为空；`--rerun` `PASS_WITH_SCOPE` / `EXACT_EXIT_STDOUT_STDERR_MATCH` | `KERNEL_ACCEPTED_WITH_SCOPE` |
| `MP-CG001-TERMINATION-GATE-NEG-001` | `CG001-C-431`（负控制） | 同目录 `GodelQ/Negative/WrongLoop.lean` | `verification/runs/20261015-CG001-TERMINATION-GATE-NEG-01/`；exit 1，`fail to show termination` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-TWO-CHOICES-CUBICAL-001` | `CG001-C-426` | `formal/claude-cg001/two-choices-cubical/TwoChoicesCubical.agda`（`limBit↔LPO`、`noSettlingWithoutMonotone`、`UniverseAnswers.allNo`、`UniverseAnswers.settlesAtZero`、`Stage.stopsAtStage`、`stageJudge`、`universeRun100`、`setsGatheringRun`、`fourTypesGatheringRun`、`qual-C426`；导入 `same-q-univalent`、`questioning-delay`、`universe-questioning` 等） | `verification/runs/20261015-CG001-TWO-CHOICES-CUBICAL-01/`（macOS 工具链记录 `formal/dedekind-omega-missile/TOOLCHAIN.json`）；exit 0，stderr 0 B；`--rerun` `PASS_WITH_SCOPE` / `EXACT_EXIT_STDOUT_STDERR_MATCH` | `KERNEL_ACCEPTED_WITH_SCOPE` |
| `MP-CG001-TWO-CHOICES-CUBICAL-NEG-001` | `CG001-C-426`（负控制） | 同目录 `WrongUniverseSettles.agda` | `verification/runs/20261015-CG001-TWO-CHOICES-CUBICAL-NEG-01/`；exit 42，`false != true` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-TWO-CHOICES-CUBICAL-NEG-002` | `CG001-C-426`（负控制） | 同目录 `WrongSetsGatheringEarly.agda` | `verification/runs/20261015-CG001-TWO-CHOICES-CUBICAL-NEG-02/`；exit 42，`nothing != just 1` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-TWO-CHOICES-CUBICAL-NEG-003` | `CG001-C-426`（负控制） | 同目录 `WrongAltSettles.agda` | `verification/runs/20261015-CG001-TWO-CHOICES-CUBICAL-NEG-03/`；exit 42，`false != true` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-TWO-CHOICES-RATIONAL-001` | `CG001-C-425` | `formal/claude-cg001/two-choices-rational/GodelQ/TwoChoices/RationalConstructive.lean`（`bmcQ_of_lpo`、`limBit_of_bmcQ`、`bmcQ_iff_lpo`、`flr_mono`、`close_of_flr_eq`、`zenoQp_cauchy`、`zenoQp_to_one`、`zeno_modulus_zero_false`）、`QualificationRational.lean`；`Core.lean` 逐字节复制自 `two-choices-lpo` | `verification/runs/20261015-CG001-TWO-CHOICES-RATIONAL-01/`；exit 0，stderr 0 B；审计 15 个常量不依赖 `Classical.choice`（实际公理 `propext`、`Quot.sound`），2 个对照依赖；`--rerun` `PASS_WITH_SCOPE` / `EXACT_EXIT_STDOUT_STDERR_MATCH` | `KERNEL_ACCEPTED_WITH_SCOPE` |
| `MP-CG001-TWO-CHOICES-RATIONAL-NEG-001` | `CG001-C-425`（负控制） | 同目录 `GodelQ/Negative/WrongBMCQForFree.lean` | `verification/runs/20261015-CG001-TWO-CHOICES-RATIONAL-NEG-FREE-01/`；exit 1，审计报出依赖 `Classical.choice` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-TWO-CHOICES-RATIONAL-NEG-002` | `CG001-C-425`（负控制） | 同目录 `GodelQ/Negative/WrongZenoModulus.lean` | `verification/runs/20261015-CG001-TWO-CHOICES-RATIONAL-NEG-MODULUS-01/`；exit 1，`omega` 证不出 `k + 1 ≤ m` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-Z0-OMEGA-QUESTION-001` | `CG001-C-427` | `formal/claude-cg001/z0-omega-question/GodelQ/ZFC/Z0OmegaQuestion.lean`（`exists_z0_code`、`z0Code_done_iff`、`z0Q_never`、`zfc_confirms_every_stage`、`consistent_true_iff_z0_never`、`z0_runner_arrives`）、`QualificationZ0Omega.lean`；32 个模块逐字节复制自 `godel-q-zfc-z0-sigma1`，`OmegaQuestion.lean` 逐字节复制自 `godel-q` | `verification/runs/20261015-CG001-Z0-OMEGA-QUESTION-01/`；exit 0，stderr 0 B；150 条公理报告只有三条标准公理；`--rerun` `PASS_WITH_SCOPE` / `EXACT_EXIT_STDOUT_STDERR_MATCH` | `KERNEL_ACCEPTED_WITH_SCOPE` |
| `MP-CG001-Z0-OMEGA-QUESTION-NEG-001` | `CG001-C-427`（负控制） | 同目录 `GodelQ/Negative/WrongStagesMakeNever.lean` | `verification/runs/20261015-CG001-Z0-OMEGA-QUESTION-NEG-STAGES-01/`；exit 1，类型不符 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-ZENO-ZFC-CLASSICAL-001` | `CG001-C-423` | `formal/claude-cg001/zeno-zfc-classical/GodelQ/Zeno/`：`ZenoClassicalZFC.lean`（`models_arriveC`、`models_noFiniteC`、`zfc_arriveC`、`zfc_noFiniteC`、`zfc_not_finiteArrival`）、`ZenoReading.lean`（实数读法）、`QualificationZenoZFC.lean` | `verification/runs/20261015-CG001-ZENO-ZFC-CLASSICAL-01/`；exit 0，stderr 0 B，56 秒；92 条公理报告只有三条标准公理；`--rerun` `PASS_WITH_SCOPE` / `EXACT_EXIT_STDOUT_STDERR_MATCH` | `KERNEL_ACCEPTED_WITH_SCOPE` |
| `MP-CG001-ZENO-ZFC-CLASSICAL-NEG-001` | `CG001-C-423`（负控制） | 同目录 `GodelQ/Negative/WrongFiniteArrival.lean` | `verification/runs/20261015-CG001-ZENO-ZFC-CLASSICAL-NEG-FINITE-01/`；exit 1，`K = 0` 未解 | `NEGATIVE_CONTROL_REJECTED` |

### 4.2 命题一句话（逐字）

| 命题 | 一句话 | 包 |
|---|---|---|
| `CG001-C-84` | 过程完成恰是某一有限阶段完成；阶段观察单调且可计算 | godel-q |
| `CG001-C-85` | Kleene–罗素对角：任一可枚举接受集有 d 使“d 停机 ⟺ 被接受”（由 Kleene 第二递归定理构造）；任一可枚举可靠的永不完成观察者漏掉一个真的永不完成者 | godel-q |
| `CG001-C-86` | 可枚举、可靠、完备不可兼得；“永不完成”不可枚举（两条独立证明） | godel-q |
| `CG001-C-87` | 补丁塔：严格更大的可靠观察者仍有漏点 | godel-q |
| `CG001-C-88` | 有效理论：一致 + Σ1 完全 ⟹ Π1 可靠；每次完成、每个有限时刻都被证明（Q 不是没有） | godel-q |
| `CG001-C-89` | 哥德尔第一不完备的过程形式：有一个确实永不停的过程，理论每一刻都确认“尚未”，却证明不了“永不”（Q 不完备） | godel-q |
| `CG001-C-90` | 魔鬼交易：ω 完成规则 P 与“有效 + 一致 + Σ1/Δ0 完全”不可兼得；P 要么不可计算，要么导致矛盾 | godel-q |
| `CG001-C-91` | 哥德尔–芝诺跑者：每一刻都没到、极限存在、到达 ⟺ d 永不停；可枚举可靠的到达接受者确认不了某个确实到达的跑者；圆环读法同一；经典芝诺可确认 | godel-q |
| `CG001-C-92` | HBL 前提下 Löb、哥德尔 II、自用 P 的崩塌、ZFC-1 严格更强；一致模型 | godel-q |
| `CG001-C-93` | 同一个 ω 追问：芝诺、H0（参数）、Z0、跑者；P_fin 被否定；可观察性分界 | godel-q |
| `CG001-C-94` | ZFC + A = ZFC + P：A_general ⟺ Q 完备；P ⟹ A_general；有效理论没有 A_general；具有 A_general 的理论要么不可枚举要么不一致 | godel-q |
| `CG001-C-95` | Foundation 的 `𝗭𝗙𝗖` 有 Δ1 公理表示：分离、替换模式各有 Δ1 识别，`𝗕𝗦𝗧` 有限，`𝗔𝗖` 单句 | godel-q-zfc |
| `CG001-C-96` | Rayo 数字公式的编码是内部原始递归（Σ1）且等于真实编码；𝗭 的每个模型中 `Num_n(z) ↔ z = ofNat n` | godel-q-zfc |
| `CG001-C-97` | 对任意 Φ，𝗭𝗙𝗖 证明的 `¬∃z (Num_n(z) ∧ Φ(z))` 可枚举 | godel-q-zfc |
| `CG001-C-98` | `𝗭𝗙𝗖 ⊳ 𝗥₀`；真实 r.e. 事实的数字句被 𝗭𝗙𝗖 证明（不用可靠性） | godel-q-zfc |
| `CG001-C-99` | 真实 𝗭𝗙𝗖 是 EffectiveTheory；哥德尔 I 过程形式；魔鬼交易 | godel-q-zfc |
| `CG001-C-100` | 数字句 Σ1 可靠（`Universe` 中 ω ≅ ℕ）；`provesHalts ↔ Done`；对角过程两句都独立；`Entailment.Incomplete 𝗭𝗙𝗖` | godel-q-zfc |
| `CG001-C-101` | 跑者与 𝗭𝗙𝗖 + A = 𝗭𝗙𝗖 + P 落在 𝗭𝗙𝗖 上（以到达句的可证等价为参数，参数可满足） | godel-q-zfc |
| `CG001-C-102` | S1：Δ1、扩张 𝗥₀、Σ1 可靠的算术理论上的过程形式与魔鬼交易；Foundation `incomplete_of_halting_problem` 交叉核对 | godel-q-zfc |
| `CG001-C-104` | 图灵路线（抽象层）：可靠、可枚举的永不完成观察者与有效理论，漏掉的“永不完成”不可枚举且无穷，有限补丁补不完；有效理论的 Q 不完备，证明不经过对角点 | godel-q-zfc-turing |
| `CG001-C-105` | 图灵路线落在真实 𝗭𝗙𝗖 上：漏点恰是“永不停机”句独立于 𝗭𝗙𝗖 的过程，不可枚举且无穷；𝗭𝗙𝗖 对每个漏点的每个有限时刻证明“尚未停机”；𝗭𝗙𝗖 不完全；不对 𝗭𝗙𝗖 做自指（依赖检查） | godel-q-zfc-turing |
| `CG001-C-106` | 归因：第一可数空间中“极限到达必在有限阶段取到” ⟺ 终点孤立；ℝ 每点有芝诺式过程；格点上贴近即取到；离散空间同样 | zeno-density-attainment |
| `CG001-C-107` | 量子化半步跑者（每个粒度）的闭式，第 m+1 步完成，前 m+1 步与稠密跑者相同；极限接口判不了“取到”；完成在稠密化的极限里丢失 | zeno-density-attainment |
| `CG001-C-108` | 时间一侧：稠密时间有超任务，连续端点 t = 1 取到 1 却不是任何阶段；量子化时间里严格递增的阶段时刻无上界 | zeno-density-attainment |
| `CG001-C-112` | 同一个 ω 追问的图式（Cubical Agda）：永不落定 ⟺ 搜索 ≡ never；P_fin 被否定；单调追问的减半跑者到达 ⟺ 永不落定（单调前提不可去）；判定器追问即搜索 | same-q-univalent |
| `CG001-C-113` | 实例同在一个单价内核：芝诺；H0（原生，经 C-78，内核燃料 100 实跑）；截断宇宙对照（第 1 阶段停，跑者不到达）；Z0 为参数 | same-q-univalent |
| `CG001-C-114` | 想法 T 的形式化（AI 提案）：接口压平维度 ⟹ 无可靠完备观察者；维度不可枚举 ⟹ 每个可靠可枚举观察者漏点不可枚举、无穷，可严格加细而仍漏；脚手架：可靠完备可枚举观察者存在 ⟺ 纤维恒定且可枚举；两种形式不同；实例 𝗭𝗙𝗖、芝诺极限接口 | idea-t-c6-p |
| `CG001-C-115` | C6（定义是 AI 提案）：有效的审查都不完备；𝗭𝗙𝗖 留下标准解确实出错、它却证不了充分也证不了不充分的跑者；对任一可靠使用的 ℒₛₑₜ 公式，未被批判的错误无穷且列不全 | idea-t-c6-p |
| `CG001-C-116` | P 的两侧：统一接受形式完成并宣称原完成被一个稠密实例否定（反现实）；统一接受恰为形式完成不可枚举（不可计算）；ℝ 每点语义 P₁ 不成立、格点成立；A ⟺ ω 规则 P ⟺ 无桥完成代换；有效理论没有 A，真值理论有而不可枚举 | idea-t-c6-p |
| `CG001-C-117` | 到达句的算术层：Σ1 代码公式 θ；`stopF` 在每个 𝗣𝗔⁻ 模型里单调；𝗣𝗔⁻ 模型里 `arrF e ↔ ¬ haltsF e`；剩余距离 ≤ 2⁻ᴷ 恰是前 K 步都还没停；ℕ 里 `arrF ⌜d⌝` 逐字是 ε–N 写法，恰是跑者到达 | godel-q-zfc-runner-arrival |
| `CG001-C-118` | 𝗭𝗙𝗖 逐个证明到达句 `arrS a`（不是 `neverS`）与永不停机句 `neverS ΦS a` 等价；`arrS` 在 `Universe` 里恰是到达；C-101 的跑者部分不再带参数；C-115 改用到达句后，未被批判的错误仍无穷且列不全 | godel-q-zfc-runner-arrival |
| `CG001-C-413` | 𝗭 的每个模型 V 里，对任意（可以非标准的）a、b，数字公式 N_a 存在、属于 ω、唯一、相合，并与加法、乘法、序双向相容（`numF_*`） | godel-q-zfc-z0-sigma1 |
| `CG001-C-414` | 标准算术项的翻译：在数字假设下，`Z V` 证明项值存在于 ω 中，且满足变量等式者就是该项值的数字（`term_ve`） | godel-q-zfc-z0-sigma1 |
| `CG001-C-415` | 有界量词合并：对每个 i < b 证得 ∀x(N_i(x) → Φ(x))，就证得 ∀z∀x(N_b(z) → x ∈ z → Φ(x))（`ball_merge`） | godel-q-zfc-z0-sigma1 |
| `CG001-C-416` | 经翻译的形式化 Σ1 完全性：V 中为真的 Σ1 句，它的翻译在 `Z V` 中可证（`tr_sigma1_complete`） | godel-q-zfc-z0-sigma1 |
| `CG001-C-417` | 第三可推导性条件 `zfcTr_D3`；完整 Z0：`𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ`，不带未证前提（Con(𝗭𝗙𝗖) 由 Lean 元层的 `Universe` 模型提供） | godel-q-zfc-z0-sigma1 |
| `CG001-C-418` | 两次选择是同一条原则：`LimBit ↔ LPO`、`NatBMC ↔ LPO`，不依赖 `Classical.choice`；去掉“有界”，落定原则不成立 | two-choices-lpo |
| `CG001-C-419` | 芝诺读数在精度 2⁻ᵏ 上于第 k 步落定，由公式给出、不是搜索：芝诺的极限数用不着 A | two-choices-lpo |
| `CG001-C-420` | A 的结果机器交不出：停机搜索的开关在经典逻辑里都有落定的一步，却没有可计算的 F 交出落定的一步，也没有可计算的 f 交出终值 | two-choices-lpo |
| `CG001-C-421` | 经典逻辑不拿可计算性当门槛：LPO 由排中律得到；每个“会停”的陈述都有现成真假；停机集与偶数集同样是集合，一个不可判定、一个可判定 | two-choices-lpo |
| `CG001-C-422` | 判不全不靠排中律：¬(P ↔ ¬P)；有翻转程序的编程系统里，没有程序恰好认出“永不停机”，也没有完全的停机判定器；构造一侧不依赖任何公理 | halting-without-lem |
| `CG001-C-423` | 经典芝诺两句落到 Foundation 的 𝗭𝗙𝗖：𝗭𝗙𝗖 证明“极限意义上到达”与“没有哪一步余量为零”的翻译，证不出“有一步余量为零” | zeno-zfc-classical |
| `CG001-C-424` | 圆环悖论逐句形式化（Mathlib 拓扑）：拆开是一步同胚；合回的远端是芝诺跑者，任何有限阶段形态都不是 M，缺口含无穷多点、长度大于 0，只在极限那一刻是 M；拿走的点不孤立；离散环有限步合上 | circle-paradox |
| `CG001-C-425` | 两次选择的有理数形态：自写有理数上 `BMCQ ↔ LPO`、`BMCQ ↔ LimBit`，不依赖 `Classical.choice`；芝诺的柯西步由公式 k + 1 给出 | two-choices-rational |
| `CG001-C-426` | 两次选择在 HoTT 内核里也是同一条原则（Cubical Agda `--safe`，`LimBit ↔ LPO`）；同一检查单元里 B 成立而不假定 LPO：宇宙上的追问 ≡ never | two-choices-cubical |
| `CG001-C-427` | Z0 是 Lean 里具体的 ω 追问：完成 ⟺ 𝗭𝗙𝗖 ⊢ ⊥；永不落定；对每个 k，𝗭𝗙𝗖 证明“到第 k 步还没找到矛盾”，却证不出一致性句的翻译 | z0-omega-question |
| `CG001-C-428` | 有理精度的 ε–N 到达句：𝗭𝗙𝗖 逐个证明它与 2⁻ᴷ 写法、与永不停机句等价；有到达的跑者，𝗭𝗙𝗖 证不出它的有理精度到达句；𝗭𝗙𝗖 证明经典芝诺的有理精度极限句 | runner-arrival-rational |
| `CG001-C-430` | B 的两个成因（合并 `main` 第 4 节已有的消融）：对任意收集，单价且所有高度一次交出 ⟹ 追问 ≡ never；高度有上限 ⟹ 停；编码的相同是事实 ⟹ 第 1 问停；四个见证 | a-univalence-b |
| `CG001-C-431` | 终止检查是这道门：不设门的定义原则 `∀ α, (α → α) → α` 推出 `False` 与一切命题；良基递归的定义方程有解；不依赖任何公理 | termination-gate |

## 5. 运行清单

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
| `20261003-CG001-ZFC-HOTT-COMPLETION-REFLECTION-04` | `MP-ZFC-HOTT-COMPLETION-REFLECTION-001` | C-358 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20261003-CG001-ZFC-HOTT-COMPLETION-REFLECTION-NEG-03` | `MP-ZFC-HOTT-COMPLETION-REFLECTION-NEG-001` | C-358 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20261003-CG001-ZFC-HOTT-OBSERVATION-BRIDGE-02` | `MP-ZFC-HOTT-OBSERVATION-BRIDGE-001` | C-357 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR |
| `20261003-CG001-ZFC-HOTT-OBSERVATION-BRIDGE-NEG-02` | `MP-ZFC-HOTT-OBSERVATION-BRIDGE-NEG-001` | C-357 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR |
| `20261007-CG001-GODEL-Q-01` | `MP-CG001-GODEL-Q-001` | CG001-C-84、CG001-C-85、CG001-C-86、CG001-C-87、CG001-C-88、CG001-C-89、CG001-C-90、CG001-C-91、CG001-C-92、CG001-C-93、CG001-C-94 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261007-CG001-GODEL-Q-NEG-CONSISTENCY-01` | `MP-CG001-GODEL-Q-NEG-CONSISTENCY-001` | CG001-C-90 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261007-CG001-GODEL-Q-NEG-EFFECTIVENESS-01` | `MP-CG001-GODEL-Q-NEG-EFFECTIVENESS-001` | CG001-C-90 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261007-CG001-GODEL-Q-NEG-GODEL-II-01` | `MP-CG001-GODEL-Q-NEG-GODEL-II-001` | CG001-C-92 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261007-CG001-GODEL-Q-NEG-SOUNDNESS-01` | `MP-CG001-GODEL-Q-NEG-SOUNDNESS-001` | CG001-C-85 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261008-CG001-GODEL-Q-ZFC-01` | `MP-CG001-GODEL-Q-ZFC-001` | CG001-C-95、CG001-C-96、CG001-C-97、CG001-C-98、CG001-C-99、CG001-C-100、CG001-C-101、CG001-C-102 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261008-CG001-GODEL-Q-ZFC-NEG-CONSISTENCY-01` | `MP-CG001-GODEL-Q-ZFC-NEG-CONSISTENCY-001` | CG001-C-95、CG001-C-96、CG001-C-97、CG001-C-98、CG001-C-99、CG001-C-100、CG001-C-101、CG001-C-102 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261008-CG001-GODEL-Q-ZFC-NEG-DELTA1-01` | `MP-CG001-GODEL-Q-ZFC-NEG-DELTA1-001` | CG001-C-95、CG001-C-96、CG001-C-97、CG001-C-98、CG001-C-99、CG001-C-100、CG001-C-101、CG001-C-102 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261008-CG001-GODEL-Q-ZFC-NEG-SOUNDNESS-01` | `MP-CG001-GODEL-Q-ZFC-NEG-SOUNDNESS-001` | CG001-C-95、CG001-C-96、CG001-C-97、CG001-C-98、CG001-C-99、CG001-C-100、CG001-C-101、CG001-C-102 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261008-CG001-GODEL-Q-ZFC-TURING-01` | `MP-CG001-GODEL-Q-ZFC-TURING-001` | CG001-C-104、CG001-C-105 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261008-CG001-GODEL-Q-ZFC-TURING-NEG-TRUTH-01` | `MP-CG001-GODEL-Q-ZFC-TURING-NEG-TRUTH-001` | CG001-C-104 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261008-CG001-ZENO-DENSITY-ATTAINMENT-01` | `MP-CG001-ZENO-DENSITY-ATTAINMENT-001` | CG001-C-106、CG001-C-107、CG001-C-108 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261008-CG001-ZENO-DENSITY-ATTAINMENT-NEG-DENSE-01` | `MP-CG001-ZENO-DENSITY-ATTAINMENT-NEG-DENSE-001` | CG001-C-106 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-01` | `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-001` | CG001-C-117、CG001-C-118 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-01` | `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-001` | CG001-C-118 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-02` | `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-002` | CG001-C-118 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261009-CG001-IDEA-T-C6-P-01` | `MP-CG001-IDEA-T-C6-P-001` | CG001-C-114、CG001-C-115、CG001-C-116 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261009-CG001-IDEA-T-C6-P-NEG-01` | `MP-CG001-IDEA-T-C6-P-NEG-001` | CG001-C-114 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261009-CG001-IDEA-T-C6-P-NEG-02` | `MP-CG001-IDEA-T-C6-P-NEG-002` | CG001-C-115 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261009-CG001-IDEA-T-C6-P-NEG-03` | `MP-CG001-IDEA-T-C6-P-NEG-003` | CG001-C-116 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261009-CG001-SAME-Q-UNIVALENT-01` | `MP-CG001-SAME-Q-UNIVALENT-001` | CG001-C-112、CG001-C-113 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261009-CG001-SAME-Q-UNIVALENT-NEG-01` | `MP-CG001-SAME-Q-UNIVALENT-NEG-001` | CG001-C-113 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | ZFC1 |
| `20261009-CG001-SAME-Q-UNIVALENT-NEG-02` | `MP-CG001-SAME-Q-UNIVALENT-NEG-002` | CG001-C-113 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | ZFC1 |
| `20261009-CG001-SAME-Q-UNIVALENT-NEG-03` | `MP-CG001-SAME-Q-UNIVALENT-NEG-003` | CG001-C-112 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | ZFC1 |
| `20261014-CG001-GODEL-Q-ZFC-Z0-SIGMA1-01` | `MP-CG001-GODEL-Q-ZFC-Z0-SIGMA1-001` | CG001-C-413、CG001-C-414、CG001-C-415、CG001-C-416、CG001-C-417 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261014-CG001-GODEL-Q-ZFC-Z0-SIGMA1-NEG-BALL-01` | `MP-CG001-GODEL-Q-ZFC-Z0-SIGMA1-NEG-BALL-001` | CG001-C-415 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261014-CG001-HALTING-WITHOUT-LEM-01` | `MP-CG001-HALTING-WITHOUT-LEM-001` | CG001-C-422 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261014-CG001-HALTING-WITHOUT-LEM-NEG-FLIP-01` | `MP-CG001-HALTING-WITHOUT-LEM-NEG-001` | CG001-C-422 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261014-CG001-TWO-CHOICES-LPO-01` | `MP-CG001-TWO-CHOICES-LPO-001` | CG001-C-418、CG001-C-419、CG001-C-420、CG001-C-421 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261014-CG001-TWO-CHOICES-LPO-NEG-FREE-01` | `MP-CG001-TWO-CHOICES-LPO-NEG-001` | CG001-C-418 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261014-CG001-TWO-CHOICES-LPO-NEG-SETTLING-01` | `MP-CG001-TWO-CHOICES-LPO-NEG-003` | CG001-C-420 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261014-CG001-TWO-CHOICES-LPO-NEG-UNBOUNDED-01` | `MP-CG001-TWO-CHOICES-LPO-NEG-002` | CG001-C-418 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261015-CG001-A-UNIVALENCE-B-01` | `MP-CG001-A-UNIVALENCE-B-001` | CG001-C-430 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR、ZFC1 |
| `20261015-CG001-A-UNIVALENCE-B-NEG-01` | `MP-CG001-A-UNIVALENCE-B-NEG-001` | CG001-C-430 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR、ZFC1 |
| `20261015-CG001-A-UNIVALENCE-B-NEG-02` | `MP-CG001-A-UNIVALENCE-B-NEG-002` | CG001-C-430 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR、ZFC1 |
| `20261015-CG001-A-UNIVALENCE-B-NEG-03` | `MP-CG001-A-UNIVALENCE-B-NEG-003` | CG001-C-430 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR、ZFC1 |
| `20261015-CG001-CIRCLE-PARADOX-01` | `MP-CG001-CIRCLE-PARADOX-001` | CG001-C-424 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261015-CG001-CIRCLE-PARADOX-NEG-CLOSE-01` | `MP-CG001-CIRCLE-PARADOX-NEG-001` | CG001-C-424 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261015-CG001-RUNNER-ARRIVAL-RATIONAL-01` | `MP-CG001-RUNNER-ARRIVAL-RATIONAL-001` | CG001-C-428 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261015-CG001-RUNNER-ARRIVAL-RATIONAL-NEG-STEP-01` | `MP-CG001-RUNNER-ARRIVAL-RATIONAL-NEG-001` | CG001-C-428 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261015-CG001-TERMINATION-GATE-01` | `MP-CG001-TERMINATION-GATE-001` | CG001-C-431 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261015-CG001-TERMINATION-GATE-NEG-01` | `MP-CG001-TERMINATION-GATE-NEG-001` | CG001-C-431 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261015-CG001-TWO-CHOICES-CUBICAL-01` | `MP-CG001-TWO-CHOICES-CUBICAL-001` | CG001-C-426 | Cubical Agda | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | UR、ZFC1 |
| `20261015-CG001-TWO-CHOICES-CUBICAL-NEG-01` | `MP-CG001-TWO-CHOICES-CUBICAL-NEG-001` | CG001-C-426 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR、ZFC1 |
| `20261015-CG001-TWO-CHOICES-CUBICAL-NEG-02` | `MP-CG001-TWO-CHOICES-CUBICAL-NEG-002` | CG001-C-426 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR、ZFC1 |
| `20261015-CG001-TWO-CHOICES-CUBICAL-NEG-03` | `MP-CG001-TWO-CHOICES-CUBICAL-NEG-003` | CG001-C-426 | Cubical Agda | 被拒（预期），exit 42，`KERNEL_REJECTED` | UR、ZFC1 |
| `20261015-CG001-TWO-CHOICES-RATIONAL-01` | `MP-CG001-TWO-CHOICES-RATIONAL-001` | CG001-C-425 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261015-CG001-TWO-CHOICES-RATIONAL-NEG-FREE-01` | `MP-CG001-TWO-CHOICES-RATIONAL-NEG-001` | CG001-C-425 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261015-CG001-TWO-CHOICES-RATIONAL-NEG-MODULUS-01` | `MP-CG001-TWO-CHOICES-RATIONAL-NEG-002` | CG001-C-425 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261015-CG001-Z0-OMEGA-QUESTION-01` | `MP-CG001-Z0-OMEGA-QUESTION-001` | CG001-C-427 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261015-CG001-Z0-OMEGA-QUESTION-NEG-STAGES-01` | `MP-CG001-Z0-OMEGA-QUESTION-NEG-001` | CG001-C-427 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
| `20261015-CG001-ZENO-ZFC-CLASSICAL-01` | `MP-CG001-ZENO-ZFC-CLASSICAL-001` | CG001-C-423 | Lean 4 | 接受，exit 0，`KERNEL_ACCEPTED_WITH_SCOPE` | ZFC1 |
| `20261015-CG001-ZENO-ZFC-CLASSICAL-NEG-FINITE-01` | `MP-CG001-ZENO-ZFC-CLASSICAL-NEG-001` | CG001-C-423 | Lean 4 | 被拒（预期），exit 1，`KERNEL_REJECTED` | ZFC1 |
