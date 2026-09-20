#!/usr/bin/env python3
"""Derive an isolated no-erasure variant; never modify the pinned upstream tree.

This is a deterministic dependency generator, not a claimed soundness proof.
The original archive is the parent, and the exact two-file patch defines the variant.
"""
from pathlib import Path
import difflib,importlib.util,json,shutil

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
FORM=ROOT/'HoTT/formal/agda-unimath/no-erasure'
sp=importlib.util.spec_from_file_location('capture',ROOT/'scripts/audit/capture_agda_unimath_replay_run.py')
C=importlib.util.module_from_spec(sp);sp.loader.exec_module(C)
cfg=json.loads((ROOT/'HoTT/formal/agda-unimath/UNIMATH_TOOLCHAIN.json').read_text())
lib=cfg['agda_unimath_library'];original=Path(lib['local_root'])
variant=original.with_name(original.name+'-astra-no-erasure-v1')
assert not variant.exists(), 'Never overwrite an existing derivative'
assert C.deterministic_tree(original)=={'file_count':lib['tree_file_count'],'total_bytes':lib['tree_total_bytes'],'tree_sha256':lib['tree_sha256']}
shutil.copytree(original,variant,ignore=shutil.ignore_patterns('*.agdai','.DS_Store'))
module='src/reflection/erasing-equality.lagda.md'
old=(original/module).read_text()
new='''# Identity-preserving replacement for equality erasure

This local derivative replaces the Agda primitive with the ordinary identity
function. It has no rule reducing an arbitrary loop to reflexivity. The upstream
file and full diff remain in the parent archive and the project's derivation.
This change does not certify the other postulates or the whole library.

```agda
module reflection.erasing-equality where

open import foundation.universe-levels
open import foundation-core.identity-types

primEraseEquality : {l : Level} {A : UU l} {x y : A} → x ＝ y → x ＝ y
primEraseEquality p = p
```
'''
(variant/module).write_text(new)
name='agda-unimath-no-erasure'
libfile=Path(lib['library_file']).name
oldlib=(original/libfile).read_text()
newlib=oldlib.replace('name: agda-unimath','name: '+name).replace(' -WnoWithoutKFlagPrimEraseEquality','')
assert newlib!=oldlib
(variant/libfile).write_text(newlib)
changes=[];patch=''
for rel,before,after in [(module,old,new),(libfile,oldlib,newlib)]:
 patch+=''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/'+rel,tofile='b/'+rel))
 changes.append({'path':rel,'before_sha256':C.sha(before.encode()),'after_sha256':C.sha(after.encode())})
# Recheck every source path, not just the planned edits.
actual=[]
for p in sorted(variant.rglob('*')):
 if p.is_file() and p.read_bytes()!=(original/p.relative_to(variant)).read_bytes():actual.append(p.relative_to(variant).as_posix())
assert sorted(actual)==sorted(x['path'] for x in changes)
FORM.mkdir(parents=True,exist_ok=True)
C.exclusive_write(FORM/'identity-replacement.patch',patch.encode())
C.exclusive_write(FORM/'AGDA_LIBRARIES',(str(variant/libfile)+'\n').encode())
tree=C.deterministic_tree(variant)
lib.update(name=name,local_root=str(variant),library_file=str(variant/libfile),
 library_file_bytes=len(newlib.encode()),library_file_sha256=C.sha(newlib.encode()),
 library_flags=newlib.split('flags: ',1)[1].strip(),tree_file_count=tree['file_count'],
 tree_total_bytes=tree['total_bytes'],tree_sha256=tree['tree_sha256'])
lib['upstream_commit_is_parent_not_exact_variant']=True
cfg['theory_variant']='Agda without-K HoTT with explicit foundation postulates; local agda-unimath derivative removing primEraseEquality reduction (not unmodified upstream; not a full soundness certification)'
cfg['project_library_registry']='HoTT/formal/agda-unimath/no-erasure/AGDA_LIBRARIES'
cfg['derivation']={'parent_toolchain':'HoTT/formal/agda-unimath/UNIMATH_TOOLCHAIN.json','patch':'HoTT/formal/agda-unimath/no-erasure/identity-replacement.patch','patch_sha256':C.sha(patch.encode()),'changed_files':changes,'policy':'Parent source/archive unchanged; no interfaces copied; exactly two changed files; original archive is the parent, not an archive of the derivative.'}
C.exclusive_write(FORM/'TOOLCHAIN.json',C.json_bytes(cfg))
C.exclusive_write(OUT/'DERIVATION.json',C.json_bytes({'status':'ISOLATED_VARIANT_PREPARED_NOT_YET_CHECKED','original_root':str(original),'variant_root':str(variant),'actual_changed_paths':actual,'changes':changes,'tree':tree,'parent_tree_still_matches':C.deterministic_tree(original)['tree_sha256']==json.loads((ROOT/'HoTT/formal/agda-unimath/UNIMATH_TOOLCHAIN.json').read_text())['agda_unimath_library']['tree_sha256']}))
print(json.dumps({'variant':str(variant),'changes':actual,'tree':tree}))
