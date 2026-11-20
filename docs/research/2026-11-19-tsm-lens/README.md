# TSM re-test and the three-risk lens (Nov 19, 2026)

Screen date Thu Nov 19, 2026, after the close. Rules: framework revision 27, recovery-board revision 27. Scorer run: `.claude/skills/asymmetry-gates/scripts/board_2026_11_19_lens.py`; output in [`results.txt`](results.txt).

## Verdict

- **Gates:** out of core on A3(c), no alternate route, zero new capital. Unchanged from Oct 24.
- **Recovery-board score:** 5.84 at $352.09 against a 4.46 line.
- **Under the lens:** 4.86 with rates rising, 3.58 if SemiAnalysis is also right, 1.17 if capex also peaks in 2028.

## Gates

| Test | Result | Figure |
|---|---|---|
| ID gross margin | pass | 65.85% TTM |
| A1 share count | pass | +0.01% YoY |
| A3(c) capex / OCF | **fail** | trailing 52.7% ($50.07B / $95.08B); forward 54 to 58% on Oct 24, not re-pulled |
| 3a, M | closed | 2023 revenue fell 4.5% in NT$; reopens when FY2028 reports |
| G2 | fail | same 50% capex test |
| A4 leverage | pass | net cash $100.36B |
| #11 valuation | pass | forward P/E 16.96 |
| #12 target | pass | $586.69, +66.6%, 21 analysts |
| #19, #7 | pass | carried from the Oct 24 deep check |
| Market Mondays (20% down) | pass | 27.5% below the $485.80 record close of Oct 5, 2026 |
| EB falling estimates | pass | 2027 EPS $23.39 now against $21.28 ninety days ago, +9.9% |
| PH, DM | clear | high is six weeks old |

The one failed gate is TSM's own capex load: $60 to 64B guided for 2026, with brokers at $83 to 105B for 2027 and 2028 on Oct 16. That spend lands in the years SemiAnalysis now sees accelerator spending slow.

## Score build

- Quality 9.99: 3-year EPS growth forecast 42.41%, operating margin 57.96%, ROIC 60.30%, net cash, revisions +9.9%.
- Fair value: the $586.69 target alone. stockanalysis shows no forward P/E history for the ADR. With an estimated 19x multiple leg the score is 5.46.
- CW -1.0: latest quarterly ROIC 66.30% against a 20-quarter average of 43.29%, 1.53x. Under 1.5x it clears.
- YT -0.5: +15.9% from the $303.89 Dec 31, 2025 close. A close under $349.47 clears it (score about 6.4).
- CC -0.25: Customer A 19% and Customer B 17% of 2025 net revenue (20-F).
- Bear -0.38 on a 30% bear case. RE +0.25 on a 25.2% three-year estimate (entry and exit 15.05x).
- No PB, IX, BB or GP points. HT open.

## Lens inputs for TSM

- ai 0.33: AI accelerators were a high-teens share of 2025 revenue and are growing faster than the company.
- e1 0.05, e2 0.12: TSM is paid per wafer, and SemiAnalysis cut chip area 17% over 2026 to 2030 against 28 to 40% for dollars. The 2028 figure allows for customers pushing back on wafer prices.
- Mid-cycle factor 0.653 (average / latest ROIC); mid-cycle NTM EPS $13.56 against $20.76; estimated normal forward P/E 19x.
- Return estimate if SemiAnalysis is right: 17.2% a year.

## Board sensitivity

See `results.txt`. The 22 board names run on Nov 6 closes, the last complete pull, so the table shows how each score moves under the three risks. It is not a Nov 19 ranking.

## Sources

- stockanalysis: TSM overview, statistics (updated Nov 13, 2026), forecast and quarterly ratios pages
- Yahoo Finance: TSM analysis page (EPS trend)
- TSMC 2025 Form 20-F (customer concentration)
- 24/7 Wall St, Nov 16, 2026, and macrotrends (record close, year-end close)
- Yahoo Finance and VLSI.kr on the SemiAnalysis Nov 13, 2026 update; Toobit for the 2029 figure
- Oct 24, 2026 deep check: `docs/research/2026-10-24-rev8-history-rerun/deep/taiwan.md`

## Caveats

- e1, e2, ai, d and bear are judgment inputs.
- #7, #19 and forward capex/OCF were not re-pulled.
- The user's app showed TSM up about 7% YTD at $345 after hours, which fits a start at the first close of 2026. YT is defined on the prior year-end close.
