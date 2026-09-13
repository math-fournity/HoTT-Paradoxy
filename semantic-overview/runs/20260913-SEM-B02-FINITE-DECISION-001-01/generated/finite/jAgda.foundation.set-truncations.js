var agdaRTS = require("agda-rts");

var h_10823327230712899574 = require("jAgda.foundation.dependent-pair-types");
var h_10698326953427394189 = require("jAgda.foundation.effective-maps-equivalence-relations");
var h_5216136863360517686 = require("jAgda.foundation.equality-coproduct-types");
var h_13070193349384219227 = require("jAgda.foundation.equivalences-contractible-types");
var h_7932228134871894119 = require("jAgda.foundation.functoriality-cartesian-product-types");
var h_5198847278490018244 = require("jAgda.foundation.functoriality-coproduct-types");
var h_7667273620339339099 = require("jAgda.foundation.mere-equality");
var h_16264356163029116985 = require("jAgda.foundation.morphisms-slice");
var h_9446248875876436424 = require("jAgda.foundation.postcomposition-functions");
var h_6746806437286055912 = require("jAgda.foundation.reflecting-maps-equivalence-relations");
var z_jAgda_foundation_retractions = require("jAgda.foundation.retractions");
var h_7421844154760758885 = require("jAgda.foundation.retracts-of-types");
var z_jAgda_foundation_sets = require("jAgda.foundation.sets");
var h_13973617263457888061 = require("jAgda.foundation.surjective-maps");
var z_jAgda_foundation_truncations = require("jAgda.foundation.truncations");
var h_2228770168641309355 = require("jAgda.foundation.uniqueness-set-truncations");
var h_10252439710734579043 = require("jAgda.foundation.unit-type");
var h_1457687909564816682 = require("jAgda.foundation.universal-property-coproduct-types");
var h_16356954940953503326 = require("jAgda.foundation.universal-property-dependent-pair-types");
var h_9404261176179494174 = require("jAgda.foundation.universal-property-image");
var h_5451024213145242139 = require("jAgda.foundation.universal-property-set-quotients");
var h_13072951035424358255 = require("jAgda.foundation.universal-property-set-truncation");
var h_13895875897459204243 = require("jAgda.foundation.universe-levels");
var h_17782012858669056648 = require("jAgda.foundation-core.cartesian-product-types");
var h_2418303217177004088 = require("jAgda.foundation-core.contractible-types");
var h_2062783598648249311 = require("jAgda.foundation-core.coproduct-types");
var h_2786395204839164476 = require("jAgda.foundation-core.embeddings");
var h_13003858539280958212 = require("jAgda.foundation-core.empty-types");
var h_13732920155217937999 = require("jAgda.foundation-core.equivalences");
var h_14760288009917190900 = require("jAgda.foundation-core.function-types");
var h_15242941738594866383 = require("jAgda.foundation-core.functoriality-dependent-function-types");
var h_11564779420424108469 = require("jAgda.foundation-core.functoriality-dependent-pair-types");
var h_5867296165752451136 = require("jAgda.foundation-core.homotopies");
var h_5153263140774292640 = require("jAgda.foundation-core.identity-types");
var h_2968556139525224136 = require("jAgda.foundation-core.propositions");
var h_5150322816240164337 = require("jAgda.foundation-core.truncation-levels");

exports["trunc-Set"] = a => z_jAgda_foundation_truncations["trunc"](a)(h_5150322816240164337["zero-𝕋"]);
exports["is-set-type-trunc-Set"] = a => b => z_jAgda_foundation_truncations["is-trunc-type-trunc"](a)(
    h_5150322816240164337["𝕋"]["succ-𝕋"](h_5150322816240164337["neg-one-𝕋"])
  )(null);
exports["unit-trunc-Set"] = a => b => z_jAgda_foundation_truncations["unit-trunc"](a)(h_5150322816240164337["zero-𝕋"])(null);
exports["unit-trunc-Set'"] = a => b => exports["unit-trunc-Set"](a)(null);
exports["is-set-truncation-trunc-Set"] = a => b => c => z_jAgda_foundation_truncations["is-truncation-trunc"](a)(
    h_5150322816240164337["𝕋"]["succ-𝕋"](
      h_5150322816240164337["𝕋"]["succ-𝕋"](
        h_5150322816240164337["𝕋"]["neg-two-𝕋"]
  ) ) )(null)(c);
