#!/usr/bin/env python3
"""Execute only the explicitly supplied finite method fixtures, not HoTT discovery."""
from pathlib import Path
import hashlib, itertools, json
HERE=Path(__file__).resolve().parent

def main():
    expected=json.loads((HERE/'expected-oracle.json').read_text())
    assignments=list(itertools.product([0,1], repeat=3))
    independent=[(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]
    assert assignments==independent
    predicates={'x_eq_y':lambda a:a[0]==a[1], 'y_eq_z':lambda a:a[1]==a[2], 'x_ne_z':lambda a:a[0]!=a[2], 'x_eq_z':lambda a:a[0]==a[2]}
    traces={}
    for name,key in [('negative','constraints'),('normal','normal_constraints')]:
        constraints=expected['joint_fixture'][key]
        rows=[]
        for mask in range(8):
            chosen=[c for j,c in enumerate(constraints) if mask&(1<<j)]
            models=[list(a) for a in assignments if all(predicates[c](a) for c in chosen)]
            rows.append({'mask':mask,'selected_constraints':chosen,'models':models,'model_count':len(models)})
        counts=[r['model_count'] for r in rows]
        assert counts==expected['joint_fixture']['expected_solution_counts_by_mask'][name]
        traces[name]={'single_pair_selection':[r for r in rows if len(r['selected_constraints'])<=2], 'structural_joint_selection':rows[7], 'full_rows':rows}
    def evaluate(order):
        value=1;trace=[value]
        for op in order:
            value=value+1 if op=='inc' else value*2
            trace.append(value)
        return {'order':order,'trace':trace,'output':value}
    ab=evaluate(['inc','double']);ba=evaluate(['double','inc'])
    assert ab['output']==expected['order_fixture']['expected_ab'] and ba['output']==expected['order_fixture']['expected_ba']
    result={'schema':'mo3-fixed-method-controls/v1','status':'FIXED_FIXTURES_MATCHED_ORACLE','input_hashes':{p:hashlib.sha256((HERE/p).read_bytes()).hexdigest() for p in ['CONTROL-SCOPE.md','expected-oracle.json','run_fixed_controls.py']},'assignment_denominator':8,'selection_masks_per_fixture':8,'enumeration_remainder':0,'joint':traces,'order':{'ab':ab,'ba':ba},'boundary':'provided fixtures and explicit selection modes; not proof of autonomous grouping, real HoTT result, general mathematical completeness, or C04 completion'}
    target=HERE/'fixed-controls-result.json'
    with target.open('x') as f:f.write(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'assignment_denominator':8,'negative_joint_model_count':traces['negative']['structural_joint_selection']['model_count'],'normal_joint_model_count':traces['normal']['structural_joint_selection']['model_count'],'order_outputs':[ab['output'],ba['output']]},ensure_ascii=False))

if __name__=='__main__':main()
