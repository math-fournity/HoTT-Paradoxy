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

module MAlonzo.Code.Qfoundation.Qtruncations where

import MAlonzo.RTE (coe, erased, AgdaAny, addInt, subInt, mulInt,
                    quotInt, remInt, geqInt, ltInt, eqInt, add64, sub64, mul64, quot64,
                    rem64, lt64, eq64, word64FromNat, word64ToNat)
import qualified MAlonzo.RTE
import qualified Data.Text
import qualified MAlonzo.Code.Agda.Primitive
import qualified MAlonzo.Code.QfoundationZ45Zcore.QcontractibleZ45Zmaps
import qualified MAlonzo.Code.QfoundationZ45Zcore.QcontractibleZ45Ztypes
import qualified MAlonzo.Code.QfoundationZ45Zcore.Qequivalences
import qualified MAlonzo.Code.QfoundationZ45Zcore.QfunctionZ45Ztypes
import qualified MAlonzo.Code.QfoundationZ45Zcore.QfunctorialityZ45ZdependentZ45ZfunctionZ45Ztypes
import qualified MAlonzo.Code.QfoundationZ45Zcore.QfunctorialityZ45ZdependentZ45ZpairZ45Ztypes
import qualified MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes
import qualified MAlonzo.Code.QfoundationZ45Zcore.QprecompositionZ45Zfunctions
import qualified MAlonzo.Code.QfoundationZ45Zcore.QtruncatedZ45Ztypes
import qualified MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels
import qualified MAlonzo.Code.QfoundationZ45Zcore.QuniversalZ45ZpropertyZ45Ztruncation
import qualified MAlonzo.Code.Qfoundation.QcontractibleZ45Ztypes
import qualified MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes
import qualified MAlonzo.Code.Qfoundation.QdependentZ45ZproductsZ45ZtruncatedZ45Ztypes
import qualified MAlonzo.Code.Qfoundation.QequivalencesZ45ZcontractibleZ45Ztypes
import qualified MAlonzo.Code.Qfoundation.QfunctionZ45Zextensionality
import qualified MAlonzo.Code.Qfoundation.QfunctorialityZ45ZdependentZ45ZfunctionZ45Ztypes
import qualified MAlonzo.Code.Qfoundation.QfundamentalZ45ZtheoremZ45ZofZ45ZidentityZ45Ztypes
import qualified MAlonzo.Code.Qfoundation.QidentityZ45Ztypes
import qualified MAlonzo.Code.Qfoundation.QtruncatedZ45Ztypes
import qualified MAlonzo.Code.Qfoundation.QuniversalZ45ZpropertyZ45ZdependentZ45ZpairZ45Ztypes

-- foundation.truncations.type-trunc
d_type'45'trunc_8
  = error
      "MAlonzo Runtime Error: postulate evaluated: foundation.truncations.type-trunc"
-- foundation.truncations.is-trunc-type-trunc
d_is'45'trunc'45'type'45'trunc_16
  = error
      "MAlonzo Runtime Error: postulate evaluated: foundation.truncations.is-trunc-type-trunc"
-- foundation.truncations.trunc
d_trunc_22 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () -> MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_trunc_22 v0 v1 ~v2 = du_trunc_22 v0 v1
du_trunc_22 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_trunc_22 v0 v1
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
      erased (coe d_is'45'trunc'45'type'45'trunc_16 v0 v1 erased)
-- foundation.truncations.unit-trunc
d_unit'45'trunc_38
  = error
      "MAlonzo Runtime Error: postulate evaluated: foundation.truncations.unit-trunc"
-- foundation.truncations.is-truncation-trunc
d_is'45'truncation'45'trunc_46
  = error
      "MAlonzo Runtime Error: postulate evaluated: foundation.truncations.is-truncation-trunc"
-- foundation.truncations.equiv-universal-property-trunc
d_equiv'45'universal'45'property'45'trunc_58 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_equiv'45'universal'45'property'45'trunc_58 v0 v1 v2 ~v3 v4
  = du_equiv'45'universal'45'property'45'trunc_58 v0 v1 v2 v4
du_equiv'45'universal'45'property'45'trunc_58 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_equiv'45'universal'45'property'45'trunc_58 v0 v1 v2 v3
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
      (coe
         MAlonzo.Code.QfoundationZ45Zcore.QprecompositionZ45Zfunctions.du_precomp_22
         (coe d_unit'45'trunc_38 v0 v2 erased))
      (coe d_is'45'truncation'45'trunc_46 v0 v2 erased v1 v3)
-- foundation.truncations.universal-property-trunc
d_universal'45'property'45'trunc_74 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  (AgdaAny -> AgdaAny) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_universal'45'property'45'trunc_74 v0 v1 ~v2 v3
  = du_universal'45'property'45'trunc_74 v0 v1 v3
du_universal'45'property'45'trunc_74 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  (AgdaAny -> AgdaAny) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_universal'45'property'45'trunc_74 v0 v1 v2
  = coe
      MAlonzo.Code.QfoundationZ45Zcore.QuniversalZ45ZpropertyZ45Ztruncation.du_universal'45'property'45'truncation'45'is'45'truncation_204
      (coe d_is'45'truncation'45'trunc_46 v0 v1 erased) (coe v2)
-- foundation.truncations._.apply-universal-property-trunc
d_apply'45'universal'45'property'45'trunc_98 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  (AgdaAny -> AgdaAny) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_apply'45'universal'45'property'45'trunc_98 v0 v1 v2 ~v3 v4 v5
  = du_apply'45'universal'45'property'45'trunc_98 v0 v1 v2 v4 v5
