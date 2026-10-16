# CG001-C-84 至 C-94：哥德尔式 Q——过程完成的观察力及其不完备

> **证明包：** `MP-CG001-GODEL-Q-001`（主包）；负控制 `MP-CG001-GODEL-Q-NEG-SOUNDNESS-001`、`MP-CG001-GODEL-Q-NEG-CONSISTENCY-001`、`MP-CG001-GODEL-Q-NEG-EFFECTIVENESS-001`、`MP-CG001-GODEL-Q-NEG-GODEL-II-001`。
>
> **目标包：** CG-005（`.claude/goals/CG-005-godel-q-synthesis/`），本机会话 d58e0c0d，Opus 5.5，2026-10-07。
>
> **理论变体：** Lean 4（v4.34.0，commit `293d5d0c`）内核，加 Mathlib（commit `5ed29652…`，本项目工具链缓存）；经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`，证明论层（C-92）不依赖任何公理。不涉及 HoTT 路径；HoTT 一侧的 H0 实例只以参数接入（见 §4）。
>
> **身份：** 抽象定理与计算层定理为机器证明（运行收据见 §6）；对 bare ZFC 的实例化以 §3 列出的标准元定理与一致性假设为条件，那些元定理本包没有机器证明。

## 1. 记号

- 过程 `Process := Nat.Partrec.Code`（部分递归程序的代码）。
- 原过程完成 `Done e := (Code.eval e 0).Dom`（程序在输入 0 上停机）。这是研究发起人自己的口径：时间悖论以“不可计算性/不可停机性”为特征（KC-000010），芝诺是“结结实实的计算步骤、过程”（2026-10-04，`原话摘录.md` 0109 第 45 轮）。
- 阶段观察 `DoneBy e k := (Code.evaln k e 0).isSome = true`（在 `k` 步燃料内已停机）。
- 永不完成观察者 `NeverObserver`：一个接受集 `accepts`，它可枚举（`REPred accepts`），并且可靠（`accepts e → ¬ Done e`）。
- 有效理论 `EffectiveTheory`：三类陈述 `provesHalts`、`provesNever`、`provesNotYet`，附四条元性质（R）`re_never : REPred provesNever`、（Σ1C）`Done e → provesHalts e`、（Δ0C）`¬ DoneBy e k → provesNotYet e k`、（Con）不同时证明 `e` 停机与永不停机。
- ω 完成规则 P（`OmegaClosed`）：`(∀ k, provesNotYet e k) → provesNever e`。
- 跑者：`remaining d 0 = 1`，`remaining d (n+1) = if DoneBy d n then remaining d n else remaining d n / 2`；`position d n = 1 - remaining d n`；`Arrives d := Tendsto (position d) atTop (𝓝 1)`；`Restores d := Tendsto (remaining d) atTop (𝓝 0)`。
- `RunnerTheory`：有效理论另加 `provesArrives` 与 `arrives_iff_never : provesArrives d ↔ provesNever d`（理论证明“跑者到达 ⟺ d 永不停机”）；`AGeneral := ∀ d, Arrives d → provesArrives d`。
- `HBLTheory`：句子、可证性、蕴涵、`bot`、内部可证性 `box`，附 K、S、分离规则、D1–D3 与对角引理；`con := box bot → bot`。

## 2. 精确命题（类型逐字见 `GodelQ/Qualification.lean`）

| 编号 | 定理（`Qualification.lean`） | 内容 | 前提 |
|---|---|---|---|
| CG001-C-84 | `qual_C84` | `Done e ↔ ∃ k, DoneBy e k`；`DoneBy` 单调；`DoneBy` 作为二元谓词可计算 | 无 |
| CG001-C-85 | `qual_C85` | 对任一可枚举 `accepts`，存在 `d` 使 `Done d ↔ accepts d`（`d` 由 `Code.fixed_point₂`，即 Kleene 第二递归定理构造）；对任一 `NeverObserver O`，存在 `d`：`¬ Done d ∧ ¬ O.accepts d ∧ (Done d ↔ O.accepts d)` | 无 |
| CG001-C-86 | `qual_C86` | 不存在完备的 `NeverObserver`；可靠且完备的接受集不可枚举；`¬ REPred (fun e => ¬ Done e)`（Mathlib 经 Rice 定理的独立证明） | 无 |
| CG001-C-87 | `qual_C87` | 任一 `O` 有严格更大的 `O'`（多接受一个 `O` 漏掉的真永不完成者），`O'` 仍有漏点 | 无 |
| CG001-C-88 | `qual_C88` | 有效理论：`provesNever e → ¬ Done e`；每次完成都被证明；永不完成者的每个有限时刻都被证明“尚未完成” | R、Σ1C、Δ0C、Con |
| CG001-C-89 | `qual_C89` | 存在 `d`：`¬ Done d`，`¬ provesNever d`，`∀ k, provesNotYet d k`，且 `Done d ↔ provesNever d`；`¬ CompleteForNever` | 同上 |
| CG001-C-90 | `qual_C90` | 有效理论 `¬ OmegaClosed`；封闭于 P 的一致 Σ1C/Δ0C 理论 `¬ REPred provesNever`；有效 + Σ1C + Δ0C + P（不预设一致性）⟹ 存在 `e` 同时被证明停机与永不停机 | 同上 |
| CG001-C-91 | `qual_C91` | 对任一可枚举可靠的到达接受者 `O`，存在 `d`：`Arrives d`，`¬ O.accepts d`，`∀ n, position d n < 1`，极限存在，`Arrives d ↔ ¬ O.accepts d`；`Arrives d ↔ ¬ Done d`；`Restores d ↔ Arrives d`；`rfind' succ` 驱动的跑者恰是经典芝诺序列，到达，且 `toyTheory` 确认它 | 无（理论实例化同 C-89） |
| CG001-C-92 | `qual_C92` | HBL 理论：Löb；`Pr con → Pr bot`；一致 ⟹ `¬ Pr con`；扩张若证明 `con`，则严格更强；`trivialBoxModel` 一致且 `¬ Pr con` | HBL、Diag |
| CG001-C-93 | `qual_C93` | 任一永不完成的 ω 追问上，“形式上完成的整体 ⟹ 有限阶段完成”（P_fin）被否定；芝诺：永不在有限阶段到达而极限为 1；H0（参数形式）：在“每一问都答否”之下 P_fin 被否定；`(processQ d).Never ↔ Arrives d`；可观察性的分界 | 无（H0 的“每一问都答否”由 §4 接入） |
| CG001-C-94 | `qual_C94` | `AGeneral ↔ CompleteForNever`；`OmegaClosed → AGeneral`；有效 `RunnerTheory` 没有 `AGeneral`；具有 `AGeneral` 的 Σ1C/Δ0C 理论要么 `¬ REPred provesNever`，要么不一致 | R、Σ1C、Δ0C、Con、跑者链接 |

