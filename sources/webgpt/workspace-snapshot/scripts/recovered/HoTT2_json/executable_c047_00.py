import subprocess
import os

script_path = os.path.join(os.getcwd(), 'scripts', 'governance', 'r018_update_zlaw_closure.py')
result = subprocess.run(['python3', script_path], capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("stderr:", result.stderr)
