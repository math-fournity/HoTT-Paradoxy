# 增量研究与审计交换协议 · v1.0

## 目标、目录和单一权威

默认交流总目录是项目根下 **exchange/**，与任何厂商目录无关。每次单独目录：`exchange/rounds/<round_id>/`。正式数学正文仍保存在已有研究记录路径，程序在 scripts/，运行数据在 artifacts/。交流记录指向这些证据，不创建第二套结论真值。

- `rounds/`：用户原请求、增量研究记录、精确依赖、实际执行账本、审计问题；必须 Git 跟踪。
- `outbox/`：用户要求时导出的 ZIP 和导出收据；不入 Git，避免 ZIP 包含自己。
- `inbox/`：实际收到的原始审计包；不自动执行、不自动应用。重要审计原文经审查复制到 `audits/` 后入 Git。
- `audits/<audit_id>/`：实际审计原文、结果、目标包 SHA、base/head、逐条接受/拒绝理由和后续证据。未收到不得创建假回信。
- `templates/`：模板，不是执行成果。

## 每轮最小记录

`REQUEST.md` 保存原请求；`RESEARCH_DELTA.md` 说明旧状态、本轮实际动作、正反结果、数学/实现/现实桥梁分别到哪一步、失败与受影响结论；`AUDIT_REQUEST.md` 指定待审问题；`RUNS.json` 记录实际 argv/cwd/工具版本/源码输入哈希/stdout/stderr/退出码，未运行写 NOT_RUN；`ROUND.json` 绑定唯一 round_id 与 base_commit。

初始化：

```bash
python3 -B scripts/handoff/delta_tool.py round-init --id R041-EXAMPLE --request-file <用户原请求文件> --base handoff-r040
```

这里只创建模板，不启动研究、不自动生成证明。填写实际内容，完成原治理 checkpoint 和本地 Git commit 后，用户说“把本轮增量交给 Astra 审计”时执行：

```bash
python3 -B scripts/handoff/delta_tool.py export --round R041-EXAMPLE
```

生成 `exchange/outbox/R041-EXAMPLE.zip` 和 `.receipt.json`，将 ZIP 交给用户，**不通过任何账号自动发送**。

## 基线：不能把“已发送”当成“已确认”

首次基线是不可移动的标签 `handoff-r040`，实际 commit 在完整交接包的 manifests/HANDOFF_IDENTITY.json 中。后续优先使用双方真实确认的准确 commit SHA；接收方未保存中间增量时，继续从共同已知基线导出累计净增量。`--base` 可以显式指定已确认基线，但必须与 ROUND.json 一致，不得在导出时悄悄改掉。

一次增量必须满足 base 是 head 的祖先。发送成功、文件验收成功、数学审计认可和修改合并不同。审计员意见不是用户授权；不得为了通过审计重写旧日志、旧原话或事后伪造实验。

## ZIP 的精确定义

本协议只导出已提交、干净工作树的差量。未提交、新建未跟踪的研究资料会使导出失败。原工具忽略的缓存/虚拟环境不是研究证据，不能往那里藏运行成果。

ZIP 包含：

1. `MANIFEST.json`：协议、轮次、base/head commit和tree、每一包成员的 SHA-256/长度、审计状态 NOT_AUDITED。
2. `BASE_SNAPSHOT.json` 与 `HEAD_SNAPSHOT.json`：全量路径/模式/哈希目录，不携带全部旧内容。
3. `CHANGES.json`：新增/修改/删除及前后哈希；重命名按删除＋新增，避免含糊检测。
4. `payload/`：仅新增和修改后的文件字节；删除只有清单，不伪造空文件。
5. `changes.patch`：可读的完整差分（含二进制差分）；不是自动执行脚本。
6. `commits.bundle`：仅 base 之后的 Git 对象和历史，恢复时需要准确基线。
7. README：审计范围和安全入口。

同时携带 patch、payload和薄bundle用于交叉核对，不意味着包含全量旧项目。文件哈希不是签名，不能认证作者或数学真理。当前v1支持 Git SHA-1仓库、普通/可执行文件，拒绝symlink、submodule、跨平台大小写冲突、不安全路径、重复ZIP成员；这些情况需要显式迁移而非静默丢弃。单次解压总量上限512MiB，超过时拆分真实工作批次或明确建立新全量基线，不能任意删证据。

## Astra／其它审计员接收

必须用**已信任基线中的工具**验证新包，不先执行新包里的脚本：

```bash
python3 -B scripts/handoff/delta_tool.py verify /path/to/R041-EXAMPLE.zip --with-base
python3 -B scripts/handoff/delta_tool.py stage /path/to/R041-EXAMPLE.zip --destination /path/to/new_isolated_audit_workspace
```

`stage` 要求调用方根的 HEAD 精确等于 base；若当前工作已前进，先另建该 base 的独立检出。它只克隆到不存在的新目录，再验证bundle、完整前后清单与检出字节，**不覆盖活动研究目录**，不自动运行研究代码、钩子、测试或合并。

验收不等于审计。审计应先读当次原请求与差量，再沿依赖回到共享基线，分别判断数学主张、模型对应、程序行为和治理变化。若依赖的旧全量包缺失，报告 NEED_BASELINE，不猜补。

## 审计后采用

只存真实回信，记录其针对的 ZIP SHA、head commit、结论与限制。逐项接受或拒绝并给理由；需要改动时新建 Session/commit，保留失败版本。下一基线只有在用户和审计双方确实保存了同一版本时才更新；导出工具不自动推进基线。跨机器没有分布式锁，分支分歧不能靠“最后写者”覆盖。
