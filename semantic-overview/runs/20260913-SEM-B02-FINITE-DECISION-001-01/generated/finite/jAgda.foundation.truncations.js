var agdaRTS = require("agda-rts");

var h_10703868370912634042 = require("jAgda.foundation.action-on-identifications-functions");
var h_13987581571296672568 = require("jAgda.foundation.contractible-types");
var h_10823327230712899574 = require("jAgda.foundation.dependent-pair-types");
var h_10420338014630663402 = require("jAgda.foundation.dependent-products-contractible-types");
var h_16941223491982578228 = require("jAgda.foundation.dependent-products-truncated-types");
var h_13070193349384219227 = require("jAgda.foundation.equivalences-contractible-types");
var h_3983882577351044911 = require("jAgda.foundation.function-extensionality");
var h_15039806190516174065 = require("jAgda.foundation.function-extensionality-axiom");
var h_11039019999760051401 = require("jAgda.foundation.functoriality-dependent-function-types");
var h_16806042658982196604 = require("jAgda.foundation.fundamental-theorem-of-identity-types");
var h_16838802912213570003 = require("jAgda.foundation.identity-types");
var h_14534997119401925645 = require("jAgda.foundation.truncated-types");
var h_16356954940953503326 = require("jAgda.foundation.universal-property-dependent-pair-types");
var h_13895875897459204243 = require("jAgda.foundation.universe-levels");
var h_1030295682763128560 = require("jAgda.foundation.whiskering-homotopies-composition");
var h_48501317845670118 = require("jAgda.foundation-core.contractible-maps");
var h_2418303217177004088 = require("jAgda.foundation-core.contractible-types");
var h_9124282701215928881 = require("jAgda.foundation-core.equality-dependent-pair-types");
var h_13732920155217937999 = require("jAgda.foundation-core.equivalences");
var h_10876773354425769947 = require("jAgda.foundation-core.fibers-of-maps");
var h_14760288009917190900 = require("jAgda.foundation-core.function-types");
var h_15242941738594866383 = require("jAgda.foundation-core.functoriality-dependent-function-types");
var h_11564779420424108469 = require("jAgda.foundation-core.functoriality-dependent-pair-types");
var h_5867296165752451136 = require("jAgda.foundation-core.homotopies");
var h_5641685678543537553 = require("jAgda.foundation-core.precomposition-functions");
var h_2968556139525224136 = require("jAgda.foundation-core.propositions");
var h_7698443413829557010 = require("jAgda.foundation-core.retractions");
var h_15054705020946909390 = require("jAgda.foundation-core.retracts-of-types");
var h_8972795701410112077 = require("jAgda.foundation-core.sections");
var h_11234684111983375459 = require("jAgda.foundation-core.torsorial-type-families");
var h_18376098553934461998 = require("jAgda.foundation-core.truncated-types");
var h_5150322816240164337 = require("jAgda.foundation-core.truncation-levels");
var h_2533281586512140065 = require("jAgda.foundation-core.universal-property-truncation");

exports["trunc"] = a => b => c => h_10823327230712899574["pair"](null)(
    exports["is-trunc-type-trunc"](a)(b)(null)
  );
exports["equiv-universal-property-trunc"] = a => b => c => d => e => h_10823327230712899574["pair"](
    h_5641685678543537553[
    "_NameId 6 (ModuleNameHash 11376859841528145647)"
    ]["precomp"](null)(null)(null)(null)(null)(exports["unit-trunc"](a)(c)(null))(null)
  )(
    exports["is-truncation-trunc"](a)(c)(null)(b)(e)
  );
exports["universal-property-trunc"] = a => b => c => d => h_2533281586512140065[
  "_NameId 178 (ModuleNameHash 12419389839831763855)"
  ][
  "universal-property-truncation-is-truncation"
  ](null)(null)(null)(null)(null)(null)(
    exports["is-truncation-trunc"](a)(b)(null)
  )(d);
