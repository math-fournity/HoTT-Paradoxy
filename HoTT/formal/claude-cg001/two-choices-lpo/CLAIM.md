# CG001-C-418 至 C-421：两次选择是同一条原则；A 的结果机器交不出；芝诺的极限用不着 A

> **证明包**：`MP-CG001-TWO-CHOICES-LPO-001`（`GodelQ/TwoChoices/QualificationTC.lean`）；负控制 `MP-CG001-TWO-CHOICES-LPO-NEG-001` 至 `-NEG-003`。
>
> **目标包**：CG-007（`.claude/goals/CG-007-formalization-completion/`），W8 之后的单元，承接研究发起人 2026-10-14 的新表述。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-14；独立 worktree `claude/012-opus-w8`。
>
> **理论变体**：Lean 4（v4.34.0）内核。
> - `GodelQ/TwoChoices/Core.lean` 只用 Lean 内核，不导入 Mathlib。它的定理经机器审计不依赖 `Classical.choice`，只用 `propext` 与 `Quot.sound`，有两条不依赖任何公理。
> - `Machines.lean`、`Rational.lean` 用 Mathlib（`5ed29652`），是经典的。
> - 不涉及 HoTT 路径。
>
> **身份**：四条都是机器证明，范围见 §2 与 §8。“放弃 ASK”“选择 A”“两次选择”是研究发起人的话；把它们对应到 LPO 与 `LimBit`、`NatBMC`，是 AI 的读法（§3）。

## 0. 这一条在研究里的位置

研究发起人 2026-10-14 的原话（逐字节选，全文见 `.claude/思考与发现/CN-078`）：

- “ZFC缺的Q，是一种对数学理论M的观察力，这种观察力就是对某种存在于理论M中的表述L是否是“可计算的、可停机的”的判断。”
- “一种表述是不可停机的，另外一种表述是可停机的，这两种表述在ZFC那里，在是否可停机这个观察角度上，不存在辨别力。”
- “ZFC放弃了这种观察力，得到了A型数学便利，并同时异化为了ZFC-1=ZFC+A。放弃是一次选择，而A是第二次选择。A是什么？A就是一个无限的步骤才能到达，从而存在的结果，当作已经存在的结果，参与运算。”
- “ZFC-1对现实的否定，与其说在于Q，不如说在于A。”
- “ZFC-1这个反现实的逻辑，不仅仅在现实中是无法完成A的，而且在思维中，必然产生我们重新复活和新找到的悖论。”

本包回答其中三个可以机器检查的问题：
1. 两次选择（放弃 Q；选择 A）在数学上是什么关系？
2. A 断言其存在的结果，机器交不交得出？
3. 芝诺的极限 1 用不用得着 A？

## 1. 记号

- **ω 追问** `OmegaQ := ℕ → Bool`：第 `k` 步回答“落定了吗”。它与 `same-q-univalent` 的 `OmegaQ` 同型（C-112、C-113）。
- **LPO**（有限全知原理）：`∀ q : OmegaQ, (∀ k, q k = false) ∨ (∃ k, q k = true)`。每个 ω 追问要么永远答“否”，要么某一步答“是”。
- **落定**：`SettlesAt s N := ∀ m, N ≤ m → s m = s N`，即第 `N` 步之后值不再变。
- **A 的两种形态**：
  - `LimBit`：每个单调开关序列（`MonoBits`：一旦为真，此后都为真）都有落定的一步；
  - `NatBMC`：每个有界单调的自然数序列都有落定的一步。
- **“到这一问为止见过‘是’吗”**：`seen q n`。
- **芝诺读数**：`zenoReading k n := 2ᵏ - 2^(k-n)`（自然数减法），即第 `n` 步的位置 `1 - 2⁻ⁿ` 在精度 `2⁻ᵏ` 上的读数。
- **芝诺位置**：`zenoQ n := 1 - (1/2)ⁿ : ℚ`。柯西性 `CauchyQ`：每个精度 `1/(k+1)` 都有一步，此后两两相差小于它。
- **停机搜索的开关**：`haltBits e k := decide (DoneBy e k)`，即“程序 `e` 到第 `k` 步停了吗”。`Process`、`Done`、`DoneBy` 同 `../godel-q/CLAIM.md` §1。

