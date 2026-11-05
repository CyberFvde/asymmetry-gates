"""Recovery board, Nov 5, 2026 close rerun (revision 21). Midday file plus closing prices where a close was reachable.

Closes (sources checked 3:20-3:40 pm CT):
  financhle Nasdaq-100 / S&P 500 lists, after-hours status: NVDA, AVGO, LRCX, MPWR, AMAT, GOOGL, META, ASML, MU,
    TER, CDNS, KLAC, STX.
  bullfincher, 4:03-4:09 pm ET: ANET $159.16 (-10.82%), GEV $770.51 (-7.48%).
  StockStory, Nov 5 session: SMTC $92.60 (-16.7%).
  eodhd, Nov 5: TSEM $130.92. Single source with an inconsistent change field; below the $142.29 dead-money line.
Midday quotes kept (no close reached): ALAB, CRDO, FIX, MTSI, VRT. Nov 4 kept: UBER, BE and the rest.
"""
from board_2026_11_05 import INPUTS as MIDDAY, PRICES as MID_PRICES
from recovery_score import score, LINE

CLOSE = {
    'NVDA': 181.80, 'AVGO': 291.48, 'LRCX': 183.74, 'MPWR': 1131.94, 'AMAT': 319.33, 'GOOGL': 282.35,
    'META': 605.31, 'ASML': 1358.02, 'MU': 659.71, 'TER': 212.56, 'CDNS': 311.59, 'KLAC': 129.70, 'STX': 466.00,
    'ANET': 159.16, 'GEV': 770.51, 'SMTC': 92.60, 'TSEM': 130.92,
}
INPUTS = {k: dict(v, price=CLOSE.get(k, v["price"])) for k, v in MIDDAY.items()}

if __name__ == "__main__":
    rows, off = [], []
    for k, v in INPUTS.items():
        r = score(**v)
        (rows if "final" in r else off).append((k, r))
    rows.sort(key=lambda x: -x[1]["_raw"])
    src = lambda k: "close" if k in CLOSE else ("midday" if k in MID_PRICES else "Nov 4")
    for i, (k, r) in enumerate(rows, 1):
        ex = (f" GP{r['gp']:+.2f}" if r['gp'] else "") + (f" CG" if r['cg'] else "")
        ex += (f" CW{r['cw']:+.1f}" if r['cw'] else "") + (f" YT{r['yt']:+.1f}" if r['yt'] else "")
        ytd = f"{r['ytd']*100:+5.1f}%" if r['ytd'] is not None else "  n/a"
        print(f"{'ON ' if r['on_board'] else '   '}{i:>2} {k:5} {r['final']:5.2f} ${INPUTS[k]['price']:<8} ytd {ytd} 12m {r['ret_12m']*100:5.0f}% yrs {r['years']:.2f}{ex} [{src(k)}]")
    for k, r in off:
        print(f"OFF    {k:5} ${INPUTS[k]['price']:<8} {r['excluded']} [{src(k)}]")
