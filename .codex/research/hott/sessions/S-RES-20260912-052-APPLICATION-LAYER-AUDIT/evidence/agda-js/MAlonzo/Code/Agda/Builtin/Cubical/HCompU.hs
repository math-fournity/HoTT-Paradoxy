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

module MAlonzo.Code.Agda.Builtin.Cubical.HCompU where

import MAlonzo.RTE (coe, erased, AgdaAny, addInt, subInt, mulInt,
                    quotInt, remInt, geqInt, ltInt, eqInt, add64, sub64, mul64, quot64,
                    rem64, lt64, eq64, word64FromNat, word64ToNat)
import qualified MAlonzo.RTE
import qualified Data.Text
import qualified MAlonzo.Code.Agda.Builtin.Cubical.Sub
import qualified MAlonzo.Code.Agda.Builtin.Sigma
import qualified MAlonzo.Code.Agda.Primitive
import qualified MAlonzo.Code.Agda.Primitive.Cubical

-- Agda.Builtin.Cubical.HCompU.Helpers.hfill
d_hfill_24 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  () ->
  MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
  (MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
   AgdaAny -> AgdaAny) ->
  AgdaAny -> MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> AgdaAny
d_hfill_24 v0 ~v1 v2 v3 v4 v5 = du_hfill_24 v0 v2 v3 v4 v5
du_hfill_24 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
  (MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
   AgdaAny -> AgdaAny) ->
  AgdaAny -> MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> AgdaAny
du_hfill_24 v0 v1 v2 v3 v4
  = coe
      MAlonzo.Code.Agda.Primitive.Cubical.d_primHComp_104 v0 erased
      (coe
         MAlonzo.Code.Agda.Primitive.Cubical.d_primIMax_16 v1
         (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primINeg_18 v4))
      (\ v5 ->
         let v6
               = case coe v4 of
                   MAlonzo.Code.Agda.Primitive.Cubical.C_i0_10
                     -> coe
                          (\ v6 ->
                             coe
                               MAlonzo.Code.Agda.Builtin.Cubical.Sub.d_primSubOut_30 v0 erased v1
                               (coe v2 v4) v3)
                   _ -> erased in
         coe
           (case coe v1 of
              MAlonzo.Code.Agda.Primitive.Cubical.C_i1_12
                -> coe
                     (\ v7 ->
                        coe
                          v2 (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primIMin_14 v4 v5)
                          erased)
              _ -> coe v6))
      (coe
         MAlonzo.Code.Agda.Builtin.Cubical.Sub.d_primSubOut_30 v0 erased v1
         (coe v2 (coe MAlonzo.Code.Agda.Primitive.Cubical.C_i0_10)) v3)
-- Agda.Builtin.Cubical.HCompU.Helpers.fill
d_fill_54 ::
  (MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
   MAlonzo.Code.Agda.Primitive.T_Level_18) ->
  (MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> ()) ->
  MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
  (MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
   AgdaAny -> AgdaAny) ->
  AgdaAny -> MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> AgdaAny
d_fill_54 v0 ~v1 v2 v3 v4 v5 = du_fill_54 v0 v2 v3 v4 v5
du_fill_54 ::
  (MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
   MAlonzo.Code.Agda.Primitive.T_Level_18) ->
  MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
  (MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
   AgdaAny -> AgdaAny) ->
  AgdaAny -> MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> AgdaAny
du_fill_54 v0 v1 v2 v3 v4
  = coe
      MAlonzo.Code.Agda.Primitive.Cubical.d_primComp_78
      (\ v5 ->
         coe
           v0 (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primIMin_14 v4 v5))
      erased
      (coe
         MAlonzo.Code.Agda.Primitive.Cubical.d_primIMax_16 v1
         (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primINeg_18 v4))
      (\ v5 ->
         let v6
               = case coe v4 of
                   MAlonzo.Code.Agda.Primitive.Cubical.C_i0_10
                     -> coe
                          (\ v6 ->
                             coe
                               MAlonzo.Code.Agda.Builtin.Cubical.Sub.d_primSubOut_30 (coe v0 v4)
                               erased v1 (coe v2 v4) v3)
                   _ -> erased in
         coe
           (case coe v1 of
              MAlonzo.Code.Agda.Primitive.Cubical.C_i1_12
                -> coe
                     (\ v7 ->
                        coe
                          v2 (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primIMin_14 v4 v5)
                          erased)
              _ -> coe v6))
      (coe
         MAlonzo.Code.Agda.Builtin.Cubical.Sub.d_primSubOut_30
         (coe v0 (coe MAlonzo.Code.Agda.Primitive.Cubical.C_i0_10)) erased
         v1 (coe v2 (coe MAlonzo.Code.Agda.Primitive.Cubical.C_i0_10)) v3)