exports[
"_NameId 82 (ModuleNameHash 7980212233017128774)"
] = {};
exports[
"_NameId 82 (ModuleNameHash 7980212233017128774)"
]["apply-universal-property-trunc"] = a => b => c => d => e => f => h_2418303217177004088["center"](null)(null)(
    h_2533281586512140065[
    "_NameId 178 (ModuleNameHash 12419389839831763855)"
    ][
    "universal-property-truncation-is-truncation"
    ](null)(null)(null)(null)(null)(null)(
      exports["is-truncation-trunc"](a)(c)(null)
    )(b)(e)(f)
  );
exports[
"_NameId 82 (ModuleNameHash 7980212233017128774)"
]["map-universal-property-trunc"] = a => b => c => d => e => f => h_10823327230712899574["Σ"]["pr1"](
    exports[
    "_NameId 82 (ModuleNameHash 7980212233017128774)"
    ]["apply-universal-property-trunc"](a)(b)(c)(null)(e)(f)
  );
exports[
"_NameId 124 (ModuleNameHash 7980212233017128774)"
] = {};
exports[
"_NameId 124 (ModuleNameHash 7980212233017128774)"
]["dependent-universal-property-trunc"] = a => b => c => d => h_2533281586512140065[
  "_NameId 248 (ModuleNameHash 12419389839831763855)"
  ][
  "dependent-universal-property-truncation-is-truncation"
  ](null)(a)(b)(null)(exports["trunc"](a)(b)(null))(exports["unit-trunc"](a)(b)(null))(
    exports["is-truncation-trunc"](a)(b)(null)
  )(null);
exports[
"_NameId 124 (ModuleNameHash 7980212233017128774)"
][
"equiv-dependent-universal-property-trunc"
] = a => b => c => d => e => h_10823327230712899574["pair"](
      f => g => f(exports["unit-trunc"](a)(b)(null)(g))
  )(
    exports[
    "_NameId 124 (ModuleNameHash 7980212233017128774)"
    ]["dependent-universal-property-trunc"](a)(b)(null)(null)(e)
  );
exports[
"_NameId 124 (ModuleNameHash 7980212233017128774)"
]["unique-dependent-function-trunc"] = a => b => c => d => e => f => h_13070193349384219227[
  "_NameId 32 (ModuleNameHash 7521924699594338453)"
  ]["is-contr-equiv'"](null)(null)(null)(null)(
    h_11564779420424108469[
    "_NameId 352 (ModuleNameHash 3121437647020500036)"
    ]["equiv-tot"](null)(null)(null)(null)(null)(null)(
        g => h_3983882577351044911[
      "_NameId 38 (ModuleNameHash 16845966502362288139)"
      ]["equiv-funext"](null)(null)(null)(null)(null)(null)
  ) )(
    h_48501317845670118[
    "_NameId 110 (ModuleNameHash 16045497013434728364)"
    ]["is-contr-map-is-equiv"](null)(null)(null)(null)(null)(
      exports[
      "_NameId 124 (ModuleNameHash 7980212233017128774)"
      ]["dependent-universal-property-trunc"](a)(b)(null)(null)(e)
    )(f)
  );
exports[
"_NameId 124 (ModuleNameHash 7980212233017128774)"
][
"apply-dependent-universal-property-trunc"
] = a => b => c => d => e => f => h_2418303217177004088["center"](null)(null)(
    exports[
    "_NameId 124 (ModuleNameHash 7980212233017128774)"
    ]["unique-dependent-function-trunc"](a)(b)(null)(null)(e)(f)
  );
exports[
"_NameId 124 (ModuleNameHash 7980212233017128774)"
][
"function-dependent-universal-property-trunc"
] = a => b => c => d => e => f => h_10823327230712899574["Σ"]["pr1"](
    exports[
    "_NameId 124 (ModuleNameHash 7980212233017128774)"
    ][
    "apply-dependent-universal-property-trunc"
    ](a)(b)(null)(null)(e)(f)
  );
