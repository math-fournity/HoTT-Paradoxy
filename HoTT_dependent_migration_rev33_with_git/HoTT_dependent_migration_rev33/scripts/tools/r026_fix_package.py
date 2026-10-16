"""Preserve the failed packaging version and fix a result-field lookup."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'scripts/tools/r026_package.py'
saved=ROOT/'scripts/history/r026_package_v0.py'
if saved.exists():raise FileExistsError(saved)
saved.write_bytes(p.read_bytes())
s=p.read_text()
assert s.count("v1['checks']")==2
s=s.replace("v1['checks']","v1['groups']")
s=s.replace('原稿497行、32478字节完整保全，历史撰写日期未验证。',
            '原稿32478字节完整保全；497个LF换行，Python Unicode splitlines计498行，属于行分隔口径差异。历史撰写日期未验证。')
s=s.replace('本地Git继承rev25历史，不push、不联络其他AI。',
            '首次打包程序将结果字段groups误读为checks，触发KeyError且未提交Git；失败代码与收据已保留，修正后重跑。本地Git继承rev25历史，不push、不联络其他AI。')
p.write_text(s,encoding='utf-8')
failure=ROOT.parent/'HoTT_early_reassessment_rev26_packaging_failure.json'
out=ROOT/'artifacts/r026/PACKAGING_ATTEMPT1_FAILURE.json'
if out.exists():raise FileExistsError(out)
out.write_bytes(failure.read_bytes())
b=(ROOT/'.codex/research/hott/reviews/EARLY-GEMINI-001/ORIGINAL.md').read_bytes()
metrics={'bytes':len(b),'LF_count':b.count(b'\n'),'bytes_splitlines':len(b.splitlines()),'unicode_splitlines':len(b.decode().splitlines()),
    'note':'The source contains a Unicode line separator; byte-LF and Unicode logical line metrics are distinguished, without changing source text.'}
(ROOT/'artifacts/r026/LINE_METRICS.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(metrics,ensure_ascii=False))
