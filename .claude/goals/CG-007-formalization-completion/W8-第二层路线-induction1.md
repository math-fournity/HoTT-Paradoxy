# CG-007 · W8 第二层路线：把 `ShCraigElim` 落到 `Derivation.induction1` 上

> 状态：`LAYER2_ROUTE_SPECIFIED`。**`ShCraigElim` 仍未证。**
> 本文记录 2026-10-11 本机实测确认的**完整零件清单**与**精确卡点**，
> 使下一个工作单元不必重新发现它们。
>
> 所有标 **[实测]** 的条目都有本机 Lean 4.34.0 + Foundation `1fb01b72` 运行支撑。

---

## 1. 要证什么（一句话）

```lean
abbrev ShCraigElim (V : Type*) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] : Prop :=
  ∀ (σ : ArithmeticSentence),
    Provable Sh.craig (⌜σ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)
```

`Provable Sh.craig ⌜σ⌝` 展开为 `∃ d, Proof Sh.craig d ⌜σ⌝`——V 中存在一条推导编码 `d`。
`d` 在非标准 V 中可能是非标准推导，所以**必须对 `d` 做 V 内归纳**，
逐条规则把它翻成 `𝗭𝗙𝗖` 推导。这正是 Foundation 的 `of_provability` 语义地做掉、
却搬不进非标准 V 的那一步。

---

## 2. 零件清单（全部本机实测可用）

### 2.1 归纳原理 —— 路径的入口

| 零件 | 位置 | 说明 |
|---|---|---|
| `Derivation.induction1` | `Proof/Basic.lean:642` | **[实测]** 对 `Derivation T d` 做归纳，**逐条给出 10 条规则的假设** |
| `Derivation.of_ss` | `Proof/Basic.lean:756` | **[实测]** 同一归纳的**完整使用范例**（跨理论弱化），逐规则消去 10 条 |

`induction1` 的假设正好是 10 条规则（顺序与 `blueprint` 一致）：

```
hAxL, hVerumIntro, hAnd, hOr, hAll, hExs, hWk, hShift, hCut, hRoot
```

**`hRoot` 是唯一用到 `T.Δ₁Class` 的支**——也就是唯一用 `Sh.craig` 公理的地方。

### 2.2 谓词必须是 Σ1

`induction1` 要求 `hP : Γᴬ_[1]-Predicate P`。本机实测确认：

| 谓词 | 状态 |
|---|---|
| `Derivable T` | **[实测]** `{ Γ := 𝚺, rank := 1 }-Predicate` |
| `Provable T` | **[实测]** `{ Γ := 𝚺, rank := 1 }-Predicate` |
| `derivable T : Semisentence 1` | **[实测]** 可直接用作公式基底 |
| `provable T : Semisentence 1` | **[实测]** 同上 |

### 2.3 sequent 翻译 —— 已有

| 零件 | 状态 |
|---|---|
| `translateSeq : V → V` | **[实测]** `SeqTranslate.lean` 已证 |
| `translateSeq.definable` | **[实测]** `𝚺ᴬ₁-Function₁[V]` |
| `translateSeq_insert` | **[实测]** `translateSeq (insert x s) = insert (iT 0 x) (translateSeq s)` |
| `translateSeq_mono` | **[实测]** 单调性 |
| `mem_translateSeq_iff` | **[实测]** `y ∈ translateSeq s ↔ ∃ x ∈ s, y = iT 0 x` |

---

## 3. 建议的证明形状

```lean
-- 谓词：d 的结论 sequent 翻译后 𝗭𝗙𝗖 可导
P d := Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))

-- 用 induction1 逐规则消去：
apply Derivation.induction1 𝚺 (hP := ?_) hd
-- 10 个支：
--   hAxL        : 直接翻译（translate 保持 ∼）
--   hVerumIntro : 直接翻译（translate ⊤ = ⊤）
--   hAnd/hOr    : 用 translateSeq_insert + 相应的 𝗭𝗙𝗖 规则
--   hAll/hExs   : 需要 iT 与 setShift / substs1 的相容（**未证**）
--   hWk         : translateSeq_mono
--   hShift      : 需要 iT 与 setShift 的相容（**未证**）
--   hCut        : 直接翻译
--   hRoot       : 用 Sh.craig 公理的结构（ρ.padding k，ρ ∈ Sh）
```

