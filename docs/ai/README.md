# AI / 模型与轨迹证据

本项目Goal任务现由root AGENTS与[任务角色路由](../../.codex/cognition/TASK_ROUTING.md)接入；第三轮执行/审计Skill、
单体Goal6闭包与短提示词见[第三轮入口](../../第三轮机器统观/README.md)。最高指示作为全Session完整输入，研究、
审计、治理、机械任务分别消费；加载计划/静态检查不认证实际认知。方法与边界见[治理化方案](../../dev-docs/Goal任务项目治理化与全局复用方案-20260923.md)。

三类 AI 的 role、可见性和 trajectory 证据合同见 `.codex/skills/`、`audit/` 和历史 WebGPT 快照；隐藏推理不作为证据。

当前 AI 的数学结论交付行为受根 `AGENTS.md` 的 `MATH_PROOF_BEFORE_DELIVERY_V1` 和 `docs/quality/数学结论机器证明与证据留存规范.md` 约束；Prompt/Skill 中出现“机器证明”不证明实际调用了 proof assistant，必须回到 repo 内 source/run/index 实物。
