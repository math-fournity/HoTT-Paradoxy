# 运行收据修订

- `20261005-MP-ZFC-DENSE-QUANTIZED-CONTRACT-001-01` 是首次接受的内核运行。随后 C4D TaskCard 由 `LEAF_ACTIVE` 写成其实际的 `LOCAL_LEAF_CLOSED` 状态，导致该 run 的 source-manifest 文档 pin 不再等于 current source。数学 Lean source未变。
- `...-02` 重新捕获同一 Lean source和命题，刷新当前 source-to-spec documentation pin，并成为 registry primary run。`-01`保留为不可变历史收据，不再作current version-closure依据。
