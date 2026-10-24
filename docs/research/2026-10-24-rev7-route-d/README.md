# Oct 24, 2026 — route D (revision 7) re-test: LITE, CIEN, COHR, NBIS, IREN

- Framework: Oct 24, 2026 revision 7 (route D, with the 1.99× D/E cap and the D2(c) capex-cycle branch).
- Quotes: Oct 23, 2026 close. Market data from stockanalysis Statistics/Forecast pages pulled Oct 24; filings and press as linked.
- HWM yardstick (D5(d)): ~15.4% framework C estimate from the Oct 22 roster → D line ~20.4%; HWM 3Y revenue CAGR ~15%. D's 25% floor binds first.
- Return math: `d_return.py` with `inputs.json`; output in `results.txt`.
- Verdict: **no D-growth pass today.** CIEN and LITE are D-watch (LITE after P14 was adopted later the same day). COHR, NBIS and IREN fail D2.

## Summary

| Name / Oct 23 close | Route status | Deciding evidence | Numeric unlock / next event |
|---|---|---|---|
| **CIEN — $320.26** | **D-watch** (closest) | Passes D1–D4, D5(a), D5(d), #19. Fails #12 by $1.54. D5(b) unresolved: 32.9% with no exit cap, but the 5Y median fwd P/E was not obtainable and decides it (24.0% at 25×, 15.1% at 20×). | Close ≥ 0.8 × 200DMA (today $321.80, falling); 5Y median fwd P/E or FY28+ consensus showing D5(b) ≥25%; A5/A7 check; Dec 10 print. |
| **LITE — $756.17** | **D-watch** (after P14) | Before P14: out on D1(c), NVIDIA's $2.0B 1:1 preferred at $695.31 had ~0% premium. P14 passes it as an at-VWAP strategic placement (~$695.89 approximate 5-day VWAP). D5(b) fails: 21.8% governing (28.4% on the higher FY28 source). Everything else passes. | D5(b) ≥25% at ≤~$700 on the governing path (stress 20.6%), or verified higher FY28–29 consensus; Nov 5 print. |
| **COHR — $209.29** | **Out of D (D2)** | FY26 OCF $79.5M (1.1% margin) after an inventory/receivables build; FCF −$1.02B. Fails D2(a) and D2(c)(1). Leverage, growth and valuation pass. | OCF margin ≥20% with positive op income and FY+2 FCF consensus ≥6%, or FCF margin ≥6%. Nov 4 print. |
| **NBIS — $158.74** | **Out of D (D2(c), D5(a))** | TTM GAAP operating loss −$507.3M; net debt/EBITDA 8.3× vs 2.5×; no forward P/E. Passes the 1.99× D/E cap (0.99). | Operating profit, net debt ≤2.5× EBITDA, FY+2 FCF ≥6%. H is its route. Nov 10 print. |
| **IREN — $24.91** | **Out of D (D2(c), D5(a))** | TTM operating loss −$378.8M; net debt/EBITDA ~51×; shares +41.6% YoY; no forward P/E. D/E 1.87 passes the cap. | Same as NBIS. Nov 5 print. |

