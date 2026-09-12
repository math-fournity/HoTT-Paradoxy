# R033 · 来源与主张归属

## 项目当前依据
- `MEMORY.md` 的 revision32 版：明确下一项依赖上下文/替换问题，恢复副本在当前 Git 的继承提交中可取得。
- `.codex/research/hott/reviews/SELF-REFERENCE-004/PROOF_NOTE.md`：非依赖迁移判据，不自动涵盖本轮的新条件。
- `HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md` §8—11：自反射范围、版本、局部证据，不以本轮有限模型认证整个HoTT。
- `HoTT/THEORY_SCHEMA.md`：通过身份/依赖对/传输的规则入口回查源码，不将Schema的组织关系当作定理。

## 固定的一手理论正文（随包本地保存）
`HoTT/theory-schema/upstream/book-578b85cc/basics.tex`：
- 761起：transport及路径归纳构造。
- 800起：path lifting，沿p把(x,u)连接到(y,transport(p,u))。
- 859—882：依赖函数作用于路径；自然性证明的规则依据。
- 1394—1499：§2.7依赖对，特别是1417—1422的同一首分量不推出固定纤维元素相等；1426起的路径Σ分解。
- 1501—1525：嵌套Σ的transport公式，后层使用提升后的路径而不是原首分量路径。
- 1763附近：ua的命题性计算规律。涉及ua的等式不是本轮宣称执行过的判断归约。
- 2693—2695：`(Bool,false)=(Bool,true)`在总空间内的标准练习；不推出固定Bool中false=true。
`HoTT/theory-schema/upstream/book-578b85cc/logic.tex` 801—838：命题截断与唯一选择，可通过唯一刻画的中间命题提取目标数据。

## 本轮外部核对
2026-09-11 通过web读取：
- https://raw.githubusercontent.com/HoTT/book/master/basics.tex ，定位`thm:path-sigma`、`transport-Sigma`、依赖函数路径作用。
- https://raw.githubusercontent.com/HoTT/book/master/logic.tex ，定位`sec:unique-choice`。
master页面是在线交叉核对，不声称与本地固定commit逐字节相同。固定commit原始URL的web抓取失败；不能将失败抓取当新来源。

## 本轮构造与未执行范围
PROOF_NOTE P1—P6 是对标准规则的显式应用、条件证明及本项目任务解释，不宣称原创。
Python实现的是有限C2群胚的集合值作用，不能把一个局部表的通过称为HoTT Π项被内核接受。
Agda共享MLTT源码只包含参数化的依赖运输/自然性/不兼容条件；没有原生编译。完整HoTT语法迁移、所有高阶相干、任意值类型的有效计算尚未建立。
本轮没有新增物理实验、HOTT内部矛盾或已闭合的现实相对悖论。