非空与必要性控制（同一主运行内机器检查）：`toyTheory`（四条前提可被一个具体有效理论同时满足）、`truthTheory`（P 可一致但不可枚举）、`consistency_needed`（不要一致性时 P 可被有效理论满足）、`soundness_needed`（不要可靠性时对角逃逸不成立）、`trivialBoxModel`（HBL 前提可被一致模型满足）。

## 3. 对 bare ZFC 的实例化：所依赖的标准元定理

本包的理论层定理对任何满足前提的结构成立。把它们读成关于 bare ZFC 的陈述，需要以下事实；它们是数理逻辑的标准结果（来源），本包**没有**对 ZFC 的语法与证明系统作形式化，因此这一层的身份是 `CONDITIONAL_ON_STANDARD_METATHEOREMS_SOURCE_REPORTED`。

| 前提 | 对 bare ZFC 的内容 | 来源（标准文献） |
|---|---|---|
| R | ZFC 有效公理化，其定理集可枚举；因而 `{e ∣ ZFC ⊢ ⌜e 永不停机⌝}` 可枚举 | Gödel 1931；Kleene 1952《Introduction to Metamathematics》；Shoenfield 1967《Mathematical Logic》第 6 章 |
| Σ1C、Δ0C | 真的 Σ1 句（含“e 在第 k 步前停机”这类有界句）在 Robinson 算术 Q 中可证；ZFC 经 ω 解释 Q | Boolos–Burgess–Jeffrey《Computability and Logic》（第 5 版，2007）第 16–17 章；Smoryński 1977 “The incompleteness theorems”（Handbook of Mathematical Logic） |
| Con | ZFC 一致（通行的前提；由哥德尔第二定理，ZFC 自身证明不了） | — |
| HBL、Diag | ZFC 的标准可证性谓词满足 Hilbert–Bernays–Löb 可推导条件；对角引理对扩张 Q 的理论成立 | Hilbert–Bernays 1939；Löb 1955（JSL 20）；Boolos–Burgess–Jeffrey 第 17–18 章；Boolos 1993《The Logic of Provability》 |
| 跑者链接 | ZFC 证明“跑者到达 ⟺ d 永不停机”（本包 `arrives_iff` 只用初等实分析：单调收敛、几何级数、极限唯一） | 本包 `arrives_iff` 的证明可在 ZFC 中复述 |

形式锚点（来源转述，本目标未重放）：FormalizedFormalLogic/Foundation@`f3972f42` 在 Lean 4 中对扩张 𝗥₀ 的一阶算术理论形式化了第一不完备定理（GPT 在 dev-09 的 C-369 重放过），并含第二不完备定理模块；它没有给出 ZFC 语言到算术的解释实例（dev-09 `8fce0b92` 的直接映射负控制）。

## 4. HoTT 一侧：H0 的跨内核接口

