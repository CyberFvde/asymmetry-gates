# Recovery board: fundamentals-first contest ranking (revision 21, Nov 5, 2026)

The high-IRR ranking used for contest picks and quick comparisons. Half the score is business quality; the other half is how much the stock can make over the next 12 months against its fair value, per unit of risk. Distance to the high only decides who enters (15% minimum) and who is dead money. It orders names only: framework gates (ID, #19 blackouts), dilution limits, sizing and caps still apply, verified gate fails cost points under GP (revision 19), and cyclical names at a peak are scored on through-cycle numbers under CG (revision 20). Scorer: [`../scripts/recovery_score.py`](../scripts/recovery_score.py); dated inputs: [`../scripts/board_2026_11_04.py`](../scripts/board_2026_11_04.py).

## Universe

- **Pool:** underlyings of US-listed leveraged single-stock ETFs (any launch year), plus names the user adds.
- **Excluded before scoring:**
  - ETFs, and companies trading on pending deal terms (CART, LITE, ACLS).
  - Less than 15% below the high (highest split-adjusted close in the last 10 years).
  - ID fail: TTM gross margin under 20% (framework ID).
  - Dilution: trailing 12-month share growth + undrawn ATM + maximum pending deal shares over 50% of current shares (the IREN rule, H4a's budget). One-time strategic mergers count unless the user exempts them.
  - **Guide-down (GD, revision 18):** the latest guidance midpoint for revenue, EPS or EBITDA (next quarter, or full year when that is all the company gives) came in more than 3% below consensus at the print (misses of 3% or less count as in line; Nov 4 addendum). One metric past the band is enough; use the consensus reported with the print and record its source. Out until the next print; companies that give no numeric guidance pass. Check it first, every screen.
  - **Dead money:** more than 2.7 years to the high when the price compounds at consensus 3-year EPS growth (capped at 35%). No credit for re-rating: a name has to earn its way back.
  - **No fair value:** more than 35% below the high, estimates not rising over 90 days, and no usable 5-year P/E history.
- **Convexity bucket:** GAAP-unprofitable (TTM net income below zero) or binary names can still rank, but only with convexity judgment inputs: d ≥30–35%, bear ≥45–50%.

## Quality (50%)

Six factors, each 0–10 on fixed ranges, averaged (a missing factor drops out of the average):

| Factor | Source | 0 points | 10 points |
|---|---|---|---|
| Growth | stockanalysis 3-year EPS growth forecast | 0% | 30%+ |
| Margin | TTM operating margin | 0% | 40%+ |
| Cash | average of TTM OCF and FCF margins, capped at operating margin + 10 points | 0% | 30%+ |
| Return on capital | stockanalysis ROIC (EBIT after actual tax ÷ average debt + equity − cash) | 0% | 30%+ |
| Debt | Debt / EBITDA; full marks whenever stockanalysis shows net cash | 4.0x | 0.5x or less, or net cash |
| Revisions | Yahoo EPS trend: next-year consensus EPS, now vs 90 days ago | −10% | +10% |

- The cash cap stops customer prepayments (GEV) from passing as quality. Averaging OCF with FCF credits heavy reinvestment (GOOGL, META) while still docking capex that hasn't proven its return.
- Net cash scores the debt factor 10 even when gross Debt / EBITDA is high (convert proceeds held as cash, e.g. MTSI, ONTO; Nov 4 addendum).
- No revision data scores neutral (5). Compute a missing ROIC with the stockanalysis method rather than a different formula.

## CG: cycle guard (revision 20, Nov 5, 2026)

Peak-cycle earnings make a cyclical look like a compounder: every quality factor maxes out and peak EPS times a normal P/E inflates fair value. CG scores those names on through-cycle numbers instead.

- **Who it covers:** cyclical industries where pricing and volume swing with supply: memory and storage, semiconductor equipment and foundry, and commodity producers (energy, metals and mining, chemicals). Fabless and design-led growth names are exempt, since rising returns there come from growth rather than the cycle.
- **Trigger:** the latest stockanalysis quarterly-ratios ROIC is at least 2× the average of its latest 20 readings (about five years), or that average is zero or negative. Compare like with like on that one series; it differs from the statistics-page ROIC used in quality.
- **When triggered, with k = max(0.25, average ÷ latest):**
  - Return on capital factor: board ROIC × k.
  - Margin and cash factors: simple averages of the last five fiscal-year operating, OCF and FCF margins.
  - Multiple leg: NTM EPS × k (mid-cycle earnings), times the same fair P/E. The analyst-target leg is unchanged.
- **Not changed:** growth, debt and revisions factors; the lines; GP.
- **Re-check each screen:** a name drops out of CG once its latest ROIC falls under 2× its average.

## CW and YT: cycle-warning and hot-year penalties (revision 21, Nov 5, 2026)

Two hard ranking penalties for late-cycle and already-run names. Both stack with each other, with CG and with GP, and neither unlocks or blocks capital.

- **CW cycle warning:** uses CG's ROIC ratio (latest reading ÷ its average).
  - 1.5× to under 2×: −1.0.
  - 2× or more, or an average of zero or below: −1.5, on top of CG's through-cycle rescoring.
  - **Scope:** CG's industries, plus booking-cycle names (power and electrical equipment, construction contractors). Booking-cycle names take the points without CG rescoring and are read on stockanalysis annual ROIC: latest reading (TTM, or the latest fiscal year when TTM is blank) against the average of all shown readings, up to five fiscal years plus the latest.
- **YT hot year:** YTD price return = board price ÷ prior year-end close − 1.
  - Above 25%: −1.0. Above 50%: −1.5. Above 100%: −2.0.
  - Every name, every screen. Measure at the board price, not a later quote.

## Fair value

- **Multiple leg:** NTM EPS × fair P/E × (1 + g), where fair P/E = the lower of the median of the last 20 quarterly forward P/Es (stockanalysis ratios) and 2 × the 3-year EPS growth rate.
- **Target leg:** 12-month average analyst target, cut by the revision when estimates fell.
- **12-month fair value** = 50% target leg + 50% multiple leg. Names without a usable 5-year forward P/E history (spin-offs, loss years, no data) use the target leg alone.
- **Deep-drawdown guard:** more than 35% below the high and estimates not rising → the target leg is dropped (stale targets after big drops); no multiple leg either → no fair value, off the board.
- g = consensus 3-year EPS growth, capped at 35%. Fair value today = 12-month fair value ÷ (1 + g).

## Score

- **Asymmetry (25%)** = min(10, 3 × upside to fair value today × (1 − d) ÷ bear). d rises 10 points when 90-day estimates fell 2% or more (smaller dips are noise).
- **Speed (25%)** = 12-month return to the 12-month fair value: 0 points at 0%, 10 points at 75%+. A name sitting at fair value still earns its growth rate, so there is no cliff at fair value.
- **Bear penalty:** −0.25 per 10 points of bear beyond −15%.
- **PB:** politician-buy boost (framework PB): +0.2 buy, +0.1 Pelosi holding, cap +0.3.
- **IX:** index-leader bonus (framework IX): +0.1 per top-10 S&P 500 / Nasdaq-100 holding, cap +0.2.
- **PO policy adjustment:** ±0.1 per specific, sourced policy channel (a law, moratorium, tax credit or regulation tied to the company's revenue), cap ±0.2. Re-check each screen. It rates exposure to named policies, never a view on parties.
- **GP gate-fail penalty (revision 19):** see the section below; 0 to −1.5.
- **CW and YT (revision 21):** see the section above; CW 0 to −1.5, YT 0 to −2.0.
- **Final** = 0.5 × quality + 0.25 × asymmetry + 0.25 × speed − bear penalty + PB + IX + PO + GP + CW + YT. Report one decimal (two at the line); break ties on the unrounded score.

## GP: gate-fail penalty (revision 19, Nov 5, 2026)

A name that ranks but fails a framework gate loses points by how bad the fail is. GP never unlocks capital: a failing name stays capital-ineligible until the fail clears.

- **Which fails count:** verified fails on the name's best route (the route its share count and cash put it on). A watch flag on that route is not a fail (a G4 three-officer cluster below the 25%-of-holdings line, for example).
- **Which gates count:** only what the score can't see: insiders (A7, G4, H5), share issuance past the route's limit (A1, D1, G3), #19 blackouts, legal or regulatory vetoes, PH impairment. Leverage, cash, valuation, growth, guide-downs and dead money are already scored or already remove the name, so they earn no GP.
- **Tiers:**

| Gate | Minor −0.25 | Moderate −0.5 | Severe −1.0 |
|---|---|---|---|
| Insiders (A7 / G4 / H5) | three-officer count reached only through sell-to-cover sales missing the issuer footnote; net selling 1.5–1.65% | three officers with clean discretionary non-plan sales in one quarter; net selling 1.65–3% | net selling above 3%; G4's reject line (three officers each selling >25% of holdings in 90 days); failing quarters in 3 of the last 4 |
| Issuance (A1 / D1 / G3) | past the route limit by 1 point or less | more than 1 point past, rolling off within 12 months | no roll-off date, or more than 12 months away |
| #19 blackout | miss within twice its trigger | miss beyond twice its trigger | blackout on two prints in a row |
| Legal / regulatory veto, PH impairment | | | any |

- **Timing:** a fail that clears within 3 months drops one tier (never below minor). #19 blackouts always clear at the next print, so they are tiered on size alone.
- **Stacking:** one gate counts once, at its worst finding; different gates add up; cap −1.5.
- **Open items:** unverified items earn no points and are tagged "open" with what is missing. Re-run the sweep at each screen and drop the points on the cure date.
- **Quick sweep standard:** route from the share count (A1); insiders from a 12-month sales list (calendar-quarter officer counts; net selling including directors and 10% owners), with Form 4 plan status pulled only for quarters that have three or more officer sellers; #19 on the latest print against pre-print consensus; legal check on known cases. Run it on every name above the line, so checked names aren't penalized next to unchecked ones.

## Lines (fixed Nov 4, 2026)

- **Board line:** final score ≥4.46, set by UBER's post-print score (4.51) less the 0.05 band. The number stays fixed even though UBER itself is now out on GD.
- **Dead-money line:** ≤2.7 years to the high at consensus growth, set by CRDO (2.68).
- Both are fixed numbers. They don't float with UBER's or CRDO's prices; change them only by user request.

## Known limits

- **Peak-cycle quality:** CG (revision 20) covers memory, storage, equipment, foundry and commodity names. Booking-cycle names (power equipment, contractors) get CW points but no rescoring, on annual data. A 20-reading average can sit inside one long upcycle (LRCX, ASML); CW's 1.5× band is there to catch those.
- **YT timing:** YTD resets every Jan 1, so a name that ran in December escapes in January. Recent winners have tended to keep winning over 6–12 months, so YT gives up some momentum upside for less chase risk; the user chose that trade.
- **Stale data:** stockanalysis pages can lag a print (TER's statistics were pre-print on Nov 4; CRDO's statistics page still served FY24). Cross-check against the financials pages and record the source date.
- **Data gaps:** Yahoo has no estimate trend for some names (CEG, RMBS, MTSI, STRL on Nov 4); they score neutral on revisions and fall under the deep-drawdown guard.
- **Judgment inputs:** d, bear and PO are per-name calls; record them with the score.
