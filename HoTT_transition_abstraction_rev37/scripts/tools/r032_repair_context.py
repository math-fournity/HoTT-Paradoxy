from pathlib import Path
import json
root=Path(__file__).resolve().parents[2]
p=root/'scripts/tools/r032_context.py'
s=p.read_text()
s=s.replace("if (ROOT/rel).read_bytes()!=data: raise RuntimeError('Restoration mismatch: '+rel)","if rel != '.git/index' and (ROOT/rel).read_bytes()!=data: raise RuntimeError('Restoration mismatch: '+rel)")
p.write_text(s)
(root/'artifacts/r032/INITIAL_RESTORE_FAILURE.json').write_text(json.dumps({'error':'Restoration mismatch: .git/index','cause':'git status refreshed index stat cache after unzip; source content comparison retained for all other archive files','repair':'Exclude volatile .git/index byte identity only; verify git status/fsck/object history separately; failed script and partial plan retained'},indent=2)+'\n')
