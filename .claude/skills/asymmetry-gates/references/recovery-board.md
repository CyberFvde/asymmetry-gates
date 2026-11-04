# Recovery board: fundamentals-first contest ranking (revision 17, Nov 4, 2026)

The high-IRR ranking used for contest picks and quick comparisons. Half the score is business quality; the other half is how much the stock can make over the next 12 months against its fair value, per unit of risk. Distance to the high only decides who enters (15% minimum) and who is dead money. It orders names only: framework gates (ID, #19 blackouts), dilution limits, sizing and caps still apply. Scorer: [`../scripts/recovery_score.py`](../scripts/recovery_score.py); dated inputs: [`../scripts/board_2026_11_04.py`](../scripts/board_2026_11_04.py).

## Universe

- **Pool:** underlyings of US-listed leveraged single-stock ETFs (any launch year), plus names the user adds.
- **Excluded before scoring:**
  - ETFs, and companies trading on pending deal terms (CART, LITE, ACLS).
  - Less than 15% below the high (highest split-adjusted close in the last 10 years).
  - ID fail: TTM gross margin under 20% (framework ID).
  - Dilution: trailing 12-month share growth + undrawn ATM + maximum pending deal shares over 50% of current shares (the IREN rule, H4a's budget). One-time strategic mergers count unless the user exempts them.
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
| Debt | Debt / EBITDA | 4.0x | 0.5x or less |
| Revisions | Yahoo EPS trend: next-year consensus EPS, now vs 90 days ago | −10% | +10% |

- The cash cap stops customer prepayments (GEV) from passing as quality. Averaging OCF with FCF credits heavy reinvestment (GOOGL, META) while still docking capex that hasn't proven its return.
- No revision data scores neutral (5). Compute a missing ROIC with the stockanalysis method rather than a different formula.

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
- **Final** = 0.5 × quality + 0.25 × asymmetry + 0.25 × speed − bear penalty + PB + IX + PO. Report one decimal (two at the line); break ties on the unrounded score.

## Lines (fixed Nov 4, 2026)

- **Board line:** final score ≥4.46, set by UBER's post-print score (4.51) less the 0.05 band.
- **Dead-money line:** ≤2.7 years to the high at consensus growth, set by CRDO (2.68).
- Both are fixed numbers. They don't float with UBER's or CRDO's prices; change them only by user request.

## Known limits

- **Peak-cycle quality:** chip-equipment margins and ROIC are measured near the top of the AI capex cycle, and the consensus growth that clears them through the dead-money cut can fall. The revision factor and the deep-drawdown guard catch that at the next screen.
- **Stale data:** stockanalysis pages can lag a print (TER's statistics were pre-print on Nov 4; CRDO's statistics page still served FY24). Cross-check against the financials pages and record the source date.
- **Data gaps:** Yahoo has no estimate trend for some names (CEG, RMBS, MTSI, STRL on Nov 4); they score neutral on revisions and fall under the deep-drawdown guard.
- **Judgment inputs:** d, bear and PO are per-name calls; record them with the score.
