# 发射包：Dedekind-Ω 簇双发导弹（第一枚·过程层）

> 方案权威：`Atria的方案/修订片/024 - 从测试击落改为执行击落：交付纪律与第一枚发射记录.md`
> 供给来源：`.codex/research/hott/PREMISE-001/008 - SUPPLY-010 F2 缺口层两问与两枚导弹（Dedekind-Ω 簇）.md`
> 门禁：`MATH_PROOF_BEFORE_DELIVERY_V1`（AGENTS.md 项目级）

## 1. 身份

| 字段 | 值 |
|---|---|
| claim id | `CAND-F2-7-M1`（候选锚点；非已注册数学主张） |
| proof id | `MP-DEDEKIND-OMEGA-M1` |
| 目标簇 | F2-7 Dedekind-Ω（实数完备性与 Ω 选择；Book §11.2，`reals.tex:85`） |
| 弹种 | 第一枚·过程层（023 片 §2 / 修订片 024 §3） |
| 状态 | `MACHINE_PROVED_LOCAL_UNCOMMITTED`（核已接受；已提交到本 repo；未 push、未外部审计） |
| run | `HoTT/verification/runs/20260917-MP-DEDEKIND-OMEGA-M1-04/` |
| 工具链 | Agda 2.8.0 + cubical v0.9；`--safe --cubical --guardedness`；无 LEM、无 resizing、无追加公理 |

## 2. 精确命题（可形式化对照）

设 `pellP/pellQ : ℕ → ℤ` 为互递推

```text
pellP 0     = 1
pellQ 0     = 1
pellP (suc n) = pellP n + 2 · pellQ n
pellQ (suc n) = pellP n + pellQ n
D n          = (pellP n · pellP n) + (- (2 · (pellQ n · pellQ n)))
```

主定理（已证、核已接受）：

```agda
pell-gap-never-closes : (n : ℕ) → (D n ≡ 1r) ⊎ (D n ≡ -1r)
gap-never-zero        : (n : ℕ) → ¬ (D n ≡ pos 0)
```

量词与假设逐项对照：
- 量词：全称于 `n : ℕ`（自然数上的全称命题，非有限枚举）。
- 假设：纯 Cubical Agda 规则；`--safe`；**不使用** LEM、resizing、AC、unique choice
  或任何追加公理；`ℤ` 的环结构由 `Cubical.Algebra.CommRing.Instances.Int` 提供，
  环恒等式由 `Cubical.Tactics.CommRingSolver` 的 `solve! ℤCommRing` 反射求解。
- 语义读法（非命题的一部分）：`pellP n / pellQ n` 是 √2 的最优有理夹钳（连分数
  收敛子），`D n ≡ ±1` 表示该夹钳的判别式在任意步数后都**不为 0**，即夹钳两端
  在 ℚ 上永不相遇——「把 Dedekind cut 两端夹到相遇」这一过程在 ℚ 上不可完成。

## 3. 证明结构与关键引理

1. `D-step-identity : (p q : ℤ) → … ≡ …`——环恒等式
   `(p+2q)² - 2(p+q)² ≡ -(p²-2q²)`，`solve! ℤCommRing`（唯一的非平凡步骤）。
2. `D-step : (n : ℕ) → D (suc n) ≡ - (D n)`——提升到序列。
3. `D-invariant : (n : ℕ) → D n ≡ sign n`——ℕ 归纳 + `D-step`。
4. `sign-shape : (n : ℕ) → (sign n ≡ 1r) ⊎ (sign n ≡ -1r)`——符号分类。
5. `pell-gap-never-closes`——主定理（3 ∘ 4）。
6. `gap-never-zero`——推论，用 `znots`/`injPos`/`posNotnegsuc`
   （**不可用荒模式 `()`：cubical 下 Path 不接受**，见 run -01/-02/-03 轨迹）。

## 4. 禁止外推（交付措辞边界）

- **不**声称这是 HoTT 的内部矛盾，**不**声称 HoTT 不一致（repo 纪律 + 修订片 024 §2）。
- **不**声称「实数完备性非现实」已被证明；本包只提供「该具体过程在 ℚ 上不可完成」
  的机械锚点。
- **不**声称 `∀ q : ℚ, q · q ≠ 2`（全称无理性）已被证明——Pell 不变量只证了
  **这条最优序列**的永不闭合。全称式是第二枚的目标（修订片 024 §4）。
- **不**声称本命题依赖任何 HoTT 特有规则（univalence / cubical path / HIT）；
  它是 `ℤ` 上的环计算，在 cubical 系统中被核接受只说明该工具链可承载它。
- run -01/-02/-03 是被 Gate 使用过的失败 run，按 `HoTT/verification/runs/README.md`
  保留不删；它们证明的是工具链接口事实（`--guardedness` 必需、`¬_` 的导入位置、
  荒模式不可用），不构成数学证据。

## 5. falsifier（可被推翻，020 片审计纪律）

- 若存在一个 `n : ℕ` 使 `D n ≡ pos 0` 可被核接受，则本命题被推翻。
- 若 `pellP/pellQ` 的递推被证明不是 √2 的最优有理夹钳（连分数收敛子），
  则「夹钳」的语义读法失效（命题本身仍为真，但与 Dedekind-Ω 簇的连接断裂）。

## 6. 第二枚（声明层）——本包不含

第二枚的数学锚 = 全称 `¬ (∃ q : ℚ, q · q ≡ 2)`（下降法 / 良基归纳），
规格见修订片 024 §4；其声明层论证（理想元素不对应过程完成）交付时须标注
`ARGUMENT_ANCHORED_ON_MACHINE_PROOVED_FACTS`，不得写成单一机器定理。
