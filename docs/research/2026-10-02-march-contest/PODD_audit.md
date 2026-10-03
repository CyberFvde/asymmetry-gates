# PODD follow-up audit — October 2, 2026

**The full insider test now clears. PODD remains a capital watch, because the NTM cash-yield source conflict and exact NTM gross-margin proof remain unresolved.** This supersedes the earlier statement that 20 insider filings were missing. No repository or skill files were changed.

## Complete insider review

All 46 filings were retrieved: 45 Form 4 and one Form 4/A. The SEC submissions index reaches back to August 2015 and is current through October 2, so the relevant year is covered. Downloads were sequential at approximately one request per second; no rate-limit bypass. Transactions, rather than filing dates alone, were filtered to October 3, 2025–October 2, 2026. Code F withholding and code G gifts are excluded from market trades.

| Measure | Result |
|---|---:|
| Code S market sales | 2,269 shares |
| Code P market purchases | 14,632 shares |
| Net sales (S minus P) | -12,363 shares: net buying |
| Net sales / 69,351,014 shares outstanding | -0.01783% |
| Officer code S transactions | 0 |
| Derivative S/P rows | 0 |
| Duplicate S/P rows | 0 |
| Mandatory sell-to-cover exemptions used | 0 |

The two sellers were directors Luciana Borio (418 shares, June 3) and Wayne Frederick (1,851 shares, December 15), not officers. CEO Ashley McEvoy purchased 4,300 shares February 20 and 1,100 August 21; other director purchases account for the remainder. Plans are not deducted from annual S/P totals. There are no officer S trades needing either a 10b5-1 exclusion or the mandatory, non-discretionary sell-to-cover interpretation. The July 7 Huffines Form 4/A corrects a deferred director-compensation grant; it contains no S/P transaction.

