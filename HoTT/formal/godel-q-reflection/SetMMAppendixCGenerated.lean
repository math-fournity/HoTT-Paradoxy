/-
  MACHINE_MANAGED_CANONICAL
  generator: scripts/audit/generate_setmm_appendix_c_vocabulary.py
  schema: setmm-appendix-c-vocabulary/v1
  source_sha256: d8420798bcedcd04fcfe337736e2609b66914c76f8f2db967fa79673d5026b2a
  This file encodes only the pinned raw database vocabulary and $f
  assignments. It is not an internal mFS witness, a proof relation, or
  an adequacy theorem for set.mm.
-/

namespace SetMMAppendixCGenerated

inductive RawType where
  | wff
  | setvar
  | class
deriving DecidableEq, Repr

inductive RawVar where
  | v000
  | v001
  | v002
  | v003
  | v004
  | v005
  | v006
  | v007
  | v008
  | v009
  | v010
  | v011
  | v012
  | v013
  | v014
  | v015
  | v016
  | v017
  | v018
  | v019
  | v020
  | v021
  | v022
  | v023
  | v024
  | v025
  | v026
  | v027
  | v028
  | v029
  | v030
  | v031
  | v032
  | v033
  | v034
  | v035
  | v036
  | v037
  | v038
  | v039
  | v040
  | v041
  | v042
  | v043
  | v044
  | v045
  | v046
  | v047
  | v048
  | v049
  | v050
  | v051
  | v052
  | v053
  | v054
  | v055
  | v056
  | v057
  | v058
  | v059
  | v060
  | v061
  | v062
  | v063
  | v064
  | v065
  | v066
  | v067
  | v068
  | v069
  | v070
  | v071
  | v072
  | v073
  | v074
  | v075
  | v076
  | v077
  | v078
  | v079
  | v080
  | v081
  | v082
  | v083
  | v084
  | v085
  | v086
  | v087
  | v088
  | v089
  | v090
  | v091
  | v092
  | v093
  | v094
  | v095
  | v096
  | v097
  | v098
  | v099
  | v100
  | v101
  | v102
  | v103
  | v104
  | v105
  | v106
  | v107
  | v108
  | v109
  | v110
  | v111
  | v112
  | v113
  | v114
  | v115
  | v116
  | v117
  | v118
  | v119
  | v120
  | v121
  | v122
  | v123
  | v124
  | v125
  | v126
  | v127
  | v128
  | v129
  | v130
  | v131
  | v132
  | v133
  | v134
  | v135
  | v136
  | v137
  | v138
  | v139
  | v140
  | v141
  | v142
  | v143
  | v144
  | v145
  | v146
  | v147
  | v148
  | v149
  | v150
  | v151
  | v152
  | v153
  | v154
  | v155
  | v156
  | v157
  | v158
  | v159
  | v160
  | v161
  | v162
  | v163
  | v164
  | v165
  | v166
  | v167
  | v168
  | v169
  | v170
  | v171
  | v172
  | v173
  | v174
  | v175
  | v176
  | v177
  | v178
  | v179
  | v180
  | v181
  | v182
  | v183
  | v184
  | v185
  | v186
  | v187
  | v188
  | v189
  | v190
  | v191
  | v192
  | v193
  | v194
  | v195
  | v196
  | v197
  | v198
  | v199
  | v200
  | v201
  | v202
  | v203
  | v204
  | v205
  | v206
  | v207
  | v208
  | v209
  | v210
  | v211
  | v212
  | v213
  | v214
  | v215
  | v216
  | v217
  | v218
  | v219
  | v220
  | v221
  | v222
  | v223
  | v224
  | v225
  | v226
  | v227
  | v228
  | v229
  | v230
  | v231
  | v232
  | v233
  | v234
  | v235
  | v236
  | v237
  | v238
  | v239
  | v240
  | v241
  | v242
  | v243
  | v244
  | v245
  | v246
  | v247
  | v248
  | v249
  | v250
  | v251
  | v252
  | v253
  | v254
  | v255
  | v256
  | v257
  | v258
  | v259
  | v260
  | v261
  | v262
  | v263
  | v264
  | v265
  | v266
  | v267
  | v268
  | v269
  | v270
  | v271
  | v272
  | v273
  | v274
  | v275
  | v276
  | v277
  | v278
  | v279
  | v280
  | v281
  | v282
  | v283
  | v284
  | v285
  | v286
  | v287
  | v288
  | v289
  | v290
  | v291
  | v292
  | v293
  | v294
  | v295
  | v296
  | v297
  | v298
  | v299
  | v300
  | v301
  | v302
  | v303
  | v304
  | v305
  | v306
  | v307
  | v308
  | v309
  | v310
  | v311
  | v312
  | v313
  | v314
  | v315
  | v316
  | v317
  | v318
  | v319
  | v320
  | v321
  | v322
  | v323
  | v324
  | v325
  | v326
  | v327
  | v328
  | v329
  | v330
  | v331
  | v332
  | v333
  | v334
  | v335
  | v336
  | v337
  | v338
  | v339
  | v340
  | v341
  | v342
  | v343
  | v344
  | v345
  | v346
  | v347
  | v348
  | v349
  | v350
  | v351
  | v352
  | v353
  | v354
