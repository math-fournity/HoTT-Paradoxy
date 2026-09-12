import os

scripts_dir = os.path.join(os.getcwd(), 'scripts', 'governance')
os.makedirs(scripts_dir, exist_ok=True)
script_path = os.path.join(scripts_dir, 'r018_update_zlaw_closure.py')

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(script_content)

result = subprocess.run(['python3', script_path], capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("stderr:", result.stderr)