---

## 4. 精确卡点（本机实测）

### 4.1 `definability` 战术在复合谓词上卡住，但 `via` + `.mk` 可行

**症状**：任何"复合"谓词（如 `Provable 𝗭𝗙𝗖 ∘ translateSeq`）交给 `definability` 都报

```
error: typeclass instance problem is stuck
  Tarski.Structure ?m.12 V
```

**已试无效**：显式写 `(L := ℒₛₑₜ)`、用 `@` 形式给全部参数、先 `#synth` 再传、`definability` 各变体。

**本机实测可行的模式**（照 `Z0Full.lean:44` 的 `trProv_defined`）：

```lean
-- 单层谓词：via + .mk
example : { Γ := 𝚺, rank := 1 }-Predicate (Provable (L := ℒₛₑₜ) 𝗭𝗙𝗖 : V → Prop)
    via FFL.FirstOrder.Arithmetic.Bootstrapping.provable 𝗭𝗙𝗖 :=
  .mk fun v => by simp                    -- [实测] exit 0

-- 复合谓词：手写显式 Semisentence，再 via + .mk
noncomputable def provTransSeqDef : { Γ := 𝚺, rank := 1 }.Semisentence 1 := .mkSigma
  “s. ∃ y, !(translateSeqGraph (V := V)) y s ∧ !(provable 𝗭𝗙𝗖) y”

example : { Γ := 𝚺, rank := 1 }-Predicate
    (fun s : V => Provable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s))
    via provTransSeqDef (V := V) :=
  .mk fun v => by simp [provTransSeqDef]   -- [实测] 结构正确，剩 simp 展开
```

**结论**：这不是数学障碍，是 tactic 深度问题。**用显式 `Semisentence` + `.mk`，不要靠 `definability`。**

### 4.2 谓词必须用 `Provable` 而不是 `Derivable`（当目标是 𝗭𝗙𝗖 时）

**[实测]** `Provable (L := ℒₛₑₜ) 𝗭𝗙𝗖 : V → Prop` 可以直接构造成
`{ Γ := 𝚺, rank := 1 }-Predicate`（`via provable 𝗭𝗙𝗖`，exit 0）。

`Derivable` 也可作谓词，但它需要 sequent（位集）而非单公式；
`ShCraigElim` 要的是 `Provable Sh.craig ⌜σ⌝ → Provable 𝗭𝗙𝗖 ⌜translate σ⌝`，
所以**谓词取 `Provable 𝗭𝗙𝗖 ∘ translateSeq`**（对 sequent 形式）或
`Provable 𝗭𝗙𝗖 ∘ iT 0`（对单公式形式）。

### 4.3 两个未证的相容性引理

| 需要的 | 用在哪 | 现状 |
|---|---|---|
| `iT` 与 `setShift` 的相容 | `hShift` 支 | **未证** |
| `iT` 与 `substs1` 的相容 | `hExs` 支 | **未证** |

这两条是 W8 规格 §3 第 1 层列的 `shift` / `subst` 项，属"纯语法、可独立做"的类别。

---

## 5. 与 `keyE` / `bwd` 的关系

```
ShCraigElim  ──(C-390 的 bwd_of_shcraig_elim)──▶  bwd  ──▶  keyE  ──▶  D3  ──▶  Z0 完整形式
```

`Z0UniBridge.bwd_of_shcraig_elim`（C-390，已收据）表明：**`ShCraigElim` 一旦成立，
`bwd` 立即成立**，无需其他东西。宇宙层级障碍（本机实测 `rw [models_zfcTr_iff]` 在
`V : Type*` 下失败）已由 `models_zfcTr_iff'` 清除。

