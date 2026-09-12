import subprocess
from pathlib import Path

# 找到刚才写入的脚本并执行
current_dir = Path.cwd()
root_dir = current_dir
for _ in range(5):
    if (root_dir / 'AGENTS.md').exists():
        break
    root_dir = root_dir.parent
else:
    root_dir = Path('/mnt/data/HoTT_workspace_rev16')

script_path = root_dir / 'scripts' / 'governance' / 'r017_update_closure.py'

result = subprocess.run(['python', str(script_path)], capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("Error:", result.stderr)
