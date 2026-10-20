#!/usr/bin/env python3
"""Assumption sensitivities only: no live fetch, no eligibility or order engine.
USD millions except per-share prices. Annual buckets end Oct 15, 2027..2031.
Latest reported cash proxies adjusted only for known deals are not Oct15 cash.
Run: python3 defense_model.py
"""
import json, pathlib
OUT=pathlib.Path(__file__).resolve().parent
CFG={
'AVAV': {'price':120.60,'cash':547.384,'notes':747.5,'lease':0.,'facility':336.981,'shares':52.,'convert_reserve':2.319,'max24':60.,'max5':85.,'prevrev':1976.8,'interest':0.,'fees_y1':4.8,'raise_price':60.,
 'bear': {'rev':[1980,2000,2100,2205,2315.25],'ebit':[-.02,0,.03,.05,.06],'da':[.06,.06,.05,.04,.04],'ppe':[.09,.07,.06,.05,.05],'wc':.15,'dilution':.03,'multiple':18},
 'base': {'rev':[2200,2540,2921,3300.73,3696.8176],'ebit':[10.21/2200,.08,.11,.13,.15],'da':[.06,.06,.05,.04,.04],'ppe':[.08,.06,.05,.04,.04],'wc':.03,'dilution':.02,'multiple':25},
 'bull': {'rev':[2225,2700,3375,4050,4860],'ebit':[.02,.10,.15,.19,.21],'da':[.06,.06,.05,.04,.04],'ppe':[.075,.055,.045,.04,.035],'wc':.02,'dilution':.01,'multiple':30}},
'KRMN': {'price':30.14,'cash':54.741,'notes':868.478,'lease':102.139,'facility':150.,'shares':133.,'convert_reserve':0.,'max24':145.,'max5':175.,'prevrev':741.3,'interest':.06,'fees_y1':0.,'raise_price':15.,
 'bear': {'rev':[800,920,1012,1092.96,1180.3968],'ebit':[.15,.16,.17,.18,.19],'da':[.07,.06,.05,.04,.04],'ppe':[.06,.055,.05,.045,.04],'wc':.35,'dilution':.03,'multiple':18},
 'base': {'rev':[948.84,1167.0732,1400.48784,1652.5756512,1916.987755392],'ebit':[.20,.22,.24,.25,.26],'da':[.07,.06,.05,.04,.04],'ppe':[.04,.04,.035,.03,.03],'wc':.20,'dilution':.01,'multiple':25},
 'bull': {'rev':[1000,1300,1690,2197,2746.25],'ebit':[.22,.25,.27,.28,.29],'da':[.07,.06,.05,.04,.04],'ppe':[.04,.035,.03,.03,.03],'wc':.15,'dilution':.005,'multiple':30}}
}

