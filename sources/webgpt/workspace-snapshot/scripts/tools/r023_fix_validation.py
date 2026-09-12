"""Preserve the initial packaging check and correct its overly literal H05 test."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[2]
p=R/'scripts/tools/r023_package.py'
backup=R/'scripts/recovered/r023/package_initial.py'
if backup.exists():raise FileExistsError(str(backup))
backup.parent.mkdir(parents=True,exist_ok=True);original=p.read_bytes();backup.write_bytes(original)
failure=R.parent/'HoTT_Gemini_response_rev23_packaging_failure.json'
(R/'artifacts/r023/PACKAGING_INITIAL_FAILURE.json').write_bytes(failure.read_bytes())
s=original.decode()
s=s.replace("check('letter_all_topics',all(f'H{i:02}' in text for i in range(1,7)))", "check('letter_all_topics', all(f'H{i:02}' in text for i in (1,2,3,4,6)) and '## 六、我怎样调整下一步，而不让研究重新陷入纠错循环' in text and {x['id'] for x in json.loads((R/(N+'RESPONSE_MAP.json')).read_text())['items']} == {f'H{i:02}' for i in range(1,7)})")
s=s.replace("check('new_scripts_parse',len(parsed)==5,parsed)","check('new_scripts_parse',len(parsed)==6,parsed)")
s=s.replace('四次远程源码下载因DNS失败，保留所有错误；', '首次打包检查按编号字面匹配H05而失败：正文第六节已完整回应调度，但标题未含H05。保留原检查源码与失败日志，将该项校验改为核正文节标题及完整回应映射，未改信件或其已登记哈希。四次远程源码下载因DNS失败，保留所有错误；')
if s==original.decode():raise AssertionError('No patch')
p.write_text(s,encoding='utf-8')
record={'reason':'H05 scheduling answer is substantive section VI but did not literally include H05; validate section and six-item map, not only a label.',
 'letter_changed':False,'checkpoint_changed':False,'original_script':'scripts/recovered/r023/package_initial.py',
 'original_sha256':hashlib.sha256(original).hexdigest(),'patched_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(R/'artifacts/r023/VALIDATION_FIX.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False))
