# Taiwan deep check: TSM and Winbond (2344.TW)

Screen date Sat Oct 24, 2026. Rules read: framework.md rev 8 (A1, A3/3a, #7, #19, C return), stage-paths.md rev 8 (G2/G3, M0, D0-D5), price-health.md. Calcs: `tw_calc.py`, `tw_ret.py` in this folder. No repo files edited.

## Verdicts

- **TSM: out of core (A3(c) fail). No alternate route available.** 3a is closed by Q3 (2023 revenue fell). M is closed by M0 (same 5-year revenue test). G fails G2 (same ≤50% capex/OCF test). D does not apply (no issuance). H does not apply (has a cash engine). Everything else checked passes.
- **Winbond: out.** It fails A1 (US$750M convert, Mar 2026) and fails D1(c) because the convert priced at a 10.0% conversion premium against the 30% minimum. G3 also fails: period-end shares are up 4.90%, above the 3% cap. The "+0.95%" headline is a lagging WASO figure.

## 1. TSM (ADR $418.51; 5 sh/ADR; USDTWD 32.5853)

### 2026 capex guidance
- US$60-64B. Raised Jul 16 from $52-56B and reiterated on the Oct 15 Q3 call. Sources: [Newsquawk Jul 16](https://www.newsquawk.com/headlines/tsmc-tsm2330-tt-q3-guidance-usd-revenue-at-446-458bln-exp-426bln-gross-margin-66-67-exp-659-2026-capex-60-64bln-prev-saw-52-56bln), [Q3 transcript via Webull](https://www.webull.com/news/15751044230423552).
- Jan-Sep spend: $40.64B, so the Q4 residual is $19.4-23.4B ([Xenospectrum](https://xenospectrum.com/en/tsmc-q3-2026-gross-margin-capex/)).
- Q3 capex: NT$443B ($13.8B).
- Q3 OCF: about NT$903B per the transcript, but NT$920B per [TradingNews](https://www.tradingnews.com/news/tsm-slides-to-413-usd-on-chip-rout-as-q4-guide-points-to-58-percent-growth). The two sources conflict.

### 2027 capex
- No company figure. The CFO called it "a bit too early" and said 2026-28 capex will be "significantly higher than the past three years."
- Pre-print Bloomberg survey average: $75B ([StockHub/Newspim](https://stockhub.kr/en/news/news_4de4710ddfb2)).
- Post-print brokers ([TrendForce Oct 16](https://www.trendforce.com/news/?p=65394)):
  - Morgan Stanley: $83B for 2027, $92B for 2028
  - GS and BofA: $85B for 2027
  - UBS: $90B for 2027, $105B for 2028
- MarketScreener consensus ([financials](https://in.marketscreener.com/quote/stock/TSMC-TAIWAN-SEMICONDUCTOR-6492349/finances/)), TWD m (analyst count not shown; consensus page blocked):
  - Capex: 1,991,411 (2026), 2,553,775 (2027, about $80B), 2,948,382 (2028)
  - FCF: 1,454,764 / 2,262,058 / 3,089,583

### A3(c): guided/consensus capex vs NTM OCF
- OCF = FCF + capex, same vendor:
  - FY26: 3,446B, capex/OCF **57.8%**
  - FY27: 4,816B, **53.0%**
  - FY28: 6,038B, **48.8%**
- NTM blend (0.25 FY26 + 0.75 FY27): 2,413 / 4,473 = **53.9%**. Time-weighted: 53.7%.
- Q4'26 guided residual + 0.75×FY27 consensus: **56.3-58.0%**.
- With 2027 capex at the $75B Bloomberg survey: NTM **55.2%**. At broker $83-90B: **59-63%**.
- stockanalysis basis (FY26 FCF consensus NT$1.45T + $62B guide midpoint): **57.5-57.9%**.
- NTM OCF ≈ NT$4.47-4.61T, or **US$141-145B**.
- **Fail on every consensus basis.**
- Alternative reading, flagged for the caller:
  - The framework's vague-guidance default (trailing capex $50.54B × 1.25 = $63.2B) would give about 45% and pass.
  - I did not use it. Sources rule: that default applies only when falling back to company guidance, and consensus capex exists ($75-90B range).
  - Using it would mean picking the weaker source to get a pass.

### 3a eligibility
- Q1 passes: NTM OCF about $141B, well above $50B.
- Q2 passes: FY27 OCF margin about 63%; NTM gross margin about 66-67%, above 60%.
- **Q3 fails:**
  - 2023 revenue NT$2,161.74B, down 4.5% YoY ([TSMC Dec 2023 revenue report](https://pr.tsmc.com/english/news/3098)).
  - USD 2023 decline (about -8.7%): unverified this session. Not needed, since the NT$ decline already fails.
- **3a unavailable.** It reopens only once FY2028 is reported (window 2024-28, about Jan 2029). M0 has the same timing.
- Re-entry trigger (ordinary A3(c)): NTM consensus capex/OCF ≤50%.
  - FY28 consensus is 48.8%, so the NTM blend crosses about 50% around Q3 2027.
  - That assumes 2027-28 capex consensus does not rise. Brokers are already above consensus.

### #19: Q3 2026 print (Oct 15)
- (a) Revenue NT$1,494.24B vs LSEG SmartEstimate NT$1.46T (19 analysts): **+2.35%, pass**. Sources: [TrendForce Oct 8](https://www.trendforce.com/news/?p=65041), [TSMC PR](https://pr.tsmc.com/english/news/3346).
- (b) EPS:
  - ADR EPS $4.60 vs $4.42: **+4.1%** ([TradingNews](https://www.tradingnews.com/news/tsm-slides-to-413-usd-on-chip-rout-as-q4-guide-points-to-58-percent-growth))
  - Net income NT$763.06B vs NT$746.3B (LSEG SmartEstimate, 16 analysts): +2.25%; vs NT$739.5B: +3.2% ([Euronews](https://www.euronews.com/2026/10/15/taiwan-chip-giant-tsmc-says-net-profit-hit-record-in-third-quarter))
  - **Pass**
- (c) Revenue $46.72B vs own guide $44.6-45.8B: **above the high end, pass**.
- (d) Q4 guide $52.3-54.3B (midpoint $53.3B):
  - Reported as "above analyst estimates" ([TradingNews](https://www.tradingnews.com/news/tsm-slides-to-413-usd-on-chip-rout-as-q4-guide-points-to-58-percent-growth); [Goldesel](https://goldesel.de/aktien/news/tsmc-aktie-q4-umsatzprognose-ubertrifft-markterwartungen))
  - No published consensus figure found
  - Implied Q4 consensus: about US$50.4B, derived from the FY26 revenue consensus of NT$5.466T ([TIKR](https://www.tikr.com/ja/blog/tsmc-posts-a-sixth-straight-record-quarter-and-its-q4-guide-says-the-ai-boom-isnt-slowing-heres-the-fuller-picture)). That puts the guide about **5.8% above**. Derived; the timing of that consensus is unconfirmed.
  - **Pass**
- FY26 guide raised to about 44% USD growth.
- **#19 clear.**

### #7: insiders (12 monthly 6-Ks, Oct 2025-Sep 2026, all read)
- Filings: [Oct25](https://www.sec.gov/Archives/edgar/data/1046179/000104617925000133/tsm-monthend6kx20251125.htm), [Nov25](https://www.streetinsider.com/SEC+Filings/Form+6-K+TAIWAN+SEMICONDUCTOR+For%3A+Nov+30/25772832.html), [Dec25](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000012/tsm-monthend6kx20260123.htm), [Jan26](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000021/tsm-monthend6kx20260225.htm), [Feb26](https://www.stocktitan.net/sec-filings/TSM/6-k-taiwan-semiconductor-manufacturing-co-ltd-current-report-foreign--9f035093f6f8.html), [Mar26](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000205/tsm-monthend6kx20260424.htm), [Apr26](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000292/tsm-monthend6kx20260526.htm), [May26](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000377/tsm-monthend6kx20260625.htm), [Jun26](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000459/tsm-monthend6kx20260724.htm), [Jul26](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000545/tsm-monthend6kx20260825.htm), [Aug26](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000660/tsm-monthend6kx20260924.htm), [Sep26](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000728/tsm-monthend6kx20261022.htm).
- Decreases:
  - Lora Ho (SVP): -10,000, Oct 2025, method not stated
  - VP Arthur Chuang: -200,000, May 2026, market sale per [Chinatimes](https://wantrich.chinatimes.com/news/20260625900314-420101)
  - VP Arthur Chuang: -1,000,000, Jun 2026, gifts to family per [LTN](https://ec.ltn.com.tw/article/paper/1762165) (not a market sale)
- Increases: +1.76M shares in total, mostly stock awards in the Mar and Sep 2026 filings.
- Net: **+549k (net buying)**.
- Gross dispositions: 0.0047% of 25.94B shares. Market sales: ≤0.0008%. The 1.5% cap is about 389M shares.
- Officer test: at most 1 officer with a disposal in any quarter.
- Pledges: none.
- National Development Fund (director): no changes reported.
- **Pass.**

### EPS consensus per ADR, for the return check
- FY26: NT$110.13/share = $16.90 ([stockanalysis](https://stockanalysis.com/stocks/tsm/forecast/?d=20261024); 41 analysts).
- FY27:
  - NT$148.61 = **$22.80** (stockanalysis)
  - NT$148.1 = $22.72 (MarketScreener)
  - $22.30 (TIKR, FX basis unclear)
  - Two sources agree.
- FY28: NT$188.2 = **$28.88** (MarketScreener only; analyst count unverified).
  - It lowers the estimate versus fading (27.1% growth vs 29.7% faded), so it is usable but flagged.
- Return:
  - Base FY27 $22.80, FY28 consensus, then fade (23.0%, 19.6%), entry and exit 18.35×, dividend 0.97%: **24.1%**
  - Mechanical full fade: 26.4%
  - Stress (-5pt): 19.1%
  - Passes the 20% guardrail (EPS CAGR 23.2% and revenue CAGR 36.5% also pass). Moot given the A3 fail.
- 5Y median forward P/E: unverified. TIKR shows a chart average of 19.32× over an unstated window, so it would not bind.

### Other
- ADV $4.67B (screen).
- 52W high $487.47 (TradingNews, date not given). Price is above the 200DMA ($397.63).

## 2. Winbond (2344.TW)

Price: NT$154.50 is the **Oct 22** close ([stockanalysis](https://stockanalysis.com/quote/tpe/2344/history/?d=20261024), wearn, nstock). No Oct 23 row was found on any source, so the Oct 23 close is unverified.

### Share-count driver (A1 / D1)
- **4th overseas unsecured convertible bond:**
  - US$750M, zero coupon, 1-year, SGX-listed, issued Mar 31, 2026
  - Conversion price NT$109.45, adjusted to NT$108.94 on Apr 4; fixed FX 32.027
  - Source: [2026Q1 consolidated report, note 19c](https://www.winbond.com/export/sites/winbond/about-winbond/investor/financial-information/financial-reports/financial/2026Q1-Consolidated-Financial-Report-EN.pdf)
- **Premium at pricing: 7.5-10% range; final 109.45 / 99.50 = 10.0%** ([Communications Today](https://www.communicationstoday.co.in/?p=401016); [S&C](https://www.sullcrom.com/About/News-and-Events/Highlights/2026/March/SC-Advises-Initial-Purchasers-Winbond-Electronics-750-Million-Convertible-Bond-Offering)).
- Use of proceeds: foreign-currency equipment for capacity expansion. Not survival financing (about NT$62B cash).
- Called for early redemption on Aug 12, 2026 under the 120% trigger ([Chinatimes Jul 13](https://wantrich.chinatimes.com/news/20260713900629-420101)).
- **Full conversion:**
  - The 2026 "cash capital increase" line rose NT$2.2049B at par = **220.49M shares**, exactly US$750M × 32.027 / 108.94 ([Fubon capital table](https://fubon-ebrokerdj.fbs.com.tw/z/zc/zcb/zcb_2344.djhtm))
  - Shares issued now **4.721B** (paid-in capital NT$47.204B; [cnyes](https://www.cnyes.com/twstock/2344)), vs 4.500B at Mar 2025 / Dec 2025 / Mar 2026
  - **+4.90% period-end YoY**
  - stockanalysis's 4.50B and +0.95% are stale
  - The Yahoo TW profile still shows 4,500,000,193 as of Sep 9 (registration lag)
- No restricted stock awards or employee share issuance disclosed (Q1 report).
- **Pending issuance** (board resolution Sep 16; [Yahoo TW announcements](https://tw.finance.yahoo.com/quote/2344.TW/announcement)):
  - Domestic 4th unsecured CB up to **NT$14B**, 0%, 5-year
  - Domestic 5th unsecured CB up to **NT$4B**
  - Conversion terms deferred until regulatory approval, so the maximum share count is unknown
  - Estimated about 90-117M shares (1.9-2.5%) at NT$155-200 conversion prices. Estimate only.
- Also pending: an all-cash acquisition of Infineon's NOR/F-RAM business for **US$1.12B (about NT$35.6B)**, closing 2H27 ([StorageNewsletter](https://www.storagenewsletter.com/?p=305665), [TrendForce](https://www.trendforce.com/news/?p=64219)).
- Route results:
  - **A1: fail** (convert in trailing 12 months, plus pending converts)
  - **D1(c): fail** (10.0% premium < 30%)
  - D1(a)/(b) would be D-watch anyway (pending CB maximum shares unknown)
  - **G3: fail** (4.90% > 3%)

### Other D tests (for the record; D already fails)
- D0 passes: about US$22.4B market cap on 4.72B shares; non-FT.
- D2(a)/(b) pass: TTM FCF margin 22.1%; FY26 FCF consensus NT$62.7B, FY27 NT$196B.
- D3 passes:
  - Net debt NT$8.3B
  - Pro forma Infineon about NT$44B, roughly 0.3× NTM FCF
  - Debt/equity 0.41
- D4 cannot be verified: FY26 has **3 analysts** ([stockanalysis forecast](https://stockanalysis.com/quote/tpe/2344/forecast/?d=20261024)), below the ≥5 required. FY27 has 7 analysts ([Simply Wall St](https://simplywall.st/stocks/tw/semiconductors/twse-2344/winbond-electronics-shares/future)).
- D5(a) passes: forward P/E 3.63, PEG 0.02.
- Return estimate (below):
  - Base 27.6% ≥25%
  - Stress 22.6% ≥20%
  - HWM yardstick 20.4% cleared
- A5 contested:
  - Winbond leads NOR (about 34% combined post-Infineon per TrendForce)
  - But specialty DRAM (CMS) is 53% of revenue, and the prior roster call was #5 fail (commodity memory)
- #7: not checked; MOPS insider transfers unverified.

### EPS consensus and return
- FY26: NT$25.42 (3 analysts).
- FY27: **NT$52.55** (7 analysts).
- FY28: **NT$69.28** (1 analyst; [MarketScreener](https://ca.marketscreener.com/quote/stock/WINBOND-ELECTRONICS-CORPO-6491617/finances/)).
  - FY28 revenue NT$679.2B (+39.7%)
  - Inconsistency: FY28 net income 377.2B / 69.28 implies 5.44B shares, which doesn't reconcile. Flagged.
- Broker dispersion in August ([Chinatimes Aug 7](https://wantrich.chinatimes.com/news/20260807900125-420101)):
  - KGI: FY26 NT$29, FY27 NT$69.9
  - Hongyuan: NT$23.68 / NT$43.57
  - Capital: NT$24.85 (FY26)
- Return:
  - Base FY27; FY28 consensus at +31.8% (lowers the estimate vs the 90.7% fade, so usable but flagged at 1 analyst); then fade to 27.0% and 23.0%; entry and exit 2.94×; dividend 0.32%
  - **27.6%**
  - Stress: 22.6%
  - Scenario where FY28 is the peak and earnings stay flat after: 10.0%
  - The earlier mechanical full fade (77.8%) is not credible
  - D dilution restatement does not change the result: it scales every year by the same factor, and exit multiple = entry multiple
- Cycle view:
  - Winbond expects 2027 to be tighter than 2026
  - Customers are negotiating long-term agreements into 2029-30 ([TrendForce Aug 7](https://www.trendforce.com/news/2026/08/07/news-winbond-says-customers-seek-ltas-through-2030-adata-expects-even-tighter-dram-supply-in-2027/))
  - Brokers expect smaller price gains in 2H26
  - No dated analyst call on the cycle peak found
- 5Y median forward P/E: **unverified**. It would bind only if below 2.94×.

### #19
- Q3 2026 not yet reported; investor conference **Nov 3**. That is about 6 trading days out, so re-test after the print.
- Q2 2026 (Aug 6) ([Winbond PR](https://winbond.com/hq/about-winbond/news-and-events/news/news00582.html)):
  - Revenue NT$59.84B (+184.7% YoY), already known from monthly revenue reports
  - Gross margin 66.2%
  - EPS NT$5.40, "significantly better than expected" (Chinatimes), but no consensus figure was found
  - **Unresolved** (missing comparison ≠ pass)

### PH
- ATH set in 2026:
  - Jan 2026 record NT$136; NT$158 called an all-time high on May 29 ([ETtoday](https://finance.ettoday.net/news/3174228))
  - 52W / 10Y high **NT$233.50 intraday**, set between Jun 1 and Aug 10, 2026 (the max high from Aug 11 to Oct 22 was 193)
  - **Exact closing ATH and date: unverified.** At least 188 (Sep 8 close); June-end close about 208 (derived from histock yield)
- Drawdown at Oct 22: **-18% to -34%**.
- ATH is under 5 months old, so **no PH-warning or impairment possible**.
- 3Y price return: MarketScreener +592.46% to Oct 2 (179.00) implies about NT$25.85 base, so about **+498%** at 154.5. Benchmark not fetched; immaterial with a fresh ATH.
- Price is above the 200DMA (139.57) but below the 50DMA (173.6).

### Liquidity
- 20-day average volume 66.0M shares × about NT$165 ≈ **US$334M/day**. Screen figure: US$313M. Investing.com 3-month average: 131M shares.
- **Passes the ≥$25M floor.**
