"""Explicit research assumptions, not consensus or a certified H entry model.
USD millions; one-year periods ending October 14, 2027 through 2031.
Terminal operating cash FCF is OCF minus cash PP&E; additional software cash,
employee tax withholding, and debt maturity are separately included in liquidity.
No unopened ATM funding is assumed. No cash dividends. No double-counted cash.
"""
import json,pathlib
root=pathlib.Path(__file__).parent
price=14.13
scenarios={
 'bear': {'revenue':[470,530,580,630,680],'op_margin':[-.15,-.10,-.05,0,.05], 'sbc_margin':[.12,.10,.08,.06,.05],'tax_margin':[0,0,0,0,0],'capex_margin':[.25,.23,.21,.18,.16],'shares':[405,430,450,465,505],'new_equity':[0,0,0,0,200],'multiple':15},
 'base': {'revenue':[540,700,880,1060,1250],'op_margin':[-.08,0,.08,.15,.20], 'sbc_margin':[.12,.10,.09,.08,.07],'tax_margin':[0,0,.01,.03,.04],'capex_margin':[.22,.19,.16,.13,.12],'shares':[405,425,440,452,465],'new_equity':[0,0,0,0,0],'multiple':22},
 'bull': {'revenue':[600,900,1300,1800,2500],'op_margin':[0,.12,.23,.30,.35], 'sbc_margin':[.12,.10,.08,.06,.05],'tax_margin':[0,.01,.03,.05,.06],'capex_margin':[.20,.18,.16,.13,.10],'shares':[410,435,457,475,489],'new_equity':[0,0,0,0,0],'multiple':22}}
out={'as_of':'2026-10-15','governing_close':'2026-10-14','entry':price,'starting_cash_actual_July_31':865.418,'starting_cash_model_Oct_14':840.418,'cash_bridge_assumption':-25,'period_ends':['2027-10-14','2028-10-14','2029-10-14','2030-10-14','2031-10-14'],'quality_deadline_proposed':'2031-10-14','not_approved_entry':True,'source_anchors':['https://www.sec.gov/Archives/edgar/data/1836833/000119312526382016/pl-20260731.htm','https://stockanalysis.com/stocks/pl/forecast/','https://stockanalysis.com/stocks/vrsk/statistics/','https://stockanalysis.com/stocks/trmb/statistics/'],'scenarios':{}}
for name,c in scenarios.items():
 cash=840.418;rows=[]
 for i,r in enumerate(c['revenue']):
  # D&A 10% and working-capital use 2% of sales, all years.
  op=r*c['op_margin'][i];da=r*.10;sbc=r*c['sbc_margin'][i];tax=r*c['tax_margin'][i];wc=r*.02
  # Interest cash conservatively included in other cash consumption below;
  # no interest income from surplus cash is credited.
  ocf=op+da+sbc-tax-wc;capex=r*c['capex_margin'][i];fcf=ocf-capex
  software=5;withholding=20;interest=2.3 if i<4 else 0;maturity=460 if i==4 else 0;financing=c['new_equity'][i]
  cash+=fcf-software-withholding-interest-maturity+financing
  rows.append({'year_end':out['period_ends'][i],'revenue':r,'gaap_operating_margin':c['op_margin'][i],'cash_OCF_before_note_interest':ocf,'cash_PP&E':capex,'company_FCF_before_note_interest':fcf,'additional_software_cash':software,'financing_cash_employee_withholding':withholding,'note_cash_interest':interest,'note_maturity_cash_repayment':maturity,'new_equity_cash':financing,'fully_diluted_shares':c['shares'][i],'ending_cash':cash})
 terminalfcf=rows[-1]['company_FCF_before_note_interest'];leaseclaim=40
 equity=max(0,terminalfcf*c['multiple']+cash-leaseclaim);cash_value=equity/c['shares'][-1]
 # Company may deliver all shares on conversion. Use no capped-call credit.
 # Compare full physical delivery of 38.48889M shares, restoring the cash
 # principal repayment, against cash maturity repayment. Take the lower
 # shareholder value; never deduct the same USD460M and add convert shares.
 convert_shares=460000*83.6715/1000000
 convert_value=max(0,equity+460)/(c['shares'][-1]+convert_shares)
 value=min(cash_value,convert_value)
 out['scenarios'][name]={'annual_cash_maturity_case':rows,'terminal_cash_FCF_multiple_assumption':c['multiple'],'terminal_lease_claim_assumption':leaseclaim,'cash_maturity_terminal_value':cash_value,'full_physical_conversion_terminal_value':convert_value,'convert_physical_shares':convert_shares,'terminal_share_value':value,'annualized_return':(value/price)**.2-1,'H4_return_only_entry_ceiling_assumption':value/1.2**5,'maximum_24_month_fully_diluted_shares_proposed':480,'maximum_deadline_fully_diluted_shares_proposed':550,'funding_note':'bear later USD200M equity at USD5/share included in year5 505M ordinary shares; not funding available today' if name=='bear' else 'no future raise; lesser of cash-maturity and physical-convert per-share outcomes; capped calls receive zero credit'}
out['failed_commercialization']={'equity_value':0,'share_loss':-1,'loss_at_H_initial_sleeve_cap':-.025,'loss_at_H_initial_portfolio_cap':-.006}
base=out['scenarios']['base'];terminal_cash=base['annual_cash_maturity_case'][-1]['ending_cash']-40
out['reverse_hurdle']={'required_year5_share_value':price*1.2**5,'required_company_FCF_cash_maturity_case':(price*1.2**5*465-terminal_cash)/22,'required_company_FCF_full_physical_conversion_case':(price*1.2**5*(465+convert_shares)-terminal_cash-460)/22}
(root/'PL-H-sensitivity.json').write_text(json.dumps(out,indent=2))
for n,s in out['scenarios'].items():print(n,round(s['terminal_share_value'],2),round(s['annualized_return']*100,2),round(s['H4_return_only_entry_ceiling_assumption'],2))
print('required_FCF',out['reverse_hurdle'])