---

## 6. 停止条件

- 若 `hAll`/`hExs`/`hShift` 三条相容性引理被证明需要 𝗭𝗙𝗖 内的归纳（而 𝗜𝚺₁ 供不起），
  照实写明，把最小可续状态留在本文件。
- **不要**为了"完成"收窄 `ShCraigElim` 的陈述。
- `C-120` 的影子形式无条件成立，不受本路线进展影响。

---

## 7. 2026-10-11 追加：谓词构造的**可用模式**（本机逐条实测）

`induction1` 要求 `hP : Γᴬ_[1]-Predicate P`。要让这个义务真正落地，
**不能用 `definability`**（它在 `Provable`/`Derivable` 的语言参数 `L` 未定时就
试图解析 `Tarski.Structure L V`，必报 `typeclass instance problem is stuck`）。

### 7.1 可用的三层模式（本机 exit 0）

```lean
-- 第 1 层：单个 Σ1 谓词，用 `via` + `.mk`
example : { Γ := 𝚺, rank := 1 }-Predicate (Provable (L := ℒₒᵣ) 𝗜𝚺₁ : V → Prop)
    via FFL.FirstOrder.Arithmetic.Bootstrapping.provable 𝗜𝚺₁ :=
  .mk fun v => by simp                                    -- [实测] exit 0

-- 第 2 层：Σ1 谓词用 ℒₛₑₜ（目标理论是 𝗭𝗙𝗖 时）
example : { Γ := 𝚺, rank := 1 }-Predicate (Provable (L := ℒₛₑₜ) 𝗭𝗙𝗖 : V → Prop)
    via FFL.FirstOrder.Arithmetic.Bootstrapping.provable 𝗭𝗙𝗖 :=
  .mk fun v => by simp                                    -- [实测] exit 0

-- 第 3 层：复合（谓词 ∘ Σ1 函数）——**手写显式 Semisentence**
noncomputable def provTransSeq : 𝚺ᴬ₁.Semisentence 1 := .mkSigma
  “s. ∃ y, !(translateSeqGraph) y s ∧ !(provable 𝗭𝗙𝗖) y”
-- 然后 via provTransSeq + .mk + 展开定义（本机已到"只剩 simp 展开"这一步）
```

### 7.2 关键的类型事实（本机实测）

| 名字 | 实际类型 |
|---|---|
| `translateSeqGraph` | `{ Γ := 𝚺, rank := 1 }.Semisentence 2`（**不是** `𝚺ᴬ₁.Semisentence`） |
| `provable T` | `{ Γ := 𝚺, rank := 1 }.Semisentence 1` |
| `derivable T` | `{ Γ := 𝚺, rank := 1 }.Semisentence 1` |
| `Provable.defined` | `{ Γ := 𝚺, rank := 1 }-Predicate Provable T via provable T` |

**`trProv`（`Z0Full.lean:40`）的声明形式是范本**：`noncomputable def trProv : 𝚺ᴬ₁.Semisentence 1 := .mkSigma “...”`，
随后 `instance ... via trProv := .mk fun v => by simp [...]`。

### 7.3 下一步的具体动作

1. 把 `provTransSeq` 的 `simp` 展开做完（展开 `Semiformula.Evalb` + `translateSeqGraph` 的 `via` 定义）；
2. 用 `Provable.defined` 的 `via` 事实把 `∃ y, ...` 与 `Provable 𝗭𝗙𝗖 (translateSeq s)` 对接；
3. 得到 `hP` 后即可开 `induction1`，逐条攻 10 个规则支。

**这三步都是技术性的，不是数学障碍。** 真正的数学内容在 §4.3 的两条相容性引理
（`iT` 与 `setShift` / `substs1`），以及 `hRoot` 支对 `Sh.craig` 公理结构的处理。
