"""Reproduce Oct 14 close PH under Oct 15 rev5. Default: captured inputs; --refresh: network."""
import urllib.request,urllib.parse,json,datetime,concurrent.futures,pathlib,bisect,calendar
import csv,sys
B=pathlib.Path(__file__).resolve().parent
REFRESH='--refresh' in sys.argv
END=datetime.date(2026,10,14);PS=int(datetime.datetime(2026,10,16,tzinfo=datetime.timezone.utc).timestamp())
TICKERS='GFS FPS AVAV ALGM RKLB ASTS PL KRMN UUUU'.split();SPAC={'RKLB':'2021-08-25','ASTS':'2021-04-06','PL':'2021-12-08'}
def fetch(t):
 u=f'https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(t,safe="")}?period1=0&period2={PS}&interval=1d&events=div%2Csplits'
 if not REFRESH:
  info=json.loads((B/'price_inputs/sources.json').read_text())[t]
  with (B/'price_inputs'/(t.replace('^','')+'.csv')).open() as f:
   rows=[(r['date'],float(r['close']),float(r['adjclose'])) for r in csv.DictReader(f) if r['date']>=SPAC.get(t,'0000-00-00') and r['date']<=str(END)]
  return t,rows,info['meta'],u,info['events']
 j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30))
 r=j['chart']['result'][0];assert r['meta']['dataGranularity']=='1d'
 q=r['indicators']['quote'][0]['close'];a=r['indicators'].get('adjclose',[{'adjclose':q}])[0]['adjclose'];rows=[]
 for ts,c,ad in zip(r['timestamp'],q,a):
  d=datetime.datetime.fromtimestamp(ts,datetime.timezone.utc).date().isoformat()
  if c is not None and ad is not None and d<=str(END) and d>=SPAC.get(t,'0000-00-00'):rows.append((d,float(c),float(ad)))
 return t,rows,r['meta'],u,r.get('events',{})
_,br,_,bu,_=fetch('^SP500TR');bm={r[0]:r[2] for r in br}
def backmonths(m):
 y=END.year+(END.month-1-m)//12;mo=(END.month-1-m)%12+1;return datetime.date(y,mo,min(END.day,calendar.monthrange(y,mo)[1])).isoformat()
def ma(v,n):return [sum(v[i+1-n:i+1])/n if i>=n-1 else None for i in range(len(v))]
def calc(t,rows,meta,u,events):
 assert rows[-1][0]==str(END),(t,rows[-1][0]);cl=[r[1] for r in rows];md={r[0]:r for r in rows};dates=[r[0] for r in rows];ath=max(cl);ai=max(i for i,v in enumerate(cl) if abs(v-ath)<1e-7);age=(END-datetime.date.fromisoformat(rows[ai][0])).days/365.25;dd=100*(1-cl[-1]/ath)
 ma200=ma(cl,200);ma50=ma(cl,50);count=0
 for i in range(len(cl)-1,-1,-1):
  if ma200[i] is not None and cl[i]>ma200[i]:count+=1
  else:break
 ret={}
 for name,start in [('three_year',str(END.replace(year=END.year-3))),('three_month',backmonths(3)),('six_month',backmonths(6))]:
  common=[d for d in dates if d in bm and d<=start]
  if not common:ret[name]=None;continue
  d=common[-1];sr=100*(rows[-1][2]/md[d][2]-1);bret=100*(bm[str(END)]/bm[d]-1);ret[name]={'start_date':d,'stock_total_return_pct':sr,'benchmark_total_return_pct':bret,'gap_pp':sr-bret}
 impaired=age>=3 and dd>=30 and ret['three_year'] is not None and ret['three_year']['gap_pp']<=-20
 trend=(ma200[-1] is not None and len(ma200)>=220 and ma200[-21] is not None and ma200[-1]>ma200[-21]) or (ma200[-1] is not None and ma50[-2] is not None and ma50[-1]>ma200[-1] and ma50[-1]>ma50[-2])
 rel=any(ret[k] is not None and ret[k]['gap_pp']>=0 for k in ['three_month','six_month']);technical=count>=10 and trend and rel
 return {'ticker':t,'asof':str(END),'currency':meta.get('currency'),'first_operating_quote':dates[0],'rows':len(rows),'close':cl[-1],'closing_ath':ath,'ath_date':rows[ai][0],'ath_age_years':age,'drawdown_pct':dd,'relative_returns':ret,'sma200':ma200[-1],'sma200_20_sessions_ago':ma200[-21] if len(ma200)>=220 else None,'sma50':ma50[-1],'sma50_prior_session':ma50[-2],'consecutive_completed_closes_above_sma200':count,'technical_recovery_conjunction':bool(technical),'route_qualified_print_not_assumed':True,'status':'PH-impaired' if impaired else 'PH-warning' if age>=3 else 'PH-short-history' if ret['three_year'] is None else 'PH-clear-by-age','source':u,'source_events':events,'metadata_firstTradeDate':meta.get('firstTradeDate')}
results=[];errors=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 fut={ex.submit(fetch,t):t for t in TICKERS}
 for f in concurrent.futures.as_completed(fut):
  t=fut[f]
  try:
   z=calc(*f.result());results.append(z);print(t,round(z['close'],2),z['ath_date'],round(z['drawdown_pct'],2),z['status'],'above200',z['consecutive_completed_closes_above_sma200'],flush=True)
  except Exception as e:errors.append({'ticker':t,'error':str(e)});print(t,str(e),flush=True)
results.sort(key=lambda z:TICKERS.index(z['ticker']))
(B/'price_health_results.json').write_text(json.dumps({'framework':'Oct15rev5','asof':str(END),'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'benchmark':'S&P500 Total Return','benchmark_source':bu,'method':'Full split-adjusted operating-history closes for ATH/trends; dividend-adjusted stock vs total-return index on identical common start/end dates. Price-return fallback not required. SPAC shells excluded. UUUU pre-US-listing issuer continuity and 2013 share consolidation verified with primary documents linked in root_audit.md; exact 2007 USD close remains single-vendor. Offline default uses captured CSV inputs; --refresh downloads updated vendor history with the same endpoint.','results':results,'errors':errors},indent=2))
print('DONE',len(results),'errors',errors)
