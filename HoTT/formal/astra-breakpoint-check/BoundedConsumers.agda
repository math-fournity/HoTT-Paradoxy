{-# OPTIONS --safe --cubical --guardedness #-}
module BoundedConsumers where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool
open import Cubical.Data.Empty
id : Bool → Bool
id x = x

c000f : Bool → Bool
c000f false = false
c000f true = false
c000 : Bool → Bool
c000 x = c000f x
c000compatible : (a b : Bool) → c000 a ≡ c000 b
c000compatible false false = refl
c000compatible false true = refl
c000compatible true false = refl
c000compatible true true = refl

c001f : Bool → Bool
c001f false = false
c001f true = true
c001 : Bool → Bool
c001 x = c001f x
c001incompatible : ((a b : Bool) → c001 a ≡ c001 b) → ⊥
c001incompatible p = true≢false (p true false)

c002f : Bool → Bool
c002f false = true
c002f true = false
c002 : Bool → Bool
c002 x = c002f x
c002incompatible : ((a b : Bool) → c002 a ≡ c002 b) → ⊥
c002incompatible p = false≢true (p true false)

c003f : Bool → Bool
c003f false = true
c003f true = true
c003 : Bool → Bool
c003 x = c003f x
c003compatible : (a b : Bool) → c003 a ≡ c003 b
c003compatible false false = refl
c003compatible false true = refl
c003compatible true false = refl
c003compatible true true = refl

c004f : Bool → Bool
c004f false = false
c004f true = false
c004 : Bool → Bool
c004 x = c004f (id x)
c004compatible : (a b : Bool) → c004 a ≡ c004 b
c004compatible false false = refl
c004compatible false true = refl
c004compatible true false = refl
c004compatible true true = refl

c005f : Bool → Bool
c005f false = false
c005f true = true
c005 : Bool → Bool
c005 x = c005f (id x)
c005incompatible : ((a b : Bool) → c005 a ≡ c005 b) → ⊥
c005incompatible p = true≢false (p true false)

c006f : Bool → Bool
c006f false = true
c006f true = false
c006 : Bool → Bool
c006 x = c006f (id x)
c006incompatible : ((a b : Bool) → c006 a ≡ c006 b) → ⊥
c006incompatible p = false≢true (p true false)

c007f : Bool → Bool
c007f false = true
c007f true = true
c007 : Bool → Bool
c007 x = c007f (id x)
c007compatible : (a b : Bool) → c007 a ≡ c007 b
c007compatible false false = refl
c007compatible false true = refl
c007compatible true false = refl
c007compatible true true = refl

c008f : Bool → Bool
c008f false = false
c008f true = false
c008 : Bool → Bool
c008 x = c008f (not x)
c008compatible : (a b : Bool) → c008 a ≡ c008 b
c008compatible false false = refl
c008compatible false true = refl
c008compatible true false = refl
c008compatible true true = refl

c009f : Bool → Bool
c009f false = false
c009f true = true
c009 : Bool → Bool
c009 x = c009f (not x)
c009incompatible : ((a b : Bool) → c009 a ≡ c009 b) → ⊥
c009incompatible p = false≢true (p true false)

c010f : Bool → Bool
c010f false = true
c010f true = false
c010 : Bool → Bool
c010 x = c010f (not x)
c010incompatible : ((a b : Bool) → c010 a ≡ c010 b) → ⊥
c010incompatible p = true≢false (p true false)

c011f : Bool → Bool
c011f false = true
c011f true = true
c011 : Bool → Bool
c011 x = c011f (not x)
c011compatible : (a b : Bool) → c011 a ≡ c011 b
c011compatible false false = refl
c011compatible false true = refl
c011compatible true false = refl
c011compatible true true = refl

c012f : Bool → Bool
c012f false = false
c012f true = false
c012 : Bool → Bool
c012 x = c012f (id (id x))
c012compatible : (a b : Bool) → c012 a ≡ c012 b
c012compatible false false = refl
c012compatible false true = refl
c012compatible true false = refl
c012compatible true true = refl

c013f : Bool → Bool
c013f false = false
c013f true = true
c013 : Bool → Bool
c013 x = c013f (id (id x))
c013incompatible : ((a b : Bool) → c013 a ≡ c013 b) → ⊥
c013incompatible p = true≢false (p true false)

c014f : Bool → Bool
c014f false = true
c014f true = false
c014 : Bool → Bool
c014 x = c014f (id (id x))
c014incompatible : ((a b : Bool) → c014 a ≡ c014 b) → ⊥
c014incompatible p = false≢true (p true false)

c015f : Bool → Bool
c015f false = true
c015f true = true
c015 : Bool → Bool
c015 x = c015f (id (id x))
c015compatible : (a b : Bool) → c015 a ≡ c015 b
c015compatible false false = refl
c015compatible false true = refl
c015compatible true false = refl
c015compatible true true = refl

c016f : Bool → Bool
c016f false = false
c016f true = false
c016 : Bool → Bool
c016 x = c016f (not (id x))
c016compatible : (a b : Bool) → c016 a ≡ c016 b
c016compatible false false = refl
c016compatible false true = refl
c016compatible true false = refl
c016compatible true true = refl

c017f : Bool → Bool
c017f false = false
c017f true = true
c017 : Bool → Bool
c017 x = c017f (not (id x))
c017incompatible : ((a b : Bool) → c017 a ≡ c017 b) → ⊥
c017incompatible p = false≢true (p true false)

c018f : Bool → Bool
c018f false = true
c018f true = false
c018 : Bool → Bool
c018 x = c018f (not (id x))
c018incompatible : ((a b : Bool) → c018 a ≡ c018 b) → ⊥
c018incompatible p = true≢false (p true false)

c019f : Bool → Bool
c019f false = true
c019f true = true
c019 : Bool → Bool
c019 x = c019f (not (id x))
c019compatible : (a b : Bool) → c019 a ≡ c019 b
c019compatible false false = refl
c019compatible false true = refl
c019compatible true false = refl
c019compatible true true = refl

c020f : Bool → Bool
c020f false = false
c020f true = false
c020 : Bool → Bool
c020 x = c020f (id (not x))
c020compatible : (a b : Bool) → c020 a ≡ c020 b
c020compatible false false = refl
c020compatible false true = refl
c020compatible true false = refl
c020compatible true true = refl

c021f : Bool → Bool
c021f false = false
c021f true = true
c021 : Bool → Bool
c021 x = c021f (id (not x))
c021incompatible : ((a b : Bool) → c021 a ≡ c021 b) → ⊥
c021incompatible p = false≢true (p true false)

c022f : Bool → Bool
c022f false = true
c022f true = false
c022 : Bool → Bool
c022 x = c022f (id (not x))
c022incompatible : ((a b : Bool) → c022 a ≡ c022 b) → ⊥
c022incompatible p = true≢false (p true false)

c023f : Bool → Bool
c023f false = true
c023f true = true
c023 : Bool → Bool
c023 x = c023f (id (not x))
c023compatible : (a b : Bool) → c023 a ≡ c023 b
c023compatible false false = refl
c023compatible false true = refl
c023compatible true false = refl
c023compatible true true = refl

c024f : Bool → Bool
c024f false = false
c024f true = false
c024 : Bool → Bool
c024 x = c024f (not (not x))
c024compatible : (a b : Bool) → c024 a ≡ c024 b
c024compatible false false = refl
c024compatible false true = refl
c024compatible true false = refl
c024compatible true true = refl

c025f : Bool → Bool
c025f false = false
c025f true = true
c025 : Bool → Bool
c025 x = c025f (not (not x))
c025incompatible : ((a b : Bool) → c025 a ≡ c025 b) → ⊥
c025incompatible p = true≢false (p true false)

c026f : Bool → Bool
c026f false = true
c026f true = false
c026 : Bool → Bool
c026 x = c026f (not (not x))
c026incompatible : ((a b : Bool) → c026 a ≡ c026 b) → ⊥
c026incompatible p = false≢true (p true false)

c027f : Bool → Bool
c027f false = true
c027f true = true
c027 : Bool → Bool
c027 x = c027f (not (not x))
c027compatible : (a b : Bool) → c027 a ≡ c027 b
c027compatible false false = refl
c027compatible false true = refl
c027compatible true false = refl
c027compatible true true = refl

c028f : Bool → Bool
c028f false = false
c028f true = false
c028 : Bool → Bool
c028 x = c028f (id (id (id x)))
c028compatible : (a b : Bool) → c028 a ≡ c028 b
c028compatible false false = refl
c028compatible false true = refl
c028compatible true false = refl
c028compatible true true = refl

c029f : Bool → Bool
c029f false = false
c029f true = true
c029 : Bool → Bool
c029 x = c029f (id (id (id x)))
c029incompatible : ((a b : Bool) → c029 a ≡ c029 b) → ⊥
c029incompatible p = true≢false (p true false)

c030f : Bool → Bool
c030f false = true
c030f true = false
c030 : Bool → Bool
c030 x = c030f (id (id (id x)))
c030incompatible : ((a b : Bool) → c030 a ≡ c030 b) → ⊥
c030incompatible p = false≢true (p true false)

c031f : Bool → Bool
c031f false = true
c031f true = true
c031 : Bool → Bool
c031 x = c031f (id (id (id x)))
c031compatible : (a b : Bool) → c031 a ≡ c031 b
c031compatible false false = refl
c031compatible false true = refl
c031compatible true false = refl
c031compatible true true = refl

c032f : Bool → Bool
c032f false = false
c032f true = false
c032 : Bool → Bool
c032 x = c032f (not (id (id x)))
c032compatible : (a b : Bool) → c032 a ≡ c032 b
c032compatible false false = refl
c032compatible false true = refl
c032compatible true false = refl
c032compatible true true = refl

c033f : Bool → Bool
c033f false = false
c033f true = true
c033 : Bool → Bool
c033 x = c033f (not (id (id x)))
c033incompatible : ((a b : Bool) → c033 a ≡ c033 b) → ⊥
c033incompatible p = false≢true (p true false)

c034f : Bool → Bool
c034f false = true
c034f true = false
c034 : Bool → Bool
c034 x = c034f (not (id (id x)))
c034incompatible : ((a b : Bool) → c034 a ≡ c034 b) → ⊥
c034incompatible p = true≢false (p true false)

c035f : Bool → Bool
c035f false = true
c035f true = true
c035 : Bool → Bool
c035 x = c035f (not (id (id x)))
c035compatible : (a b : Bool) → c035 a ≡ c035 b
c035compatible false false = refl
c035compatible false true = refl
c035compatible true false = refl
c035compatible true true = refl

c036f : Bool → Bool
c036f false = false
c036f true = false
c036 : Bool → Bool
c036 x = c036f (id (not (id x)))
c036compatible : (a b : Bool) → c036 a ≡ c036 b
c036compatible false false = refl
c036compatible false true = refl
c036compatible true false = refl
c036compatible true true = refl

c037f : Bool → Bool
c037f false = false
c037f true = true
c037 : Bool → Bool
c037 x = c037f (id (not (id x)))
c037incompatible : ((a b : Bool) → c037 a ≡ c037 b) → ⊥
c037incompatible p = false≢true (p true false)

c038f : Bool → Bool
c038f false = true
c038f true = false
c038 : Bool → Bool
c038 x = c038f (id (not (id x)))
c038incompatible : ((a b : Bool) → c038 a ≡ c038 b) → ⊥
c038incompatible p = true≢false (p true false)

c039f : Bool → Bool
c039f false = true
c039f true = true
c039 : Bool → Bool
c039 x = c039f (id (not (id x)))
c039compatible : (a b : Bool) → c039 a ≡ c039 b
c039compatible false false = refl
c039compatible false true = refl
c039compatible true false = refl
c039compatible true true = refl

c040f : Bool → Bool
c040f false = false
c040f true = false
c040 : Bool → Bool
c040 x = c040f (not (not (id x)))
c040compatible : (a b : Bool) → c040 a ≡ c040 b
c040compatible false false = refl
c040compatible false true = refl
c040compatible true false = refl
c040compatible true true = refl

c041f : Bool → Bool
c041f false = false
c041f true = true
c041 : Bool → Bool
c041 x = c041f (not (not (id x)))
c041incompatible : ((a b : Bool) → c041 a ≡ c041 b) → ⊥
c041incompatible p = true≢false (p true false)

c042f : Bool → Bool
c042f false = true
c042f true = false
c042 : Bool → Bool
c042 x = c042f (not (not (id x)))
c042incompatible : ((a b : Bool) → c042 a ≡ c042 b) → ⊥
c042incompatible p = false≢true (p true false)

c043f : Bool → Bool
c043f false = true
c043f true = true
c043 : Bool → Bool
c043 x = c043f (not (not (id x)))
c043compatible : (a b : Bool) → c043 a ≡ c043 b
c043compatible false false = refl
c043compatible false true = refl
c043compatible true false = refl
c043compatible true true = refl

c044f : Bool → Bool
c044f false = false
c044f true = false
c044 : Bool → Bool
c044 x = c044f (id (id (not x)))
c044compatible : (a b : Bool) → c044 a ≡ c044 b
c044compatible false false = refl
c044compatible false true = refl
c044compatible true false = refl
c044compatible true true = refl

c045f : Bool → Bool
c045f false = false
c045f true = true
c045 : Bool → Bool
c045 x = c045f (id (id (not x)))
c045incompatible : ((a b : Bool) → c045 a ≡ c045 b) → ⊥
c045incompatible p = false≢true (p true false)

c046f : Bool → Bool
c046f false = true
c046f true = false
c046 : Bool → Bool
c046 x = c046f (id (id (not x)))
c046incompatible : ((a b : Bool) → c046 a ≡ c046 b) → ⊥
c046incompatible p = true≢false (p true false)

c047f : Bool → Bool
c047f false = true
c047f true = true
c047 : Bool → Bool
c047 x = c047f (id (id (not x)))
c047compatible : (a b : Bool) → c047 a ≡ c047 b
c047compatible false false = refl
c047compatible false true = refl
c047compatible true false = refl
c047compatible true true = refl

c048f : Bool → Bool
c048f false = false
c048f true = false
c048 : Bool → Bool
c048 x = c048f (not (id (not x)))
c048compatible : (a b : Bool) → c048 a ≡ c048 b
c048compatible false false = refl
c048compatible false true = refl
c048compatible true false = refl
c048compatible true true = refl

c049f : Bool → Bool
c049f false = false
c049f true = true
c049 : Bool → Bool
c049 x = c049f (not (id (not x)))
c049incompatible : ((a b : Bool) → c049 a ≡ c049 b) → ⊥
c049incompatible p = true≢false (p true false)

c050f : Bool → Bool
c050f false = true
c050f true = false
c050 : Bool → Bool
c050 x = c050f (not (id (not x)))
c050incompatible : ((a b : Bool) → c050 a ≡ c050 b) → ⊥
c050incompatible p = false≢true (p true false)

c051f : Bool → Bool
c051f false = true
c051f true = true
c051 : Bool → Bool
c051 x = c051f (not (id (not x)))
c051compatible : (a b : Bool) → c051 a ≡ c051 b
c051compatible false false = refl
c051compatible false true = refl
c051compatible true false = refl
c051compatible true true = refl

c052f : Bool → Bool
c052f false = false
c052f true = false
c052 : Bool → Bool
c052 x = c052f (id (not (not x)))
c052compatible : (a b : Bool) → c052 a ≡ c052 b
c052compatible false false = refl
c052compatible false true = refl
c052compatible true false = refl
c052compatible true true = refl

c053f : Bool → Bool
c053f false = false
c053f true = true
c053 : Bool → Bool
c053 x = c053f (id (not (not x)))
c053incompatible : ((a b : Bool) → c053 a ≡ c053 b) → ⊥
c053incompatible p = true≢false (p true false)

c054f : Bool → Bool
c054f false = true
c054f true = false
c054 : Bool → Bool
c054 x = c054f (id (not (not x)))
c054incompatible : ((a b : Bool) → c054 a ≡ c054 b) → ⊥
c054incompatible p = false≢true (p true false)

c055f : Bool → Bool
c055f false = true
c055f true = true
c055 : Bool → Bool
c055 x = c055f (id (not (not x)))
c055compatible : (a b : Bool) → c055 a ≡ c055 b
c055compatible false false = refl
c055compatible false true = refl
c055compatible true false = refl
c055compatible true true = refl

c056f : Bool → Bool
c056f false = false
c056f true = false
c056 : Bool → Bool
c056 x = c056f (not (not (not x)))
c056compatible : (a b : Bool) → c056 a ≡ c056 b
c056compatible false false = refl
c056compatible false true = refl
c056compatible true false = refl
c056compatible true true = refl

c057f : Bool → Bool
c057f false = false
c057f true = true
c057 : Bool → Bool
c057 x = c057f (not (not (not x)))
c057incompatible : ((a b : Bool) → c057 a ≡ c057 b) → ⊥
c057incompatible p = false≢true (p true false)

c058f : Bool → Bool
c058f false = true
c058f true = false
c058 : Bool → Bool
c058 x = c058f (not (not (not x)))
c058incompatible : ((a b : Bool) → c058 a ≡ c058 b) → ⊥
c058incompatible p = true≢false (p true false)

c059f : Bool → Bool
c059f false = true
c059f true = true
c059 : Bool → Bool
c059 x = c059f (not (not (not x)))
c059compatible : (a b : Bool) → c059 a ≡ c059 b
c059compatible false false = refl
c059compatible false true = refl
c059compatible true false = refl
c059compatible true true = refl

