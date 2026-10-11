import GodelQ.ZFC.CG008Probe11

/-!
# CG-008 · 缺口的最终形状（本轮定型的完整陈述）

本文件把 CG-008 的缺口**逐字固定**下来，供后续工作单元直接接手。
所有条目都是机器检查过的（`rc=0`），但**不构成 D3 的证明**。

## 缺口的六步等价链

**第 1 步**：缺口原形（`Z0Blocked.lean:61-65`）

```
Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V) →
Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V)
```

**第 2 步**：归约到内部演算形状（`CG008Reduce.lean`）
—— `Provable 𝗭𝗙𝗖 (⌜σ⌝ : V) ⟺ 𝗭𝗙𝗖.internalize V ⊢ ⌜σ⌝`。

**第 3 步**：`zfcTr τ` 展开（`Z0Full.lean:40,65`）
—— `zfcTr σ = trProv.val/[⌜σ⌝]`，
`trProv = .mkSigma “x. ∃ y, !iTDef y 0 x ∧ !(provable 𝗭𝗙𝗖) y”`。

**第 4 步**：`iT_quote`（`InternalTranslate.lean:611`）把 `iTDef` 消掉
—— 结论句的算术核是 `provabilityPred 𝗭𝗙𝗖 (translate τ)`。

**第 5 步**：因此缺口 = **集合语言的 `provable_internalize`**（`CG008Probe9.lean`）

```
Provable 𝗭𝗙𝗖 (⌜translate τ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜translate (provabilityPred 𝗭𝗙𝗖 (translate τ))⌝ : V)
```

与算术版 `D3.lean:175` **逐字同形**，只差 `T : ArithmeticTheory` → `T = 𝗭𝗙𝗖 : Theory ℒₛₑₜ`。

**第 6 步**：V 内部对 `Derivation` 的完全性（`CG008Probe10.lean`）
—— `Provable 𝗭𝗙𝗖 ψ` 展开是 `∃ d : V, Proof 𝗭𝗙𝗖 d ψ`；
要跨到编码层的 `provable 𝗭𝗙𝗖 ⌜ψ⌝`，需要 V 内部证明
「`d` 是推导 ⟹ 结论可证」。

## 为什么不是循环（纠一处误诊）

`Z0Blocked.lean` 文档第 16-18 行说 `zfcTr_D3_syntactic`（`translate τ 🡒 translate (zfcTr τ)`）
不是 ZFC 定理——**那是对的，但说的不是缺口**。

缺口的前提是「V 内部**有一条推导**」（`Provable`），不是「该句为真」。
从「推导存在」到「可证性句可证」是 **Σ₁ 完全性**，不是**反射原理**。
这个区分是缺口不循环的原因。

## 为什么算术版搬不过来

| 环节 | 算术版 | 集合版 |
|---|---|---|
| `sigma_one_complete` | ✅ 有（`D3.lean:170`） | ❌ 无（`T` 须 `ArithmeticTheory`） |
| `bold_sigma_one_complete` 的 `P` | 用 `toNumVec w ⤔ ⌜φ⌝` 把自由变量的值**命名成数字项** | ❌ `ℒₛₑₜ` **无常项与函数符号**（`IsEmpty ((ℒₛₑₜ).Func 0)`） |
| `term_complete` | ✅ 有（`D3.lean:45`，项求值完全性） | ❌ 无（集合项只有 `bvar`/`fvar`） |
| `ball_intro` | 需把 `< n` 展开成有限析取 | ✅ 真量词，本轮已建（`set_ball_intro`） |
| `SoundOnHierarchy` 桥（`Absoluteness.lean:121-152`） | 前提含 `[T.SoundOnHierarchy 𝚺 1]` | ❌ 定义在 `ArithmeticTheory` 上；且那是**反方向**（真⟹可证，靠可靠性） |
| V 内部对 `Derivation` 的归纳 | —— | ❌ `Fixpoint.induction`（`HFS/Fixpoint.lean:283`）是**元层**引理 |

## 本轮已建成的工具（全部 `rc=0`，过禁用标记检查）

**typed 层**（`ZFCSetInternal.lean` 13 条 + `CG008SetAll.lean` 4 条）：
`set_eq_refl`、`set_eq_symm`、`set_ne_symm`、`set_eq_uniform_trans`、`set_eq_trans`、
`set_subst_eq`、`set_subst_mem`、`set_K_intro`、`set_A_intro_left`、`set_A_intro_right`、
`set_exs_intro`、`set_all_intro`、`set_all_elim`、`set_ball_intro`、`set_mem_of_eq`，
加引号求值辅助 `eval_quote_mem`、`eval_quote_eq`。

**编码层**（`CG008Raw.lean` 2 条桥 + `CG008RawSigma1.lean` 14 条）：
`internal_derivable_of_tprovable`、`tprovable_of_internal_derivable`，
以及全部 `d_*` 下沉版本。

**归约**（`CG008Reduce.lean` 4 条）：`provable_iff_internal`、
`zfcTr_D3_internalize_iff_internal`、`zfcTr_D3_internalize_of_internal`、
`zfc_z0_full_of_internal`。

## 下一步

在编码层（`Derivable`）试 V 内部对 `Derivation` 的完全性——
`Derivable` 层没有「自由变量」概念（`CG008Raw.lean` 的发现），
所以算术版的 `toNumVec` 障碍在那里可能不存在。
`CG008RawSigma1.lean` 的 14 条 `d_*` 已是该层的工具集。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
- **不声称 D3 已证**；`Z0Blocked.lean` 的未证标记仍在。
-/

-- 本文件是记录文件（无定理）。导入 `CG008Probe11` 以确保本文件之前的整条链都编译。
--
-- 缺口原型的**类型**见 `Z0Blocked.lean:61-65`（那里带未证标记，故本文件不导入它，
-- 以保持本文件可进收据）。

