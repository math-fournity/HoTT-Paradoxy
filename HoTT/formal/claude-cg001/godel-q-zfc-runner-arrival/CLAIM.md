# CG001-C-117、C-118：跑者的到达句——一族具体的 ℒₛₑₜ 句，𝗭𝗙𝗖 逐个证明它与永不停机句等价

> **证明包**：`MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-001`（`GodelQ/ZFC/QualificationArrival.lean`）；负控制 `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-001`、`-NEG-002`。
>
> **目标包**：CG-007（`.claude/goals/CG-007-formalization-completion/`），单元 W5；本机会话 d58e0c0d，Opus 5.5，2026-10-09。
>
> **理论变体**：Lean 4（v4.34.0）内核，加 Mathlib（`5ed29652`）与 FormalizedFormalLogic/Foundation（`1fb01b72`）。经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。对象是 Foundation 中的一阶 `𝗭𝗙𝗖`（ℒₛₑₜ 语法、LK 证明系统）与算术语言 ℒₒᵣ。不涉及 HoTT 路径。
>
> **身份**：机器证明，范围见 §5。𝗭𝗙𝗖 的一致性与数字句的可靠性，沿用 `../godel-q-zfc/` 的 Lean 元层 `Universe` 模型（要用宇宙），不是 𝗭𝗙𝗖 内部可证的事。

## 0. 这一条在研究里的位置

- C-101（`../godel-q-zfc/`）把哥德尔–芝诺跑者落到 𝗭𝗙𝗖 上，跑者部分有一个显式参数：一族 ℒₛₑₜ 句 `arr`，使 `𝗭𝗙𝗖 ⊢ arr a 🡘 neverS ΦH a` 对每个 a 成立。参数可满足（取 `arr := neverS ΦH`），但那样“到达句”就是永不停机句本身，没有内容。
- CG-007 完成门 3 要的是：一族具体的 ℒₛₑₜ 句，它不是 `neverS` 本身，且 𝗭𝗙𝗖 逐个证明它与永不停机句等价。本包给出这一族句子，并把 C-101 的跑者部分与 C-115 的 𝗭𝗙𝗖 审查都改成用它。
- 【解释】一句话：“跑者到了”在通常的数学里写成“剩余距离趋于 0”，即对每个精度 2⁻ᴷ，从某一步起剩余距离都不超过它。本包把这句话写成算术句：剩余距离 ≤ 2⁻ᴷ，就是“到这一步，跑者已经减半至少 K 次”。再把它翻译成集合论的句子，𝗭𝗙𝗖 证明它恰好等价于“那个过程永不停机”。

## 1. 记号

- 过程、`Done`、`DoneBy`、`remaining`、`position`、`Arrives`、`Restores`、`EffectiveTheory`、`RunnerTheory`：同 `../godel-q/CLAIM.md` §1。`haltsS`、`neverS`、`ΨN`、`Universe`：同 `../godel-q-zfc/CLAIM.md` §1。`W M`、`theta`：同 `../godel-q-zfc-z0-pa/CLAIM.md`（ω 的标准解释与翻译解释）。`Adequate`、`Review`：同 `../idea-t-c6-p/CLAIM.md`（C-115）。
- 算术层（`GodelQ/ZFC/ArrivalArith.lean`）：
  - `stopB n i`：代码为 n 的程序在 i 步燃料内已停机（布尔值，可计算）；
  - `θ e i`：它的 Σ1 代码公式（Foundation 的 `codeOfPartrec'`，输出取 1）；
  - `stopF e k := ∃ i ≤ k, θ e i`；`haltsF e := ∃ k, stopF e k`；
  - `halvedF e K n := K ≤ n ∧ ∀ i < K, ¬ stopF e i`：到第 n 步已减半至少 K 次；
  - `arrF e := ∀ K, ∃ N, ∀ n, N ≤ n → halvedF e K n`：到达的 ε–N 写法，ε 取 2⁻ᴷ。
- 𝗭𝗙𝗖 层（`GodelQ/ZFC/ArrivalZFC.lean`）：
  - `ΦS := arithTrln.translate haltsF`：新的停机公式；
  - `arrS a := haltsS (arithTrln.translate arrF) a`：跑者到达句；
  - `zfcEffective'`：以 ΦS 为停机公式的 𝗭𝗙𝗖 观察接口，“第 k 步尚未停”仍用 `ΨN`；
  - `zfcRunner`：加上到达句的 `RunnerTheory`；
  - `zfcReviewArr`：用到达句的 C6 审查。

## 2. 精确命题（类型逐字见 `GodelQ/ZFC/QualificationArrival.lean`）

