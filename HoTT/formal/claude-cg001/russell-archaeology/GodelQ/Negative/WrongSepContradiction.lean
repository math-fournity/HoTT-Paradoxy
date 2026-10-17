import GodelQ.Russell.Sep

/-!
# 负控制 MP-CG001-RUSSELL-ARCHAEOLOGY-NEG-001：把 C-432 的对角结尾照搬到分离层

被否定的说法：分离层的成员刻画同样自我爆炸（「Zermelo 的『解决』= 在新系统内
证明出矛盾」的误读，或「分离版罗素论证与无界版一样给出矛盾」）。照搬主包
C-432 `noRussellSet` 的证明结尾 `exact hne (h.mpr hne)`：在无界层，`h.mpr hne`
从 `R ∉ R` 直接造出 `R ∈ R`，爆炸；同一行照搬到分离层，`h.mpr` 需要的是
`R ∈ A ∧ R ∉ R`，多出的 `R ∈ A` 无从提供。

预期：拒绝。`h.mpr hne` 类型不符：`hne : R ∉ R`，但 `h.mpr` 期望
`R ∈ A ∧ R ∉ R`。这道门正是 1908 年 Zermelo 用分离替换无界概括留下的
精确空隙：对角论证在分离层只走得出一半（正面定理 C-433 `sep_russell_not_mem`
的 `R ∉ A`），另一半被基底条件挡住——准入层拒绝不是矛盾。
-/

namespace GodelQ.Russell.Negative

open FFL

variable {V : Type*} [SetStructure V]

theorem sep_russell_contradiction (A R : V)
    (hR : ∀ z : V, z ∈ R ↔ (z ∈ A ∧ z ∉ z)) : False := by
  have h := hR R
  have hne : R ∉ R := fun hmem => (h.mp hmem).2 hmem
  exact hne (h.mpr hne)

end GodelQ.Russell.Negative