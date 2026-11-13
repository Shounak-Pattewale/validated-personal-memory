from pathlib import Path
import json,re,string,collections,hashlib
import pandas as pd
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'data/benchmarks'
OUT=ROOT/'results'
OUT.mkdir(exist_ok=True)
D=pd.read_csv(P/'scores.csv.gz',dtype={'id':str,'category':str})
G='gemma4:31b';N='nemotron-3-super';rng=np.random.default_rng(20261112);B=20000
Q=D[D.model==G].merge(D[D.model==N],on=['suite','id'],suffixes=('_g','_n'),validate='one_to_one')
assert len(Q)==41486 and (Q.prompt_hash_g==Q.prompt_hash_n).all()
Q['diff']=Q.score_g-Q.score_n
out={}
for suite,z in Q.groupby('suite'):
 if suite=='LoCoMo-QA':
  z=z.copy();z['cluster']=z.id.str.rsplit('_',n=1).str[0];a=z.groupby('cluster')['diff'].agg(['sum','size']);ix=rng.integers(len(a),size=(B,len(a)));bt=a['sum'].to_numpy()[ix].sum(1)/a['size'].to_numpy()[ix].sum(1)
  method='Paired conversation-cluster bootstrap, 10 conversations, question-weighted ratio.'
 elif suite=='LongMemEval-S':
  cl=pd.read_csv(P/'lme_evidence_clusters.csv',dtype={'id':str});z=z.merge(cl,on='id',validate='one_to_one');a=z.groupby('evidence_cluster')['diff'].agg(['sum','size']);ix=rng.integers(len(a),size=(B,len(a)));bt=a['sum'].to_numpy()[ix].sum(1)/a['size'].to_numpy()[ix].sum(1)
  method='Paired shared-evidence-session cluster bootstrap, 495 components; reused background sessions not isolated.'
 else:
  z=z.copy();z['index']=z.id.str.rsplit('_',n=1).str[-1];a=z.groupby(['category_g','index'])['diff'].mean();bt=np.zeros(B)
  for _,v in a.groupby(level=0):
   v=v.to_numpy()
   for st in range(0,B,1000):bt[st:st+1000]+=v[rng.integers(len(v),size=(min(1000,B-st),len(v)))].mean(1)/13
  method='Paired task-stratified sample-index block bootstrap across six lengths; fixed tasks and generation seed.'
 trunc=(z.status_g=='output_limit')|(z.status_n=='output_limit')
 out[suite]=dict(n=len(z),gemma=z.score_g.mean(),nemotron=z.score_n.mean(),difference=z['diff'].mean(),ci=np.quantile(bt,[.025,.975]).tolist(),method=method,excluding_truncated_difference=z.loc[~trunc,'diff'].mean(),worst_case_truncation_difference=(z.score_g.where(z.status_g!='output_limit',0)-z.score_n.where(z.status_n!='output_limit',1)).mean())

expected=json.loads((P/'statistics.json').read_text())['results']
for suite in expected:
 for field in ('gemma','nemotron','difference'):
  assert abs(out[suite][field]-expected[suite][field])<1e-9
(OUT/'benchmark_analysis.json').write_text(json.dumps(out,indent=2)+'\n')
pd.DataFrame(out).T.to_csv(OUT/'benchmark_summary.csv',index_label='suite')
print('PASS: 82,972 saved scores paired; benchmark means and confidence intervals calculated offline.')