Evidence: `insiders/PODD.json`, `insiders/PODD_summary.json`, and 46 cached XML documents. [SEC submissions](https://data.sec.gov/submissions/CIK0001145197.json), [CEO August purchase](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000172/form4.xml), [Borio sale](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000142/form4.xml), [Frederick sale](https://www.sec.gov/Archives/edgar/data/1145197/000114519725000074/form4.xml), [grant amendment](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000159/form4a.xml).

## Remaining gates

| Test | Evidence and status |
|---|---|
| A1 dilution / financing | Q2 diluted WASO 69.403M versus 70.652M (-1.77%); H1 69.803M versus70.641M (-1.19%). No secondary, ATM, stock-funded acquisition or convertible filing identified in the reviewed year. Employee stock/RSU/ESPP activity is disclosed and treated under ordinary compensation dilution; a reading banning all employee-plan shares would require explicit clarification of the rule. |
| A2 buybacks | $300M ASR completed March 31; 1.25M shares repurchased in H1. Positive last-four-quarter gross buybacks established. |
| A3 cash | Trailing company FCF293.7M /revenue3.0535B=9.62%. Raw cash consensus NTM469.75M and capex177.85M imply OCF647.60M. More conservative capex cases below still leave FCF375.7–439.5M above trailing and capex32.1–42.0% of OCF, within50%; exact consensus period/source reconciliation remains required. |
| A4 leverage | June net debt413.5M plus full97M construction-guarantee reserve gives conservative510.5M exposure. Dividing by stressed375.725M cash FCF gives1.36x, below2.5x. Avoid double-counting guarantee amounts already booked when finalizing. September21 refinancing replaces the same475M term loan; no added principal. Undrawn750M revolver is liquidity, not debt already incurred. |
| A5 share and margins | Issuer has600K+ global customers and #1 US requested/prescribed AID product, with claim sources disclosed. This supports segment leadership but is not an exported market-share percentage for every geography. FY2025 GM71.63%; designated FY2026 forecast71.81%. Exact NTM gross profit including FY2027 has not been retrieved, so **do not mark the NTM margin leg verified**. |
| A6 market | Underpenetrated AID adoption and geographical/type2 expansion support growth. Do not substitute PODD's own revenue growth for a rigorously measured whole-market GDP comparison. |
| A7 insiders/legal | Insider portion passes in full. No liability plus structural remedy against PODD was found. July securities case is defended and issuer says loss is not probable/no accrual; no quantified reasonably-possible loss >5% NTM FCF was disclosed in the reviewed filing. Device correction costs remain cash/quality watch items. |
| A8 chain | No external platform bypass identified; smart pens, competing pumps and GLP-1s are competitive/adoption risks requiring triggers. |
| #9 growth | FY2026 is the framework's next-FY because FY2025 is last completed. Designated forecast21.38% growth and own20–22% constant-currency guide support≥12% organic hurdle; 3Y revenue CAGR16.15% clears15%. FY2027 forecast13.76% is a subsequent-year check, not the next-FY definition at October2. |
| #11 valuation | Governing forward P/E19.09 and PEG0.96 pass. Cash-yield cases4.12–5.15% all pass1.5%, while #12's5% hurdle is sensitive. |
| #12 asymmetry | PT leg void at31.9% below200DMA. Raw blended cash consensus gives5.145%; conservative capex reconciliations give4.814% or4.115%. **Unresolved; not a clean pass.** |
| #13/#19 | Next confirmed printNovember4 outside five-trading-day pause. Previously sourced Q2 actual/own-guide/preprint-consensus comparisons clear #19; next-quarter midpoint was1.007% below dated consensus, within3%. |
| PH | ATH September9,2025; drawdown62.675%; PH-clear under the age conjunction, with severe weak-trend warning. |
| #15/#16 | Proposed triggers below need to be adopted for a funded entry, with portfolio headroom established. |

Financial statements: [Q2 10-Q](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000169/podd-20260630.htm), [FY2025 release](https://investors.insulet.com/news/news-details/2026/Insulet-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx). Recent financing: [September21 8-K](https://www.sec.gov/Archives/edgar/data/1145197/000119312526396779/d71204d8k.htm). Leadership evidence: [issuer homepage, sources footnoted](https://www.insulet.com/). Governing statistics: [StockAnalysis](https://stockanalysis.com/stocks/podd/statistics/).

## Cash forecast conflict and vintage

StockAnalysis financial forecast was last updated September30, with25 analysts; its public FY2026 cash FCF is396.72M, and public next-year EPS7.72/revenue3.74B are visible. Price and statistics are October2. The current US-listed MarketScreener page header matches October2 price131.69 and shows FY2026/FY2027 FCF396.7/494.1M and cash capex151/186.8M, though it supplies no explicit cash-estimate update timestamp or analyst count. [Designated forecast](https://stockanalysis.com/stocks/podd/forecast/), [US cash forecast](https://www.marketscreener.com/quote/stock/INSULET-CORPORATION-50468/finances/).

Management's annual and Q2 filings both say2026 capital expenditure will increase versus2025's191.6M. Thus the151M public estimate conflicts with current guidance. The framework's fallback for vague 'growing' capex is trailing cash PP&E217.5M ×1.25=271.875M. Do not quietly use the lower capex estimate to gain eligibility.

| October2 NTM convention | Cash PP&E | OCF retained for comparison | Company FCF | Yield at9.13B | #12-only price ceiling |
|---|---:|---:|---:|---:|---:|
| Raw25%FY26+75%FY27 consensus |177.850M|647.600M|469.750M|5.145%|135.47|
| FY26 fallback271.875M, then25/75blend with FY27consensus186.8M |208.069M|647.600M|439.531M|4.814%|126.76|
| EntireNTM fallback217.5×1.25 |271.875M|647.600M|375.725M|4.115%|108.35|

The last two rows are **conservative recomputations**, not supplied consensus forecasts. Annual straight-line blending does not prove seasonal quarterly cash timing. A clean funded verdict needs a current, consistent OCF/PP&E/FCF forecast and the exactNTM GM leg. At today's market cap, #12 requires≥456.5M companyFCF, hence capex≤191.1M if647.6M OCF is maintained. Alternatively an all-A verified wide-moat name failing only#12 could fit the one ballast slot if available; that verdict is not yet established.

The prior G5 draft's184.58 ceiling is not an approved entry. Its5%-revenue capex assumption also needs reconciliation with the current capex warning; do not retain that ceiling as if the missing cash evidence were solved.

## Proposed numeric #15 thesis triggers

These are proposed policy choices, not management guidance and not an instruction to execute. Re-test at November4 and after every print. Entry eligibility remains conditional on the selected route's full proof.

1. Cash engine: verified trailing companyFCF margin<6%, or proforma net debt/NTMcompanyFCF>2.5x, invalidates Core/G qualification. NTM capex>50%OCF or Core NTMFCF<trailing293.7M forces an immediate route re-test and no additions.
2. Guide/retention: US Omnipod organic growth<10% for two consecutive quarters is a thesis-exit trigger; a single quarter below10% freezes additions and requires customer-retention explanation. FY2026 US guide below17% or total ccguide below20% triggers immediate #17 re-test; a >5% like-for-like estimate cut follows the framework's revision rules rather than an automatic sell.
3. Product quality: incremental cash device-correction/replacement cost>50M over the next12months, or a safety action preventing Omnipod sales for>90days in a market representing≥10%of revenue, triggers a full cash/competitive review and freezes additions. Exit if that review breaches the cash/solvency floor or destroys the commercialization thesis.
4. Capacity/claims: new CostaRica or supplier guarantees raising total proforma claims>2.5xNTMFCF are a hard failure. CashPP&E plus financed/JV/lease buildout>60%NTMOCF is a separate buildout kill/re-test line; do not re-label financed construction as free capacity.
5. Governance: annual insider net sales>0.5%, a Core quarter with≥3 discretionary non-plan selling officers, forbidden Core financing, or regulatory liability plus structural remedy triggers route failure. A disclosed reasonably-possible legal loss>5%NTMFCF applies the statutory framework veto, with denominator refreshed at that print.
6. Model discipline: no G entry above the supported numeric G5 ceiling; new annual ordinary dilution>3%, unreconciled warrants/earnouts, or a modeled3Y fully dilutedFCF/shareCAGR<12% blocks G additions. No options sizing or stockprice-only exit is inferred from these checks.

Confirmed next-print source: [October 1 issuer announcement: November 4 before market open](https://investors.insulet.com/news/news-details/2026/Insulet-to-Announce-Third-Quarter-2026-Financial-Results-on-November-4-2026/default.aspx).