def run(t,case):
 c=CFG[t]; a=c[case]; cash=c['cash']; notes=c['notes']; lease=c['lease']; revprev=c['prevrev']; shares=c['shares']; revolver=0.; rows=[]; earlygap=False; capbreach=False
 for i,rev in enumerate(a['rev']):
  ebit=rev*a['ebit'][i]; da=rev*a['da'][i]
  interest=notes*c['interest']+lease*.0729+revolver*.07
  tax=max(ebit-interest,0)*.25
  wc=max(rev-revprev,0)*a['wc']
  if case=='bear': wc+=([100,40,20,0,0] if t=='AVAV' else [20,20,10,0,0])[i] # assumed slower cash collection / stranded inventory
  if t=='AVAV' and case=='base' and i==0:
   wc=ebit-interest-tax+da-rev*a['ppe'][i]+89.19 # fixes Y1 company FCF to flagged FY27 forecast
  sbc=rev*(.02 if t=='AVAV' else .005)
  if t=='AVAV' and case=='base' and i==0: wc+=sbc # preserve Y1 forecast calibration
  ocf=ebit-interest-tax+da+sbc-wc
  ppe=rev*a['ppe'][i]; companyfcf=ocf-ppe
  software=rev*.01 if t=='AVAV' else 0.
  awardtax=rev*(.0175 if i==0 else .01) if t=='AVAV' else rev*.005
  leaseprincipal=min(5.009,lease) if t=='KRMN' else 0.
  lease-=leaseprincipal
  cashfcf=companyfcf-software-awardtax-leaseprincipal
  uf=companyfcf-software-awardtax+interest*.75
  due=min(notes,8.64+(4.516 if i==0 else 0)) if t=='KRMN' else (747.5 if i==3 else 0)
  notes-=due
  cash+=cashfcf-due-(c['fees_y1'] if i==0 else 0)
  shares*=1+a['dilution']
  draw=raise_amt=newshares=0.
  if cash<50:
   draw=min(50-cash,c['facility']-revolver); cash+=draw; revolver+=draw
  if cash<50:
   if i<2: earlygap=True
   else:
    raise_amt=50-cash; newshares=raise_amt/c['raise_price']; cash+=raise_amt; shares+=newshares
  voluntary=0.
  if t=='KRMN' and cash>50 and cashfcf>due:
   voluntary=min(notes,cash-50,.5*(cashfcf-due));notes-=voluntary;cash-=voluntary
  if revolver>0 and cash>50 and cashfcf>due:
   repay=min(revolver,cash-50,.5*(cashfcf-due));revolver-=repay;cash-=repay
  fd=shares+c['convert_reserve']
  if (i<2 and fd>c['max24']) or fd>c['max5']:capbreach=True
  rows.append(dict(year_end=f'{2027+i}-10-15',revenue=rev,ebit_margin=a['ebit'][i],ebit=ebit,da=da,sbc_addback=sbc,cash_interest=interest,cash_tax=tax,working_capital_use=wc,ocf=ocf,cash_ppe=ppe,company_fcf=companyfcf,software_cash=software,award_tax_cash=awardtax,finance_lease_principal=leaseprincipal,cash_fcf_after_other_uses=cashfcf,terminal_unlevered_cash_fcf=uf,mandatory_note_principal=due,voluntary_note_principal=voluntary,revolver_draw=draw,equity_raise=raise_amt,new_issued_shares=newshares,ending_cash=cash,ending_notes=notes,ending_finance_leases=lease,ending_revolver=revolver,fully_diluted_shares=fd))
  revprev=rev
 r=rows[-1]; ev=max(r['terminal_unlevered_cash_fcf'],0)*a['multiple']; debt=notes+lease+revolver; eq=max(ev+cash-debt,0); value=eq/r['fully_diluted_shares']; tr=(value/c['price'])**.2-1 if value>0 else -1
 return dict(rows=rows,terminal_multiple=a['multiple'],terminal_ev=ev,terminal_cash=cash,terminal_debt_finance_leases_revolver=debt,terminal_equity=eq,terminal_share_value=value,annualized_return=tr,conditional_H4_ceiling=value/1.2**5,early_funding_gap=earlygap,share_cap_breached=capbreach,company_fcf_margin_year5=r['company_fcf']/r['revenue'],capex_to_ocf_year5=r['cash_ppe']/r['ocf'],net_debt_to_company_fcf_year5=(debt-cash)/r['company_fcf'])
