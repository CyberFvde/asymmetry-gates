# Board on Nov 19, 2026 closes through the SL lens (fresh pull)

## What this is

- The 22 board names plus TSM, scored on Nov 19, 2026 closes and run through the SL three-risk lens (revision 27).
- Data: `board_pull.csv` (23 rows; sources and dates in each row's notes).
- Runner: `../../../.claude/skills/asymmetry-gates/scripts/board_from_pull.py`.
- Results: `results_repo_lens.txt` (repo lens inputs) and `results_sourced_lens.txt` (CSV lens inputs where all three are given).
- The two result files match except the header line. No row has ai, e1 and e2 all filled, so both runs use the repo's lens estimates.
- Reporting only. Not a trade instruction.

## Results (results_repo_lens.txt)

- Line 4.46. \* = under the line. Sorted by the rates plus SemiAnalysis column.
- nofv = no fair value; est = falling-estimates block; dead = dead money; <20% = Market Mondays block.

| Ticker | Close | Today | +Rates | +SemiAnalysis | +Capex peak | Why off today |
|---|---|---|---|---|---|---|
| NVDA | $145.98 | 9.12 | 8.48 | 7.45 | 4.53 | |
| TER | $227.43 | 6.56 | 6.12 | 5.50 | 0.72\* | |
| META | $596.22 | 5.67 | 4.75 | 4.75 | 4.75 | |
| GOOGL | $272.66 | 5.38 | 4.38\* | 4.38\* | 4.38\* | |
| SMTC | $101.81 | 5.64 | 5.01 | 4.38\* | 0.57\* | |
| TSEM | $127.77 | 6.20 | 5.26 | 4.37\* | 0.36\* | |
| MPWR | $1295.86 | 6.02 | 5.02 | 4.34\* | -0.06\* | |
| AVGO | $346.65 | 6.12 | 5.10 | 4.29\* | 0.29\* | |
| RMBS | $76.19 | 6.50 | 5.54 | 4.27\* | 1.07\* | |
| KLAC | $141.48 | 5.66 | 4.83 | 4.06\* | 0.94\* | |
| CDNS | $304.88 | dead | 4.36\* | 3.62\* | 3.02\* | dead money: trails UBER on return (31%) and growth (18%) |
| TSM | $352.09 | 5.84 | 4.86 | 3.58\* | 1.17\* | |
| MTSI | $218.55 | 5.31 | 4.36\* | 3.54\* | 0.35\* | |
| UBER | $65.6 | est | 3.19\* | 3.19\* | 3.19\* | falling estimates: next-year EPS -4.8% over 90 days |
| LRCX | $203.68 | 4.93 | 3.99\* | 3.07\* | 0.11\* | |
| ASML | $1356.2 | 4.51 | 3.61\* | 2.78\* | 0.31\* | |
| AMAT | $338.93 | 4.39\* | 3.51\* | 2.70\* | -0.53\* | |
| VRT | $184.99 | 5.25 | 4.33\* | 2.52\* | 0.10\* | |
| GEV | $756.28 | 4.04\* | 3.13\* | 2.20\* | nofv | |
| FIX | $1114.02 | 3.88\* | 2.93\* | 2.01\* | -0.67\* | |
| CRDO | $117.76 | 6.25 | 5.75 | nofv | nofv | |
| ALAB | $211.6 | 3.85\* | 2.98\* | nofv | nofv | |
| ANET | $189.59 | <20% | <20% | <20% | <20% | less than 20% below the high; stale: debt_ebitda |

## At or above 4.46

- **Today (16):** NVDA 9.12, TER 6.56, RMBS 6.50, CRDO 6.25, TSEM 6.20, AVGO 6.12, MPWR 6.02, TSM 5.84, META 5.67, KLAC 5.66, SMTC 5.64, GOOGL 5.38, MTSI 5.31, VRT 5.25, LRCX 4.93, ASML 4.51.
- **With rates (11):** NVDA 8.48, TER 6.12, CRDO 5.75, RMBS 5.54, TSEM 5.26, AVGO 5.10, MPWR 5.02, SMTC 5.01, TSM 4.86, KLAC 4.83, META 4.75.
- **With rates and SemiAnalysis (3):** NVDA 7.45, TER 5.50, META 4.75.
- **With all three (2):** META 4.75, NVDA 4.53.
- **Blocked today:** UBER (falling estimates), CDNS (dead money), ANET (12.5% below its high).
- **Under the line today:** AMAT 4.39, GEV 4.04, FIX 3.88, ALAB 3.85.

## What changed after the soft-spot fixes

- **No name changed sides of the line** in any column.
- **Targets:** TSEM, RMBS, ALAB, MPWR and ASML re-checked on Nov 19 pages (stockanalysis forecast page and Yahoo quote page, both at the Nov 19 close). Same averages; no rating actions after the last-updated dates. Kept.
- **pe_price:** filled for all 23. For the 16 names whose forward P/E came from the Nov 18 close, NTM EPS rises (price fell Nov 19).
  - Today column: NVDA +0.08, TER +0.04, META +0.12, GOOGL +0.14, AVGO +0.10, KLAC +0.08, LRCX +0.14, AMAT +0.13, VRT +0.18, MPWR +0.02, FIX +0.03.
  - TER's SemiAnalysis column 5.25 to 5.50; NVDA's capex-peak column 4.48 to 4.53; META's stressed columns 4.65 to 4.75; GOOGL's 4.27 to 4.38.
- **Forward P/E re-pulled at the Nov 19 close:** CRDO 16.52 to 16.14, FIX 17.87 to 17.73, ALAB 31.38 to 30.76 (stockanalysis ratios page). NTM EPS barely moves.
- **fpe_est:** TSM 18, UBER 19, ASML 34 (TIKR five-year averages).
  - TSM: no score change (the capex-peak fair value sits below price at 18x or 19x).
  - UBER: no effect (ai is 0).
  - ASML: capex-peak column 0.90 to 0.31. Its cycle factor (0.577) times NTM EPS times a 30x fair P/E lands below price, which pulls fair value down.
- **EPS:** no corrections. SMTC and TSM confirmed.
- **UBER guide gap:** stays -3.0%.

## Verification (items 4a to 4e)

- **4a SMTC:** both figures are FY2028 (Jan 2028) on the Yahoo Nov 19 page: 6.67 now, 3.93 ninety days ago (+70%). The jump follows the Aug 25 beat-and-raise. Zacks (Sep 3) shows next-year consensus going from $3.65 to $5.55 after that print. Kept.
- **4b TSM:** the fresh Yahoo table is live now: 2027 EPS 23.39 now, 22.30 a week ago, 21.28 ninety days ago. TIKR (Nov 5) also gives $23.39; Zacks (Oct 27) gives $22.44, up 6% since the Oct 15 report. Kept.
- **4c GOOGL:** stockanalysis quote page, at close Nov 19, $272.66 (-3.46%, previous close $282.44). Confirmed.
- **4d UBER:** guide midpoint $0.97 (8-K: $0.95 to $0.99). Best-documented pre-print consensus is $1.00 (Yahoo Dec-quarter estimate 30 days ago, 30 analysts; MoneyCheck also $1.00). Gap -3.0%, exactly at the line, so no guide-down. Newsquawk's $0.98 would give -1.0%.
- **4e NVDA:**
  - DOJ antitrust probe: still press reports only. Semafor (Nov 12) cited two anonymous officials; neither Nvidia nor the DOJ confirmed. The Nov 17 results release mentions only generic regulatory inquiries. The Q3 FY27 10-Q was not checked.
  - California: AG Rob Bonta issued an investigative subpoena, announced by the California Department of Justice on Nov 19 (AP). It covers possible chip or data diversion to China and whether Nvidia misled investors. Nvidia had not commented.

## Disclosed AI or data-center share

- ai filled in the CSV for six names: NVDA 0.929, AVGO 0.564, MTSI 0.443, MPWR 0.421, TER 0.60 (floor), ANET 0.263 (target).
- Repo estimates for comparison: NVDA 0.90, AVGO 0.60, MTSI 0.35, MPWR 0.30, TER 0.50, ANET 0.45.

| Ticker | Share | Period | Source (date) |
|---|---|---|---|
| NVDA | 92.9% (Data Center $107.6B of $115.8B) | Q3 FY2027, to Oct 25, 2026 | Results release (Nov 17, 2026) |
| AVGO | 56.4% (AI semis $16.7B of $29.6B) | Q3 FY2026, to Aug 2, 2026 | 8-K Ex 99.1 (Sep 2, 2026) |
| MTSI | 44.3% (Data Center $188.1M of $424.8M) | Q4 FY2026, to Oct 2, 2026 | Zacks (Nov 6, 2026); total from Nov 5 release |
| MPWR | 42.1% (Enterprise Data $506.7M of $1,202.4M) | Q3 2026 | 8-K Ex 99.1 (Oct 29, 2026) |
| TER | More than 60% AI-related (floor) | Not stated | CEO on Q3 call, via Zacks (Oct 29, 2026) |
| ANET | 26.3% (AI target $3.5B of $13.3B revenue guide) | FY2026 targets | Q3 call (Nov 3, 2026) |
| TSM | AI accelerators high-teens %; HPC 68% | 2025; Q3 2026 | Q4 2025 call via NextPlatform (Jan 16, 2026); Futurum (Oct 20, 2026) |
| FIX | Technology customers 59% (data centers and chip plants) | First nine months of 2026 | Q3 call via Zacks (Oct 26, 2026) |
| SMTC | Infrastructure 36.2% (data center plus telecom) | Q2 FY2027, to Jul 26, 2026 | Zacks via Nasdaq (Aug 26, 2026) |
| TSEM | Not disclosed as a share; SiPho target near 46% of Q4 guide (derived) | Q4 2026 target | 6-K (Nov 2, 2026) |
| GEV | Not disclosed as revenue; $2.4B data-center Electrification orders; 20% of 100 GW gas contracts | Q1 2026 | Power Engineering (Apr 23, 2026) |
| CRDO | Not disclosed | | Q1 FY27 release (Sep 1, 2026) |
| ALAB | Not disclosed | | Q3 release (Nov 3, 2026) |
| RMBS | Not disclosed | | Q3 results (Oct 26, 2026) |
| KLAC | Not disclosed | | Filings summary, sec-api.io (Nov 2, 2026) |
| CDNS | Not disclosed | | Q3 call (Oct 26, 2026) |
| LRCX | Not disclosed (none found) | | |
| AMAT | Not disclosed (none found) | | |
| ASML | Not disclosed (none found) | | |
| VRT | Not disclosed (none found) | | |

## SemiAnalysis Nov 13, 2026 revision (press summaries)

- **Source note:** Accelerator & HBM Model update, a subscriber note. Figures come from press summaries; SemiAnalysis has not confirmed them publicly.
- **Accelerator capex (previous to revised):** 2026 about $392B, unchanged; 2027 $770B to $627B (-19%); 2028 $1,054B to $758B (-28%); 2029 $1,352B to $796B (-41%); 2030 $1,531B to $923B (-40%). About $1.6T less over 2027 to 2030.
- **Nvidia compute revenue (shipments):** -22% 2027, -39% 2028, -56% 2029, -66% 2030. Power basis -14%, -35%, -50%, -59%. Feynman price about $110k to $78k.
- **Broadcom custom chips:** cumulative 2026 to 2030 ASIC revenue -11%, mostly lower prices as HBM costs fall.
- **AMD:** spend basis -11% 2027, -29% 2028, -35% 2029, -32% 2030; power basis flat 2027, then -23%, -55%, -57%.
- **Chip area (logic wafer area):** 2026 to 2030 total -17%; by year -13%, -16%, -24%, -15% (2027 to 2030). Nvidia is 66% of the cut.
- **HBM bits:** 2028 9.0 EB to 6.4 EB (-30%); 2029 10.3 to 7.9 EB (-23%); 2030 10.9 to 9.6 EB (-12%).
- **Power:** 2029 108.7 GW to 72.5 GW (-33%); 2030 122.8 GW to 80.7 GW (-34%).
- **TSMC wafers or CoWoS:** no figures in any summary found.
- **Company revenue or EPS against consensus:** none published that I found. TIKR (Nov 17) only says Nvidia's FY2029 consensus ($895B revenue) has the most to give back and FY2028 ($689B) has more cushion, with no number.
- **Sources:** [iTiger (Nov 16)](https://www.itiger.com/news/1126271736), [36Kr (Nov 17)](https://eu.36kr.com/en/p/4073175160460424), [XenoSpectrum (Nov 17)](https://xenospectrum.com/en/semianalysis-ai-accelerator-spending-forecast/), [OfficeChai (Nov 16)](https://officechai.com/ai/semianalysis-reportedly-cuts-2028-ai-accelerator-spend-forecast-by-28/), [TechNews (Nov 17)](https://finance.technews.tw/2026/11/17/ai-slowdown-research-firms-downgrade-spending-forecasts-nvidia-under-pressure/), [TIKR (Nov 17)](https://www.tikr.com/blog/semianalysis-downgrading-accelerator-capex-forecast-by-28-hours-before-nvidia-reports), [Coincamps (Nov 16)](https://coincamps.ai/article/e64148).

## Still NA or stale

- **e1, e2:** NA for all 23 names.
- **ai:** NA for 17 names (see the AI share table; GOOGL, META, UBER are 0 by design in the repo).
- **fpe_est:** NA for CRDO, ALAB, GEV. Only one-year or three-year averages were found (TIKR: CRDO 62x to 63x three-year; ALAB 72x one-year; GEV 55x one-year). Names with 20-quarter P/E history don't use it.
- **guide_gap_pct:** NA for FIX, GOOGL, GEV, CDNS, ASML (no numeric guide against consensus).
- **debt_ebitda:** NA for ANET (falls back to the Nov 4 value and prints as stale).
- **Target last-updated dates:** ASML Oct 16, RMBS Oct 27, MPWR Oct 30, TSEM Nov 3, ALAB Nov 5 (confirmed unchanged on Nov 19 pages); other names per their notes.
- **Forward P/E snapshots:** Nov 18 close for 16 names. pe_price fixes the NTM EPS math; a Nov 19 estimate change would not show.
- **Highs with no year printed:** RMBS, ALAB, SMTC, MTSI, ANET.
- **Older inputs reused:** RE inputs from the Nov 11 pull; CC, BB, HT, GP, d, bear, PB, IX, PO from earlier boards; cycle ROIC readings from Nov 4 to 6.
- **SMTC:** latest report Aug 25; it reports Nov 23.
- **Next earnings dates:** not found for 11 names.
- **NVDA:** Q3 FY27 10-Q not checked for the DOJ item.

## Known limits

- **e1 and e2 remain judgment inputs wherever the CSV leaves them NA, which is every name.** The lens columns run on the repo's estimates in `board_2026_11_19_lens.py`.
- **SemiAnalysis figures** come from press summaries of a paid note, not the note itself.
- **fpe_est values** are five-year averages; the board's own method uses a 20-quarter median. Zacks put TSM's five-year median near 21.3x (Jun 17).
- **AI shares** mix definitions: segment revenue, end markets, company targets and a floor. They are not one measure.
- **Targets:** stockanalysis and Yahoo both draw on S&P Global, so the second source is not fully independent.
- **UBER's gap** sits exactly at -3.0%. A consensus of $1.0004 or more would trip the guide-down gate.
- **Rates** are modeled only through multiples. The capex-peak case has no date.

## Sourced AI shares applied (added after review)

- `results_sourced_lens.txt` now uses each disclosed AI share in place of the repo estimate: NVDA 0.929, AVGO 0.564, MTSI 0.443, MPWR 0.421, TER 0.60, ANET 0.263.
- Only the capex-peak column moves, because the AI share sets the mid-cycle factor.
- NVDA's worst case goes from 4.53 to 4.45, which is 0.01 under the 4.46 line. TER 0.72 to 0.66, AVGO 0.29 to 0.37, MPWR -0.06 to -0.18, MTSI 0.35 to -0.03.
- e1 and e2 are unchanged everywhere. No published company-level estimate of the SemiAnalysis revision was found, so they stay judgment inputs.
- Design note: in the capex-peak case mid-cycle EPS is today's NTM EPS times the mid-cycle factor. The case-2 cut (e1) is not applied on top of it.
