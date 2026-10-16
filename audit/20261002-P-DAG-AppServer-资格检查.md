# P-DAG App Server 资格检查

> **身份：** `HOST_CAPABILITY_SOURCE_INSPECTION / NOT_A_WORKER_SMOKE / NO_HOST_MUTATION`。
>
> **结论：** `APP_SERVER_PERMISSION_FORWARDING_NOT_QUALIFIED`。本机 Codex App Server schema 支持动态 thread/turn、model、effort、sandbox 和 approval fields；当前共享 broker 的 Codex adapter 尚未把 `sandbox` 转发到 `thread/start`，因此在获得实际 read-only/never 回显前，P-DAG 不以它启动研究 worker。

## 已检查范围

| 对象 | 可观察事实 | 范围 |
|---|---|---|
| `codex-cli` | `codex-cli 0.157.0`；`codex app-server` 提供 `daemon`、`proxy`、schema/TS generation | 本机当前命令面 |
| App Server schema | `ThreadStartParams` 有 `model`、`sandbox`、`approvalPolicy`；`TurnStartParams` 有 `model`、`effort`、`sandboxPolicy`、`approvalPolicy` | `/tmp/codex-appserver-schema-20261002/ClientRequest.json` 的本次生成物 |
| shared broker | `CodexAppServerAdapter.new_session()` 向 `thread/start` 传 `cwd`、`ephemeral`、`model`，并只透传 `permissions`、`approvalPolicy`、`serviceTier`、instructions；未透传 schema 的 `sandbox` | `/Users/aurolafly/codex/tools/agent_session_broker.py` 的本次只读源码定位 |
| turn control | adapter 使用 `turn/start`，会传 selected effort；worker lifecycle 由 shared broker 的 Codex App Server facade 承担 | 同一源码范围 |

## 判词理由

P-DAG 的任务授权要求每个研究 worker 为 read-only、approval=`never`。App Server 本身具有配置字段不证明共享 broker 的 Codex facade 在本机当前版本将该字段传入、也不证明 thread/turn 实际回显了该权限。未经资格化就启动 worker，只能靠 prompt 声称“只读”，不满足 NodeCard 的环境权限条件。

因此，本轮只使用已可见地显示 `sandbox: read-only`、`approval: never`、`model: gpt-5.6-terra`、`reasoning effort: max` 的 fresh CLI lane 完成 `P-DAG-BATTLE-001`。没有启动 App Server worker、没有改 `/Users/aurolafly/codex`、没有改用户 Codex config、没有创建 token/socket、没有进行网络或外部系统动作。

## 重新资格化条件

要启用 App Server dynamic-worker lane，必须至少完成：

1. 在共享 broker 或经过审查的 project adapter 中把 `sandbox`／`sandboxPolicy` 和 `approvalPolicy` 精确转发；
2. 用 exact `gpt-5.6-terra / max` 启动无害 read-only thread，并保存 model/effort/sandbox/approval 的实际回显；
3. 通过 observer ACL、private wire、cancel→terminal／force-stop 与 worker/session cleanup smoke；
4. 将共享工具的任何修改按其所在 `/Users/aurolafly/codex` 主库的独立治理、验证和用户授权处理。

未满足以上条件前，本判词不说 App Server 不能用；只说它尚未有资格承担本项目的 P-DAG read-only research worker。