exports["unique-truncated-fam-trunc"] = a => b => c => d => e => h_13070193349384219227[
  "_NameId 32 (ModuleNameHash 7521924699594338453)"
  ]["is-contr-equiv'"](null)(null)(null)(null)(
    h_11564779420424108469[
    "_NameId 352 (ModuleNameHash 3121437647020500036)"
    ]["equiv-tot"](null)(null)(null)(null)(null)(null)(
        f => h_15242941738594866383[
      "_NameId 184 (ModuleNameHash 11317354623944083570)"
      ]["equiv-Π-equiv-family"](null)(null)(null)(null)(null)(null)(
          g => h_13732920155217937999[
        "_NameId 366 (ModuleNameHash 12729305969224249291)"
        ]["_∘e_"](null)(null)(null)(null)(null)(null)(
          h_14534997119401925645["extensionality-Truncated-Type"](null)(null)(e(g))(
            h_14760288009917190900["_∘_"](null)(null)(null)(null)(null)(null)(h => f)(
              exports["unit-trunc"](a)(
                h_5150322816240164337["𝕋"]["succ-𝕋"](c)
              )(null)
            )(g)
        ) )(
          h_16838802912213570003[
          "_NameId 68 (ModuleNameHash 14912215433483829617)"
          ]["equiv-inv"](null)(null)(null)(null)
  ) ) ) )(
    exports["universal-property-trunc"](a)(
      h_5150322816240164337["𝕋"]["succ-𝕋"](c)
    )(null)(null)(
      h_14534997119401925645["Truncated-Type-Truncated-Type"](b)(c)
    )(e)
  );
exports[
"_NameId 250 (ModuleNameHash 7980212233017128774)"
] = {};
exports[
"_NameId 250 (ModuleNameHash 7980212233017128774)"
]["truncated-fam-trunc"] = a => b => c => d => e => h_10823327230712899574["Σ"]["pr1"](
    h_2418303217177004088["center"](null)(null)(
      exports["unique-truncated-fam-trunc"](a)(b)(c)(null)(e)
  ) );
exports[
"_NameId 250 (ModuleNameHash 7980212233017128774)"
]["compute-truncated-fam-trunc"] = a => b => c => d => e => h_10823327230712899574["Σ"]["pr2"](
    h_2418303217177004088["center"](null)(null)(
      exports["unique-truncated-fam-trunc"](a)(b)(c)(null)(e)
  ) );
exports[
"_NameId 250 (ModuleNameHash 7980212233017128774)"
]["map-compute-truncated-fam-trunc"] = a => b => c => d => e => f => h_10823327230712899574["Σ"]["pr1"](
    exports[
    "_NameId 250 (ModuleNameHash 7980212233017128774)"
    ]["compute-truncated-fam-trunc"](a)(b)(c)(null)(e)(f)
  );
exports[
"_NameId 280 (ModuleNameHash 7980212233017128774)"
] = {};
exports[
"_NameId 280 (ModuleNameHash 7980212233017128774)"
][
"dependent-universal-property-total-truncated-fam-trunc"
] = a => b => c => d => e => f => g => h => h_13070193349384219227[
  "_NameId 6 (ModuleNameHash 7521924699594338453)"
  ]["is-contr-equiv"](null)(null)(null)(null)(
    h_11564779420424108469[
    "_NameId 662 (ModuleNameHash 3121437647020500036)"
    ]["equiv-Σ"](null)(null)(null)(null)(null)(null)(null)(null)(
      h_16356954940953503326[
      "_NameId 6 (ModuleNameHash 12959987678419543149)"
      ]["equiv-ev-pair"](null)(null)(null)(null)(null)(null)
    )(
        i => h_15242941738594866383[
      "_NameId 184 (ModuleNameHash 11317354623944083570)"
      ]["equiv-Π-equiv-family"](null)(null)(null)(null)(null)(null)(
          j => h_13732920155217937999[
        "_NameId 366 (ModuleNameHash 12729305969224249291)"
        ]["_∘e_"](null)(null)(null)(null)(null)(null)(
          h_13732920155217937999[
          "_NameId 222 (ModuleNameHash 12729305969224249291)"
          ]["inv-equiv"](null)(null)(null)(null)(
            h_3983882577351044911[
            "_NameId 38 (ModuleNameHash 16845966502362288139)"
            ]["equiv-funext"](null)(null)(null)(null)(null)(null)
        ) )(
          h_11039019999760051401[
          "_NameId 6 (ModuleNameHash 6956139225801197267)"
          ]["equiv-Π"](null)(null)(null)(null)(null)(null)(null)(null)(
            h_10823327230712899574["Σ"]["pr2"](
              h_2418303217177004088["center"](null)(null)(
                exports["unique-truncated-fam-trunc"](a)(b)(d)(null)(f)
            ) )(j)
          )(
              k => h_16838802912213570003[
            "_NameId 68 (ModuleNameHash 14912215433483829617)"
            ]["equiv-concat'"](null)(null)(null)(null)(null)(null)
  ) ) ) ) )(
    exports[
    "_NameId 124 (ModuleNameHash 7980212233017128774)"
    ]["unique-dependent-function-trunc"](a)(
      h_5150322816240164337["𝕋"]["succ-𝕋"](d)
    )(null)(null)(
        i => h_18376098553934461998["truncated-type-succ-Truncated-Type"](d)(null)(
        h_16941223491982578228["Π-Truncated-Type"](d)(null)(null)(null)(
            j => g(h_10823327230712899574["pair"](i)(j))
    ) ) )(
        i => h_11039019999760051401[
      "_NameId 6 (ModuleNameHash 6956139225801197267)"
      ]["map-equiv-Π"](null)(null)(null)(null)(null)(null)(null)(null)(
        exports[
        "_NameId 250 (ModuleNameHash 7980212233017128774)"
        ]["compute-truncated-fam-trunc"](a)(b)(d)(null)(f)(i)
      )(
          j => h_13732920155217937999[
        "_NameId 108 (ModuleNameHash 12729305969224249291)"
        ]["id-equiv"](null)(null)
      )(h(i))
  ) );