du_apply'45'universal'45'property'45'trunc_98 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  (AgdaAny -> AgdaAny) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_apply'45'universal'45'property'45'trunc_98 v0 v1 v2 v3 v4
  = coe
      MAlonzo.Code.QfoundationZ45Zcore.QcontractibleZ45Ztypes.du_center_18
      (coe
         MAlonzo.Code.QfoundationZ45Zcore.QuniversalZ45ZpropertyZ45Ztruncation.du_universal'45'property'45'truncation'45'is'45'truncation_204
         (coe d_is'45'truncation'45'trunc_46 v0 v2 erased) (coe v1) (coe v3)
         (coe v4))
-- foundation.truncations._.map-universal-property-trunc
d_map'45'universal'45'property'45'trunc_106 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  (AgdaAny -> AgdaAny) -> AgdaAny -> AgdaAny
d_map'45'universal'45'property'45'trunc_106 v0 v1 v2 ~v3 v4 v5
  = du_map'45'universal'45'property'45'trunc_106 v0 v1 v2 v4 v5
du_map'45'universal'45'property'45'trunc_106 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  (AgdaAny -> AgdaAny) -> AgdaAny -> AgdaAny
du_map'45'universal'45'property'45'trunc_106 v0 v1 v2 v3 v4
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.d_pr1_26
      (coe
         du_apply'45'universal'45'property'45'trunc_98 (coe v0) (coe v1)
         (coe v2) (coe v3) (coe v4))
-- foundation.truncations._.triangle-universal-property-trunc
d_triangle'45'universal'45'property'45'trunc_116 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  (AgdaAny -> AgdaAny) ->
  AgdaAny ->
  MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes.T_Id_14
d_triangle'45'universal'45'property'45'trunc_116 = erased
-- foundation.truncations._.dependent-universal-property-trunc
d_dependent'45'universal'45'property'45'trunc_132 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_dependent'45'universal'45'property'45'trunc_132 v0 v1 ~v2 ~v3
  = du_dependent'45'universal'45'property'45'trunc_132 v0 v1
du_dependent'45'universal'45'property'45'trunc_132 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_dependent'45'universal'45'property'45'trunc_132 v0 v1
  = coe
      MAlonzo.Code.QfoundationZ45Zcore.QuniversalZ45ZpropertyZ45Ztruncation.du_dependent'45'universal'45'property'45'truncation'45'is'45'truncation_262
      (coe v0) (coe v1) (coe du_trunc_22 (coe v0) (coe v1))
      (coe d_unit'45'trunc_38 v0 v1 erased)
      (coe d_is'45'truncation'45'trunc_46 v0 v1 erased)
-- foundation.truncations._.equiv-dependent-universal-property-trunc
d_equiv'45'dependent'45'universal'45'property'45'trunc_142 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_equiv'45'dependent'45'universal'45'property'45'trunc_142 v0 v1
                                                           ~v2 ~v3 v4
  = du_equiv'45'dependent'45'universal'45'property'45'trunc_142
      v0 v1 v4
du_equiv'45'dependent'45'universal'45'property'45'trunc_142 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_equiv'45'dependent'45'universal'45'property'45'trunc_142 v0 v1
                                                            v2
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
      (coe (\ v3 v4 -> coe v3 (coe d_unit'45'trunc_38 v0 v1 erased v4)))
      (coe du_dependent'45'universal'45'property'45'trunc_132 v0 v1 v2)
-- foundation.truncations._.unique-dependent-function-trunc
d_unique'45'dependent'45'function'45'trunc_160 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (AgdaAny -> AgdaAny) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_unique'45'dependent'45'function'45'trunc_160 v0 v1 ~v2 ~v3 v4 v5
  = du_unique'45'dependent'45'function'45'trunc_160 v0 v1 v4 v5
du_unique'45'dependent'45'function'45'trunc_160 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (AgdaAny -> AgdaAny) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_unique'45'dependent'45'function'45'trunc_160 v0 v1 v2 v3
  = coe
      MAlonzo.Code.Qfoundation.QequivalencesZ45ZcontractibleZ45Ztypes.du_is'45'contr'45'equiv''_52
      (coe
         MAlonzo.Code.QfoundationZ45Zcore.QfunctorialityZ45ZdependentZ45ZpairZ45Ztypes.du_equiv'45'tot_368
         (coe
            (\ v4 ->
               coe
                 MAlonzo.Code.Qfoundation.QfunctionZ45Zextensionality.du_equiv'45'funext_54)))
      (coe
         MAlonzo.Code.QfoundationZ45Zcore.QcontractibleZ45Zmaps.du_is'45'contr'45'map'45'is'45'equiv_122
         (coe du_dependent'45'universal'45'property'45'trunc_132 v0 v1 v2)
         v3)
-- foundation.truncations._.apply-dependent-universal-property-trunc
d_apply'45'dependent'45'universal'45'property'45'trunc_180 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (AgdaAny -> AgdaAny) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_apply'45'dependent'45'universal'45'property'45'trunc_180 v0 v1
                                                           ~v2 ~v3 v4 v5
  = du_apply'45'dependent'45'universal'45'property'45'trunc_180
      v0 v1 v4 v5
du_apply'45'dependent'45'universal'45'property'45'trunc_180 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (AgdaAny -> AgdaAny) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_apply'45'dependent'45'universal'45'property'45'trunc_180 v0 v1
                                                            v2 v3
  = coe
      MAlonzo.Code.QfoundationZ45Zcore.QcontractibleZ45Ztypes.du_center_18
      (coe
         du_unique'45'dependent'45'function'45'trunc_160 (coe v0) (coe v1)
         (coe v2) (coe v3))
