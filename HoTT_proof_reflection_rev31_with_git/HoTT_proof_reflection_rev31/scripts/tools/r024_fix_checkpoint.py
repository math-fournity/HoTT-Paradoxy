"""Repair a recorded transcription typo; preserve failed source and actual retry log."""
from pathlib import Path
from datetime import datetime, timezone
import ast
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / 'scripts/session/r024_checkpoint.py'
OLD = "{'path:k,'text:v,'expected_sha256':"
NEW = "{'path':k,'text':v,'expected_sha256':"

def main() -> None:
    data = TARGET.read_bytes()
    text = data.decode('utf-8')
    if text.count(OLD) != 1:
        raise ValueError('Expected exactly one known malformed dictionary literal')
    backup = ROOT / 'scripts/recovered/r024/checkpoint_initial.py'
    backup.parent.mkdir(parents=True, exist_ok=True)
    if backup.exists():
        raise FileExistsError(backup)
    backup.write_bytes(data)
    corrected = text.replace(OLD, NEW)
    ast.parse(corrected, filename=str(TARGET))
    TARGET.write_text(corrected, encoding='utf-8')
    evidence = ROOT / 'artifacts/r024'
    record = {
        'status': 'SOURCE_TYPO_REPAIRED_BEFORE_ANY_CHECKPOINT_EXECUTION',
        'original_path': str(TARGET.relative_to(ROOT)),
        'failed_source_copy': str(backup.relative_to(ROOT)),
        'failed_source_sha256': hashlib.sha256(data).hexdigest(),
        'error': 'SyntaxError at line 181: malformed path/text keys in payload dictionary',
        'provenance': 'Recorded from actual previous tool invocation; no runtime writes from that failed script',
        'corrected_sha256': hashlib.sha256(TARGET.read_bytes()).hexdigest(),
        'repaired_at_utc': datetime.now(timezone.utc).isoformat(),
    }
    (evidence / 'CHECKPOINT_INITIAL_FAILURE.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    argv = [sys.executable, '-B', str(TARGET)]
    started = datetime.now(timezone.utc).isoformat()
    proc = subprocess.run(argv, cwd=ROOT, text=True, capture_output=True, timeout=90)
    execution = {'argv': argv, 'cwd': str(ROOT), 'started_at_utc': started,
                 'finished_at_utc': datetime.now(timezone.utc).isoformat(),
                 'exit_code': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr}
    (evidence/'CHECKPOINT_EXECUTION.json').write_text(json.dumps(execution, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(execution, ensure_ascii=False, indent=2))
    if proc.returncode:
        raise SystemExit(proc.returncode)

if __name__ == '__main__':
    main()
