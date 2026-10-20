"""Reproduce FPS H sensitivity. USD millions except per-share data.
All future operating, valuation, cash settlement and share inputs are own research
assumptions, not consensus or verified contractual maxima. Does not establish H.
"""
import json
from pathlib import Path
out=Path(__file__).with_name('FPS_model.json')
d=json.loads(out.read_text())
px=32.70
start_cash=97.477
principal=598.5
tra=338.925
leases=121.596
surety=17.6
scenarios={
 'bear':dict(revenue=[2000,2200,2400,2600,2800],fcf=[100,132,176,208,240],ppe=[100,88,96,104,112],shares=[313,322,331,340,350],multiple=18),
 'base':dict(revenue=[2500,3200,3800,4300,4800],fcf=[250,384,532,602,672],ppe=[87,96,114,129,144],shares=[310,316,322,329,335],multiple=25),
 'bull':dict(revenue=[2600,3400,4200,5000,5800],fcf=[312,510,714,800,928],ppe=[87,102,126,150,174],shares=[309,314,319,324,330],multiple=30),
}
results={}
for name,a in scenarios.items():
 cash=start_cash; debt=principal; remaining_tra=tra; rows=[]
 for i in range(5):
  debt_payment=6; tra_payment=25
  cash += a['fcf'][i]-debt_payment-tra_payment
  debt -= debt_payment; remaining_tra -= tra_payment
  rows.append(dict(year_ending=f'{2027+i}-10-14',revenue=a['revenue'][i],cash_ppe=a['ppe'][i],company_ocf=a['fcf'][i]+a['ppe'][i],company_fcf=a['fcf'][i],fcf_margin_pct=100*a['fcf'][i]/a['revenue'][i],principal_payment=debt_payment,tra_payment=tra_payment,retained_cash=cash,financial_principal=debt,remaining_tra=remaining_tra,maximum_economic_shares_assumed=a['shares'][i]))
 claims=debt+remaining_tra+leases+surety
 netcash=cash-claims
 enterprise=a['fcf'][-1]*a['multiple']
 equity=max(0,enterprise+netcash)
 final=equity/a['shares'][-1]
 results[name]=dict(annual=rows,terminal_ev_company_fcf_multiple=a['multiple'],terminal_enterprise_value=enterprise,terminal_claims=claims,terminal_net_cash_after_all_modeled_claims=netcash,terminal_equity_value=equity,terminal_price=final,annualized_total_return_pct=100*((final/px)**.2-1),twenty_percent_return_entry_ceiling=final/1.2**5)
d['scenarios']=results
d['scenarios_note']='Rolling Oct14 years are approximate fiscal blends. OCF = company FCF + all cash PP&E; rent, cash interest and cash tax are already in OCF. Additional TRA cash payments 25/year and principal 6/year are financing/claim settlement cash flows. Debt maturity beyond FY31 is retained as a terminal claim, not forgotten. Terminal TRA is reduced only by modeled actual cash payments; no TRA tax benefit is added again. Residual lease and full surety balances conservatively remain terminal claims; this is not a prediction that all become payable at once. Cash is retained and valued once, no dividends, buybacks or additional acquisitions assumed. Future shares include current Opco interests; provisional share paths are not a verified full maximum-award register. Complete funding obligations, TRA timing, interest-rate response and peer/own-median valuation cap are unresolved, so none of the three scenarios establishes H2/H4.'
d['price']=px
d['proposed_quality_path']['valuation_base']=results['base']
d['failure_tail']=dict(terminal_equity_value=0,stock_cash_loss_pct=100,probability='not assigned')
out.write_text(json.dumps(d,indent=2)+'\n')
for name,r in results.items():
 print(name,round(r['terminal_price'],4),round(r['annualized_total_return_pct'],4),round(r['twenty_percent_return_entry_ceiling'],4),round(r['terminal_net_cash_after_all_modeled_claims'],4))