| 编号 | 定理 | 内容 | 前提 |
|---|---|---|---|
| CG001-C-117 | `qual_C117` | (1) θ 是 Σ1 公式，在 ℕ 里恰说“程序在 i 步燃料内已停机”。(2) 在**每一个** 𝗣𝗔⁻ 模型里：`stopF` 对步数单调；“已减半 K+1 次”恰是“n ≥ K+1 且到第 K 步还没停”；`arrF e ↔ ¬ haltsF e`。(3) 实数一侧：剩余距离 ≤ 2⁻ᴷ，恰是 K ≤ n 且前 K 步都还没停；跑者到达恰是 ε–N 写法。(4) 标准模型里：`haltsF ⌜d⌝` 恰是 d 停机；`halvedF ⌜d⌝ K n` 恰是剩余距离 ≤ 2⁻ᴷ；`arrF ⌜d⌝` 逐字是 ε–N 写法，恰是跑者到达 | 无 |
| CG001-C-118 | `qual_C118` | (1) 对每个 a，`arrS a ≠ neverS ΦS a`，而 `𝗭𝗙𝗖 ⊢ arrS a 🡘 neverS ΦS a`。(2) 到达句在 `Universe` 里的意思恰是跑者到达；𝗭𝗙𝗖 证明的到达句都不错。(3) `𝗭𝗙𝗖 ⊢ haltsS ΦS ⌜e⌝` 恰好当 e 停机。(4) **C-101 的跑者部分不再带参数**：有一个跑者确实到达，𝗭𝗙𝗖 每一刻都确认它尚未停，位置每一刻 < 1、极限存在，𝗭𝗙𝗖 却证明不了它的到达句。(5) A_general ⟺ Q 完备；𝗭𝗙𝗖 没有 A_general，也不封闭于 ω 完成规则；对角过程的停机句、永不停机句与到达句都不可证。(6) **C-115 改用到达句**：有一个标准解确实出错的跑者，𝗭𝗙𝗖 既证不了它停机，也证不了它的到达句；未被批判的错误无穷且列不全；这样的审查不完备 | 无（一致与可靠经 `Universe`，见 §5 第 4 条） |

## 3. 证明的要点

- **为什么要新的停机公式 ΦS**：
  - 旧的 `ΦH` 是 Foundation 的 `codeOfREPred`，由 `Classical.epsilon` 选出，在非标准模型里的行为无从推理。
  - 对永不停机的 d，“`ΦH(⌜d⌝)` 与 `∃k stopF(⌜d⌝, k)` 等价”在 𝗭𝗙𝗖 中能不能证，本包不知道，也不声称。
  - ΦS 与到达句来自同一个 `stopF`，二者的等价在每个模型里都成立。
  - 负控制 `WrongArrivalOldPhi` 核对：同一论证换成 `ΦH`，类型对不上，被拒。
- **𝗭𝗙𝗖 中的等价是语义证明**：
  - 在 𝗭𝗙𝗖 的每个模型 M 里，数字句 `haltsS (·)⁺ a` 的真假等于该公式在 ω（翻译解释）的 `ofNat a` 处的真假（`models_haltsS_iff`，C-100 的工具）。
  - ω 的翻译解释与标准解释 `W M` 满足同样的公式（`eval_W_iff`，C-109 的工具）。
  - `W M` 是 𝗣𝗔⁻ 的模型（C-109）。
  - 在任何 𝗣𝗔⁻ 模型里，`arrF e ↔ ¬ haltsF e` 只用到 `N ≤ N` 与 `k < k + 1`（C-117 (2)）。
  - 最后用 𝗭𝗙𝗖 的完备性（`SetTheory.complete`）。
- **到达句的意思**：
  - 原子部分 `halvedF ⌜d⌝ K n` 在 ℕ 里恰是 `remaining d n ≤ (1/2)^K`。对步数归纳证明，用到阶段观察的单调性。
  - 于是 `arrF ⌜d⌝` 在 ℕ 里逐字是“对每个 K，从某一步起剩余距离 ≤ 2⁻ᴷ”。
  - 实分析的引理 `restores_iff_eps` 说它恰是剩余距离趋于 0，用的是剩余距离为正与 2⁻ᴷ → 0；`restores_iff_arrives`（C-91）又说这恰是位置趋于 1。
  - 由 `Universe` 中 ω ≅ ℕ（C-100），ℒₛₑₜ 的到达句在 `Universe` 里的意思就是跑者到达。
- **四条元性质**（`zfcEffective'`）：
  - 可枚举：C-97 的 `never_re`，对任意公式成立；
  - Σ1 完全：对任一 Σ1 算术公式，`zfc_proves_haltsS_sigma1`；
  - Δ0 完全：同 C-99；
  - 一致：Foundation 的 `zfc_consistent`。

