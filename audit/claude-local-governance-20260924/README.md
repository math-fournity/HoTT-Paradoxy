# Claude Code项目本地治理方案的取证

2026-09-24；T1 / GOVERNANCE_ALIGNMENT；一次性派生证据，不是第二份研究数据库或Claude安装收据。

方案入口：[Claude Code项目本地治理安装方案](../../dev-docs/Claude-Code项目本地治理安装方案-20260924.md)。

- `capture_static.py`：唯一producer；只读源/版本/配置安全字段并写入一个新证据目录，不启动模型、不安装、不checkpoint、不修改Git。
- `run-001/source-inventory.json`：作者声明全文审阅的66个物理文件及捕获时SHA/bytes/lines。不能由哈希认证模型阅读、理解或数学。
- `run-001/host-path-hits.json`：71文件、162行宿主/路径候选；派生检索，不替代语义审阅。
- `run-001/git.json`：捕获时root/common-dir/HEAD/branch/index/dirty/tag；他人继续变化不属于本任务。
- `run-001/state-hot.json`：时点热字段，不是新的current owner。
- `run-001/*-plan.json`与`*-plan-command.json`：canonical只读plan及原始命令结果；`plan-summary.json`是其派生体积摘要。
- `run-001/claude-version.json`、`claude-safe-config.json`：版本和非敏感配置投影；未复制认证文件或环境变量值。
- `run-001/legacy-manifest-check.json`：旧1.3.3 manifest的19项中7项失配；没有重写旧收据。

正文审阅、官方调研与未来适配裁决由方案第001/002片拥有。原始官方`.md`批量下载返回HTTP403，改用内置web可读页面；没有制作或宣称完整官方离线镜像。

实际未执行：Claude模型会话、fresh/compact行为、项目安装、研究/数学proof、checkpoint apply、Git commit/tag/push。全局既有安装器verify在本轮返回20文件PASS，原始结果另保存在`global-verify.json`。