## 2. 精确命题（类型逐字见 `GodelQ/TwoChoices/QualificationTC.lean`）

| 编号 | 定理 | 内容 | 公理 |
|---|---|---|---|
| CG001-C-418 | `qual_C418` | (1) `LimBit ↔ LPO`；(2) `NatBMC ↔ LPO`；(3) 去掉“有界”，“每个单调自然数序列都有落定的一步”不成立（`x n = n`） | 只有 `propext`、`Quot.sound`；**不依赖 `Classical.choice`**（机器审计） |
| CG001-C-419 | `qual_C419` | 芝诺读数在精度 `2⁻ᵏ` 上于第 `k` 步落定（公式，不是搜索）；落定后的读数加 1 等于 `2ᵏ`；每一步的读数都小于 `2ᵏ`；读数单调 | 同上，不依赖 `Classical.choice` |
| CG001-C-419（桥） | `qual_C419_bridge` | `zenoReading k n = ⌊2ᵏ · zenoQ n⌋`；`zenoQ` 单调，每一步都小于 1；从第 `k` 步起离 1 不超过 `(1/2)ᵏ`；柯西步由公式 `k + 1` 给出 | 经典（Mathlib 的 ℚ 本身依赖 `Classical.choice`） |
| CG001-C-420 | `qual_C420` | 每个停机搜索的开关都单调，在经典逻辑里都有落定的一步；可是不存在可计算的 `F`，对每个程序交出落定的一步；也不存在可计算的 `f`，交出终值 | 经典（Mathlib 的停机定理） |
| CG001-C-421 | `qual_C421` | (1) 在经典逻辑里 LPO 是定理（来自排中律）；(2) 每个“会停”的陈述都有现成的真假；(3) 会停的程序组成一个集合，偶数也组成一个集合；(4) 偶数可判定，停机不可判定 | 经典 |

## 3. 每条承接了原话的哪一部分

**C-418：两次选择**
- 【解释】“放弃 Q（ASK）”落在真假值上，最简单的形态是 LPO：不问判定它的过程停不停，就当每个无限搜索都已经有了答案。
- 【解释】“A”落在对象上，最简单的形态是 `LimBit`（开关序列的终值现成可用），以及 `NatBMC`（有界单调序列的终值现成可用）。它们正是“一个无限的步骤才能到达……的结果，当作已经存在的结果，参与运算”：终值要等无限多步之后才见分晓。
- 【证明】在不预设排中律的底座上，两者互推。证明依赖哪些公理由机器审计核对，见 §4。
- 【判断】所以在这一层，两次选择是同一条原则的两面：选择 A，就已经放弃了 ASK；放弃 ASK，就得到了 A。
- **在经典逻辑里**，LPO 直接来自排中律（C-421 (1)），所以 ZFC 的“缺 Q”不是什么都没说。它用排中律断言了每个搜索“要么停、要么不停”，而这句断言本身就是 A 型的。
- **没有承接**：
  - 互推只到 Σ1 这一层，即最简单的无限搜索和整数刻度的单调序列。ZFC 的全部排中律、全部 A（幂集、实无穷集合、实数的极限）都比这强得多。
  - 实数形态“有界单调的实数列都收敛 ⟺ LPO”是文献结果（§5），本包没有做构造性的机器证明：Mathlib 的 ℚ 本身依赖 `Classical.choice`（审计核对了 `Rat.le_total`）。它由整数刻度形态在每个精度上取地板函数得到，这一步是初等的。
  - 换一个底座，两次选择可以分开：在经典逻辑而集合存在受限的系统里，有排中律而没有单调收敛（文献，§5）。所以“一次还是两次”取决于底座。

