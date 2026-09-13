var agdaRTS = require("agda-rts");

var z_jAgda_Agda_Builtin_IO = require("jAgda.Agda.Builtin.IO");
var z_jAgda_Agda_Primitive = require("jAgda.Agda.Primitive");
var h_1959573496066403698 = require("jAgda.foundation.decidable-types");
var h_10252439710734579043 = require("jAgda.foundation.unit-type");
var h_13895875897459204243 = require("jAgda.foundation.universe-levels");
var h_11596926212631638473 = require("jAgda.foundation-core.booleans");
var h_2062783598648249311 = require("jAgda.foundation-core.coproduct-types");
var h_5153263140774292640 = require("jAgda.foundation-core.identity-types");

exports["decisionTag"] = a => b => c => c({
    "inl": d => h_11596926212631638473["bool"]["true"],
    "inr": d => h_11596926212631638473["bool"]["false"]
  });
exports["explicitDecision"] = h_2062783598648249311["_+_"]["inr"](null);
exports["printBool"] = function (b) { return function () { console.log(b({ "true": () => "TRUE", "false": () => "FALSE" })); return null; }; };
exports["main"] = exports["printBool"](
    exports["decisionTag"](null)(null)(exports["explicitDecision"])
);
exports["main"](a => ({}))
