import urllib.request,urllib.parse,json,datetime,time,concurrent.futures,pathlib,bisect,csv
BASE=pathlib.Path('work/research'); BASE.mkdir(parents=True,exist_ok=True)
END='2026-10-02'; asof=datetime.date.fromisoformat(END)
TICKERS='PANW CRWD ZS FTNT TENB QLYS CHKP OKTA PODD LLY NVO REGN RMD ISRG ALGN SYK HWM WWD GE HEI RTX LMT GD NOC LHX RKLB ASTS PL RDW AVAV KTOS AXON VST CEG CCJ NVT HUBB ETN PWR EME ABB ROK SYM TER IONQ RGTI QBTS AMZN ORCL HOOD COIN TOST MELI SE XYZ SCHW TW PDD GLBE KSPI FUTU VKTX GPCR ALT'.split()
SPAC={'RKLB':'2021-08-25','ASTS':'2021-04-06','PL':'2021-12-08','RDW':'2021-09-03','IONQ':'2021-09-30','RGTI':'2022-03-02','QBTS':'2022-08-08','SYM':'2022-06-07'}
def fetch(ticker):
 p=BASE/(ticker.replace('^','')+'-daily.json');u='https://query1.finance.yahoo.com/v8/finance/chart/'+urllib.parse.quote(ticker,safe='')+'?period1=0&period2=1791072000&interval=1d&events=div%2Csplits'
 if p.exists(): j=json.loads(p.read_text())
 else:
  for n in range(2):
   try:
    b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=35).read();j=json.loads(b);p.write_bytes(b);break
   except Exception:
    if n:raise
    time.sleep(.8)
 r=j['chart']['result'][0];q=r['indicators']['quote'][0]['close'];a=r['indicators'].get('adjclose',[{'adjclose':q}])[0]['adjclose']
 rows=[]
 for ts,c,adj in zip(r['timestamp'],q,a):
  d=datetime.datetime.fromtimestamp(ts,datetime.timezone.utc).date().isoformat()
  if c is not None and adj is not None and d<=END and d>=SPAC.get(ticker,'0000-00-00'):rows.append((d,float(c),float(adj)))
 if r['meta'].get('dataGranularity')!='1d':raise ValueError('daily history not provided')
 return ticker,rows,r['meta'],u
bt,br,bm,bu=fetch('^SP500TR');bd=[x[0] for x in br];bc={x[0]:x[1] for x in br}
def val(rows,day,k):
 ds=[x[0] for x in rows];i=bisect.bisect_right(ds,day)-1
 if i<0:return None
 return rows[i][k]
def calc(t,rows,meta,url):
 if not rows:raise ValueError('no history')
 dates=[r[0] for r in rows];cl=[r[1] for r in rows];adj=[r[2] for r in rows]
 last=rows[-1];d=datetime.date.fromisoformat(last[0]);ath=max(cl);ai=max(i for i,v in enumerate(cl) if abs(v-ath)<1e-6)
 age=(d-datetime.date.fromisoformat(rows[ai][0])).days/365.25;dd=(ath-last[1])/ath*100
 y3=(d.replace(year=d.year-3)).isoformat();m6=(d-datetime.timedelta(days=183)).isoformat()
 # Align each total-return measurement to the exact same common stock/benchmark date.
 start3=max(x for x in set(dates).intersection(bd) if x<=y3) if dates[0]<=y3 else None
 start6=max(x for x in set(dates).intersection(bd) if x<=m6) if dates[0]<=m6 else None
 ret3=(last[2]/val(rows,start3,2)-1)*100 if start3 else None;bret3=(bc[last[0]]/bc[start3]-1)*100 if start3 else None
 ret6=(last[2]/val(rows,start6,2)-1)*100 if start6 else None;bret6=(bc[last[0]]/bc[start6]-1)*100 if start6 else None
 sma=[None]*len(cl);s=0
 for i,c in enumerate(cl):
  s+=c
  if i>=200:s-=cl[i-200]
  if i>=199:sma[i]=s/200
 count=0
 for i in range(len(cl)-1,-1,-1):
  if sma[i] is not None and cl[i]>sma[i]:count+=1
  else:break
 ma=sma[-1];prior=sma[-21] if len(sma)>220 else None
 gap3=ret3-bret3 if ret3 is not None else None;gap6=ret6-bret6 if ret6 is not None else None
 impaired=age>=3 and dd>=30 and gap3 is not None and gap3<=-20
 technical_recovery=count>=20 and prior is not None and ma>prior and gap6 is not None and gap6>=0
 status='PH-impaired' if impaired else ('PH-warning' if age>=3 else 'PH-clear')
 if impaired and technical_recovery:status='PH-recovery technical candidate; latest qualifying print still required'
 return {'ticker':t,'date':last[0],'close':round(last[1],4),'currency':meta['currency'],'first_operating_quote':dates[0],'rows':len(rows),'closing_ath':round(ath,4),'ath_date':rows[ai][0],'ath_age_years':round(age,3),'drawdown_pct':round(dd,3),'three_year_start':start3,'three_year_total_return_pct':round(ret3,3) if ret3 is not None else None,'benchmark_three_year_total_return_pct':round(bret3,3) if bret3 is not None else None,'three_year_gap_pp':round(gap3,3) if gap3 is not None else None,'six_month_start':start6,'six_month_gap_pp':round(gap6,3) if gap6 is not None else None,'sma200':round(ma,4) if ma else None,'sma200_20_sessions_ago':round(prior,4) if prior else None,'consecutive_above_sma200':count,'status':status,'benchmark':'S&P500 Total Return (^SP500TR)','source':url,'history_link':'https://finance.yahoo.com/quote/'+urllib.parse.quote(t,safe='')+'/history/','spac_start':SPAC.get(t)}
results=[];errors=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 fut={ex.submit(fetch,t):t for t in TICKERS}
 for f in concurrent.futures.as_completed(fut):
  t=fut[f]
  try:args=f.result();r=calc(*args);results.append(r);print(t,r['status'],r['close'],r['ath_date'],r['drawdown_pct'],r['three_year_gap_pp'],flush=True)
  except Exception as e:errors.append({'ticker':t,'error':str(e)});print(t,'ERROR',str(e),flush=True)
results.sort(key=lambda x:TICKERS.index(x['ticker']))
(BASE/'price_health_results.json').write_text(json.dumps({'asof':END,'benchmark_source':bu,'note':'Computations from full split-adjusted Yahoo daily closes and dividend-adjusted close total returns. Benchmark S&P500TR same dates. Verify quote/split consistency against governing source before any capital verdict. Technical recovery alone does not establish latest full financial-route qualification.','results':results,'errors':errors},indent=2))
with (BASE/'price_health_results.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(results[0]),lineterminator='\n');w.writeheader();w.writerows(results)
print('DONE',len(results),'errors',errors)
