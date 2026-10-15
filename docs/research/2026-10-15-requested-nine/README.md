# Requested nine-name screen, Oct 15, 2026

Names: GFS, FPS, AVAV, ALGM, RKLB, ASTS, PL, KRMN, UUUU. Framework: main `530e049`, Oct 2 revision 3 (G/H/FT revision 2, PH revision 3). Governing prices: Oct 14, 2026 completed closes. No rule changed in this screen.

## Result

- No name qualifies for capital on any route.
- Watch only, zero capital: ALGM (G-watch), PL (H-watch, #19 blackout), ASTS (H-watch, #19 blackout).
- Outside: GFS, FPS, KRMN, RKLB, AVAV, UUUU.
- Unmerged PR 3 "revision 4" (G5 10%, H4 18%, G3 3.5%, #12 4.5%) would not change any verdict here. It was checked for sensitivity only and not applied.

## Sources and limits

- Capital IQ connector not authorized. Consensus from stockanalysis (S&P Global MI) Statistics/Forecast pages; NTM cash flow from stockanalysis or MarketScreener, flagged.
- Pre-print consensus for #19 from MarketBeat, Zacks, Earnings Whispers, Yahoo and Benzinga aggregators. Provider spreads noted where material.
- Filings from SEC EDGAR (data.sec.gov submissions/XBRL, Archives). Insider counts from Form 4 XML; RKLB/ASTS totals from OpenInsider spot-checked against Form 4s.
- PH from full Yahoo daily history vs S&P 500 TR (`^SP500TR`); SPAC shells excluded. Data: [price_health_results.json](price_health_results.json), script: [price_health.py](price_health.py).

## Price health (Oct 14 close)

| Ticker | Close | Closing ATH / age | Drawdown | 3Y gap vs SPXTR | 200DMA / 20 sessions ago | PH |
|---|---:|---|---:|---:|---|---|
| GFS | 48.94 | 89.96 May 26 '26 / 0.39y | 45.6% | −97.2 pp | 54.73 / 53.67 | clear (young ATH) |
| FPS | 32.70 | 64.59 Jun 4 '26 / 0.36y | 49.4% | n/a (IPO Feb '26) | n/a | short history |
| AVAV | 120.60 | 409.83 Oct 13 '25 / 1.00y | 70.6% | −77.3 pp | 196.77 / 208.01 | clear (young ATH) |
| ALGM | 32.22 | 69.62 Jun 30 '26 / 0.29y | 53.7% | −76.3 pp | 40.63 / 39.79 | clear (young ATH) |
| RKLB | 59.18 | 150.23 May 27 '26 / 0.38y | 60.6% | +1,194 pp | 81.43 / 80.23 | clear |
| ASTS | 42.14 | 133.09 May 28 '26 / 0.38y | 68.3% | +1,192 pp | 80.28 / 81.61 | clear |
| PL | 14.13 | 51.40 May 28 '26 / 0.38y | 72.5% | +463 pp | 27.25 / 27.16 | clear |
| KRMN | 30.14 | 115.29 Jan 28 '26 / 0.71y | 73.9% | n/a (IPO Feb '25) | 67.12 / 70.73 | short history |
| UUUU | 8.34 | 235.00 Apr 13 '07 / 19.5y | 96.5% | −74.8 pp | 16.94 / 17.34 | **impaired** |

- UUUU's 2007 high is the same issuer (Energy Fuels Inc., renamed 2006, TSX history in USD). Starting at the 2013 US listing would give a $27.72 Jan 2026 high and no impairment; full public history governs.
- Every name is 45% to 74% below a 2026 high. Young ATHs mean the age condition fails, not that trend or fundamentals pass.

## ALGM, $32.22: A–E out (A1), G-watch

