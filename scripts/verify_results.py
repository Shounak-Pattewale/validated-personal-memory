"""Verify the principal paper numbers from supplied audit exports. No network or model calls."""
from pathlib import Path
import csv, json, math
ROOT=Path(__file__).resolve().parents[1]/'data/audit'
def rows(name):
 with (ROOT/name).open(newline='') as f:return list(csv.DictReader(f))
def truth(s):return s=='True'
scores=rows('scores.csv');costs=rows('costs.csv');states=rows('state_checks.csv')
expected={
'deepseek-v4.1-flash:1017':[24,60,58,51,46,41,38,60,60],
'gemma4:31b':[24,37,46,0,45,44,44,60,60],
'glm-5.2':[24,51,54,0,45,45,44,57,60]}
arms=['no_memory','full_history','recent_6','rolling_summary','bm25_6','dense_6','hybrid_6','middleware_selected','middleware_visible']
for m,counts in expected.items():
 for arm,n in zip(arms,counts):
  r=next(x for x in scores if x['model']==m and x['arm']==arm)
  assert int(r['n'])==60 and math.isclose(float(r['strict_accuracy'])*60,n,abs_tol=1e-8)
  assert int(r['score_mismatches'])==0
 g=[r for r in states if r['model']==m]
 assert len(g)==162 and all(truth(r['state_equal']) for r in g)
 assert not any(truth(r['recomputed_incorrect_mutation']) for r in g)
 assert sum(truth(r['proposal_exact']) for r in g)==(159 if m=='glm-5.2' else 162)
for m, totals in zip(expected,[(133607,168946,171613),(127175,151375,153361),(129253,154799,156784)]):
 for arm,total in zip(['full_history','middleware_selected','middleware_visible'],totals):
  r=next(x for x in costs if x['model']==m and x['arm']==arm)
  assert int(float(r['total_tokens']))==total
  assert int(r['attributed_calls'])==(60 if arm=='full_history' else 222)
parity=rows('within_model_parity.csv')
assert len(parity)==3 and all(all(truth(r[k]) for k in ['all_answer_payloads_present','same_explicit_settings','same_system_prompt','submitted_alias_matches']) for r in parity)
coverage=rows('request_coverage.csv');assert sum(int(r['saved_payloads']) for r in coverage)==1620
report=json.loads((ROOT/'v76_recovered_reports.json').read_text())
r=next(x['data'] for x in report if x['name']=='final_report.json')
assert r['supported_strict']==119 and r['supported_cases']==120
assert r['counts']['state_exact']==128 and r['counts']['incorrect_mutation']==0
assert r['decision']=='BOUNDED_ACCEPTANCE_FAILED_KEEP_STAGED'
p=json.loads((ROOT/'public_reproduced_results.json').read_text())
assert p['LongMemEval-S']['gemma']==.79 and p['LongMemEval-S']['nemotron']==.586
print('PASS: primary accuracy counts, score agreement, state traces, token totals, request parity, acceptance decision, and public LongMemEval summary.')
print('Verification scope: supplied audit exports. This does not reconstruct missing raw archives, validate gold semantics, or establish novelty.')
