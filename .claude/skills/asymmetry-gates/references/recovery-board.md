# Recovery board — 50/50 asymmetry and time-to-high ranking (revision 16, Nov 4, 2026)

The high-IRR ranking used for contest picks and quick comparisons. It scores how much a name can make per unit of risk and how fast it can get back to its high. It orders names only: framework gates (ID, #19 blackouts), dilution limits, sizing and caps still apply. Scorer: [`../scripts/recovery_score.py`](../scripts/recovery_score.py).

## Universe

- **Pool:** underlyings of US-listed leveraged single-stock ETFs (any launch year), plus names the user adds.
- **Excluded before scoring:**
  - ETFs, and companies trading on pending deal terms (CART, LITE, ACLS).
  - Less than 15% below the high.
  - ID fail: TTM gross margin under 20% (framework ID).
  - Dilution: trailing 12-month share growth + undrawn ATM + maximum pending deal shares over 50% of current shares (the IREN rule, H4a's budget). One-time strategic mergers count unless the user exempts them.
  - More than 5 years to the high at the name's growth assumption ("may never return").
- **Convexity bucket:** GAAP-unprofitable (TTM net income below zero) or binary names. They can still rank, but only on convexity inputs: discount ≥30–35%, bear ≥ −45% to −50%, growth ≤35%.

## Inputs

- **High:** highest split-adjusted close in the last 10 years (Nov 4 change; was all-time high). Use closes, not intraday highs.
- **Price:** latest close, or a timestamped intraday quote when repricing during the session.
- **Analyst target:** 12-month average (stockanalysis; MarketBeat when fresher). Record the source date.
- **Target weight w:**
  - w = clip((25% − drawdown) ÷ 10%, 0, 1): fully on the target at 15% below the high, fully on the high at 25%, blended in between.
  - w = 1 when the high was set at more than 2x today's forward P/E (forward EV/sales or P/B when EPS is negative).
- **Upside:** w × (target ÷ price − 1) + (1 − w) × (high ÷ price − 1).
- **Risk discount d:** the name's own "never gets back" risk. The target leg uses max(20%, d); blend with w.
- **Bear case b:** a plausible drop from today's price.
- **Growth g:** expected earnings growth, capped at 35%. Years = ln(high ÷ price) ÷ ln(1 + g).

## Score

- **Asymmetry** = min(10, 3 × upside × (1 − d) ÷ b).
- **Time** = max(0, 10 − 2 × years).
- **Base** = (asymmetry + time) ÷ 2 − 0.25 per 10 points of bear beyond −15%.
- **Time penalty:** −0.15 × (years − 1)² when years > 1 (−0.15 at 2 years, −0.60 at 3, −1.35 at 4).
- **PB:** politician-buy boost (framework PB): +0.2 buy, +0.1 Pelosi holding, cap +0.3.
- **IX:** index-leader bonus (framework IX): +0.1 per top-10 S&P 500 / Nasdaq-100 holding, cap +0.2.
- **PO policy adjustment:** ±0.1 per specific, sourced policy channel (a law, moratorium, tax credit or regulation tied to the company's revenue), cap ±0.2. Re-check each screen. It rates exposure to named policies, never a view on parties.
- **Final** = base − time penalty + PB + IX + PO. Report one decimal; break ties on the unrounded score.

## Labels

- **DM-2yr:** more than 2 years to the 5-year high (the user's dead-money definition). The time penalty already scores it; the label flags it.
- **Board cutoff:** the user sets it (Nov 4: UBER's score and above). Names within 0.05 of the cutoff score also make the board (Nov 4 addendum).

## Known limits

- **Growth-only timeline:** ignores re-rating, so deep cyclicals (chip equipment, power) can recover faster than the model says.
- **Stale targets:** analyst averages lag sharp moves; check the source date.
- **Basis switch:** the 2x forward P/E test uses today's estimates against the multiple at the high; estimate revisions can flip it.
- **Judgment inputs:** d, b, g and PO are per-name calls; record them with the score.
