#!/usr/bin/env python3
"""Clarify the model and evidence levels; save typed claim inventory."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
review=ROOT/'.codex/research/hott/reviews/SELF-REFERENCE-004'
p=review/'PROOF_NOTE.md';t=p.read_text()
t=t.replace('反模型取P=false，Q=true。目标公理全真而P假；按通常推导规则的归纳可靠性，目标不可能有P的闭证明。',
'''反模型取P解释为空类型、Q解释为单位类型。目标公理具有实际的单位元素；若有目标中P的闭证明，按第3节解释就得到Empty元素。因此构造性地排除目标P证明，不需要排中律或一般语义完备性。有限Boolean检查对应这个实例，Agda草稿还写出了noTargetP。''')
t=t.replace('Python的interpret实际构造/运行普通函数',
'''本解释消费实际推导数据Der，不是凭一句Box_T(A)就得到A。若只提供截断的推导存在，要按目标是否已为命题另外判断消去；不能一般地将截断存在当作任意类型的实现，也不能否定命题目标下的合法恢复。

Python的interpret实际构造/运行普通函数''')
p.write_text(t)
claims=[
 ('R032-C1','CONSTRUCTIVE_SCOPED_PAPER','Finite Der interpretation consumes explicit realizers of used global/local assumptions; no whole-HoTT reflection.'),
 ('R032-C2','CONSTRUCTIVE_SCOPED_PAPER_AND_FINITE_REPLAY','Proof-producing macro expansion yields a base derivation in the target environment; conservative on this object fragment.'),
 ('R032-C3','CONSTRUCTIVE_SCOPED_PAPER','Bridges to all source axioms iff a uniform all-formula proof transfer; mutual implication only, not inverse proof-level equivalence.'),
 ('R032-C4','CONSTRUCTIVE_SCOPED_PAPER_AND_FINITE_REPLAY','Used-axiom bridges suffice for a given derivation, but their absence is not a no-proof theorem for its conclusion.'),
 ('R032-C5','CONSTRUCTIVE_COUNTERMODEL_AND_FINITE_REPLAY','Changing permit:P to permit:Q does not preserve a proof of P; target Q model with P empty separates them.'),
 ('R032-C6','NATIVE_NOT_RUN','Shared Agda file is uncompiled; Python parser to Der correspondence not proved in a native kernel.'),
 ('R032-C7','NOT_ESTABLISHED','No assertion that standard HoTT or deployed Agda uses the deliberately unsafe receipt-only policy.'),
]
obj={'schema':'scoped-research-claims/v1','round':32,
     'claims':[{'id':i,'status':s,'statement':v,'source':'PROOF_NOTE.md'} for i,s,v in claims],
     'new_hott_paradox_confirmed':False,'originality':'NOT_CLAIMED','native_kernel':'NOT_RUN',
     'full_business_cognition':'INCOMPLETE_AFTER_ACTUAL_COMPACTION',
     'tests':{'v0_count':30,'v1_count':33,'all_passed':True,'all_quantifier_proofs_from_tests':False}}
(review/'CLAIMS.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
