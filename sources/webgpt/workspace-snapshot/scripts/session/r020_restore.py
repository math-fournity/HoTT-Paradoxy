"""Restore the supplied rev19 repository safely, preserving Git and inputs."""
from pathlib import Path, PurePosixPath
import hashlib, json, stat, zipfile
ROOT=Path(__file__).resolve().parents[2]
SRC=Path('/mnt/data/HoTT2_audit_rev19_with_git.zip')
PREFIX='HoTT2_audit_rev19/'
rows=[]
with zipfile.ZipFile(SRC) as z:
    for info in z.infolist():
        if not info.filename.startswith(PREFIX):
            raise ValueError('Unexpected root '+info.filename)
        rel=PurePosixPath(info.filename[len(PREFIX):])
        if not rel.parts:
            continue
        if rel.is_absolute() or '..' in rel.parts or stat.S_ISLNK(info.external_attr>>16):
            raise ValueError('Unsafe archive member '+info.filename)
        target=ROOT.joinpath(*rel.parts)
        if info.is_dir():
            target.mkdir(parents=True,exist_ok=True)
            continue
        data=z.read(info)
        if target.exists() and target.read_bytes()!=data:
            raise ValueError('Refusing changed file '+str(rel))
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(data)
        if (info.external_attr>>16)&0o111:
            target.chmod(0o755)
        rows.append({'path':str(rel),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    assert z.testzip() is None
out=ROOT/'artifacts/r020'
out.mkdir(parents=True,exist_ok=True)
receipt={'schema_version':'hott-r020-restore/v1','archive':str(SRC),'archive_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'root':str(ROOT),'files':rows,'git_restored':(ROOT/'.git').is_dir(),'basis_revision':19,'no_claim_of_rev24_restoration':True}
(out/'RESTORE.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'root':str(ROOT),'files':len(rows),'git_restored':receipt['git_restored'],'archive_sha256':receipt['archive_sha256']},ensure_ascii=False,indent=2))
