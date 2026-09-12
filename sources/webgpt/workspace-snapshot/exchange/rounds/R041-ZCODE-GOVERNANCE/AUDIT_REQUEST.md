# 增量审计请求

请审计本轮新增或修改内容；不要把接收文件当作认可。

## 重点问题
1. `governance/ZCODE_INTEGRATION.md` 对 ZCode 产品事实（两级 AGENTS 组合、Skill 限制、Hook/Memory 边界、无 CLI/ACP）的表述是否与本机权威库 `/Users/aurolafly/zcode` 一致、有无夸大宿主能力或自动加载语义。
2. 新增文档是否保持单真值源：未复制可变状态、未改动 `.codex` 原引擎与 LOAD_SET、未声称自动加载认证。
3. RTK 输出过滤警告的对策（`rtk proxy` / 内置 Read）是否足以保证全文加载语义；是否有遗漏的宿主侧截断风险。
4. checkpoint（revision 40→41）五文档同步是否逐值保留旧记录，新 Session 依赖登记是否完整。

## 理论配置与机器证据范围
本轮无数学理论与机器证明内容；验证仅限文件/清单/Git 层：`verify_package.py` PASS、`git fsck/status/rev-parse`、`govern.py plan/install-entry` 实际运行（RUNS.json）。原生证明助手 NOT_RUN。

## 治理修改
新增 `governance/ZCODE_INTEGRATION.md`、`.zcode/HOTT_ENTRYPOINT.md`（经官方 install-entry）；MEMORY/FRONTIER/LESSONS/RESUME/STATE 经唯一引擎 checkpoint 更新（revision 41）；未修改 AGENTS.md、PATHS.json、LOAD_SET.json、原两 Skill、PROTOCOL 与任何数学语料。包外层新增 `onboarding/RECEIVER_ACK.md`（不入 Git）。
