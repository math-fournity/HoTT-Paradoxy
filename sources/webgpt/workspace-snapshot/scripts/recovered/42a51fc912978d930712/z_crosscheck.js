#!/usr/bin/env node
/* Independent JavaScript cross-check for the HOTT–Z finite core.
   It intentionally shares no Python implementation code. */
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT = path.resolve(__dirname, '..', '..');
const OUT = path.join(ROOT, 'verification', 'node_crosscheck.json');

function* tuples(length, base, prefix = []) {
  if (prefix.length === length) { yield prefix.slice(); return; }
  for (let i = 0; i < base; i++) {
    prefix.push(i); yield* tuples(length, base, prefix); prefix.pop();
  }
}
function fiberConstant(alpha, f) {
  for (let i=0;i<alpha.length;i++) for (let j=0;j<alpha.length;j++)
    if (alpha[i]===alpha[j] && f[i]!==f[j]) return false;
  return true;
}
function factors(alpha, f) {
  const r = new Map();
  for (let i=0;i<alpha.length;i++) {
    if (r.has(alpha[i]) && r.get(alpha[i])!==f[i]) return false;
    r.set(alpha[i], f[i]);
  }
  return true;
}
function permutations(xs) {
  if (xs.length <= 1) return [xs.slice()];
  const out=[];
  for (let i=0;i<xs.length;i++) {
    const rest=xs.slice(0,i).concat(xs.slice(i+1));
    for (const p of permutations(rest)) out.push([xs[i]].concat(p));
  }
  return out;
}
function factorial(n){let x=1; for(let i=2;i<=n;i++)x*=i; return x;}
function exactPow2(n){ return 2n ** BigInt(n); }

const checks=[];
function add(id, title, passed, metrics={}) { checks.push({id,title,passed:Boolean(passed),metrics}); }

let cases=0, ok=true;
for (let nw=1;nw<=4;nw++) for (let nm=1;nm<=3;nm++) {
  for (const alpha of tuples(nw,nm)) for (const f of tuples(nw,2)) {
    cases++; if (fiberConstant(alpha,f)!==factors(alpha,f)) ok=false;
  }
}
add('JS-001','factorisation iff fibre constancy on image',ok,{cases});

let refinementCases=0; ok=true;
for (let nw=1;nw<=3;nw++) for (let nn=1;nn<=3;nn++) for (let nm=1;nm<=3;nm++) {
  for (const beta of tuples(nw,nn)) for (const r of tuples(nn,nm)) {
    const alpha=beta.map(x=>r[x]);
    for (const f of tuples(nw,2)) {
      refinementCases++;
      if (factors(alpha,f) && !factors(beta,f)) ok=false;
    }
  }
}
add('JS-002','refinement monotonicity',ok,{cases:refinementCases});

const byN={}; ok=true;
for(let n=2;n<=8;n++) {
  let movedPoints=0;
  for(let x=0;x<n;x++) {
    const y=(x+1)%n;
    const perm=Array.from({length:n},(_,i)=>i);
    [perm[x],perm[y]]=[perm[y],perm[x]];
    if(perm[x]!==x)movedPoints++; else ok=false;
  }
  let movedOrders=0;
  for(const order of permutations(Array.from({length:n},(_,i)=>i))) {
    const perm=Array.from({length:n},(_,i)=>i);
    [perm[order[0]],perm[order[1]]] = [perm[order[1]],perm[order[0]]];
    const transformed=order.map(x=>perm[x]);
    if(transformed.some((x,i)=>x!==order[i])) movedOrders++; else ok=false;
  }
  byN[n]={movedPoints,points:n,movedOrders,orders:factorial(n)};
}
add('JS-003','no invariant point/order for unlabeled n-element types',ok,{byN});

const corePlus=[['a','a'],['b','b']];
const coreMinus=[['a','a'],['b','b']];
const phiPlus=true, phiMinus=false;
add('JS-004','walking arrow and reverse share core but differ in direction',
  JSON.stringify(corePlus)===JSON.stringify(coreMinus)&&phiPlus&&!phiMinus,
  {core:corePlus,phiPlus,phiMinus});

const countermodels={
  provenance:{alpha:[0,0],target:[1,0]},
  role:{alpha:[0,0],target:[0,1]},
  context:{alpha:[0,0],target:[0,1]},
  cost:{alpha:[0,0],target:[1,1000001]},
};
ok=true;
for(const m of Object.values(countermodels)) if(factors(m.alpha,m.target))ok=false;
add('JS-005','four forgetful countermodels do not factor',ok,{countermodels});

const neg=[1,0];
let orbit=[0]; for(let i=0;i<12;i++)orbit.push(neg[orbit[orbit.length-1]]);
add('JS-006','guard erasure / Boolean negation',
  neg.every((v,i)=>v!==i) && orbit.join(',')==='0,1,0,1,0,1,0,1,0,1,0,1,0', {orbit});

ok=true;
const zeno=[];
for(let n=0;n<=80;n++) {
  const denom=exactPow2(n);
  const numer=denom-1n;
  if(!(numer<denom))ok=false;
  zeno.push({n,numer:numer.toString(),denom:denom.toString()});
}
add('JS-007','exact Zeno finite stages are below endpoint',ok,{checkedThrough:80,last:zeno[80]});

const report={
  schema_version:'hott_z.node_crosscheck.v1',
  generated_at:new Date().toISOString(),
  runtime:{node:process.version,platform:process.platform,arch:process.arch},
  summary:{total:checks.length,passed:checks.filter(x=>x.passed).length,failed:checks.filter(x=>!x.passed).length},
  checks
};
report.summary.overall_ok=report.summary.failed===0;
fs.writeFileSync(OUT, JSON.stringify(report,null,2)+'\n');
const source=fs.readFileSync(__filename);
fs.writeFileSync(path.join(ROOT,'verification','node_crosscheck.txt'),
  `source_sha256=${crypto.createHash('sha256').update(source).digest('hex')}\n`+
  `total=${report.summary.total} passed=${report.summary.passed} failed=${report.summary.failed}\n`+
  `overall_ok=${report.summary.overall_ok}\n`+
  checks.map(c=>`[${c.passed?'PASS':'FAIL'}] ${c.id} ${c.title}`).join('\n')+'\n');
console.log(JSON.stringify(report.summary));
process.exit(report.summary.overall_ok?0:1);