exports[
"dependent-universal-property-trunc-Set"
] = a => b => c => z_jAgda_foundation_truncations[
  "_NameId 124 (ModuleNameHash 7980212233017128774)"
  ]["dependent-universal-property-trunc"](a)(h_5150322816240164337["zero-𝕋"])(null)(null);
exports[
"equiv-dependent-universal-property-trunc-Set"
] = a => b => c => z_jAgda_foundation_truncations[
  "_NameId 124 (ModuleNameHash 7980212233017128774)"
  ][
  "equiv-dependent-universal-property-trunc"
  ](a)(h_5150322816240164337["zero-𝕋"])(null)(null);
exports[
"_NameId 66 (ModuleNameHash 5664870595032622303)"
] = {};
exports[
"_NameId 66 (ModuleNameHash 5664870595032622303)"
][
"function-dependent-universal-property-trunc-Set"
] = a => b => c => d => e => z_jAgda_foundation_truncations[
  "_NameId 124 (ModuleNameHash 7980212233017128774)"
  ][
  "function-dependent-universal-property-trunc"
  ](a)(h_5150322816240164337["zero-𝕋"])(null)(null)(d)(e);
exports[
"_NameId 66 (ModuleNameHash 5664870595032622303)"
][
"apply-dependent-universal-property-trunc-Set'"
] = a => b => c => d => e => h_13732920155217937999[
  "_NameId 222 (ModuleNameHash 12729305969224249291)"
  ]["map-inv-equiv"](null)(null)(null)(null)(
    exports[
    "equiv-dependent-universal-property-trunc-Set"
    ](a)(null)(null)(d)
  )(e);
exports[
"_NameId 98 (ModuleNameHash 5664870595032622303)"
] = {};
exports[
"_NameId 98 (ModuleNameHash 5664870595032622303)"
][
"apply-twice-dependent-universal-property-trunc-Set'"
] = a => b => c => d => e => f => g => exports[
  "_NameId 66 (ModuleNameHash 5664870595032622303)"
  ][
  "apply-dependent-universal-property-trunc-Set'"
  ](a)(null)(null)(
      h => z_jAgda_foundation_sets["Π-Set"](null)(null)(null)(f(h))
  )(
      h => exports[
    "_NameId 66 (ModuleNameHash 5664870595032622303)"
    ][
    "apply-dependent-universal-property-trunc-Set'"
    ](b)(null)(null)(
      f(exports["unit-trunc-Set"](a)(null)(h))
    )(g(h))
  );
exports[
"_NameId 132 (ModuleNameHash 5664870595032622303)"
] = {};
exports[
"_NameId 132 (ModuleNameHash 5664870595032622303)"
][
"apply-thrice-dependent-universal-property-trunc-Set'"
] = a => b => c => d => e => f => g => h => i => exports[
  "_NameId 98 (ModuleNameHash 5664870595032622303)"
  ][
  "apply-twice-dependent-universal-property-trunc-Set'"
  ](a)(b)(null)(null)(null)(
      j => k => z_jAgda_foundation_sets["Π-Set"](null)(null)(null)(h(j)(k))
  )(
      j => k => exports[
    "_NameId 66 (ModuleNameHash 5664870595032622303)"
    ][
    "apply-dependent-universal-property-trunc-Set'"
    ](c)(null)(null)(
      h(exports["unit-trunc-Set"](a)(null)(j))(exports["unit-trunc-Set"](b)(null)(k))
    )(i(j)(k))
  );
