#!/usr/bin/env python3
"""Extract the generated archive once into an independent path containing spaces."""
from pathlib import Path,PurePosixPath
import hashlib,json,shutil,tarfile
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
DEST=Path('/Volumes/D/HoTT-toolchain-cache/astra-review-20260921/relocated with spaces')
build=json.loads((OUT/'BUILD.json').read_text());archive=Path(build['archive'])
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(archive)==build['archive_sha256'];assert not DEST.exists();DEST.mkdir(parents=True)
with tarfile.open(archive,'r:gz') as t:
    members=t.getmembers()
    assert all(m.isfile() and not PurePosixPath(m.name).is_absolute() and '..' not in PurePosixPath(m.name).parts for m in members)
    t.extractall(DEST,filter='data')
bundle=DEST/'four-stage-review';assert sha(bundle/'MANIFEST.json')==build['manifest_sha256']
tool=json.loads((ROOT/'HoTT/formal/agda-unimath/no-erasure/TOOLCHAIN.json').read_text())['agda'];compiler=DEST/'compiler/agda';compiler.parent.mkdir();shutil.copy2(tool['local_binary'],compiler)
assert sha(compiler)==tool['binary_sha256']
receipt={'status':'EXTRACTED_INDEPENDENT_LOCATION','archive_sha256':sha(archive),'manifest_sha256':sha(bundle/'MANIFEST.json'),'bundle':str(bundle),'compiler':str(compiler),'compiler_sha256':sha(compiler),'actual_extract_members':len(members),'launch_cwd':'/Volumes/D','source_package_copied_from_archive_not_builder_tree':True}
(OUT/'EXTRACT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt))
