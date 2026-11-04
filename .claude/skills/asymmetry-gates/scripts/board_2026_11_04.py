"""Recovery board, Nov 4, 2026 (revision 17). Inputs as pulled; run to reprint the board.

Prices: one intraday snapshot, about 1:30 pm ET Nov 4 (UBER after its Q3 print, +7.4%),
except ETN $354 (user, same afternoon) and STRL $345.91 (Nov 2 close, latest available).
Fundamentals: stockanalysis statistics pages (Oct 27 to Nov 1 updates; CRDO from its
financials pages; TER pre-print with MarketBeat's post-print $412.64 consensus target).
rev90: Yahoo EPS trend, next-year EPS now vs 90 days ago (CIEN current year; UBER
-0.32% post-print per Yahoo Finance, Nov 4; None = no data). ntm_eps / fpe_hist:
stockanalysis quarterly ratios (GOOGL NTM EPS = Yahoo Q4'26 + 3/4 of 2027).
d, bear: per-name judgment inputs carried from revision 16 (UBER d = 25% after the Waymo unwind).
"""
from recovery_score import score, LINE

INPUTS = {
'AVGO': dict(price=327.88, high=481.57, target=530.14, eg=64.53, opm=48.81, ocf_margin=45.62, fcf_margin=44.22, roic=30.68, debt_ebitda=1.13, rev90=-0.0077, ntm_eps=16.743, fpe_hist=[24.7, 31.24, 32.17, 44.02, 39.55, 29.43, 34.84, 28.55, 26.24, 25.4, 26.1, 18.77, 20.72, 14.89, 14.5, 11.74, 13.57, 15.04, 16.91, 17.43], d=0.1, bear=0.25, pb=0.1, ix=0.1, po=0),
'GOOGL': dict(price=291.26, high=402.62, target=406.55, eg=19.09, opm=33.32, ocf_margin=38.11, fcf_margin=4.19, roic=23.79, debt_ebitda=0.79, rev90=0.0251, ntm_eps=14.68, fpe_hist=[25.62, 28.53, 25.08, 29.41, 24.5, 19.15, 17.23, 22.05, 20.65, 23.53, 22.22, 21.69, 21.14, 21.38, 20.39, 17.89, 17.77, 18.73, 23.98, 26.61], d=0.15, bear=0.2, pb=0.2, ix=0.2, po=0),
'VST': dict(price=119.06, high=217.92, target=208.77, eg=35.24, opm=19.79, ocf_margin=26.65, fcf_margin=11.76, roic=9.72, debt_ebitda=3.09, rev90=-0.0824, ntm_eps=None, fpe_hist=None, d=0.15, bear=0.25, pb=0.1, ix=0, po=-0.2),
'CEG': dict(price=247.01, high=403.95, target=339.25, eg=21.0, opm=15.05, ocf_margin=13.46, fcf_margin=0.94, roic=7.43, debt_ebitda=3.04, rev90=None, ntm_eps=None, fpe_hist=None, d=0.15, bear=0.25, pb=0, ix=0, po=0),
'CRDO': dict(price=135.34, high=302.52, target=284.05, eg=82.35, opm=31.74, ocf_margin=31.45, fcf_margin=27.57, roic=38.21, debt_ebitda=0.0, rev90=0.0875, ntm_eps=None, fpe_hist=None, d=0.15, bear=0.4, pb=0, ix=0, po=0),
'GEV': dict(price=822.05, high=1159, target=1190.82, eg=30.48, opm=8.22, ocf_margin=43.64, fcf_margin=38.87, roic=50.73, debt_ebitda=0.7, rev90=0.0181, ntm_eps=None, fpe_hist=None, d=0.15, bear=0.3, pb=0, ix=0, po=-0.1),
'RMBS': dict(price=82.73, high=170.66, target=140.14, eg=25.66, opm=36.74, ocf_margin=43.56, fcf_margin=39.31, roic=37.18, debt_ebitda=0.06, rev90=None, ntm_eps=3.395, fpe_hist=[31.45, 41.76, 29.14, 32.37, 39.11, 25.27, 21.24, 22.57, 18.48, 27.75, 30.39, 34.41, 30.95, 35.61, 29.05, 20.41, 15.57, 13.57, 21.77, 20.25], d=0.3, bear=0.25, pb=0, ix=0, po=0),
'KLAC': dict(price=150.21, high=301.71, target=232.38, eg=29.44, opm=41.69, ocf_margin=30.49, fcf_margin=27.76, roic=66.75, debt_ebitda=1.01, rev90=0.0732, ntm_eps=6.188, fpe_hist=[35.74, 63.32, 35.01, 32.72, 30.73, 27.35, 21.49, 20.69, 26.01, 30.5, 28.87, 24.39, 20.28, 24.99, 21.98, 17.6, 12.38, 13.43, 16.26, 19.7], d=0.15, bear=0.35, pb=0, ix=0, po=0),
'AMAT': dict(price=366.81, high=732.45, target=627.83, eg=36.0, opm=31.22, ocf_margin=27.24, fcf_margin=18.22, roic=35.64, debt_ebitda=0.72, rev90=0.1039, ntm_eps=17.635, fpe_hist=[35.9, 34.46, 33.48, 25.46, 19.32, 16.31, 19.89, 20.07, 23.51, 24.51, 21.59, 17.34, 23.61, 17.72, 16.75, 13.19, 13.37, 12.78, 16.24, 17.07], d=0.15, bear=0.35, pb=0, ix=0, po=0),
'CDNS': dict(price=328.98, high=416.39, target=411.76, eg=17.56, opm=29.94, ocf_margin=32.14, fcf_margin=28.71, roic=17.09, debt_ebitda=1.2, rev90=0.0181, ntm_eps=8.589, fpe_hist=[46.11, 35.09, 40.58, 47.52, 44.9, 37.79, 44.38, 40.52, 48.14, 52.42, 48.22, 43.5, 45.63, 42.17, 37.24, 40.23, 39.09, 44.03, 54.88, 48.11], d=0.15, bear=0.2, pb=0, ix=0, po=0),
'MPWR': dict(price=1269.58, high=1690, target=1799.8, eg=32.24, opm=28.72, ocf_margin=25.15, fcf_margin=17.91, roic=31.71, debt_ebitda=0.02, rev90=0.153, ntm_eps=30.495, fpe_hist=[53.98, 50.81, 45.68, 49.54, 42.45, 34.41, 37.05, 57.91, 58.65, 52.92, 53.24, 38.82, 45.22, 37.75, 28.1, 26.83, 31.38, 50.16, 60.78, 64.17], d=0.15, bear=0.3, pb=0, ix=0, po=0),
'LRCX': dict(price=222.3, high=432.72, target=364.03, eg=35.37, opm=36.95, ocf_margin=29.01, fcf_margin=25.03, roic=79.14, debt_ebitda=0.36, rev90=0.1959, ntm_eps=10.275, fpe_hist=[33.29, 50.2, 34.36, 36.1, 28.61, 23.7, 18.96, 20.29, 23.1, 31.65, 31.13, 27.5, 22.94, 25.81, 20.55, 13.75, 10.29, 12.42, 15.58, 19.75], d=0.15, bear=0.35, pb=0, ix=0, po=0),
'FIX': dict(price=1079.17, high=2067, target=1916.88, eg=41.55, opm=16.78, ocf_margin=24.0, fcf_margin=19.46, roic=103.2, debt_ebitda=0.15, rev90=0.0857, ntm_eps=63.539, fpe_hist=[31.09, 44.87, 37.51, 31.59, 33.64, 27.42, 17.61, 25.84, 26.91, 24.39, 28.71, 22.34, 21.18, 22.98, 21.48, 19.18, 17.95, 17.31, 18.38, 21.51], d=0.15, bear=0.35, pb=0, ix=0, po=-0.2),
'META': dict(price=634.56, high=790, target=848.38, eg=12.54, opm=37.78, ocf_margin=55.08, fcf_margin=11.86, roic=29.62, debt_ebitda=0.95, rev90=-0.0322, ntm_eps=32.939, fpe_hist=[21.81, 17.16, 18.87, 22.59, 25.72, 28.95, 22.74, 23.96, 25.31, 24.73, 24.3, 20.78, 18.71, 22.41, 21.97, 16.39, 15.08, 13.63, 17.93, 24.69], d=0.24, bear=0.25, pb=0, ix=0.2, po=-0.1),
'TER': dict(price=251.13, high=478.23, target=412.64, eg=56.61, opm=30.74, ocf_margin=23.77, fcf_margin=17.94, roic=38.24, debt_ebitda=0.06, rev90=0.143, ntm_eps=10.529, fpe_hist=[41.56, 63.19, 47.16, 38.03, 35.15, 26.98, 24.89, 32.34, 36.06, 42.23, 38.64, 32.71, 28.78, 36.36, 33.68, 25.2, 18.26, 16.49, 24.0, 26.09], d=0.2, bear=0.35, pb=0, ix=0, po=0),
'MTSI': dict(price=222.06, high=409.68, target=390.33, eg=42.48, opm=18.19, ocf_margin=23.38, fcf_margin=17.59, roic=14.5, debt_ebitda=1.43, rev90=None, ntm_eps=8.251, fpe_hist=[51.91, 50.26, 41.48, 32.49, 37.27, 24.73, 39.73, 35.74, 38.54, 34.98, 34.53, 32.48, 28.78, 23.34, 20.51, 17.04, 15.12, 20.69, 29.77, 27.42], d=0.2, bear=0.35, pb=0, ix=0, po=0),
'ASML': dict(price=1500.87, high=1976, target=2141.09, eg=45.21, opm=38.55, ocf_margin=56.58, fcf_margin=52.69, roic=92.13, debt_ebitda=0.12, rev90=0.1102, ntm_eps=None, fpe_hist=None, d=0.15, bear=0.3, pb=0, ix=0, po=0),
'UBER': dict(price=71.54, high=100.1, target=100.86, eg=30.91, opm=12.13, ocf_margin=18.87, fcf_margin=18.32, roic=19.18, debt_ebitda=1.87, rev90=-0.0032, ntm_eps=None, fpe_hist=None, d=0.25, bear=0.25, pb=0.2, ix=0, po=0),
'VRT': dict(price=204.12, high=376.23, target=333.0, eg=40.93, opm=19.96, ocf_margin=29.18, fcf_margin=25.52, roic=37.58, debt_ebitda=1.19, rev90=0.042, ntm_eps=7.547, fpe_hist=[49.07, 40.78, 32.39, 35.14, 34.0, 20.09, 34.24, 34.33, 34.55, 35.79, 23.29, 21.45, 19.07, 12.11, 13.29, 9.2, 8.77, 21.19, 20.82, 24.28], d=0.15, bear=0.4, pb=0, ix=0, po=-0.1),
'BE': dict(price=197.16, high=345.85, target=284.77, eg=121.27, opm=14.33, ocf_margin=18.04, fcf_margin=11.4, roic=27.24, debt_ebitda=4.38, rev90=0.1333, ntm_eps=None, fpe_hist=None, d=0.25, bear=0.45, pb=0.1, ix=0, po=0),
'CIEN': dict(price=300.3, high=637.51, target=219.29, eg=None, opm=6.52, ocf_margin=16.9, fcf_margin=13.95, roic=4.41, debt_ebitda=3.48, rev90=0.0963, ntm_eps=10.389, fpe_hist=[48.34, 80.95, 47.15, 50.46, 35.03, 28.89, 36.12, 25.69, 22.29, 20.82, 17.72, 14.15, 15.71, 15.88, 19.52, 29.51, 22.64, 17.28, 20.78, 17.88], d=0.25, bear=0.45, pb=0, ix=0, po=0),
'ETN': dict(price=354.0, high=459.96, target=485.47, eg=16.3, opm=18.17, ocf_margin=16.48, fcf_margin=13.09, roic=10.61, debt_ebitda=3.07, rev90=0.0298, ntm_eps=15.147, fpe_hist=[30.29, 26.79, 23.84, 28.81, 28.7, 22.55, 28.24, 29.02, 29.07, 30.49, 24.54, 22.83, 23.1, 20.7, 19.46, 16.77, 16.35, 20.12, 23.9, 21.16], d=0.15, bear=0.3, pb=0, ix=0, po=-0.1),
'STRL': dict(price=345.91, high=993.74, target=836.71, eg=41.98, opm=18.13, ocf_margin=17.38, fcf_margin=14.01, roic=41.69, debt_ebitda=0.43, rev90=None, ntm_eps=26.265, fpe_hist=[21.94, 43.02, 30.12, 26.2, 34.17, 26.81, 14.09, 27.37, 25.27, 19.73, 22.15, 19.14, 17.03, 15.14, 11.03, 9.89, 6.77, 7.33, 9.57, 12.06], d=0.2, bear=0.45, pb=0, ix=0, po=-0.2),
# Photonics / connectivity sweep, added 4:20 pm CT: Nov 4 closes (ALAB, TSEM, ANET as quoted by the
# user's council; SMTC $110.96, StockStory had $111.19 that afternoon). Highs: Yahoo 52-week intraday highs,
# except SMTC's $197.20 (StockStory). TSEM: +19.5% 90-day estimates per Investing.com (Nov 2), target =
# MarketBeat consensus $311, NTM EPS ~6.0 (26x forward at the Nov 2 close). ANET: stockanalysis lists only a
# 5-year EPS forecast (17.23%) and a $112.98 target that sits below the price, so the target is Yahoo's $243.59.
# ALAB: no usable P/E history (IPO Mar 2024), target only.
'ALAB': dict(price=223.27, high=499.48, target=382.68, eg=63.64, opm=22.75, ocf_margin=27.98, fcf_margin=23.02, roic=62.97, debt_ebitda=0.15, rev90=0.4128, ntm_eps=None, fpe_hist=None, d=0.15, bear=0.40, pb=0, ix=0, po=0),
'SMTC': dict(price=110.96, high=197.20, target=217.07, eg=79.5, opm=12.03, ocf_margin=18.29, fcf_margin=16.45, roic=14.15, debt_ebitda=2.81, rev90=None, ntm_eps=5.409, fpe_hist=[42.28, 49.56, 40.53, 37.75, 30.89, 17.96, 46.27, 40.67, 37.98, 57.03, 69.92, 23.42, 43.78, 38.29, 16.13, 11.17, 18.21, 17.75, 22.4, 30.33], d=0.15, bear=0.40, pb=0, ix=0, po=0),
'TSEM': dict(price=148.80, high=319.94, target=311.0, eg=64.07, opm=16.16, ocf_margin=50.64, fcf_margin=17.58, roic=14.84, debt_ebitda=0.23, rev90=0.195, ntm_eps=6.0, fpe_hist=[68.83, 59.3, 43.6, 29.66, 19.36, 17.19, 24.42, 20.98, 20.94, 17.74, 15.0, 12.29, 17.85, 19.11, 18.08, 18.21, 20.1, 21.58, 19.58, 19.17], d=0.15, bear=0.40, pb=0, ix=0, po=0),
'ANET': dict(price=178.48, high=217.41, target=243.59, eg=17.23, opm=42.05, ocf_margin=53.0, fcf_margin=52.49, roic=21.23, debt_ebitda=0.02, rev90=0.1704, ntm_eps=4.62, fpe_hist=[45.02, 34.69, 40.86, 48.79, 39.4, 31.06, 46.87, 44.61, 43.76, 38.73, 33.56, 28.88, 27.32, 28.89, 23.53, 26.65, 24.65, 38.25, 44.18, 30.99], d=0.15, bear=0.30, pb=0, ix=0, po=0),
}

if __name__ == "__main__":
    rows, off = [], []
    for k, v in INPUTS.items():
        r = score(**v)
        (rows if "final" in r else off).append((k, r))
    rows.sort(key=lambda x: -x[1]["_raw"])
    print(f"line {LINE}")
    for i, (k, r) in enumerate(rows, 1):
        tag = "ON " if r["on_board"] else "   "
        print(f"{tag}{i:>2} {k:5} {r['final']:5.2f}  Q {r['quality']:4.1f}  12m {r['ret_12m']*100:6.1f}%  yrs {r['years']:4.2f}")
    for k, r in off:
        print(f"OFF    {k:5} {r['excluded']}")
