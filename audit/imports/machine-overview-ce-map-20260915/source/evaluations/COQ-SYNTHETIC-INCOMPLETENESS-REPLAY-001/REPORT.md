# 作者源代码原生重放：Synthetic essential incompleteness 与 Robinson `Q`

> Evaluation：`COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001`  
> Source：`uds-psl/coq-synthetic-incompleteness@cd7d8490f8542bfe85658c465bcb26b2ed163f53`  
> Native target：`FOL/Incompleteness/fol_incompleteness.vo`  
> Verdict：`NATIVE_COQ_BUILD_AND_CLEAN_REPLAY_PASS_WITH_SCOPE`  
> HoTT instance：`NOT_INSTANTIATED`  
> Reality correspondence：`NOT_ESTABLISHED`

## 1. 本轮实际完成了什么

本评价不只读取 Kirst–Peters 2023 的论文摘要，也不只检查四个核心 `.v` 文件。它在固定的 Coq 8.15 历史环境中，从两个独立干净 Git worktree 分别构建论文仓库声明的最终目标：

```text
make FOL/Incompleteness/fol_incompleteness.vo
```

两次构建都从 commit `cd7d849…` 开始，均 exit 0。随后在只读 build tree 上编译一个独立资格化模块，加载并核对：

```text
self_halting_diverge
recursively_separating_diverge
insep_essential_incompleteness
epf_mu_ctq
Q_incomplete
```

该资格化 run 独立重跑后，exit/stdout/stderr 逐字一致。

## 2. 来源与环境身份

| 项目 | 固定结果 |
|---|---|
| repository | `https://github.com/uds-psl/coq-synthetic-incompleteness.git` |
| branch / commit | `csl` / `cd7d8490f8542bfe85658c465bcb26b2ed163f53` |
| tracked source | 807 files / 7,423,361 B / tree SHA `d9dd001b…80ca` |
| base image | `coqorg/coq:8.15@sha256:2a9a7f61…7098` |
| derived image | `hott-coq-synthetic-incompleteness:cd7d849@sha256:d4a84f07…010b` |
| container platform | linux/amd64；当前 arm64 host 上仿真 |
| Coq / OCaml / opam | Coq 8.15.2 / OCaml 4.07.1 / opam 2.3.0 |
| fixed dependencies | Equations 1.3+8.15；Smpl 8.15；MetaCoq Template `dev+8.15` from commit `9493bb6` |
| derived image size | 1,533,425,178 B |

`SOURCE-MANIFEST.json` 保存 807 个 tracked path 的逐文件 bytes/SHA。`Dockerfile` 保存构建环境；由于 OCaml 4.07.1+flambda 已从 current opam repository 迁出，Dockerfile 显式加入官方 `opam-repository-archive`。两次真实依赖设置失败及其解决方式保存在 `DEPENDENCY-SETUP-FAILURES.json`。

## 3. 两次干净构建的比较

| 项目 | First | Replay | 比较 |
|---|---:|---:|---|
| exit | 0 | 0 | exact |
| wrapper duration | 600.114 s | 600.126 s | observation only；20 秒轮询使其不是精密 benchmark |
| stdout | 11,661 B / `5e3ba359…09ff` | 同左 | byte-exact |
| stderr | 966 B / `c70066e0…020d` | 同左 | byte-exact |
| stable `.vo/.vos/.vok/.glob` artifacts | 1,284 / 61,429,144 B / manifest `6c2bd66c…958` | 同左 | path/bytes/SHA 全部 exact |
| final `.vo` | 95,450 B / `e770c7bf…3e4` | 同左 | byte-exact |
| `.aux` artifacts | 321 / 863,365 B | 同数量/路径/字节 | 319 个 hash 不同 |

`.aux` 文件包含构建辅助信息，两个干净工作树的路径不同，因此未把其字节稳定性冒充内核产物稳定性。两次构建的 `.vo/.vos/.vok/.glob` 全部逐文件相同，构建日志也相同；可复核的 exact replay 主张限定在这些稳定产物。

两次 stderr 的 6 个 warning 都来自 `utils.v` 中 Equations 自动内联 signature 的提示，不是未解决目标、`Admitted` 或内核拒绝。

## 4. 作者代码中真正证明的抽象定理

资格化输出确认 `insep_essential_incompleteness` 的完整类型：

```text
forall theta,
  is_universal theta ->
  forall S neg (fs fs' : FS S neg),
  extension fs' fs ->
  forall r,
  strongly_separates fs' (theta_self_return theta true)
                         (theta_self_return theta false) r ->
  exists n, independent fs (r n)
```

这与本地 Cubical 包 `PF-CUBICAL-SYNTHETIC-INCOMPLETENESS-001` 的结构一致：

- universal step-indexed partial function family；
- self-return-true / self-return-false 两个递归不可分离 predicate；
- proof/refutation 部分 classifier；
- strong separation；
- extension；
- 构造出的 classifier-divergence index 与 independent sentence。

这个对应支持“本地移植抓住了论文的数学骨架”。它不证明两份形式化定义逐项等价；本地 `PartBool` 只处理 Boolean partial functions，作者库使用一般 `part Y`，并在完整 first-order infrastructure 上工作。