**C-419：芝诺的极限用不着 A**
- 【证明】芝诺过程在每个精度上的读数，落定的一步由公式给出（第 `k` 步），不需要搜索，也不需要 LPO。有理数一侧，收敛步也由公式给出（第 `k + 1` 步），极限是 1，每一步都小于 1。
- 【判断】所以在芝诺这里，A 起作用的地方不是“极限等于 1”这个数，而是把“无穷多步走完”当作已经发生的结果，即“在所有步之后的那一刻到了”。这一面已有机器证明：
  - 两种“到了”恰在稠密时分开（C-106）；
  - 时刻 1 不是任何一步（C-108）；
  - 语义 P₁ 在实数轴的每一点都不成立（C-116 (1)(3)）。

**C-420：A 的结果，机器交不出**
- 【证明】每个停机搜索的终值，在经典逻辑里都“存在”。可是没有任何可计算的方法统一交出它落定的那一步，也交不出终值本身。
- 【解释】这是原话“在现实中是无法完成A的”在计算上的精确形态：A 断言其存在的东西，没有哪个有限的机械过程交得出来。
- 这是经典定理（Mathlib 的停机定理）。它说的是“交不出”，不是“不存在”。

**C-421：辨别力不是没有，只是不当门槛用**
- 【证明】在经典逻辑里（Lean 与 ZFC 一样），“会停”和“永不停”都有现成的真假；集合的存在也不过问可计算性。可是同一个理论证得出二者可计算性的差别。
- 【判断】所以“不存在辨别力”要说得精确些：理论里说得出“可不可计算”，但不拿它当承认“存在”“为真”的门槛。这与 KC-000066 的“不是没有，只是没有完备的观察力”一致。

## 4. 公理审计（机器核对）

`QualificationTC.lean` 末尾的 `run_cmd` 用 `Lean.collectAxioms` 逐个核对，违反即报错，编译失败：
1. **构造一侧**：下列 12 个常量都不依赖 `Classical.choice`：
   - `qual_C418`、`qual_C419`；
   - `lpo_of_limBit`、`limBit_of_lpo`、`settles_of_lpo_gap`、`natBMC_of_lpo`、`limBit_of_natBMC`、`unbounded_settling_false`；
   - `zenoReading_settles`、`zenoReading_final`、`zenoReading_lt`、`zenoReading_mono`。
2. **对照一侧**：下列常量必须依赖 `Classical.choice`：`qual_C420`、`qual_C421`、`lpo_classical`、`qual_C419_bridge`，以及 Mathlib 的 `Rat.le_total`。这说明审计不是空的，也说明有理数一侧只能作桥。

负控制 NEG-001 用同一个审计拒绝“借排中律免费得到 LPO”。

**为什么这一条是全部内容**：在经典逻辑里，LPO、`LimBit`、`NatBMC` 都是定理，它们的互推没有内容。内容只在“不用排中律也互推”上，所以审计是证明的一部分。

## 5. 与已有命题和文献的关系

- **C-116 (4) `A_iff_P`**：在理论的接受规则一层，A（接受一切到达）与 P（ω 完成规则）在闭包条件下等价。C-418 是逻辑原则一层的对应：A（关于对象）与 LPO（关于真假值）在构造性底座上等价。
- **C-93**：在永不完成的 ω 追问上，P_fin 被否定。LPO 说的是：每个 ω 追问的结局都已经定了。
- **C-129–C-133**（GPT，`HoTT/formal/cauchy-modulus/`，Cubical Agda）：用同一个表示 `EventuallyConst s = Σ N, ∀ n ≥ N, s n ≡ s N`，讲的是按极限值取商会忘掉落定的那一步。
- **C-106–C-108、C-116 (1)(3)**：两种“到了”。C-419 补上另一面：极限这个数本身是可计算的。
- **C-86、C-104**：停机与图灵路线。C-420 用的是 Mathlib 的停机定理。
- **文献**（没有做查重）：
  - **已核对原文（2026-10-14）**：H. Diener,《Constructive Reverse Mathematics》（arXiv:1804.05495v3，2020 年 4 月，1.3 版）。
    - §1.2：LPO 这个名字是 Bishop 起的。
    - 命题 1.2.1 第 3 项：在 Bishop 式构造性数学里，LPO 等价于“每个有界单调的实数列都收敛”。出处是其文献 [93]：M. Mandelkern, *Limited omniscience and the Bolzano–Weierstrass principle*, Bull. London Math. Soc. 20 (1988), 319–320。
    - 那里的底座带可数选择与依赖选择。本包的证明不用选择。
  - **只经检索确认书目，未读原文**：E. Specker, *Nicht konstruktiv beweisbare Sätze der Analysis*, J. Symbolic Logic 14 (1949), 145–158。它给出一个可计算的单调有界有理数列，极限不可计算。
  - **凭记忆，未核对**：在经典的反推数学里，单调收敛在 RCA₀ 上等价于 ACA₀（Simpson《Subsystems of Second Order Arithmetic》第三章）。

