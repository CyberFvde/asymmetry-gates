# RKLB / ASTS / PL — fresh Oct 15 revision 5 review

Framework: merged-main `f6171aa`, Oct 15, 2026 revision 5. G3 ordinary dilution remains 3%; G5 base return remains 12%; H4 base return remains 20%; #12 remains 5%. PR3 revision 4 and PR6 research are background only. Governing stock prices are Oct 14 completed closes supplied to this delegated review: RKLB $59.18, ASTS $42.14, PL $14.13. Root computes PH separately. All three require H; none is a core pass. This is a full H1–H5 assessment, including funding and price rather than stopping at A1. All portfolio headroom is unknown.

**Result: no verified H-early pass. PL is the closest of these three to a funded, evidenced quality transition, but H3/H4, the latest annual insider verification and #19 are not closed. RKLB has a verified annual insider-sales failure. ASTS retains a verified revenue-miss blackout plus material funding/dilution/governance gaps.** These are framework verdicts, not predictions that the companies cannot rally or succeed.

## PL — H-watch; #19 unresolved, potential guide blackout

### H1 — passes demonstrated product/demand test

Actual quarterly revenue $116.1M (+58%), recurring ACV 98%, non-cancelable RPO $753.1M; 46% expected in twelve months and 68% in twenty-four months. Backlog $814.9M includes cancelable or not-yet-appropriated amounts; use RPO, not all backlog, for binding demand. Pelican-11 technical demo was launched in July. These establish achieved delivery and paying customers; they do not prove every future service margin.

