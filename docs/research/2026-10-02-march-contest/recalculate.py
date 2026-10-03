"""Recompute March scenario returns from contest-data.json; no network/trading.

Usage: python3 recalculate.py --end 2027-03-31 --iv-multiplier 0.75
Continuous premium weights are paper assumptions, not executable whole contracts.
"""
import argparse, json, math
from datetime import date
from pathlib import Path

def call_value(s, k, t, r, v):
    if t <= 0:
        return max(s-k, 0)
    n = lambda z: (1+math.erf(z/math.sqrt(2)))/2
    d1 = (math.log(s/k)+(r+v*v/2)*t)/(v*math.sqrt(t))
    return max(0, s*n(d1)-k*math.exp(-r*t)*n(d1-v*math.sqrt(t)))

def calculate(data, end, multiplier):
    seeds = {x['ticker']:x for x in data['seeds']}
    result=[]
    for scenario in ['bear','base','bull']:
        total=0
        for pos in data['illustrative_portfolio']:
            seed=seeds[pos['ticker']]; s=seed['prices'][scenario]
            if pos['instrument']=='shares': ret=s/seed['close']-1
            else:
                days=(date.fromisoformat(pos['expiry'])-end).days
                if days<0:
                    raise ValueError('Contest ends after a contract expiry; its prior cash settlement/path is not modeled.')
                value=call_value(s,pos['strike'],days/365,data['model']['rate'],pos['entry_iv']*multiplier)
                ret=value/pos['entry_ask']-1
            total+=pos['weight_pct']/100*ret
        result.append(dict(case=scenario,contest_end=end.isoformat(),iv_multiplier=multiplier,return_pct=total*100))
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--end',default='2027-03-31');p.add_argument('--iv-multiplier',type=float,default=.75)
    a=p.parse_args()
    if a.iv_multiplier<=0:p.error('IV multiplier must be positive')
    data=json.loads((Path(__file__).parent/'contest-data.json').read_text())
    assert sum(x['weight_pct'] for x in data['illustrative_portfolio'])==100
    print(json.dumps(calculate(data,date.fromisoformat(a.end),a.iv_multiplier),indent=2))