-- foundation.truncations._.function-dependent-universal-property-trunc
d_function'45'dependent'45'universal'45'property'45'trunc_196 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (AgdaAny -> AgdaAny) -> AgdaAny -> AgdaAny
d_function'45'dependent'45'universal'45'property'45'trunc_196 v0 v1
                                                              ~v2 ~v3 v4 v5
  = du_function'45'dependent'45'universal'45'property'45'trunc_196
      v0 v1 v4 v5
du_function'45'dependent'45'universal'45'property'45'trunc_196 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (AgdaAny -> AgdaAny) -> AgdaAny -> AgdaAny
du_function'45'dependent'45'universal'45'property'45'trunc_196 v0
                                                               v1 v2 v3
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.d_pr1_26
      (coe
         du_apply'45'dependent'45'universal'45'property'45'trunc_180
         (coe v0) (coe v1) (coe v2) (coe v3))
-- foundation.truncations._.htpy-dependent-universal-property-trunc
d_htpy'45'dependent'45'universal'45'property'45'trunc_210 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (AgdaAny -> AgdaAny) ->
  AgdaAny ->
  MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes.T_Id_14
d_htpy'45'dependent'45'universal'45'property'45'trunc_210 = erased
-- foundation.truncations.unique-truncated-fam-trunc
d_unique'45'truncated'45'fam'45'trunc_230 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_unique'45'truncated'45'fam'45'trunc_230 v0 v1 v2 ~v3 v4
  = du_unique'45'truncated'45'fam'45'trunc_230 v0 v1 v2 v4
du_unique'45'truncated'45'fam'45'trunc_230 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_unique'45'truncated'45'fam'45'trunc_230 v0 v1 v2 v3
  = coe
      MAlonzo.Code.Qfoundation.QequivalencesZ45ZcontractibleZ45Ztypes.du_is'45'contr'45'equiv''_52
      (coe
         MAlonzo.Code.QfoundationZ45Zcore.QfunctorialityZ45ZdependentZ45ZpairZ45Ztypes.du_equiv'45'tot_368
         (coe
            (\ v4 ->
               coe
                 MAlonzo.Code.QfoundationZ45Zcore.QfunctorialityZ45ZdependentZ45ZfunctionZ45Ztypes.du_equiv'45'Π'45'equiv'45'family_228
                 (coe
                    (\ v5 ->
                       coe
                         MAlonzo.Code.QfoundationZ45Zcore.Qequivalences.du__'8728'e__420
                         (coe
                            MAlonzo.Code.Qfoundation.QtruncatedZ45Ztypes.du_extensionality'45'Truncated'45'Type_22
                            (coe v3 v5)
                            (coe
                               MAlonzo.Code.QfoundationZ45Zcore.QfunctionZ45Ztypes.du__'8728'__50
                               (coe (\ v6 -> v4))
                               (coe
                                  d_unit'45'trunc_38 v0
                                  (coe
                                     MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.C_succ'45'𝕋_8
                                     (coe v2))
                                  erased)
                               (coe v5)))
                         (coe
                            MAlonzo.Code.Qfoundation.QidentityZ45Ztypes.du_equiv'45'inv_90))))))
      (coe
         du_universal'45'property'45'trunc_74 v0
         (coe
            MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.C_succ'45'𝕋_8
            (coe v2))
         ()
         (MAlonzo.Code.Qfoundation.QtruncatedZ45Ztypes.d_Truncated'45'Type'45'Truncated'45'Type_44
            (coe v1) (coe v2))
         v3)
-- foundation.truncations._.truncated-fam-trunc
d_truncated'45'fam'45'trunc_262 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_truncated'45'fam'45'trunc_262 v0 v1 v2 ~v3 v4
  = du_truncated'45'fam'45'trunc_262 v0 v1 v2 v4
du_truncated'45'fam'45'trunc_262 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_truncated'45'fam'45'trunc_262 v0 v1 v2 v3
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.d_pr1_26
      (coe
         MAlonzo.Code.QfoundationZ45Zcore.QcontractibleZ45Ztypes.du_center_18
         (coe
            du_unique'45'truncated'45'fam'45'trunc_230 (coe v0) (coe v1)
            (coe v2) (coe v3)))
-- foundation.truncations._.fam-trunc
d_fam'45'trunc_264 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  AgdaAny -> ()
d_fam'45'trunc_264 = erased
-- foundation.truncations._.compute-truncated-fam-trunc
d_compute'45'truncated'45'fam'45'trunc_268 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_compute'45'truncated'45'fam'45'trunc_268 v0 v1 v2 ~v3 v4
  = du_compute'45'truncated'45'fam'45'trunc_268 v0 v1 v2 v4
du_compute'45'truncated'45'fam'45'trunc_268 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_compute'45'truncated'45'fam'45'trunc_268 v0 v1 v2 v3
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.d_pr2_28
      (coe
         MAlonzo.Code.QfoundationZ45Zcore.QcontractibleZ45Ztypes.du_center_18
         (coe
            du_unique'45'truncated'45'fam'45'trunc_230 (coe v0) (coe v1)
            (coe v2) (coe v3)))
-- foundation.truncations._.map-compute-truncated-fam-trunc
d_map'45'compute'45'truncated'45'fam'45'trunc_272 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  AgdaAny -> AgdaAny -> AgdaAny
d_map'45'compute'45'truncated'45'fam'45'trunc_272 v0 v1 v2 ~v3 v4
                                                  v5
  = du_map'45'compute'45'truncated'45'fam'45'trunc_272 v0 v1 v2 v4 v5
