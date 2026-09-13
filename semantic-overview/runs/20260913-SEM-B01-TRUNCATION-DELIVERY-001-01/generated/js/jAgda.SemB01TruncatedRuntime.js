var agdaRTS = require("agda-rts");

var z_jAgda_Agda_Builtin_IO = require("jAgda.Agda.Builtin.IO");
var z_jAgda_Agda_Primitive = require("jAgda.Agda.Primitive");
var z_jAgda_SemB01Kernel = require("jAgda.SemB01Kernel");
var h_10252439710734579043 = require("jAgda.foundation.unit-type");
var h_11596926212631638473 = require("jAgda.foundation-core.booleans");

exports["printBool"] = function (b) { return function () { console.log(b ? "TRUE" : "FALSE"); return null; }; };
exports["main"] = exports["printBool"](
    z_jAgda_SemB01Kernel["truncatedResult"]
);
exports["main"](a => ({}))
