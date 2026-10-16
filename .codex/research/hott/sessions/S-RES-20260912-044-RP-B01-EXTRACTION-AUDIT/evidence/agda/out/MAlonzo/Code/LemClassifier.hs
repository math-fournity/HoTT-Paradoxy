{-# LANGUAGE BangPatterns #-}
{-# LANGUAGE EmptyCase #-}
{-# LANGUAGE EmptyDataDecls #-}
{-# LANGUAGE ExistentialQuantification #-}
{-# LANGUAGE NoMonomorphismRestriction #-}
{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE PatternSynonyms #-}
{-# LANGUAGE RankNTypes #-}
{-# LANGUAGE ScopedTypeVariables #-}

{-# OPTIONS_GHC -Wno-overlapping-patterns #-}

module MAlonzo.Code.LemClassifier where

import MAlonzo.RTE (coe, erased, AgdaAny, addInt, subInt, mulInt,
                    quotInt, remInt, geqInt, ltInt, eqInt, add64, sub64, mul64, quot64,
                    rem64, lt64, eq64, word64FromNat, word64ToNat)
import qualified MAlonzo.RTE
import qualified Data.Text

-- LemClassifier.Bool
d_Bool_2 = ()
data T_Bool_2 = C_true_4 | C_false_6
-- LemClassifier.⊥
d_'8869'_8 = ()
data T_'8869'_8
-- LemClassifier._⊎_
d__'8846'__14 a0 a1 = ()
data T__'8846'__14
  = C_inj'8321'_20 AgdaAny | C_inj'8322'_22 AgdaAny
-- LemClassifier.ℕ
d_ℕ_24 = ()
data T_ℕ_24 = C_zero_26 | C_suc_28 T_ℕ_24
-- LemClassifier.lem
d_lem_32
  = error
      "MAlonzo Runtime Error: postulate evaluated: LemClassifier.lem"
-- LemClassifier.chi
d_chi_36 :: () -> T_Bool_2
d_chi_36 ~v0 = du_chi_36
du_chi_36 :: T_Bool_2
du_chi_36
  = let v0 = coe d_lem_32 erased in
    coe
      (case coe v0 of
         C_inj'8321'_20 v1 -> coe C_true_4
         C_inj'8322'_22 v1 -> coe C_false_6
         _ -> MAlonzo.RTE.mazUnreachableError)
-- LemClassifier.equalConst
d_equalConst_50 :: () -> T_Bool_2
d_equalConst_50 ~v0 = du_equalConst_50
du_equalConst_50 :: T_Bool_2
du_equalConst_50
  = let v0 = coe d_lem_32 erased in
    coe (coe seq (coe v0) (coe C_true_4))
-- LemClassifier.haltWithin
d_haltWithin_62 :: T_ℕ_24 -> T_Bool_2
d_haltWithin_62 ~v0 = du_haltWithin_62
du_haltWithin_62 :: T_Bool_2
du_haltWithin_62 = coe C_true_4
