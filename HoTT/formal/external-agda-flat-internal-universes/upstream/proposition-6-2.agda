{-# OPTIONS --no-pattern-matching --rewriting #-}

module proposition-6-2 where

  open import agda.prelude
  open import agda-flat.prelude
  open import agda.postulates
  open import agda.fibration

  -- Prop 6.2. concerns fibrations with respect to the
  -- exponential path object functor, (_)^𝕀.
  open import agda.exp-path

  module
    Univ
      (C :{♭} {l : Level} (A : ℘ (Set l)) → Set (ℓ₁ ⊔ l))
      {l :{♭} Level}
      where
    open module F = Fib ℘ ℘` ℘`comp C

    postulate
      U  : Set (ℓ₂ ⊔ lsuc l)

      -- unpacked version is more REWRITE-friendly
      El₀ : U → Set (l)
      El₁ : F.isFib U El₀

    El : Fib l U
    El = El₀ , El₁ 

    postulate
      code :
        {Γ :{♭} Set (ℓ₂ ⊔ lsuc l)}
        (Φ :{♭} Fib l Γ)
        → ------------------------
        Γ → U
      β :
        {Γ :{♭} Set (ℓ₂ ⊔ lsuc l)}
        (Φ :{♭} Fib l Γ)
        → ------------------------
        El [ code Φ ] ≡ Φ
      η :
        {Γ :{♭} Set (ℓ₂ ⊔ lsuc l)}
        (A :{♭} Γ → U)
        → ------------------------
        A ≡ code (El [ A ])


    -- unpack the two parts of β and install them as rewrites

    β1 :
        {Γ :{♭} Set (ℓ₂ ⊔ lsuc l)}
        (Φ :{♭} Fib l Γ)
        (x : Γ)
        → ------------------------
        El₀ (code Φ x) ≡ fst Φ x
    β1 Φ x = cong (\ h → fst h x) (β Φ)
    {-# REWRITE β1 #-}

    β2 :
        {Γ :{♭} Set (ℓ₂ ⊔ lsuc l)}
        (Φ :{♭} Fib l Γ)
        → --------------------------------------
        ∀ p → El₁ (\ i → code Φ (p i)) ≡ snd Φ p
    β2 Φ p = cong (\ h → subst (λ z → C (λ i → z (p i))) h ((snd (El [ code Φ ]) p))) {x = refl} {y = (cong fst (β Φ))} uip ·
             (cong (\ h → h (snd (El [ code Φ ]) p)) (symm (subst-cong-assoc (λ z → C (℘` z p)) fst (β Φ)))) ·
             congd (\ x → snd x p) (β Φ)
    {-# REWRITE β2 #-}


    -- some lemmas about equality in U

    -- ported these from an old file but didn't need them; maybe need them later

    -- cong-code-com : {l1 :{♭} Level} {Γ :{♭} Set _} {A :{♭} Γ → Set l} {φ1 φ2 :{♭} F.isFib Γ A} {x : Γ}
    --           → φ1 ≡ φ2 
    --           → (code (A , φ1)) x ≡ (code (A , φ2)) x
    -- cong-code-com refl = refl

    -- comEl-code-subst : ∀ {l2 :{♭} Level} {Δ :{♭} Set l2} {Γ :{♭} Set (ℓ₂ ⊔ lsuc l)} 
    --                  {A :{♭} Fib l Γ} (f : Δ → Γ)
    --                → El [ (code A) ∘ f ] ≡ A [ f ]
    -- comEl-code-subst {A = A} f = refl

    -- universal-code-η : ∀ {l :{♭} Level} → (A : U) → A ≡ (code El) A
    -- universal-code-η A = cong (\ h → h A) {x = (\ x → x)}{_} (η (\ X → X))

    code-flat-assoc : ∀ {Γ Δ :{♭} Set (lsuc (lsuc lzero) ⊔ lsuc l)} 
                      {Φ :{♭} Fib l Γ} (f :{♭} Δ → Γ)
                      → (x : Δ) → (code Φ) (f x) ≡ (code (Φ [ f ])) x
    code-flat-assoc {Φ = Φ} f x = cong (\ h → h x) (η (\ x → (code Φ) (f x)))


  -- Agda doesn't seem to let you quantify over levels like this, so can't abstract this :(
  -- isFib-morphism-raw : (C1 C2 :{♭} {l : Level} (A : ℘ (Set l)) → Set (ℓ₁ ⊔ l)) → ?
  -- isFib-morphism-raw C1 C2 = {l1 l2 : Level} {Γ : Set l1} (A : Γ → Set l2) → Fib.isFib C1 Γ A → Fib.isFib C2 Γ A

  i : (C1 C2 :{♭} {l : Level} (A : ℘ (Set l)) → Set (ℓ₁ ⊔ l))
        {l :{♭} Level} 
     → (Fib12 :{♭} {l1 l2 : Level} {Γ : Set l1} (A : Γ → Set l2) → Fib.isFib ℘ ℘` ℘`comp C1 Γ A → Fib.isFib ℘ ℘` ℘`comp C2 Γ A)
     → Univ.U C1 {ℓ₁ ⊔ l} → Univ.U C2 {ℓ₁ ⊔ l}
  i C1 C2 {l} Fib12 =
    Univ.code C2 {Γ = Univ.U C1} (fst (Univ.El C1) , \ p → Fib12 (fst ((Univ.El C1) {lsuc lzero ⊔ l})) (snd (Univ.El C1 {ℓ₁ ⊔ l})) p)

  ident : (C1 :{♭} {l : Level} (A : ℘ (Set l)) → Set (ℓ₁ ⊔ l))
          {l :{♭} Level} (A :{♭} Univ.U C1 {ℓ₁ ⊔ l})
        → i C1 C1 {l} (\ A f → f) A ≡ A
  ident C1 A = symm (cong (\ h → h A) (Univ.η C1 (\ X → X)))

  composition : (C1 C2 C3 :{♭} {l : Level} (A : ℘ (Set l)) → Set (ℓ₁ ⊔ l))
                (Fib12 :{♭} {l1 l2 : Level} {Γ : Set l1} (A : Γ → Set l2) → Fib.isFib ℘ ℘` ℘`comp C1 Γ A → Fib.isFib ℘ ℘` ℘`comp C2 Γ A)
                (Fib23 :{♭} {l1 l2 : Level} {Γ : Set l1} (A : Γ → Set l2) → Fib.isFib ℘ ℘` ℘`comp C2 Γ A → Fib.isFib ℘ ℘` ℘`comp C3 Γ A)
                (Fib23-reindex :{♭} {l1 l2 : Level} {Γ Δ : Set l1} (f : Δ → Γ) (A : Γ → Set l2)
                                    → (φ : Fib.isFib ℘ ℘` ℘`comp C2 Γ A) (δ : ℘ Δ)
                                    → (Fib23 A φ) (℘` f δ) ≡ Fib23 (A ∘ f) (\ p → φ (f ∘ p)) δ)
                {l :{♭} Level}
                (A :{♭} Univ.U C1)
                → i C2 C3 {l} Fib23 (i C1 C2 {l} Fib12 A) ≡
                  i C1 C3 {l} (\ A x → Fib23 A (Fib12 A x)) A
  composition C1 C2 C3 Fib12 Fib23 Fib23-reindex {l} A = 
    -- also uses the β's as rewrites
    (Univ.code-flat-assoc C3 {Φ = Fib._[_] ℘ ℘` ℘`comp C3 (Univ.El C3) (i C2 C3 {l} Fib23)} (i C1 C2 {l} Fib12) A) ·
     cong♭ (\ h → Univ.code C3 (Univ.El₀ C1 , h) A)
           (funext (\ B → Fib23-reindex (Univ.code C2 (Univ.El₀ C1 , Fib12 (Univ.El₀ C1) (Univ.El₁ C1))) _ _ B))



  -- not sure if this will be useful in examples,
  -- but checks that the previous version involving comp morphisms is an instance

  comp-morphism-to-fib-morphism : (C1 :{♭} {l : Level} (A : ℘ (Set l)) → Set (ℓ₁ ⊔ l))
                                  (C2 :{♭} {l : Level} (A : ℘ (Set l)) → Set (ℓ₁ ⊔ l))
                                  (C12 :{♭} {l : Level} (A : ℘ (Set l)) → C1 A → C2 A)
                                  → ({l1 l2 : Level} {Γ : Set l1} (A : Γ → Set l2) → Fib.isFib ℘ ℘` ℘`comp C1 Γ A → Fib.isFib ℘ ℘` ℘`comp C2 Γ A)
  comp-morphism-to-fib-morphism C1 C2 C12 A φ p = C12 (℘` A p) (φ p)

  comp-morphism-to-fib-morphism-reindex : (C1 :{♭} {l : Level} (A : ℘ (Set l)) → Set (ℓ₁ ⊔ l))
                                          (C2 :{♭} {l : Level} (A : ℘ (Set l)) → Set (ℓ₁ ⊔ l))
                                          (C12 :{♭} {l : Level} (A : ℘ (Set l)) → C1 A → C2 A)
                                          {l1 l2 : Level} {Γ Δ : Set l1} (f : Δ → Γ) (A : Γ → Set l2)
                                        → (φ : _) (δ : ℘ Δ) →
                                          (comp-morphism-to-fib-morphism C1 C2 C12 A φ) (℘` f δ) ≡
                                          comp-morphism-to-fib-morphism C1 C2 C12 (A ∘ f) (\ p → φ (f ∘ p)) δ
  comp-morphism-to-fib-morphism-reindex C1 C2 C12 A φ p δ = refl
