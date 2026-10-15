# CG001-C-425：两次选择的有理数形态——有界单调的有理数列都收敛 ⟺ LPO（构造性）

> **证明包**：`MP-CG001-TWO-CHOICES-RATIONAL-001`（`GodelQ/TwoChoices/QualificationRational.lean`）；负控制 `MP-CG001-TWO-CHOICES-RATIONAL-NEG-001`、`-NEG-002`。
>
> **目标包**：CG-010（worktree `claude/012-opus-w8`）R3。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-15。
>
> **理论变体**：Lean 4（v4.34.0）内核。有理数是包内自写的整数对。导入 Mathlib 只为用 `ring` 策略（`Mathlib.Tactic.Ring`）。不涉及 HoTT 路径。
> - 本包定理由公理审计机器断言不依赖 `Classical.choice`，实际用到的内核公理是 `propext`、`Quot.sound`。
> - `ring` 在 ℤ 上只用 `propext`，2026-10-14 已探测。
>
> **身份**：机器证明，范围见 §2、§8。

## 0. 这一条在研究里的位置

- 研究发起人 2026-10-14【原话】：“放弃是一次选择，而A是第二次选择。A是什么？A就是一个无限的步骤才能到达，从而存在的结果，当作已经存在的结果，参与运算。”（`dev-notes/0118` 第 10 轮）
- C-418（`../two-choices-lpo/`）在整数刻度上证明了两次选择互推，并写明了它的局限：
  - 实数形态的等价只是文献结果，没有构造性的机器证明；
  - 原因是 Mathlib 的 ℚ 本身依赖 `Classical.choice`，审计核对过 `Rat.le_total`。
  
  `形式化追踪/README.md` 缺口表第 12 行记着这个缺口，本包补上。
- 读法：“两次选择在最简一层是同一原则”是 Claude 的读法（CN-078），待研究发起人确认（CG-010 D5）。

## 1. 记号

- `Qp := Int × Nat`：`(a, b)` 表示 a/b。用到时都要求 b > 0。
- 比较用交叉相乘：`QLe p q := a·b' ≤ a'·b`；`QLt` 同样写法，取严格小于。
- `CloseQ c p q`：|p − q| < 1/c，即 `c·(a·b' − a'·b) < b·b'`，且反过来的差也一样。
- 数列的性质：
  - `MonoQ`：单调；
  - `BoundedQ`：有上界；
  - `CauchyQ x := ∀k ∃N ∀m n ≥ N, CloseQ (k+1) (x m) (x n)`：柯西，取命题层的存在，不给出模的函数。
- `BMCQ`：每个有界单调、分母为正的有理数列都满足 `CauchyQ`。这是 A 的“单调有界必有极限”形态（有理数刻度）。
- 证明用到的构件：
  - `flr c p := (c·a) / b`：精度 1/c 上的整数读数。分母为正时，`Int` 的带余除法就是取整。
  - `bitQ s n`：把开关 `s n` 看成 0 或 1，分母取 1。
  - `zenoQp n := (2ⁿ − 1, 2ⁿ)`：芝诺跑者第 n 步后的位置 1 − 2⁻ⁿ。
- `LPO`、`LimBit`、`MonoNat`、`NatBMC`：同 C-418，`GodelQ/TwoChoices/Core.lean` 逐字节复制。

## 2. 精确命题（类型逐字见 `GodelQ/TwoChoices/QualificationRational.lean`）

| 编号 | 定理 | 内容 |
|---|---|---|
| CG001-C-425 | `qual_C425` | (1) `BMCQ ↔ LPO`；(2) `BMCQ ↔ LimBit`；(3) 芝诺位置的分母都为正；(4) 它单调；(5) 有上界（1）；(6) 每一步都小于 1；(7) 从第 k + 1 步起两两相差小于 1/(k+1)，即柯西步由公式给出；(8) 从第 k + 1 步起离 1 小于 1/(k+1)，即极限是 1，步数由公式给出；(9) 柯西步不能一律取第 0 步 |

公理审计（`QualificationRational.lean` 末尾的 `run_cmd`，违反则编译失败）分两组：
- **构造性一组**：`qual_C425` 及其 14 个组成定理都不依赖 `Classical.choice`。实际公理是 `propext` 与 `Quot.sound`；`zeno_modulus_zero_false` 只用 `propext`。
- **对照一组**：借排中律证出的 `bmcQ_classical`，以及 `Classical.em` 本身，确实依赖 `Classical.choice`。这说明审计不是空的。

## 3. 证明思路

- **LPO ⟹ BMCQ**（`bmcQ_of_lpo`）。给定精度 1/(k+1)，按下面四步：
  1. 取整数读数 ⌊(k+1)·xₙ⌋。数列单调，读数也单调（`flr_mono`）；数列有界，读数也有界。
  2. 减去第 0 项的读数，落到自然数。
  3. 用 C-418 的整数刻度定理 `natBMC_of_lpo` 得到落定的一步 N。
  4. 读数相同的两项相差小于 1/(k+1)（`close_of_flr_eq`）。
  
  LPO 只在第 3 步用到，每精度用有限次。
- **BMCQ ⟹ LPO**（`limBit_of_bmcQ`、`lpo_of_bmcQ`）：
  1. 把单调开关序列看成 0/1 的有理数列，取精度 1（k = 0）的柯西步 N。
  2. 此后相邻两项相差小于 1，0/1 值只能相等，所以开关在第 N 步落定（`LimBit`）。
  3. 再用 C-418 的 `lpo_of_limBit`。