## 4. 与已有命题的关系

- **C-101**：跑者部分的参数 `harr` 在 ΦS 接口上被支付（C-118 (1)(4)）。C-101 本身对旧接口 `ΦH` 的陈述不变。
- **C-99、C-100**：哥德尔 I 的过程形式与独立性，对新接口重新得到（C-118 (5)）。抽象定理（C-85、C-89、C-90、C-94）对任一 `EffectiveTheory` 成立，这里只是换了一个接口。
- **C-115**：原来 𝗭𝗙𝗖 的审查句取停机句与永不停机句，依据 Lean 元层的等价；现在“证明不充分”取作证明到达句（C-118 (6)），这是 C-115 CLAIM §3 留下的那一步。
- **C-109**（`𝗭𝗙𝗖 ⊳ 𝗣𝗔`）：本包用到它的模型部分（每个 𝗭𝗙𝗖 模型的 ω 是 𝗣𝗔⁻ 的模型），没有用归纳。
- **CG-007 方案 §2 W5 的设计**：原设计先做“无限多次减半”的退路版，再做指数版。实际直接做了 ε–N 版：剩余距离 ≤ 2⁻ᴷ 用“已减半至少 K 次”来写，所以不需要在算术里定义指数或计数。

## 5. 禁止外推

1. 不推出 ZFC ⊢ ⊥，也不推出 bare ZFC 不一致。
2. 到达句是算术写法，经翻译放进 ℒₛₑₜ。它没有在 𝗭𝗙𝗖 内部构造实数：剩余距离 2⁻ᴷ 用“已减半至少 K 次”表达，实数的读法在 Lean 元层（`arrF_encode`、`universe_arrS_iff`）。
3. 等价 `𝗭𝗙𝗖 ⊢ arrS a 🡘 neverS ΦS a` 是对新停机公式 ΦS 的。对旧的 `ΦH` 不声称，参见 §3 第 1 条。
4. 𝗭𝗙𝗖 一致与数字句可靠来自 Lean 元层的 `Universe` 模型，不是 𝗭𝗙𝗖 内部可证。
5. 等价的证明很短，只用到 ω 上的两条序的事实。它的内容是：一旦把“剩余距离 ≤ 2⁻ᴷ”写成“已减半至少 K 次”，到达就恰是永不停机。分析的部分（2⁻ᴷ → 0、剩余距离为正）在元层。
6. 圆环的完整结构（此前已得到 M、零大小的点、反向过程）没有承接。
7. 标签（跑者、到达、剩余距离）不证明任何物理事实；“时间维度 = 过程的逐步运行”是解释桥。

## 6. 负控制

| proof id | 文件 | 被否定的说法 | 预期 |
|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-001` | `GodelQ/Negative/WrongArrivalOldPhi.lean` | 同一语义论证给出 `𝗭𝗙𝗖 ⊢ arrS a 🡘 neverS ΦH a`（旧的不透明停机公式） | 拒绝：类型不符，手里的结论是关于 `haltsS ΦS a` 的，要的是 `haltsS ΦH a` |
| `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-002` | `GodelQ/Negative/WrongHaltingRunnerArrives.lean` | 会停的过程 `Code.zero` 的到达句在 `Universe` 里为真 | 拒绝：要补的“`Code.zero` 永不停机”是假的，目标 `¬(zero.eval 0).Dom` 证不出 |

## 7. 文件

- **逐字节复制，复制时核对过（21 个）**：
  - 自 `../godel-q-zfc-z0-pa/GodelQ/`：`ProcessObservation`、`EffectiveTheory`、`GodelZenoRunner`、`FoundationArith`，以及 `ZFC/` 下的 SetLanguage、SchemaDelta1、ReplacementDelta1、ZFCDelta1、NumeralCode、NeverRE、OmegaArith、NumeralSemantics、ArithInterp、R0Model、Effective、Soundness、OmegaLaws、PAModel；
  - 自 `../idea-t-c6-p/GodelQ/`：`Turing`、`ZFC/TuringZFC`、`C6Review`。
- **新文件**：
  - `GodelQ/ZFC/ArrivalArith.lean`：算术层；
  - `GodelQ/ZFC/ArrivalZFC.lean`：𝗭𝗙𝗖 层；
  - `GodelQ/ZFC/QualificationArrival.lean`：命题对照；
  - `GodelQ/Negative/` 下的两个负控制。
- `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`：固定的 Lean 文件与导入闭包的逐模块哈希。