Sources: [issuer earnings release](https://investors.planet.com/news/news-details/2026/Planet-Reports-Financial-Results-for-Second-Quarter-of-Fiscal-Year-2027/default.aspx), [SEC release](https://www.sec.gov/Archives/edgar/data/1836833/000119312526381874/pl-ex99_1.htm), [quarterly filing](https://www.sec.gov/Archives/edgar/data/1836833/000119312526382016/pl-20260731.htm).

### Current cash engine / routing

Trailing OCF $117.63M less cash PP&E $92.96M = $24.67M, 6.52% of revenue. That actual cash margin is encouraging. G still does not pass: FY25 OCF was negative, ordinary period-end economic shares grew about 11.5%, and forward cash conversion requires a new capex-heavy investment cycle. FY27 is the fiscal year ending January 31, 2027, the fiscal year after the last completed FY26, not FY28. The publicly visible forecast gives FY27 FCF -$29.08M and FY28 revenue $570.56M; later forecasts are not publicly verified here. Do not treat historical forecast-table FCF as identical to the skill's OCF-minus-cash-PP&E definition.

Sources: [statistics](https://stockanalysis.com/stocks/pl/statistics/), [forecast](https://stockanalysis.com/stocks/pl/forecast/), quarterly filing above.

### H2 — funding looks sufficient on an explicit stress model; not a full contracted-spend certification

July 31 unrestricted cash/investments $865.418M excludes $8.498M restricted cash. A flagged $25M bridge allowance to Oct 14 gives $840.418M modeled usable liquidity. Remaining ATM authority of about $1.378B is excluded entirely; no forward sale had been entered at July 31.

Stress the next two years at $40M annual negative OCF, $150M annual cash satellite/software investment (above the $100M–$115M FY27 total-capex guide), $50M annual financing cash employee withholding, and $2.3M annual note interest. Need = 2 × ($40M + $150M + $50M + $2.3M) × 1.25 = **$605.75M**. That leaves about **$234.67M** modeled cushion. This deliberately includes capitalized software in the gross investment stress and does not count it a second time. Lease operating costs are in OCF; do not add the same lease payments twice. Customer receipts are slowed through negative OCF, rather than extrapolating the strong prepayment quarter.

The $460M notes mature October 15, 2030, outside today's 24-month window. Conversion is already permitted this quarter; the company can deliver shares and need not assume a $460M cash outflow today. A fundamental-change cash repurchase is contingent, not an ordinary scheduled 24-month use. The terms still must be incorporated into the five-year model, and the liquid cash buffer is not permission to omit future replacement satellites, leases or manufacturing commitments.

### H3/H4 — credible destination can be modeled; current entry is not supported by the base case

Created a reproducible annual sensitivity, **not a consensus forecast or a certified intrinsic valuation**, at `oct15-space/PL-H-sensitivity.json` with `oct15-space/pl_h_sensitivity.py`. All units below USD millions except percentages/shares (millions).

Proposed quality deadline if eventually entering: **October 14, 2031**, inside five years. It is a proposed research deadline, not an already-started entry clock. Base route aims at G: 19% cash FCF margin, positive OCF in the last two years, capex/OCF 38.7%, no terminal note principal, and ordinary dilution converging below 3%. The model must subsequently demonstrate G1 durability, ≥10% next-FY and 3Y organic growth, ≥12% forward FCF/share growth, all insider/legal protections and G5 valuation at graduation. Modeled 16% subsequent organic growth with ≤2.9% dilution could supply about 12.7% FCF/share growth at flat margins; that is an assumption, not existing analyst coverage.

| Year ending Oct 14 | Revenue | GAAP operating margin | OCF before note interest | Cash PP&E | Cash FCF before note interest | Ordinary fully diluted shares | Cash after software/withholding/interest/maturity |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2027 | 540 | -8% | 64.8 | 118.8 | -54.0 | 405 | 759.1 |
| 2028 | 700 | 0% | 126.0 | 133.0 | -7.0 | 425 | 724.8 |
| 2029 | 880 | 8% | 211.2 | 140.8 | 70.4 | 440 | 767.9 |
| 2030 | 1,060 | 15% | 296.8 | 137.8 | 159.0 | 452 | 899.6 |
| 2031 | 1,250 | 20% | 387.5 | 150.0 | 237.5 | 465 | 652.1 |

Working-capital consumption is 2% of sales annually. D&A is 10%; SBC declines from 12% to 7%; cash tax from zero to 4%. Additional annual software cash $5M and financing employee withholding $20M are deducted in the annual liquidity roll. No interest income is credited. Note cash interest $2.3M through year four, then the scheduled $460M maturity in year five, is modeled separately from the table's pre-interest operating FCF. No future base-case equity financing is credited.

**Conversion reconciliation:** $460M principal × 83.6715 shares per $1,000 = **38.48889M** initial physical-conversion shares, before make-whole/antidilution changes. The model compares cash maturity repayment with full physical conversion (restoring the $460M cash, adding the 38.48889M shares) and takes the lower per-share outcome. It never both pays the same principal and adds those conversion shares. Capped calls receive zero valuation credit. The first-year ordinary diluted forecast accommodates current option/RSU overhang; proposed ownership maximums including conversion/future awards are **480M at 24 months and 550M at the deadline**. These are research constraints requiring reconciliation with final contract maximums and actual subsequent awards; they are not company promises. A conversion make-whole maximum has not been fully reconciled, so H4 maximum dilution is still open even though the initial ratio is known.

Terminal assumptions have explicit context rather than a TAM multiple: profitable geospatial/data peers TRMB and VRSK currently trade near 19.4× and 22.3× EV/FCF. They are imperfect comparables with established economics, and their spot multiples do not validate five-year durability or the chosen PL margin. Use 22× operating cash FCF for base/bull, 15× for bear, add modeled available terminal cash and subtract an assumed $40M terminal lease claim. This is a cash-multiple sensitivity, not a full DCF; no claim of a verified five-year median is made.

| Scenario | 2031 revenue | 2031 cash FCF | Year-five share value | Annualized return at $14.13 |
|---|---:|---:|---:|---:|
| Operating bear | 680 | 13.6 | $0.73 | -44.8% |
| Base | 1,250 | 237.5 | $12.51 | -2.4% |
| Bull | 2,500 | 800.0 | $37.71 | +21.7% |
| Failed commercialization | — | — | $0 | -100% |

The bear includes a later $200M equity raise at $5/share, not counted as available H2 funding today. The base uses no new raise; the bull assumes sustained acceleration and a much higher 32% terminal cash FCF margin. Only the bull clears 20%. The return-only base price condition is about $5.03, **not an approved entry ceiling**: price cannot cure #19, incomplete H5, funding-contract maximums or unsupported operating assumptions.

Reverse the hurdle instead of presenting a made-up precise ceiling: $14.13 × 1.20^5 = **$35.16** year-five share value. At the model's base shares/cash, that requires roughly **$715M–$756M cash FCF** at 22×, depending on note settlement, versus base $237.5M. A researched case supporting those cash economics, a lower entry, or materially better per-share funding could change H4. A high analyst price target alone cannot.

Sources: [VRSK statistics](https://stockanalysis.com/stocks/vrsk/statistics/), [TRMB statistics](https://stockanalysis.com/stocks/trmb/statistics/), PL filing and forecast above. Peer spot comparisons were read Oct 15 and are context; Oct 14 closes govern requested-stock entry math.

### H5 / #19 — not a verified pass

Fresh PL annual Form 4 downloads were blocked by SEC 429 responses (61 attempted, all retrieval errors). The draft's 1,583,170-share net-selling total (0.435%) is **not independently verified in this run**. Latest submissions include an October 14 filing that must be reconciled. Do not present H5 as passed or net sales as zero because the download failed. Full annual totals, applicable officers' rolling holdings/context and known material legal maximums remain required. Previously settled litigation is not an automatic new veto, and ordinary generic litigation-risk language does not by itself establish an unknown material exposure.

The Sep 3 print itself has strong actuals: revenue $116.1M versus approximately $104.5M provider expectations and above own $102M–$107M range; non-GAAP EPS $0.02 versus provider -$0.02. Adjusted EBITDA $13.9M also beat its own guidance. H can pre-record cash/gross-profit substitutions rather than manufacture EPS relevance.

Q3 guidance is $101M–$105M, midpoint $103M. MarketBeat currently displays a **Q3 FY27** $114.3M revenue estimate and says it was the comparison on Sep 3, implying -9.9%. However its table identifies only one estimate, has inconsistent other period estimates versus its FAQ, and no independently archived pre-print consensus snapshot was recovered. Therefore **withdraw the draft's unconditional verified-blackout label for PL**; label **#19 unresolved / possible material guide blackout** until comparable pre-print evidence is authenticated. This does not mean #19 is clear. A verified comparison above $103M / 0.97 = **$106.186M** triggers the >3% guide leg.

The new rev5 #19(d) exemption is unavailable on present evidence: the issuer's financial-outlook section does **not provide full-year company FCF guidance**, nor a separate full-year organic-revenue guide comparison. Thus three joint beats alone cannot establish exemption; do not use reaffirmed adjusted EBITDA or a good reported revenue growth rate as substitutes. If the $114.3M comparator is authenticated, exemption conditions still remain unfulfilled and the blackout binds until a later clean print.

Sources: [MarketBeat provider table](https://www.marketbeat.com/stocks/NYSE/PL/earnings/), [issuer outlook](https://investors.planet.com/financials/quarterly-results/). Next Q3 report is **estimated Dec 9**, not issuer-confirmed in sources inspected. Numeric next-print operating checks: actual revenue ≥$101M own low end; non-GAAP GM ≥56% own low end; model cash burn ≤120% of the pre-recorded ceiling; also fresh consensus comparisons and all remaining H tests. No capital until closure.

## RKLB — out of H on verified H5 annual net sales; financing and valuation also need work

### H1 — achieved business passes

Electron/HASTE launches and revenue are achieved, independently evidenced progress. Q2 revenue $234.1M, backlog about $2.36B and September's 20-launch Synspective agreement support real demand. Do not require Neutron success to pretend that no Rocket Lab product has ever commercialized, but do not treat Neutron's eventual scale or backlog options as achieved quality.

Sources: [Q2 release](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-announces-second-quarter-2026-financial-results-posts), [quarterly filing](https://www.sec.gov/Archives/edgar/data/1819994/000181999426000062/rklb-20260630.htm).

### H2 — acquisition cash funded; full stressed corporate execution not yet certified

June unrestricted cash/current/non-current liquid securities total $2.387590B. September ATM is **completed**, $1.944B gross / 29.3M shares; subtract actual commissions/fees before treating as usable liquidity. The September permanent financing retains Iridium's $1.775B term loan with a Rocket Lab operating-parent guarantee; the $3.6B bridge is **canceled** and supplies no cash.

Iridium cash consideration is $27 × shares eligible at close; at about 105.96M shares that is $2.861B before award settlements/fees. The stock collar is 0.4000 Rocket Lab shares per IRDM share if the specified pre-close VWAP is ≤$67.50; do not calculate shares using $27 divided by today's lower RKLB quote. That implies around 42.38M consideration shares on the illustrative IRDM count.

Liquidity before post-June burn is roughly $4.30B after an illustrative 1.5% ATM cost. Cash-deal leg leaves around $1.44B. H1 operating outflow $134.407M plus cash capital equipment/software $53.112M = $187.519M six-month burn. Annualizing that through two years with 25% buffer is $937.595M; using faster Q2 pace is about $1.10B. Neither is a certified H2 model: actual post-June drawdown, Neutron redesign/ramp, acquisition fees, integration, working capital, guaranteed-loan debt service and Iridium's own replacement/integration needs require a reconciled 24-month model. Include Iridium conservative operating cash when consolidating it, without adding all future principal as immediately due unless the loan actually matures inside the window. A fully funded purchase price is not proof that every subsequent corporate use is funded. **H2 remains unresolved, not a verified failure on gross-cash arithmetic alone.**

Source: [September financing release](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-fully-funds-iridium-acquisition-including-completion), quarterly filing above.

### H3/H4 — full quality path absent; no supported formal entry ceiling

The large Iridium combination and Neutron schedule require an annual combined-company cash, capex, claims and maximum-share model through a fixed quality deadline. The current draft has not supplied one. June economic shares are roughly 598.180M common outstanding + 40.951M economically equivalent preferred = 639.132M; completed September ATM adds 29.3M, about **668.432M** before subsequent activity. June disclosed anti-dilutive instruments also include 13.096M options/RSUs, 2.608M convertible-note shares and 7.451M collared-forward shares, requiring reconciliation of exercised/settled amounts so they are not counted twice. Unused award-plan capacity is not all current dilution, but a maximum projection must explicitly control future awards. Do not use the stock site's unadjusted 598M common-only denominator or call a rounded 740M estimate a certified maximum.

At $59.18, H4 needs year-five **$147.26/share**. At an explicitly illustrative 740M fully diluted shares, equity must be about $109B; at 25× cash FCF and zero terminal net debt, this requires around $4.36B FCF. This is a **reverse hurdle**, not a sourced forecast or a verified $21 ceiling. Profitable space-services peer IRDM has roughly 22.4× EV/FCF currently, but the pending takeout distorts its trading comparison; a restrained durable multiple and full combined operating model must be researched before publishing a formal H4 ceiling. Mark H3/H4 unproven rather than presenting a terminal earnings guess as a verified intrinsic failure.

### H5 — independently verified hard failure

Fresh full recent-submissions coverage: 62 Form 4/4A filings in the annual filing window; raw XML retrieved successfully for every one (zero errors). Transaction window Oct 15, 2025 through Oct 14, 2026; filings searched through Oct 15. Market-code S sales **8,880,247 shares**, market-code P buys **zero**. Annual net sales are **1.3285%** using illustrative current economic shares 668.432M, well above 0.5%. CEO Beck alone sold **5,813,493 (0.8697%)**. His trust's plan transactions are counted once, not once per indirect beneficiary. Rule 10b5-1 status does not exempt the annual numerator. Code F withholding and gifts were excluded from market totals. All transactions are ordinary common shares; no split conversion is needed in this window. A known sale purpose/plan cannot rescue the annual breach through rev5's minor-footnote fallback.

Audit files: `oct15-space/RKLB-insiders.json` (full rows/footnotes/URLs), `RKLB-insiders-summary.json`, captured raw footnotes/URLs, `audit_captured_insiders.py` offline totals checker. Raw source example [Beck July filing](https://www.sec.gov/Archives/edgar/data/1819994/000200101126000109/edgardoc.xml). Current verified net sales would need to fall to ≤3.342M at unchanged shares. No-new-sales/unchanged-share arithmetic first drops under that threshold around **July 7, 2027**, when the July 6, 2026 transactions leave the rolling year; actual future purchases/sales/shares can change that date. This is not a guarantee of eligibility then.

### New Neutron news and #19

[Oct 14 after-close issuer update](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-provides-update-neutron-development-and-adjusts) and [SEC 8-K](https://www.sec.gov/Archives/edgar/data/1819994/000181999426000067/rklb-20261014.htm) verify first Neutron launch has shifted to **2027**. This is material information available to today's screen, although Oct 14 regular-session close predates it. First launch and pad delivery are different milestones: the release alone does **not** establish draft assertions that the Q4 pad-delivery milestone has already been missed or that a checkpoint is >90 days late. Q4 is still underway. No automatic H7 terminal failure or held-position exit is inferred from that schedule statement alone. A new entry would require a documented funded revised technical plan and achieved checkpoints.

Q2 revenue $234.1M versus published roughly $231.6M–$232.1M estimates and own guidance clears revenue comparisons. Q3 guide $250M–$265M was above then-published expectations. Pre-recorded H gross-profit/burn/milestone substitutions and full pre-print comparisons are not independently closed here, so do not promote #19 from a first-failure draft. Next financial print estimated **Nov 9**, confirmation not found. H5 independently keeps entry out regardless.

## ASTS — H-watch, verified #19(a) blackout; material governance/funding gaps

### H1 — achieved technical progress and real commercial receipts

BlueBird deliveries, actual ordinary-phone demonstrations and Q2 service revenue **$7.092M** are meaningful progress. Total Q2 revenue **$31.520M** includes gateway products/government milestones rather than all recurring consumer subscriptions. The company says 13 BlueBirds in orbit, while the second-generation scale constellation and production economics remain incomplete. Verizon has a definitive commercial agreement and a $45M prepayment due after approvals; that is stronger than an MOU but should be reconciled to actual collections before counting the same receivable as cash. The $1.3B headline backlog must be separated into enforceable consideration, conditional service commitments and optional future capacity.

Sources: [Q2 release](https://www.sec.gov/Archives/edgar/data/1780312/000119312526342540/asts-ex99_1.htm), [Q2 10-Q](https://www.sec.gov/Archives/edgar/data/1780312/000119312526342550/asts-20260630.htm).

### H2 — funding claim needs schedule reconciliation; do not double-count Ligado

June unrestricted cash **$2,288.253M**; **$434.581M restricted cash excluded**. July $1.15B convert has $1,131.2M net proceeds less **$111.4M capped-call cost**, so incremental usable liquidity is **$1,019.8M**. Total June cash plus July net usable is **$3,308.053M**, before subsequent burn/collections. Do not use $3.7B including restricted cash or the $149.20 capped-call cap as the note conversion strike: initial strike is **$79.57**, 12.5672 shares per $1,000.

Important correction to gross-obligation approaches: **$520M of the $550M Ligado consideration was paid already** ($420M Oct 2025 plus $100M Mar 2026, the latter escrowed). Only **$30M** in that consideration remains at closing. Adding $550M again to June cash and recent cash consumption double-counts prior spend. Spectrum usage fees are at least $80M annually plus Crown Castle cash fees and a 30% share/cash premium, with parts of fee alternatives creating dilution. Their actual cash/share election needs modeling.

The undrawn Sound Point $550M facility was conditional on approvals/documents and had an Oct 5, 2026 availability end with an optional paid 180-day extension. It is not demonstrated available today, so excluded unless extension and draw conditions are verified. The preliminary up-to-$1B Japanese program selection is not final committed funding and is excluded. Do not count the conditional sponsor refund backstop as available operating cash.

For context, first-half OCF outflow $145.212M + cash PP&E $859.215M = **$1,004.427M**. Flat spending over the next 24 months with 25% buffer implies **$5,022.135M**, $1,714.082M above June-plus-net-July liquidity even before intervening burn or other uses. That is a stress illustration, **not proof that every feasible funding plan fails**: construction cash is front-loaded; the issuer explicitly says the 90-satellite build is funded and the modular rollout can slow. A model must reconcile remaining rather than already-paid satellite costs, actual contracted receipts, launch deposits/remaining payments, fees and lower/slower service revenue. No such complete 24-month buffered reconciliation was verified. Hence H2 **unresolved/H-watch**, with a large measured stress gap to close; not a certified universal $1.3B–$2.7B funding deficit.

### H3/H4 — not verified

No sourced annual operating, replacement-capex, working-capital, financing and maximum-convert-share path to positive cash FCF/≥6% margin and full G/A qualification by a fixed deadline is complete. Four outstanding convertible tranches have different strikes and settlement/make-whole terms; July's initial ratio alone is not the fully diluted maximum. H4 needs actual principal/retirement/hedge reconciliation, spectrum share obligations and any later raise at conservative prices.

The public forecast's FY27 revenue is **$581.65M** versus $650.78M previously recorded Oct 2 (about -10.6%). That supports immediate #17 re-test only after confirming like-for-like fiscal years and source snapshots; it is not an automatic H exit. Current loss/capex forecasts and the slower commercial ramp do not establish graduation.

At $42.14, H4 needs **$104.86** in year five (42.14×1.2^5). A rounded 520M fully diluted-share assumption would require about $54.53B equity, approximately $2.18B cash FCF at 25× and no net debt; keeping $4.17B claims would raise that to about $2.35B. Those are reverse-hurdle sensitivities, **not verified share maxima, forecasts or entry ceilings**. A complete model may produce different outcomes; no formal H4 pass/fail intrinsic-price claim is made from them.

### H5 — annual verification incomplete; strategic holders cannot silently vanish

69 annual Form 4/4A filings identified; 61 retrieved, 8 hit SEC 429. Successfully read rows have market sales **5,582,430**, buys **12,837**, before missing filings/amendment reconciliation. These are partial totals, not a completed annual pass or a finalized net-sales failure.

Rakuten's joint filing reports **3,040,000 Class A sales Apr 14–15**. The three joint reporting names (Mikitani/Rakuten Group/Rakuten Mobile) share the same beneficial interest, so count the actual sale once. Raw role fields on this filing are **ten-percent-owner=true and director=false**; the draft's claim that this filing had a director box checked is incorrect. At June economic Class A+B+C shares ~389.109M, those sales alone are about 0.781%. American Tower reports another **2,288,621** sale in a filing with officer/director/ten-percent boxes all false, requiring the historical holder/filing-obligation context. Excluding both entities to get an officer-only ~0.08% is not an adopted revision-5 instruction. Treat the institutional-insider scope explicitly, verify missing offsets and do not adopt pending P12 during a screen. H5 remains unresolved; an inclusive interpretation after complete net reconciliation could create an additional hard failure.

Raw filing [Rakuten joint Form 4](https://www.sec.gov/Archives/edgar/data/1780312/000095010326005837/ownership.xml); cached `oct15-space/ASTS-insiders.json` records retrieved rows/errors. Ordinary generic legal-risk language or a class-action solicitation is not automatically a material undisclosed-loss veto. Identify an actual company-disclosed material exposure and stress any disclosed reasonably-possible maximum against liquidity; otherwise label the legal evidence incomplete without fabricating a definite maximum or veto.

### #19 — material actual-revenue miss verified; rev5 guide exemption cannot cure it

Q2 actual $31.520M versus contemporaneous **$34.5M** reported expectation = **-8.64%**, far beyond the >2% material revenue threshold. A contemporaneous original Newsquawk feed headline at Aug 10 20:33 UTC records that comparison; other providers differ slightly but all located revenue estimates above $33.9M leave it material. Do not use an EPS miss that mixes GAAP, adjusted and conversion/launch incident charges to strengthen the case unnecessarily. #19(d)'s new exemption applies only to next-quarter guidance, so it cannot cure this actual-revenue leg.

Source: [contemporaneous Newsquawk expectation](https://www.newsquawk.com/headlines/ast-spacemobile-asts-q2-2026-usd-eps--077-revenue-315mln-exp-345mln-fy-revenue-view-150-200mln-exp-1557mln), SEC actual above. Next financial print is **estimated Nov 9**, not issuer-confirmed in inspected sources. A fixed $45.1M next-print cure is not justified now: cure requires actual ≥98% of authentic pre-print revenue consensus, own-guidance floors/cash-burn and delivery milestones clear, next-period guide conditions, and the entire H route. Numeric standalone market-price cure does not exist for these gaps.

## Ranking of these three for research priority

1. **PL — H-watch.** Most evident cash-backed progression toward a repeatable data business. Funding can plausibly clear a meaningful stress without another raise. Base valuation, complete dilution/insiders and #19 still block a pass.
2. **RKLB — out of H for current entry.** Proven launch/space-systems business and funded acquisition cash leg are strengths, but annual insider net sales unambiguously violate the current rule. Neutron's 2027 launch and the acquisition require a new full per-share model. This order is research interest among nonqualifiers, not an investable seed.
3. **ASTS — H-watch + blackout.** Strong achieved technology and opportunity; actual revenue miss, 24-month funding reconciliation, maximum dilution and strategic-holder interpretation are more unresolved. A lower share price alone does not cure them.

No verified investable ranking entries from these three. If H eventually passes, initial cap is ≤2.5% sleeve at cost AND ≤0.60% portfolio; max/name ≤5%/1.25%, max two/aggregate10%/2.5%, all shared caps/headroom and written dated checkpoints still required. Failed commercialization at the initial H cap can lose 2.5% of sleeve /0.60% of portfolio; it is not protected by cash on the issuer's balance sheet. No trades, repository edits or gate changes were made by this delegated review.
