# 实数拓扑圆模型的来源与工具链资格化

目标是为GEO-01/02提供真正的实数拓扑圆去点、开区间及端部/环境模型；普通Lean几何结论不会直接冒充原生HoTT结论。本文件目前只保存来源与环境资格，不交付新的数学结论。

## 已取得的直接事实

- 本机已有Lean 4.34.0，实际binary输出commit `293d5d0c0c3f3dded4688b3ccd6a33939ac5102b`、arm64-apple-darwin。
- 官方mathlib4标签v4.34.0解析为 `5ed2965256430c3649e86755f9576b54eca72435`，其lean-toolchain恰为`leanprover/lean4:v4.34.0`。
- 已按该commit保存`Sphere.lean`、lean-toolchain与Apache 2.0 LICENSE，路径、URL、hash见[SOURCE.json](SOURCE.json)。不是只保存一个会随master变化的文档链接。
- 已检视源码的模块说明、导入及stereographic/stereographic'接口。官方在线入口为[Sphere模块](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/Instances/Sphere.html)，它提供立体投影的开放部分同胚及source/target接口；这里只按SOURCE_INSPECTED_NOT_REPLAYED转述，尚未在本任务编译。
- 已查的两个旧候选项目没有实际mathlib依赖目录：formal-qkd虽登记mathlib但锁Lean4.27.0-rc1；verified-ledger没有mathlib。不能冒称已具备本轮几何运行环境。

## 下一实际步骤

1. 按外置大文件Skill在D盘为上述exact版本准备独占依赖与构建缓存，避免修改借阅的候选项目。
2. 在HoTT/formal的独占几何目录创建真实Lean入口，以实数二维空间中的单位圆为对象，实例化所需source/target与连续双逆，不只写接口名。
3. 明确经典选择/非计算定义与实际程序/物理动作的区别；stereographic'使用线性等距识别，不能把声明的homeomorphism当作已经执行了所有点的运动。
4. 检查开区间及端部完成、ambient homeomorphism/允许过程的保持性，避免再将内在同胚与外在固定端部条件混为同一关系。
5. 通过匹配语义的kernel与完整本地证据门禁后才交付数学结论；若需将几何结果用于HoTT实例，另闭合保真接口。

当前没有下载整个mathlib归档/编译缓存，没有运行该几何入口；未证明原M/N复原或HoTT缺陷。全部仍属于原持续Goal，不以本资格说明结束它。
