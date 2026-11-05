"""Recovery board, Nov 5, 2026 intraday rerun (revision 21). Same inputs as board_2026_11_04.py except price.

User, 10:34 am CT: "make sure you pull today prices." Midday quotes during the post-midterm AI selloff
(Nasdaq about -4%); sources move minute to minute, so times are recorded.
  financhle Nasdaq-100 live list, ~11:40 am ET: NVDA, AVGO, LRCX, MPWR, AMAT, GOOGL, META, ASML, MU, TER, CDNS, KLAC.
  User's YTD figures, 11:34 am ET, on the Dec 31, 2025 closes in board_2026_11_04.py: ANET +23.6%, SMTC +25.5%,
    MTSI +13.5%, GEV +16%, VRT +2%.
  Motley Fool, 11:19 am ET, day moves on Nov 4 closes: ALAB -17.24% (from $223.28), FIX -12.14% (from $1,087.83).
  TIKR, Nov 5: CRDO -17% (from the $136.39 Nov 4 close, twelvedata).
Not refreshed (no live quote reached): TSEM, UBER, BE, and names that can't reach the line on a down day
(ETN, STX, CIEN, VST, CEG, RMBS, STRL, BKNG). TSEM is dead money below $142.26.
"""
from board_2026_11_04 import INPUTS as NOV4
from recovery_score import score, LINE

YE = {k: v["ye_close"] for k, v in NOV4.items() if v.get("ye_close")}
PRICES = {
    'NVDA': 187.27, 'AVGO': 305.85, 'LRCX': 197.25, 'MPWR': 1170.07, 'AMAT': 335.51, 'GOOGL': 284.71,
    'META': 610.31, 'ASML': 1402.79, 'MU': 710.77, 'TER': 223.82, 'CDNS': 319.41, 'KLAC': 135.99,
    'ANET': round(YE['ANET'] * 1.236, 2), 'SMTC': round(YE['SMTC'] * 1.255, 2), 'MTSI': round(YE['MTSI'] * 1.135, 2),
    'GEV': round(YE['GEV'] * 1.16, 2), 'VRT': round(YE['VRT'] * 1.02, 2),
    'ALAB': round(223.28 * (1 - 0.1724), 2), 'FIX': round(1087.83 * (1 - 0.1214), 2), 'CRDO': round(136.39 * 0.83, 2),
}
INPUTS = {k: dict(v, price=PRICES.get(k, v["price"])) for k, v in NOV4.items()}

if __name__ == "__main__":
    rows, off = [], []
    for k, v in INPUTS.items():
        r = score(**v)
        (rows if "final" in r else off).append((k, r))
    rows.sort(key=lambda x: -x[1]["_raw"])
    print(f"line {LINE}")
    for i, (k, r) in enumerate(rows, 1):
        tag = "ON " if r["on_board"] else "   "
        px = INPUTS[k]["price"]
        ex = (f"  GP {r['gp']:+.2f}" if r['gp'] else "") + (f"  CG x{r['cg']:.2f}" if r['cg'] else "")
        ex += (f"  CW {r['cw']:+.1f}" if r['cw'] else "") + (f"  YT {r['yt']:+.1f}" if r['yt'] else "")
        ytd = f"{r['ytd']*100:+5.1f}%" if r['ytd'] is not None else "   n/a"
        stale = "" if k in PRICES else "  (Nov 4 price)"
        print(f"{tag}{i:>2} {k:5} {r['final']:5.2f}  ${px:<8} ytd {ytd}  12m {r['ret_12m']*100:6.1f}%  yrs {r['years']:4.2f}{ex}{stale}")
    for k, r in off:
        stale = "" if k in PRICES else "  (Nov 4 price)"
        print(f"OFF    {k:5} ${INPUTS[k]['price']:<8} {r['excluded']}{stale}")