exports["universal-property-trunc-Set"] = a => b => c => z_jAgda_foundation_truncations["universal-property-trunc"](a)(h_5150322816240164337["zero-𝕋"])(null)(c);
exports[
"_NameId 190 (ModuleNameHash 5664870595032622303)"
] = {};
exports[
"_NameId 190 (ModuleNameHash 5664870595032622303)"
]["equiv-universal-property-trunc-Set"] = a => b => c => d => z_jAgda_foundation_truncations["equiv-universal-property-trunc"](a)(b)(
    h_5150322816240164337["𝕋"]["succ-𝕋"](
      h_5150322816240164337["𝕋"]["succ-𝕋"](
        h_5150322816240164337["𝕋"]["neg-two-𝕋"]
  ) ) )(null)(d);
exports[
"_NameId 190 (ModuleNameHash 5664870595032622303)"
]["apply-universal-property-trunc-Set"] = a => b => c => d => e => f => z_jAgda_foundation_truncations[
  "_NameId 82 (ModuleNameHash 7980212233017128774)"
  ]["map-universal-property-trunc"](a)(b)(
    h_5150322816240164337["𝕋"]["succ-𝕋"](
      h_5150322816240164337["𝕋"]["succ-𝕋"](
        h_5150322816240164337["𝕋"]["neg-two-𝕋"]
  ) ) )(null)(d)(f)(e);
exports[
"_NameId 190 (ModuleNameHash 5664870595032622303)"
]["map-universal-property-trunc-Set"] = a => b => c => d => z_jAgda_foundation_truncations[
  "_NameId 82 (ModuleNameHash 7980212233017128774)"
  ]["map-universal-property-trunc"](a)(b)(
    h_5150322816240164337["𝕋"]["succ-𝕋"](
      h_5150322816240164337["𝕋"]["succ-𝕋"](
        h_5150322816240164337["𝕋"]["neg-two-𝕋"]
  ) ) )(null)(d);
exports["apply-universal-property-trunc-Set'"] = a => b => c => d => e => f => exports[
  "_NameId 190 (ModuleNameHash 5664870595032622303)"
  ]["map-universal-property-trunc-Set"](a)(b)(null)(e)(f)(d);
exports[
"reflecting-map-mere-eq-unit-trunc-Set"
] = a => b => h_10823327230712899574["pair"](exports["unit-trunc-Set"](a)(null))(null);
exports["is-set-quotient-trunc-Set"] = a => b => c => h_13072951035424358255["is-set-quotient-is-set-truncation"](null)(null)(null)(null)(null)(
    exports["is-set-truncation-trunc-Set"](a)(null)
  )(c);
exports[
"_NameId 262 (ModuleNameHash 5664870595032622303)"
] = {};
exports[
"_NameId 262 (ModuleNameHash 5664870595032622303)"
][
"is-surjective-and-effective-unit-trunc-Set"
] = a => b => h_5451024213145242139[
  "_NameId 464 (ModuleNameHash 17822779249686690915)"
  ][
  "is-surjective-and-effective-is-set-quotient"
  ](null)(null)(null)(null)(
    h_7667273620339339099["mere-eq-equivalence-relation"](a)(null)
  )(exports["trunc-Set"](a)(null))(
    h_10823327230712899574["pair"](exports["unit-trunc-Set"](a)(null))(null)
  )(
    exports["is-set-quotient-trunc-Set"](a)(null)
  );
exports[
"_NameId 262 (ModuleNameHash 5664870595032622303)"
]["is-surjective-unit-trunc-Set"] = a => b => h_10823327230712899574["Σ"]["pr1"](
    exports[
    "_NameId 262 (ModuleNameHash 5664870595032622303)"
    ][
    "is-surjective-and-effective-unit-trunc-Set"
    ](a)(null)
  );
exports[
"_NameId 262 (ModuleNameHash 5664870595032622303)"
]["is-effective-unit-trunc-Set"] = a => b => h_10823327230712899574["Σ"]["pr2"](
    exports[
    "_NameId 262 (ModuleNameHash 5664870595032622303)"
    ][
    "is-surjective-and-effective-unit-trunc-Set"
    ](a)(null)
  );
