"""Recovery board, Nov 6, 2026 closes, with the RE return-estimate boost (revision 23). Run Nov 11, 2026.

Same inputs as board_2026_11_06_close.py plus the new re_ret input. Prices stay on Nov 6 closes, the last full
pull, so the only change shown is RE. Nov 9-11 closes were not run (see roster.md for the names known to have
moved).

RE inputs (pulled Nov 11, 2026, about 8:15 pm CT) feed return_estimate(), framework C's method:
  base year  = the first fiscal year ending on or after May 11, 2027 (six months after the screen date).
  base, prior = stockanalysis forecast page, "EPS This Year" / "EPS Next Year" tiles and the first open table
               column (non-GAAP adjusted). The page shows analyst counts only for the first forecast year.
  out-years  = stockanalysis locks later columns. The third forecast year is backed out of the statistics
               page's "EPS Growth Forecast (3Y)": last reported fiscal-year EPS x (1 + growth)^3. Check: AVGO
               gives FY2028 $30.38, in line with the "FY28 EPS above $30" company comment already in roster.md.
               These are single-source figures with unknown coverage, so framework C uses one only when it is
               below the faded value. Every later year fades at 85% of the prior year's growth.
  dividend   = stockanalysis statistics page, Dividend Per Share, divided by the board price.
  exit cap   = median of the 20 quarterly forward P/Es already in INPUTS, where the board has them.

Page dates (stockanalysis serves snapshots; forecast page / statistics page):
  NVDA Nov 6 / Nov 6. FY2027 (Jan 31, 2027) $9.31, 54 analysts; base FY2028 $15.91; FY2026 actual $4.77;
       3Y growth 64.78% -> FY2029 $21.34. Dividend $1.00.
  AVGO Nov 6 / Nov 6. FY2026 (Oct 31, 2026) $11.67, 41 analysts; base FY2027 $19.47; FY2025 actual $6.82;
       3Y growth 64.53% -> FY2028 $30.38. Dividend $2.60.
  TER  Oct 30 / Oct 27. FY2026 $9.44, 15 analysts; base FY2027 $11.90; FY2025 $3.96; 56.61% -> FY2028 $15.21.
       Dividend $0.52.
  LRCX Oct 30 / Oct 27. Base FY2027 (Jun 30, 2027) $9.63, 30 analysts; FY2026 actual $5.82; FY2028 $12.15 (tile);
       35.37% -> FY2029 $14.44. Dividend $1.32.
  MTSI Oct 23 / Oct 26, both before the Nov 5 print. FY2026 $5.51, 15 analysts; base FY2027 $8.50; FY2025 $3.47;
       42.48% -> FY2028 $10.04. No dividend. Re-pull when the pages roll to the reported year.
  GOOGL Nov 6 / Nov 6. FY2026 $15.77, 47 analysts; base FY2027 $15.19, below 2026; FY2025
       $10.81; 19.04% -> FY2028 $18.24, above the faded value, so the path fades. On the $18.24 figure the
       estimate is 17.5%, also under 25%. Dividend $0.88.
  META Nov 6 / Nov 6. FY2026 $29.73, 54 analysts; base FY2027 $35.59; FY2025 $29.68; 12.54% -> FY2028 $42.31.
       Dividend $2.10.
  MPWR Oct 23 / Oct 26, both before the Oct 29 print. FY2026 $27.55, 15 analysts; base FY2027 $35.27; FY2025
       $17.77; 32.24% -> FY2028 $41.09. Dividend $8.00.
  SMTC Oct 23 / Oct 26. FY2027 (Jan 31, 2027) $3.65, 15 analysts; base FY2028 $6.67; FY2026 actual $1.71;
       79.50% -> FY2029 $9.89. No dividend.
  AMAT Oct 27 / Oct 27, before the Nov 12 print. FY2026 (Oct 31, 2026) $12.79, 34 analysts; base FY2027 $18.49;
       FY2025 $9.42; 36.00% -> FY2028 $23.70. Dividend $2.12. Lands 0.2 points under the 25% tier; re-pull
       after the print.
  FIX  Oct 30 / Oct 26. FY2026 $51.01, 9 analysts; base FY2027 $65.86; FY2025 $28.88; 41.55% -> FY2028 $81.91.
       Dividend $4.00.
  UBER Nov 6 / Oct 27 (statistics page predates the Nov 4 print). FY2026 $3.36, 36 analysts; base FY2027 $4.42;
       FY2025 $2.45; 30.91% -> FY2028 $5.50. A fully faded path gives 23.0%, also under 25%. No dividend.
  CDNS Oct 26 / Nov 6. FY2026 $8.41, 12 analysts; base FY2027 $9.73; FY2025 $7.14; 17.56% -> FY2028 $11.60.
  VRT  Oct 26 / Nov 6. FY2026 $6.73, 30 analysts; base FY2027 $9.19; FY2025 $4.20; 44.00% -> FY2028 $12.54,
       above the faded value, so the path fades. The Nov 1 snapshot's 40.93% would give 24.0% and no points.
       Dividend $0.25.
  ASML Nov 6 / Nov 6. EPS in EUR: FY2026 41.33, 35 analysts; base FY2027 56.22; FY2025 24.71; 45.58% -> FY2028
       76.24. Entry multiple: stockanalysis Forward PE 22.47 (USD, next 12 months). It is under the 35x cap and
       the board has no P/E history for ASML, so the estimate is EPS growth plus yield whatever the exchange
       rate. Dividend $7.91.
  GEV  Oct 30 / Nov 6. FY2026 $15.62, 32 analysts; base FY2027 $25.79; FY2025 $16.67; 30.82% -> FY2028 $37.32.
       Dividend $2.00.
  BE   Nov 6 / Nov 9. FY2026 $3.27, 25 analysts; base FY2027 $5.32; FY2025 $0.76; 121.31% -> FY2028 $8.24.
RE open: ANET (forecast page dated Oct 23, before its Nov 3 print, against a Nov 6 statistics page; 0.91 under the
line, so RE cannot put it on the board), and the names off the board on other tests: MU, CRDO, ALAB, RMBS, KLAC,
STRL, TSEM, STX, ETN, CIEN, VST, CEG, BKNG.
"""
from board_2026_11_06_close import INPUTS as NOV6, CLOSE, CC
from recovery_score import score, return_estimate, LINE


