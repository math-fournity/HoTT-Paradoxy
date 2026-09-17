# 发射包：Dedekind-Ω 簇三发导弹（第二枚·声明层）

> 方案权威：`Atria的方案/修订片/024`（第二枚规格）+ `025`（三枚齐射结构、
> M2→M3 链式不可倒置、声明层地位）
> 供给来源：`.codex/research/hott/PREMISE-001/008`（SUPPLY-010，F2-7 Dedekind-Ω 簇）
> 门禁：`MATH_PROOF_BEFORE_DELIVERY_V1`（AGENTS.md 项目级）

## 1. 身份

| 字段 | 值 |
|---|---|
| claim id | `CAND-F2-7-M2`（候选锚点；非已注册数学主张） |
| proof id | `MP-DEDEKIND-OMEGA-M2` |
| 目标簇 | F2-7 Dedekind-Ω（实数完备性与 Ω 选择；Book §11.2，`reals.tex:85`） |
| 弹种 | 第二枚·声明层（023 片 §2 / 025 片 §5：交付类型 `Spec_B` 的居住性为空） |
| 状态 | `MACHINE_PROVED_LOCAL_UNCOMMITTED`（核已接受；提交后仍非 VERSION_CLOSED） |
| run | `HoTT/verification/runs/20260917-MP-DEDEKIND-OMEGA-M2-01/`；exit 0；43.9s |
| 工具链 | Agda 2.8.0（`/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64`）+ cubical v0.9；`--safe --cubical --guardedness`；无 LEM、无 resizing、无追加公理 |

## 2. 精确命题（可形式化对照）

主定理（已证、核已接受）：

```agda
√2-irrational : ∀ q → ¬ (q ·ℚ q ≡ 2r)
spec-B-empty  : ¬ (Σ[ q ∈ ℚ ] q ·ℚ q ≡ 2r)
```

其中 `ℚ` = `(ℤ × ℕ₊₁) // _∼_`（`Cubical.Data.Rationals.Base` 的 set quotient），
`_·ℚ_` 为库乘法，`2r = [ pos 2 / 1⁺ ]`。

量词与假设逐项对照：
- 量词：`∀ q : ℚ`——有理数集商上的**全称**命题（非有限枚举）；Σ 形式即
  「交付类型的居住性为空」。
- 假设：纯 Cubical Agda 规则；`--safe`；**不使用** LEM、resizing、AC、unique
  choice 或任何追加公理。ℚ 的 set quotient 与其乘法为库标准构造。
- 语义读法（非命题的一部分）：「输出 √2 的有理位置」这一任务的交付类型
  `Spec_B = Σ (q : ℚ), q·q ≡ 2r` **不可能有居住者**——任何以有理数输出 √2 位置
  的过程都不可能停机交付。这不是「还没停」，是「不可能停」。

## 3. 证明结构与关键引理

1. **ℚ 提取**：`elimProp`（于点构造子定义性归约）取代表元 `(zm, n⁺)`；
   `ℚ·` 经 `rec2` 在点构造子上定义性归约为 `[ (zm·zm , n⁺·₊₁n⁺) ]`；
   `eq/⁻¹`（quotient effectiveness）得同分母关系
   `(zm·zm)·ℤ ℕ₊₁→ℤ 1⁺ ≡ pos 2 ·ℤ pos N`；经 `·IdR`、`abs·`、
   `ℕ₊₁→ℕ-·₊₁` 与 `+-zero` 得 ℕ 方程 `|zm|² ≡ (n·n)+(n·n)`。
2. **奇偶工具包**（自备，~120 行）：`Par/fl/par`；L1（偶+偶=偶）、L6（奇偶形状
   提取）、ev-add（一般偶加法）、L9（偶×任意=偶）、`·-distrib-l/r`、
   `sq-double`（平方膨胀 (a+a)² ≡ 2(2a²)）、**`even-square`（偶平方引理）**、
   `even-inj`（偶和单射）。
3. **强归纳**（手写 `strongℕ`，≤ 的 Σ 编码下直接拆见证）。
4. **无穷下降 `noRoot`**：解 `(p, suc n₀)`（p² = 2n²，n ≥ 1）⟹ 偶平方引理给
   p = k+k；平方膨胀 + 偶和单射给 n² = 2k²；偶平方引理给 n = j+j（j ≥ 1）；
   得更小解 (k, j)，k < p（`k<kk` 非零半减）；与强归纳假设矛盾。

## 4. 禁止外推（交付措辞边界）

- **不**声称这是 HoTT 的内部矛盾，**不**声称 HoTT 不一致（修订片 024 §2 / 025 §6）。
- **不**声称「实数完备性非现实」已被证明；本包只提供 Spec_B 居住性为空的机械锚点。
- **不**声称本命题依赖任何 HoTT 特有规则（univalence / cubical path / HIT）；
  它是 ℚ/ℕ 层的标准计算。
- **不**声称「任何过程不停机」——本命题证的是**交付类型无居住者**；「任何逼近
  策略都不可能交付」是对该事实的语义读法，按
  `ARGUMENT_ANCHORED_ON_MACHINE_PROOVED_FACTS` 标注交付（见 §5）。
- `20260917-…-M2-01` 为本 run 目录；开发期的 26 次编译迭代（接口缓存增量检查）
  未作为独立 run 收据保存——正式 run 为 `--ignore-interfaces` 全量复检
  （exit 0，43.9s），与 M1 的 -04 同一纪律。

## 5. 第二枚的声明层论证（非单一机器定理）

第二枚的完整交付 = 本包的机械锚点 + 以下声明层论证
（`ARGUMENT_ANCHORED_ON_MACHINE_PROOVED_FACTS`，锚 = M1 run + M2 run）：

> 反弹（023 片预先替防守方生成）："实数**就是**这个 cut。`L` 与 `U` 已经构成它，
> 不需要『夹到相遇』。完备性是**定义**出来的。"
> 第二击：该反弹引入的理想元素（实数 = cut 的等价类）**不对应任何把两端夹到
> 相遇的过程完成**——M2 机械地证明确不存在任何有理位置可被交付；M1 证明最优
> 夹钳序列永不闭合。理想元素的「已在」与过程的「不可达」由两条独立收据钉住，
> 其落差即 `PROCESS_DECLARATION_GAP`。
> 加锐（Ω 依赖链，Book §11.2 自陈）：「实数取值命题塌缩到单一 Ω」须假设
> resizing 或 LEM——「实数已完成」的身份逻辑上依赖「命题判定已完成」，
> 两个理想元素相互支撑（025 片 §1.2）。

## 6. falsifier（可被推翻，020 片审计纪律）

- 若存在 q : ℚ 使 `q ·ℚ q ≡ 2r` 可被核接受，则本命题被推翻。
- 若 `ℚ·` 的 rec2 点归约或 `eq/⁻¹` 的库语义被证明与本包的使用方式不符
  （提取链断裂），则「√2 无有理平方」的读法失效（ℕ 层 `noRoot` 命题仍真，
  但与 Dedekind-Ω 簇的连接断裂）。

## 7. 第三枚（识别层）——本包不含

第三枚 = M3-L1 `LEMᵒ → ¬ (Spec_A ≃ Spec_B)` + A 合法性构造（025 片 §3/§5），
**消费本包的 `spec-B-empty`**。序列不可倒置。见
`MissileThreeVerdictCollision.agda`（另行发射登记）。