exports[
"_NameId 262 (ModuleNameHash 5664870595032622303)"
]["apply-effectiveness-unit-trunc-Set"] = a => b => c => d => h_10823327230712899574["Σ"]["pr1"](
    exports[
    "_NameId 262 (ModuleNameHash 5664870595032622303)"
    ]["is-effective-unit-trunc-Set"](a)(null)(c)(d)
  );
exports[
"_NameId 262 (ModuleNameHash 5664870595032622303)"
]["emb-trunc-Set"] = a => b => h_5451024213145242139[
  "_NameId 204 (ModuleNameHash 17822779249686690915)"
  ]["emb-is-surjective-and-effective"](null)(null)(null)(null)(
    h_7667273620339339099["mere-eq-equivalence-relation"](a)(null)
  )(exports["trunc-Set"](a)(null))(exports["unit-trunc-Set"](a)(null))(
    exports[
    "_NameId 262 (ModuleNameHash 5664870595032622303)"
    ][
    "is-surjective-and-effective-unit-trunc-Set"
    ](a)(null)
  );
exports[
"_NameId 262 (ModuleNameHash 5664870595032622303)"
]["hom-slice-trunc-Set"] = a => b => h_10823327230712899574["pair"](exports["unit-trunc-Set"](a)(null))(null);
exports[
"_NameId 262 (ModuleNameHash 5664870595032622303)"
]["is-image-trunc-Set"] = a => b => c => h_5451024213145242139[
  "_NameId 204 (ModuleNameHash 17822779249686690915)"
  ][
  "is-image-is-surjective-and-effective"
  ](null)(null)(null)(null)(
    h_7667273620339339099["mere-eq-equivalence-relation"](a)(null)
  )(exports["trunc-Set"](a)(null))(exports["unit-trunc-Set"](a)(null))(
    exports[
    "_NameId 262 (ModuleNameHash 5664870595032622303)"
    ][
    "is-surjective-and-effective-unit-trunc-Set"
    ](a)(null)
  )(c);
exports[
"_NameId 336 (ModuleNameHash 5664870595032622303)"
] = {};
exports[
"_NameId 336 (ModuleNameHash 5664870595032622303)"
]["is-equiv-is-set-truncation'"] = a => b => c => d => e => f => g => h => h_2228770168641309355[
  "_NameId 6 (ModuleNameHash 16558898588672841477)"
  ][
  "is-equiv-is-set-truncation-is-set-truncation"
  ](null)(b)(null)(null)(d)(e)(null)(exports["unit-trunc-Set"](a)(null))(null)(null)(null)(
    exports["is-set-truncation-trunc-Set"](a)(null)
  );
exports[
"_NameId 336 (ModuleNameHash 5664870595032622303)"
]["is-set-truncation-is-equiv'"] = a => b => c => d => e => f => g => h => i => h_2228770168641309355[
  "_NameId 6 (ModuleNameHash 16558898588672841477)"
  ][
  "is-set-truncation-is-equiv-is-set-truncation"
  ](null)(null)(null)(null)(null)(null)(null)(null)(f)(null)(
    exports["is-set-truncation-trunc-Set"](a)(null)
  )(h)(i);
exports[
"_NameId 366 (ModuleNameHash 5664870595032622303)"
] = {};
exports[
"_NameId 366 (ModuleNameHash 5664870595032622303)"
]["is-equiv-is-set-truncation"] = a => b => c => d => e => f => g => h => h_2228770168641309355[
  "_NameId 6 (ModuleNameHash 16558898588672841477)"
  ][
  "is-equiv-is-set-truncation-is-set-truncation"
  ](null)(a)(null)(null)(exports["trunc-Set"](a)(null))(exports["unit-trunc-Set"](a)(null))(null)(e)(null)(null)(null)(h);
exports[
"_NameId 366 (ModuleNameHash 5664870595032622303)"
]["is-set-truncation-is-equiv"] = a => b => c => d => e => f => g => h => i => h_2228770168641309355[
  "_NameId 6 (ModuleNameHash 16558898588672841477)"
  ][
  "is-set-truncation-is-set-truncation-is-equiv"
  ](null)(null)(null)(null)(null)(null)(null)(null)(f)(null)(h)(
    exports["is-set-truncation-trunc-Set"](a)(null)
  )(i);