def third_year(last_actual, growth_3y):
    """Third forecast year's EPS from stockanalysis' 3-year EPS growth forecast (percent)."""
    return last_actual * (1 + growth_3y / 100) ** 3


# base EPS, prior-year EPS, out-year figures (single source, unknown coverage), dividend per share.
RE = {
    'NVDA': dict(base_eps=15.91, prior_eps=9.31, out_years=[third_year(4.77, 64.78)], dividend=1.00),
    'AVGO': dict(base_eps=19.47, prior_eps=11.67, out_years=[third_year(6.82, 64.53)], dividend=2.60),
    'TER': dict(base_eps=11.90, prior_eps=9.44, out_years=[third_year(3.96, 56.61)], dividend=0.52),
    'LRCX': dict(base_eps=9.63, prior_eps=5.82, out_years=[12.15, third_year(5.82, 35.37)], dividend=1.32),
    'MTSI': dict(base_eps=8.50, prior_eps=5.51, out_years=[third_year(3.47, 42.48)]),
    'GOOGL': dict(base_eps=15.19, prior_eps=15.77, out_years=[third_year(10.81, 19.04)], dividend=0.88),
    'META': dict(base_eps=35.59, prior_eps=29.73, out_years=[third_year(29.68, 12.54)], dividend=2.10),
    'MPWR': dict(base_eps=35.27, prior_eps=27.55, out_years=[third_year(17.77, 32.24)], dividend=8.00),
    'SMTC': dict(base_eps=6.67, prior_eps=3.65, out_years=[third_year(1.71, 79.50)]),
    'AMAT': dict(base_eps=18.49, prior_eps=12.79, out_years=[third_year(9.42, 36.00)], dividend=2.12),
    'FIX': dict(base_eps=65.86, prior_eps=51.01, out_years=[third_year(28.88, 41.55)], dividend=4.00),
    'UBER': dict(base_eps=4.42, prior_eps=3.36, out_years=[third_year(2.45, 30.91)]),
    'CDNS': dict(base_eps=9.73, prior_eps=8.41, out_years=[third_year(7.14, 17.56)]),
    'VRT': dict(base_eps=9.19, prior_eps=6.73, out_years=[third_year(4.20, 44.00)], dividend=0.25),
    'ASML': dict(base_eps=56.22, prior_eps=41.33, out_years=[third_year(24.71, 45.58)], dividend=7.91,
                 entry_pe=22.47),
    'GEV': dict(base_eps=25.79, prior_eps=15.62, out_years=[third_year(16.67, 30.82)], dividend=2.00),
    'BE': dict(base_eps=5.32, prior_eps=3.27, out_years=[third_year(0.76, 121.31)]),
}
ESTIMATES = {k: return_estimate(price=NOV6[k]["price"], fpe_hist=NOV6[k].get("fpe_hist"), **v)
             for k, v in RE.items()}
INPUTS = {k: dict(v, re_ret=ESTIMATES[k]["ret"] if k in ESTIMATES else None) for k, v in NOV6.items()}

if __name__ == "__main__":
    rows, off = [], []
    for k, v in INPUTS.items():
        r = score(**v)
        (rows if "final" in r else off).append((k, r))
    rows.sort(key=lambda x: -x[1]["_raw"])
    for i, (k, r) in enumerate(rows, 1):
        ex = (f" GP{r['gp']:+.2f}" if r['gp'] else "") + (" CG" if r['cg'] else "")
        ex += (f" CW{r['cw']:+.1f}" if r['cw'] else "") + (f" YT{r['yt']:+.1f}" if r['yt'] else "")
        ex += (f" CC{r['cc']:+.2f}" if r['cc'] else "") + ("" if k in CC else " CC open")
        e = ESTIMATES.get(k)
        est = (f"RE {e['ret']*100:5.1f}% {r['re']:+.2f} (EPS {e['cagr']*100:.1f}%/yr, {e['entry_pe']}x -> "
               f"{e['exit_pe']}x, {'/'.join(h for _, h in e['path'])})") if e else "RE open"
        print(f"{'ON ' if r['on_board'] else '   '}{i:>2} {k:5} {r['final']:5.2f} (pre-RE {r['final'] - r['re']:5.2f}) "
              f"${INPUTS[k]['price']:<8}{ex} | {est}")
    for k, r in off:
        print(f"OFF    {k:5} ${INPUTS[k]['price']:<8} {r['excluded']}")
