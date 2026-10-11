# C-369：Foundation Lean 第一不完备性 R3 重放

> **证明包：** `MP-FOUNDATION-INCOMPLETENESS-R3-001`。
>
> **理论变体：** Foundation Lean 4 中的 first-order arithmetic；不是 exact HoTT calculus，也不是 ZFC 对象语言。
>
> **冻结来源：** `FormalizedFormalLogic/Foundation@f3972f4204fc61e1b736ed843415894c83f35508`，module `Foundation.FirstOrder.Incompleteness.First`。

## 精确主张

在冻结来源的 `FFL.FirstOrder.Arithmetic.incomplete` 中，给定：

```text
T : ArithmeticTheory
[T.Δ₁]
[𝗥₀ ⪯ T]
[T.SoundOnHierarchy 𝚺 1]
```

Lean 证明 `Entailment.Incomplete T`。源码定义：

```text
D φ := IsSemiformula ℒₒᵣ 1 φ
       ∧ Provable T (neg ℒₒᵣ (subst ℒₒᵣ ?[numeral φ] φ))
δ := codeOfREPred D
π := δ/[⌜δ⌝]
```

并证明 `T ⊢ π ↔ T ⊢ ∼π`，随后由一致性得到 `π` 与其否定均不可证。该文件还导出：

- `incomplete_of_RE`；
- `exists_true_but_unprovable_sentence_of_sigma1sound`；
- `exists_true_but_unprovable_sentence_of_RE_of_sigma1sound`。

主 qualification 打印这些声明及其 kernel axioms。当前定理依赖 Lean 的
`propext`、`Classical.choice`、`Quot.sound`；算术强度、可表示性和 soundness 条件仍是显式 theorem assumptions。

## 负控制

`WrongMissingSoundness.lean` 尝试只在 `[T.Δ₁] [𝗥₀ ⪯ T]` 下调用 `incomplete T`。
Lean 必须拒绝它，并报告缺少 `T.SoundOnHierarchy 𝚺 1`。这证明本包没有把 source theorem 的 soundness 前提静默抹去。

## 它支付的 G0 内容

本包支付的是：一个版本固定的一阶算术 proof system 中，编码、quote、substitution、provability、固定点句与一致性前提如何形成可机器检查的第一不完备性结果。

## 它不支付

- exact HoTT calculus 的 object-level proof code、arithmetic interpretation、representability 或 independent sentence；
- HoTT 的 Path、univalence、HIT 对该机制是否必要；
- bare ZFC 的 `Accept_ZFC`、completion policy、`FormalDone → OriginDone` bridge；
- 芝诺、圆环或 fixed H0 与此一阶算术任务的同一性；
- ZFC 的对象语言矛盾，或 bare ZFC 理论精度不足的最终判词。