res={t:{k:run(t,k) for k in ['bear','base','bull']} for t in CFG}
data={'as_of':'2026-10-15','price_as_of':'2026-10-14 close','units':'USD million except share values; shares million','assumptions':CFG,'scenarios':res,'failure_case':{'equity_value':0,'return':-1,'loss_at_initial_H_portfolio_cap':.006,'loss_at_initial_H_sleeve_cap':.025},'limitations':['Annual Oct15 buckets use fiscal-year evidence as proxies, not a verified consensus NTM roll.','Cash begins at reported Aug1 AVAV and June30 KRMN balances adjusted known campus/holdback/Walker/assumed fees; missing interim OCF means not current cash.','All future margins, working capital, dilution, capital allocation, funding prices and terminal multiples are analyst assumptions; terminal peer-multiple support incomplete.','AVAV cash principal747.5 repaid2030; full2.319M initial-conversion-share reserve conservatively retained alongside cash principal; unverified make-whole maximum prevents a verified contractual maximum.','All modeled operating-lease rent is in EBIT/OCF. Finance-lease interest and principal explicitly funded; remaining finance-lease debt subtracted at terminal.','No future M&A assumed. No dividends; accumulated cash added only once to terminal EV.','Future equity funding, if needed after first24months, is a sensitivity, not committed liquidity.','Insider and legal checks remain incomplete: this model does not authorize an entry.']}
(OUT/'defense_model.json').write_text(json.dumps(data,indent=2)+'\n')
lines=['\n## Explicit annual H3/H4 sensitivities (researcher assumptions, not consensus)\n','The reproducible model is `defense_model.py`, with full inputs/outputs in `defense_model.json`. All dollar and share totals below are millions. These are annual buckets ending Oct 15, 2027–2031. The first buckets use fiscal-year evidence as proxies, not a verified NTM roll. Cash starts from the last reported balance adjusted for known transactions: AVAV $547.384M after campus and paid holdback; KRMN $54.741M after Walker financing/purchase and an assumed $2M fee. Neither is asserted to be actual Oct 15 cash.\n','Anchors: AVAV issuer FY27 revenue $2.125–$2.225B; vendor FY27 $2.20B, FY28 $2.54B and FY27 FCF −$89.19M ([forecast](https://stockanalysis.com/stocks/avav/forecast/)). KRMN issuer FY26 revenue $730–$745M / capex $35–$38M and vendor FY26/FY27 revenue $741.30M/$948.84M ([forecast](https://stockanalysis.com/stocks/krmn/forecast/)). AVAV base Y1 company FCF is calibrated to the vendor forecast; later cash forecasts are entirely our estimates.\n','OCF = EBIT − cash interest − 25% cash tax on positive EBIT after interest + D&A + assumed noncash SBC − incremental working-capital use. Company FCF = OCF − all cash PP&E. Funding cash further deducts capitalized software, award-tax cash settlements and finance-lease principal. Noncash SBC addback is assumed at 2% of revenue for AVAV and 0.5% for KRMN; award-tax cash settlement is separately funded, and ordinary dilution is modeled. D&A assumptions and all operating margins are explicit in JSON. Bear working capital adds cash-collection/stranded-inventory stress of $100/$40/$20/$0/$0M for AVAV and $20/$20/$10/$0/$0M for KRMN on top of the incremental-revenue requirement; this prevents lower sales from mechanically becoming a stronger cash case. Operating rent remains in operating expenses. Terminal EV uses unlevered cash FCF after software/award cash costs; add retained cash once and subtract notes, drawn revolvers and remaining finance leases. No dividends, repurchases or further M&A are assumed; future capacity additions are assumed funded through modeled cash PP&E rather than new finance leases. This annual H3/H4 path does not apply H2’s 25% overrun buffer or prove quarterly liquidity: the separate H2 stress remains binding.\n','| Name / scenario | FY31 value | 5Y annualized return | Conditional 20% hurdle ceiling | FY31 company FCF margin | FY31 net debt / company FCF | Funding / cap flags |\n|---|---:|---:|---:|---:|---:|---|']
for t in CFG:
 for case,r in res[t].items():
  lines.append(f"| {t} {case} | ${r['terminal_share_value']:.2f} | {r['annualized_return']:.1%} | ${r['conditional_H4_ceiling']:.2f} | {r['company_fcf_margin_year5']:.1%} | {r['net_debt_to_company_fcf_year5']:.2f}× | first24 gap={r['early_funding_gap']}; cap breach={r['share_cap_breached']} |")
