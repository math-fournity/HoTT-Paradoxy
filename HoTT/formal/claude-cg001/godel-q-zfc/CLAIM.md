# CG001-C-95 至 C-102：哥德尔式 Q 落在真实的 𝗭𝗙𝗖 上

> **证明包：** `MP-CG001-GODEL-Q-ZFC-001`（主包）；负控制 `MP-CG001-GODEL-Q-ZFC-NEG-SOUNDNESS-001`、`MP-CG001-GODEL-Q-ZFC-NEG-DELTA1-001`、`MP-CG001-GODEL-Q-ZFC-NEG-CONSISTENCY-001`。
>
> **目标包：** CG-006（`.claude/goals/CG-006-zfc-complete-formalization/`），本机会话 d58e0c0d，Opus 5.5，2026-10-08。
>
> **理论变体：** Lean 4（v4.34.0）内核，加本项目的 Mathlib（commit `5ed29652…`，Astra 缓存）与 FormalizedFormalLogic/Foundation（commit `1fb01b72`，本机禁网编译）。经典逻辑；内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。不涉及 HoTT 路径。
>
> **身份：** 全部命题为机器证明（运行收据见 §7）。相对 CG-005，变化在于：把 CG-005 读成关于 bare ZFC 时所依赖的标准元定理，除哥德尔第二定理所需的可推导条件之外，现在都对 Foundation 的 `𝗭𝗙𝗖` 证明成了 Lean 定理（§3）。

## 1. 记号

- `𝗭𝗙𝗖`：Foundation 的 `ZermeloFraenkelChoice = ((𝗕𝗦𝗧 ∪ 𝗦𝗘𝗣) ∪ 𝗥𝗘𝗣𝗟) ∪ 𝗔𝗖`，ℒₛₑₜ 上的一阶理论；`𝗭𝗙𝗖 ⊢ σ` 是 Foundation 的 LK 可推导性。这是 bare ZFC 的对象理论，不是它的某个模型，也不是扩张。
- `Process`、`Done`、`DoneBy`、`EffectiveTheory`、`OmegaClosed`、`RunnerTheory`、`AGeneral`、`Arrives`、`position`：沿用 CG-005（`../godel-q/CLAIM.md` §1）。`Done e` 是程序 `e` 在输入 0 上停机。
- `numeralF n`：Rayo 式冯·诺依曼数公式 `Num_n(z)`，`Num_0(z) := ∀w (w ∉ z)`，`Num_{n+1}(z) := ∃y (Num_n(y) ∧ ∀w (w ∈ z ↔ w ∈ y ∨ w = y))`。
- `φH := codeOfREPred haltsNat`、`ψN := codeOfREPred notYetNat`：Foundation 给出的 Σ1 算术公式（S1）；`ΦH`、`ΨN`：它们经翻译 `arithTrln`（ω 为定义域，`0 ↦ ∅`，`1 ↦ succ ∅`，加乘取 ω 上递归定义，`< ↦ ∈`）得到的 ℒₛₑₜ 公式。
- `haltsS Φ n := ∃z (Num_n(z) ∧ Φ(z))`，`neverS Φ n := ¬ haltsS Φ n`。三类陈述：`provesHalts e := 𝗭𝗙𝗖 ⊢ haltsS ΦH ⌜e⌝`，`provesNever e := 𝗭𝗙𝗖 ⊢ neverS ΦH ⌜e⌝`，`provesNotYet e k := 𝗭𝗙𝗖 ⊢ haltsS ΨN ⌜(e,k)⌝`（`⌜·⌝` 为 `Encodable.encode`）。
- `Universe`：Foundation 在 Lean 中构造的 𝗭𝗙𝗖 标准模型（需要 Lean 的宇宙层级）；`natEquivN : ℕ ≃ N Universe` 是 ℕ 与该模型 ω 上算术结构之间的同构。

## 2. 精确命题（类型逐字见 `GodelQ/ZFC/Qualification.lean`）

