# Oct 24, 2026 — 52-name triage (revision 7 with amendments)

- Scope: the user's list of popular stocks and their distance from 52-week highs, plus GOOGL and UBER. Quotes: Oct 23 close from stockanalysis Statistics/Forecast pages (MRCY Oct 22; EOSE intraday).
- Method: `triage.py` runs hard-gate kill tests for A–E, G, M and D from the page fields; `d_return.py` gives framework C return estimates for survivors (out-years faded where consensus is paywalled, so high-growth estimates are mechanical and optimistic). Issuance terms, insiders, #19, PH and full G5/H models were not run for most names; "headline pass" and "watch" mean exactly that.
- Proxy caveat: the triage reads stockanalysis "buyback yield" (net share change), so names with gross buybacks but SBC dilution (AVGO, AMD) can show false A1/A2 flags; AVGO's held-core status stands.
- Mandatory H check: every out name carries an H line. "H-watch at best" means H would be the only route and its first visible blocker is named; a full H review was run only for NBIS and IREN.

| Ticker | Oct 23 | Verdict | Deciding evidence | H check | Next |
|---|---|---|---|---|---|
| NVDA | $210.96 | **Core, headline pass** | FCF 41.9%, shares −1.0%, net cash, fwd P/E 17.4, PEG 0.35, PT +56%. Return ~51% (FY2028 base $15.91; later years faded from 71%, unverified). Open: #7 annual insider sweep; OpenAI commitment in A4 at maximum; AI-capex factor headroom. | n/a (cash engine) | Nov 18 print |
| TSM | $418.51 | **Core, headline pass** (3a or NTM capex test) | FCF 30%, net cash $100B, fwd P/E 19.6, EPS growth ~35–42%; trailing capex/OCF 52.7% needs the NTM guide or 3a(Q2) (OCF margin 62%). Return ~26% (faded). Open: PEG like-for-like, Taiwan insider disclosure (#7 non-US), Oct 15 print vs consensus. | n/a | #7 via local filings; #19 on Oct 15 |
| ASML | $1,571.80 | **Core, headline pass** | FCF 54%, shares −1.3%, net cash, fwd P/E 24.7, EPS +36% next year, PT +37%. Return ~27% (faded). Open: AFM insider check (#7 non-US), Oct 14 print vs consensus, 5Y median fwd P/E. | n/a | #7, #19 on Oct 14 |
| CRDO | $147.29 | **D-watch, strongest D candidate** | Core out on A1 (DustPhotonics stock, +2.5% shares). D: FCF 27.6%, D/E 0.01, growth 56% 3Y / 87% / 55%, fwd P/E 20.2, PEG 0.40. D return ~42% with 2.5%/yr dilution restated (FY28 $9.69 single source, lower than fade). Open: DustPhotonics G3 test (small: $169M stock + ≤3.21M contingent shares), A7 (Jun–Jul officer sales), #19, A5. | n/a | Nov 30 print |
| MRVL | $228.51 | **D-watch** | Core out on A1 (+2.6%). D: FCF 18.3%, D/E 0.29, growth 57% / 47% / 63%, fwd P/E 40.4, PEG 0.72. D return ~50% (faded, mechanical). Open: Celestial AI deal (27.2M shares at close Feb 2, 2026; earnout to ~$5.5B total, form unknown) must pass G3's 24-month FCF/share test. | n/a | Dec 1 print |
| BE | $193.30 | **D-watch** | Shares +33% (note exchanges). Nov 2025 $2.2B 0% 2030 converts at $194.97 (52.5% premium; proceeds to exchanges and capex) pass D1(c)'s premium and purpose tests. FCF 11.4%, D/E 1.42, growth 72% / 124% / 56%, fwd P/E 39.9, PEG 0.43. D return ~35% with 5%/yr dilution. Open: full FDSO model, A5, A7, Oct 22 print. | n/a | D1 model; #19 |
| VRT | $194.32 | **D-watch + #19 blackout** | A1/A2 fail core (no buybacks). D: FCF 25.5%, D/E 0.70, growth 29% / 37% / 30%, fwd P/E 24.5, PEG 0.61; UIG earnout is cash. D return 24.1–25.3% (borderline: depends on whether consensus share counts include SBC). Q2 revenue miss blocks entry until a clean print. | n/a | Oct 28 print (#13) |
| LITE | $756.17 | **D-watch** (Oct 24) | D5(b) 21.8% governing; clears 25% at ≤~$700. | n/a | Nov 5 print |
| SKHY | $137.02 | **G-watch** | Core A1 out to Jul 10, 2027 (ADR listing issuance). D fails D5(b): ~24% return at a flat ~3–4× multiple. G: FCF 48%, net cash; needs G1, G4 (DART) and a cyclical G5 model. | n/a | Oct 28 print |
| MU | $877.55 | **G-watch** | A1 +1.6% with net dilution fails core; D4 fails (next-year growth 15.7%). G: FCF 44%, net cash, shares ≤3%; needs a cyclical G5 five-year model. | n/a | — |
| NOW | $158.96 | **Ballast candidate** | Passes A, #9 and #11 (P/E 35.1, PEG 1.44, FCF yield 2.8%); fails only #12 (PT −1.5%, FCF yield <5%). | n/a | Oct 28 print (#13) |
| AMD | $516.79 | **Alert (#11)** | Fwd P/E 46.5 vs 45 and FCF yield 1.0% vs 1.15% on the high-velocity path; D5(a) misses on P/E by 1.5. P/E 45 ≈ $500. | n/a | Nov 3 print |
| ALAB | $257.16 | **D near-miss** | Shares +7.8% (SBC); fwd P/E 45.8 vs 45 (≈$253 line); FCF 23%, growth 65% / 124% / 56%. | n/a | Nov 3 print |
| GOOGL | $320.21 | M-watch | M2(d) FY2027 FCF margin unresolved vs $195–205B 2026 capex. | n/a | Oct 28 print |
| AMZN | $248.00 | Out of M (M2(d)) | FY27 FCF margin ~−0.9% (Oct 20). | n/a | Oct 29 print |
| AVGO | $321.68 | Held core | Return ~29% (Oct 22). | n/a | Dec 10 print |
| UBER | $66.70 | Waiver (#10) | Return ~16%; #10 EPS leg re-check. | n/a | Nov 4 print |
| COHR | $209.29 | Out of D (D2) | OCF $79.5M on $7.1B revenue; FCF −$1.02B; shares +26%. | n/a (established business) | Nov 4 print |
| MRCY | $75.56 | Out | G2 leverage: net debt ~4.2× FCF; growth ~10%. | n/a | Nov 10 |
| INTC | $86.96 | Out | FCF 4.96%; shares +13.3%; net debt. | n/a | Oct 29 |
| ARM | $210.33 | Out | Fwd P/E 88, PEG 2.90. | n/a | Nov 4 |
| AMKR | $39.30 | Out | Negative FCF; growth 12%. | n/a (mature) | Oct 26 |
| TSLA | $372.22 | Out | FCF 3.2%; fwd P/E 175; M2(a) OCF margin 18% < 20%. | n/a | — |
| SYM | $39.28 | Out | Shares +18.6%; fwd P/E 57.5. | n/a | Nov 23 |
| PLTR | $196.75 | Out | Fwd P/E 103; PT +5%. | n/a | Nov 2 |
| CRWD | $257.57 | Out | Fwd P/E 182; shares +3.2%; growth 23%. | n/a | Dec 1 |
| SNOW | $325.43 | Out | Operating loss; fwd P/E 129; shares +3.4%. | n/a | Dec 2 |
| SNDK | $1,238.03 | Out | A5 (five-player NAND) in every route; shares +6.9%. | n/a | Oct 29 |
| SPCX | $147.49 | Out of M (M1) | Shares +117% from its 2026 IPO: financing issuance inside 12 months; FCF −$39B on $55B capex. | n/a (OCF positive; issuance ban governs) | 12 months after IPO |
| NBIS | $158.74 | Out of D; **H-watch** | Operating loss; net debt/EBITDA 8.3×. | H-watch (Oct 24 review) | Nov 10 |
| IREN | $24.91 | Out of D; **H-watch + #19 blackout** | Operating loss; ~51× EBITDA. | H-watch (Oct 24 review) | Nov 5 |
| CRWV | $54.24 | Out | D/E 10.3; FCF −$13.7B; shares +76%. | H-watch at best; leverage and dilution are the blockers | Nov 9 |
| HUT | $61.23 | Out | D/E 4.4; negative OCF. | H-watch at best; leverage | Nov 4 |
| CORZ | $13.10 | Out | Negative FCF; operating loss. | H-watch at best; funding | Nov 5 |
| AAOI | $67.51 | Out | Shares +49%; FCF −$0.90B. | H-watch at best; dilution | Nov 5 |
| AEHR | $55.31 | Out | Small, loss-making. | H-watch at best | Nov 2 |
| RKLB | $52.60 | Out | Shares +15.7%; negative FCF. | Out of H on H5 (insider sales ~1.33%, Oct 15) | Nov 9 |
| ASTS | $39.79 | Out | Shares +39.7%; FCF −$1.64B. | H-watch (Oct 15; #19(a) history) | Nov 9 |
| PL | $13.41 | Out | Shares +11.5%; FCF margin 6.5% but G3 fails; cap < $10B for D. | H-watch (Oct 15) | Dec 9 |
| IONQ | $31.27 | Out | Shares +50%; operating loss −$0.94B. | H-watch at best; dilution path | Nov 5 |
| RGTI | $11.52 | Out | Revenue $13M; shares +32%. | H-watch at best; H1 demand thin | Nov 9 |
| QBTS | $11.66 | Out | Revenue $12M; shares +40%. | H-watch at best; H1 demand thin | Nov 5 |
| QUBT | $6.56 | Out | Revenue ~$10M; shares +74%. | Out of H on H1 (no binding demand evidenced) | Nov 13 |
| AVAV | $123.19 | Out | Shares +52%; negative FCF; growth ~11–15%. | H-watch (Oct 15) | Dec 8 |
| KTOS | $38.68 | Out | Shares +15%; negative FCF. | H-watch at best; dilution | Nov 3 |
| ONDS | $6.20 | Out | Shares +297%. | Out of H on dilution (H4 share limits) | Nov 12 |
| OKLO | $26.35 | Out | Revenue $1.2M; shares +30%. | Out of H on H1 (no realized revenue or binding offtake shown) | Nov 6 |
| SMR | $5.38 | Out | Shares +132%; revenue $11M. | Out of H on H1/H4 | Nov 5 |
| LEU | $102.45 | Out | Growth ~0–5%; shares +31%; negative FCF. | H not applicable (established business) | Nov 4 |
| UUUU | $7.52 | F-out, PH-impaired | Commodity; F1 fails. | F-only (no H) | Nov 6 |
| EOSE | $1.71 | Out | Shares +40%; FCF −$0.42B. | H-watch at best; funding | Nov 5 |
| NVTS | $8.38 | Out | Shares +20%; next-year growth 4%. | H-watch at best; H1 | Nov 3 |

## Sources
- stockanalysis Statistics and Forecast pages for each ticker (Oct 23–24, 2026), e.g. [NVDA](https://stockanalysis.com/stocks/nvda/forecast/), [CRDO](https://stockanalysis.com/stocks/crdo/forecast/), [MRVL](https://stockanalysis.com/stocks/mrvl/forecast/), [VRT](https://stockanalysis.com/stocks/vrt/forecast/), [BE](https://stockanalysis.com/stocks/be/forecast/), [TSM](https://stockanalysis.com/stocks/tsm/forecast/), [ASML](https://stockanalysis.com/stocks/asml/forecast/), [SKHY](https://stockanalysis.com/stocks/skhy/forecast/). Raw fields: `batch1.json`–`batch4.json`.
- Bloom Energy 2030 converts: [Business Wire, Oct 30, 2025](https://www.businesswire.com/news/home/20251030137221/en/Bloom-Energy-Corporation-Prices-Upsized-2.2-Billion-Convertible-Senior-Notes-Offering).
- Marvell–Celestial AI terms: [technologies.org](https://technologies.org/marvell-mrvl-turns-celestial-ai-into-product-and-the-5-5-billion-earnout-clock-is-now-running/), [8-K/A](https://www.sec.gov/Archives/edgar/data/1835632/000119312526032861/d45933d8ka.htm).
- Earlier evidence: roster Oct 15/22/24 sections; Oct 24 route D and H research.

## Fundamental floor prices (Oct 24, user request)

Definition: the highest price at which the framework C return still reaches **25% a year** if (a) every forward year's EPS growth comes in 5 points below the consensus/faded path and (b) the stock ends year 3 at **20× forward earnings**, about a market-average multiple. Dilution is restated as in D5(b) (CRDO 2.5%/yr, VRT 1%/yr, BE 5%/yr, LITE 0.6%/yr, AVGO 1%/yr). The "fair" column keeps consensus growth with the same 20× exit. These sit beside the rules: the D5(a) P/E-45 ceilings (CRDO ~$328, VRT ~$356, BE ~$218, LITE ~$980) are far above, and VRT/CRDO's base D5(b) return does not depend on price while the exit equals entry. Out-years are mostly faded, so treat the floors as framework outputs, not forecasts.

| Name | Oct 23 | Floor (stress, 20×) | Fair (consensus, 20×) | User's level |
|---|---|---|---|---|
| CRDO | $147.29 | ~$163 | ~$181 | $141 |
| VRT | $194.32 | ~$157 | ~$178 | now (blocked until the Oct 28 print) |
| BE | $193.30 | ~$124 | ~$138 | $160 |
| LITE | $756.17 | ~$567 | ~$631 | — (D5(b) ceiling ~$700) |
| AVGO | $321.68 | ~$360 | ~$405 | held core |
