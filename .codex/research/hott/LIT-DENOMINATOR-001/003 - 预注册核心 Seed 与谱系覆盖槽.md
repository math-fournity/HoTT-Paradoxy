<!-- governance-shard:v2
logical_id: LIT-DENOMINATOR-001
shard_id: 003
index: ../LIT-DENOMINATOR-001.md
-->

# 预注册核心 Seed 与谱系覆盖槽

## 一、为什么必须预注册

18×2 discovery 对 33 个已知必需 seed 只 exact-title 命中 13 个；20 个需要手工一手入口。若只信 API 排名，Turing、Gödel、Church、Rosser、Rice、Löb、Lawvere、O’Connor、Dominances 等会从“全面覆盖”中消失。因此核心 seed 与 discovery 候选取并集，任一方都不能替代另一方。

## 二、经典与计算基础

| Seed | 作用 | 当前状态 |
|---|---|---|
| `SEED-GODEL-1931` | 算术化与第一不完备性 | primary entry known；全文/前提提取待完成；API exact miss |
| `SEED-TURING-1936` | 可计算机与 Entscheidungsproblem | primary entry known；全文待完成；API exact miss |
| `SEED-CHURCH-1936` | λ-可定义性与不可解性 | primary entry known；全文待完成；API exact miss |
| `SEED-ROSSER-1936` | simple consistency 下加强不完备性 | DOI `10.2307/2269028`；全文待完成；API exact miss |
| `SEED-KLEENE-1938` | 程序索引自指/第二递归定理来源 | DOI `10.2307/2267778`；全文待完成；API exact miss |
| `SEED-POST-1944` | r.e.、归约与不可解度 | BAMS 50(5) 整期原件固定；印刷页 284–316 抽取、页界核验、全文首读完成；theorems 未机器重放 |
| `SEED-RICE-1953` | 非平凡程序语义性质不可判定 | primary entry known；全文待完成；API exact miss |
| `SEED-LOB-1955` | provability/self-guarantee 固定点约束 | primary entry known；全文待完成；API exact miss |
| `SEED-RADO-1962` | 有限机器族与不可计算最大运行 | primary entry known；全文待完成；API exact miss |
| `SEED-LAWVERE-1969` | CCC 中的统一对角论证 | primary entry known；全文待完成；API exact miss |

Tarski、Hilbert–Bernays、s-m-n/normal form、Rogers/Myhill、Rice–Shapiro 和 Chaitin 作为 v1 必需 coverage slots 登记在本逻辑文档；它们没有因 33-seed 初始数组未逐项列出而被排除，必须在 `LIT-CLASSICS-001` 补为稳定 seed。

## 三、部分性、HoTT 与机器化不完备性

| Seed | 作用 | 当前状态 |
|---|---|---|
| `SEED-CAPRETTA-2005` | coinductive partial elements/general recursion | exact discovery；全文待完成 |
| `SEED-OConnor-2005` | Coq Gödel–Rosser 数值编码 | PDF 已下载/相关章节已读；API exact miss |
| `SEED-PARTIALITY-REVISITED` | partiality quotient/HIT | primary entry known；全文待完成；API exact miss |
| `SEED-2LTT-2017` | inner HoTT / outer strict metatheory | exact discovery；PDF 相关章节已读 |
| `SEED-DOMINANCES-2017` | univalent TT 中 partiality/dominance/computability | primary entry confirmed；全文待完成；API exact miss |
| `SEED-CUBICAL-NORM-2021` | normalization 与 judgmental equality decidability | exact discovery；全文待完成 |
| `SEED-PARAMETRIC-CT-2021` | universal function、s-m-n、无选择 synthetic computability | primary/source qualified；`coq-synthetic-computability@b9523cb` 109 文件树固定；C-219–C-222 条件内部否定在 Coq 8.13.2 重放；paper 全文/citation chain 仍开放 |
| `SEED-KIRST-HERMES-2021` | Coq 中 synthetic undecidability/incompleteness | proceedings+journal exact discovery；PDF相关章节已读 |
| `SEED-CUBICAL-ASSEMBLIES` | Church thesis 在 cubical/univalent 模型中的适用域 | exact discovery；PDF模型角色已读 |
| `SEED-KIRST-PETERS-2023` | synthetic essential incompleteness | PDF/作者 Coq 已读与重放；API exact miss（标点/版本差） |
| `SEED-INTERNAL-SCONING-2023` | 类型论内部元理论、normalization/canonicity | exact discovery；全文待完成 |
| `SEED-CANONICITY-COMPUTABILITY-2023` | HoTT 中 canonicity/computability 的直接连接 | exact discovery；新增核心全文义务 |

## 四、2024–2026 与官方项目

| Seed | 作用 | 当前状态 |
|---|---|---|
| `SEED-ORACLE-MODALITIES-2024` | HoTT higher modalities 中的 Turing reducibility | `awswan/oraclemodality@e6e3f75` 34 文件 MIT 源树完整导入并提取 postulate/consumer 边界；paper/source full machine replay 仍待 Agda 2.6.4.3/Cubical v0.7 |
| `SEED-POST-CIC-2024` | CIC 中 Kleene–Post、jump、Post hierarchy | exact discovery；primary abstract checked；全文/源码待资格化 |
| `SEED-SYNTHETIC-OVERVIEW-2025` | 截至 2025 的机器化 computability/logic 总图 | primary proceedings entry confirmed；API exact miss |
| `SEED-COFIBRATION-COMPLEXITY-2025` | cubical cofibration entailment 的复杂度 | primary proceedings entry confirmed；API exact miss |
| `SEED-STRICTIFIED-SYNTAX-2025` | type theory in type theory、strictified syntax | exact discovery；primary body 待读 |
| `SEED-ORDINAL-DECIDABILITY-2026` | HoTT 中 α-decidability 分级 | proceedings+arXiv exact discovery；primary abstract checked |
| `SEED-GROUPOID-SYNTAX-2026` | HoTT/HIIT/GCwF 语法与可判定相等 | official paper/body reviewed；`akaposi/cohtt@5babc385` 91 文件树固定；20 TT 模块与 C-223–C-226 两阶段 Cubical Agda exact replay；完整 HoTT calculus 仍开放 |
| `SEED-EXTENSION-TYPES-2026` | 2LTT、cubical gluing、univalence、conservativity | arXiv/title exact discovery；primary abstract checked |
| `SEED-AGDA-GODEL` | Agda 的一/二不完备、Löb、Chaitin | official repo confirmed；不应期待 bibliographic API exact match |
| `SEED-LEAN-FOUNDATION` | Lean 4 的 Gödel/Rosser/Löb/Tarski/Church | official repo confirmed；不应期待 bibliographic API exact match |
| `SEED-METAROQ` | quotation、reference checker、self-formalization | official repo confirmed；build/full paper qualification 待完成 |

机器 seed 数组与 exact-match keys 位于 `TRIAGE.json`；本表加入人工已知状态，不修改机器结果。
