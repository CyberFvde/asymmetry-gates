# Non-AI open-universe re-screen, Oct 24, 2026 (revision 8)

Verdicts and gate math: [non-ai-screen-audit.md](../../../non-ai-screen-audit.md). This folder holds the inputs and scripts.

## Files
- `data/batch_*.json`: stockanalysis fields per ticker (Oct 23 closes), 136 names in 13 lanes.
- `screen.py`: headline hard gates (A–E, FT, G, D with revision 8's D4, M scope, H flag), the framework C return (lower of fade and the 3Y EPS forecast path), the revision 8 growth door and #12 without the 200DMA void. `results.txt` is its output.
- `report.py` + `overrides.json`: builds the audit table; overrides carry deep-check verdicts and H lines.
- `d_return.py` + `deep_inputs.json`: exact returns for deep-checked names on their consensus paths.

Run: `python3 -I screen.py data/*.json` and `python3 -I report.py overrides.json data/*.json`.

## Limits
- **Next-FY correction (later on Oct 24):** the first run tested #9, G2 and D4 on the return base year (FY27 for December filers). The framework's next-FY is the year after the last completed FY (FY26 here), and D4's second leg is the year after that. `screen.py` now does this; `results.txt` and the audit table are the corrected run. No tier changed; HALO moved to Rule B.
- Headline gates use stockanalysis fields; "buyback yield" there is net share change, so A2 flags are not decisive.
- Out-year consensus beyond the forecast-page boxes was checked only for deep-check names.
- PH measured for deep-check and H-watch names only. H4 models not built.

## Deep-check sources (selection; full agent notes reproduced in the audit)
**DASH**
- [stockanalysis forecast](https://stockanalysis.com/stocks/dash/forecast/), [statistics](https://stockanalysis.com/stocks/dash/statistics/), [price history API](https://stockanalysis.com/api/symbol/s/dash/history?range=5Y&period=daily)
- [Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0001792789/000179278926000048/proddashex991-pressrelease.htm), [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001792789/000179278926000050/dash-20260630.htm), [10-Q income statement (R4)](https://www.sec.gov/Archives/edgar/data/1792789/000179278926000050/R4.htm)
- [2030 convertible closing](https://www.businesswire.com/news/home/20250530905818/en/DoorDash-Announces-Closing-of-Upsized-%242.75-Billion-Offering-of-0-Convertible-Senior-Notes)
- Consensus: [Yahoo](https://finance.yahoo.com/quote/DASH/analysis), [WallStreetZen](https://www.wallstreetzen.com/stocks/us/nasdaq/dash/stock-forecast), [Simply Wall St](https://www.simplywall.st/stocks/us/consumer-services/nasdaq-dash/doordash/future), [tickflow](https://www.tickflow.io/stock/DASH/forecast)
- Insiders: [EarningsWhispers](https://earningswhispers.com/whales/DASH/insiders), [Quantisnow](https://quantisnow.com/insiders/DASH), [Form 4 sell-to-cover example](https://www.sec.gov/Archives/edgar/data/0001792789/000189968826000014/form4-08242026_040805.xml)
- Print vs consensus: [StreetInsider](https://www.streetinsider.com/Earnings/DoorDash+%28DASH%29+Reports+In-Line+Q2+EPS/26874724.html), [KSL/Reuters](https://www.ksl.com/article/51606479/doordash-projects-strong-growth-as-delivery-demand-holds-firm)
- Share: [Walnut (Oct 2026)](https://walnutinvest.com/stocks/dash/is-it-a-buy); ATH: [chartrow](https://chartrow.com/quote/dash/drawdown)

**RHM.DE**
- [stockanalysis forecast](https://stockanalysis.com/quote/etr/RHM/forecast/), [MarketScreener finances](https://uk.marketscreener.com/quote/stock/RHEINMETALL-AG-436527/finances/), [Simply Wall St future](https://simplywall.st/stocks/it/capital-goods/bit-1rhm/rheinmetall-shares/future)
- [H1 2026 report](https://www.rheinmetall.com/en/media/news-watch/news/2026/08/2026-08-06-rheinmetall-news-half-yearly-financial-report-h1), [convertible notices](https://www.rheinmetall.com/en/investor-relations/creditor-relations/convertible-bonds), [managers' transactions](https://www.rheinmetall.com/de/investor-relations/veroeffentlichungen/managers-transactions), [May 2026 bond](https://www.rheinmetall.com/de/media/news-watch/news/2026/05/2026-05-28-rheinmetall-platziert-500-mioeur-bond)
- Guidance cut: [t-online](https://www.t-online.de/finanzen/boerse/ticker/rheinmetall-senkt-umsatzprognose-nach-f126-aus-aktie-unter-druck/0DBA0C003967E174/); voting rights: [MarketScreener](https://www.marketscreener.com/news/rheinmetall-ag-release-according-to-article-40-section-1-of-the-wphg-the-german-securities-tradin-ce7d5fd2df88f72c)

**ARGX**
- [Q3 2026 release](https://www.sec.gov/Archives/edgar/data/0001697862/000169786226000034/a02earningspressreleaseq3.htm), [H1 2026 statements](https://www.sec.gov/Archives/edgar/data/0001697862/000169786226000033/argx-20260630_d2.htm), [AFM directors' dealings](https://www.afm.nl/en/sector/registers/meldingenregisters/bestuurders-commissarissen?KeyWords=argenx), [insiderscreener](https://www.insiderscreener.com/en/company/argenx-se), [SEC EEA Form 4 relief (Cleary)](https://www.clearygottlieb.com/news-and-insights/publication-listing/sec-grants-exemptive-relief-for-foreign-private-issuers-in-certain-jurisdictions), [Q3 consensus (Investing)](https://ca.investing.com/news/earnings/argenx-slips-as-q3-operating-profit-miss-offsets-vyvgart-sales-beat-4895827), [FactSet via cnyes](https://news.cnyes.com/news/id/6563270)

**NBIX, KRYS**
- [NBIX Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0000914475/000091447526000037/nbix-20260630.htm), [NBIX forecast](https://stockanalysis.com/stocks/nbix/forecast/), [NBIX insiders](https://marketbeat.com/stocks/NASDAQ/NBIX/insider-trades), [KRYS Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001711279/000171127926000057/krys-20260630.htm), [KRYS insiders](https://www.marketbeat.com/stocks/NASDAQ/KRYS/insider-trades)

**KOG.OL, LLY, AXON**
- [KOG forecast](https://stockanalysis.com/quote/osl/KOG/forecast/), [KOG MarketScreener](https://uk.marketscreener.com/quote/stock/KONGSBERG-GRUPPEN-ASA-1413189/finances/), [KOG Q2 2026](https://kongsberg.com/news/news-archive/2026/q2-2026-kongsberg-delivers-a-strong-second-quarter-with-increased-revenue-and-solid-profitability), [KOG 2029 ambition](https://www.kongsberg.com/news/news-archive/2026/kongsberg-launches-revenue-ambitions-of-nok-100-billion-in-2029-and-nok-150-bn-in-2033/)
- [LLY forecast](https://stockanalysis.com/stocks/lly/forecast/), [LLY tickflow](https://tickflow.io/stock/LLY/forecast)
- [AXON forecast](https://stockanalysis.com/stocks/axon/forecast/), [AXON tickflow](https://tickflow.io/stock/AXON/forecast), [AXON ATH](https://www.macrotrends.net/stocks/charts/AXON/axon-enterprise/stock-price-history)

**RDDT**
- [stockanalysis forecast](https://stockanalysis.com/stocks/rddt/forecast/), [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001713445/000171344526000100/rddt-20260630.htm), [MarketBeat insiders](https://www.marketbeat.com/stocks/NYSE/RDDT/insider-trades), [WallStreetZen](https://www.wallstreetzen.com/stocks/us/nyse/rddt/stock-forecast), [therighttrader](https://therighttrader.com/earnings-calendar/rddt)

**Samsung Heavy (010140.KS)**
- [stockanalysis cash flow](https://stockanalysis.com/quote/krx/010140/financials/cash-flow-statement/), [forecast](https://stockanalysis.com/quote/krx/010140/forecast/), [Q2 2026 (Asiae)](https://view.asiae.co.kr/en/article/2026072415562434799), [Q2 consensus (StockHub)](https://stockhub.kr/en/news/news_c818f24c3e23)

**Price health**
- [DKNG drawdown](https://chartrow.com/quote/dkng/drawdown), [S&P 500 Oct 2023](https://spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-october-2023), [S&P monthly returns](https://chartrow.com/sp500/monthly-returns), [KTOS history](https://macrotrends.net/stocks/charts/KTOS/kratos-defense-security-solutions/stock-price-history), [RSI history](https://www.financialcontent.com/quote/NY:RSI/historical)

**Precious metals and takeouts**
- stockanalysis statistics/forecast per ticker; Gold Fields–Northern Star bid (businessday.co.za and miningmx.com, Sep 28, 2026); [ICE–MarketAxess](https://www.insidearbitrage.com/2026/08/nyse-parent-ice-to-acquire-marketaxess-merger-arbitrage-mondays/); [Amazon–Globalstar](https://trendspider.com/blog/gsat-stock-surges-as-amazon-confirms-90-share-globalstar-acquisition/)
