---
name: fades-sig
description: Tony's leveraged 2x single-stock fund plan (our 9Sig variant): allocation, dip-buy triggers, trim rules and regime-aware trigger calibration. Use when reviewing, rerunning or updating it.
---

# Fades Sig: 1.8x single-stock 2x fund plan

Our version of Jason Kelly's 9Sig, built on 2x single-stock funds instead of TQQQ and bonds. Set up Nov 9, 2026. Format every answer as headers plus short bullets, plain English, no em dashes. End investing answers with "Not financial advice."

## Core setup
- Target leverage: 1.8x total = 90% in 2x funds + 10% cash. Cash is cash (money market or sweep), never bonds.
- Funds only, no 1x shares. Every name runs at 2x, so the only choice is the weight per name.
- Funds: NVDL or NVDU (NVDA), AVGX (AVGO), GGLL (GOOGL), UBRL (UBER). NVDU is about 0.1%/yr cheaper than NVDL; NVDL is much larger. Either is fine.
- Target weights (after earnings staging): NVDL 30%, GGLL 30%, AVGX 15%, UBRL 15%, cash 10%.
- Caps: semis (NVDA + AVGO funds) at or under 50%. Any fund under about $100M AUM capped at 15% (closure = forced taxable sale). UBRL is tiny, so it stays at or under 15%.
- GGLL is the stabilizer (biggest, cheapest, calmest fund) but GOOGL has the lowest expected growth. If NVDA's guide is strong, NVDL 35% / GGLL 25% is allowed (semis then at the 50% cap).

## Earnings staging
- If a name reports within about 2 weeks and options are pricing an unusually big move, hold that fund at about two-thirds of target and keep the rest in cash.
- After the print, if guidance holds (no guide-down), move the held cash into that fund.
- Nov 2026 example: NVDL 20% and cash 20% (1.6x) until NVDA's Nov 17 print, then NVDL 30% and cash 10% (1.8x).

## Rules
- DCA: keep adding new money on schedule at target weights.
- Sell: only when the underlying stock (not the fund) makes a new closing high. Trim that fund back to target weight and move the proceeds to cash to refill the 10%. Never sell into a downtrend.
- Dip cash: split the 10% cash into 2.5% per name. When a name closes at or below its trigger price, put its 2.5% into its 2x fund. If all four fire, leverage reaches about 2.0x.
- Rebalance to target weights every quarter, separate from trims and dip buys, so a winner's fund doesn't take over.
- Re-run triggers each quarter, after each earnings print, and after any regime change.

## Trigger calibration (regime-aware)
1. Window: last 10 years of daily closes (or since IPO). Measure drops from closing highs, not intraday highs.
2. Regime start: the latest of (a) 10 years ago, (b) the first year of sustained positive GAAP net income and positive free cash flow, (c) a user-flagged structural break (major merger, business-model change). Drops from before the current regime don't count.
3. List every drawdown of 20% or more inside the regime, including the current one at its depth so far.
4. Trigger = the second-deepest of those drawdowns, rounded toward zero to the nearest 5%. This is the deepest level the stock has hit at least twice.
5. Cap at -40% so the cash doesn't wait for a once-a-decade crash.
6. Fallback: fewer than two 20%+ drawdowns in the regime means a -30% trigger until more history builds.
7. Trigger price = closing high x (1 + trigger).
8. Today's buy counts as the first tranche. The dip cash only goes in at the trigger, even if the stock was already down when the plan started.

## Triggers as of Nov 9, 2026
| Name | Regime | Drops counted | Trigger | Price | Status |
|---|---|---|---|---|---|
| NVDA | full decade | 2018 -56%, 2020 ~-38%, 2022 -66%, 2024 ~-27%, 2025 ~-37% | -40% (capped from -55%) | $143.54 | 19% away |
| AVGO | full decade | 2018 -27%, 2020 -48%, 2022 -35%, 2025 -42%, now -39% | -40% | $288.94 | 1.6% away |
| GOOGL | full decade | 2018 -23%, 2020 -31%, 2022 -44%, 2025 ~-30%, now -29% | -30% | $281.83 | 1% away |
| UBER | since 2023 (first profitable year) | 2024 -28%, 2024 -31%, now -31% | -30% | $70.07 | Fired (UBER $68.59) |

Closing highs (10-year, from the asymmetry-gates board): NVDA $239.24, AVGO $481.57, GOOGL $402.62, UBER $100.10.

## Leverage math (why the numbers are what they are)
- Max-growth leverage per name: L* = 0.5 + (ln(1 + expected stock CAGR) - borrow cost) / volatility^2. Borrow cost = risk-free rate + about 1.5% (about 5.75% in late 2026).
- Decay in a daily 2x fund comes from each stock's own volatility. Holding four funds doesn't diversify it away.
- At about 48% volatility, 1.8x beats 1.5x only if the stock compounds about 35%/yr or more. At 75% of consensus growth, the best blended leverage for these four was about 1.27x; at full consensus, about 1.56x. Tony chose 1.8x knowingly as a bet on strong AI-era growth.
- Nov 2026 per-name best leverage at full consensus: NVDA ~2.0x, UBER ~2.0x, AVGO ~1.5x, GOOGL ~1.4x. NVDA's number is very sensitive to volatility: at 50% vol it drops to ~1.5x.
- Reality check from NVDL: NVDA rose about 10x over NVDL's life; a frictionless 2x would have made about 100x; NVDL made about 17x.

## Data sources
- Drawdown history: portfolioslab.com/symbol/TICKER (Worst Drawdowns table; check it isn't stale, and fill recent drops from dated news if missing).
- Volatility: alphaquery 180-day historical volatility (close-to-close).
- Prices and closes: stockanalysis.com/stocks/TICKER/history/ (dated closes); stockscan.io as backup.
- Growth: consensus 3-year EPS growth, capped at 35% (same as the board).
- Fund AUM and fees: issuer pages, stockanalysis ETF pages.

## When asked to review or rerun
- Pull fresh closes, recompute each name's drawdown from its closing high, and report which triggers fired.
- Check for regime changes (profitability flips, big mergers) and recalibrate those names.
- Flag any fund whose AUM fell or that announced closure.
- Report current leverage, weights versus target, and any trims due at new closing highs.