-- Agda.Builtin.Cubical.HCompU.Helpers._.refl
d_refl_82 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  () ->
  AgdaAny -> MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> AgdaAny
d_refl_82 ~v0 ~v1 v2 ~v3 = du_refl_82 v2
du_refl_82 :: AgdaAny -> AgdaAny
du_refl_82 v0 = coe v0
-- Agda.Builtin.Cubical.HCompU.Helpers._.sym
d_sym_92 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  () ->
  AgdaAny ->
  AgdaAny ->
  AgdaAny -> MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> AgdaAny
d_sym_92 ~v0 ~v1 ~v2 ~v3 v4 v5 = du_sym_92 v4 v5
du_sym_92 ::
  AgdaAny -> MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> AgdaAny
du_sym_92 v0 v1
  = coe v0 (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primINeg_18 v1)
-- Agda.Builtin.Cubical.HCompU.Helpers._.cong
d_cong_114 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  () ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  (AgdaAny -> ()) ->
  AgdaAny ->
  AgdaAny ->
  (AgdaAny -> AgdaAny) ->
  AgdaAny -> MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> AgdaAny
d_cong_114 ~v0 ~v1 ~v2 ~v3 ~v4 ~v5 v6 v7 v8 = du_cong_114 v6 v7 v8
du_cong_114 ::
  (AgdaAny -> AgdaAny) ->
  AgdaAny -> MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> AgdaAny
du_cong_114 v0 v1 v2 = coe v0 (coe v1 v2)
-- Agda.Builtin.Cubical.HCompU.Helpers.isContr
d_isContr_124 :: MAlonzo.Code.Agda.Primitive.T_Level_18 -> () -> ()
d_isContr_124 = erased
-- Agda.Builtin.Cubical.HCompU.Helpers.fiber
d_fiber_144 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  () -> () -> (AgdaAny -> AgdaAny) -> AgdaAny -> ()
d_fiber_144 = erased
-- Agda.Builtin.Cubical.HCompU.prim^glueU
d_prim'94'glueU_162 = \_ _ _ _ _ x -> x
-- Agda.Builtin.Cubical.HCompU.prim^unglueU
d_prim'94'unglueU_172 = \_ _ _ _ x -> x
-- Agda.Builtin.Cubical.HCompU.primFaceForall
d_primFaceForall_174 = \f -> f True == True && f False == True
-- Agda.Builtin.Cubical.HCompU.transpProof
d_transpProof_192 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  (MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> ()) ->
  MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
  (AgdaAny -> AgdaAny) ->
  AgdaAny -> MAlonzo.Code.Agda.Builtin.Sigma.T_Σ_14
d_transpProof_192 v0 ~v1 v2 v3 v4 = du_transpProof_192 v0 v2 v3 v4
du_transpProof_192 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
  (AgdaAny -> AgdaAny) ->
  AgdaAny -> MAlonzo.Code.Agda.Builtin.Sigma.T_Σ_14
du_transpProof_192 v0 v1 v2 v3
  = coe
      MAlonzo.Code.Agda.Builtin.Sigma.C__'44'__32
      (coe du_f_228 (coe v0) (coe v1) (coe v2) (coe v3))
      (coe
         (\ v4 ->
            coe
              MAlonzo.Code.Agda.Primitive.Cubical.d_primComp_78 (\ v5 -> v0)
              erased
              (coe
                 MAlonzo.Code.Agda.Primitive.Cubical.d_primIMax_16 v1
                 (coe
                    MAlonzo.Code.Agda.Primitive.Cubical.d_primIMax_16
                    (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primINeg_18 v4) v4))
              (\ v5 ->
                 let v6
                       = case coe v4 of
                           MAlonzo.Code.Agda.Primitive.Cubical.C_i0_10
                             -> coe
                                  (\ v6 ->
                                     coe
                                       MAlonzo.Code.Agda.Primitive.Cubical.d_primTransp_90
                                       (\ v7 -> v0) erased
                                       (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primINeg_18 v5)
                                       (coe du_f_228 (coe v0) (coe v1) (coe v2) (coe v3)))
                           MAlonzo.Code.Agda.Primitive.Cubical.C_i1_12
                             -> coe
                                  (\ v6 ->
                                     coe
                                       du_g_214 (coe v0) (coe v1) (coe v2) (coe v3)
                                       (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primINeg_18 v5))
                           _ -> MAlonzo.RTE.mazUnreachableError in
                 coe
                   (case coe v1 of
                      MAlonzo.Code.Agda.Primitive.Cubical.C_i1_12
                        -> coe
                             (\ v7 ->
                                coe
                                  MAlonzo.Code.Agda.Primitive.Cubical.d_primTransp_90 (\ v8 -> v0)
                                  erased (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primINeg_18 v5)
                                  (coe v2 erased))
                      _ -> coe v6))
              (coe du_f_228 (coe v0) (coe v1) (coe v2) (coe v3))))
