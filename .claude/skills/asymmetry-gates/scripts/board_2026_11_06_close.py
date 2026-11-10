"""Recovery board, Nov 6, 2026 close, with CC customer-concentration points (revision 22).

Same inputs as board_2026_11_05_close.py except price and the new cc input. Run Nov 10, 2026.

Closes (pulled Nov 9): stockanalysis history pages dated "At close: Nov 6, 2026" for NVDA, AVGO, TER, MPWR, ANET,
GOOGL, META, ASML, VRT, GEV, BE, LRCX, AMAT; stockanalysis quote pages for UBER and CDNS; stockscan dated Nov 6
closes for SMTC, FIX, TSEM; MTSI from stockscan (prior close $190.35, +10.84%). Names not listed keep their Nov 5
close; none of them can reach the line.

CC inputs: shares of revenue from the latest annual report (10-K, or 20-F for ASML), as fractions. "direct" are
10%+ customers; "resellers" are 10%+ customers the filing calls a distributor or reseller (half weight); "backlog"
is one customer's share of disclosed backlog or remaining performance obligations; "combined" is used when the
filing gives only the total. Pulled Nov 10, 2026.
  NVDA  FY2026 10-K: two direct customers, 22% and 14%.
  AVGO  FY2025 10-K: one distributor 32% (top five end customers about 40%). Backlog: remaining performance
        obligations went from $45.0B to $164.6B in the quarter the Anthropic TPU lease was signed and stood at
        $179.2B on Aug 2, 2026. That $119.6B step is 67% of the total (Anthropic's S-1 lists $161.2B of
        non-cancelable Broadcom leases, which would be 90%).
  TER   2025 10-K: one direct customer 19%. Two specifying customers at 12% and 10% overlap direct sales and
        are not added.
  LRCX  FY2026 10-K: four customers, 16%, 15%, 12%, 12%.
  AMAT  FY2025 10-K: two customers, 19% and 15%.
  ASML  2025 annual report: four customers above 10%, 61.2% combined (single shares not found; the largest
        cannot exceed 31.2%).
  ANET  2025 10-K: two customers, 26% and 16%.
  MPWR  2025 10-K: three distributors, 26%, 18%, 10%; no end customer at 10%.
  MTSI  FY2025 10-K: two resellers, 12.4% and 11.2%; no direct customer at 10%.
  SMTC  FY2026 10-K: two customers, 14% and 11%.
  FIX   2025 10-K: one customer 12.8%.
  BE    2025 10-K: three customers, 43%, 13%, 12% (the largest a related party).
  CDNS, VRT, GEV: no 10% customer found in the latest 10-K.
  GOOGL, META, UBER: advertiser, cloud and rider bases with no 10% customer; not re-pulled for this screen.
Open (not pulled; off the board on other tests, so CC cannot change their standing): MU, CRDO, ALAB, RMBS, KLAC,
STRL, TSEM, STX, ETN, CIEN, VST, CEG, BKNG.
"""
from board_2026_11_05_close import INPUTS as NOV5, CLOSE as NOV5_CLOSE
from recovery_score import score, cc_points, LINE

CLOSE = {
    'NVDA': 186.64, 'AVGO': 293.69, 'TER': 218.22, 'MPWR': 1190.44, 'MTSI': 210.98, 'ANET': 170.80,
    'GOOGL': 284.78, 'SMTC': 103.21, 'META': 610.15, 'FIX': 1017.50, 'ASML': 1424.75, 'UBER': 68.59,
    'CDNS': 319.92, 'VRT': 182.86, 'GEV': 774.11, 'BE': 173.24, 'LRCX': 200.44, 'AMAT': 332.72, 'TSEM': 137.34,
}
CC = {
    'NVDA': dict(direct=(0.22, 0.14)),
    'AVGO': dict(resellers=(0.32,), backlog=0.67),
    'TER': dict(direct=(0.19,)),
    'LRCX': dict(direct=(0.16, 0.15, 0.12, 0.12)),
    'AMAT': dict(direct=(0.19, 0.15)),
    'ASML': dict(combined=0.612),
    'ANET': dict(direct=(0.26, 0.16)),
    'MPWR': dict(resellers=(0.26, 0.18, 0.10)),
    'MTSI': dict(resellers=(0.124, 0.112)),
    'SMTC': dict(direct=(0.14, 0.11)),
    'FIX': dict(direct=(0.128,)),
    'BE': dict(direct=(0.43, 0.13, 0.12)),
    'CDNS': {}, 'VRT': {}, 'GEV': {}, 'GOOGL': {}, 'META': {}, 'UBER': {},
}
INPUTS = {k: dict(v, price=CLOSE.get(k, v["price"]), cc=cc_points(**CC.get(k, {}))) for k, v in NOV5.items()}

if __name__ == "__main__":
    rows, off = [], []
    for k, v in INPUTS.items():
        r = score(**v)
        (rows if "final" in r else off).append((k, r))
    rows.sort(key=lambda x: -x[1]["_raw"])
    src = lambda k: "Nov 6" if k in CLOSE else ("Nov 5" if k in NOV5_CLOSE else "Nov 4")
    for i, (k, r) in enumerate(rows, 1):
        ex = (f" GP{r['gp']:+.2f}" if r['gp'] else "") + (f" CG" if r['cg'] else "")
        ex += (f" CW{r['cw']:+.1f}" if r['cw'] else "") + (f" YT{r['yt']:+.1f}" if r['yt'] else "")
        ex += (f" CC{r['cc']:+.2f}" if r['cc'] else "") + ("" if k in CC else " CC open")
        ytd = f"{r['ytd']*100:+5.1f}%" if r['ytd'] is not None else "  n/a"
        print(f"{'ON ' if r['on_board'] else '   '}{i:>2} {k:5} {r['final']:5.2f} (pre-CC {r['final'] - r['cc']:5.2f}) "
              f"${INPUTS[k]['price']:<8} ytd {ytd} yrs {r['years']:.2f}{ex} [{src(k)}]")
    for k, r in off:
        print(f"OFF    {k:5} ${INPUTS[k]['price']:<8} {r['excluded']} [{src(k)}]")
