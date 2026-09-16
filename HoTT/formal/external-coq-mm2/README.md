# Coq Undecidability Library：MM2 外部定理重放源

本目录保存 `R2-UNIVERSALITY-001` 所需的外部两计数器机器来源身份、关键上游源码和本地 kernel 重放探针。

重放基线是上游 `coq-8.15` 分支提交 `c486697da8cfa4b9bb11b4c53eea7d57781c0deb`，Git tree 为 `6469b73eb0e8cd73d8ecd0cac5711a07912c54d2`。`SOURCE_TREE_MANIFEST.json` 固定该提交 Git archive 的全部 777 个文件；`upstream-coq-8.15-c486697/` 保存直接决定本轮语义和定理身份的 12 个原文件。完整树在外置缓存中重放，关键源码和全树 manifest 留在项目内。

本机重放使用 Docker image ID `sha256:d4a84f07bbfe0bf3f2dce5b07e7fb43423ff64f990678a114ec6b080d131010b`，其中 Coq 为 8.15.2、OCaml 为 4.07.1。`CheckMM2Undec.v` 在上游依赖编译后再次执行：

```coq
Check MM2_HALTING_undec.
Print Assumptions MM2_HALTING_undec.
```

必须按上游定义解释结果：

```coq
Definition undecidable {X} (p : X -> Prop) :=
  decidable p -> enumerable (complement SBTM_HALT).
```

所以 `MM2_HALTING_undec` 证明的是一条 synthetic undecidability 蕴含，不是在无附加前提的构造元理论中直接给出 `~ decidable MM2_HALTING`。`decidable P` 在该库中是存在一个逐点反映 `P` 的总布尔函数；从上述定理升级到内部否定，还需要证明 `complement SBTM_HALT` 不可枚举或加入相称的计算原则。

当前 `rocq-9.2` 分支提交 `c7257b736763d7b2bc3bd25ac47d5fb7ce749c9c` 的独立来源资格化位于 `audit/literature/LIT-MECH-META-001/coq-library-undecidability/`。两代关键定义经逐条审读保持同一 MM2 指令／步进／停机核心及同一 `undecidable` 定义，但文件不逐字相同；当前分支增加了 `MM2_ZERO_HALTING` 等结果并迁移到 Rocq/Stdlib/MPL-2.0。

本目录尚不证明上游 `MM2` 与项目 `ProgramCode` 的编译等价。那条桥必须在 Cubical Agda 中另行给出逐步模拟、有限运行保持和停机双向对应，不能由源码形似自动获得。

