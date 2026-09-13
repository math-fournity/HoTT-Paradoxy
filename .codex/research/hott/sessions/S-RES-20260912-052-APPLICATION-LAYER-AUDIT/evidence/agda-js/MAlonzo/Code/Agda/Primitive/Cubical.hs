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

module MAlonzo.Code.Agda.Primitive.Cubical where

import MAlonzo.RTE (coe, erased, AgdaAny, addInt, subInt, mulInt,
                    quotInt, remInt, geqInt, ltInt, eqInt, add64, sub64, mul64, quot64,
                    rem64, lt64, eq64, word64FromNat, word64ToNat)
import qualified MAlonzo.RTE
import qualified Data.Text

-- Agda.Primitive.Cubical.I
d_I_8 = ()
data T_I_8 = C_i1_12 | C_i0_10
-- Agda.Primitive.Cubical.primIMin
d_primIMin_14 = (&&)
-- Agda.Primitive.Cubical.primIMax
d_primIMax_16 = (||)
-- Agda.Primitive.Cubical.primINeg
d_primINeg_18 = not
-- Agda.Primitive.Cubical.IsOne
type T_IsOne_20 a0 = ()
d_IsOne_20 = ()
-- Agda.Primitive.Cubical.itIsOne
d_itIsOne_22 = ()
-- Agda.Primitive.Cubical.IsOne1
d_IsOne1_28 = \_ _ _ -> ()
-- Agda.Primitive.Cubical.IsOne2
d_IsOne2_34 = \_ _ _ -> ()
-- Agda.Primitive.Cubical.Partial
d_Partial_36 = \_ _ x -> x
-- Agda.Primitive.Cubical.PartialP
d_PartialP_38 = \_ _ x -> x
-- Agda.Primitive.Cubical.isOneEmpty
d_isOneEmpty_44 = \_ x _ -> x ()
-- Agda.Primitive.Cubical.primPOr
d_primPOr_62 = \_ i _ _ x y -> if i then x else y
-- Agda.Primitive.Cubical.primComp
d_primComp_78 = \_ _ _ _ x -> x
-- Agda.Primitive.Cubical.primTransp
d_primTransp_90 = \_ _ _ x -> x
-- Agda.Primitive.Cubical.primHComp
d_primHComp_104 = \_ _ _ _ x -> x
-- Agda.Primitive.Cubical.PathP
type T_PathP_110 a0 a1 a2 a3 = T_I_8 -> AgdaAny
d_PathP_110 = \_ _ _ _ -> ()