exports["is-equiv-unit-trunc-Set"] = a => z_jAgda_foundation_truncations[
  "_NameId 358 (ModuleNameHash 7980212233017128774)"
  ]["is-equiv-unit-trunc"](a)(
    h_5150322816240164337["𝕋"]["succ-𝕋"](
      h_5150322816240164337["𝕋"]["succ-𝕋"](
        h_5150322816240164337["𝕋"]["neg-two-𝕋"]
  ) ) );
exports["equiv-unit-trunc-Set"] = a => z_jAgda_foundation_truncations[
  "_NameId 358 (ModuleNameHash 7980212233017128774)"
  ]["equiv-unit-trunc"](a)(
    h_5150322816240164337["𝕋"]["succ-𝕋"](
      h_5150322816240164337["𝕋"]["succ-𝕋"](
        h_5150322816240164337["𝕋"]["neg-two-𝕋"]
  ) ) );
exports["is-contr-trunc-Set"] = a => b => c => h_13070193349384219227[
  "_NameId 32 (ModuleNameHash 7521924699594338453)"
  ]["is-contr-equiv'"](null)(null)(null)(null)(
    exports["equiv-unit-trunc-Set"](a)(
      h_10823327230712899574["pair"](b)(
        z_jAgda_foundation_sets["is-set-is-contr"](a)(null)(c)
  ) ) )(c);
exports[
"_NameId 442 (ModuleNameHash 5664870595032622303)"
] = {};
exports[
"_NameId 442 (ModuleNameHash 5664870595032622303)"
]["uniqueness-trunc-Set"] = a => b => c => d => e => f => h_2228770168641309355[
  "_NameId 48 (ModuleNameHash 16558898588672841477)"
  ]["uniqueness-set-truncation"](null)(a)(b)(null)(exports["trunc-Set"](a)(null))(exports["unit-trunc-Set"](a)(null))(d)(e)(
    exports["is-set-truncation-trunc-Set"](a)(null)
  )(f);
exports[
"_NameId 442 (ModuleNameHash 5664870595032622303)"
]["equiv-uniqueness-trunc-Set"] = a => b => c => d => e => f => h_10823327230712899574["Σ"]["pr1"](
    h_2418303217177004088["center"](null)(null)(
      exports[
      "_NameId 442 (ModuleNameHash 5664870595032622303)"
      ]["uniqueness-trunc-Set"](a)(b)(null)(d)(e)(f)
  ) );
exports[
"_NameId 442 (ModuleNameHash 5664870595032622303)"
]["map-equiv-uniqueness-trunc-Set"] = a => b => c => d => e => f => h_10823327230712899574["Σ"]["pr1"](
    exports[
    "_NameId 442 (ModuleNameHash 5664870595032622303)"
    ]["equiv-uniqueness-trunc-Set"](a)(b)(null)(d)(e)(f)
  );
exports[
"_NameId 470 (ModuleNameHash 5664870595032622303)"
] = {};
exports[
"_NameId 470 (ModuleNameHash 5664870595032622303)"
]["uniqueness-trunc-Set'"] = a => b => c => d => e => f => h_2228770168641309355[
  "_NameId 48 (ModuleNameHash 16558898588672841477)"
  ]["uniqueness-set-truncation"](null)(b)(a)(null)(d)(e)(exports["trunc-Set"](a)(null))(exports["unit-trunc-Set"](a)(null))(f)(
    exports["is-set-truncation-trunc-Set"](a)(null)
  );
exports[
"_NameId 470 (ModuleNameHash 5664870595032622303)"
]["equiv-uniqueness-trunc-Set'"] = a => b => c => d => e => f => h_10823327230712899574["Σ"]["pr1"](
    h_2418303217177004088["center"](null)(null)(
      exports[
      "_NameId 470 (ModuleNameHash 5664870595032622303)"
      ]["uniqueness-trunc-Set'"](a)(b)(null)(d)(e)(f)
  ) );
