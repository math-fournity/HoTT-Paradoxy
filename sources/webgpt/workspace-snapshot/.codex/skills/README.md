# Skill 名称与职责（治理 v1.3.0）

| 名称 | 角色 | 指称与入口 |
|---|---|---|
| **hott-session-governance** | 治理 Skill | 管每次全文恢复、版本/依赖、证据分层、里程碑保存、回读与交接。 [SKILL](hott-session-governance/SKILL.md) |
| **hott-paradox-research** | 业务 Skill | 管 HoTT 悖论的构造、证明、反模型、自主调度与结论范围。 [SKILL](hott-paradox-research/SKILL.md) |

唯一机器角色表是 [SKILL_ROLES.json](SKILL_ROLES.json)，根 AGENTS 统一路由。用户说“继续 HoTT 研究”即在同一次调用中先完成治理入口，再执行业务；结束回到治理保存。用户仅让审计治理则不自动研究数学。

不需要每次分别 @ 两个 Skill。这里的自动是守协议的文件读取和行动路由，不是已安装宿主钩子或会话外后台程序。新增治理 Skill 必须有独立职责和实际需求，不为形式完整拆出许多相同入口。

为兼容旧路径，既有加载/checkpoint 引擎仍在业务 Skill 的 scripts/cognition_runtime.py；语义所有权由治理 Skill 与 PROTOCOL 拥有，不复制第二套引擎。
