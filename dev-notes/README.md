# dev-notes 对话原文归档

本目录保存历史问答。当前Codex归档入口是[dev-notes-archive Skill](/Users/aurolafly/.codex/skills/dev-notes-archive/SKILL.md)，新问答由其 `prepare → commit` 流程自动分配编号、复用Session文件并校验原文。编号是文件定位信息；文件日期、Session与turn身份另行保留。

自 2026-10-04 的用户裁定起，本目录的当前 Skill 归档不能只停留在 working tree：main Agent 必须先保存
`git status --porcelain=v1 --untracked-files=all -- dev-notes` 基线，再对 helper receipt 返回、且没有既有 delta
也未被 ignore 的**单一** note 执行 `git add -- <note>` 和
`git commit --only -m 'archive: record dev notes' -- <note>`。提交后新 HEAD 只能包含该 note，且 note 必须 tracked/clean；
禁止 `git add -A`、无路径 commit、混入其它 Session 的归档、tag、push、发布或分享。存在预先 delta、Git失败或不应
进入 Git 的敏感正文时，如实保留 `ARCHIVED_NOT_VERSION_CLOSED`，不能以 broad commit 假装完成。

这使归档进入本地 `dev` 历史；它不改变本项目的发布边界：`main` 仍只由发布构建过程生成结论与证据，不携带
`dev-notes/` 的过程性对话内容。归档仍是 pre-final 草稿投影，而非 Host UI 的事后收据。

2026-09-20修复了17组历史重复编号，并从既有完整暂存补录31轮问答。旧编号、标题与新文件的对照，以及正文哈希、恢复记录和两份未补录材料的原因，见[修复记录](../audit/dev-notes-recovery-20260920/README.md)。

本线程当前归档为[0093](<0093 - 2026-09-19 - 另外一个AI正在为你的审计报告增加索引，这不应该影响你继续工作.md>)。补录是原pre-final暂存投影，不自动证明当时界面显示字节，也不意味着此前未留下暂存的轮次均已恢复。