| 编号 | 定理 | 内容 | 前提 |
|---|---|---|---|
| CG001-C-95 | `qual_C95` | `𝗭𝗙𝗖` 有 Foundation 意义下的 Δ1 公理表示（`Theory.Δ₁`：Δ1 定义在 𝗜𝚺₁ 中可证地恰当）；`𝗦𝗘𝗣`、`𝗥𝗘𝗣𝗟` 各有 Δ1 识别（仿 Foundation 对归纳模式的 `InductionR`）；`𝗕𝗦𝗧` 有限 | 无 |
| CG001-C-96 | `qual_C96` | `numCode`（经 `PR.Blueprint` 的内部原始递归，Σ1）在 ℕ 中等于 `⌜Num_n⌝`；在 `𝗭` 的每个模型中 `Num_n(z) ↔ z = ofNat n` | 无 |
| CG001-C-97 | `qual_C97` | 对任意 ℒₛₑₜ 公式 `Φ`，`{n ∣ 𝗭𝗙𝗖 ⊢ neverS Φ n}` 可枚举（经 `𝗭𝗙𝗖.Δ₁`、内部可证性、`provable_iff_provable`、`rePred_iff_sigma1`） | 无 |
| CG001-C-98 | `qual_C98` | `𝗭𝗙𝗖 ⊳ 𝗥₀`（直接解释）；每个真实 r.e. 事实 `p a` 的数字句 `haltsS (arithTrln.translate (codeOfREPred p)) a` 被 𝗭𝗙𝗖 证明（𝗥₀ 的 Σ1 完全性，不需要可靠性） | 无 |
| CG001-C-99 | `qual_C99` | `zfcEffective : EffectiveTheory`，四条元性质全为定理；存在 `d`：`¬ Done d`，对每个 k `𝗭𝗙𝗖 ⊢ haltsS ΨN ⌜(d,k)⌝`，`𝗭𝗙𝗖 ⊬ neverS ΦH ⌜d⌝`，且 `Done d ↔ 𝗭𝗙𝗖 ⊢ neverS ΦH ⌜d⌝`；`¬ zfcEffective.OmegaClosed` | 无 |
| CG001-C-100 | `qual_C100` | 数字句 Σ1 可靠：`𝗭𝗙𝗖 ⊢ haltsS (…codeOfREPred p…) a → p a`；`provesHalts e ↔ Done e`；对角过程的两句都独立（`𝗭𝗙𝗖 ⊬ neverS`、`𝗭𝗙𝗖 ⊬ haltsS`）；`Entailment.Incomplete 𝗭𝗙𝗖` | 无（可靠性经 `Universe`，见 §8 第 2 条） |
| CG001-C-101 | `qual_C101`、`qual_C101_nonvacuous` | 对任意一族 ℒₛₑₜ 句 `arr`，若 `∀ a, 𝗭𝗙𝗖 ⊢ arr a 🡘 neverS ΦH a`：存在确实到达的跑者，𝗭𝗙𝗖 每一刻确认它尚未停、位置 < 1、有极限，却证明不了 `arr ⌜d⌝`；`AGeneral ↔ CompleteForNever`；`OmegaClosed → AGeneral`；`¬ AGeneral`。参数可满足（取 `arr := neverS ΦH`） | 参数 `harr` |
| CG001-C-102 | `qual_C102`、`qual_C102_crosscheck` | S1：对任意 `[T.Δ₁] [𝗥₀ ⪯ T] [T.SoundOnHierarchy 𝚺 1]` 的算术理论 T，哥德尔 I 过程形式（含独立性）与魔鬼交易；交叉核对：Foundation 自带的 `incomplete_of_halting_problem` 对同一 T（另加 `𝗜𝚺₁ ⪯ T`）给出 `Entailment.Incomplete T` | 所列类型类实例 |

## 3. 与 CG-005 §3 条件前提的逐条对照

| CG-005 的前提（读作 bare ZFC 时） | CG-005 的身份 | 现在 |
|---|---|---|
| R：ZFC 有效公理化，`{e ∣ ZFC ⊢ Never(e)}` 可枚举 | 来源（标准结果） | **机器证明**：C-95（`𝗭𝗙𝗖.Δ₁`）、C-97（可枚举） |
| Σ1C、Δ0C | 来源 | **机器证明**：C-98（𝗥₀ 的 Σ1 完全性 + `𝗭𝗙𝗖 ⊳ 𝗥₀` + 数字公式语义 C-96） |
| Con：ZFC 一致 | 通行前提 | **Lean 元层定理**：Foundation 的 `zfc_consistent`（`Universe.{0}` 是模型）。它在 Lean 的元理论里成立，不是 𝗭𝗙𝗖 内部可证的事 |
| Σ1 可靠（只用于“⊬ Halts(d)”） | CG-005 未单列 | **Lean 元层定理**：C-100（`Universe` 中 ω ≅ ℕ） |
| HBL、Diag（哥德尔第二定理，C-92 的 ZFC 读法） | 来源 | **仍未形式化**（CG-006 的 S6）。卡点：把算术句的翻译 `arithTrln.translate` 在 𝗜𝚺₁ 中内部化为 Σ1 函数，以及在每个 ZFC 模型的 ω 上验证 𝗜𝚺₁ |
| 跑者链接：ZFC 证明“跑者到达 ⟺ d 永不停机” | 来源（实分析在 ZFC 中复述） | **显式参数**：C-101 以 `harr` 为参数；元层对应是 CG-005 已证的 `arrives_iff` |

