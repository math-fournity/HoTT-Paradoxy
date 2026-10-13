import GodelQ.ZFC.ShCraigElimSetupQ

/-! ## `ExsBlockerQ` 拆解：主攻 `Derivable.and_m`，一条已证、义务显式化（2026-10-13）

### 结论

`iT` 的 exs 支给的是 **`^∃ domZero ^⋏ iT (n+1) p`**（一个**合取**，不是存在量词），
所以 `Derivable.exs` **形状直接不匹配**——它给的是 `^∃ q`。
**但 `Derivable.and_m` 正好对 `⋏`**：
```
Derivable.and_m : p ^⋏ q ∈ s → Derivable T (p ⫽ s) → Derivable T (q ⫽ s) → Derivable T s
```
而 `iT 0 (^∃ p) ∈ translateSeq s` 是现成的。于是 `ExsBlockerQ` 拆成三件：

**① 已证（exit 0）**：`iT 0 (^∃ p) ∈ translateSeq s`，
由 `mem_translateSeq_iff` + `(iT_exs (n := 0) hp).symm` 一步。

**② 义务一**：`Derivable 𝗭𝗙𝗖 (domZero ⫽ translateSeq s)`。
（`domZero` 是引号化句子，`hRoot_core` 型搬运的思路可用。）

**③ 义务二（核心）**：
```
ih : Derivable 𝗭𝗙𝗖 (iT 0 (substs1 ℒᵣ t p) ⫽ translateSeq s)
⊢   Derivable 𝗭𝗙𝗖 (iT (0+1) p ⫽ translateSeq s)
```
**只有主公式不同**——与 `hAll` 末步同型（我用过同类 `wk` 思路处理 hAll）。

### 关键机制：`conjunct` 就是层数对齐器

本机 `#print conjunct` 得：
```
conjunct b n i y = subst ℒₜ (?[^#i]) ↑cDomN ⋏ subst ℒₜ (^#i ∷ shiftVec b n) y
```

两边差别全在 `conjunct 2 n i (...)` 的 `n` 与项 `v`：
LHS 用 `n = 0` 与代入后的 `^&0`，RHS 用 `n = 1` 与原始 `^#0`。
`conjunct` 的 `shiftVec b n` 正是吸收这个层数位移的部件。

### 与 `AllBlocker` 的关系（重要）

**`ExsBlocker` 不需要 `free`**——这是它比 `AllBlocker` 便宜的根本原因
（`AllBlocker` 的 `free` 已被判死）。`ExsBlocker` 要的是
**`iT 0 (substs1 ℒᵣ t p)` 与 `iT 1 p` 的内部互相可导**，
即 `iT_substs1` 的**同层数**版本——与 Master 判给 003 线的桥不同，
这条**不跨语言到 `iVE` 层**，只在 `iT` 与 `substs1` 之间。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ① 已证（exit 0） -/
theorem exsB_membership (s p : V) (hp : IsUFormula ℒₒᵣ p)
    (hps : ^∃ p ∈ (s : V)) :
    ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V) ∈ translateSeq s :=
  (mem_translateSeq_iff.mpr ⟨_, hps, (iT_exs (V := V) (n := (0:V)) hp).symm⟩)

/-! ③ 义务二的精确形状（本轮 trace 出，尚未证） -/
theorem exsB_branch2 (s p t dd : V)
    (hfd : fstIdx dd = insert (substs1 ℒₒᵣ t p) s)
    (ih : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) (fstIdx dd))) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (((iT (0+1:V) p) ⫽ (translateSeq (V := V) s) : V)) := by
    rw [hfd, translateSeq_insert] at ih
    sorry

-- `conjunct` 的形状（本机 #print，义务二的关键机制）
example (b n i y : V) :
    conjunct (V := V) b n i y
      = subst ℒₛₑₜ ((?[^#i] : V)) ↑cDomN ^⋏ subst ℒₛₑₜ ((^#i ∷ shiftVec b n : V)) y := rfl

end GodelQ.ProbeExsB
