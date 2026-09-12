# HoTT 工作治理 · v1.2.0

项目入口：根AGENTS。行动入口：[SKILL](skills/hott-paradox-research/SKILL.md)。完整协议：[PROTOCOL](cognition/PROTOCOL.md)。

本版的关键不是多一份说明，而是动态闭环：LOAD_SET固定认知职责，STATE展开最新会话/当前候选/待核问题/依赖；每次全文重读当前内容。里程碑和收工前写回MEMORY等，并原子发布新HEAD。下次Session自然读取新的文件集合，不依赖聊天记忆。

[MEMORY](../MEMORY.md)、[FRONTIER](research/hott/FRONTIER.md)、[LESSONS](research/hott/LESSONS.md)、[RESUME](research/hott/RESUME.md)都是实际当前文件，不是模板。旧版本和变更前字节在history，数学原文不因治理而改。

[工具](skills/hott-paradox-research/scripts/cognition_runtime.py)只管文件/版本/引用；[测试](skills/hott-paradox-research/checks/test_cognition_runtime.py)只作机械验证。宿主自动加载和独立Fresh理解尚未测试。当前官方原生技能发现路径未必是.codex，本项目用根AGENTS显式路由；不修改全局宿主设置，也不声称自动注入全文。

新会话在可读这个目录的环境中执行：先读AGENTS，按Skill完整加载，再接RESUME。新挂载缺件可从用户包恢复精确文件，禁止覆盖较新内容。没有后台运行。