## 4. 与 GPT 的“六道门”逐门对照

六道门原文出自主干第 113 轮的最终回答（`audit/GUI-SYNTH-REDO/qa/dev-08/0113.md`；GPT 自述，作为要求清单使用）。

| 门 | 要求（摘述） | 本包怎样支付 |
|---|---|---|
| 1 固定理论 T | 不得把 bare ZFC、扩张、模型、共同体接口混写 | T 是 Foundation 的对象理论 `𝗭𝗙𝗖`；`Universe` 只在元层用于一致性与可靠性，标明身份（§8） |
| 2 固定真实消费者 Accept_T | 来自真实形式系统，不能为对角化临时虚构 | Accept 取 𝗭𝗙𝗖 自己的可推导性 `⊢`，以及 Foundation 的内部可证性 `Provable 𝗭𝗙𝗖`（`provable_iff_provable`） |
| 3 编码有效 | 编码、接受、替换、有限验证关系可表示或可计算 | `𝗭𝗙𝗖.Δ₁`（C-95）、`numCode` Σ1（C-96）、`Provable` 的 Σ1 性与可枚举（C-97）；过程编码为 Mathlib 的 `Nat.Partrec.Code`，停机由 Foundation 的 `codeOfREPred` 表示 |
| 4 对角操作真实存在 | 可执行的 diag 或不动点构造 | Kleene 第二递归定理 `Code.fixed_point₂`（CG-005 C-85），作用在 𝗭𝗙𝗖 的真实接受关系上（`zfcEffective.observer`） |
| 5 同一任务桥 | OriginDone 须与圆环／芝诺／H0 的原完成同一 | OriginDone 取停机，依据是研究发起人自己的口径（KC-000010、KC-000024；0109 第 45 轮“芝诺……从第一天开始，就是一个可计算性问题”）。与芝诺的连接是 C-101 的跑者（到达恰当 d 永不停）；与 H0 的连接是 CG-005 C-93 的同一 ω 追问（跨内核的结构对应）。这一门的“同一”是解释桥，不是定理 |
| 6 承认合法防御 | 拒绝接受、要求 bridge 或改写任务可能是防御或不完备，不自动叫矛盾 | 本包证明的正是“拒绝”：𝗭𝗙𝗖 既不证 `neverS` 也不证 `haltsS`（不完全，C-100）。矛盾只出现在“𝗭𝗙𝗖 + P”中（魔鬼交易，C-99；CG-005 C-90） |

与“形似”夹具的区别：C-368 把不动点 `step d = d` 与桥写进前提；dev-02 与主干的 `ZFCOneUse` 中“ZFC”是一个命题变量；本包的 T 是 Foundation 的真实对象理论，接受关系是它的可推导性，对角点由递归定理构造，四条元性质都是定理，没有任何结论性的东西写在前提里。

## 5. 主要中间引理（便于审计）

- `SchemaR`、`chSchema`、`SchemaR.defined`、`schemaR_quote_iff`、`schemaDelta1`（`SchemaDelta1.lean`）：公理模式的通用 Δ1 识别。`φ ⇜ ![#0]`、`φ ⇜ ![#0,#1]` 只是 `castLE`，编码不变，所以主体编码函数里可以直接放 `k`，界 `k ≤ F k` 结构性成立。
- `quote_substs_eq`（`ReplacementDelta1.lean`）：`⌜φ ⇜ v⌝ = subst ℒₛₑₜ ↑(vecCode v) ⌜φ⌝`。
- `eval_numeralF_iff`（`NumeralSemantics.lean`）。
- `models_haltsS_iff`、`models_subst_numeral_iff`（`Effective.lean`）：数字句的真值与 ω 结构中 `ofNat a` 处的真值相同。
- `eval_equiv_iff`（`Soundness.lean`）：保持函数与关系的结构双射保持一切公式的求值（Foundation 只有 `ofEquiv` 版与开公式的同态版）。
- `universe_mem_ω`：`Universe` 中 ω 的元素都是 `ofNat n`（`Universe.omega = range ofNat` 是归纳集，ω 是最小归纳集）。

## 6. 负控制

