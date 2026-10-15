import GodelQ.Diagonal.Core

/-!
# 负控制 MP-CG001-HALTING-WITHOUT-LEM-NEG-001：没有翻转程序，也照样证“认不出永不停机”

被否定的说法：在“什么都不停机、判定器一律回答‘否’”的系统里，也没有程序恰好认出“永不停机”。
这里照搬主包的对角论证：把程序 `d` 自己当输入。可这个系统没有翻转程序，`hd d d` 只是
`True ↔ ¬False`，不是 `P ↔ ¬P` 的形状。

预期：拒绝，类型不匹配。主包的正面定理 `recognizer_without_flip`（C-422 (3)）证明这个说法本来
就不成立：认出者在这里存在。所以翻转程序是对角论证真正用到的前提。
-/

namespace GodelQ.Diagonal.Negative

open GodelQ.Diagonal

theorem no_recognizer_without_flip :
    ¬ ∃ d : Nat, ∀ e x : Nat,
      (fun (_ _ _ : Nat) => True) d e x ↔ ¬ (fun (_ _ : Nat) => False) e x := by
  intro ⟨d, hd⟩
  exact no_liar _ (hd d d)

end GodelQ.Diagonal.Negative