exports[
"_NameId 470 (ModuleNameHash 5664870595032622303)"
]["map-equiv-uniqueness-trunc-Set'"] = a => b => c => d => e => f => h_10823327230712899574["Σ"]["pr1"](
    exports[
    "_NameId 470 (ModuleNameHash 5664870595032622303)"
    ]["equiv-uniqueness-trunc-Set'"](a)(b)(null)(d)(e)(f)
  );
exports[
"_NameId 498 (ModuleNameHash 5664870595032622303)"
] = {};
exports[
"_NameId 498 (ModuleNameHash 5664870595032622303)"
]["equiv-unit-trunc-set"] = a => b => z_jAgda_foundation_truncations[
  "_NameId 358 (ModuleNameHash 7980212233017128774)"
  ]["equiv-unit-trunc"](a)(
    h_5150322816240164337["𝕋"]["succ-𝕋"](
      h_5150322816240164337["𝕋"]["succ-𝕋"](
        h_5150322816240164337["𝕋"]["neg-two-𝕋"]
  ) ) )(b);
exports["retract-Set-UU"] = a => h_10823327230712899574["pair"](
      b => h_10823327230712899574["Σ"]["pr1"](b)
  )(
    h_10823327230712899574["pair"](exports["trunc-Set"](a))(null)
  );
exports[
"_NameId 520 (ModuleNameHash 5664870595032622303)"
] = {};
exports[
"_NameId 520 (ModuleNameHash 5664870595032622303)"
]["distributive-trunc-coproduct-Set"] = a => b => c => d => exports[
  "_NameId 442 (ModuleNameHash 5664870595032622303)"
  ]["uniqueness-trunc-Set"](null)(null)(null)(
    h_5216136863360517686["coproduct-Set"](null)(null)(exports["trunc-Set"](a)(null))(exports["trunc-Set"](b)(null))
  )(
    h_5198847278490018244[
    "_NameId 6 (ModuleNameHash 10818589992476166280)"
    ]["map-coproduct"](null)(null)(null)(null)(null)(null)(null)(null)(exports["unit-trunc-Set"](a)(null))(exports["unit-trunc-Set"](b)(null))
  )(
      e => f => h_13732920155217937999[
    "_NameId 454 (ModuleNameHash 12729305969224249291)"
    ]["is-equiv-right-factor"](null)(null)(null)(null)(null)(null)(
      h_1457687909564816682[
      "_NameId 6 (ModuleNameHash 14437841148830725153)"
      ]["ev-inl-inr"](null)(null)(null)(null)(null)(null)
    )(null)(
      h_1457687909564816682[
      "_NameId 6 (ModuleNameHash 14437841148830725153)"
      ]["universal-property-coproduct"](null)(null)(null)(null)(null)(null)
    )(
      h_13732920155217937999[
      "_NameId 366 (ModuleNameHash 12729305969224249291)"
      ]["is-equiv-comp"](null)(null)(null)(null)(null)(null)(null)(null)(
        h_1457687909564816682[
        "_NameId 6 (ModuleNameHash 14437841148830725153)"
        ]["universal-property-coproduct"](null)(null)(null)(null)(null)(null)
      )(
        h_7932228134871894119[
        "_NameId 172 (ModuleNameHash 10403123445029018779)"
        ]["is-equiv-map-product"](null)(null)(null)(null)(null)(null)(null)(null)(null)(null)(
          exports["is-set-truncation-trunc-Set"](a)(null)(e)(f)
        )(
          exports["is-set-truncation-trunc-Set"](b)(null)(e)(f)
  ) ) ) );
exports[
"_NameId 520 (ModuleNameHash 5664870595032622303)"
][
"equiv-distributive-trunc-coproduct-Set"
] = a => b => c => d => h_10823327230712899574["Σ"]["pr1"](
    h_2418303217177004088["center"](null)(null)(
      exports[
      "_NameId 520 (ModuleNameHash 5664870595032622303)"
      ]["distributive-trunc-coproduct-Set"](a)(b)(null)(null)
  ) );
