# CSL 2026 groupoid syntax：G-HOTT-SYNTAX 的首个精确机器切片

本目录固定 Altenkirch、Kaposi、Xie 的 *The Groupoid-Syntax of Type Theory Is a Set* 配套 Cubical Agda 代码。来源为 `https://bitbucket.org/akaposi/cohtt` 的 master commit `5babc385d01500c1777ff932dd8c79299a1d766a`；Bitbucket archive 与独立 Git export 的 91 个文件、1,706,237 bytes 逐文件相同。

它适合作为 `G-HOTT-SYNTAX-001` 的第一片，因为这里的 syntax 不再只是论文伪代码：`TT/Groupoid/Syntax.agda` 直接定义四 sort 与全部构造／路径／二阶相干，`TT/Groupoid/NTy.agda` 机器证明 `Ty` 为 set，`TT/Groupoid/IsoSet.agda` 构造与 set syntax 的四类同构。`CheckGroupoidSyntax.agda` 把这些决定性 theorem 类型在项目内显式重述。

它仍不是完整 HoTT 自语法。该 object theory 没有 Nat、一般 identity type、对象层 univalence/HIT、proof checker/enumerator 或 arithmetic interpretation；因此本包只关闭“选择一个 exact、可重放的 HoTT-relevant syntax slice”，并为下一步扩张列出缺件。2017 2LTT 论文的 §2.1 只提供建议语法且明说完整 term-model/initiality 证明超出范围，不能替代这个机器边界；basic 2LTT 的 conservativity 与 strengthened variants 仍须分别处理。

上游 `cohtt.agda-lib` 没有 `name:` 字段。项目的 `cohtt-replay.agda-lib` 只增加 `name: cohtt-replay`，其余 include、Cubical v0.9 dependency 和 flags 逐项相同。重放采用两阶段：先从源建立 pinned Cubical dependency interfaces，再删去全部 cohtt `.agdai`，用上游 flags 重查 20 个 `TT` 模块及项目探针。直接把 `--hidden-argument-puns` 命令行应用到 Cubical v0.9 全源，会在 `Cubical/Foundations/Prelude.agda:610` 触发 `WrongHidingInLHS`；该现象作为工具配置边界，不解释为 groupoid-syntax theorem 失败。

项目没有复制上游正文源码。固定仓库包含论文的 CC-BY 资产，但没有根或源码许可证文件；本地源码缓存只用于研究重放，不由此推断代码再分发许可。
