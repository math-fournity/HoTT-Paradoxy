var agdaRTS = require("agda-rts");

var z_jAgda_Agda_Primitive = require("jAgda.Agda.Primitive");
var h_14933256709764318676 = require("jAgda.foundation.propositional-truncations");
var h_10252439710734579043 = require("jAgda.foundation.unit-type");
var h_1998016453582150760 = require("jAgda.foundation.universal-property-propositional-truncation-into-sets");
var h_9296533212890123197 = require("jAgda.foundation.weakly-constant-maps");
var h_11596926212631638473 = require("jAgda.foundation-core.booleans");
var h_5153263140774292640 = require("jAgda.foundation-core.identity-types");

exports["toTrue"] = a => h_11596926212631638473["bool"]["true"];
exports["truncatedUnit"] = h_14933256709764318676["unit-trunc-Prop"](null)(null)(null);
exports["truncatedResult"] = h_1998016453582150760[
  "map-universal-property-set-quotient-trunc-Prop"
  ](null)(null)(null)(null)(exports["toTrue"])(null)(exports["truncatedUnit"]);
