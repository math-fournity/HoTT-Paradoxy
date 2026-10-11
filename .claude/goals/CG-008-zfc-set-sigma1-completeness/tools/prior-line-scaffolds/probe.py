import json, os, subprocess, pathlib, sys
cl=json.load(open('/Volumes/D/HoTT_AI_HANDOFF_20260911/外部资料/Z0-D3-Foundation全量源码/项目模块/MATHLIB_CLOSURE.json'))
lp=[p for p in cl['lean_path'] if os.path.isdir(p)]
lp.append('/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean')
lp.append('/tmp/d3build/devbuild/godel-q-zfc-z0-full')
LEAN='/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean'
env=dict(os.environ)
env['LEAN_PATH']=':'.join(lp)
env['LEAN_SYSROOT']='/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0'
name=sys.argv[1]
src=pathlib.Path(f'/tmp/z0probe/{name}.lean').read_text()
r=subprocess.run([LEAN,'-DautoImplicit=false',f'{name}.lean'],capture_output=True,text=True,env=env,cwd='/tmp/z0probe')
print('exit',r.returncode)
print(r.stdout[:8000])
if r.stderr: print('STDERR',r.stderr[:4000])