du_map'45'compute'45'truncated'45'fam'45'trunc_272 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  AgdaAny -> AgdaAny -> AgdaAny
du_map'45'compute'45'truncated'45'fam'45'trunc_272 v0 v1 v2 v3 v4
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.d_pr1_26
      (coe du_compute'45'truncated'45'fam'45'trunc_268 v0 v1 v2 v3 v4)
-- foundation.truncations._.total-truncated-fam-trunc
d_total'45'truncated'45'fam'45'trunc_276 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  ()
d_total'45'truncated'45'fam'45'trunc_276 = erased
-- foundation.truncations._.dependent-universal-property-total-truncated-fam-trunc
d_dependent'45'universal'45'property'45'total'45'truncated'45'fam'45'trunc_310 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (AgdaAny -> AgdaAny -> AgdaAny) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_dependent'45'universal'45'property'45'total'45'truncated'45'fam'45'trunc_310 v0
                                                                               v1 ~v2 v3 ~v4 v5 v6
                                                                               v7
  = du_dependent'45'universal'45'property'45'total'45'truncated'45'fam'45'trunc_310
      v0 v1 v3 v5 v6 v7
du_dependent'45'universal'45'property'45'total'45'truncated'45'fam'45'trunc_310 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (AgdaAny -> AgdaAny -> AgdaAny) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_dependent'45'universal'45'property'45'total'45'truncated'45'fam'45'trunc_310 v0
                                                                                v1 v2 v3 v4 v5
  = coe
      MAlonzo.Code.Qfoundation.QequivalencesZ45ZcontractibleZ45Ztypes.du_is'45'contr'45'equiv_24
      (coe
         MAlonzo.Code.QfoundationZ45Zcore.QfunctorialityZ45ZdependentZ45ZpairZ45Ztypes.du_equiv'45'Σ_702
         (coe
            MAlonzo.Code.Qfoundation.QuniversalZ45ZpropertyZ45ZdependentZ45ZpairZ45Ztypes.du_equiv'45'ev'45'pair_36)
         (coe
            (\ v6 ->
               coe
                 MAlonzo.Code.QfoundationZ45Zcore.QfunctorialityZ45ZdependentZ45ZfunctionZ45Ztypes.du_equiv'45'Π'45'equiv'45'family_228
                 (coe
                    (\ v7 ->
                       coe
                         MAlonzo.Code.QfoundationZ45Zcore.Qequivalences.du__'8728'e__420
                         (coe
                            MAlonzo.Code.QfoundationZ45Zcore.Qequivalences.du_inv'45'equiv_244
                            (coe
                               MAlonzo.Code.Qfoundation.QfunctionZ45Zextensionality.du_equiv'45'funext_54))
                         (coe
                            MAlonzo.Code.Qfoundation.QfunctorialityZ45ZdependentZ45ZfunctionZ45Ztypes.du_equiv'45'Π_48
                            (coe
                               MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.d_pr2_28
                               (coe
                                  MAlonzo.Code.QfoundationZ45Zcore.QcontractibleZ45Ztypes.du_center_18
                                  (coe
                                     du_unique'45'truncated'45'fam'45'trunc_230 (coe v0) (coe v1)
                                     (coe v2) (coe v3)))
                               v7)
                            (coe
                               (\ v8 ->
                                  coe
                                    MAlonzo.Code.Qfoundation.QidentityZ45Ztypes.du_equiv'45'concat''_244))))))))
      (coe
         du_unique'45'dependent'45'function'45'trunc_160 (coe v0)
         (coe
            MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.C_succ'45'𝕋_8
            (coe v2))
         (coe
            (\ v6 ->
               MAlonzo.Code.QfoundationZ45Zcore.QtruncatedZ45Ztypes.d_truncated'45'type'45'succ'45'Truncated'45'Type_84
                 (coe v2) (coe ())
                 (coe
                    MAlonzo.Code.Qfoundation.QdependentZ45ZproductsZ45ZtruncatedZ45Ztypes.du_Π'45'Truncated'45'Type_142
                    (coe v2)
                    (coe
                       (\ v7 ->
                          coe
                            v4
                            (coe
                               MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
                               (coe v6) (coe v7)))))))
         (coe
            (\ v6 ->
               coe
                 MAlonzo.Code.Qfoundation.QfunctorialityZ45ZdependentZ45ZfunctionZ45Ztypes.du_map'45'equiv'45'Π_34
                 (coe du_compute'45'truncated'45'fam'45'trunc_268 v0 v1 v2 v3 v6)
                 (\ v7 ->
                    coe
                      MAlonzo.Code.QfoundationZ45Zcore.Qequivalences.du_id'45'equiv_116)
                 (coe v5 v6))))
-- foundation.truncations._.function-dependent-universal-property-total-truncated-fam-trunc
d_function'45'dependent'45'universal'45'property'45'total'45'truncated'45'fam'45'trunc_348 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (AgdaAny -> AgdaAny -> AgdaAny) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  AgdaAny
d_function'45'dependent'45'universal'45'property'45'total'45'truncated'45'fam'45'trunc_348 v0
                                                                                           v1 ~v2 v3
                                                                                           ~v4 v5 v6
                                                                                           v7
  = du_function'45'dependent'45'universal'45'property'45'total'45'truncated'45'fam'45'trunc_348
      v0 v1 v3 v5 v6 v7
