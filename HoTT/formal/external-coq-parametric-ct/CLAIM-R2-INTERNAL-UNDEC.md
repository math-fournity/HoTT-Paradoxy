# MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001

## 固定身份

- proof ID：`MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001`
- run ID：`20260914-MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001-01`
- claims：`C-219`–`C-222`
- 上游：`yforster/coq-synthetic-computability`，branch `code`，commit `b9523cb33180dc58b227432e60045cc38615b711`，Git tree `9cfc31a04f31e0a73cd9494a8d745a39ee639082`
- kernel：Coq 8.13.2 / OCaml 4.07.1；目标依赖为 Equations 1.2.3+8.13 与 stdpp 1.5.0

## 精确命题

`C-219`：Coq 接受

```coq
EPF_SCT_halting :
  EPF_bool + SCT ->
  exists K : nat -> Prop,
    semi_decidable K /\
    ~ semi_decidable (compl K) /\
    ~ decidable K /\
    ~ decidable (compl K).
```

`C-220`：Coq 接受

```coq
K_nat_bool_undec :
  EPF_bool + SCT -> ~ decidable (compl K_nat_bool).
```

`C-221`：Coq 接受

```coq
K_nat_undec :
  EPF_bool + SCT ->
  ~ decidable (fun f : nat -> nat => forall n : nat, f n = 0).
```

`C-222`：`Print Assumptions` 对上述三个定理都输出 `Closed under the global context`。这里的强度必须按定理类型读取：`EPF_bool + SCT` 是显式前提，结果是在 Coq 对象语言内的 `~ decidable`；输出并不证明 `EPF_bool` 或 `SCT` 在 ambient HoTT 中成立。

## 证据与禁止外推

重放从 109 文件的哈希固定上游树中只取 `TARGET_CLOSURE.json` 登记的 20 个实际依赖文件，在干净目录构建 `Axioms/halting.vo`，再编译 `CheckInternalUndec.v`。本包因此关闭的是：**在显式 EPF_bool 或 SCT 前提下，内部否定形式可由 kernel 重放**。

本包不证明 ambient HoTT 中无条件 `~ decidable`，不证明 EPF/CT 与任意 univalent universe 相容或成立，不使用 Path、univalence、HIT 或 modality，不建立 HoTT essentiality、natural consumer、现实同任务桥梁、Gödel 不完备性或 HoTT 内部矛盾。上游固定提交没有许可证文件；源码只在外置缓存中用于本地研究重放，不能从本包推断再分发许可。