`h0Q settled` 与 `h0_P_fin_refuted` 以参数 `settled : ℕ → Prop` 与假设 `∀ n, ¬ settled n` 接入。读法：`settled n` 为“宇宙 `Type ℓ-zero` 上的逐层追问程序在燃料 `n` 内交出了某个落定层”。“每一问都答否”是 Cubical Agda 中的定理 CG001-C-78（`HoTT/formal/claude-cg001/questioning-delay/`；对任意判定器，`question (Type ℓ-zero) judge ≡ never`，任何燃料都得 `nothing`），另有 GPT 的 C-365（dev：`trace (question (Type ℓ-zero) judge) = λ _ → nothing`）。两个内核之间没有形式翻译；同图式是结构对应，身份 `CROSS_KERNEL_SCHEMA_CORRESPONDENCE_NOT_A_SINGLE_KERNEL_PROOF`。

## 5. 负控制

| proof id | 文件 | 去掉的前提 | 预期 |
|---|---|---|---|
| `MP-CG001-GODEL-Q-NEG-SOUNDNESS-001` | `GodelQ/Negative/WrongEscapeWithoutSoundness.lean` | 观察者的可靠性（对“接受一切”的集合套对角逃逸） | 拒绝：`sound` 字段无法提供 |
| `MP-CG001-GODEL-Q-NEG-CONSISTENCY-001` | `GodelQ/Negative/WrongTheoryWithoutConsistency.lean` | 理论的一致性（什么都证明的理论） | 拒绝：`consistent` 字段无法提供 |
| `MP-CG001-GODEL-Q-NEG-EFFECTIVENESS-001` | `GodelQ/Negative/WrongBargainWithoutEffectiveness.lean` | 有效性（把 `truthTheory` 当有效理论套魔鬼交易） | 拒绝：`re_never` 无法提供 |
| `MP-CG001-GODEL-Q-NEG-GODEL-II-001` | `GodelQ/Negative/WrongConsistencyProvable.lean` | — （在一致 HBL 模型中证明一致性陈述） | 拒绝：目标为假 |

每一条被拒的目标，主包里都另有正面定理证明它本来不成立：`soundness_needed`、`consistency_needed`、`never_done_not_re`（与 `truthTheory`）、`trivialBoxModel_con_unprovable`。

## 6. 运行

见 `README.md` 的运行表与 CG-001 目标本地证据索引 §24。全部运行由 `.claude/goals/CG-005-godel-q-synthesis/tools/godelq_lean_check.py` 执行：固定路径的 Lean、`sandbox-exec` 禁网、编译前逐一核对 `LEAN_TOOLCHAIN.json` 与 `MATHLIB_CLOSURE.json`（1,692 个模块的编译产物哈希）。

## 7. 禁止外推

1. 不推出 `ZFC ⊢ ⊥`，也不推出 bare ZFC 不一致。C-90/C-94 的“不一致”分支说的是：给有效理论加上 ω 完成规则（或 A_general）之后的那个理论。
2. ZFC 实例化以 §3 的标准元定理与 Con(ZFC) 为条件；本包没有形式化 ZFC 的语法、证明系统、对 Q 的解释或可推导条件。
3. `EffectiveTheory`、`RunnerTheory`、`HBLTheory` 只刻画理论中与过程相关的片段，不是 ZFC 的形式化。它们的字段是标准元性质，不含对角点或结论；对角点在证明内由递归定理构造（这一点区别于 C-368、C-359 一类把不动点、桥或冲突写进前提的夹具）。
4. 哥德尔、Kleene、Turing、Löb 的数学是经典结果，不是新发现。新的是读法与综合：把“理论对时间维度的观察力”落实为“理论对过程完成的观察”，把 ZFC + A = ZFC + P 落实为 C-94 的等价与二难，把哥德尔句落实为芝诺跑者，并把芝诺、H0、Z0 放进同一个 ω 追问图式。
5. “时间维度”在这里是离散的计算步骤；把它读作研究发起人所说的时间维度，依据是研究发起人自己的框架（KC-000010/013/024），属于解释桥，不是定理。
6. P 是“数学幻觉”、“与魔鬼达成交易”、“数学的灵魂”是研究发起人的读法与 AI 的解释，不是定理。
7. 平凡芝诺控制（C-91 末项）表明：经典芝诺序列的到达是看得见的。所以本包不主张“极限理论在经典芝诺上失败”；它主张的是“极限理论解决芝诺式问题”作为一般方法（A_general）在 bare ZFC 中不成立（C-94）。
8. 圆环读法（`Restores`）只抓住“两端逼近、复原却确认不了”这一面；研究发起人圆环悖论中的“此前已经得到 M”、零大小的点与反向过程，本包没有承接。
9. H0 在 Lean 中是参数实例；HoTT 内容在 Agda（C-78），跨内核对应不是单一内核的证明。
