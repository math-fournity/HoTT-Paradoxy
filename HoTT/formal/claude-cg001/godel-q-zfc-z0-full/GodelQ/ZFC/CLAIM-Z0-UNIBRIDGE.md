# CG001-C-390：Z0 D3 攻坚——宇宙层级障碍清除，`bwd` 归约为一条消去

> **证明包**：`MP-CG001-Z0-UNIBRIDGE-001`。
> **目标包**：CG-007，单元 W8 续（依据 `.claude/goals/CG-007-formalization-completion/W8-下一单元-V内部语法解释定理-规格.md`）。
> **理论变体**：同 `godel-q-zfc-z0-full`。

## 0. 位置与身份

**身份**：机器证明（有范围）。这是 D3 攻坚的**基础设施**，不是 D3 本身。
它做两件事：**清除一个被两轮修订都指出但没人实际处理的前置障碍**，
并把缺口**精确归约**为一条消去。

**它不是阻塞引理，也不触及 `zfcTr_D3_internalize` 的证明。**

## 1. 清除了什么障碍

`Z0Blocked.lean:29` 的目标定理写的是 `{V : Type*}`，而项目里现成的两条桥
（`models_trProv_iff`、`models_zfcTr_iff`，`Z0Full.lean:54` / `:67`）都锁在 `V : Type`。

于是 `rw [models_zfcTr_iff]` 在目标定理的宇宙下**直接失败**（本机实测）：

```
error: Tactic `rewrite` failed: Did not find an occurrence of the pattern
  Semantics.Models.{1, 0} ?V↓[ℒₒᵣ] (↑zfcTr ?σ)
in the target expression
  Semantics.Models.{u_1 + 1, 0} V↓[ℒₒᵣ] (↑zfcTr (↑zfcTr σ))
```

外部复核 AI 在 2026-10-10 的反馈里已经指出这个层级差异（"证明最好绕 `trProvable_quote`，
或先把前两条推广"），但没有机器验证。**本包把它做成机器验证的。**

## 2. 精确命题

`GodelQ/ZFC/Z0UniBridge.lean` 中 `namespace GodelQ.Z0UniBridge` 的两条：

| 名字 | 命题 |
|---|---|
| `models_zfcTr_iff'` | `{V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (σ) : (V ⊧ zfcTr σ) ↔ Provable 𝗭𝗙𝗖 ⌜translate σ⌝` |
| `bwd_of_shcraig_elim` | 给定 `ShCraigElim V`，`bwd` 的结论成立 |

其中 `ShCraigElim V := ∀ σ, Provable Sh.craig ⌜σ⌝ (V) → Provable 𝗭𝗙𝗖 ⌜translate σ⌝ (V)`，
即**唯一剩下的消去**。

## 3. 证明

### 3.1 `models_zfcTr_iff'`

同 `Z0Full.models_zfcTr_iff`，只是不经过 `(V : Type)` 的限制：

```lean
rw [zfcTr_def, ← trProvable_quote]
simp [models_iff]
```

关键在于 `trProvable_quote`（`Z0Full.lean:46`）本身是 `V : Type*` 的，
而 `models_zfcTr_iff` 之所以锁在 `V : Type`，是因为它写成
`(V : Type) [ORingStructure V] ...` 的函数形式（`complete` 的模型量化需要 `Type 0`）。
把参数改成隐式 `{V : Type*}` 后同一条证明照样过。**无新数学。**

### 3.2 `bwd_of_shcraig_elim`

两侧的零件都现成：

- 结论侧 `V ⊧ zfcTr (zfcTr σ)` 经 `models_zfcTr_iff'` 变成
  `Provable 𝗭𝗙𝗖 ⌜translate (zfcTr σ)⌝`；
- 假设侧 `V ⊧ provabilityPred Sh.craig (zfcTr σ)` 经 `models_iff` 变成
  `Provable Sh.craig ⌜zfcTr σ⌝`。

中间的桥就是 `elim`。

## 4. 它没有做什么（诚实边界）

**`ShCraigElim` 没有证明。** 它是 D3 的实质内容：`of_provability`（`LK/Interpretation.lean:443`）
经完备性定理语义地给出 `U ⊢ σ → T ⊢ π.translate σ`，**不产生 V 内部的证明编码**，
所以搬不进非标准 V。本机全量 grep 308 个 Foundation 源文件确认**不存在内化版本**
（`grep -rn "Provable.*translate" --include="*.lean" .` 无输出）。

**因此**：

- 本包**不**推出 `zfcTr_D3_internalize`；
- 本包**不**推出 Z0 的完整形式；
- `C-120` 的影子形式仍是无条件成立的（不受影响）。

## 5. 负控制

`GodelQ/ZFC/WrongZ0UniBridge.lean`：把 `models_zfcTr_iff'` 的层级限制去掉后
断言 `Provable 𝗭𝗙𝗖 ⌜translate σ⌝` 可由 `zfcTr σ` 的**任意**模型满足推出——
内核以类型不匹配拒绝（见 §7 的 run）。

## 6. 运行

- `HoTT/verification/runs/20261011-CG001-Z0-UNIBRIDGE-01/`：
  25 个依赖模块 + `Z0UniBridge.lean`，exit 0，stderr 0 B，
  2 条 `#print axioms` 只有三条标准公理。
- `...-NEG-01/`：加 `WrongZ0UniBridge.lean`，exit 1，内核类型不匹配。

## 7. 对上游修订的影响

本包与 `外部资料/zfcTr-D3-plan-review-3.md` 一致：
D3 攻坚的第 1 层免费、第 2 层缩为一条消去。本包把"第 2 层的入口"从
"还要先处理宇宙层级"变成"只剩一条消去"，**这是本轮唯一的实质推进**。
