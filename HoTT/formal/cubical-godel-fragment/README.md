# GZ-008：来源对应 cubical proof-code fragment

本目录实现 `CCTTmini₀`：一个明确受限的 typed certificate calculus。它以 cctt/redtt
共有的 `Nat`、`suc`、Path/refl 构造为对应点，但**不是**任一上游系统的完整 syntax、checker
或 metatheory。

## 结构

```text
CCTTmini.agda       finite types/terms/certificates and a structural checker
WrongCCTTmini.agda  negative control
CLAIM.md             C-370–C-374 and non-goals
TOOLCHAIN.json       pinned native Agda compiler identity
capture_*.py         immutable primary/negative run capture
```

`RawCert` 不提供 hole、import、metavariable 或 recursive-definition constructor。`check` 对
certificate syntax 结构递归；`Checked` 将返回 type 和 `Deriv` witness 放在同一结果中。

这个包的下一步是 GZ-009：把 `RawCert` 接到 total Nat coding/decoding。那一步之前，不能把这里的
有限 tree syntax 叫作 Gödel numbering，也不能声称已经有 object-level provability predicate。
