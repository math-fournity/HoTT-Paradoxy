"""Auditor's isolated replay and local ablation observations, not new claims."""
import hashlib,json,os,pathlib,shutil,subprocess,tempfile
from audit_capture import OUT,ROOT,write_json,sha,now
cfg=json.loads((ROOT/'HoTT/formal/partiality-race-timeout/TOOLCHAIN.json').read_text())
binary=cfg['agda']['local_binary']
assert sha(pathlib.Path(binary).read_bytes())==cfg['agda']['binary_sha256']
base=OUT/'native-observations-02';base.mkdir(exist_ok=False)
env=os.environ.copy()
env['XDG_DATA_HOME']=cfg['runtime_cache']['xdg_data_home'];env['XDG_CONFIG_HOME']=cfg['runtime_cache']['xdg_config_home']
inputs={
 'delay':'HoTT/formal/partiality-race-timeout/PartialityRaceTimeout.agda',
 'cost':'HoTT/formal/partiality-race-timeout/CostFactorization.agda',
 'replacement':'HoTT/formal/two-level-fibrant-replacement-uip/TwoLevelReplacementUIP.agda'}
with tempfile.TemporaryDirectory(prefix='astra-proof-audit-',dir='/Volumes/D/HoTT-toolchain-cache') as tmp:
 work=pathlib.Path(tmp)
 shutil.copytree(cfg['cubical_library']['local_root'],work/'cubical',ignore=shutil.ignore_patterns('*.agdai','.DS_Store','_build'))
 (work/'AGDA_LIBRARIES').write_text(str(work/'cubical/cubical.agda-lib')+'\n')
 rows=[]
 for label,rel in inputs.items():
  source=ROOT/rel; target=work/label/source.name;target.parent.mkdir()
  data=source.read_bytes();target.write_bytes(data)
  saved=base/label;saved.mkdir();(saved/source.name).write_bytes(data)
  command=[binary,'--ignore-interfaces','--library-file='+str(work/'AGDA_LIBRARIES'),'-l','cubical-0.9','-i',str(target.parent),str(target)]
  started=now();p=subprocess.run(command,cwd=work,env=env,capture_output=True,timeout=180)
  (saved/'stdout.txt').write_bytes(p.stdout);(saved/'stderr.txt').write_bytes(p.stderr)
  row={'label':label,'source':rel,'source_sha256':sha(data),'command':command,'started_at':started,'ended_at':now(),'exit_code':p.returncode,'stdout_sha256':sha(p.stdout),'stderr_sha256':sha(p.stderr),'scope':'AUDIT_ISOLATED_KERNEL_OBSERVATION_NOT_NEW_MATRIX_CLAIM'}
  write_json(saved/'RUN.json',row);rows.append(row)
  if label=='cost':
   ablated=data.decode().replace('funExt (λ x → refl)','refl')
   assert ablated!=data.decode() and 'funExt (' not in ablated
   target.write_text(ablated)
   saved=base/'cost-refl';saved.mkdir();(saved/source.name).write_text(ablated)
   p=subprocess.run(command,cwd=work,env=env,capture_output=True,timeout=180)
   (saved/'stdout.txt').write_bytes(p.stdout);(saved/'stderr.txt').write_bytes(p.stderr)
   row={'label':'cost-refl','input_source':rel,'original_sha256':sha(data),'changed_sha256':sha(ablated.encode()),'change':'Replace both funExt applications with refl in isolated copy only','command':command,'exit_code':p.returncode,'stdout_sha256':sha(p.stdout),'stderr_sha256':sha(p.stderr),'scope':'LOCAL_ABLATION_OBSERVATION; not a theorem about every cost model or every HoTT calculus'}
   write_json(saved/'RUN.json',row);rows.append(row)
write_json(base/'SUMMARY.json',{'observed_at':now(),'rows':rows,'mathematical_delivery':'NO_NEW_PROJECT_CLAIM; source and proof scope must be read individually'})
print(json.dumps([{'label':r['label'],'exit':r['exit_code']} for r in rows]))