| proof id | 文件 | 去掉的前提 | 预期 |
|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-NEG-SOUNDNESS-001` | `GodelQ/Negative/WrongSoundnessWithoutModel.lean` | 模型（给 𝗭𝗙𝗖 加一句 `haltsS ΦH a`） | 拒绝：`Universe ⊧* insert (haltsS ΦH a) 𝗭𝗙𝗖` 找不到 |
| `MP-CG001-GODEL-Q-ZFC-NEG-DELTA1-001` | `GodelQ/Negative/WrongREWithoutDelta1.lean` | Δ1 公理表示（`Universe` 的全部真句） | 拒绝：`Theory.Δ₁ trueInUniverse` 找不到 |
| `MP-CG001-GODEL-Q-ZFC-NEG-CONSISTENCY-001` | `GodelQ/Negative/WrongConsistencyWithBot.lean` | 一致性（`insert ⊥ 𝗭𝗙𝗖`） | 拒绝：`Entailment.Consistent (insert ⊥ 𝗭𝗙𝗖)` 找不到 |

每个负控制去掉的，正是主包里对应一步所用的输入：`zfc_haltsS_sound` 用 `Universe` 的模型实例，`never_re` 用 `𝗭𝗙𝗖.Δ₁`，`zfcEffective.consistent` 用 `zfc_consistent`。

## 7. 运行

见本节下方运行表（捕获之后填写）与 CG-001 目标本地证据索引 §25。全部运行由 `.claude/goals/CG-006-zfc-complete-formalization/tools/capture_zfc_run.py` 捕获，驱动 `zfc_lean_check.py` 在编译前逐一核对 `LEAN_TOOLCHAIN.json` 与 `MATHLIB_CLOSURE.json`（Foundation、Mathlib 与依赖的逐模块哈希），固定路径的 Lean 在 `sandbox-exec` 禁网环境中运行。`GodelQ/ProcessObservation.lean`、`EffectiveTheory.lean`、`GodelZenoRunner.lean` 与 `../godel-q/GodelQ/` 中同名文件逐字节相同。

## 8. 禁止外推

1. 不推出 `𝗭𝗙𝗖 ⊢ ⊥`，也不推出 bare ZFC 不一致。“不一致”只出现在给 𝗭𝗙𝗖 加上 ω 完成规则 P（或 A_general）之后的理论里。
2. 一致性（`zfc_consistent`）与数字句的 Σ1 可靠（C-100）来自 Lean 元层的模型 `Universe`，它要用 Lean 的宇宙层级（比 ZFC 强的元理论）。它们是 Lean 定理，不是 𝗭𝗙𝗖 内部可证的事；𝗭𝗙𝗖 自己证明不了自己的一致性（这是哥德尔第二定理，本包没有对 𝗭𝗙𝗖 形式化，见第 4 条）。
3. “e 停机”“e 永不停机”“e 在 k 步内尚未停机”在 ℒₛₑₜ 中取本包的特定写法（数字公式加翻译后的 Σ1 公式）。别的写法要另证与它们在 𝗭𝗙𝗖 中可证等价。
4. 哥德尔第二定理对 𝗭𝗙𝗖 的形式（C-92 的 ZFC 读法、Z0 的“𝗭𝗙𝗖 证明不了自己的矛盾搜索永不停”）没有在本包形式化；它仍以 HBL 可推导条件与对角引理为来源前提。
5. C-101 的跑者部分以“到达句与永不停机句在 𝗭𝗙𝗖 中逐个可证等价”为显式参数；“跑者到达”的实分析句在 ℒₛₑₜ 中的写法与这一等价的 𝗭𝗙𝗖 内部证明不在本包。
6. “时间维度 = 过程的逐步运行”是按研究发起人框架所作的解释桥（KC-000010、013、024），不是定理。
7. 哥德尔、Kleene、Turing、Löb 的数学与 Foundation 的形式化机制（内部可证性、Δ1 表示、直接解释、`Universe` 模型、`zfc_consistent`）是既有工作。新的是：把它们落到 𝗭𝗙𝗖 上所需的部分（分离与替换模式的 Δ1 识别、`𝗭𝗙𝗖 ⊳ 𝗥₀`、Rayo 数字公式的编码与语义、`Universe` 中 ω ≅ ℕ），以及由此得到的、关于真实 𝗭𝗙𝗖 的过程形式定理。
8. P 是“数学幻觉”、“与魔鬼达成交易”、“数学的灵魂”是研究发起人的读法与 AI 的解释，不是定理。