du_function'45'dependent'45'universal'45'property'45'total'45'truncated'45'fam'45'trunc_348 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (AgdaAny -> AgdaAny -> AgdaAny) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  AgdaAny
du_function'45'dependent'45'universal'45'property'45'total'45'truncated'45'fam'45'trunc_348 v0
                                                                                            v1 v2 v3
                                                                                            v4 v5
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.d_pr1_26
      (coe
         MAlonzo.Code.QfoundationZ45Zcore.QcontractibleZ45Ztypes.du_center_18
         (coe
            du_dependent'45'universal'45'property'45'total'45'truncated'45'fam'45'trunc_310
            (coe v0) (coe v1) (coe v2) (coe v3) (coe v4) (coe v5)))
-- foundation.truncations._.htpy-dependent-universal-property-total-truncated-fam-trunc
d_htpy'45'dependent'45'universal'45'property'45'total'45'truncated'45'fam'45'trunc_354 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  (AgdaAny ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
   MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12) ->
  (AgdaAny -> AgdaAny -> AgdaAny) ->
  AgdaAny ->
  AgdaAny ->
  MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes.T_Id_14
d_htpy'45'dependent'45'universal'45'property'45'total'45'truncated'45'fam'45'trunc_354
  = erased
-- foundation.truncations._.map-inv-unit-trunc
d_map'45'inv'45'unit'45'trunc_366 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  AgdaAny -> AgdaAny
d_map'45'inv'45'unit'45'trunc_366 v0 v1 v2
  = coe
      du_map'45'universal'45'property'45'trunc_106 (coe v0) (coe v0)
      (coe v1) (coe v2) (coe (\ v3 -> v3))
-- foundation.truncations._.is-retraction-map-inv-unit-trunc
d_is'45'retraction'45'map'45'inv'45'unit'45'trunc_368 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  AgdaAny ->
  MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes.T_Id_14
d_is'45'retraction'45'map'45'inv'45'unit'45'trunc_368 = erased
-- foundation.truncations._.is-section-map-inv-unit-trunc
d_is'45'section'45'map'45'inv'45'unit'45'trunc_370 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  AgdaAny ->
  MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes.T_Id_14
d_is'45'section'45'map'45'inv'45'unit'45'trunc_370 = erased
-- foundation.truncations._.is-equiv-unit-trunc
d_is'45'equiv'45'unit'45'trunc_372 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_is'45'equiv'45'unit'45'trunc_372 v0 v1 v2
  = coe
      MAlonzo.Code.QfoundationZ45Zcore.Qequivalences.du_is'45'equiv'45'is'45'invertible_146
      (coe d_map'45'inv'45'unit'45'trunc_366 (coe v0) (coe v1) (coe v2))
      erased erased
-- foundation.truncations._.equiv-unit-trunc
d_equiv'45'unit'45'trunc_374 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_equiv'45'unit'45'trunc_374 v0 v1 v2
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
      (coe d_unit'45'trunc_38 v0 v1 erased)
      (coe d_is'45'equiv'45'unit'45'trunc_372 (coe v0) (coe v1) (coe v2))
-- foundation.truncations._.is-equiv-map-inv-unit-trunc
d_is'45'equiv'45'map'45'inv'45'unit'45'trunc_376 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_is'45'equiv'45'map'45'inv'45'unit'45'trunc_376 v0 v1 ~v2
  = du_is'45'equiv'45'map'45'inv'45'unit'45'trunc_376 v0 v1
du_is'45'equiv'45'map'45'inv'45'unit'45'trunc_376 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_is'45'equiv'45'map'45'inv'45'unit'45'trunc_376 v0 v1
  = coe
      MAlonzo.Code.QfoundationZ45Zcore.Qequivalences.du_is'45'equiv'45'is'45'invertible_146
      (coe d_unit'45'trunc_38 v0 v1 erased) erased erased
-- foundation.truncations._.inv-equiv-unit-trunc
d_inv'45'equiv'45'unit'45'trunc_378 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_inv'45'equiv'45'unit'45'trunc_378 v0 v1 v2
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
      (coe d_map'45'inv'45'unit'45'trunc_366 (coe v0) (coe v1) (coe v2))
      (coe
         du_is'45'equiv'45'map'45'inv'45'unit'45'trunc_376 (coe v0)
         (coe v1))
-- foundation.truncations.is-retraction-trunc
d_is'45'retraction'45'trunc_384 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes.T_Id_14
d_is'45'retraction'45'trunc_384 = erased
-- foundation.truncations.retract-Truncated-Type-UU
d_retract'45'Truncated'45'Type'45'UU_396 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_retract'45'Truncated'45'Type'45'UU_396 v0 v1
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
      (coe
         (\ v2 ->
            MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.d_pr1_26
              (coe v2)))
      (coe
         MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
         (\ v2 -> coe du_trunc_22 (coe v0) (coe v1)) erased)
-- foundation.truncations._.is-equiv-unit-trunc-is-contr
d_is'45'equiv'45'unit'45'trunc'45'is'45'contr_414 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_is'45'equiv'45'unit'45'trunc'45'is'45'contr_414 v0 v1 v2 v3
  = coe
      d_is'45'equiv'45'unit'45'trunc_372 (coe v0) (coe v1)
      (coe
         MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
         (coe v2)
         (coe
            MAlonzo.Code.Qfoundation.QcontractibleZ45Ztypes.du_is'45'trunc'45'is'45'contr_14
            (coe v0) (coe v1) (coe v3)))
-- foundation.truncations._.is-contr-type-trunc
d_is'45'contr'45'type'45'trunc_418 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_is'45'contr'45'type'45'trunc_418 v0 v1 ~v2 v3
  = du_is'45'contr'45'type'45'trunc_418 v0 v1 v3