## 5. Robinson `Q` 实例的精确假设

`Q_incomplete` 并不是一个无参数的 `Q` 不完备常量。资格化输出显示：

```text
forall p : peirce,
  CTQ ->
  forall T,
  list_theory Qeq ⊑ T ->
  enumerable T ->
  ~ T ⊢T ⊥ ->
  exists φ,
    bounded 0 φ /\ Σ1 φ /\ ~ T ⊢T φ /\ ~ T ⊢T ¬φ
```

因此结论覆盖：同一算术语言内，包含 `Qeq`、可枚举且一致的理论 `T`，在显式 Peirce 与 `CTQ` 条件下存在 closed `Σ₁` 独立句。

作者代码还证明：

```text
epf_mu_ctq : is_universal theta_mu -> CTQ
```

这把 `CTQ` 归约到具体 μ-recursive interpreter 的 universality，但仍保留 `is_universal theta_mu` 参数。构建成功不会生成这个参数的 inhabitant，也不会把 Church thesis 变成普通 Coq 定理。

`Print Assumptions` 对 `insep_essential_incompleteness`、`epf_mu_ctq` 和 `Q_incomplete` 均打印 `Closed under the global context`。这里的含义是没有未列出的**全局公理依赖**；签名中显式出现的 `Universal/CTQ/Peirce/consistency` 参数仍然是调用者必须提供的前提。

## 6. 与本地 Cubical 路线的差距现在怎样量化

本地路线已经完成：

1. 小型 K/S/MP 对象语言与 indexed derivations；
2. raw proof checker soundness/completeness；
3. formula/proof finite bit coding；
4. natural-number proof code 与总 checker；
5. 穷举 proof/refutation 的 `PartBool` classifier；
6. conditional separator-divergence / essential-incompleteness core。

作者 Coq 路线额外完成的决定性部分是：

1. full first-order syntax、substitution、deduction 和 arithmetic signature；
2. Robinson `Qeq` 与其标准自然数解释；
3. `Σ₁` 公式、`Q`-decidability、`Σ₁` completeness；
4. μ-recursive computation、DPRM 与 `EPFμ → CTQ`；
5. disjoint enumerable predicates 的 strong `Σ₁` separation；
6. 把 abstract theorem 实例化到任意一致、可枚举、包含 `Q` 的理论。

这说明当前本地缺口不在 proof code 或 proof search，而在**对象算术中的 strong representability**。用一个 `repr` constructor 直接加入该性质，会跳过作者开发中最重的数学段落。

## 7. 它是否已经证明 HoTT 不完备

没有。本次 build 的对象是 Coq 中形式化的 first-order arithmetic theorem。Coq 作为元证明系统检查了它，`Q_incomplete` 的 `T` 是 `Q` 同一 first-order language 中的可枚举理论。源码没有把 `T` 实例化为 HoTT、Coq-HoTT 或 Cubical Agda 的判定系统。

要得到 exact HoTT instance，至少还需：

1. 固定 HoTT calculus 的有限 syntax 与 judgment/proof code；
2. 证明 proof relation 可枚举，或提供与其对应的 deterministic partial classifier；
3. 定义其 arithmetic consequence theory，证明包含 `Q`；
4. 证明该 consequence theory 可枚举且一致；
5. 把 strong separation / `CTQ` 路线接到这个 exact calculus；
6. 明确 metatheory 位于 inner HoTT、outer 2LTT、MetaRocq 还是外部 kernel。

Swan–Uemura 的模型论结果进一步要求：Church thesis 的适用域必须绑定到具体 cubical/univalent 模型或反射子宇宙，不能对任意 HoTT universe 无条件使用。

## 8. 对不可停机悖论搜索的意义

作者代码为“不可完成”提供了比运行超时严格得多的模板。`recursively_separating_diverge` 返回一个具体 `c` 并证明分类器对任一 Boolean 都不收敛；`insep_essential_incompleteness` 再把这种非完成翻译为 `r c` 与 `¬r c` 均不可证。这个模板已经由本地 Cubical 形式化独立复现，并由作者 Coq build 校准。

但它仍然更接近**一切足够强的有效形式系统共有的边界**。要成为用户定义的现实相对 HoTT 非现实性悖论，还须证明：某项具体 HoTT 抽象、同一性原则、截断、层级安排或自我担保接口，针对同一现实任务新增或遮蔽了完成条件。目前没有这样的自然 consumer 与现实桥梁。

## 9. 可复核入口

```bash
python3 machine-overview/coq_synthetic_incompleteness.py verify \
  --receipt machine-overview/evaluations/COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001/BUILD-RECEIPT.json \
  --rerun-qualification

python3 -m unittest \
  machine-overview/tests/test_coq_synthetic_incompleteness.py
```

当前结果：verifier `COQ_SYNTHETIC_INCOMPLETENESS_REPLAY_VALID`；qualification exact rerun；专项测试 4/4。外部 source/build trees、derived image 和 61 MB 稳定构建产物保存在 `/Volumes/D/HoTT-machine-overview-cache/community-frameworks/`；repo 内保存 receipt、source/stable manifests、两次日志、资格化源码/输出、Dockerfile 和失败说明。