- A1 fails: Q1 FY27 diluted WASO 187.77M vs 184.59M (+1.72%), or +1.27% on non-GAAP diluted; period-end +0.75%. No buybacks, and FY27 growth 23% is under the 25% exception. No issuance in 12 months (Jan 2026 refinancing is a plain $285M term loan). [10-Q](https://www.sec.gov/Archives/edgar/data/866291/000119312526327128/algm-20260626.htm)
- A2 fails: zero buybacks FY26 and Q1 FY27, no authorization, net debt $115M to $142M.
- A7 flag: 12-month net sales 125,848 shares (0.07%) pass. Five officers (Doogue, Kent, Webster, Coleman, Madormo) sold May 11 to Jun 3, 2026 with no 10b5-1 footnote, which fails the officer-count test. Sell-to-cover status not established. [Doogue Form 4](https://www.sec.gov/Archives/edgar/data/866291/000119312526221669/ownership.xml)
- Pass on the numbers: FCF $87.85M / 9.29%; FY27 FCF consensus $131.0M; capex ~25% of NTM OCF; net debt/NTM FCF 1.08×; NTM GM 51.3% to 51.6% vs FY26 non-GAAP 49.4%; FY27 revenue +22.98%, 3Y CAGR 18.58%; fwd P/E 28.8, PEG 0.47.
- #12 fails: price 20.8% below the 200DMA voids the PT leg; NTM FCF yield 2.17% < 5%. PT leg returns at a close ≥ ~$32.5 (0.8 × 200DMA).
- #19 clear (Jul 30): revenue $259.2M vs $251.4M (+3.1%), above the $245M to $255M guide; EPS $0.23 vs $0.21; Q2 guide mid $270M vs $264.5M.
- G: G2 cash, leverage and growth pass; 3Y FCF/share CAGR needs FY28/29 FCF (paywalled). G3 passes (+0.75% to +1.7%). G4: only Webster sold >25% of holdings, so no cluster rejection; sale context undocumented. G5 model not built.
- Indicative G5 hurdle (not a model): 12%/yr needs $56.78 in year five, ~$10.8B equity at ~190M shares, so ~$360M FCF at 30× or ~$430M at 25×, vs FY27 consensus $131M.
- Why it fell: semis rout Jul 1 to 2; Barclays downgrade Jul 20; CFO said on the Q1 call data-center growth is "not in the 20s" and the industrial pull-in is "largely gone"; TD Cowen and Mizuho target cuts. No guidance cut, 8-K or short report.
- Next: Q2 FY27 print Oct 29 (10 trading days out). Semi name: carries the shared "AI capex 2027" trigger on entry.

## PL, $14.13: G out, H-watch, #19 blackout

- G2 fails: OCF FY25 −$14.4M (two positive years not met); FY27 FCF consensus −$29.1M vs trailing +$24.7M; FY27 capex guide $100M to $115M vs ~$80M implied OCF. Trailing FCF margin 6.52% (5.25% if capitalized software is included).
- G3 fails: period-end shares +11.5%, Q2 diluted WASO +18.2% (ATM 3.78M shares / $122.4M plus 11.1M warrant shares).
- H1 passes: revenue +58%, RPO $753.1M, Pelican-11 launched, Tanager-2 and 18 SuperDoves launched Oct 1.
- H2 passes on a flagged model: $865.4M cash vs ~$194M stressed 24-month need; 2030 converts outside the window.
- H3 unresolved: no sourced FY28 to FY31 FCF, capex or share path; $1.378B ATM capacity remains.
- H4 fails at $14.13: 20%/yr hurdle $35.16 needs ~$530M to $630M FY32 FCF at ~450M shares; consensus extrapolation gives 7% to 11%/yr. Indicative ceiling ~$8 to $9 (flagged model).
- H5 passes: 12-month insider sales 1,583,170 shares (0.435%), no cluster; legal matters settled or accrued.
- #19(d): Q3 guide midpoint $103M vs ~$114.0M to $114.3M aggregator consensus (−9.7%). Material miss; blackout until a clean print. Revenue $116.1M vs ~$104.5M and adj EPS $0.02 vs −$0.02 beat. Consensus source is an aggregator, so verify pre-print consensus before relying on the size of the miss.
- Since Oct 2: −19%; no 8-K; Barclays initiated Hold $17 (Oct 8); two director 10b5-1 sales; small ESA pilot (Oct 13). [Release](https://www.sec.gov/Archives/edgar/data/1836833/000119312526381874/pl-ex99_1.htm), [10-Q](https://www.sec.gov/Archives/edgar/data/1836833/000119312526382016/pl-20260731.htm)

## ASTS, $42.14: H-watch, #19 blackout, #17 re-test

- #19(a): Q2 revenue $31.5M vs $34.5M consensus (−8.7%). Blackout until a clean Nov 9 print (Q3 revenue ≥ ~$45.1M needed per agent estimate).
- #17: FY27 revenue consensus fell 10.6% ($650.8M to $581.7M).
- H1 partial: 13 BlueBirds in orbit, FCC commercial authorization Apr 21, TTM revenue $115M, Q2 service revenue $7.1M; $1.3B backlog not reconciled to contracted obligations.
- H2 fails: est. Sep 30 cash ~$2.81B vs 24-month buffered need $4.10B to $5.52B; gap $1.3B to $2.7B. Japan J-LEO subsidy (~$1B) not final, excluded. Dependence on uncommitted funding keeps it H-watch.
- H4 fails: hurdle $104.86 needs ~$2.9B FCF by 2031 at ~520M post-funding shares (~470M now incl. ~$4.17B converts, estimated).
- H5 open: officers/independent directors net 0.08%. Rakuten (director box marked) sold 3.04M in April (0.86%); with American Tower's 2.29M, 1.45%. See pending P12.
- Legal: securities class action filed (W.D. Tex. 26-cv-00378, class period Mar 2025 to Jul 2026); lead-plaintiff deadline Nov 13.
- Why it fell (−27.9% since Oct 2): FCC cleared SpaceX direct-to-phone (Oct 8), SpaceX bought Grain low-band spectrum (Oct 9), Piper Sandler cut to Neutral $54 (Oct 13). BlueBirds 14 to 16 at Cape Canaveral, no launch date.

## GFS, $48.94: A–E out (A1), G out (G2)

- "Trump bought" is a U.S. government equity stake, not a personal trade. Sep 3: 9,907,399 new shares to Commerce at $37.8505 (~$375M). Oct 14: ~4% more equity tied to reallocating $955M of the CHIPS award; share count, price and close date not disclosed. A $300M silicon-photonics LOI adds ~1%. [Oct 14 release](https://www.sec.gov/Archives/edgar/data/1709048/000170904826000252/gfpressreleasefinal.htm), [Sep 3 exhibit](https://www.sec.gov/Archives/edgar/data/0001709048/000170904826000239/exhibit44-fx3asr.htm)
- Trump OGE 278-T filings through Sep 17, 2026 show no GFS line (OCR search; September trades not yet filed). F2 credit does not apply: GFS is not F-routed and this is not a politician's own trade.
- A1 fails on the issuance (diluted WASO 556M vs 557M is otherwise −0.2%). Also failing: A3b (NTM FCF $731M < $796M), A3c (capex 66% of NTM OCF), A5 (#5 foundry, ~3.3% share, [TrendForce](https://www.trendforce.com/presscenter/news/20260909-13225.html)), #9 (FY26 +7.6% incl. acquisitions, 3Y 11.3%), #10.
- Passing: A2 ($400M buybacks H1), A3a (11.5%), A4 (net cash $1.63B), #11 (22.15×, PEG 0.85), #12 (PT +52.6%).
- A7/G4: officers and directors 0.01%. Mubadala sold 50.8M shares (9.1%) as a >10% holder; counting it fails. See pending P12.
- G1 provisional pass (single-sourced design wins, comms/datacenter +62%, SiGe sold out through 2027; company-sourced). G2 fails: capex 66% of NTM OCF, FY26 growth 7.6%, FCF/share +4.7%/yr. G3 likely fails once government shares issue (~+5.3%). G5 fails: base 5.3%/yr at 15× FCF (10.2% at 20×); indicative ceiling ~$36 (15×) to ~$45 (20×), unsourced multiple.
- #19 clear (Aug 5): revenue $1,786M vs ~$1.76B to $1.77B, above the $1,735M to $1,785M guide; adj EPS $0.46 vs $0.43; Q3 guide mid $1,885M vs ~$1.87B.
- Why it fell: Mubadala 22M-share block May 26 (−9.8% next day); semis multiple compression June to July; Q2 FCF −$3M and capex ~20% of revenue; government shares priced at $37.85.
- Next: Nov 4 print (Q3 guide $1,885M ± $25M). Semi name: shared "AI capex 2027" trigger on entry.

## FPS, $32.70: A–E out (A1), G out (G2), out of H (H5)

- A1 fails: Class A shares issued in the Feb 5 IPO and Mar 30, Jun 1, Jul 6 follow-ons (19.1M, 10.8M, 15.9M, 14.6M). Proceeds bought sponsor units, so total shares stayed 304.43M. Rule fails as written; rolls off Jul 2027. See pending P13.
- A3(a)/G2 fail: FY26 (Jun 30) FCF $109.08M − $115.91M = −$6.82M (−0.48%); FY25 −5.2%. OCF positive both years. A2 fails (no buybacks, net debt). A4 2.44× on FY27 FCF consensus $248M, 3.81× if the $338.9M TRA payable counts.
- H is a poor fit for a profitable manufacturer funding expansion capex; it fails H5 regardless: Neos (10% owner, five board seats) sold 135.2M shares Feb 9 to Jul 6 (44.4% of shares).
- #19 clear (Sep 15): revenue $461.7M vs ~$425.6M (+8.5%), above own guide; adj EPS $0.25 vs $0.22 to $0.24; Q1 guide mid $455M vs $456.7M (−0.4%); FY27 guide $2.4B to $2.6B vs ~$2.1B.
- Why it fell (−49% from Jun 4): sponsor supply (Jun/Jul follow-ons at $47/$49, lock-up end Aug 4, −17% Aug 21), AI-stock selloff Oct 14, JPMorgan target $56 to $49. No guidance cut.
- Legal: stayed March 2026 suit over pre-IPO MGM acquisition payments; no loss estimate; watch.
- 59% of FY26 revenue from data centers: carries AI-capex factor exposure on entry.
- [Release](https://www.sec.gov/Archives/edgar/data/2080126/000208012626000034/exhibit991earningsrelease_.htm), [Jul prospectus](https://www.sec.gov/Archives/edgar/data/2080126/000119312526294982/olympus_iv_-_form_424b4.htm)

## KRMN, $30.14: A–E out (A1), G out (G2)

- A1 fails: stock consideration in Five Axis (closed Oct 28, 2025; 68,625 shares) and Seemann (closed Feb 3, 2026; $17.0M stock). Rolls off ~Feb 2027. Diluted shares +0.16%; stockanalysis −11.44% compares to a pre-IPO count. The May 28 secondary was selling holders only. [Deals note](https://www.sec.gov/Archives/edgar/data/2040127/000204012726000024/R13.htm)
- A3(a)/G2 fail: trailing FCF $5.86M − $33.53M = −$27.67M (−4.69%); FY25 OCF −$22.1M. A4 ~9.5× on FY26 FCF consensus $86.6M before ~$100M Walker deal debt.
- H not used: an EBITDA-profitable incumbent (30% adj EBITDA margin) whose failure is converting EBITDA to cash is a G2 failure, consistent with AVAV, AMZN and ORCL. Under the alternative reading it would be H-watch: H1 pass, H2 thin provisional pass ($51.7M cash + $150M revolver vs ~$142M need), H3/H4 missing, indicative ceiling ~$24 (15× 2031 EBITDA ~$555M gives ~14.7%/yr).
- H5/A7: net insider sales 613,225 (0.46%) pass by 49k shares; Trive (chairman is a partner) May sales would make it 1.44% if counted. See pending P12.
- #19 clear (Aug 6): revenue $182.06M vs $179.9M; adj EPS $0.14 vs $0.13; FY guide raised to $730M to $745M.
- Quality flags: CEO change Mar 23; late 10-K with three material weaknesses; CFO exit Aug 26; J Capital short report Sep 2 questioning cash flow ([report](https://jcapitalresearch.substack.com/p/karman-holdings-inc-krmn)); auditor switched to PwC; ~12% short interest. No class action found.
- Next: Q3 print Nov 5. FY26 FCF consensus needs ~+$111M in H2.

## RKLB, $59.18: out of H (H5), H4 fails, Neutron slip

- H5 fails, verified: 12-month open-market sales 8.88M shares, zero purchases, 1.33% of ~668M economic shares vs 0.5%. Beck's 5.81M alone is 0.87%. Officer cluster clears. Earliest roll-off ~Jul 6, 2027.
- Oct 14 after close: Neutron first launch moved to 2027 after voids in the composite forward tank dome; new dome by year-end, tank pressure and cryo tests Q1 2027. The Q4 2026 pad milestone is missed. Treat as an H7 recoverable failure: no entry until the Q1 2027 stage test is verified. [8-K](https://www.sec.gov/Archives/edgar/data/1819994/000181999426000067/rklb-10142026ex991.htm)
- H1 passes: TTM revenue $769M, GM 37%, RPO $2.356B; Synspective 20-launch deal (2028 to 2031) value undisclosed.
- H2 thin provisional pass: est. Sep 30 liquidity ~$4.19B vs ~$4.04B uses (Iridium cash $2.861B, fees ~$0.075B, Q2-pace burn × 1.25 = $1.101B); cushion ~$0.15B. Excludes the $1.775B Iridium loan RKLB will guarantee.
- H3 unresolved: FY26 FCF consensus −$220M, FY27 revenue $1.35B; shares +15.7% YoY.
- H4 fails: hurdle $147.26 at ~740M fully diluted shares (668M + ~42.4M Iridium at the fixed 0.4 ratio below $67.50 + ~25M awards) needs ~$4.4B FCF at 25×; indicative ceiling ~$21.
- #19 clear (Aug 10): revenue $234.1M vs $231.6M to $232.1M; adj EBITDA −$8.8M beat the −$20M to −$26M guide; Q3 guide mid $257.5M vs ~$235.9M (one source).
- Why it fell (−19.9% since Oct 2): SpaceX D2C clearance and spectrum purchase read as Iridium competition; Goldman target $80 to $75; −7.8% Oct 14 before the Neutron release, cause not found.
- Next: Nov 9 print.

## AVAV, $120.60: A–E out (A1), G out (G2)

- A1: diluted WASO +6.3% (Jul 2025 $1.006B equity raise).
- G2 fails: TTM FCF $58.82M − $83.85M = −$25.03M (−1.25%); OCF FY25 −$1.3M, FY26 −$78.4M; FY27 FCF consensus −$89.2M; capex 143% of OCF plus a $29.25M campus purchase Aug 21. G3 fails on +6.3% WASO.
- H not used: a ~$2B-revenue incumbent with $218.8M adj EBITDA failing cash conversion is a G2 failure. Even if tested, H4 fails (hurdle $300.09 needs ~$650M FY32 FCF); flagged base ~8%/yr also misses G5 (12%, $212.5).
- Legal: two securities class actions (E.D. Va., D. Del.), unspecified damages; two material weaknesses; June $89M goodwill restatement.
- #19 (Sep 9): revenue $480.5M vs ~$456M (+5.3%), adj EPS $0.59 vs $0.25, FY guide reaffirmed; adj EBITDA consensus not found, so unresolved.
- G1 likely passes: funded backlog $1.5B (+37%), book-to-bill 1.4.
- Next: Q2 FY27 print ~early December (unconfirmed). Earliest G pass ~Jun 2028 (two positive OCF years). [Release](https://www.sec.gov/Archives/edgar/data/1368622/000110465926106304/avav-20260909xex99d1.htm), [10-Q](https://www.sec.gov/Archives/edgar/data/1368622/000110465926106423/avav-20260801x10q.htm)

## UUUU, $8.34: F only, F1 fails, PH-impaired

- F1 fails: FCF margin −113.9% (−$120.4M on $105.8M); EBITDA margin −67.8%; interest coverage −18.1×; ROIC −16.1% vs WACC 11.1%; 8 analysts (< 15).
- Issuance: ~$300M ATM sales; 14.81M shares for ASM Aug 28; new $500M ATM filed Oct 13; pending VAC deal 65.85M shares + $718M cash. The $700M converts (~Oct 3, 2025) are just outside 12 months. No buybacks.
- F2 none: CEO bought $0.97M Jul 7 and a director 4,000 shares Jul 8 (< $2M, two insiders, > 30 days).
- Why it fell (−43% since Sep 9): VAC deal and a terminated VAC customer contract (Jul 1, in arbitration; Oct 13 amendment allows price adjustment), ASM dilution, uranium selloff Oct 7, new ATM, BMO target $18 to $14 (Oct 14).
- Next: Nov 2 print; Donald project FID Q4; VAC close ~Q1 2027. [Oct 13 8-K](https://www.sec.gov/Archives/edgar/data/1385849/000106299326005306/form8k.htm), [ATM prospectus](https://www.sec.gov/Archives/edgar/data/1385849/000106299326005309/form424b5.htm)

## Open items carried

- ALGM: FY28/29 FCF consensus, sell-to-cover status of the May/June officer sales, G5 model.
- PL: verified pre-print Q3 consensus; next print date.
- ASTS: strategic-holder reading (P12); Q3 cash; full convert terms from the 10-Q.
- GFS: final terms of the Oct 14 government stake; Japan-fab guarantees.
- KRMN: Sep 30 cash after Walker; FY27 FCF consensus.
- AVAV/PL: adj EBITDA consensus for the last prints.
