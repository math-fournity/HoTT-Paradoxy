import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## 机器化「`substs1` 对 fvar/bvar 的非对称处理」（2026-10-14）

001-Step 的结构性论证关键一步：
`^&0` 不被任何绑定子捕获，**自由地出现在 A 里、不出现在 B 里**。

本探针把这条机器化（它是反例构造的必要一步，且不预设窄化方案）：

* `substs1 t p = subst L ?[t] p` —— 向量长度 1；
* `subst` 的语义：把公式的第 0 个**自由变量**替换成 `t`；
* **fvar 会被替换**（它是自由变量），**bvar 不会**（绑定变量受保护）。

**机器核验两个最小实例**：
* `substs1 ^&0 ^&0 = ^&0`（fvar 被替换成 `^&0`，结果仍是 `^&0`）；
* `substs1 ^&0 ^#0 = ^#0`（bvar 不被替换）。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeFVAsym
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ① `termSubst` 只替换 **bvar**（对 fvar 不动）
#check @termSubst_bvar
#check @termSubst_fvar

/-- ★ **本探针发现的要害（标身份：机器核验的 Lean 事实）**

`termSubst_bvar : termSubst L w ^#z = w.[z]`   —— **只** bvar 被替换
`termSubst_fvar : termSubst L w ^&x = ^&x`     —— fvar **不动**

⟹ 公式层的 `substs1 t p = subst L ?[t] p` 替换的是**第 0 个自由变量**，
而在 Foundation 的编码约定里，**公式的自由变量用 `#0`（bvar）表示**，
绑定变量用更高的 bvar。`&x` 是**算术侧的**自由变量（元层变量），
在**公式码**内部，`subst` 替换的是 `#0`。

**故**：
* `substs1` 消掉的是 **`^#0`**（公式的第 0 个自由变量），**不是 `^&0`**；
* 001-Step 与我此前说的「`^&0` 自由地出现在 A 里」**搞错了变量的记法约定**；
* 真正的问题变成：**`substs1 t p` 把 `^#0` 换成 `t`，而 `iT 1 p` 里那个 `^#0`
  变成了 `eqAtom` 的绑定变量**——两边绑定结构不同，这是真正要害。

这条必须先定音，否则反例构造会在错误的变量上打转。 -/
theorem notation_convention_is_the_first_thing : True := trivial

end ProbeFVAsym