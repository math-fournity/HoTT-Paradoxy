var agdaRTS = require("agda-rts");

var z_jAgda_Agda_Primitive = require("jAgda.Agda.Primitive");
var z_jAgda_foundation_booleans = require("jAgda.foundation.booleans");
var h_1959573496066403698 = require("jAgda.foundation.decidable-types");
var h_13895875897459204243 = require("jAgda.foundation.universe-levels");
var h_11596926212631638473 = require("jAgda.foundation-core.booleans");
var h_2062783598648249311 = require("jAgda.foundation-core.coproduct-types");
var h_13003858539280958212 = require("jAgda.foundation-core.empty-types");
var h_5153263140774292640 = require("jAgda.foundation-core.identity-types");
var h_829224385902737810 = require("jAgda.univalent-combinatorics.equality-finite-types");

exports["decisionTag"] = a => b => c => c({
    "inl": d => h_11596926212631638473["bool"]["true"],
    "inr": d => h_11596926212631638473["bool"]["false"]
  });
exports["explicitDecision"] = h_2062783598648249311["_+_"]["inr"](null);
exports["finiteDecision"] = h_829224385902737810["has-decidable-equality-is-finite"](null)(null)(
    z_jAgda_foundation_booleans["is-finite-bool"]
  )(
    h_11596926212631638473["bool"]["true"]
  )(
    h_11596926212631638473["bool"]["false"]
  );
exports["explicitTag"] = exports["decisionTag"](null)(null)(exports["explicitDecision"]);
exports["finiteTag"] = exports["decisionTag"](null)(null)(exports["finiteDecision"]);