for t in CFG:
 lines += [f'\n### {t}: annual assumptions and cash/share bridge\n','| Case / year | Revenue | EBIT margin | Cash PP&E | ΔWC use | Company FCF | Cash after other uses | Mandatory note principal | Optional note principal | New equity $ | End cash | End debt + finance leases | FD shares |\n|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
 for case,r in res[t].items():
  for x in r['rows']:
   debt=x['ending_notes']+x['ending_finance_leases']+x['ending_revolver']
   lines.append(f"| {case} {x['year_end'][:4]} | {x['revenue']:.1f} | {x['ebit_margin']:.1%} | {x['cash_ppe']:.1f} | {x['working_capital_use']:.1f} | {x['company_fcf']:.1f} | {x['cash_fcf_after_other_uses']:.1f} | {x['mandatory_note_principal']:.1f} | {x['voluntary_note_principal']:.1f} | {x['equity_raise']:.1f} | {x['ending_cash']:.1f} | {debt:.1f} | {x['fully_diluted_shares']:.2f} |")
lines += ['\nAVAV assumptions: annual ordinary dilution 3%/2%/1% bear/base/bull on an assumed 52M economic starting-share allowance, plus a conservative constant 2.319M conversion reserve. Model share limits: **60M at 24 months; 85M at deadline**. The reserve is intentionally conservative: principal is still paid $747.5M cash in 2030 even though normal net settlement issues only conversion value above principal. Make-whole terms and all awards are not fully verified, so these proposed monitoring caps are not a verified contractual maximum. Revolver use is limited to the reported $336.981M commitment; any later assumed equity is priced $60, unavailable as present H2 liquidity. The annual base company FCF crosses 6% in Y2, has positive OCF throughout, and terminal capex/OCF and net leverage satisfy numeric cash tests; it still requires current and forward organic-demand / insider / legal / G5 validation.\n','KRMN assumptions: beginning notes include $100M Walker debt, plus $102.139M finance leases. Annual note rate 6%, finance lease 7.29%, revolver 7%; scheduled term principal $8.64M annually plus $4.516M other notes in Y1; finance-lease principal $5.009M annually. Half available cash FCF after mandatory note principal is used for optional deleveraging, with a $50M minimum cash balance. These capital-allocation choices are assumptions, not promises. Ordinary share dilution 3%/1%/0.5% bear/base/bull on a 133M starting allowance; model caps **145M at 24 months; 175M at deadline**. Later equity, if required, is priced $15 and does not count toward current funding. Base company FCF already clears 6% in Y1 and the terminal cash/capex/leverage metrics fit a prospective G destination; actual completed-year cash evidence and the remaining G tests must still be earned.\n','**Interpretation:** both base operating transitions can reach several numeric G cash-quality targets, but this particular base valuation sensitivity does not clear H4’s 20% hurdle at the Oct14 price. The printed conditional ceilings are outputs of *assumed* 18×/25×/30× bear/base/bull unlevered-FCF multiples, not fully supported intrinsic entry ceilings: profitable-peer validation is incomplete. A different supported operating/multiple case could change that judgment. Do not call either a proven universal valuation failure or an approved H entry. The previous “no annual model” gap is partly addressed by this transparent researcher model; input support, current funding/legal/insider evidence and full route qualification remain unresolved.\n','A separate failed-commercialization / invalidated-transition case sets equity to **zero** (−100%). At maximum initial H size that is a loss of 0.60% of portfolio / 2.5% of sleeve, or 1.25% / 5% at the total per-name caps. Annual ending balances do not prove intra-year funding sufficiency; the separate H2 slower-revenue stress and current-balance/covenant reconciliation remain required. No probabilities or guaranteed drawdown limits are assigned. H5 unknown means **$0 new capital** regardless of these model values.\n']
section='\n'.join(lines)+'\n'
(OUT/'defense_model_tables.md').write_text(section.rstrip()+'\n')
for t in res:
 print(t,{k:{'value':round(r['terminal_share_value'],2),'cagr':round(r['annualized_return']*100,2),'conditional_ceiling':round(r['conditional_H4_ceiling'],2),'earlygap':r['early_funding_gap'],'capbreach':r['share_cap_breached']} for k,r in res[t].items()})
