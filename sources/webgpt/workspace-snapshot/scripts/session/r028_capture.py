"""Preserve the new peer message, exact visible request framing, and code blocks."""
from pathlib import Path
import hashlib,json,re,datetime
ROOT=Path(__file__).resolve().parents[2]
D=ROOT/'.codex/research/hott/dialogues/GEMINI-001/rounds/008'
def main():
    peer=(D/'IN-007.md').read_text()
    before='刚刚gemini回复了，但你继续评估它的最新回复之前，请你不要把之前的评估工作都丢了，你作为AI的工作认知要跨回复、跨压缩边界保持完整性、连续性、一致性。\n\n评估Gemini对你上次006号发信的最新回复，看看有无可以吸收的内容？看看是否需要程序化验证一些东西再回复？\n\n这是Gemini的回复：\n\n```\n'
    after='```\n\n另外，你需要考虑和评估，是否需要给Gemini再次回信？注意，我们是从和Gemini的探讨中获得对问题的共同探讨之后的深化认识，而不是驱动它完成悖论发现，更不是让它驱动你完成悖论发现。\n\n如果需要，请你给出新的回信。如果不需要，请你自行推动后续工作。'
    request=before+peer+after
    (D/'USER_REQUEST.md').write_text(request)
    rows=[]
    for i,m in enumerate(re.finditer(r'```lean\n(.*?)```',peer,re.S),1):
        b=m.group(1).encode();p=ROOT/f'scripts/recovered/Gemini_IN007/fragment_{i:02d}.lean'
        p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
        rows.append({'path':p.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'execution':'NOT_RUN; original includes placeholders'})
    out={'received_via':'user-pasted public text; no direct model communication','date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'peer_sha256':hashlib.sha256(peer.encode()).hexdigest(),'request_sha256':hashlib.sha256(request.encode()).hexdigest(),
         'boundary':'Hashes identify this saved UTF-8 transcription, not a separately supplied Gemini file or upstream execution receipt',
         'code_fragments':rows,'prior_head':'ba227f4e71a1ca4f0ac21dd9cdbf86fb802782d2'}
    (ROOT/'artifacts/r028/INPUT_PROVENANCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