exports[
"_NameId 280 (ModuleNameHash 7980212233017128774)"
][
"function-dependent-universal-property-total-truncated-fam-trunc"
] = a => b => c => d => e => f => g => h => h_10823327230712899574["Σ"]["pr1"](
    h_2418303217177004088["center"](null)(null)(
      exports[
      "_NameId 280 (ModuleNameHash 7980212233017128774)"
      ][
      "dependent-universal-property-total-truncated-fam-trunc"
      ](a)(b)(null)(d)(null)(f)(g)(h)
  ) );
exports[
"_NameId 358 (ModuleNameHash 7980212233017128774)"
] = {};
exports[
"_NameId 358 (ModuleNameHash 7980212233017128774)"
]["map-inv-unit-trunc"] = a => b => c => exports[
  "_NameId 82 (ModuleNameHash 7980212233017128774)"
  ]["map-universal-property-trunc"](a)(a)(b)(null)(c)(d => d);
exports[
"_NameId 358 (ModuleNameHash 7980212233017128774)"
]["is-equiv-unit-trunc"] = a => b => c => h_13732920155217937999[
  "_NameId 120 (ModuleNameHash 12729305969224249291)"
  ]["is-equiv-is-invertible"](null)(null)(null)(null)(null)(
    exports[
    "_NameId 358 (ModuleNameHash 7980212233017128774)"
    ]["map-inv-unit-trunc"](a)(b)(c)
  )(null)(null);
exports[
"_NameId 358 (ModuleNameHash 7980212233017128774)"
]["equiv-unit-trunc"] = a => b => c => h_10823327230712899574["pair"](exports["unit-trunc"](a)(b)(null))(
    exports[
    "_NameId 358 (ModuleNameHash 7980212233017128774)"
    ]["is-equiv-unit-trunc"](a)(b)(c)
  );
exports[
"_NameId 358 (ModuleNameHash 7980212233017128774)"
]["is-equiv-map-inv-unit-trunc"] = a => b => c => h_13732920155217937999[
  "_NameId 120 (ModuleNameHash 12729305969224249291)"
  ]["is-equiv-is-invertible"](null)(null)(null)(null)(null)(exports["unit-trunc"](a)(b)(null))(null)(null);
exports[
"_NameId 358 (ModuleNameHash 7980212233017128774)"
]["inv-equiv-unit-trunc"] = a => b => c => h_10823327230712899574["pair"](
    exports[
    "_NameId 358 (ModuleNameHash 7980212233017128774)"
    ]["map-inv-unit-trunc"](a)(b)(c)
  )(
    exports[
    "_NameId 358 (ModuleNameHash 7980212233017128774)"
    ]["is-equiv-map-inv-unit-trunc"](a)(b)(null)
  );
