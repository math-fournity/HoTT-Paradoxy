# GitHub 对接与 LFS 迁移证据（2026-09-26）

> 事件：本 repo 于 2026-09-26 对接 GitHub 远程 `https://github.com/math-fournity/HoTT-Paradoxy`（裁定 35）。`archive/objects.pack`（206,914,914 字节）超过 GitHub 单文件 100MB 硬限制，经用户决策（路径 A）执行 `git lfs migrate import --everything --include="archive/objects.pack"`。

## 发生了什么

- 迁移重写了 **644 个提交**（自仓库原始根提交起的全部历史）：`archive/objects.pack` 在每个提交中变为 LFS 指针，`.gitattributes` 增加 `archive/objects.pack filter=lfs diff=lfs merge=lfs -text`。
- 所有 `refs/heads/*` 与 `refs/tags/*` 均已重写指向新历史；工作区文件由本地 LFS 存储恢复（217,002,151 字节，`git lfs fsck` OK）。
- **`refs/codex/turn-diffs/checkpoints/*` 检查点 ref（约 263 个，Codex checkpoint 事务留痕）未被迁移重写**，仍指向改写前历史。它们只存在于本地、不会被推送；其留证价值按原身份保留。

## 哈希解读规则

**本 repo 各文档中登记的提交哈希（总索引 §5、audit 记录、claim 记录等）一律是"改写前引用"。**解析到当前历史用本目录的映射：

| 文件 | 内容 |
|---|---|
| `COMMIT_MAP.csv` | 642 对 `pre_migrate_sha → post_migrate_sha`（含 1 个同日期同标题键，已按父链消歧） |
| `REF_MAP.csv` | 各分支/标签 tip 的新旧对照 |
| `pre-migrate-history.txt` | 迁移前全 ref 历史清单（生成于 HEAD `7f2f7dc7`） |
| `post-migrate-history.txt` | 迁移后全 ref 历史清单 |

补记：`fa05d43b`（"evidence: pre-migration history listing…"，迁移前最后一笔）是在备份之后、清单生成之后创建的，不在 COMMIT_MAP 中；其改写后哈希为 `90d559d1`。故完整覆盖为 643/643。

关键对照（查证用）：

- `7f2f7dc7`（records: git remote and identity ruling 35）→ `36dbf7b3`
- `685878ce`（Merge GitHub initial commit (LICENSE)）→ `2134ee6f`
- `ba732f2d`（GLM workspace and shared-truth registration）→ `30f6a54d`
- tag `governance-v4.0.0`：`067c844d` → `7f6a4d7a`

## 备份

迁移前的完整历史（含原始 blob）保存在本地裸仓库 **`/Volumes/D/HoTT-pre-lfs-backup-20260926`**（349MB，未推送）。该备份是本次改写的回退点与原始 blob 的独立副本；其保存与最终处置由用户决定。

## 备份覆盖范围（2026-09-26 全量推送后）

**GitHub（`math-fournity/HoTT-Paradoxy`，private）已有**：全部 5 个分支（`main`、`codex/astra-proof-wiring-snapshot-20260919`、`codex/astra-restoration-snapshot-20260919`、`codex/semantic-overview`、`feat/machine-overview-m1`）、全部 9 个 governance tag、LFS 对象（`archive/objects.pack`，217MB）——即本 repo 的**全部常规 git refs 与可达对象**。

**仅本地、不推送**（按设计）：

1. **19 个 `refs/codex/turn-diffs/checkpoints/*` 检查点 ref**：指向改写前历史，其中含原始 206.9MB 常规 blob（GitHub 硬拒绝）；重写它们会摧毁"指向改写前哈希"的留证身份。已复制进本地裸备份（19/19），持久性不依赖工作仓库。
2. **可再生构建产物**：`*.agdai`、`__pycache__/`、`.DS_Store`（.gitignore 排除，按设计）。

**Git 之外三块的处置（2026-09-26 用户决策后完成）**：

- `AI对话录/`（独立 git repo，master）→ 私有仓库 `math-fournity/HoTT-Paradoxy-dialogue`（全历史凭据扫描 106 blob 0 命中后推送）。
- `workspace/`（独立 git repo，main + 2 tag）→ 私有仓库 `math-fournity/HoTT-Paradoxy-workspace`（1883 blob 0 命中）。
- `private-audit/`（原始 model-io，治理禁止入 Git）→ 加密归档 `/Volumes/D/HoTT-private-audit-backup-20260926.tar.gz.enc`（AES-256 + PBKDF2，20.8MB，42 文件逐字节比对一致）；解密口令存于本机登录钥匙串（服务名 `HoTT-private-audit-backup-20260926`，`security find-generic-password -a math-fournity -s HoTT-private-audit-backup-20260926 -w` 取回）。口令本身不落盘、不入对话记录。

结论：GitHub 侧 = 主 repo 完整镜像 + 两个独立历史 repo；本地备份盘 = 改写前历史裸备份 + 检查点 ref + private-audit 加密归档。三层合起来构成完整备份；`private-audit` 的明文仍只有工作盘一份，其异地副本是加密态。
