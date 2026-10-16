# GLM 线的修复件：C02 忠实版、三个修复/近失负控制（审计项 D1/Q7）

> 2026-09-27；Cloud-Opus 审计会话。GLM 原包与原收据**不改**（哈希锁定）；修复件单独成包、单独收据。
> - `MP-COPUS-GLM-FIX-001`（`IotaC02Faithful.agda`）：claims COPUS-GLM-FIX-C02a、COPUS-GLM-FIX-C02b。
> - 负控制：`MP-COPUS-GLM-FIX-NEG-001`（`GroupoidNegFixed.agda`）、`-NEG-002`（`GroupoidNegTrivialLoop.agda`）、`-NEG-003`（`IotaC03NegTrivialInterp.agda`）。

## 1. C02 的声明层↔证明层断裂及修复

- GLM 的声明：标准解释把 ι 路径构造子**定义性地**送到 refl（"真实等式是事实"）。
- GLM 的形式见证：`valReflT : (t s : Tm) → Path (Path Bool (val (cond (lit true) t s)) (val t)) refl refl`——类型里**没有** `betaT`；只要两端定义性相等，`refl ≡ refl` 恒成立。
- **COPUS-GLM-FIX-C02a**（忠实版）：`valBetaT-refl : (t s : Tm) → cong val (betaT t s) ≡ refl`、`valBetaF-refl`，证明均为 `refl`。
- **COPUS-GLM-FIX-C02b**（断裂的机器演示）：GLM 的陈述形式在**人工等式** `art`（其解释是 ua not ≠ refl）处同样成立——`glmFormHoldsAtArt : Path (Path Type (f boolTy) (f boolTy)) refl refl`；而忠实形式在 `art` 处被驳斥——`faithfulFormFailsAtArt : ¬ (cong f art ≡ refl)`。结论：原见证不能区分真实与人工等式，忠实版可以。

## 2. 负控制

| id | 文件 | 预期拒绝理由 | 意义 |
|---|---|---|---|
| NEG-001 | `GroupoidNegFixed.agda` | `false != true`（a(tt,tt)=(ff,tt)） | GLM 原负控制 `WrongGroupoidWitness.agda` 因 `true` 未导入而在**作用域检查**阶段失败（其自有收据 stdout 即为 `[NotInScope] true`），从未检验它声称的算术；本文件补上导入后按原意被拒 |
| NEG-002 | `GroupoidNegTrivialLoop.agda` | `true != false`（链终点变为 (tt,tt)） | GLM 的 τ≠refl 脚本逐字作用于恒等等价的环：被拒，说明非平凡性确实依赖 a 移动 (tt,tt) |
| NEG-003 | `IotaC03NegTrivialInterp.agda` | `Bool != primGlue …`（cong f′ art = refl） | GLM 的 ¬isSetTmA 脚本逐字作用于把 art 解释为常路径的 f′：被拒，说明 C03 依赖人工等式的非平凡解释（GLM 原负控制只检验 art 与 refl 不定义性相等） |

## 3. 禁止外推

- 修复件不改变 GLM-R1-C01/C03、GLM-R3-C01 的形式命题真值；它们修的是**声明读法与证据的对应**。
- C02 忠实版仍只覆盖一阶 ι 玩具片段（Tm ≃ Bool）。
