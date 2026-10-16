# 发射包：Dedekind-Ω 簇三发导弹（第三枚·识别层）

> 方案权威：`Atria的方案/修订片/025`（三枚齐射结构、Spec_A/Spec_B 双规格、
> M3-L1 引理候选、逼选结构、M2→M3 链式不可倒置）
> 供给侧来源：GLM 独立分析（`GLM/2026-09-17 - 第三枚导弹构思：读出与算出的
> 判定对撞（GLM 独立分析）.md`，已按 025 片 §7 对撞评估采纳）
> 门禁：`MATH_PROOF_BEFORE_DELIVERY_V1`（AGENTS.md 项目级）

## 1. 身份

| 字段 | 值 |
|---|---|
| claim id | `CAND-F2-7-M3`（候选锚点；非已注册数学主张） |
| proof id | `MP-DEDEKIND-OMEGA-M3` |
| 目标簇 | F2-7 Dedekind-Ω（实数完备性与 Ω 选择；Book §11.2，`reals.tex:85`） |
| 弹种 | 第三枚·识别层（025 片 §3：核拒绝「读出 = 算出」的任务同一性） |
| 状态 | `MACHINE_PROVED_LOCAL_UNCOMMITTED`（核已接受；提交后仍非 VERSION_CLOSED） |
| run | `HoTT/verification/runs/20260917-MP-DEDEKIND-OMEGA-M3-01/`；exit 0；55.6s |
| 工具链 | Agda 2.8.0 + cubical v0.9；`--safe --cubical --guardedness`；**LEM 为显式假设**（`LEMᵒ`），无其他追加公理 |

## 2. 精确命题（可形式化对照）

两个主定理（已证、核已接受）：

```agda
-- ① A 合法（数据层；LEM 显式假设）
specA-inhabited : LEMᵒ → Spec_A

-- ③ M3-L1（本枚核心）：核拒绝任务同一性
M3-L1 : LEMᵒ → ¬ (Spec_A ≃ Spec_B)
```

其中：
- `Spec_B = Σ (q : ℚ), q ·ℚ q ≡ 2r`（算出任务的交付类型；M2 已证居住性为空）；
- `Spec_A = Σ (f : ℚ → Bool), ∀ q, (f q ≡ true → q·ℚ q < 2r) × (q·ℚ q < 2r → f q ≡ true)`
  （√2 的判定表作为给定数据；布尔表对应 §11.2 的 Ω ≡ Bool 塌缩读法）；
- `LEMᵒ = (A : Type₀) → isProp A → A ⊎ (A → ⊥)`。

量词与假设逐项对照：
- ①的假设：`LEMᵒ` 为**显式假设**，逐字标注（025 片 §2：Spec_A 的居住性依赖
  LEM——这是 Book §11.2 Ω 依赖链「实数已完成 ⟹ 命题判定已完成」的具体体现，
  不藏在「显然」里）。
- ③的依赖：`M3-L1` 消费第二枚的 `spec-B-empty`（`KERNEL_ACCEPTED_WITH_SCOPE`，
  run `…-M2-01`）——链式序列不可倒置（025 片 §5）。
- 语义读法（非命题的一部分）：理论在实数层按「A=B」工作（「实数就是 cut」、
  「位置已经确定」），而核在 ③ 证明该同一性不成立。这个「当作」不在核里、
  不在任何定理里，只住在前提层（Book §11.2 自陈的 Ω 依赖链接缝）。

## 3. 证明结构

1. `specA-inhabited`：逐点 `lem (q·ℚ q < 2r) (isProp< (q·ℚ q) 2r)` 定义判定表
   `f : ℚ → Bool`；表的双向对应在 LEM 两个析取支上分别构造（inl 支直接交付；
   inr 支由 `true≢false` / `np h` 消去）。
2. `M3-L1`：等价传输——`equivFun eq (specA-inhabited lem) : Spec_B`，与
   `spec-B-empty` 矛盾。核心一次传输 + M2 的空类型引理（025 片 §5 预估的
   短证明，兑现）。

## 4. 禁止外推（交付措辞边界）

- **不**声称这是 HoTT 的内部矛盾，**不**声称 HoTT 不一致，**不**声称爆炸原理
  被点燃（025 片 §6；「炸弹在前提里，不在核里」）。
- **不**声称用户第③件事（A=B）内部可证——M3-L1 恰证明其在最自然判据 J
  （规格类型等价）下被核否定。寻找使 ③ 内部可证的 J 等价于寻找 HoTT(+LEM)
  的不一致性证明——合法的开放前沿，`registers_new_claim: false`，不预设、
  不追逐。
- **不**声称 Spec_A 无条件居住——①是 LEM 条件定理；LEM 的出现本身是
  Ω 依赖链的证据，不是缺陷。
- **不**声称「实数完备性非现实」已被证明；本包提供的是逼选结构的核侧事实：
  `Spec_A`（LEM 下）居住 + `Spec_B` 为空 + `Spec_A ≄ Spec_B`。
- 逼选的「两支都命中」是论证结构（`ARGUMENT_ANCHORED_ON_MACHINE_PROOVED_FACTS`，
  锚 = M1+M2+M3 三条收据 + Book §11.2 逐字定位），不是单一机器定理。

## 5. falsifier（可被推翻，020 片审计纪律）

- 若存在 Spec_A ≃ Spec_B 的等价（LEMᵒ 假设下）可被核接受，则 M3-L1 被推翻。
- 若存在不依赖 LEM 的 Spec_A 居住构造，则「A 的合法性依赖经典叠加」这一定位
  被削弱（Ω 依赖链读法需重新评估）；引理本身仍真。
- 若 Spec_A 的判定表被证明不能代表「实数 = cut」的识别（例如防守方主张判定表
  不足以充当 cut），则识别层的语义读法需修订——此时防守方须给出其认定的
  最小「cut 数据」形态，并说明它为何不被 LEM 判定表覆盖（025 片反弹 4 的
  第二击同步适用）。

## 6. 三枚齐射的完成状态

| 枚 | 层 | 证明包 | run | 状态 |
|---|---|---|---|---|
| 第一枚 | 过程层 | `MP-DEDEKIND-OMEGA-M1`（缝隙永不闭合） | `…-M1-04` | `KERNEL_ACCEPTED_WITH_SCOPE` |
| 第二枚 | 声明层 | `MP-DEDEKIND-OMEGA-M2`（Spec_B 为空） | `…-M2-01` | `KERNEL_ACCEPTED_WITH_SCOPE` |
| 第三枚 | 识别层 | `MP-DEDEKIND-OMEGA-M3`（Spec_A ≄ Spec_B） | `…-M3-01` | `KERNEL_ACCEPTED_WITH_SCOPE` |

齐射结构完整。剩余开放项（025 片 §9 全部继承）：廉价副产品 `decGapAt`/
`noGapWitness` 待跑核；反弹族第二击强度逐例核验；M3 强形式（寻找判据 J）
为开放前沿；外部追溯审计未做；push 未授权。
