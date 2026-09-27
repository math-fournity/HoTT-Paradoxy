{-# OPTIONS --safe --cubical --guardedness #-}
{-
  Kraus–Sattler, "Higher Homotopies in a Hierarchy of Univalent Universes"
  (arXiv:1311.4002v3, ACM TOCL 16(2), 2015), Section 5, replayed for ALL n
  in Cubical Agda 2.8.0 + cubical 0.9.
  (Cloud-Opus completion of the GLM work order, 2026-09-27; claim ids
  COPUS-KS-C01 .. C05, full statements in CLAIM.md.)

  Paper map (KS numbering):
    Lemma 4.5  Ω commutes with Σ•                 ΩΣ≃∙
    Lemma 4.7  Ω commutes with Π•                 ΩΠpt, Ω^Πpt   (from C-75, Opus)
    Lemma 5.1  a truncated Σ-component is
               neutralised by Ω^n                 ΩΣtrunc
    Lemma 5.2  local-global looping (pointed)     localGlobal∙  (pointed form of
                                                                 C-75's localGlobal)
    Lemma 5.4  (=>) n-type => Ω^(n+1) contractible hLevelΩ^     (from C-75, Opus)
    Lemma 5.5  U^{<=n} is (n+1)-truncated          isOfHLevelTypeOfHLevel (library)
    Cor.  5.6  P_n is a family of sets             isSetP
    Lemma 5.7  Loop_n is (n+1)-truncated           hLoop
    Lemma 5.8  a non-trivial (n+1)-loop exists     base / step / tower
               (xi := λ(X,q).(q,d_q); d_q from
                q⁻¹·q·q for m = 0, from set-ness
                of the fibres for m >= 1)
    Thm   5.9  U_n is not an n-type                KS-Theorem-5-9, workOrderForm
    Thm   5.10 U_n^{<=n}, Loop_n strict (n+1)-types KS-Theorem-5-10-*

  The induction step `step` is stated for an ARBITRARY universe level L and
  an ARBITRARY truncation index k (it is not tied to "universe index =
  truncation index"); the tower instantiates it at (lvl n, n), and the
  work order's tail-recursive level `iterSuc` is obtained from the same
  step by `towerFrom`.

  No postulates, --safe.  HIT-freeness of the closure is certified
  mechanically by HITScan (see CertKSUniverseTower.agda).
-}
module KSUniverseTower where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Pointed
open import Cubical.Foundations.GroupoidLaws using (assoc ; lCancel ; lUnit)
open import Cubical.Foundations.Path using (compPathL→PathP)
open import Cubical.Data.Nat using (ℕ ; zero ; suc ; _+_ ; +-suc ; +-zero ; +-comm)
open import Cubical.Data.Sigma
open import Cubical.Data.Bool using (Bool ; true ; false)
open import Cubical.Data.Bool.Properties using (notEquiv ; isSetBool ; true≢false)
open import Cubical.Relation.Nullary using (¬_)
open import Cubical.Homotopy.Loopspace using (Ω ; Ω^_ ; Ω^≃∙)

private
  variable
    ℓ ℓ' : Level

------------------------------------------------------------------------
-- 0. Pointed-equivalence utility.

pathToEquiv∙ : {A B : Pointed ℓ} → A ≡ B → A ≃∙ B
pathToEquiv∙ P = pathToEquiv (cong typ P) , fromPathP (cong pt P)

------------------------------------------------------------------------
-- 1. Iterated loop spaces (Ω^suc, hLevelΩ^, Πpt, ΩΠpt, Ω^Πpt, U∙, ΩU≃∙,
--    ΩEquiv≡ΩFun are copied from Opus's C-75 package
--    HoTT/formal/claude-cg001/universe-questioning/UniverseHasNoLevel.agda,
--    whose name-level closure of these parts is HIT-free per HITScan).

Ω^suc : (n : ℕ) (A : Pointed ℓ) → (Ω^ (suc n)) A ≡ (Ω^ n) (Ω A)
Ω^suc zero A = refl
Ω^suc (suc n) A = cong Ω (Ω^suc n A)

-- KS Lemma 5.4 (=>): an (n-1)-type has contractible n-fold loop spaces.
hLevelΩ^ : (n : ℕ) {A : Type ℓ} (a : A) → isOfHLevel (suc n) A → isContr (typ ((Ω^ n) (A , a)))
hLevelΩ^ zero a h = a , h a
hLevelΩ^ (suc n) {A} a h =
  subst (λ P → isContr (typ P)) (sym (Ω^suc n (A , a)))
        (hLevelΩ^ n refl (isOfHLevelPath' (suc n) h a a))

-- Truncation level of iterated loop spaces (used for KS Cor. 5.6).
isOfHLevelΩ^ : (k n : ℕ) {A : Type ℓ} (a : A)
  → isOfHLevel (k + n) A → isOfHLevel k (typ ((Ω^ n) (A , a)))
isOfHLevelΩ^ k zero {A} a h = subst (λ j → isOfHLevel j A) (+-zero k) h
isOfHLevelΩ^ k (suc n) {A} a h =
  isOfHLevelPath' k
    (isOfHLevelΩ^ (suc k) n a (subst (λ j → isOfHLevel j A) (+-suc k n) h)) _ _

Πpt : (A : Type ℓ) (B : A → Pointed ℓ') → Pointed (ℓ-max ℓ ℓ')
Πpt A B = ((x : A) → typ (B x)) , (λ x → pt (B x))

-- KS Lemma 4.7.
ΩΠpt : (A : Type ℓ) (B : A → Pointed ℓ') → Ω (Πpt A B) ≡ Πpt A (λ x → Ω (B x))
ΩΠpt A B = ua∙ (isoToEquiv πIso) refl
  where
  πIso : Iso (typ (Ω (Πpt A B))) (typ (Πpt A (λ x → Ω (B x))))
  Iso.fun πIso p x i = p i x
  Iso.inv πIso h i x = h x i
  Iso.rightInv πIso h = refl
  Iso.leftInv πIso p = refl

Ω^Πpt : (n : ℕ) (A : Type ℓ) (B : A → Pointed ℓ')
  → (Ω^ n) (Πpt A B) ≡ Πpt A (λ x → (Ω^ n) (B x))
Ω^Πpt zero A B = refl
Ω^Πpt (suc n) A B =
  Ω^suc n (Πpt A B)
  ∙ cong (Ω^ n) (ΩΠpt A B)
  ∙ Ω^Πpt n A (λ x → Ω (B x))
  ∙ cong (Πpt A) (funExt λ x → sym (Ω^suc n (B x)))

U∙ : (X : Type ℓ) → Pointed (ℓ-suc ℓ)
U∙ {ℓ} X = Type ℓ , X

ΩU≃∙ : (X : Type ℓ) → Ω (U∙ X) ≃∙ ((X ≃ X) , idEquiv X)
ΩU≃∙ X = univalence , pathToEquivRefl

ΩEquiv≡ΩFun : (X : Type ℓ) → Ω ((X ≃ X) , idEquiv X) ≡ Ω ((X → X) , (λ x → x))
ΩEquiv≡ΩFun X = ua∙ ((λ p → cong fst p) , isEmbeddingFstΣProp (λ f → isPropIsEquiv f)) refl

-- KS Lemma 5.2 (local-global looping), as a POINTED equivalence.
localGlobal∙ : (n : ℕ) (X : Type ℓ)
  → (Ω^ (suc (suc n))) (U∙ X) ≃∙ Πpt X (λ x → (Ω^ (suc n)) (X , x))
localGlobal∙ n X =
  compEquiv∙ (pathToEquiv∙ (Ω^suc (suc n) (U∙ X)))
  (compEquiv∙ (Ω^≃∙ (suc n) (ΩU≃∙ X))
  (pathToEquiv∙
     (Ω^suc n ((X ≃ X) , idEquiv X)
     ∙ cong (Ω^ n) (ΩEquiv≡ΩFun X ∙ ΩΠpt X (λ x → X , x))
     ∙ Ω^Πpt n X (λ x → Ω (X , x))
     ∙ cong (Πpt X) (funExt λ x → sym (Ω^suc n (X , x))))))

------------------------------------------------------------------------
-- 2. Ω and Σ•.

-- KS Lemma 4.5 (pointed).
ΩΣ≃∙ : {A : Type ℓ} {B : A → Type ℓ'} (a : A) (b : B a)
  → Ω ((Σ A B) , (a , b)) ≃∙ ((Σ[ p ∈ a ≡ a ] PathP (λ i → B (p i)) b b) , (refl , refl))
ΩΣ≃∙ a b = isoToEquiv (invIso ΣPathIsoPathΣ) , refl

-- KS Lemma 5.1: a Σ-component of truncation level k-2 (h-level k) is
-- neutralised by Ω^k.
ΩΣtrunc : (k : ℕ) {A : Type ℓ} {B : A → Type ℓ'} (a : A) (b : B a)
  → ((x : A) → isOfHLevel k (B x))
  → (Ω^ k) ((Σ A B) , (a , b)) ≃∙ (Ω^ k) (A , a)
ΩΣtrunc zero a b h = Σ-contractSnd h , refl
ΩΣtrunc (suc k) {A} {B} a b h =
  compEquiv∙ (pathToEquiv∙ (Ω^suc k ((Σ A B) , (a , b))))
  (compEquiv∙ (Ω^≃∙ k (ΩΣ≃∙ a b))
  (compEquiv∙ (ΩΣtrunc k {A = a ≡ a} {B = λ p → PathP (λ i → B (p i)) b b} refl refl
                 (λ p → isOfHLevelPathP' k (h a) b b))
  (pathToEquiv∙ (sym (Ω^suc k (A , a))))))

------------------------------------------------------------------------
-- 3. The KS construction at an arbitrary universe level L and
--    truncation index k.

-- U^{<=k} at level L (KS Definition 5.3, with h-level 2+k = k-type).
T : (L : Level) (k : ℕ) → Type (ℓ-suc L)
T L k = TypeOfHLevel L (2 + k)

-- KS Lemma 5.5.
hT : (L : Level) (k : ℕ) → isOfHLevel (3 + k) (T L k)
hT L k = isOfHLevelTypeOfHLevel (2 + k)

-- KS P_k(X) := Ω^{k+1}(U^{<=k}, X).
P : (L : Level) (k : ℕ) → T L k → Pointed (ℓ-suc L)
P L k X = (Ω^ (suc k)) (T L k , X)

-- KS Corollary 5.6: P is a family of sets.
isSetP : (L : Level) (k : ℕ) (X : T L k) → isSet (typ (P L k X))
isSetP L k X = isOfHLevelΩ^ 2 (suc k) X (hT L k)

-- KS Loop_k := Σ (X : U^{<=k}) P_k(X).
Loop : (L : Level) (k : ℕ) → Type (ℓ-suc L)
Loop L k = Σ (T L k) (λ X → typ (P L k X))

-- KS Lemma 5.7: Loop_k is (k+1)-truncated.
hLoop : (L : Level) (k : ℕ) → isOfHLevel (3 + k) (Loop L k)
hLoop L k = isOfHLevelΣ (3 + k) (hT L k) (λ X → isOfHLevelPlus' {n = suc k} 2 (isSetP L k X))

-- The self-sliding square q⁻¹·q·q = q  (KS Lemma 5.8, case m = 0;
-- construction taken from GLM's NoHitGroupoidUniverse.agda, `D`).
D : {C : Type ℓ} {c : C} (q : c ≡ c) → PathP (λ i → q i ≡ q i) q q
D q = compPathL→PathP
  ( (sym q ∙ q ∙ q) ≡⟨ assoc (sym q) q q ⟩
    ((sym q ∙ q) ∙ q) ≡⟨ cong (λ s → s ∙ q) (lCancel q) ⟩
    (refl ∙ q) ≡⟨ sym (lUnit q) ⟩ q ∎ )

-- The pair (q , d_q) of KS Lemma 5.8, packaged with the pointed map E
-- that reads its first component back.
record LiftData (L : Level) (k : ℕ) (X : T L k) (q : typ (P L k X)) : Type (ℓ-suc L) where
  field
    E  : (Ω^ (suc k)) (Loop L k , (X , q)) →∙ P L k X
    ω  : typ ((Ω^ (suc k)) (Loop L k , (X , q)))
    Eω : fst E ω ≡ q

liftData : (L : Level) (k : ℕ) (X : T L k) (q : typ (P L k X)) → LiftData L k X q
-- m = 0: d_q is the square q⁻¹·q·q = q; E = cong fst.
liftData L zero X q = record
  { E  = (λ p → cong fst p) , refl
  ; ω  = ΣPathP (q , D q)
  ; Eω = refl }
-- m >= 1: the fibres are sets (Cor. 5.6), so by Lemma 5.1 the (m+1)-loops
-- of Loop at (X , q) ARE the (m+1)-loops of U^{<=m} at X; d_q is the
-- canonical (contractible) choice, realised here by the inverse map.
liftData L (suc k) X q = record
  { E  = ≃∙map e
  ; ω  = invEq (fst e) q
  ; Eω = secEq (fst e) q }
  where
  e : (Ω^ (suc (suc k))) (Loop L (suc k) , (X , q)) ≃∙ P L (suc k) X
  e = ΩΣtrunc (suc (suc k)) X q (λ Y → isOfHLevelPlus' {n = k} 2 (isSetP L (suc k) Y))

-- "U^{<=k} at level L has a non-trivial (k+1)-loop" (KS Lemma 5.8, the
-- strengthened form carried through the induction).
NT : (L : Level) (k : ℕ) → Type (ℓ-suc L)
NT L k = Σ[ W ∈ T L k ] Σ[ q ∈ typ (P L k W) ] ¬ (q ≡ pt (P L k W))

-- KS Lemma 5.8, induction step (at arbitrary L and k).
step : (L : Level) (k : ℕ) → NT L k → NT (ℓ-suc L) (suc k)
step L k (W , q̃ , nt) = W' , q' , nt'
  where
  W' : T (ℓ-suc L) (suc k)
  W' = Loop L k , hLoop L k

  -- ξ := λ (X , q) . (q , d_q)
  ξ : (z : Loop L k) → typ ((Ω^ (suc k)) (Loop L k , z))
  ξ (X , q) = LiftData.ω (liftData L k X q)

  -- Ω^{k+2}(U^{<=k+1}, (Loop, h)) ≃∙ Ω^{k+2}(U, Loop) ≃∙ Π• (z : Loop) Ω^{k+1}(Loop, z)
  G : (Ω^ (suc (suc k))) (T (ℓ-suc L) (suc k) , W')
      ≃∙ Πpt (Loop L k) (λ z → (Ω^ (suc k)) (Loop L k , z))
  G = compEquiv∙
        (ΩΣtrunc (suc (suc k)) (Loop L k) (hLoop L k)
           (λ Y → isProp→isOfHLevelSuc (suc k) (isPropIsOfHLevel (3 + k))))
        (localGlobal∙ k (Loop L k))

  q' : typ (P (ℓ-suc L) (suc k) W')
  q' = invEq (fst G) ξ

  nt' : ¬ (q' ≡ pt (P (ℓ-suc L) (suc k) W'))
  nt' r = nt (sym (LiftData.Eω ld) ∙ cong (fst (LiftData.E ld)) ωtriv ∙ snd (LiftData.E ld))
    where
    ξtriv : ξ ≡ pt (Πpt (Loop L k) (λ z → (Ω^ (suc k)) (Loop L k , z)))
    ξtriv = sym (secEq (fst G) ξ) ∙ cong (fst (fst G)) r ∙ snd G
    ld : LiftData L k W q̃
    ld = liftData L k W q̃
    ωtriv : LiftData.ω ld ≡ pt ((Ω^ (suc k)) (Loop L k , (W , q̃)))
    ωtriv = funExt⁻ ξtriv (W , q̃)

-- KS Lemma 5.8, base case: swap on 2 (Loop_{-1} := 2).
base : NT ℓ-zero 0
base = W₀ , q₀ , nt₀
  where
  W₀ : T ℓ-zero 0
  W₀ = Bool , isSetBool
  q₀ : W₀ ≡ W₀
  q₀ = ΣPathP (ua notEquiv , isProp→PathP (λ i → isPropIsOfHLevel 2) isSetBool isSetBool)
  nt₀ : ¬ (q₀ ≡ refl)
  nt₀ r = true≢false (sym (transportRefl true)
                      ∙ sym (cong (λ p → transport p true) (cong (cong fst) r))
                      ∙ uaβ notEquiv true)

------------------------------------------------------------------------
-- 4. From a non-trivial loop to "not an n-type" (KS Theorems 5.9, 5.10).

notHLevelT : (L : Level) (k : ℕ) → NT L k → ¬ isOfHLevel (2 + k) (T L k)
notHLevelT L k (W , q , nt) h = nt (sym (snd c q) ∙ snd c (pt (P L k W)))
  where
  c : isContr (typ (P L k W))
  c = hLevelΩ^ (suc k) W h

universeNotHLevel : (L : Level) (k : ℕ) → NT L k → ¬ isOfHLevel (2 + k) (Type L)
universeNotHLevel L k x h =
  notHLevelT L k x
    (isOfHLevelΣ (2 + k) h (λ X → isProp→isOfHLevelSuc (suc k) (isPropIsOfHLevel (2 + k))))

loopNotHLevel : (L : Level) (k : ℕ) → NT L k → ¬ isOfHLevel (2 + k) (Loop L k)
loopNotHLevel L k x h =
  notHLevelT L k x (isOfHLevelRetract (2 + k) (λ X → X , pt (P L k X)) fst (λ X → refl) h)

------------------------------------------------------------------------
-- 5. The tower U_0 : U_1 : U_2 : ...

lvl : ℕ → Level
lvl zero    = ℓ-zero
lvl (suc n) = ℓ-suc (lvl n)

tower : (n : ℕ) → NT (lvl n) n
tower zero    = base
tower (suc n) = step (lvl n) n (tower n)

-- KS Theorem 5.9: the universe U_n is not an n-type (h-level n+2).
KS-Theorem-5-9 : (n : ℕ) → ¬ isOfHLevel (2 + n) (Type (lvl n))
KS-Theorem-5-9 n = universeNotHLevel (lvl n) n (tower n)

-- KS Theorem 5.10: U_n^{<=n} and Loop_n are (n+1)-types but not n-types.
KS-Theorem-5-10-U≤ : (n : ℕ)
  → isOfHLevel (3 + n) (T (lvl n) n) × (¬ isOfHLevel (2 + n) (T (lvl n) n))
KS-Theorem-5-10-U≤ n = hT (lvl n) n , notHLevelT (lvl n) n (tower n)

KS-Theorem-5-10-Loop : (n : ℕ)
  → isOfHLevel (3 + n) (Loop (lvl n) n) × (¬ isOfHLevel (2 + n) (Loop (lvl n) n))
KS-Theorem-5-10-Loop n = hLoop (lvl n) n , loopNotHLevel (lvl n) n (tower n)

------------------------------------------------------------------------
-- 6. The work order's exact form (tail-recursive levels).

iterSuc : ℕ → Level → Level
iterSuc zero    ℓ = ℓ
iterSuc (suc n) ℓ = iterSuc n (ℓ-suc ℓ)

towerFrom : (n : ℕ) {L : Level} (k : ℕ) → NT L k → NT (iterSuc n L) (n + k)
towerFrom zero        k x = x
towerFrom (suc n) {L} k x =
  subst (NT (iterSuc n (ℓ-suc L))) (+-suc n k) (towerFrom n (suc k) (step L k x))

workOrderForm : (n : ℕ) → ¬ isOfHLevel (n + 2) (Type (iterSuc n ℓ-zero))
workOrderForm n =
  subst (λ j → ¬ isOfHLevel j (Type (iterSuc n ℓ-zero))) (+-comm 2 n)
    (universeNotHLevel (iterSuc n ℓ-zero) n
      (subst (NT (iterSuc n ℓ-zero)) (+-zero n) (towerFrom n 0 base)))

------------------------------------------------------------------------
-- 7. Instances (sanity anchors against the earlier packages).

-- n = 0: C-63 (Opus): Type₀ is not a set.
instance-n0 : ¬ isSet (Type ℓ-zero)
instance-n0 = KS-Theorem-5-9 0

-- n = 1: GLM-R3-C01: Type₁ is not a groupoid.
instance-n1 : ¬ isOfHLevel 3 (Type (ℓ-suc ℓ-zero))
instance-n1 = KS-Theorem-5-9 1

-- n = 2: new: Type₂ is not a 2-groupoid.
instance-n2 : ¬ isOfHLevel 4 (Type (ℓ-suc (ℓ-suc ℓ-zero)))
instance-n2 = KS-Theorem-5-9 2