exports[
"_NameId 520 (ModuleNameHash 5664870595032622303)"
][
"map-equiv-distributive-trunc-coproduct-Set"
] = a => b => c => d => h_10823327230712899574["Σ"]["pr1"](
    exports[
    "_NameId 520 (ModuleNameHash 5664870595032622303)"
    ][
    "equiv-distributive-trunc-coproduct-Set"
    ](a)(b)(null)(null)
  );
exports[
"_NameId 550 (ModuleNameHash 5664870595032622303)"
] = {};
exports[
"_NameId 550 (ModuleNameHash 5664870595032622303)"
]["trunc-Σ-Set"] = a => b => c => d => exports[
  "_NameId 442 (ModuleNameHash 5664870595032622303)"
  ]["uniqueness-trunc-Set"](null)(null)(null)(exports["trunc-Set"](null)(null))(
    h_14760288009917190900["_∘_"](null)(null)(null)(null)(null)(null)(
        e => exports["unit-trunc-Set"](null)(null)
    )(
      h_11564779420424108469[
      "_NameId 6 (ModuleNameHash 3121437647020500036)"
      ]["tot"](null)(null)(null)(null)(null)(null)(
          e => exports["unit-trunc-Set"](b)(null)
  ) ) )(
      e => f => h_13732920155217937999[
    "_NameId 454 (ModuleNameHash 12729305969224249291)"
    ]["is-equiv-right-factor"](null)(null)(null)(null)(null)(null)(
        g => h => i => g(h_10823327230712899574["pair"](h)(i))
    )(null)(
      h_16356954940953503326[
      "_NameId 6 (ModuleNameHash 12959987678419543149)"
      ]["is-equiv-ev-pair"](null)(null)(null)(null)(null)(null)
    )(
      h_13732920155217937999[
      "_NameId 484 (ModuleNameHash 12729305969224249291)"
      ]["is-equiv-htpy-equiv"](null)(null)(null)(null)(null)(
        h_13732920155217937999[
        "_NameId 366 (ModuleNameHash 12729305969224249291)"
        ]["_∘e_"](null)(null)(null)(null)(null)(null)(
          h_15242941738594866383[
          "_NameId 184 (ModuleNameHash 11317354623944083570)"
          ]["equiv-Π-equiv-family"](null)(null)(null)(null)(null)(null)(
              g => exports[
            "_NameId 190 (ModuleNameHash 5664870595032622303)"
            ]["equiv-universal-property-trunc-Set"](b)(e)(null)(f)
        ) )(
          h_13732920155217937999[
          "_NameId 366 (ModuleNameHash 12729305969224249291)"
          ]["_∘e_"](null)(null)(null)(null)(null)(null)(
            h_16356954940953503326[
            "_NameId 6 (ModuleNameHash 12959987678419543149)"
            ]["equiv-ev-pair"](null)(null)(null)(null)(null)(null)
          )(
            exports[
            "_NameId 190 (ModuleNameHash 5664870595032622303)"
            ]["equiv-universal-property-trunc-Set"](null)(e)(null)(f)
      ) ) )(null)
  ) );
exports[
"_NameId 550 (ModuleNameHash 5664870595032622303)"
]["equiv-trunc-Σ-Set"] = a => b => c => d => h_10823327230712899574["Σ"]["pr1"](
    h_2418303217177004088["center"](null)(null)(
      exports[
      "_NameId 550 (ModuleNameHash 5664870595032622303)"
      ]["trunc-Σ-Set"](null)(b)(null)(null)
  ) );
exports[
"_NameId 550 (ModuleNameHash 5664870595032622303)"
]["map-equiv-trunc-Σ-Set"] = a => b => c => d => h_10823327230712899574["Σ"]["pr1"](
    exports[
    "_NameId 550 (ModuleNameHash 5664870595032622303)"
    ]["equiv-trunc-Σ-Set"](null)(b)(null)(null)
  );
