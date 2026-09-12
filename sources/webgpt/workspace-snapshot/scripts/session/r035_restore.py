"""Restore the user-provided R034 archive without overwriting its source mount."""
from pathlib import Path, PurePosixPath
import hashlib, json, stat, subprocess, sys, zipfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = Path('/mnt/data/HoTT_path_certificate_rev34_with_git.zip')
PREFIX = 'HoTT_path_certificate_rev34/'
EXPECTED = '14aa846b39189e70e8e0e24299281392dec6812b'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    baseline = {}
    with zipfile.ZipFile(ARCHIVE) as archive:
        if archive.testzip() is not None:
            raise RuntimeError('Archive CRC failure')
        for item in archive.infolist():
            if not item.filename.startswith(PREFIX):
                raise RuntimeError(f'Unexpected root: {item.filename}')
            rel = item.filename[len(PREFIX):]
            if not rel:
                continue
            p = PurePosixPath(rel)
            mode = item.external_attr >> 16
            if p.is_absolute() or '..' in p.parts or stat.S_ISLNK(mode):
                raise RuntimeError(f'Unsafe archive path: {rel}')
            target = ROOT.joinpath(*p.parts)
            if item.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            data = archive.read(item)
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and target.read_bytes() != data:
                raise RuntimeError(f'Refusing overwrite: {rel}')
            target.write_bytes(data)
            if mode & 0o111:
                target.chmod(0o755)
            if '.git' not in p.parts:
                baseline[rel] = sha(data)
    def git(*args):
        p = subprocess.run(['git', *args], cwd=ROOT, text=True, capture_output=True, check=True)
        return p.stdout.strip()
    head = git('rev-parse', 'HEAD')
    if head != EXPECTED:
        raise RuntimeError(f'Unexpected HEAD: {head}')
    out = ROOT / 'artifacts/r035'
    out.mkdir(parents=True, exist_ok=True)
    record = dict(schema='r035.restore.v1', utc=datetime.now(timezone.utc).isoformat(),
                  root=str(ROOT), source=str(ARCHIVE), source_sha256=sha(ARCHIVE.read_bytes()),
                  expected_head=EXPECTED, actual_head=head, branch=git('branch', '--show-current'),
                  remotes=git('remote', '-v'), source_files=baseline,
                  original_archive_not_modified=True, status=git('status', '--porcelain'))
    (out/'RESTORE.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k!='source_files'}, ensure_ascii=False, indent=2))
    print('Baseline files:', len(baseline))

if __name__ == '__main__':
    main()