Capital: CIEN, LITE and COHR are AI/optical exposure and would carry the shared "AI capex 2027" trigger inside the 60%/25% factor cap. Current cost basis of the factor group is unknown, so even a pass gets zero capital until headroom is measured (#16).

## CIEN / Ciena — D-watch

- **D1 dilution:** shares +0.39% YoY (stockanalysis). June 11, 2026 0.00% 2031 convert, $2.875B, conversion $746.66, ~60% premium at pricing, with note hedge and warrants ([8-K](https://www.sec.gov/Archives/edgar/data/0000936395/000119312526267607/d118604d8k.htm), [pricing release](https://www.sec.gov/Archives/edgar/data/0000936395/000119312526267607/d118604dex991.htm)). ~$1.14B repaid the term loan; remainder to buybacks/general purposes ([8-K](https://www.sec.gov/Archives/edgar/data/0000936395/000119312526260665/d125730d8k.htm), [Boardroom Alpha](https://www.boardroomalpha.com/sec/cien-8-k-2026-06-11-0001193125-26-267607)). Out of the money at $320 → no FDSO add. Passes D1(a)–(c).
- **D2 cash:** TTM OCF $1.05B − capex $240.3M = FCF $814.4M, 13.53% margin ✓. NTM FCF consensus not pulled; trailing trend and FY27 margin targets make >0 likely (flagged).
- **D3 leverage:** cash $2.63B, debt $3.29B, net debt $442M ≈ 0.5× TTM FCF ✓; D/E 1.07 ✓ (stockanalysis).
- **D4 growth:** FY26 consensus $6.42B, +34.7% (15 analysts, stockanalysis); FY27 $8.45B, +31.4% ([Trefis, Oct 22](https://www.trefis.com/stock/cien/articles/619911/is-ciena-stock-really-expensive/2026-10-22)); management's FY27 floor $8.3–8.4B; 3Y revenue CAGR 31.95% ✓.
- **D5(a):** fwd P/E 30.77, PEG 0.42 ✓.
- **D5(b) return:** base FY27 EPS $10.41 (implied by the 30.77 fwd P/E at $320.26). FY28–FY30 consensus not visible → faded from the 45.2% FY26→FY27 seed (38.4%, 32.7%, 27.8%) → FY30 $24.42, 3Y EPS CAGR 32.9%. Exit multiple: lower of entry 30.76× and 35×; the 5Y median fwd P/E cap could not be retrieved (GuruFocus page not reachable; Trendlyne shows only a trailing 5Y average of 76.9×). Results: **32.9%** uncapped; 24.0% at 25×; 15.1% at 20×. Stress (−5 pts/yr) 27.9% uncapped. Unresolved until the median is sourced.
- **D5(d):** 32.9% > ~20.4% and 31.95% > ~15% ✓ (subject to D5(b)).
- **#12 fails by $1.54:** 200DMA $402.25 → PT leg void below $321.80; close $320.26. FCF yield 1.79% < 5%. The PT ($512.99, +60%) would otherwise pass.
- **#19 clear (Sep 3):** revenue $1.67B vs $1.63B consensus and above the $1.625B guide midpoint; adj EPS $2.11 vs $1.72; Q4 guide midpoint $1.75B = consensus ([SentiSense](https://app.sentisense.ai/stories/ciena-posts-record-q3-revenue-on-ai-demand-as-stock-fluctuates-09032026)).
- **Open:** A5 top-two evidence and NTM GM vs FY25; A7 annual insider totals; PH ATH date (price is below the 200DMA; the 52-week gain of +94.7% rules out a ≥3-year-old ATH, so not impaired).

## LITE / Lumentum — D-watch (D1(c) cleared by P14; D5(b) open)

- **D1(c) fails:** Mar 2, 2026, NVIDIA bought 2,876,415 Series A convertible preferred shares at $695.31 ($2.0B), 1:1 into common ([8-K](https://www.sec.gov/Archives/edgar/data/1633978/000119312526085412/d41019d8k.htm)). LITE traded near its then-52-week peak of ~$765 and rose ~5% on the news ([MEXC/CoinCentral](https://www.mexc.com/news/835533)), so the conversion premium was roughly zero, below the ≥30% rule. Purpose (fab, capacity, R&D per [Let's Data Science](https://letsdatascience.com/news/nvidia-invests-2b-in-lumentum-for-ai-optics-9dfee32c)) and non-survival status pass. The Sep 3, 2025 $1.1B convert ([pricing](https://www.businesswire.com/news/home/20250903825830/en/Lumentum-Announces-Pricing-of-1.1-Billion-Convertible-Notes-Offering/)) and the Apr/May 2026 convert-for-stock exchanges (debt retirement) do not fail the test. P14 (adopted Oct 24, 17:23 CT) then passes it: 5-day VWAP Feb 23–27, 2026 ≈ $695.89 from daily typical prices ([Yahoo history](https://finance.yahoo.com/quote/LITE/history/?period1=1771545600&period2=1772582400)), so $695.31 is at VWAP within data precision; 1:1, no coupon, pro rata liquidation, NVIDIA is a customer/partner.
- **D1(a)/(b) pass:** FDSO ≈102.5M = 90.58M basic + 2.88M preferred + ~7.5M net convert shares at $756.17 (2032 notes $187.77, 2029 $69.54, 2028 $131.03, 2026 $99.29; cash principal, shares for the excess per the [FY26 10-K](https://www.sec.gov/Archives/edgar/data/0001633978/000162828026057358/lite-20260627.htm); principals approximated from carrying values, flagged) + awards. Matches the ~102M diluted shares in Q1 FY27 guidance ([MarketBeat](https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/?.tsrc=rss)). Projected growth <1%/yr. The ~40% trailing jump in diluted shares (72.0M → 101.1M, [Finsee](https://finsee.ai/earnings/lite/2026/q4/en/)) is sunk under D1(a).
- **D2(a):** TTM OCF $751.4M − capex $451.3M = FCF $300.1M, 9.96% ✓. The −230% GAAP profit margin is the one-time $7.8B non-cash loss on converting the old notes; GAAP operating margin is 17.8%.
- **D3:** net cash $1.07B; D/E 0.36 ✓.
- **D4:** FY27 revenue $6.34B, +110% (23 analysts); FY28 +55.5% ([Trefis](https://www.trefis.com/stock/lite/articles/617928/what-is-the-true-hidden-price-of-lumentum-stock/2026-10-08)); 3Y CAGR 66.9% ✓.
- **D5(a):** fwd P/E 34.71, PEG 0.30 ✓.
- **D5(b):** base FY27 EPS $21.79 (23 analysts). FY28: $32.69 (Trefis net income +50%) or $34.65 ([Webull](https://www.webull.com/news/15707188920058880) EPS +59%); they agree within 10%, so the year is usable and the lower governs. FY29–30 faded. Exit capped at ~22.18×, the approximate 5Y median fwd P/E from [GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/LITE) quarterly snapshots (Sep 2021–Jun 2026; approximate). Restated for dilution: **21.8%** governing (28.4% on the higher FY28); stress 17.5% (24.1%). Fails 25% on the governing figure. Without the median cap: 41.8%. Entry ceiling for 25% on the governing path: ≈$700 (stress 20.6% there).
- **#12** ✓: PT $1,179.07 (+55.9%, 26 analysts); PT leg valid above $630.43.
- **#19:** Q4 adj EPS $3.23 vs ~$2.99 and above the $2.85–3.05 guide ([Crypto Briefing](https://cryptobriefing.com/lumentum-1b-revenue-beats-earnings-ai-growth/)); revenue and Q1 guide vs consensus not verified (open). **#13:** Nov 5 print, nine trading days out.
- **PH:** closing ATH $1,133.40 on Oct 6, 2026 ([stockanalysis history](https://stockanalysis.com/stocks/lite/history/)); drawdown −33.3%; ATH 18 days old → not impaired.

## COHR / Coherent — out of D on D2

- FY26 OCF $79.5M (−87.5% YoY), capex $1.103B, OCF − capex −$1.02B; inventory +79.5% to $2.58B and receivables +39.3% ([TS2](https://ts2.tech/en/coherent-stock-cohr-drops-6-despite-beat-as-cash-flow-falls-87/), [stockanalysis](https://stockanalysis.com/stocks/cohr/statistics/)). D2(a) fails; D2(c)(1) needs ≥20% OCF margin vs 1.1%.
- Passes elsewhere on stockanalysis figures: D/E 0.32; net debt $1.56B / EBITDA $1.42B = 1.1×; operating income $901.5M (12.7%); fwd P/E 22.30, PEG 0.42; 3Y revenue growth 38.9%; PT +88.6%.
- Shares +26.3% YoY, mostly NVIDIA's $2B March investment ([Techleap/Dealroom](https://finder.techleap.nl/news/feed/nvidia-invests-4b-in-photonic-makers-lumentum-and-coherent)); terms not verified, so D1(c) is unresolved as well.
- Unlock: working capital turning back into cash. Nov 4 print.

## NBIS / Nebius — out of D on D2(c) and D5(a)

- [stockanalysis](https://stockanalysis.com/stocks/nbis/statistics/): TTM revenue $1.36B, operating income −$507.3M (−37.4%), EBITDA $258M, OCF $5.26B (customer prepayments), capex $11.14B, FCF −$5.88B; cash $8.04B, debt $10.20B, net debt $2.15B; D/E 0.99; shares +22.1% YoY; no forward P/E.
- Fails D2(c)(1) (operating loss), D2(c)(5) (net debt/EBITDA 8.3×) and D5(a). Passes the 1.99× D/E cap. Debt kept rising: $10.06B by June plus $5.75B of August converts ([TIKR](https://www.tikr.com/blog/nebius-debt-hits-10-billion-does-the-balance-sheet-support-streets-290-price-target-heres-what-analysts-say), [Nebius 6-K](https://www.sec.gov/Archives/edgar/data/0001513845/000110465926100347/tm2623863d1_ex99-1.htm)).
- H is the only route that fits a funded pre-profit build-out; not run here. Nov 10 print.

## IREN — out of D on D2(c) and D5(a)

- [stockanalysis](https://stockanalysis.com/stocks/iren/statistics/): TTM revenue $707.0M, operating income −$378.8M (−53.6%), EBITDA $38.4M, OCF $2.10B, capex $4.33B, FCF −$2.23B; net debt $1.94B (~51× EBITDA); D/E 1.87; shares +41.6% YoY; no forward P/E.
- Passes the 1.99× D/E cap. Fails D2(c)(1), D2(c)(5) and D5(a). Nov 5 print.

## Unverified / open

- CIEN 5Y median forward P/E; CIEN FY28+ consensus EPS; CIEN NTM FCF consensus; CIEN A5/A7.
- LITE FY29–30 consensus (faded); exact convert principals and any capped calls; Q4 revenue and Q1 guide vs consensus; A5/A7.
- COHR NVIDIA placement price/premium; FY+2 FCF consensus.
- NBIS/IREN D1 forward dilution not modeled (fails earlier gates).
- AI-capex factor group cost basis (blocks capital for any pass).

## H reviews (mandatory H check, adopted Oct 24, 17:27 CT)

### IREN — H-watch + #19 blackout

- **H1 passes.** Realized AI cloud revenue $128.8M in FY26 (mining $578.2M) and binding demand: Microsoft definitive ~$9.7B five-year contract (20% of each tranche prepaid; Microsoft can terminate after a cure period for missed delivery) ([8-K](https://www.sec.gov/Archives/edgar/data/1878848/000114036125040072/ef20058139_8k.htm)); RPO $5.1B plus ~$11.4B contracted lease value at Jun 30, 2026 ([10-K](https://www.sec.gov/Archives/edgar/data/0001878848/000187884826000052/iren-20260630.htm)). Horizon 1 delivered Aug 2026. Operating ARR ~$1B vs a $4B year-end target ([FY26 release](https://www.sec.gov/Archives/edgar/data/0001878848/000187884826000051/irenreportsfy26results.htm)).
- **H2 not met (H-watch).** FY27 capex guide $25–30B. Committed sources: unrestricted cash $5.90B, undrawn Microsoft GPU facilities $2.71B, Mackenzie financing up to $2.4B (draw status unknown), prepayments not yet received ~$1.3B (derived, unverified) ≈ $12.3B. The FY27 gap alone is ~$12.7–17.7B before FY28 capex and H2's 25% buffer. Management's plan relies on an ~$8B GPU-financing/prepayment target, data-center financing (none closed) and "corporate sources", and the $6B ATM has ~$3.5B left; H2 counts none of these. A funded slower build plan is not disclosed.
- **H3/H4 unresolved.** FY27 FCF consensus −$21.4B (stockanalysis); EPS consensus negative through FY28 (4 analysts); no FY29+ consensus. Fully diluted shares ~447–465M today (+13.5% to +18.1% over 394.1M basic), ~563M if every convert converts, ~593M with NVIDIA's 30M rights at $70. No base-case path to G3's 3% dilution limit or a dated 6% FCF margin is supportable from disclosed data, so no five-year per-share model or entry ceiling is issued.
- **H5 / #19.** No open-market insider sales in the last 12 months (Form 4s are Jul 1 RSU grants); the co-CEOs' Sep 2025 sales (1.0M shares each) fall just outside the window. Q4 FY26 adjusted EBITDA $19.2M vs $34.9M consensus (−45%; a second source says ~53% below) is a #19(b) miss → **blackout** until a clean print. Revenue $137.2M vs $139–140.4M (−1.3% to −2.3%; one source shows $157.1M).
- **PH:** closing ATH ~$76.41 on Nov 5, 2025; drawdown −67.4%; below both moving averages. ATH under 3 years old → not impaired.
- **Next:** Nov 5 print (#19 all legs); disclosed FY27 funding closes; a funded capex plan.

Sources for this section: [IREN data pack sources: 10-K, FY26 release, Microsoft 8-K above; stockanalysis IREN](https://stockanalysis.com/stocks/iren/statistics/); [MarketBeat call summary](https://www.marketbeat.com/instant-alerts/transcript-iren-q4-earnings-call-highlights-2026-08-27/); [parameter.io on the Q4 miss](https://parameter.io/iren-iren-stock-dips-6-despite-strong-ai-revenue-growth-analysts-call-it-a-buy/); [Newsquawk](https://www.newsquawk.com/headlines/iren-iren-q4-2026-usd-revenue-137mln-exp-139mln-fy-revenue-707mln-exp-7403mln).
