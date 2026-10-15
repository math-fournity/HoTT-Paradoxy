import GodelQ.ZFC.Z0OmegaQuestion

/-!
# 负控制 MP-CG001-Z0-OMEGA-QUESTION-NEG-001：每一刻的确认，合起来就是“永不”的确认

被否定的说法：𝗭𝗙𝗖 对 Z0 每一刻都确认“到第 k 步还没找到矛盾”（C-427 (4)），这些确认合起来就是
𝗭𝗙𝗖 对“Z0 永不停机”的证明。这里直接把每一刻的确认当作“永不”的证明交上去。

预期：拒绝。每一刻的确认是一族关于 k 的证明，不是“永不停机”句的证明，类型对不上。
这一拒绝只说明这一步不能直接走；𝗭𝗙𝗖 确实证不出“自己一致”，见 C-417 与 C-427 (6)。
“永不停机”句的程序形式与 Foundation 一致性句之间，在 𝗭𝗙𝗖 内部的等价本包没有证明。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic SetTheory

namespace GodelQ.Z0Omega.Negative

open GodelQ GodelQ.Z0Omega GodelQ.ZFCEff

theorem stages_make_never : zfcEffective.provesNever z0Code :=
  zfcEffective.observes_every_instant z0Code z0Code_not_done

end GodelQ.Z0Omega.Negative