exports["retract-Truncated-Type-UU"] = a => b => h_10823327230712899574["pair"](
      c => h_10823327230712899574["Σ"]["pr1"](c)
  )(
    h_10823327230712899574["pair"](exports["trunc"](a)(b))(null)
  );
exports[
"_NameId 406 (ModuleNameHash 7980212233017128774)"
] = {};
exports[
"_NameId 406 (ModuleNameHash 7980212233017128774)"
]["is-equiv-unit-trunc-is-contr"] = a => b => c => d => exports[
  "_NameId 358 (ModuleNameHash 7980212233017128774)"
  ]["is-equiv-unit-trunc"](a)(b)(
    h_10823327230712899574["pair"](c)(
      h_13987581571296672568[
      "_NameId 6 (ModuleNameHash 4249083456210693710)"
      ]["is-trunc-is-contr"](a)(null)(b)(d)
  ) );
exports[
"_NameId 406 (ModuleNameHash 7980212233017128774)"
]["is-contr-type-trunc"] = a => b => c => d => h_13070193349384219227[
  "_NameId 32 (ModuleNameHash 7521924699594338453)"
  ]["is-contr-is-equiv'"](null)(null)(null)(null)(exports["unit-trunc"](a)(b)(null))(
    exports[
    "_NameId 406 (ModuleNameHash 7980212233017128774)"
    ]["is-equiv-unit-trunc-is-contr"](a)(b)(null)(d)
  )(d);
exports[
"_NameId 424 (ModuleNameHash 7980212233017128774)"
] = {};
exports[
"_NameId 424 (ModuleNameHash 7980212233017128774)"
]["idempotent-trunc"] = a => b => c => h_13732920155217937999[
  "_NameId 222 (ModuleNameHash 12729305969224249291)"
  ]["inv-equiv"](null)(null)(null)(null)(
    exports[
    "_NameId 358 (ModuleNameHash 7980212233017128774)"
    ]["equiv-unit-trunc"](a)(b)(exports["trunc"](a)(b)(null))
  );
exports[
"_NameId 436 (ModuleNameHash 7980212233017128774)"
] = {};
exports[
"_NameId 436 (ModuleNameHash 7980212233017128774)"
]["Eq-trunc-Truncated-Type"] = a => b => c => d => exports[
  "_NameId 250 (ModuleNameHash 7980212233017128774)"
  ]["truncated-fam-trunc"](a)(a)(b)(null)(e => exports["trunc"](a)(b)(null));
exports[
"_NameId 436 (ModuleNameHash 7980212233017128774)"
]["compute-Eq-trunc"] = a => b => c => d => exports[
  "_NameId 250 (ModuleNameHash 7980212233017128774)"
  ]["compute-truncated-fam-trunc"](a)(a)(b)(null)(e => exports["trunc"](a)(b)(null));
exports[
"_NameId 436 (ModuleNameHash 7980212233017128774)"
]["map-compute-Eq-trunc"] = a => b => c => d => e => h_10823327230712899574["Σ"]["pr1"](
    exports[
    "_NameId 436 (ModuleNameHash 7980212233017128774)"
    ]["compute-Eq-trunc"](a)(b)(null)(null)(e)
  );
exports[
"_NameId 436 (ModuleNameHash 7980212233017128774)"
]["refl-Eq-trunc"] = a => b => c => d => exports[
  "_NameId 436 (ModuleNameHash 7980212233017128774)"
  ]["map-compute-Eq-trunc"](a)(b)(null)(null)(d)(
    exports["unit-trunc"](a)(b)(null)(null)
  );