-- Agda.Builtin.Cubical.HCompU._.b'
d_b''_206 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  (MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> ()) ->
  MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
  (AgdaAny -> AgdaAny) -> AgdaAny -> AgdaAny
d_b''_206 v0 ~v1 v2 v3 v4 = du_b''_206 v0 v2 v3 v4
du_b''_206 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
  (AgdaAny -> AgdaAny) -> AgdaAny -> AgdaAny
du_b''_206 v0 v1 v2 v3
  = coe
      MAlonzo.Code.Agda.Builtin.Cubical.Sub.d_primSubOut_30 v0 erased v1
      (\ v4 ->
         coe
           MAlonzo.Code.Agda.Primitive.Cubical.d_primTransp_90 (\ v5 -> v0)
           erased (coe MAlonzo.Code.Agda.Primitive.Cubical.C_i0_10)
           (coe v2 erased))
      v3
-- Agda.Builtin.Cubical.HCompU._.g
d_g_214 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  (MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> ()) ->
  MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
  (AgdaAny -> AgdaAny) ->
  AgdaAny -> MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> AgdaAny
d_g_214 v0 ~v1 v2 v3 v4 v5 = du_g_214 v0 v2 v3 v4 v5
du_g_214 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
  (AgdaAny -> AgdaAny) ->
  AgdaAny -> MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> AgdaAny
du_g_214 v0 v1 v2 v3 v4
  = coe
      du_fill_54 (coe (\ v5 -> v0))
      (coe
         MAlonzo.Code.Agda.Primitive.Cubical.d_primIMax_16 v1
         (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primINeg_18 v1))
      (coe
         (\ v5 ->
            case coe v1 of
              MAlonzo.Code.Agda.Primitive.Cubical.C_i0_10
                -> coe
                     (\ v6 ->
                        coe
                          MAlonzo.Code.Agda.Primitive.Cubical.d_primTransp_90 (\ v7 -> v0)
                          erased (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primINeg_18 v5)
                          (coe du_b''_206 (coe v0) (coe v1) (coe v2) (coe v3)))
              MAlonzo.Code.Agda.Primitive.Cubical.C_i1_12
                -> coe
                     (\ v6 ->
                        coe
                          MAlonzo.Code.Agda.Primitive.Cubical.d_primTransp_90 (\ v7 -> v0)
                          erased v5 (coe v2 erased))
              _ -> MAlonzo.RTE.mazUnreachableError))
      (coe
         MAlonzo.Code.Agda.Builtin.Cubical.Sub.d_inS_20 v0 erased
         (coe
            MAlonzo.Code.Agda.Primitive.Cubical.d_primIMax_16 v1
            (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primINeg_18 v1))
         (coe du_b''_206 (coe v0) (coe v1) (coe v2) (coe v3)))
      (coe v4)
-- Agda.Builtin.Cubical.HCompU._.f
d_f_228 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  (MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 -> ()) ->
  MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
  (AgdaAny -> AgdaAny) -> AgdaAny -> AgdaAny
d_f_228 v0 ~v1 v2 v3 v4 = du_f_228 v0 v2 v3 v4
du_f_228 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.Cubical.T_I_8 ->
  (AgdaAny -> AgdaAny) -> AgdaAny -> AgdaAny
du_f_228 v0 v1 v2 v3
  = coe
      MAlonzo.Code.Agda.Primitive.Cubical.d_primComp_78 (\ v4 -> v0)
      erased
      (coe
         MAlonzo.Code.Agda.Primitive.Cubical.d_primIMax_16 v1
         (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primINeg_18 v1))
      (\ v4 ->
         case coe v1 of
           MAlonzo.Code.Agda.Primitive.Cubical.C_i0_10
             -> coe
                  (\ v5 ->
                     coe
                       MAlonzo.Code.Agda.Primitive.Cubical.d_primTransp_90 (\ v6 -> v0)
                       erased (coe MAlonzo.Code.Agda.Primitive.Cubical.d_primINeg_18 v4)
                       (coe du_b''_206 (coe v0) (coe v1) (coe v2) (coe v3)))
           MAlonzo.Code.Agda.Primitive.Cubical.C_i1_12
             -> coe
                  (\ v5 ->
                     coe
                       MAlonzo.Code.Agda.Primitive.Cubical.d_primTransp_90 (\ v6 -> v0)
                       erased v4 (coe v2 erased))
           _ -> MAlonzo.RTE.mazUnreachableError)
      (coe du_b''_206 (coe v0) (coe v1) (coe v2) (coe v3))
