import GodelQ.ZFC.SeqTranslate
import GodelQ.ZFC.Z0Full

/-!
# CG-007 · W8 第二层（二）：`Derivable Sh.craig s → Derivable 𝗭𝗙𝗖 (translateSeq s)`

用 `Derivation.induction1` 对 V 内部推导做归纳，逐条规则消。
`axm` 支是唯一用到 𝗭𝗙𝗖 的地方。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

open GodelQ.Translate GodelQ.ZFCZ0 GodelQ.Z0Full

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 归纳谓词：推导 `d` 的 sequent 翻译后仍可导。 -/
abbrev P (d : V) : Prop := Derivable (T := 𝗭𝗙𝗖) (L := ℒₛₑₜ) (translateSeq (fstIdx d))

theorem derivable_translateSeq {s : V} (h : Derivable (T := Sh.craig) (L := ℒₒᵣ) s) :
    Derivable (T := 𝗭𝗙𝗖) (L := ℒₛₑₜ) (translateSeq s) := by
  obtain ⟨d, hfs, hd⟩ := h
  have key : P d :=
    Derivation.induction1 (T := Sh.craig) (L := ℒₒᵣ) 𝚺
      (P := P) (by definability) hd
      -- axL
      (fun s _ p hps hnps => by
        refine ⟨axL (translateSeq s) (iT (0 : V) p), by simp [fstIdx_axL], ?_⟩
        exact Derivation.axL (translateSeq_isFormulaSet s) _ _)
      -- verumIntro
      (fun s _ hs => by
        refine ⟨verumIntro (translateSeq s), by simp [fstIdx_verumIntro], ?_⟩
        exact Derivation.verumIntro (translateSeq_isFormulaSet s) _)
      -- andIntro
      (fun s _ p q dp dq hpq hdp hdq ihp ihq => by
        obtain ⟨d₁, h₁, hd₁⟩ := ihp
        obtain ⟨d₂, h₂, hd₂⟩ := ihq
        refine ⟨andIntro (translateSeq s) (iT (0 : V) p) (iT (0 : V) q) d₁ d₂,
          by simp [fstIdx_andIntro], ?_⟩
        exact Derivation.andIntro _ _ _)
      -- orIntro
      (fun s _ p q d hpq hd ih => by
        obtain ⟨d₁, h₁, hd₁⟩ := ih
        refine ⟨orIntro (translateSeq s) (iT (0 : V) p) (iT (0 : V) q) d₁,
          by simp [fstIdx_orIntro], ?_⟩
        exact Derivation.orIntro _ _)
      -- allIntro
      (fun s _ p d hp hd ih => by
        obtain ⟨d₁, h₁, hd₁⟩ := ih
        refine ⟨allIntro (translateSeq s) (iT (0 : V) p) d₁, by simp [fstIdx_allIntro], ?_⟩
        exact Derivation.allIntro _ _)
      -- exsIntro
      (fun s _ p t d hp ht hd ih => by
        obtain ⟨d₁, h₁, hd₁⟩ := ih
        refine ⟨exsIntro (translateSeq s) (iT (0 : V) p) (iT (0 : V) t) d₁,
          by simp [fstIdx_exsIntro], ?_⟩
        exact Derivation.exsIntro _ _ _)
      -- wk
      (fun s _ d hsub hd ih => by
        obtain ⟨d₁, h₁, hd₁⟩ := ih
        refine ⟨wkRule (translateSeq s) d₁, by simp [fstIdx_wkRule], ?_⟩
        exact Derivation.wkRule (translateSeq_isFormulaSet s) _ hd₁)
      -- shift
      (fun s _ d heq hd ih => by
        obtain ⟨d₁, h₁, hd₁⟩ := ih
        refine ⟨shiftRule (setShift ℒₛₑₜ (translateSeq (fstIdx d))) d₁, by simp, ?_⟩
        exact Derivation.shiftRule _)
      -- cut
      (fun s _ p d₁ d₂ hd₁ hd₂ ih₁ ih₂ => by
        obtain ⟨e₁, k₁, he₁⟩ := ih₁
        obtain ⟨e₂, k₂, he₂⟩ := ih₂
        refine ⟨cutRule (translateSeq s) (iT (0 : V) p) e₁ e₂, by simp [fstIdx_cutRule], ?_⟩
        exact Derivation.cutRule _ _)
      -- axm
      (fun s _ p hps hpT => by
        exact derivable_translateSeq_of_axm hps hpT)
  rwa [hfs] at key

end GodelQ.SeqTranslate
