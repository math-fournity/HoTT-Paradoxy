import os
from pathlib import Path

current_dir = Path.cwd()
root_dir = current_dir
for _ in range(5):
    if (root_dir / 'AGENTS.md').exists():
        break
    root_dir = root_dir.parent
else:
    root_dir = Path('/mnt/data/HoTT_workspace_rev16')

# 查看认知闭包目录下的内容，排查为什么找不到
closure_dir = root_dir / "认知闭包"
print("Directory exists:", closure_dir.exists())
if closure_dir.exists():
    print("Files in directory:")
    for f in closure_dir.iterdir():
        print("-", f.name)
else:
    # 也许因为中文路径问题，或者之前解压的路径不同
    print("Looking for root structure:")
    for f in root_dir.iterdir():
        print("-", f.name)