exports[
"_NameId 590 (ModuleNameHash 5664870595032622303)"
] = {};
exports[
"_NameId 590 (ModuleNameHash 5664870595032622303)"
]["distributive-trunc-product-Set"] = a => b => c => d => exports[
  "_NameId 442 (ModuleNameHash 5664870595032622303)"
  ]["uniqueness-trunc-Set"](null)(null)(null)(
    z_jAgda_foundation_sets["product-Set"](null)(null)(exports["trunc-Set"](a)(null))(exports["trunc-Set"](b)(null))
  )(
    h_7932228134871894119[
    "_NameId 6 (ModuleNameHash 10403123445029018779)"
    ]["map-product"](null)(null)(null)(null)(null)(null)(null)(null)(exports["unit-trunc-Set"](a)(null))(exports["unit-trunc-Set"](b)(null))
  )(
      e => f => h_13732920155217937999[
    "_NameId 454 (ModuleNameHash 12729305969224249291)"
    ]["is-equiv-right-factor"](null)(null)(null)(null)(null)(null)(
        g => h => i => g(h_10823327230712899574["pair"](h)(i))
    )(null)(
      h_16356954940953503326[
      "_NameId 6 (ModuleNameHash 12959987678419543149)"
      ]["is-equiv-ev-pair"](null)(null)(null)(null)(null)(null)
    )(
      h_13732920155217937999[
      "_NameId 484 (ModuleNameHash 12729305969224249291)"
      ]["is-equiv-htpy-equiv"](null)(null)(null)(null)(null)(
        h_13732920155217937999[
        "_NameId 366 (ModuleNameHash 12729305969224249291)"
        ]["_∘e_"](null)(null)(null)(null)(null)(null)(
          exports[
          "_NameId 190 (ModuleNameHash 5664870595032622303)"
          ]["equiv-universal-property-trunc-Set"](a)(null)(null)(
            z_jAgda_foundation_sets["Π-Set'"](null)(null)(null)(g => f)
        ) )(
          h_13732920155217937999[
          "_NameId 366 (ModuleNameHash 12729305969224249291)"
          ]["_∘e_"](null)(null)(null)(null)(null)(null)(
            h_9446248875876436424["equiv-postcomp"](null)(null)(null)(null)(null)(null)(
              exports[
              "_NameId 190 (ModuleNameHash 5664870595032622303)"
              ]["equiv-universal-property-trunc-Set"](b)(e)(null)(f)
          ) )(
            h_16356954940953503326[
            "_NameId 6 (ModuleNameHash 12959987678419543149)"
            ]["equiv-ev-pair"](null)(null)(null)(null)(null)(null)
      ) ) )(null)
  ) );
exports[
"_NameId 590 (ModuleNameHash 5664870595032622303)"
][
"equiv-distributive-trunc-product-Set"
] = a => b => c => d => h_10823327230712899574["Σ"]["pr1"](
    h_2418303217177004088["center"](null)(null)(
      exports[
      "_NameId 590 (ModuleNameHash 5664870595032622303)"
      ]["distributive-trunc-product-Set"](a)(b)(null)(null)
  ) );
exports[
"_NameId 590 (ModuleNameHash 5664870595032622303)"
][
"map-equiv-distributive-trunc-product-Set"
] = a => b => c => d => h_10823327230712899574["Σ"]["pr1"](
    exports[
    "_NameId 590 (ModuleNameHash 5664870595032622303)"
    ][
    "equiv-distributive-trunc-product-Set"
    ](a)(b)(null)(null)
  );
exports[
"_NameId 590 (ModuleNameHash 5664870595032622303)"
][
"map-inv-equiv-distributive-trunc-product-Set"
] = a => b => c => d => h_13732920155217937999[
  "_NameId 222 (ModuleNameHash 12729305969224249291)"
  ]["map-inv-equiv"](null)(null)(null)(null)(
    exports[
    "_NameId 590 (ModuleNameHash 5664870595032622303)"
    ][
    "equiv-distributive-trunc-product-Set"
    ](a)(b)(null)(null)
  );
exports["equiv-unit-trunc-empty-Set"] = exports["equiv-unit-trunc-Set"](null)(h_13003858539280958212["empty-Set"]);
exports["equiv-unit-trunc-unit-Set"] = exports["equiv-unit-trunc-Set"](null)(h_10252439710734579043["unit-Set"]);
