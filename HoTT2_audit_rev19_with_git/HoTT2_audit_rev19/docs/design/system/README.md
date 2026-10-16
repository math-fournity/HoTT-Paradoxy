# System Design

职责：组件边界、拓扑、数据/状态生命周期、外部依赖、失败域和非功能取舍。

当前是文件型研究系统：`aistudio-docs/` 为原始归档，`proofs/` 为其他 AI 整理证明，`dev-docs/`
为过程文档，`HoTT/` 为当前专题，`HOTT_Z_AI_HANDOFF_20260831/` 为只读外部 AI 交接快照。原始
归档与派生检索层分离：`HoTT/sources/aistudio-discussions/` 是从两个权威源根生成的不可变逐字视图，
只负责发现和回源，不能反向成为数学真值或替代原始文件。

根 README 拥有组件路由；`HoTT/sources/user-originals/` 拥有用户逐字原意；
`HoTT/Z_LAW_REALITY_RELATIVE_PARADOXES.md` 拥有当前 Z/现实相对悖论；
`HoTT/INTRINSIC_TEMPORALITY_OF_HOTT.md` 拥有具体时间分层；总审计和主张矩阵拥有数学边界；代码和
运行收据拥有实现/验证事实。未来 Session 的交接通过这套 living owner + 启动路由完成，不再建立
第二个 current handoff 压缩包。逐字语料的生成、不可变 generation、原子 `CURRENT`、故障恢复与
删除边界见 `../../../HoTT/sources/aistudio-discussions/README.md` 和 ADR-003。首次增加数据库、服务
或其他跨组件 API 时再扩展系统设计。
