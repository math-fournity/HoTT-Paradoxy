# 实数拓扑圆模型的来源与工具链资格化

目标是为GEO-01/02提供真正的实数拓扑圆去点、开区间及端部/环境模型；普通Lean几何结论不会直接冒充原生HoTT结论。C-265已闭合内在同胚，端部/环境与原操作仍开放。本文件拥有来源与环境证据，结论正文见[第四轮报告](../../Astra继续尝试/断点与证明机制系统检查/第四轮执行报告.md)。

## 已取得的直接事实

- 本机已有Lean 4.34.0，实际binary输出commit `293d5d0c0c3f3dded4688b3ccd6a33939ac5102b`、arm64-apple-darwin。
- 官方mathlib4标签v4.34.0解析为 `5ed2965256430c3649e86755f9576b54eca72435`，其lean-toolchain恰为`leanprover/lean4:v4.34.0`。
- 已按该commit保存`Sphere.lean`、lean-toolchain与Apache 2.0 LICENSE，路径、URL、hash见[SOURCE.json](SOURCE.json)。不是只保存一个会随master变化的文档链接。
- 已实际实例化stereographic'的source/target并组合为去点圆到Ioo(0,1)的同胚，显式点/逆律/连续性检查通过；源码见`HoTT/formal/astra-real-geometry/PuncturedCircle.lean`，当前run为`20260920-MP-ASTRA-REAL-CIRCLE-001-02`。官方[Sphere模块](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/Instances/Sphere.html)只作来源导航，当前依据为固定本地版本和实际运行。
- 已查的两个旧候选项目没有实际mathlib依赖目录：formal-qkd虽登记mathlib但锁Lean4.27.0-rc1；verified-ledger没有mathlib。不能冒称已具备本轮几何运行环境。

## 已执行与下一实际步骤

1. 已按外置大文件Skill在D盘下载并解压固定源，8个依赖exact锁定，2568个官方master缓存对象取得并解包。默认CDN403及官方Azure备用成功分开留证，没有关闭TLS或使用fork缓存。
2. 已在HoTT/formal的独占几何目录创建真实Lean入口，以实数二维空间中的单位圆为对象，实例化source/target与连续双逆。当前C-265双校验通过，证据见DELIVERY.json。
3. 明确经典选择/非计算定义与实际程序/物理动作的区别；stereographic'使用线性等距识别，不能把声明的homeomorphism当作已经执行了所有点的运动。
4. 检查开区间及端部完成、ambient homeomorphism/允许过程的保持性，避免再将内在同胚与外在固定端部条件混为同一关系。
5. 通过匹配语义的kernel与完整本地证据门禁后才交付数学结论；若需将几何结果用于HoTT实例，另闭合保真接口。

当前已完成C-265及真实checkpoint178；未证明原M/N的端部/环境保留复原、物理过程或HoTT缺陷。全部仍属于原持续Goal，不以底层同胚结束它。
