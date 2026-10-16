# MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001 精确主张

Proof ID：`MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001`  
Claim IDs：`C-244`–`C-249`  
上游：`uds-psl/coq-synthetic-incompleteness@cd7d8490f8542bfe85658c465bcb26b2ed163f53`  
目标：Coq 8.15.2 内核重建 `FOL/Incompleteness/fol_incompleteness.vo` 并加载 exact theorem signatures。

## C-244：来源、许可证与工具链

repo-contained deterministic Git archive 解压为 807 个 tracked files / 7,423,361 bytes，逐文件与 `SOURCE_TREE_MANIFEST.json` 相同，derived tree SHA 为 `d9dd001b0dcfcab4d183b01f0eeed9d16d12c09b576507ea7fc45c87505680ca`。CeCILL 许可证随 archive 和目录原件保留。重放固定 derived image `sha256:d4a84f07bbfe0bf3f2dce5b07e7fb43423ff64f990678a114ec6b080d131010b`。

禁止外推：来源/工具链资格化本身不是数学定理；Docker image 存在不证明目标已构建。

## C-245：递归不可分离分类器的发散见证

在显式 `is_universal theta` 前提下，作者定理 `self_halting_diverge` 和 `recursively_separating_diverge` 分别对正确分类 self-halting 或两个 `theta_self_return` 集的 partial Boolean classifier 构造某个自然数 `c`，并证明对每个 `y : bool` 都没有 `part_eval (f c) y`。

禁止外推：结论依赖给定 universal partial-function family 与 classifier correctness；不是任意程序发散，也不说明 HoTT kernel 或普通 proof checker不终止。

## C-246：抽象 essential incompleteness

`insep_essential_incompleteness` 的精确强度为：给定 `is_universal theta`、两个形式系统 `fs/fs' : FS S neg`、`extension fs' fs`，以及由 `fs'` 强分离 `theta_self_return theta true/false` 的表示 `r : nat → S`，存在 `n` 使 `r n` 对 `fs` independent。

禁止外推：`Universal`、extension 与 strong separation 都是显式参数；定理尚未实例化为 HoTT syntax。

## C-247：从 μ-recursive universality 到 CTQ

在隐式 Peirce 参数下，`epf_mu_ctq : is_universal epf_mu.theta_mu → CTQ`。它把 CTQ 归约到具体 μ-recursive interpreter 的 universality。

禁止外推：构建并不产生 `is_universal epf_mu.theta_mu` 的 proof，也不把 CTQ 或 Church thesis变成无条件 Coq/HoTT 定理。

## C-248：Robinson Q 的条件性独立句

`Q_incomplete` 的 exact theorem type要求：

```text
forall p : peirce,
  CTQ ->
  forall T : theory,
  list_theory Qeq ⊑ T ->
  enumerable T ->
  ~ T ⊢T ⊥ ->
  exists φ,
    bounded 0 φ /\ Σ1 φ /\ ~ T ⊢T φ /\ ~ T ⊢T ¬φ
```

最后一项在源码中写作 `~ tprv T (Impl φ falsity)`。因此结果是在显式 Peirce 与 CTQ 下，对任意包含 `Qeq`、可枚举且一致的同语言理论 `T`，存在 closed `Σ₁` 独立句。

禁止外推：没有证明任意 HoTT calculus 包含 Q、可枚举或一致；也没有证明该句在经验现实中的同一任务可获得。

## C-249：fresh build、stable artifacts 与 assumptions replay

从 repo-contained archive 新解压后，目标 build exit 0；stdout/stderr 必须与已冻结两次 clean build逐字一致，1,284 个 `.vo/.vos/.vok/.glob` stable artifacts 与 target `.vo` 的路径/bytes/hash 必须一致。`Qualification.v` 连续两次输出逐字一致；`insep_essential_incompleteness`、`epf_mu_ctq`、`Q_incomplete` 的 `Print Assumptions` 各打印一次 `Closed under the global context`。

“Closed under the global context”只排除未列出的全局公理依赖；C-246–C-248 theorem types 中的 `Universal`、CTQ、Peirce、包含 Q、enumerability、consistency 与 separation 参数仍是调用义务。

## 本包不证明

- exact HoTT calculus 的 Gödel 不完备性；
- HoTT/Path/univalence/HIT 对一般不完备性机制是必要的；
- ambient HoTT 无条件接受 CTQ/Church thesis；
- 理论内部矛盾；
- 一次搜索超时等于不可证明性；
- 用户定义的现实相对非现实性悖论或同一现实任务桥梁；
- 本项目对一般 Gödel/Rosser 结果的原创性。