du_is'45'contr'45'type'45'trunc_418 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_is'45'contr'45'type'45'trunc_418 v0 v1 v2
  = coe
      MAlonzo.Code.Qfoundation.QequivalencesZ45ZcontractibleZ45Ztypes.du_is'45'contr'45'is'45'equiv''_44
      (coe d_unit'45'trunc_38 v0 v1 erased)
      (d_is'45'equiv'45'unit'45'trunc'45'is'45'contr_414
         (coe v0) (coe v1) erased (coe v2))
      v2
-- foundation.truncations._.idempotent-trunc
d_idempotent'45'trunc_432 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () -> MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_idempotent'45'trunc_432 v0 v1 ~v2
  = du_idempotent'45'trunc_432 v0 v1
du_idempotent'45'trunc_432 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_idempotent'45'trunc_432 v0 v1
  = coe
      MAlonzo.Code.QfoundationZ45Zcore.Qequivalences.du_inv'45'equiv_244
      (coe
         d_equiv'45'unit'45'trunc_374 (coe v0) (coe v1)
         (coe du_trunc_22 (coe v0) (coe v1)))
-- foundation.truncations._.Eq-trunc-Truncated-Type
d_Eq'45'trunc'45'Truncated'45'Type_446 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  AgdaAny ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_Eq'45'trunc'45'Truncated'45'Type_446 v0 v1 ~v2 ~v3
  = du_Eq'45'trunc'45'Truncated'45'Type_446 v0 v1
du_Eq'45'trunc'45'Truncated'45'Type_446 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_Eq'45'trunc'45'Truncated'45'Type_446 v0 v1
  = coe
      du_truncated'45'fam'45'trunc_262 (coe v0) (coe v0) (coe v1)
      (coe (\ v2 -> coe du_trunc_22 (coe v0) (coe v1)))
-- foundation.truncations._.Eq-trunc
d_Eq'45'trunc_450 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () -> AgdaAny -> AgdaAny -> ()
d_Eq'45'trunc_450 = erased
-- foundation.truncations._.compute-Eq-trunc
d_compute'45'Eq'45'trunc_456 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  AgdaAny ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_compute'45'Eq'45'trunc_456 v0 v1 ~v2 ~v3
  = du_compute'45'Eq'45'trunc_456 v0 v1
du_compute'45'Eq'45'trunc_456 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_compute'45'Eq'45'trunc_456 v0 v1
  = coe
      du_compute'45'truncated'45'fam'45'trunc_268 (coe v0) (coe v0)
      (coe v1) (coe (\ v2 -> coe du_trunc_22 (coe v0) (coe v1)))
-- foundation.truncations._.map-compute-Eq-trunc
d_map'45'compute'45'Eq'45'trunc_462 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () -> AgdaAny -> AgdaAny -> AgdaAny -> AgdaAny
d_map'45'compute'45'Eq'45'trunc_462 v0 v1 ~v2 ~v3 v4
  = du_map'45'compute'45'Eq'45'trunc_462 v0 v1 v4
du_map'45'compute'45'Eq'45'trunc_462 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  AgdaAny -> AgdaAny -> AgdaAny
du_map'45'compute'45'Eq'45'trunc_462 v0 v1 v2
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.d_pr1_26
      (coe du_compute'45'Eq'45'trunc_456 v0 v1 v2)
-- foundation.truncations._.refl-Eq-trunc
d_refl'45'Eq'45'trunc_466 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () -> AgdaAny -> AgdaAny
d_refl'45'Eq'45'trunc_466 v0 v1 ~v2 v3
  = du_refl'45'Eq'45'trunc_466 v0 v1 v3
du_refl'45'Eq'45'trunc_466 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  AgdaAny -> AgdaAny
du_refl'45'Eq'45'trunc_466 v0 v1 v2
  = coe
      du_map'45'compute'45'Eq'45'trunc_462 v0 v1 v2
      (coe d_unit'45'trunc_38 v0 v1 erased erased)
-- foundation.truncations._.refl-compute-Eq-trunc
d_refl'45'compute'45'Eq'45'trunc_468 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  AgdaAny ->
  MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes.T_Id_14
d_refl'45'compute'45'Eq'45'trunc_468 = erased
-- foundation.truncations._.is-torsorial-Eq-trunc
d_is'45'torsorial'45'Eq'45'trunc_470 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_is'45'torsorial'45'Eq'45'trunc_470 v0 v1 ~v2 v3
  = du_is'45'torsorial'45'Eq'45'trunc_470 v0 v1 v3
