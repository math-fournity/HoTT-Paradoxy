#!/usr/bin/env python3
"""Freeze selected primary Coq source contracts at the paper-linked exact commit.

Read-only upstream; local immutable snapshots, not a Coq replay or whole-library audit.
"""
from pathlib import Path
import datetime,hashlib,json,urllib.request
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
REPO='abooij/HoTT';COMMIT='478aeef5e1a2452481b378eb433e64749a0721a5'
DEST=OUT/'upstream-locator';assert not DEST.exists();DEST.mkdir()
def get(url):
    request=urllib.request.Request(url,headers={'User-Agent':'HoTT-local-source-audit','Accept':'application/vnd.github+json'})
    with urllib.request.urlopen(request,timeout=60) as response:return response.read()
def sha(raw):return hashlib.sha256(raw).hexdigest()
commit=json.loads(get('https://api.github.com/repos/'+REPO+'/commits/'+COMMIT));assert commit['sha']==COMMIT
tree_id=commit['commit']['tree']['sha'];tree=json.loads(get('https://api.github.com/repos/'+REPO+'/git/trees/'+tree_id+'?recursive=1'));assert not tree.get('truncated')
items={r['path']:r for r in tree['tree'] if r['type']=='blob'}
required=['theories/Analysis/Locator.v','theories/BoundedSearch.v','theories/ExcludedMiddle.v','theories/DProp.v','theories/Classes/interfaces/canonical_names.v','theories/Classes/interfaces/abstract_algebra.v','theories/Classes/interfaces/orders.v','theories/Classes/interfaces/cauchy.v','theories/Classes/interfaces/archimedean.v','theories/Classes/theory/apartness.v']
assert all(p in items for p in required),[p for p in required if p not in items]
optional=['README.md','INSTALL.md','_CoqProject','_CoqProject.in','configure','Makefile','LICENSE.txt','LICENSE','COPYING','hott.opam']
selected=required+[p for p in optional if p in items]
assert any('LICENSE' in p or p=='COPYING' for p in selected),'LICENSE_NOT_LOCATED'
rows=[]
for path in selected:
    url='https://raw.githubusercontent.com/'+REPO+'/'+COMMIT+'/'+path;raw=get(url)
    blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest();assert blob==items[path]['sha'],path
    local=DEST/path;local.parent.mkdir(parents=True,exist_ok=True);local.write_bytes(raw)
    rows.append({'upstream_path':path,'path':local.relative_to(ROOT).as_posix(),'bytes':len(raw),'sha256':sha(raw),'git_blob_oid':blob,'url':url})
receipt={'schema_version':'astra-primary-source-contract-snapshot/v1','status':'SELECTED_PRIMARY_BYTES_FROZEN_NOT_REPLAYED','repository':'https://github.com/'+REPO,'paper_linked_branch':'locators','observed_ls_remote_oid':COMMIT,'commit':COMMIT,'tree':tree_id,'commit_date':commit['commit']['committer']['date'],'retrieved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_selection':required,'optional_missing':[p for p in optional if p not in items],'files':rows,'scope':'Exact selected source contracts from the author branch linked by arXiv1805.06781v5. Not all history/current HoTT releases, not Coq compilation, not a new mathematical theorem. Only metadata needed for identity; no credentials or author email retained.'}
(OUT/'LOCATOR-SOURCES.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'commit':COMMIT,'date':receipt['commit_date'],'files':len(rows),'bytes':sum(r['bytes'] for r in rows)},ensure_ascii=False))
