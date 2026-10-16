# C-383–C-386：Fmini 的 formula code 与 self-code substitution shape

> **证明包：** `MP-CUBICAL-GODEL-FORMULA-CODING-001`。

| Claim | Agda declaration | 精确范围 |
|---|---|---|
| C-383 | `decodeExprCode` | `Expr₁` 的 Nat code 在像上可解码。 |
| C-384 | `decodeFormulaCode` / `formulaCodeInjective` | `Formula₁` 的 Nat code roundtrip 且单射。 |
| C-385 | `selfInstanceShape` | 模板 `prov₁(fvar 0)` 代入自己的 code 得到 `prov₁(lit(codeFormula template))`。 |
| C-386 | `selfInstanceQuotesFormula` | 该 self instance 等于显式 formula quotation 的 syntax。 |

这是一种**syntax-level diagonal shape**。它没有 `ProvWitness` 的 arithmetic representability theorem，
不证明 `selfInstance template ↔ ¬Provable(⌜selfInstance template⌝)`，不产生 fixed point 或 incompleteness。
`Fmini` 没有 binder，因此 substitution 只对 numeral/free-variable fragment 无捕获；不外推到量词。
