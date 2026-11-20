# Recovery board: fundamentals-first contest ranking (revision 27, Nov 19, 2026)

The high-IRR ranking used for contest picks and quick comparisons. Half the score is business quality; the other half is how much the stock can make over the next 12 months against its fair value, per unit of risk. Distance to the high only decides who enters (20% minimum since revision 26; 15% before). Share shrink adds points under BB (revision 24), a business line facing a headwind costs points under HT (revision 25), and every score is also shown under three stacked risks under SL (revision 27). It orders names only: framework gates (ID, #19 blackouts), dilution limits, sizing and caps still apply, verified gate fails cost points under GP (revision 19), cyclical names at a peak are scored on through-cycle numbers under CG (revision 20), names that lean on a few customers lose points under CC (revision 22), and names whose 3-year return estimate is 25% a year or more gain points under RE (revision 23). Scorer: [`../scripts/recovery_score.py`](../scripts/recovery_score.py); dated inputs: [`../scripts/board_2026_11_04.py`](../scripts/board_2026_11_04.py); CC inputs: [`../scripts/board_2026_11_06_close.py`](../scripts/board_2026_11_06_close.py); latest board with RE inputs: [`../scripts/board_2026_11_06_close_re.py`](../scripts/board_2026_11_06_close_re.py).

## Universe

- **Pool:** underlyings of US-listed leveraged single-stock ETFs (any launch year), plus names the user adds.
- **Excluded before scoring:**
  - ETFs, and companies trading on pending deal terms (CART, LITE, ACLS).
  - **Market Mondays blocker (revision 26, Nov 17, 2026; the user's "Ian Dunlap Rashad Bilal EYL Market Mondays blocker"):** less than 20% below the high (highest split-adjusted close in the last 10 years). 30% down is the ideal; 20% is the floor. Was 15%.
  - **Falling estimates (revision 26, Nov 17, 2026; framework EB):** next-year consensus EPS down 3% or more over 90 days. Down less than 3%: the name stays, tagged "watch", with no extra penalty because the revisions factor already counts it.
  - ID fail: TTM gross margin under 20% (framework ID).
  - Dilution: trailing 12-month share growth + undrawn ATM + maximum pending deal shares over 50% of current shares (the IREN rule, H4a's budget). One-time strategic mergers count unless the user exempts them.
  - **Guide-down (GD, revision 18):** the latest guidance midpoint for revenue, EPS or EBITDA (next quarter, or full year when that is all the company gives) came in more than 3% below consensus at the print (misses of 3% or less count as in line; Nov 4 addendum). One metric past the band is enough; use the consensus reported with the print and record its source. Out until the next print; companies that give no numeric guidance pass. Check it first, every screen.
  - **Dead money (revision 26, Nov 16, 2026):** a name is out only if it trails UBER on both measures, 12-month return to fair value (44%) and forecast growth (31%), and its quality score is under 7.5. However deep the drop, beating UBER on either one keeps it. GOOGL stays by name (user: Google-quality names stay). Before revision 26: more than 2.7 years to the high at consensus growth.
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
  - Above 15%: −0.5 (revision 26, Nov 16, 2026). Above 25%: −1.0. Above 50%: −1.5. Above 100%: −2.0.
  - Every name, every screen. Measure at the board price, not a later quote.

## CC: customer-concentration penalty (revision 22, Nov 10, 2026)

A name that leans on a few customers loses points, because one lost or delayed customer can reset the numbers and the market prices that risk. Ranking only: CC never unlocks or blocks capital. It stacks with GP, CW and YT and has its own cap of −1.0.

- **Source:** the latest annual report (10-K or 20-F): every customer at 10% or more of revenue. Use a later 10-Q only when it shows a new, larger exposure.
- **Three tests, worst one counts:**

| Test | Minor −0.25 | Moderate −0.5 | Severe −1.0 |
|---|---|---|---|
| Largest customer, share of revenue | 15% to under 25% | 25% to under 40% | 40% or more |
| All 10%+ customers combined | 30% to under 45% | 45% to under 65% | 65% or more |
| One customer's share of disclosed backlog or remaining performance obligations | | 25% to under 50% | 50% or more |

- **Distributors and resellers:** count at half their share. They pass product on to many end buyers, so the single-buyer risk is smaller.
- **Backlog test:** run it only when filings let you compute one customer's share of backlog or remaining performance obligations (a disclosed contract against the disclosed total). It catches revenue that is about to concentrate before the annual report shows it.
- **No double count:** direct customers and "specifying" or end-customer figures overlap. Use the direct figures and note the rest.
- **Open items:** a name whose filing hasn't been pulled is tagged "CC open" and takes no points. Pull it for every name above the line and every name within 1.0 of it, so checked names aren't penalized next to unchecked ones.
- **Re-check:** at each new annual report, and when a single contract moves backlog by a quarter or more.

## RE: return-estimate boost (revision 23, Nov 11, 2026)

A name whose 3-year return estimate is 25% a year or more moves up. The screen bar stays at 20% (framework C's guardrail); RE rewards the names that clear it with room to spare. Ranking only: RE never passes a gate, unlocks capital or changes sizing, and it stacks with every other adjustment.

- **Input:** framework C's return estimate at the board price. Base year = the first fiscal year ending at least six months out; exit multiple = the lower of the entry multiple and 30× (35× when the 3-year EPS growth is 25%+), never above the five-year median forward P/E; plus trailing dividend yield; no buyback add.
- **Tiers:**

| Return estimate | Points |
|---|---|
| Under 25% | 0 |
| 25% to under 35% | +0.25 |
| 35% or more | +0.5 |

- **Why 35%:** cut a 35% estimate by 30% and it is still 24.5%, above the 20% bar. The top tier marks names that keep their place even if the forecasts prove a third too high.
- **Growth path:** consensus where framework C's coverage test is met (3+ analysts, or two sources within 10%). A single-source figure counts only when it is below the faded value. Every other year fades at 85% of the prior year's growth. stockanalysis shows analyst counts for the first forecast year only, so on the board most paths are one single-source year followed by two faded years.
- **Third forecast year:** stockanalysis locks it. Back it out of the statistics page's "EPS Growth Forecast (3Y)": last reported fiscal-year EPS × (1 + growth)³. It is a single-source figure.
- **CG names:** a name with the cycle guard triggered takes no RE points. Its forward path is built on peak-cycle earnings.
- **Open items:** a name whose estimate hasn't been pulled is tagged "RE open" and takes no points. Pull it for every name above the line and every name within 0.5 of it, so checked names aren't ranked next to unchecked ones.
- **Re-check:** every screen (the estimate moves with price when the exit cap binds) and after each print. Record the base year, path, multiples, dividend and page dates with the score.

## BB: buyback boost (revision 24, adopted Nov 11, 2026; recorded Nov 19)

A name that is shrinking its share count moves up. Ranking only: BB never unlocks capital or overrides dead money. Cap +2.0.

- **Two legs, same tiers:** 2% to under 4% earns +0.5; 4% or more earns +1.0. Each leg pays on its own, so a name whose count fell and is set to keep falling collects twice (the user's "double bonus").
- **Trailing leg:** fall in diluted weighted-average shares, latest reported quarter against the same quarter a year earlier.
- **Forward leg:** four times the latest quarter's repurchases less stock-based compensation, limited to the remaining authorization, as a share of market cap at the board price. Trailing-12-month free cash flow has to cover it.
- **No penalty side:** a rising count earns nothing and needs no flag (user, Nov 11; GOOGL was the example). Heavy dilution is handled by the dilution exclusion in Universe.
- **Open items:** a name whose counts haven't been pulled is tagged "BB open" and takes no points.
- **Known limits:** consensus EPS growth already includes expected buybacks, so BB pays partly for something the growth factor has seen. The forward leg annualizes one quarter. Peak-cycle cash flow buys stock at peak prices; CG, CW and YT still apply.

## HT: headwinds (revision 25, adopted Nov 11, 2026; recorded Nov 19)

A business line facing a named headwind costs points by its share of latest-quarter revenue. Ranking only. Cap -1.0.

| Line's share of latest-quarter revenue | Live headwind | Near headwind |
|---|---|---|
| 10% to under 25% | -0.25 | 0 |
| 25% to under 50% | -0.5 | -0.25 |
| 50% or more | -1.0 | -0.5 |

- **Live:** the line shrank year over year, or the company reported losing share, price or a customer to the force.
- **Near:** a new substitute or entrant is selling into the line's market (or has a dated launch within 24 months) and is doubling or already 10% of that market, while the line still grows.
- **Growth rates:** organic where the company reports it. An accounting change does not make a line shrink.
- **Tailwinds were tried and retired the same day.** They paid twice for growth the quality factors already score, rewarded how a company slices its segments, and lifted 16 of 17 names against a fixed line.
- **Open items:** a name whose lines haven't been pulled is tagged "HT open" and takes no points.

## SL: three-risk stress lens (revision 27, Nov 19, 2026)

Every score and ranking is shown four ways: today, then with three risks stacked on top of each other. Reporting only: SL never moves a name on or off the board, never changes the line and never unlocks capital. Scorer: `lens()`; first run: [`../scripts/board_2026_11_19_lens.py`](../scripts/board_2026_11_19_lens.py).

| Case | What changes |
|---|---|
| **1. Rates keep rising** | Fair value cut 10% (target and fair P/E); 15% for a name at 2x Debt / EBITDA or more with no net cash. Bear case +5 points. |
| **2. SemiAnalysis is right** (adds to 1) | Next-year EPS cut by e1: the 90-day revision falls by e1 and the target by twice e1. Following-year EPS cut by e2, which lowers forecast growth and the RE estimate. Risk discount d +5 points, bear +5. |
| **3. Capex peaks in 2028, then falls** (adds to 2) | Scored on mid-cycle numbers: k = 1 - half the AI share, or average / latest ROIC for a CG name when that is lower. ROIC, margins and NTM EPS scale by k (five-year average margins when pulled). Target cut by four times e1, up to 60%. Estimates stop rising. At 25% AI exposure or more: forecast growth capped at 15%, CW set to -1.5, no RE. d +5, bear +5. |

- **Per-name judgment inputs, recorded with each board:** ai (share of revenue tied to the AI accelerator and data-center build), e1 and e2.
- **Basis for e1 and e2:** SemiAnalysis's Nov 13, 2026 model update: AI accelerator capex about $392B in 2026, $627B in 2027 (cut 19%), $758B in 2028 (cut 28%), $796B in 2029, $923B in 2030 (cut 40%); Nvidia compute revenue cut 22% for 2027 and 39% for 2028; chip area over 2026 to 2030 cut 17%; HBM cut 30% for 2028; power demand cut 34% for 2030. The figures come from press summaries of a subscriber note, not the note itself.
- **AI spenders (GOOGL, META):** no cut and no credit. Lower capex would help their cash flow; the lens doesn't score that.
- **Entry gates** (falling estimates, dead money) apply to the today column only. They are tests on today's numbers, and the dead-money bar is fixed to UBER's unstressed figures.
- **Names with no forward P/E history** (TSM, ASML): case 3 uses an estimated normal forward P/E, recorded with the board, so mid-cycle earnings have something to multiply.
- **Reading it:** a name that stays at or above the line in case 2 doesn't need SemiAnalysis to be wrong. A name that only clears the line today is a bet that it is.
- **Known limits:** the hit sizes are judgment, not data. Case 3 has no date on it, so it is a statement about how much of today's earnings are cycle, not a 12-month forecast. Rates are modeled only through multiples.

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
- **CC customer concentration (revision 22):** see the section above; 0 to −1.0.
- **RE return-estimate boost (revision 23):** see the section above; 0 to +0.5.
- **BB buyback boost (revision 24):** see the section above; 0 to +2.0.
- **HT headwinds (revision 25):** see the section above; 0 to −1.0.
- **Final** = 0.5 × quality + 0.25 × asymmetry + 0.25 × speed − bear penalty + PB + IX + PO + GP + CW + YT + CC + RE + BB + HT. Report one decimal (two at the line); break ties on the unrounded score.

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
- **Dead-money line (revision 26):** UBER's 44% 12-month return and 31% forecast growth, fixed Nov 16, 2026, with a quality pass at 7.5. The 2.7-year line set by CRDO applied through revision 25.
- Both are fixed numbers. They don't float with UBER's or CRDO's prices; change them only by user request.

## Known limits

- **Peak-cycle quality:** CG (revision 20) covers memory, storage, equipment, foundry and commodity names. Booking-cycle names (power equipment, contractors) get CW points but no rescoring, on annual data. A 20-reading average can sit inside one long upcycle (LRCX, ASML); CW's 1.5× band is there to catch those.
- **YT timing:** YTD resets every Jan 1, so a name that ran in December escapes in January. Recent winners have tended to keep winning over 6–12 months, so YT gives up some momentum upside for less chase risk; the user chose that trade.
- **CC blind spots:** half weight on distributors can hide who the end buyers are (AVGO's top five end customers are about 40% of revenue; NVDA's direct customers include server builders selling on to a few cloud companies). Equipment makers (LRCX, ASML, AMAT) have always sold to a handful of chipmakers, and CC does not separate that from a new dependence on one buyer. Shares come from the last annual report and can be a year old.
- **RE is mechanical:** a faded path seeded by one very strong year stays strong for three years, so fast growers in an upcycle reach the top tier easily (AVGO, SMTC, GEV and BE on Nov 11). A distorted base year does the opposite (GOOGL's consensus has 2027 EPS below 2026, so its path fades from a decline). The third-year figure is backed out of a growth rate and has no analyst count. RE also overlaps the growth factor in quality, so growth counts twice by design. CW, YT and the CG exclusion are the offsets.
- **Stale data:** stockanalysis pages can lag a print (TER's statistics were pre-print on Nov 4; CRDO's statistics page still served FY24). Cross-check against the financials pages and record the source date.
- **Data gaps:** Yahoo has no estimate trend for some names (CEG, RMBS, MTSI, STRL on Nov 4); they score neutral on revisions and fall under the deep-drawdown guard.
- **Judgment inputs:** d, bear and PO are per-name calls; record them with the score.
