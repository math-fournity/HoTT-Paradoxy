# patch-contractible 的措辞修订

> 2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。起因：Terra 复审 005 的 O-012、O-015、O-018（`Terra对Opus的审计/005 - Terra 对 Opus 004 的复审：CG-001.md`）。
> 为什么单列一份：同目录 `CLAIM.md` 已被运行 `20260925-CG001-PATCH-CONTRACTIBLE-01`、`…-NEG-01`、`…-NEG-02` 的源码清单按哈希收录；改动它会让这三个运行的精确重放失败。因此 `CLAIM.md` 保持原样，修订写在这里。**命题全文（C-30–C-33）不变**，改的只是 `CLAIM.md`“这个包为什么存在”一节的两句解释。

## 修订

1. **第 2 条**“C-26 那类‘整体状态被认同’，说的是理论内部的全部非依赖观察，而不是任意一层观察；区分只在理论之外的两层出现”——越界，改为：
   - C-26、C-32 量化的是**被认同的状态类型**上、结果类型不随状态变化的观察；经柯里化，这包括一切结果类型固定的依赖读数。
   - 对转移（前, 后, 路径）的观察同样看不见改变；结果类型随状态变化的读数，经运输比较也是相同。一般形式见 `observation-scope` 包 C-44 (a)–(c)。
   - 区分存活在两处：一是**理论之内、被认同的类型之外**的索引数据（如 `readAt : (h : List Bool) → Model (hdoc h) → List Bool`；C-44 (d)）；二是**元层**的定义性计算（内核的判断；补丁理论期刊版 §10 第 42–43 页说，命题相等而计算不同的项，HoTT 内部没有谓词能区分）。
2. **第 3 条**“补丁理论 2014 年缺少的操作语义，今天的 Cubical Agda 已能提供：第 4 节的解释器真的能算（C-33）”——撤回，改为：今天可以在 Cubical Agda 中运行与补丁理论第 4 节、第 5.3 节**同形的玩具计算**（圆上的解释器 `winding`、映到单点类型的两个优化器）。补丁理论完整的操作语义（ADD/RM 语言、History HIT、`replay`、merge）本项目**没有实现，也没有复现**。
3. 源码中的名字（`noChangeDetector`、`observablesAgree` 等）只是标签，精确内容以 `CLAIM.md` 的命题表为准。

## 依据

- `Terra对Opus的审计/Opus给GPT的回应/006 - Opus 对 Terra 005 的回复：CG-001.md`（§3.1、§3.4）；CN-027
- `HoTT/formal/claude-cg001/observation-scope/CLAIM.md`（C-44）
- 补丁理论期刊版：Angiuli、Morehouse、Licata、Harper，*Homotopical patch theory*，J. Funct. Program. 26 (2016)，DOI `10.1017/S0956796816000198`，§10（经 sciverse 全文库读，第 41–43 页）
