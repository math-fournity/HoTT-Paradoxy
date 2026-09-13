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

module MAlonzo.Code.ErasedCubicalImport where

import MAlonzo.RTE (coe, erased, AgdaAny, addInt, subInt, mulInt,
                    quotInt, remInt, geqInt, ltInt, eqInt, add64, sub64, mul64, quot64,
                    rem64, lt64, eq64, word64FromNat, word64ToNat)
import qualified MAlonzo.RTE
import qualified Data.Text
import qualified MAlonzo.Code.Agda.Builtin.Bool
import qualified MAlonzo.Code.Agda.Builtin.IO
import qualified MAlonzo.Code.Agda.Builtin.String
import qualified MAlonzo.Code.Agda.Builtin.Unit

-- ErasedCubicalImport.putStrLn
d_putStrLn_2
  = error
      "MAlonzo Runtime Error: postulate evaluated: ErasedCubicalImport.putStrLn"
-- ErasedCubicalImport.render
d_render_4 :: Bool -> MAlonzo.Code.Agda.Builtin.String.T_String_6
d_render_4 v0
  = if coe v0
      then coe ("TRUE" :: Data.Text.Text)
      else coe ("FALSE" :: Data.Text.Text)
-- ErasedCubicalImport.myNot
d_myNot_6 :: Bool -> Bool
d_myNot_6 v0
  = if coe v0
      then coe MAlonzo.Code.Agda.Builtin.Bool.C_false_8
      else coe MAlonzo.Code.Agda.Builtin.Bool.C_true_10
-- ErasedCubicalImport._++_
d__'43''43'__8 ::
  MAlonzo.Code.Agda.Builtin.String.T_String_6 ->
  MAlonzo.Code.Agda.Builtin.String.T_String_6 ->
  MAlonzo.Code.Agda.Builtin.String.T_String_6
d__'43''43'__8
  = coe MAlonzo.Code.Agda.Builtin.String.d_primStringAppend_16
main = coe d_main_10
-- ErasedCubicalImport.main
d_main_10 ::
  MAlonzo.Code.Agda.Builtin.IO.T_IO_8
    AgdaAny MAlonzo.Code.Agda.Builtin.Unit.T_'8868'_6
d_main_10
  = coe
      d_putStrLn_2
      (coe
         d__'43''43'__8 ("LOCAL_NOT_TRUE=" :: Data.Text.Text)
         (coe
            d__'43''43'__8
            (d_render_4
               (coe d_myNot_6 (coe MAlonzo.Code.Agda.Builtin.Bool.C_true_10)))
            (coe
               d__'43''43'__8 (";LIB_CONSTRUCTOR=" :: Data.Text.Text)
               (d_render_4 (coe MAlonzo.Code.Agda.Builtin.Bool.C_true_10)))))