exports[
"_NameId 436 (ModuleNameHash 7980212233017128774)"
]["is-torsorial-Eq-trunc"] = a => b => c => d => h_10823327230712899574["pair"](
    h_10823327230712899574["pair"](
      exports["unit-trunc"](a)(
        h_5150322816240164337["𝕋"]["succ-𝕋"](b)
      )(null)(d)
    )(
      exports[
      "_NameId 436 (ModuleNameHash 7980212233017128774)"
      ]["refl-Eq-trunc"](a)(b)(null)(d)
  ) )(
    exports[
    "_NameId 280 (ModuleNameHash 7980212233017128774)"
    ][
    "function-dependent-universal-property-total-truncated-fam-trunc"
    ](a)(a)(null)(b)(null)(e => exports["trunc"](a)(b)(null))(
      h_18376098553934461998["Id-Truncated-Type"](null)(null)(
        h_18376098553934461998["Σ-Truncated-Type"](null)(null)(
          h_5150322816240164337["𝕋"]["succ-𝕋"](b)
        )(
          exports["trunc"](a)(
            h_5150322816240164337["𝕋"]["succ-𝕋"](b)
          )(null)
        )(
            e => h_18376098553934461998["truncated-type-succ-Truncated-Type"](b)(a)(
            exports[
            "_NameId 436 (ModuleNameHash 7980212233017128774)"
            ]["Eq-trunc-Truncated-Type"](a)(b)(null)(null)(e)
      ) ) )(
        h_10823327230712899574["pair"](
          exports["unit-trunc"](a)(
            h_5150322816240164337["𝕋"]["succ-𝕋"](b)
          )(null)(d)
        )(
          exports[
          "_NameId 436 (ModuleNameHash 7980212233017128774)"
          ]["refl-Eq-trunc"](a)(b)(null)(d)
    ) ) )(
        e => exports[
      "_NameId 124 (ModuleNameHash 7980212233017128774)"
      ][
      "function-dependent-universal-property-trunc"
      ](a)(b)(null)(null)(
          f => h_18376098553934461998["Id-Truncated-Type"](null)(null)(
          h_18376098553934461998["Σ-Truncated-Type"](null)(null)(
            h_5150322816240164337["𝕋"]["succ-𝕋"](b)
          )(
            exports["trunc"](a)(
              h_5150322816240164337["𝕋"]["succ-𝕋"](b)
            )(null)
          )(
              g => h_18376098553934461998["truncated-type-succ-Truncated-Type"](b)(a)(
              exports[
              "_NameId 436 (ModuleNameHash 7980212233017128774)"
              ]["Eq-trunc-Truncated-Type"](a)(b)(null)(null)(g)
        ) ) )(
          h_10823327230712899574["pair"](
            exports["unit-trunc"](a)(
              h_5150322816240164337["𝕋"]["succ-𝕋"](b)
            )(null)(d)
          )(
            exports[
            "_NameId 436 (ModuleNameHash 7980212233017128774)"
            ]["refl-Eq-trunc"](a)(b)(null)(d)
        ) )(
          h_10823327230712899574["pair"](
            exports["unit-trunc"](a)(
              h_5150322816240164337["𝕋"]["succ-𝕋"](b)
            )(null)(e)
          )(
            exports[
            "_NameId 436 (ModuleNameHash 7980212233017128774)"
            ]["map-compute-Eq-trunc"](a)(b)(null)(null)(e)(f)
      ) ) )(null)
  ) );
exports[
"_NameId 436 (ModuleNameHash 7980212233017128774)"
]["Eq-eq-trunc"] = a => b => c => d => e => f => exports[
  "_NameId 436 (ModuleNameHash 7980212233017128774)"
  ]["refl-Eq-trunc"](a)(b)(null)(d);
exports[
"_NameId 436 (ModuleNameHash 7980212233017128774)"
]["is-equiv-Eq-eq-trunc"] = a => b => c => d => h_16806042658982196604[
  "_NameId 6 (ModuleNameHash 10294464974525777717)"
  ]["fundamental-theorem-id"](null)(null)(null)(null)(
    exports["unit-trunc"](a)(
      h_5150322816240164337["𝕋"]["succ-𝕋"](b)
    )(null)(d)
  )(null)(null);
exports[
"_NameId 436 (ModuleNameHash 7980212233017128774)"
]["extensionality-trunc"] = a => b => c => d => e => h_10823327230712899574["pair"](
    exports[
    "_NameId 436 (ModuleNameHash 7980212233017128774)"
    ]["Eq-eq-trunc"](a)(b)(null)(d)(null)
  )(
    exports[
    "_NameId 436 (ModuleNameHash 7980212233017128774)"
    ]["is-equiv-Eq-eq-trunc"](a)(b)(null)(d)(e)
  );
