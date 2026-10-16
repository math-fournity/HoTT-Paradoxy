# Parametric CT：显式计算前提下的内部不可判定性重放

本目录为 `R2-INTERNAL-UNDEC-001` 固定一条比 Coq MM2 synthetic implication 更强、但仍严格带前提的结果。上游是 Yannick Forster 的 `coq-synthetic-computability`：branch `code`，commit `b9523cb33180dc58b227432e60045cc38615b711`，Git tree `9cfc31a04f31e0a73cd9494a8d745a39ee639082`。

`SOURCE_TREE_MANIFEST.json` 固定上游 109 文件树；`TARGET_CLOSURE.json` 固定构建 `Axioms/halting.vo` 实际观察到的 20 个本地源文件。重放只编译该闭包，避免让与目标无关的 MetaCoq/Smpl 分支改变证明身份。`REPLAY_SOURCE.json` 记录 codeload archive、独立 Git fetch、树内容一致性、精确定理和前提边界。

关键区分是：

```text
MM2 上游 synthetic theorem:
  decidable P -> enumerable (complement SBTM_HALT)

本包内部否定 theorem:
  EPF_bool + SCT -> ~ decidable P
```

后者确实以 Coq 的否定类型表达“没有 total Boolean decider”，但 `EPF_bool + SCT` 是一个显式和类型前提：给出 EPF_bool 或 SCT 任一分支才得到结论。`Print Assumptions` 的 `Closed under the global context` 表示证明项没有再依赖未列出的全局公理，并不把这个显式前提变成 ambient HoTT 的定理。

作者 README 指定 Coq 8.13.2、Equations 1.2.3+8.13、stdpp 1.5.0。以 Coq 8.15.2 和 stdpp 1.7.0 尝试时，构建在 `Shared/ListAutomation.v:142` 失败；故本包使用 `DOCKER_IMAGE.json` 固定的 8.13.2 镜像，而不把跨版本失败误读成目标定理失败。

固定提交中没有许可证文件。项目没有复制上游源文件正文；完整树留在 `/Volumes/D/HoTT-literature-cache/parametric-ct-b9523cb/`，通过 archive、Git tree 和逐文件 hash 重放。该安排只说明本地研究证据身份，不推断再分发许可。

项目内验证入口：

```bash
python3 -B scripts/audit/import_coq_parametric_ct.py
python3 -B scripts/audit/verify_formal_proof_run.py \
  --run-dir HoTT/verification/runs/20260914-MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001-01 \
  --rerun
```