du_is'45'torsorial'45'Eq'45'trunc_470 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_is'45'torsorial'45'Eq'45'trunc_470 v0 v1 v2
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
      (coe
         MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
         (coe
            d_unit'45'trunc_38 v0
            (coe
               MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.C_succ'45'𝕋_8
               (coe v1))
            erased v2)
         (coe du_refl'45'Eq'45'trunc_466 (coe v0) (coe v1) (coe v2)))
      (coe
         du_function'45'dependent'45'universal'45'property'45'total'45'truncated'45'fam'45'trunc_348
         (coe v0) (coe v0) (coe v1)
         (coe (\ v3 -> coe du_trunc_22 (coe v0) (coe v1)))
         (coe
            MAlonzo.Code.QfoundationZ45Zcore.QtruncatedZ45Ztypes.du_Id'45'Truncated'45'Type_120
            (coe
               MAlonzo.Code.QfoundationZ45Zcore.QtruncatedZ45Ztypes.du_Σ'45'Truncated'45'Type_362
               (coe
                  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.C_succ'45'𝕋_8
                  (coe v1))
               (coe
                  du_trunc_22 (coe v0)
                  (coe
                     MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.C_succ'45'𝕋_8
                     (coe v1)))
               (coe
                  (\ v3 ->
                     MAlonzo.Code.QfoundationZ45Zcore.QtruncatedZ45Ztypes.d_truncated'45'type'45'succ'45'Truncated'45'Type_84
                       (coe v1) (coe v0)
                       (coe du_Eq'45'trunc'45'Truncated'45'Type_446 v0 v1 v3))))
            (coe
               MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
               (coe
                  d_unit'45'trunc_38 v0
                  (coe
                     MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.C_succ'45'𝕋_8
                     (coe v1))
                  erased v2)
               (coe du_refl'45'Eq'45'trunc_466 (coe v0) (coe v1) (coe v2))))
         (coe
            (\ v3 ->
               coe
                 du_function'45'dependent'45'universal'45'property'45'trunc_196
                 (coe v0) (coe v1)
                 (coe
                    (\ v4 ->
                       coe
                         MAlonzo.Code.QfoundationZ45Zcore.QtruncatedZ45Ztypes.du_Id'45'Truncated'45'Type_120
                         (coe
                            MAlonzo.Code.QfoundationZ45Zcore.QtruncatedZ45Ztypes.du_Σ'45'Truncated'45'Type_362
                            (coe
                               MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.C_succ'45'𝕋_8
                               (coe v1))
                            (coe
                               du_trunc_22 (coe v0)
                               (coe
                                  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.C_succ'45'𝕋_8
                                  (coe v1)))
                            (coe
                               (\ v5 ->
                                  MAlonzo.Code.QfoundationZ45Zcore.QtruncatedZ45Ztypes.d_truncated'45'type'45'succ'45'Truncated'45'Type_84
                                    (coe v1) (coe v0)
                                    (coe du_Eq'45'trunc'45'Truncated'45'Type_446 v0 v1 v5))))
                         (coe
                            MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
                            (coe
                               d_unit'45'trunc_38 v0
                               (coe
                                  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.C_succ'45'𝕋_8
                                  (coe v1))
                               erased v2)
                            (coe du_refl'45'Eq'45'trunc_466 (coe v0) (coe v1) (coe v2)))
                         (coe
                            MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
                            (coe
                               d_unit'45'trunc_38 v0
                               (coe
                                  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.C_succ'45'𝕋_8
                                  (coe v1))
                               erased v3)
                            (coe du_map'45'compute'45'Eq'45'trunc_462 v0 v1 v3 v4))))
                 erased)))
-- foundation.truncations._._.r
d_r_480 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  AgdaAny ->
  AgdaAny ->
  MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes.T_Id_14 ->
  MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes.T_Id_14
d_r_480 = erased
-- foundation.truncations._.Eq-eq-trunc
d_Eq'45'eq'45'trunc_494 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  AgdaAny ->
  AgdaAny ->
  MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes.T_Id_14 ->
  AgdaAny
d_Eq'45'eq'45'trunc_494 v0 v1 ~v2 v3 ~v4 ~v5
  = du_Eq'45'eq'45'trunc_494 v0 v1 v3
du_Eq'45'eq'45'trunc_494 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  AgdaAny -> AgdaAny
du_Eq'45'eq'45'trunc_494 v0 v1 v2
  = coe du_refl'45'Eq'45'trunc_466 (coe v0) (coe v1) (coe v2)
-- foundation.truncations._.is-equiv-Eq-eq-trunc
d_is'45'equiv'45'Eq'45'eq'45'trunc_498 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  AgdaAny ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_is'45'equiv'45'Eq'45'eq'45'trunc_498 v0 v1 ~v2 v3
  = du_is'45'equiv'45'Eq'45'eq'45'trunc_498 v0 v1 v3
du_is'45'equiv'45'Eq'45'eq'45'trunc_498 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  AgdaAny ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_is'45'equiv'45'Eq'45'eq'45'trunc_498 v0 v1 v2
  = coe
      MAlonzo.Code.Qfoundation.QfundamentalZ45ZtheoremZ45ZofZ45ZidentityZ45Ztypes.du_fundamental'45'theorem'45'id_22
      (coe
         d_unit'45'trunc_38 v0
         (coe
            MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.C_succ'45'𝕋_8
            (coe v1))
         erased v2)
-- foundation.truncations._.extensionality-trunc
d_extensionality'45'trunc_502 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  AgdaAny ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_extensionality'45'trunc_502 v0 v1 ~v2 v3 v4
  = du_extensionality'45'trunc_502 v0 v1 v3 v4
du_extensionality'45'trunc_502 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  AgdaAny ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_extensionality'45'trunc_502 v0 v1 v2 v3
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
      (\ v4 -> coe du_Eq'45'eq'45'trunc_494 (coe v0) (coe v1) (coe v2))
      (coe du_is'45'equiv'45'Eq'45'eq'45'trunc_498 v0 v1 v2 v3)
-- foundation.truncations._.effectiveness-trunc
d_effectiveness'45'trunc_510 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  AgdaAny ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_effectiveness'45'trunc_510 v0 v1 ~v2 v3 v4
  = du_effectiveness'45'trunc_510 v0 v1 v3 v4
du_effectiveness'45'trunc_510 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  AgdaAny ->
  AgdaAny ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_effectiveness'45'trunc_510 v0 v1 v2 v3
  = coe
      MAlonzo.Code.QfoundationZ45Zcore.Qequivalences.du__'8728'e__420
      (coe
         MAlonzo.Code.QfoundationZ45Zcore.Qequivalences.du_inv'45'equiv_244
         (coe
            du_extensionality'45'trunc_502 (coe v0) (coe v1) (coe v2)
            (coe
               d_unit'45'trunc_38 v0
               (coe
                  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.C_succ'45'𝕋_8
                  (coe v1))
               erased v3)))
      (coe du_compute'45'Eq'45'trunc_456 v0 v1 v3)
