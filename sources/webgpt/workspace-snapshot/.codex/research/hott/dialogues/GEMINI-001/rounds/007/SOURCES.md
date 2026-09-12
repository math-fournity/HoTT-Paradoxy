# R027 来源与阅读边界

访问日：2026-09-11。原文IN-006来自本次用户转述，不是API签名导出。引用中的结论分别标为原话、我方推导、官方文档或实际工具结果。

## 项目来源

恢复包：HoTT_early_reassessment_rev26_final_with_git.zip；SHA-256 33a1c9331018b8afb30e8cc5af1b4491910468a981b222e880f9afe868483e67。
继承Git：298ebb0861358f25ff850bafb207d72ae4eccfb6。恢复及原始非Git文件字节基线见 artifacts/r027/BASELINE.json。

实际任务读取：根AGENTS、两Skills、PROTOCOL、LOAD_SET、README、MEMORY/FRONTIER/RESUME；OUT-005全文；R025 TECHNICAL_NOTE完整相关证明；R026 ASSESSMENT及PLAN；当前IN-006全文；STATE及旧checkpoint代码用于治理。部分长工具输出曾被截断，所需直接论证以单独范围重新读取。没有将任何一项hash或plan计为全部模型认知。

完整动态合集不是本轮声称的已加载正文。此次是用户明确要求的有界通信审计与保全，不作全套hott-paradox-research验收。R026旧审读原文、测试与规约探索不重写；R024/025代码和旧证明不重写。

## 一手外部来源

[S01] Lean官方 Theorem Proving in Lean4, Propositions and Proofs，§3.1—3.2（Prop、proof term、theorem、proof irrelevance）。
https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/
使用范围：普通Lean与HoTT身份结构不能不加区别；lemma的值不是命题名称的自动别名。未据此宣称已编译本轮源码。

[S02] Lean官方语言参考，Axioms；Modifiers；Axioms and Computation。
https://lean-lang.org/doc/reference/latest/Axioms/
https://lean-lang.org/doc/reference/latest/Definitions/Modifiers/
https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/
范围：逻辑声明与编译支持、noncomputable、归约。latest为本轮文档版本，不冒称绑定本地二进制。

[S03] Lean官方语言参考，Interacting with Lean 的 #reduce/#eval/#eval!；v4.11.0发布说明。
https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/
https://lean-lang.org/doc/reference/latest/releases/v4.11.0/
范围：#eval编译运行；默认拒绝依赖sorry；#eval!不是安全/正确的实现替代。未执行#eval!。

[S04] Rocq Prover 9.0.1文档，Program extraction, Realizing axioms。
https://rocq-prover.org/doc/v9.0/refman/addendum/extraction.html
范围：有计算内容公理、逻辑公理、外部实现字符串、例外与责任。文档同时描述若干提取分支，未提供单一实际运行结果。未运行Coq/Rocq。

[S05] Cohen, Forster, Kirst, Paiva, Rahli. Separating Markov's Principles, LICS 2024。作者所在大学的论文条目及摘要。
https://research.birmingham.ac.uk/en/publications/separating-markovs-principles/
https://cris.bgu.ac.il/en/publications/separating-markovs-principles/
范围：MP为相应Σ01命题的双重否定稳定性；谓词与存在定义不同会出现不同MP。全文和模型分离证明本轮未加载，不冒称已重证独立性。本文Oracle↔EM_H是本地给出的直接构造，而非从摘要推导全部强弱关系。

## 获取与运行边界

本地原生工具路径未发现。urllib HEAD官方Lean v4.19.0 README和Linux发行包时DNS失败，保存TOOLCHAIN_PROBE.json。下载工具的小README两次请求失败：第一次因尚未被web打开，第二次为download failed；没有生成成功下载文件。web可阅读官方文档不等于容器可安装二进制。

https://lean-lang.org/doc/reference/4.19.0/Interacting-with-Lean/ 的web打开失败，未用它声称钉死4.19命令行为。所有本地原生实验状态见NATIVE_RUN.json；禁止从文档预期填写实测结果。
