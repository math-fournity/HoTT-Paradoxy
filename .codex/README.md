# 顶层 repo 的本地 Codex 治理资产

| 组件 | 唯一职责 |
|---|---|
| `AGENTS.md` | 本地路由和不可漂移边界 |
| `skills/hott-local-session-governance/SKILL.md` | 启动、全文 core、动态状态、session、恢复和结束回评 |
| `skills/hott-paradox-research/SKILL.md` | HoTT 悖论研究业务方法和证据边界 |
| `cognition/LOAD_SET.json` | 固定全文入口和动态状态路由 |
| `cognition/PROTOCOL.md` | 可执行的读入、写回、checkpoint 和失败合同 |
| `research/hott/STATE.json` | 当前状态、开放依赖和 session 路由唯一机器 owner |
| `tools/cognition_runtime.py` | 相对路径、snapshot、完整读出、乐观 checkpoint 的机械实现 |
| `verification/` | 本地治理和历史覆盖验证结果 |

WebGPT 的原始治理资产不与当前 owner 混写，完整快照位于 `sources/webgpt/workspace-snapshot/.codex/`。
