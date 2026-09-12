#!/usr/bin/env python3
"""Apply this turn's explicit code retention and local Git authorization."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[2]
p=root/'AGENTS.md';old=p.read_text();marker='## 最高目的与第一动作'
addition='''## 代码保全与本地 Git（用户2026-09-10本轮明确授权）

本轮用户要求：过程代码不得丢弃，回收到工作目录 `scripts/`，工作目录使用Git管理，最终打包。授权范围为当前沙箱工作副本的本地版本管理和研究执行，不包括远端push、部署、改模型或其他AI。

- 今后新写的研究实验、回收/打包/验证/状态更新工具，先保存到根 `scripts/` 再运行。临时探索随后实际采用时也应落为可复用脚本；不能仅留在会话工具单元。
- 历史原路径不移动、不删除。可在 `scripts/recovered/` 保存逐字节副本，并用来源路径、SHA-256和版本映射回原件。不同内容的同名代码不得覆盖；未找到的代码明确缺失，禁止重构后冒充原实验。
- 每项实际运行保存源码/输入身份、argv或入口、cwd、stdout/stderr、退出码、时间与适用范围。恢复代码不是代码已安全审查或已复现，不批量执行未知来源。
- 当前目录已有真实本地 `.git` 后，用真实HEAD/branch/status检查。里程碑和最终交付本地commit，保持checkpoint与Git两种状态互补；Git提交不是数学证书。
- 最终包包含脚本、必要输入、原始结果、研究记录和可恢复Git历史。先检查工作树干净和Git完整性，再制包并回读；不承诺跨会话自动后台运行。

'''
if addition in old:raise SystemExit('Policy already present')
assert marker in old
p.write_text(old.replace(marker,addition+marker,1))
(root/'artifacts/code-recovery/POLICY_CHANGE.json').write_text(json.dumps({'path':'AGENTS.md','old_sha256':hashlib.sha256(old.encode()).hexdigest(),'new_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'authorization':'User explicitly requests preserving scripts, Git management and continuing work','base_git':'checkpoint-rev15-import','no_original_research_source_rewritten':True},ensure_ascii=False,indent=2)+'\n')
print('Added code retention and local Git policy to root AGENTS; original paragraphs retained')