## 6. 负控制

| proof id | 文件 | 被否定的说法 | 预期 |
|---|---|---|---|
| `MP-CG001-TWO-CHOICES-LPO-NEG-001` | `GodelQ/Negative/WrongLPOForFree.lean` | 不选 A，也能在不预设排中律的底座上得到 LPO（借排中律证出，再跑同一个审计） | 拒绝：审计报出 `lpo_for_free` 依赖 `Classical.choice` |
| `MP-CG001-TWO-CHOICES-LPO-NEG-002` | `GodelQ/Negative/WrongSettlingUnbounded.lean` | 有了 LPO，每个单调自然数序列（不要求有界）都有落定的一步（照搬 `settles_of_lpo_gap`） | 拒绝：`omega` 证不出上界 `x n ≤ x 0 + x 0`；正面定理 `unbounded_settling_false` |
| `MP-CG001-TWO-CHOICES-LPO-NEG-003` | `GodelQ/Negative/WrongComputableSettling.lean` | 有一台机器交出每个停机搜索落定的一步（取“一律第 0 步”） | 拒绝：`DoneBy e m ↔ DoneBy e 0` 证不出；正面定理 `no_computable_settling_point` |

## 7. 文件

- **逐字节复制，复制时核对过**：`GodelQ/ProcessObservation.lean`，来自 `../godel-q-zfc-turing/GodelQ/`（SHA-256 `8e80fe39…46db2`）。
- **新文件**：
  - `GodelQ/TwoChoices/Core.lean`：LPO、A 的两种形态与互推，芝诺读数（只用 Lean 内核）；
  - `GodelQ/TwoChoices/Machines.lean`：停机搜索的开关，交不出落定的一步与终值，经典的 LPO 与二值性；
  - `GodelQ/TwoChoices/Rational.lean`：芝诺的有理数一侧与读数对应（经典）；
  - `GodelQ/TwoChoices/QualificationTC.lean`：命题对照与公理审计；
  - `GodelQ/Negative/` 下的三个负控制。
- `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`：固定的 Lean 文件与导入闭包的逐模块哈希。

## 8. 禁止外推

1. 不推出 ZFC ⊢ ⊥，也不说经典数学错了。
2. C-418 的内容是“不用 `Classical.choice` 也互推”。它不是“LPO 在构造性底座上不可证”，那是独立性结果，要用模型，本包没有做。
3. 互推只在 Σ1 这一层。ZFC 的全部排中律、全部 A 都比这强。实数形态的等价是文献结果，本包没有构造性的机器证明。
4. “放弃 ASK = LPO”“A = `LimBit`、`NatBMC`”是 AI 对研究发起人原话的读法，不是定理。
5. C-420 是经典定理，说的是“没有可计算的方法交出落定的一步与终值”，不是“这些结果不存在”。
6. C-419 说的是极限这个数 1 用不着 A。芝诺过程“在第几步走完”仍然没有答案（C-106–C-108，C-116 (1)(3)）。
7. Lean 的 `Prop` 带 `propext` 与 `Quot.sound`。把“不依赖 `Classical.choice`”读作“构造性”，是通常的约定。
8. 数学事实都是已知的（§5）。新的是读法：把研究发起人的“两次选择”落到这对等价上，把“交不出”落到停机定理上。
