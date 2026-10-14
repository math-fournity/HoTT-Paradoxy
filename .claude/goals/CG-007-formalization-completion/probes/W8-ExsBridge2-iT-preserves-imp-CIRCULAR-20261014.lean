import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ⚠ `ExsBridge2` 的「`iT 0` 保蕴含」短路是**循环**的（2026-10-14）

### 观察

`ExsBridge2` 的右端 `^∃ (domZero ⋏ iT 1 p)` **就是** `iT 0 (^∃ p)`
（`iT_exs`，已证；本探针 exit 0）：

```lean
example {p : V} (hp : IsUFormula ℒₒᵣ p) :
    iT (0:V) (^∃ p) = ((^∃ ((domZero (V := V)) ^⋏ iT (0+1:V) p) : V)) :=
  iT_exs (n := (0:V)) hp
```

故 `ExsBridge2` 等价于

```
Provable 𝗭𝗙𝗖 (imp (iT 0 (substs1 ℒₒᵣ t p)) (iT 0 (^∃ p)))
```

### 诱人的短路（**不可用**）

`p[t] → ∃x p(x)` 在算术里是**一阶重言式**。若 `iT 0` **保蕴含**：

```
Provable_arith (imp A B) → Provable_set (imp (iT 0 A) (iT 0 B))
```

则 `ExsBridge2` 直接得到，**不需要任何语法桥**。

### ⚠ 为什么它是循环的

「`iT 0` 保蕴含」就是

```
Derivable Sh.craig {imp A B} → Derivable 𝗭𝗙𝗖 (translateSeq {imp A B})
```

——**这正是归纳目标 `induction_setup_Q` 在 sequent `{imp A B}` 上的特例**。
用它证 `ExsBlockerQ`（`induction_setup_Q` 的一条支）是**循环论证**。

（本探针 `#check @induction_setup_Q_of_blockers` 确认该形状。）

### 结论

`ExsBridge2` **不能**靠「`iT` 保重言式」短路。
它的数学内容（`p[t] → ∃x p(x)`）虽然是真的，
但**把这条真命题搬到 `ℒₛₑₜ`** 正是我们要证的搬运本身。

**`ExsBridge2` 仍需**：
1. 语法路线（`iT_substs1` 型等式，与 `hAll` 同源），**或**
2. 在 `ℒₛₑₜ` 里直接构造该蕴含的推导（`Derivable` 层，不经 `iT`）。

**注意**：**`p` 具体的情形成立**（`exsBridge2_top_of_omega` 已证，入生产包），
一般 `p` 不行——与 [[cg007-semantic-route-refuted]] 的边界一致。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeEX4
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 右端就是 iT 0 (^∃ p)（iT_exs，已证；exit 0）
example {p : V} (hp : IsUFormula ℒₒᵣ p) :
    iT (0:V) (^∃ p) = ((^∃ ((domZero (V := V)) ^⋏ iT (0+1:V) p) : V)) :=
  iT_exs (n := (0:V)) hp

-- 「iT 0 保蕴含」= induction_setup_Q 在 {imp A B} 上的特例 ⟹ 循环
#check @induction_setup_Q_of_blockers
#check @Q

end GodelQ.ProbeEX4
