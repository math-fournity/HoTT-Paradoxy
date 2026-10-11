# CG001-C-388：Z0 D3 攻坚第 1 层——`arithTrln.translate` 的语法交换律

> **证明包**：`MP-CG001-Z0-LAYER1-TRANSLATE-COMMUTATION-001`。
> **目标包**：CG-007，单元 W8 第 1 层（依据 `.claude/goals/CG-007-formalization-completion/W8-下一单元-V内部语法解释定理-规格.md` §3 第 1 层）。
> **理论变体**：同 `godel-q-zfc-z0-full`。

## 0. 位置与身份

**身份**：机器证明（有范围）。这是 D3 攻坚计划的**第 1 层**：`arithTrln.translate` 与逻辑运算的语法交换律。
**它不是阻塞引理**，也不触及 `zfcTr_D3_internalize`。

## 1. 精确命题

`GodelQ/ZFC/Z0Layer1.lean` 中 `namespace GodelQ.Z0Layer1` 的七条定理，对任意 `n k : ℕ`：

| 名字 | 命题 |
|---|---|
| `map_and` | `translate (φ ⋏ ψ) = translate φ ⋏ translate ψ` |
| `map_or` | `translate (φ ⋎ ψ) = translate φ ⋎ translate ψ` |
| `map_neg` | `translate (∼φ) = ∼translate φ` |
| `map_all` | `translate (∀¹ φ) = arithTrln.fal (translate φ)` |
| `map_exs` | `translate (∃¹ φ) = arithTrln.exs (translate φ)` |
| `map_rel` | `translate (rel R v) = arithTrln.translateRel R v` |
| `map_nrel` | `translate (nrel R v) = ∼arithTrln.translateRel R v` |

其中 `fal`/`exs` 是 `DirectTranslation` 的相对化量词（`∀¹[emb ▹ domain/[#0]] φ` / `∃¹[…] φ`）。

## 2. 证明

- **命题连接词**：`arithTrln.translate` 是 `→ˡᶜ`（`LogicalConnective.Hom`），其 `HomClass` 实例给出
  `map_and`/`map_or`/`map_neg`/`map_imply`/`map_top`/`map_bot`。所以这三条只是实例投影，**不是新数学**。
- **量词相对化**：Foundation 的 `DirectTranslation.translate_all` / `translate_ex`（`LK/Interpretation.lean:94/97`）
  本身就是 `rfl`。所以这两条也是 `rfl`。
- **原子**：Foundation 的 `DirectTranslation.translate_rel` / `translate_nrel`（同文件 `:88/91`）是 `rfl`。

**结论**：规格 §3 第 1 层列出的"命题连接词 + 量词"部分**全部免费**，Foundation 已机器证完。
规格把这一层列为"纯语法、可独立做独立验收"是对的，但它低估了现成程度：连"做"都不需要。

## 3. 负控制

`GodelQ/ZFC/WrongZ0Layer1Overclaim.lean` 尝试用 `map_all` 推出 D3 的蕴含形状，被内核以**类型不匹配**拒绝：

```
error: Type mismatch
  GodelQ.Z0Layer1.map_all ⊤.all.all
has type
  arithTrln.translate ⊤.all.all = ∀_[arithTrln] arithTrln.translate ⊤.all
but is expected to have type
  𝗜𝚺₁ ⊢ ↑zfcTr σ 🡒 ↑zfcTr (↑zfcTr σ)
```

这钉住一件事实：**第 1 层不含可证性谓词的任何信息**，所以它不可能"顺手"给出 D3。

## 4. 还差什么（第 1 层的剩余部分）

规格 §3 第 1 层还列了 `subst`、`shift`、`free`、`setShift`、`Rew.emb` 五项。
本包**未**证这五项——它们不是 `rfl`，需要真工作。它们是第 2 层 `derivTranslate` 的
`wkRule`/`shiftRule`/`cutRule` 规则所必需。

## 5. 运行

- `HoTT/verification/runs/20261010-CG001-Z0-LAYER1-TRANSLATE-COMMUTATION-01/`：24 个依赖模块 +
  `Z0Layer1.lean`（25 个源），exit 0，stderr 0 B，7 条 `#print axioms` 只有三条标准公理。
- `...-NEG-01/`：加 `WrongZ0Layer1Overclaim.lean`，exit 1，内核类型不匹配。
