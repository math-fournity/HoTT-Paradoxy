# 发射包：Dedekind-Ω 簇第四弹·首靶（M3 去条件化 + 027 §5 待核发现核实）

> 方案权威：`Atria的方案/修订片/027`（收官版）§5（待核发现与债务定位）、§2（身份
> 陈述与主定理模式）、§3.2（哥德尔式打法——对每个理想元素 X 找到必收费命题）
> 门禁：`MATH_PROOF_BEFORE_DELIVERY_V1`

## 1. 身份

| 字段 | 值 |
|---|---|
| claim id | `CAND-F2-7-M3-UNC`（候选锚点；非已注册数学主张） |
| proof id | `MP-DEDEKIND-OMEGA-M3-UNC` |
| 性质 | 027 §5 待核发现的核实 + M3-L1 的去条件化加强（第三弹识别层收据的更强版） |
| 状态 | `KERNEL_ACCEPTED_WITH_SCOPE`（本地已提交；非 VERSION_CLOSED） |
| run | `HoTT/verification/runs/20260917-MP-DEDEKIND-OMEGA-M3-UNC-01/`；exit 0；55.6s |
| 工具链 | Agda 2.8.0 + cubical v0.9；`--safe --cubical --guardedness`；**无 LEM、无 resizing、无任何追加假设** |

## 2. 精确命题（已证、核已接受）

```agda
specA-inhabited-unc : Spec_A          -- 无条件居住（027 §5 待核发现：属实）
M3-L1-unc : ¬ (Spec_A ≃ Spec_B)       -- 识别拒绝去条件化
```

与 M3 条件版的关系：`Spec_A`/`Spec_B` 类型复用自 `MissileThreeVerdictCollision`
（同一类型身份）；条件版 `specA-inhabited : LEMᵒ → Spec_A` 仍真，本包为其**去
条件化加强**——拒绝不再依赖任何经典假设。

## 3. 核实内容与债务定位

- **待核发现核实（027 §5）**：判定表 `f : ℚ → Bool`（`f q ≡ true ↔ q·ℚ q < 2r`）
  **不需要 LEM**——ℚ 的序可构造判定（`_≟_ : (m n : ℚ) → Trichotomy m n`，
  `Cubical.Data.Rationals.Order`），序三分直接定义 f，双向对应逐分支构造
  （eq 支用 `isIrrefl<`、gt 支用 `isAsym<` 消去）。
- **债务定位（027 §5 第二条，同步修正叙事）**：ℚ 层判定可计算（不收费）；
  理想元素本体——把判定表升格为实数层对象、完整 cut——才收费。
  **完成义务在承载层跨界处收费：债务不在数据，在升格。**
- 旧叙事修正：「判定表合法性依赖 LEM」以本包为准作废；Ω 依赖链（Book §11.2）
  的正确落位 = 升格为实数层对象时的收费点，不是判定表本身。

## 4. 禁止外推

- 不声称 HoTT 不一致；不推翻 M3 条件版收据。
- 不声称完整 cut / 实数对象已无条件构造——「升格处收费」目前是语义读法 +
  靶位指引（完整 cut 的无条件/条件构造仍未做，见 027 §3 靶 B 与 §9）。
- 不声称本包给出任何「不可证性」元定理——本包是对象层拒绝收据；不可证性证书
  属于元理论（027 §4 拒证二元性）。

## 5. falsifier

- 若存在 `Spec_A ≃ Spec_B` 的等价（无任何假设）可被核接受，则 M3-L1-unc 被推翻。
- 若 `f` 的定义被证明依赖了隐藏的经典假设（本包声称无假设而实际有），则「判定表
  免费」的核实结论被推翻。
