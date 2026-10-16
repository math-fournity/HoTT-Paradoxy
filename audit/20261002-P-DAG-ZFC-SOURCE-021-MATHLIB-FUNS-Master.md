# H021：Mathlib ZFSet `funs` 的冻结 parent source card

> **身份：** `MASTER_PINNED_SOURCE_TRACER / FORMAL_MODEL_SCOPE / NOT_A_ZFC_Q_RESULT`。

## 来源身份

本卡只重述先前保存的版本固定一手来源核验：Mathlib4 `v4.16.0`、commit `a6276f4c6097675b1cf5ebd49b1146b735f38c02`、`Mathlib/SetTheory/ZFC/Basic.lean`。旧 source trace 的完整证据在 [P-DAG-SOURCE-001](20261002-P-DAG-SOURCE-001-Terra-Max.md)；该文件明确将这件事限制为 Lean underlying type theory 中的 ZFC(+Choice)模型，不能当作标准 ZFC 本体事实。

## 冻结父字段

```text
T     = Mathlib ZFSet model @ v4.16.0/a6276f4…
layer = formal-model API / semantic membership contract
u     = powerset (prod x y)
F     = powerset, with mem_powerset
C     = funs x y := ZFSet.sep (IsFunc x y) u
I     = x, y, candidate f, and u
O     = funs x y : ZFSet
Done  = model-level membership/use contract mem_funs:
        f ∈ funs x y ↔ IsFunc x y f
Q     = UNSET; H022 must test whether a nontrivial positive obligation exists
```

The source excerpt has no operation lifecycle, real-world task, runtime evaluator, or stated positive obligation beyond these fields. H022 may reject, narrow or leave `Q` absent; it may not replace `u/F/C` with a newly selected object.