deriving DecidableEq, Repr

def sourceSha256 : String := "d8420798bcedcd04fcfe337736e2609b66914c76f8f2db967fa79673d5026b2a"
def sourceVariableCount : Nat := 355

def rawVarType : RawVar → RawType
  | .v000 => .wff
  | .v001 => .wff
  | .v002 => .wff
  | .v003 => .wff
  | .v004 => .wff
  | .v005 => .wff
  | .v006 => .wff
  | .v007 => .wff
  | .v008 => .wff
  | .v009 => .wff
  | .v010 => .wff
  | .v011 => .wff
  | .v012 => .setvar
  | .v013 => .class
  | .v014 => .class
  | .v015 => .setvar
  | .v016 => .setvar
  | .v017 => .setvar
  | .v018 => .setvar
  | .v019 => .setvar
  | .v020 => .setvar
  | .v021 => .setvar
  | .v022 => .setvar
  | .v023 => .setvar
  | .v024 => .class
  | .v025 => .class
  | .v026 => .class
  | .v027 => .class
  | .v028 => .class
  | .v029 => .class
  | .v030 => .class
  | .v031 => .class
  | .v032 => .class
  | .v033 => .class
  | .v034 => .class
  | .v035 => .class
  | .v036 => .class
  | .v037 => .class
  | .v038 => .class
  | .v039 => .class
  | .v040 => .class
  | .v041 => .class
  | .v042 => .class
  | .v043 => .class
  | .v044 => .class
  | .v045 => .class
  | .v046 => .class
  | .v047 => .class
  | .v048 => .class
  | .v049 => .class
  | .v050 => .class
  | .v051 => .class
  | .v052 => .class
  | .v053 => .class
  | .v054 => .class
  | .v055 => .class
  | .v056 => .setvar
  | .v057 => .setvar
  | .v058 => .setvar
  | .v059 => .setvar
  | .v060 => .setvar
  | .v061 => .setvar
  | .v062 => .setvar
  | .v063 => .setvar
  | .v064 => .class
  | .v065 => .class
  | .v066 => .class
  | .v067 => .class
  | .v068 => .class
  | .v069 => .class
  | .v070 => .class
  | .v071 => .class
  | .v072 => .class
  | .v073 => .class
  | .v074 => .class
  | .v075 => .class
  | .v076 => .class
  | .v077 => .class
  | .v078 => .class
  | .v079 => .class
  | .v080 => .setvar
  | .v081 => .setvar
  | .v082 => .setvar
  | .v083 => .setvar
  | .v084 => .setvar
  | .v085 => .setvar
  | .v086 => .setvar
  | .v087 => .setvar
  | .v088 => .setvar
  | .v089 => .setvar
  | .v090 => .setvar
  | .v091 => .setvar
  | .v092 => .setvar
  | .v093 => .setvar
  | .v094 => .setvar
  | .v095 => .setvar
  | .v096 => .setvar
  | .v097 => .wff
  | .v098 => .class
  | .v099 => .wff
  | .v100 => .wff
  | .v101 => .wff
  | .v102 => .wff
  | .v103 => .wff
  | .v104 => .wff
  | .v105 => .wff
  | .v106 => .wff
  | .v107 => .wff
  | .v108 => .wff
  | .v109 => .wff
  | .v110 => .wff
  | .v111 => .wff
  | .v112 => .wff
  | .v113 => .wff
  | .v114 => .wff
  | .v115 => .wff
  | .v116 => .wff
  | .v117 => .wff
  | .v118 => .wff
  | .v119 => .wff
  | .v120 => .wff
  | .v121 => .wff
  | .v122 => .wff
  | .v123 => .wff
  | .v124 => .wff
  | .v125 => .wff
  | .v126 => .wff
  | .v127 => .wff
  | .v128 => .wff
  | .v129 => .wff
  | .v130 => .wff
  | .v131 => .wff
  | .v132 => .wff
  | .v133 => .wff
  | .v134 => .wff
  | .v135 => .setvar
  | .v136 => .setvar
  | .v137 => .setvar
  | .v138 => .setvar
  | .v139 => .setvar
  | .v140 => .setvar
  | .v141 => .setvar
  | .v142 => .setvar
  | .v143 => .setvar
  | .v144 => .setvar
  | .v145 => .setvar
  | .v146 => .setvar
  | .v147 => .setvar
  | .v148 => .setvar
  | .v149 => .setvar
  | .v150 => .setvar
  | .v151 => .setvar
  | .v152 => .setvar
  | .v153 => .setvar
  | .v154 => .setvar
  | .v155 => .setvar
  | .v156 => .setvar
  | .v157 => .setvar
  | .v158 => .setvar
  | .v159 => .setvar
  | .v160 => .setvar
  | .v161 => .setvar
  | .v162 => .setvar
  | .v163 => .setvar
  | .v164 => .setvar
  | .v165 => .setvar
  | .v166 => .setvar
  | .v167 => .setvar
  | .v168 => .setvar
  | .v169 => .setvar
  | .v170 => .setvar
  | .v171 => .setvar
  | .v172 => .setvar
  | .v173 => .setvar
  | .v174 => .setvar
  | .v175 => .setvar
  | .v176 => .setvar
  | .v177 => .setvar
  | .v178 => .setvar
  | .v179 => .setvar
  | .v180 => .setvar
  | .v181 => .setvar
  | .v182 => .setvar
  | .v183 => .setvar
  | .v184 => .setvar
  | .v185 => .setvar
  | .v186 => .setvar
  | .v187 => .setvar
  | .v188 => .setvar
  | .v189 => .setvar
  | .v190 => .setvar
  | .v191 => .setvar
  | .v192 => .setvar
  | .v193 => .setvar
  | .v194 => .setvar
  | .v195 => .setvar
  | .v196 => .setvar
  | .v197 => .setvar
  | .v198 => .setvar
  | .v199 => .setvar
  | .v200 => .setvar
  | .v201 => .setvar
  | .v202 => .setvar
  | .v203 => .setvar
  | .v204 => .setvar
  | .v205 => .setvar
  | .v206 => .setvar
  | .v207 => .setvar
  | .v208 => .setvar
  | .v209 => .setvar
  | .v210 => .setvar
  | .v211 => .setvar
  | .v212 => .setvar
  | .v213 => .setvar
  | .v214 => .setvar
  | .v215 => .setvar
  | .v216 => .setvar
  | .v217 => .setvar
  | .v218 => .setvar
  | .v219 => .setvar
  | .v220 => .setvar
  | .v221 => .setvar
  | .v222 => .setvar
  | .v223 => .setvar
  | .v224 => .setvar
  | .v225 => .setvar
  | .v226 => .setvar
  | .v227 => .setvar
  | .v228 => .setvar
  | .v229 => .setvar
  | .v230 => .setvar
  | .v231 => .setvar
  | .v232 => .setvar
  | .v233 => .setvar
  | .v234 => .setvar
  | .v235 => .setvar
  | .v236 => .setvar
  | .v237 => .setvar
  | .v238 => .setvar
  | .v239 => .class
  | .v240 => .class
  | .v241 => .class
  | .v242 => .class
  | .v243 => .class
  | .v244 => .class
  | .v245 => .class
  | .v246 => .class
  | .v247 => .class
  | .v248 => .class
  | .v249 => .class
  | .v250 => .class
  | .v251 => .class
  | .v252 => .class
  | .v253 => .class
  | .v254 => .class
  | .v255 => .class
  | .v256 => .class
  | .v257 => .class
  | .v258 => .class
  | .v259 => .class
  | .v260 => .class
  | .v261 => .class
  | .v262 => .class
  | .v263 => .class
  | .v264 => .class
  | .v265 => .class
  | .v266 => .class
  | .v267 => .class
  | .v268 => .class
  | .v269 => .class
  | .v270 => .class
  | .v271 => .class
  | .v272 => .class
  | .v273 => .class
  | .v274 => .class
  | .v275 => .class
  | .v276 => .class
  | .v277 => .class
  | .v278 => .class
  | .v279 => .class
  | .v280 => .class
  | .v281 => .class
  | .v282 => .class
  | .v283 => .class
  | .v284 => .class
  | .v285 => .class
  | .v286 => .class
  | .v287 => .class
  | .v288 => .class
  | .v289 => .class
  | .v290 => .class
  | .v291 => .class
  | .v292 => .class
  | .v293 => .class
  | .v294 => .class
  | .v295 => .class
  | .v296 => .class
  | .v297 => .class
  | .v298 => .class
  | .v299 => .class
  | .v300 => .class
  | .v301 => .class
  | .v302 => .class
  | .v303 => .class
  | .v304 => .class
  | .v305 => .class
  | .v306 => .class
  | .v307 => .class
  | .v308 => .class
  | .v309 => .class
  | .v310 => .class
  | .v311 => .class
  | .v312 => .class
  | .v313 => .class
  | .v314 => .class
  | .v315 => .class
  | .v316 => .class
  | .v317 => .class
  | .v318 => .class
  | .v319 => .class
  | .v320 => .class
  | .v321 => .class
  | .v322 => .class
  | .v323 => .class
  | .v324 => .class
  | .v325 => .class
  | .v326 => .class
  | .v327 => .class
  | .v328 => .class
  | .v329 => .class
  | .v330 => .class
  | .v331 => .class
  | .v332 => .class
  | .v333 => .class
  | .v334 => .class
  | .v335 => .class
  | .v336 => .class
  | .v337 => .class
  | .v338 => .class
  | .v339 => .class
  | .v340 => .class
  | .v341 => .class
  | .v342 => .class
  | .v343 => .wff
  | .v344 => .wff
  | .v345 => .wff
  | .v346 => .wff
  | .v347 => .wff
  | .v348 => .wff
  | .v349 => .wff
  | .v350 => .wff
  | .v351 => .wff
  | .v352 => .wff
  | .v353 => .wff
  | .v354 => .wff