exports[
"_NameId 436 (ModuleNameHash 7980212233017128774)"
]["effectiveness-trunc"] = a => b => c => d => e => h_13732920155217937999[
  "_NameId 366 (ModuleNameHash 12729305969224249291)"
  ]["_∘e_"](null)(null)(null)(null)(null)(null)(
    h_13732920155217937999[
    "_NameId 222 (ModuleNameHash 12729305969224249291)"
    ]["inv-equiv"](null)(null)(null)(null)(
      exports[
      "_NameId 436 (ModuleNameHash 7980212233017128774)"
      ]["extensionality-trunc"](a)(b)(null)(d)(
        exports["unit-trunc"](a)(
          h_5150322816240164337["𝕋"]["succ-𝕋"](b)
        )(null)(e)
  ) ) )(
    exports[
    "_NameId 436 (ModuleNameHash 7980212233017128774)"
    ]["compute-Eq-trunc"](a)(b)(null)(null)(e)
  );
exports[
"_NameId 524 (ModuleNameHash 7980212233017128774)"
] = {};
exports[
"_NameId 524 (ModuleNameHash 7980212233017128774)"
]["map-trunc-Σ"] = a => b => c => d => e => exports[
  "_NameId 82 (ModuleNameHash 7980212233017128774)"
  ]["map-universal-property-trunc"](null)(null)(c)(null)(exports["trunc"](null)(c)(null))(
      f => exports["unit-trunc"](null)(c)(null)(
      h_10823327230712899574["pair"](h_10823327230712899574["Σ"]["pr1"](f))(
        exports["unit-trunc"](b)(c)(null)(h_10823327230712899574["Σ"]["pr2"](f))
  ) ) );
exports[
"_NameId 524 (ModuleNameHash 7980212233017128774)"
]["map-inv-trunc-Σ"] = a => b => c => d => e => exports[
  "_NameId 82 (ModuleNameHash 7980212233017128774)"
  ]["map-universal-property-trunc"](null)(null)(c)(null)(exports["trunc"](null)(c)(null))(
      f => exports[
    "_NameId 82 (ModuleNameHash 7980212233017128774)"
    ]["map-universal-property-trunc"](b)(null)(c)(null)(exports["trunc"](null)(c)(null))(
        g => exports["unit-trunc"](null)(c)(null)(
        h_10823327230712899574["pair"](h_10823327230712899574["Σ"]["pr1"](f))(g)
    ) )(h_10823327230712899574["Σ"]["pr2"](f))
  );
exports[
"_NameId 524 (ModuleNameHash 7980212233017128774)"
]["equiv-trunc-Σ"] = a => b => c => d => e => h_10823327230712899574["pair"](
    exports[
    "_NameId 524 (ModuleNameHash 7980212233017128774)"
    ]["map-trunc-Σ"](null)(b)(c)(null)(null)
  )(
    h_13732920155217937999[
    "_NameId 120 (ModuleNameHash 12729305969224249291)"
    ]["is-equiv-is-invertible"](null)(null)(null)(null)(null)(
      exports[
      "_NameId 524 (ModuleNameHash 7980212233017128774)"
      ]["map-inv-trunc-Σ"](null)(b)(c)(null)(null)
    )(null)(null)
  );
exports[
"_NameId 524 (ModuleNameHash 7980212233017128774)"
]["inv-equiv-trunc-Σ"] = a => b => c => d => e => h_10823327230712899574["pair"](
    exports[
    "_NameId 524 (ModuleNameHash 7980212233017128774)"
    ]["map-inv-trunc-Σ"](null)(b)(c)(null)(null)
  )(
    h_13732920155217937999[
    "_NameId 120 (ModuleNameHash 12729305969224249291)"
    ]["is-equiv-is-invertible"](null)(null)(null)(null)(null)(
      exports[
      "_NameId 524 (ModuleNameHash 7980212233017128774)"
      ]["map-trunc-Σ"](null)(b)(c)(null)(null)
    )(null)(null)
  );
exports["type-trunc"] = undefined;
exports["is-trunc-type-trunc"] = undefined;
exports["unit-trunc"] = undefined;
exports["is-truncation-trunc"] = undefined;
