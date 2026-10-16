# R028 来源范围（2026-09-11）

## 当前任务直接来源

- IN-007.md：用户本轮粘贴的Gemini公开回复，逐字保存为独立正文；hash见artifacts/r028/INPUT_PROVENANCE.json。
- TO_GEMINI_006.md及rounds/007/TECHNICAL_NOTE.md：本轮实际重读的上次问题与证明条件。
- scripts/research/r024_diagonal_machine.py：本轮完整检查所用State/Returned、step、compile_diagonal并实际调用两个明确实例；原字节未改。
- reviews/EARLY-GEMINI-001/PLAN.md、最新MEMORY/FRONTIER/RESUME：保持R026规约/未知/资源三层路线，而非每封信重置任务。

## 外部一手核查（web工具读取，未下载完整网页正文）

S01. Lean Language Reference, Axioms
https://lean-lang.org/doc/reference/latest/Axioms/
支持：axiom没有定义体与归约规则；含所需非证明数据公理的代码生成受限；公理的类型合法性不验证其真实性或相容性；仅出现在证明中的公理并不一律阻止代码生成。
边界：latest是读取时文档，不冒报固定本地Lean版本；文档不是本轮运行日志。

S02. Lean Language Reference, Interacting with Lean
https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/
支持：#reduce的归约接口，#eval的编译执行接口，sorry相关默认拒绝及不同入口边界。
边界：未填写示例stderr为实测；没有运行#eval!。

S03. Rocq 9.1.0 Reference Manual, Program extraction
https://rocq-prover.org/doc/V9.1.0/refman/addendum/extraction.html
支持：信息性公理、逻辑公理、异常占位、外部实现映射及用户责任。
边界：页面同时包含fail和warning/exception描述；未固定提取配置并运行时不强断唯一输出形状。没有本轮生成的OCaml/Haskell文件。

S04. HoTT Book, Formal type theory, official source
https://raw.githubusercontent.com/HoTT/book/master/formal.tex
支持：判断/上下文/形成规则须精确固定；书式公理与计算规则的区分。
边界：网上master仅用于核查书式论述，不将其当当前所有HoTT变体的统一计算规范，也不修改仓库固定book-578b85cc快照。

本轮新数学推断（全称Reach与返回保持的后果）由TECHNICAL_NOTE.md给出，不说来源论文已经证明了本例的新命名结论。有限检查不是无界证明；没有将工具可访问的网页误说成本地工具可下载/可编译。