def rawVarLexeme : RawVar → String
  | .v000 => "ph"
  | .v001 => "ps"
  | .v002 => "ch"
  | .v003 => "th"
  | .v004 => "ta"
  | .v005 => "et"
  | .v006 => "ze"
  | .v007 => "si"
  | .v008 => "rh"
  | .v009 => "mu"
  | .v010 => "la"
  | .v011 => "ka"
  | .v012 => "x"
  | .v013 => "A"
  | .v014 => "B"
  | .v015 => "y"
  | .v016 => "z"
  | .v017 => "w"
  | .v018 => "v"
  | .v019 => "u"
  | .v020 => "t"
  | .v021 => "f"
  | .v022 => "g"
  | .v023 => "s"
  | .v024 => "./\\"
  | .v025 => ".\\/"
  | .v026 => ".<_"
  | .v027 => ".<"
  | .v028 => ".+"
  | .v029 => ".-"
  | .v030 => ".X."
  | .v031 => "./"
  | .v032 => ".^"
  | .v033 => ".0."
  | .v034 => ".1."
  | .v035 => ".||"
  | .v036 => ".~"
  | .v037 => "._|_"
  | .v038 => ".+^"
  | .v039 => ".+b"
  | .v040 => ".(+)"
  | .v041 => ".*"
  | .v042 => ".x."
  | .v043 => ".xb"
  | .v044 => ".,"
  | .v045 => ".(x)"
  | .v046 => ".o."
  | .v047 => ".0b"
  | .v048 => "C"
  | .v049 => "D"
  | .v050 => "P"
  | .v051 => "Q"
  | .v052 => "R"
  | .v053 => "S"
  | .v054 => "T"
  | .v055 => "U"
  | .v056 => "e"
  | .v057 => "h"
  | .v058 => "i"
  | .v059 => "j"
  | .v060 => "k"
  | .v061 => "m"
  | .v062 => "n"
  | .v063 => "o"
  | .v064 => "E"
  | .v065 => "F"
  | .v066 => "G"
  | .v067 => "H"
  | .v068 => "I"
  | .v069 => "J"
  | .v070 => "K"
  | .v071 => "L"
  | .v072 => "M"
  | .v073 => "N"
  | .v074 => "V"
  | .v075 => "W"
  | .v076 => "X"
  | .v077 => "Y"
  | .v078 => "Z"
  | .v079 => "O"
  | .v080 => "r"
  | .v081 => "q"
  | .v082 => "p"
  | .v083 => "a"
  | .v084 => "b"
  | .v085 => "c"
  | .v086 => "d"
  | .v087 => "l"
  | .v088 => "xO"
  | .v089 => "xL"
  | .v090 => "xR"
  | .v091 => "yO"
  | .v092 => "yL"
  | .v093 => "yR"
  | .v094 => "zO"
  | .v095 => "zL"
  | .v096 => "zR"
  | .v097 => "nu"
  | .v098 => ".c_"
  | .v099 => "ph'"
  | .v100 => "ps'"
  | .v101 => "ch'"
  | .v102 => "th'"
  | .v103 => "ta'"
  | .v104 => "et'"
  | .v105 => "ze'"
  | .v106 => "si'"
  | .v107 => "rh'"
  | .v108 => "ph\""
  | .v109 => "ps\""
  | .v110 => "ch\""
  | .v111 => "th\""
  | .v112 => "ta\""
  | .v113 => "et\""
  | .v114 => "ze\""
  | .v115 => "si\""
  | .v116 => "rh\""
  | .v117 => "ph0"
  | .v118 => "ps0"
  | .v119 => "ch0_"
  | .v120 => "th0"
  | .v121 => "ta0"
  | .v122 => "et0"
  | .v123 => "ze0"
  | .v124 => "si0"
  | .v125 => "rh0"
  | .v126 => "ph1"
  | .v127 => "ps1"
  | .v128 => "ch1"
  | .v129 => "th1"
  | .v130 => "ta1"
  | .v131 => "et1"
  | .v132 => "ze1"
  | .v133 => "si1"
  | .v134 => "rh1"
  | .v135 => "a'"
  | .v136 => "b'"
  | .v137 => "c'"
  | .v138 => "d'"
  | .v139 => "e'"
  | .v140 => "f'"
  | .v141 => "g'"
  | .v142 => "h'"
  | .v143 => "i'"
  | .v144 => "j'"
  | .v145 => "k'"
  | .v146 => "l'"
  | .v147 => "m'"
  | .v148 => "n'"
  | .v149 => "o'_"
  | .v150 => "p'"
  | .v151 => "q'"
  | .v152 => "r'"
  | .v153 => "s'_"
  | .v154 => "t'"
  | .v155 => "u'"
  | .v156 => "v'_"
  | .v157 => "w'"
  | .v158 => "x'"
  | .v159 => "y'"
  | .v160 => "z'"
  | .v161 => "a\""
  | .v162 => "b\""
  | .v163 => "c\""
  | .v164 => "d\""
  | .v165 => "e\""
  | .v166 => "f\""
  | .v167 => "g\""
  | .v168 => "h\""
  | .v169 => "i\""
  | .v170 => "j\""
  | .v171 => "k\""
  | .v172 => "l\""
  | .v173 => "m\""
  | .v174 => "n\""
  | .v175 => "o\"_"
  | .v176 => "p\""
  | .v177 => "q\""
  | .v178 => "r\""
  | .v179 => "s\"_"
  | .v180 => "t\""
  | .v181 => "u\""
  | .v182 => "v\"_"
  | .v183 => "w\""
  | .v184 => "x\""
  | .v185 => "y\""
  | .v186 => "z\""
  | .v187 => "a0_"
  | .v188 => "b0_"
  | .v189 => "c0_"
  | .v190 => "d0"
  | .v191 => "e0"
  | .v192 => "f0_"
  | .v193 => "g0"
  | .v194 => "h0"
  | .v195 => "i0"
  | .v196 => "j0"
  | .v197 => "k0"
  | .v198 => "l0"
  | .v199 => "m0"
  | .v200 => "n0_"
  | .v201 => "o0_"
  | .v202 => "p0"
  | .v203 => "q0"
  | .v204 => "r0"
  | .v205 => "s0"
  | .v206 => "t0"
  | .v207 => "u0"
  | .v208 => "v0"
  | .v209 => "w0"
  | .v210 => "x0"
  | .v211 => "y0"
  | .v212 => "z0"
  | .v213 => "a1_"
  | .v214 => "b1_"
  | .v215 => "c1_"
  | .v216 => "d1"
  | .v217 => "e1"
  | .v218 => "f1"
  | .v219 => "g1"
  | .v220 => "h1"
  | .v221 => "i1"
  | .v222 => "j1"
  | .v223 => "k1"
  | .v224 => "l1"
  | .v225 => "m1"
  | .v226 => "n1"
  | .v227 => "o1_"
  | .v228 => "p1"
  | .v229 => "q1"
  | .v230 => "r1"
  | .v231 => "s1"
  | .v232 => "t1"
  | .v233 => "u1"
  | .v234 => "v1"
  | .v235 => "w1"
  | .v236 => "x1"
  | .v237 => "y1"
  | .v238 => "z1"
  | .v239 => "A'"
  | .v240 => "B'"
  | .v241 => "C'"
  | .v242 => "D'"
  | .v243 => "E'"
  | .v244 => "F'"
  | .v245 => "G'"
  | .v246 => "H'"
  | .v247 => "I'"
  | .v248 => "J'"
  | .v249 => "K'"
  | .v250 => "L'"
  | .v251 => "M'"
  | .v252 => "N'"
  | .v253 => "O'"
  | .v254 => "P'"
  | .v255 => "Q'"
  | .v256 => "R'"
  | .v257 => "S'"
  | .v258 => "T'"
  | .v259 => "U'"
  | .v260 => "V'"
  | .v261 => "W'"
  | .v262 => "X'"
  | .v263 => "Y'"
  | .v264 => "Z'"
  | .v265 => "A\""
  | .v266 => "B\""
  | .v267 => "C\""
  | .v268 => "D\""
  | .v269 => "E\""
  | .v270 => "F\""
  | .v271 => "G\""
  | .v272 => "H\""
  | .v273 => "I\""
  | .v274 => "J\""
  | .v275 => "K\""
  | .v276 => "L\""
  | .v277 => "M\""
  | .v278 => "N\""
  | .v279 => "O\""
  | .v280 => "P\""
  | .v281 => "Q\""
  | .v282 => "R\""
  | .v283 => "S\""
  | .v284 => "T\""
  | .v285 => "U\""
  | .v286 => "V\""
  | .v287 => "W\""
  | .v288 => "X\""
  | .v289 => "Y\""
  | .v290 => "Z\""
  | .v291 => "A0"
  | .v292 => "B0"
  | .v293 => "C0"
  | .v294 => "D0"
  | .v295 => "E0"
  | .v296 => "F0"
  | .v297 => "G0"
  | .v298 => "H0"
  | .v299 => "I0"
  | .v300 => "J0"
  | .v301 => "K0"
  | .v302 => "L0"
  | .v303 => "M0"
  | .v304 => "N0"
  | .v305 => "O0"
  | .v306 => "P0"
  | .v307 => "Q0"
  | .v308 => "R0"
  | .v309 => "S0"
  | .v310 => "T0"
  | .v311 => "U0"
  | .v312 => "V0"
  | .v313 => "W0"
  | .v314 => "X0"
  | .v315 => "Y0"
  | .v316 => "Z0"
  | .v317 => "A1_"
  | .v318 => "B1_"
  | .v319 => "C1_"
  | .v320 => "D1_"
  | .v321 => "E1"
  | .v322 => "F1_"
  | .v323 => "G1_"
  | .v324 => "H1_"
  | .v325 => "I1_"
  | .v326 => "J1"
  | .v327 => "K1"
  | .v328 => "L1_"
  | .v329 => "M1_"
  | .v330 => "N1"
  | .v331 => "O1_"
  | .v332 => "P1"
  | .v333 => "Q1"
  | .v334 => "R1_"
  | .v335 => "S1_"
  | .v336 => "T1"
  | .v337 => "U1"
  | .v338 => "V1_"
  | .v339 => "W1"
  | .v340 => "X1"
  | .v341 => "Y1"
  | .v342 => "Z1"
  | .v343 => "al"
  | .v344 => "jph"
  | .v345 => "jps"
  | .v346 => "jch"
  | .v347 => "jth"
  | .v348 => "jta"
  | .v349 => "jet"
  | .v350 => "jze"
  | .v351 => "jsi"
  | .v352 => "jrh"
  | .v353 => "jmu"
  | .v354 => "jla"

end SetMMAppendixCGenerated
