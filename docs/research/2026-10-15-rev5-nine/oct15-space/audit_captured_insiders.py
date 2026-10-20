"""Sum captured market-code S/P rows; unknown filings are never assumed zero."""
import json,pathlib
root=pathlib.Path(__file__).resolve().parent
for ticker in ['RKLB','ASTS','PL']:
 data=json.loads((root/(ticker+'-insiders.json')).read_text())
 sales=buys=0
 for filing in data['filings']:
  for row in filing.get('trades',[]):
   if row['code']=='S':sales+=float(row['shares'])
   if row['code']=='P':buys+=float(row['shares'])
 print(ticker,'filings',data['filings_count'],'errors',len(data['errors']),'captured S',sales,'captured P',buys,'complete',not data['errors'])
