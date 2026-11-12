# Forward test: do the picks beat holding the giants?

Started Nov 11, 2026. Every backtest of the fades-sig plan chose its stocks with hindsight. This file keeps score going forward, where hindsight can't get in.

## Why this exists
- With no hindsight, the fades-sig rules alone roughly matched holding the five largest US companies (about 16% a year since 2009 against 18.6%).
- Any return above holding has to come from the stock picks.
- The only clean way to check the picks is to write them down on the day and score them later.

## Rules
- A cohort is a dated list of picks. Once written, a cohort is never edited and no name is ever removed from it.
- Entry price is the closing price on the cohort's entry date.
- Scoring uses plain shares in equal weights, with dividends where available. No leverage, so the score measures picking skill only.
- Benchmark A: plain shares of the five largest US companies on the entry date, in equal weights, over the same dates.
- Benchmark B: QQQ over the same dates.
- Each quarterly check also logs the newest board in `roster.md` as a new cohort, every name on it, at that day's close.
- No verdict before 12 months and at least 20 scored picks. "Beats holding" means the cohort average leads Benchmark A by 3 points a year or more across most cohorts.

## Cohort 1: May 12, 2026, physical AI infrastructure list
- Source: a top-25 list built in chat before the gates existed, so it tests the thesis more than the gates.
- Entry date: May 12, 2026 close.
- Benchmark A names and entry closes: NVDA $220.78, AAPL $294.80, GOOGL $387.35, MSFT $407.77, AMZN $265.82.

| # | Ticker | Group | Entry close |
|---|---|---|---|
| 1 | SRE | Power | to fill |
| 2 | ETR | Power | to fill |
| 3 | LNT | Power | to fill |
| 4 | PEG | Power | to fill |
| 5 | NEE | Power | to fill |
| 6 | D | Power | to fill |
| 7 | VST | Power | to fill |
| 8 | BKR | Gas and turbines | to fill |
| 9 | EQT | Gas and turbines | to fill |
| 10 | LNG | Gas and turbines | to fill |
| 11 | ANET | Networking | $142.54 |
| 12 | AVGO | Networking | $419.30 |
| 13 | CSCO | Networking | $99.29 |
| 14 | MU | Memory and storage | to fill |
| 15 | WDC | Memory and storage | to fill |
| 16 | STX | Memory and storage | to fill |
| 17 | TSM | Foundry and semi-cap | $397.28 |
| 18 | INTC | Foundry and semi-cap | to fill |
| 19 | AMAT | Foundry and semi-cap | to fill |
| 20 | LRCX | Foundry and semi-cap | to fill |
| 21 | NVT | Cooling and electrical | to fill |
| 22 | HUBB | Cooling and electrical | to fill |
| 23 | ATKR | Cooling and electrical | to fill |
| 24 | RRX | Cooling and electrical | to fill |
| 25 | CCJ | Nuclear fuel | to fill |

## Cohort 2: Nov 6, 2026, gates board (revision 22)
- Source: the board of 12 in `roster.md`, dated Nov 10, 2026, on Nov 6 closes.
- Entry date: Nov 6, 2026 close.
- Benchmark A names and entry closes: NVDA $186.64, AAPL $342.37, GOOGL $284.78, MSFT $530.61, AMZN $259.30.

| # | Ticker | Board score | Entry close |
|---|---|---|---|
| 1 | NVDA | 8.86 | $186.64 |
| 2 | TER | 7.16 | $218.22 |
| 3 | AVGO | 6.76 | $293.69 |
| 4 | LRCX | 5.74 | $200.44 |
| 5 | MTSI | 5.53 | $210.98 |
| 6 | GOOGL | 5.41 | $284.78 |
| 7 | META | 5.20 | $610.15 |
| 8 | MPWR | 5.16 | $1,190.44 |
| 9 | SMTC | 5.10 | $103.21 |
| 10 | AMAT | 4.91 | $332.72 |
| 11 | FIX | 4.82 | $1,017.50 |
| 12 | UBER | 4.82 | $68.59 |

## Results log

### Nov 9, 2026 (setup day, partial)
- Cohort 1, four of 25 names priced so far: ANET +30.6%, CSCO +0.1%, TSM -1.7%, AVGO -23.5%. Average +1.4%.
- Benchmark A over the same dates: +1.9% (MSFT +34.2%, AAPL +19.1%, AMZN +0.4%, NVDA -18.9%, GOOGL -25.5%).
- Read: even so far, and four names is too few to mean anything. The other 21 entry closes get filled at the first quarterly check.
- Cohort 2 is three days old. No score yet.
- Benchmark B (QQQ) entry values for both cohorts: to fill at the first quarterly check.
