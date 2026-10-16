#!/bin/sh
# 在你自己的机器上运行（那里的 git 有权限推标签到 math-fournity/HoTT-Paradoxy）。
#
# 背景：云端会话的 git 通道只放行分支推送，refs/tags/* 的推送被它以 HTTP 403 拒绝，
# 所以 Cloud-Opus 会话里打的两个附注标签只存在于云端容器，没有到达远端，也不会出现在你的机器上。
# 这个脚本在你的机器上用同样的说明文字重新打出这两个标签（指向同样的两个提交），然后推送。
# 两个提交都已经在远端（是 main 的祖先），标签说明文字逐字取自云端容器里的原标签。
#
# 标签指向的是打标签当时的提交，不是最新提交：
#   Cloud-Opus对GLM的审计  ->  df7e256085e3b6720ce3941ce222fb28a4122b6d  （D1–D6 交付与终局轮之后）
#   Cloud-Opus工作完成     ->  5dbd8561727d39115292599a4494b53dc9b43e79  （两份社区审计稿与根 README 之后）
# 入核、登记和 Lean 自查补强发生在它们之后。如果你希望"Cloud-Opus工作完成"指向最新状态，
# 把下面第二个 git tag 命令里的提交号换成远端分支的最新提交即可。
set -eu
cd "$(git rev-parse --show-toplevel)"
git fetch origin main claude/charming-pasteur-mvzlio
D="Cloud-Opus审计并补完GLM/附件/标签"
git tag -a "Cloud-Opus对GLM的审计" -F "$D/Cloud-Opus对GLM的审计.tag-message.txt" df7e256085e3b6720ce3941ce222fb28a4122b6d
git tag -a "Cloud-Opus工作完成"    -F "$D/Cloud-Opus工作完成.tag-message.txt"    5dbd8561727d39115292599a4494b53dc9b43e79
git push origin "refs/tags/Cloud-Opus对GLM的审计" "refs/tags/Cloud-Opus工作完成"