-- foundation.truncations._.map-effectiveness-trunc
d_map'45'effectiveness'45'trunc_516 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  AgdaAny ->
  AgdaAny ->
  AgdaAny ->
  MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes.T_Id_14
d_map'45'effectiveness'45'trunc_516 = erased
-- foundation.truncations._.refl-effectiveness-trunc
d_refl'45'effectiveness'45'trunc_520 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  AgdaAny ->
  MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes.T_Id_14
d_refl'45'effectiveness'45'trunc_520 = erased
-- foundation.truncations._.map-trunc-Σ
d_map'45'trunc'45'Σ_538 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () -> (AgdaAny -> ()) -> AgdaAny -> AgdaAny
d_map'45'trunc'45'Σ_538 ~v0 v1 v2 ~v3 ~v4
  = du_map'45'trunc'45'Σ_538 v1 v2
du_map'45'trunc'45'Σ_538 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  AgdaAny -> AgdaAny
du_map'45'trunc'45'Σ_538 v0 v1
  = coe
      du_map'45'universal'45'property'45'trunc_106 (coe ()) (coe ())
      (coe v1) (coe du_trunc_22 (coe ()) (coe v1))
      (coe
         (\ v2 ->
            coe
              d_unit'45'trunc_38 () v1 erased
              (coe
                 MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
                 (coe
                    MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.d_pr1_26
                    (coe v2))
                 (coe
                    d_unit'45'trunc_38 v0 v1 erased
                    (MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.d_pr2_28
                       (coe v2))))))
-- foundation.truncations._.map-inv-trunc-Σ
d_map'45'inv'45'trunc'45'Σ_550 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () -> (AgdaAny -> ()) -> AgdaAny -> AgdaAny
d_map'45'inv'45'trunc'45'Σ_550 ~v0 v1 v2 ~v3 ~v4
  = du_map'45'inv'45'trunc'45'Σ_550 v1 v2
du_map'45'inv'45'trunc'45'Σ_550 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  AgdaAny -> AgdaAny
du_map'45'inv'45'trunc'45'Σ_550 v0 v1
  = coe
      du_map'45'universal'45'property'45'trunc_106 (coe ()) (coe ())
      (coe v1) (coe du_trunc_22 (coe ()) (coe v1))
      (coe
         (\ v2 ->
            coe
              du_map'45'universal'45'property'45'trunc_106 v0 () v1
              (coe du_trunc_22 (coe ()) (coe v1))
              (\ v3 ->
                 coe
                   d_unit'45'trunc_38 () v1 erased
                   (coe
                      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
                      (coe
                         MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.d_pr1_26
                         (coe v2))
                      (coe v3)))
              (MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.d_pr2_28
                 (coe v2))))
-- foundation.truncations._.is-retraction-map-inv-trunc-Σ
d_is'45'retraction'45'map'45'inv'45'trunc'45'Σ_560 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  (AgdaAny -> ()) ->
  AgdaAny ->
  MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes.T_Id_14
d_is'45'retraction'45'map'45'inv'45'trunc'45'Σ_560 = erased
-- foundation.truncations._.is-section-map-inv-trunc-Σ
d_is'45'section'45'map'45'inv'45'trunc'45'Σ_586 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  (AgdaAny -> ()) ->
  AgdaAny ->
  MAlonzo.Code.QfoundationZ45Zcore.QidentityZ45Ztypes.T_Id_14
d_is'45'section'45'map'45'inv'45'trunc'45'Σ_586 = erased
-- foundation.truncations._.equiv-trunc-Σ
d_equiv'45'trunc'45'Σ_622 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  (AgdaAny -> ()) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_equiv'45'trunc'45'Σ_622 ~v0 v1 v2 ~v3 ~v4
  = du_equiv'45'trunc'45'Σ_622 v1 v2
du_equiv'45'trunc'45'Σ_622 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_equiv'45'trunc'45'Σ_622 v0 v1
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
      (coe du_map'45'trunc'45'Σ_538 (coe v0) (coe v1))
      (coe
         MAlonzo.Code.QfoundationZ45Zcore.Qequivalences.du_is'45'equiv'45'is'45'invertible_146
         (coe du_map'45'inv'45'trunc'45'Σ_550 (coe v0) (coe v1)) erased
         erased)
-- foundation.truncations._.inv-equiv-trunc-Σ
d_inv'45'equiv'45'trunc'45'Σ_626 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  () ->
  (AgdaAny -> ()) ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
d_inv'45'equiv'45'trunc'45'Σ_626 ~v0 v1 v2 ~v3 ~v4
  = du_inv'45'equiv'45'trunc'45'Σ_626 v1 v2
du_inv'45'equiv'45'trunc'45'Σ_626 ::
  MAlonzo.Code.Agda.Primitive.T_Level_18 ->
  MAlonzo.Code.QfoundationZ45Zcore.QtruncationZ45Zlevels.T_𝕋_4 ->
  MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.T_Σ_12
du_inv'45'equiv'45'trunc'45'Σ_626 v0 v1
  = coe
      MAlonzo.Code.Qfoundation.QdependentZ45ZpairZ45Ztypes.C_pair_30
      (coe du_map'45'inv'45'trunc'45'Σ_550 (coe v0) (coe v1))
      (coe
         MAlonzo.Code.QfoundationZ45Zcore.Qequivalences.du_is'45'equiv'45'is'45'invertible_146
         (coe du_map'45'trunc'45'Σ_538 (coe v0) (coe v1)) erased erased)
