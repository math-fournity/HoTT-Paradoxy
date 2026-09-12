# R031 来源、复用与原创性边界

## 本地原有依据

1. `.codex/research/hott/reviews/SELF-REFERENCE-001/PROOF_NOTE.md`（R029）：总同域评价器与反向函数闭包的条件反证。
2. `.codex/research/hott/reviews/SELF-REFERENCE-002/PROOF_NOTE.md`及PLAN（R030）：分阶段语言、代码207、无旧代表、错误自调用轨迹；当前问题由其下一动作接续。
3. `HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md`：历史自指线索、R029—030实际范围。
4. `HoTT/THEORY_SCHEMA.md`：区分对象语法、判断、元理论与可回查规则；不作为Löb条件自动成立的证据。
5. `HoTT/theory-schema/upstream/book-578b85cc/formal.tex`：固定书式语法/上下文/判断呈现。未宣称此文件已经定义了完整的内部可证明性谓词。

## 本轮外部核查（非本项目内核验收）

- Archive of Formal Proofs, Lawrence C. Paulson with Janis Bailitis, “Gödel's Incompleteness Theorems”, entry containing “Loebs_Theorem”.
  https://isa-afp.org/entries/Incompleteness.html
  访问：2026-09-11。网页明确其对象理论为HF、可证明性谓词为PfP，并使用Hilbert–Bernays–Löb导出条件。这支持本轮机制为已知结果、依赖需明确；不替本项目完成HoTT实例、运行或一致性证明。网页不是本轮重新执行的Isabelle日志。
- Mike Shulman, “Homotopy Type Theory should eat itself (but so far, it’s too big to swallow)”, 2014-03-03.
  https://homotopytypetheory.org/2014/03/03/hott-should-eat-itself/
  访问：2026-09-11。文章区分原始语法、良型性与解释，任务是第n宇宙解释较少宇宙的HoTT；作者明确它不是不可能性定理。本轮只作历史问题定位，不以2014状态推断当前仍未解，也不把相干问题直接解释成执行无限宇宙。

此前查阅的其他搜索结果未作为本轮技术结论依据；没有分析PDF，没有下载或重跑上述外部形式化工程。

## 本轮生成

完整推导为已知Löb证明在当前“有限校验—同理论反射”的问题中的展开。证书程序、上下文/依赖负例、参数化Agda转写为本轮新增资产，不据此认领定理原创性。
