# 半单纯类型的有限层：外部程序逐层生成、内核逐层接受（C-62）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325。
>
> **起因**：接手探索时提出的新方向“无穷相干”（`.claude/思考与发现/CN-034 …` §5）的第一件正控制：芝诺式结构的“每一有限步都做得到”这一半。
>
> - proof id：`MP-CG001-SST-FINITE-LEVELS-001`（主包）；负控制 `MP-CG001-SST-FINITE-LEVELS-NEG-001`。
> - claim：`CG001-C-62`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9（`HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`），`--safe --cubical --guardedness`，无公设。捕获 `scripts/audit/capture_agda_proof_run.py`。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §15（GOAL_LOCAL_INDEX_ONLY）。

## 文件

- `gen_sst.py`：外部生成器（普通 Python 程序）。对每个具体的 n，打印 n 截断半单纯类型的类型，作为一个封闭的 Agda 项。输出确定。
- `SSTLevels.agda`：`python3 -B gen_sst.py 5 > SSTLevels.agda` 的输出，未经手改。
- `WrongFace.agda`：负控制。

## 命题全文（`SSTLevels.agda`）

对 n = 0, 1, 2, 3, 4, 5：

- `SST≤n : Type₁` 是一个良构的类型：Σ[ A0 ∈ Type ] Σ[ A1 ∈ … ] … Σ[ An ∈ … ] Unit，采用索引式表示。m 维单形的面是 {0..m} 的非空真子集 U，变量名为 x 加 U 的数字；族 A_m 对每个非空真子集取一个参数，按先大小后字典序；U 的变量类型是 A_{|U|−1} 作用于 U 的非空真子集的变量。
- 第 m 层的族有 2^{m+1} − 2 个面参数：0、2、6、14、30、62（由生成器计算，写在生成文件的文首注释中）。
- `terminal≤n : SST≤n`：每一层都有居民（各层都取 Unit 的终对象），所以这些类型非空。

内核接受整个文件：每一个被打印出来的有限层都是 Cubical Agda 中的良构类型。

## 与开放问题的关系

- 【来源】所求的是理论内部的一个族 F : ℕ → U，使 F(n) 编码 (A₀, …, Aₙ)。这是 HoTT 的长期开放问题，由 Voevodsky、Lumsdaine 等人在 2012/13 年 IAS 特别年讨论（Kraus，*Internal ∞-categorical models of dependent type theory*，2021，§4）。
- 【来源】对每个外部固定的 n，第 n 层可以在 HoTT 中写出；这一类元定理在 HoTT 内部无法陈述，可以在 2LTT 中把 n 作为外层变量来陈述（Annenkov、Capriotti、Kraus、Sattler，*Two-level type theory and applications*，MSCS 摘要）。本包是这一事实前六层的机器重现。
- 【来源】Kolomatskaia 与 Shulman（*Displayed Type Theory and Semi-Simplicial Types*，MSCS 2025，§1）：每一次在理论内部把生成 A_n 的组合结构编码为 n 的函数的尝试，“似乎又导向一个无穷后退”。
- 【来源】Buchholtz（*Higher Structures in Homotopy Type Theory*，收于 *Reflections on the Foundations of Mathematics*，Springer 2019，第 162 页）：无人做到；2015 年华沙的一次非正式调查中，多数 HoTT 研究者认为它不可能。

## 禁止外推

- 不证明理论内部的 F : ℕ → U 不存在，也不证明它存在：那是开放问题。
- 生成器在理论之外运行；“每一层都能写出”不蕴含“能在理论内部一次写出全部层”。二者的差别正是本方向要研究的对象。
- 各层用的是 Unit 值的平凡居民，不涉及任何非平凡的相干数据。

## 负控制

`WrongFace.agda`：手写第 3 层，把三角形 x013 的第三条边写成 x12（应为 x13）。预期被拒：`x2 != x3 of type A0`。这说明生成文件中的面关系是被内核检查的，不只是被解析。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-SST-FINITE-LEVELS-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-SST-FINITE-LEVELS-NEG-01`。