- **芝诺对照**：位置 (2ⁿ − 1)/2ⁿ。
  - 两项之差交叉相乘后是 2ᵐ − 2ⁿ。
  - n ≥ k + 1 时 2ⁿ > k + 1（`two_pow_gt`），由此得 (7)(8)，步数就是 k + 1，不搜索，不用 LPO。
  - (9)：精度 1/2 时，第 0 步的位置是 0，第 2 步是 3/4，相差 3/4，所以步数不能一律取 0。

## 4. 承接了原话的哪一部分

- 【证明】(1)(2)：在不预设排中律的底座上，承认“每个有界单调的有理数列都收敛”，与“每个无限搜索停不停已经定了”（LPO）互推。
- 【判断】对应关系如下：
  - 单调收敛定理把单调有界数列的极限当作现成可用的东西，拿去运算。这正是研究发起人说的 A：“一个无限的步骤才能到达，从而存在的结果，当作已经存在的结果，参与运算”。
  - LPO 是“放弃 ASK”落在真假值上的形态。
  - 因此 C-425 是 CN-078 那条读法在实数形态上的机器核证：两次选择在这一层是同一原则。读法本身待研究发起人确认。
- 【证明】(3)–(9)：芝诺的极限 1 用不着 A，步数由公式给出；(9) 说明这个公式是实质内容，不是摆设。
- 【判断】
  - 所以 A 的分量不在“极限”这个数上，而在把一般单调过程的终点当作现成。一般过程的终点，机器交不出（C-420；文献：Specker 1949）。
  - 芝诺的“走完”与极限的“到了”仍是两件事：走完是在某一步余量为零，到了是所有步之后那一刻。见 C-106–C-108、C-423。
- **没有承接**：
  - **实数类型**：本包只用有理数列与柯西形态，没有构造实数类型（柯西列按“相差趋于 0”取商），也没有证明极限唯一之类的实数论命题。
  - **模的函数**：柯西步是命题层的存在，不是模的函数。有可数选择时，前者给出后者，于是得到一个 Bishop 实数；本包的底座不带选择。
  - **𝗭𝗙𝗖**：本包说的是不预设排中律的底座。在经典逻辑里，`BMCQ` 是定理（`bmcQ_classical`，来自排中律）。

## 5. 与已有命题和文献的关系

- **C-418**：整数刻度的两种形态。本包复用它的 `natBMC_of_lpo` 与 `lpo_of_limBit`（`Core.lean` 逐字节复制）。
- **C-419**：原来的有理数桥用 Mathlib 的 ℚ，是经典的。本包 (3)–(8) 是同样的内容，换成自写的有理数，构造性。
- **C-420、C-421**：A 的结果机器交不出；经典逻辑不拿可计算性当门槛。
- **文献**（没有做查重）：
  - **已核对原文（2026-10-14，见 C-418 的 `CLAIM.md` §5）**：H. Diener，《Constructive Reverse Mathematics》（arXiv:1804.05495v3）命题 1.2.1 第 3 项：在 Bishop 式构造性数学里，LPO 等价于“每个有界单调的实数列都收敛”。出处是 M. Mandelkern, Bull. London Math. Soc. 20 (1988)。
    - 那里的底座带可数选择与依赖选择，对象是实数列。
    - 本包的对象是有理数列，取柯西形态，不用选择。
    - 两者没有逐字比对。
  - **只经检索确认书目，未读原文**：E. Specker, J. Symbolic Logic 14 (1949)。它给出一个可计算的单调有界有理数列，其极限不可计算。

## 6. 负控制

| proof id | 文件 | 被否定的说法 | 预期 |
|---|---|---|---|
| `MP-CG001-TWO-CHOICES-RATIONAL-NEG-001` | `GodelQ/Negative/WrongBMCQForFree.lean` | 不选 A 也不加 LPO，就能在不预设排中律的底座上得到 `BMCQ`（借排中律证出，再跑同一个审计） | 拒绝：审计报出 `bmcQ_for_free` 依赖 `Classical.choice` |
| `MP-CG001-TWO-CHOICES-RATIONAL-NEG-002` | `GodelQ/Negative/WrongZenoModulus.lean` | 芝诺位置的柯西步与精度无关，一律取第 0 步（照搬 `zenoQp_cauchy`，把步数换成 0） | 拒绝：`omega` 证不出 `k + 1 ≤ m`；正面定理 `zenoQp_cauchy`、`zeno_modulus_zero_false` |

## 7. 文件

- **逐字节复制，复制时核对过**：`GodelQ/TwoChoices/Core.lean`，来自 `../two-choices-lpo/GodelQ/TwoChoices/`（SHA-256 `c79458be…a36a`）。
- **新文件**：
  - `GodelQ/TwoChoices/RationalConstructive.lean`：自写的有理数，`BMCQ ↔ LPO`，芝诺对照；
  - `GodelQ/TwoChoices/QualificationRational.lean`：命题对照与公理审计；
  - `GodelQ/Negative/` 下的两个负控制。
- `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`：固定的 Lean 文件与导入闭包（1,180 个模块）的逐模块哈希。

## 8. 禁止外推

1. 不推出 ZFC ⊢ ⊥，也不说经典数学错了。
2. C-425 的内容是“不用 `Classical.choice` 也互推”。它不是“`BMCQ` 在构造性底座上不可证”；那是独立性结果，要用模型，本包没有做。
3. “构造性”在这里指内核公理至多是 `propext` 与 `Quot.sound`（Lean 的 Prop 非直谓、证明无关），不是在 Bishop 的 BISH 或 Heyting 算术里证的。
4. “A = `BMCQ`、`LimBit`、`NatBMC`”“放弃 ASK = LPO”是 AI 对研究发起人原话的读法，不是定理。
5. 只做了有理数列与柯西形态，见 §4“没有承接”。
6. 芝诺对照说的是极限这个数用不着 A。芝诺过程“在第几步走完”仍然没有答案（C-106–C-108、C-423）。
