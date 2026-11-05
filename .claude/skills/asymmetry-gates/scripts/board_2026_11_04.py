"""Recovery board, Nov 4, 2026 (revision 17; GD gate revision 18; GP gate-fail penalty revision 19, CG cycle
guard revision 20 and CW / YT penalties revision 21, Nov 5).
Inputs as pulled; run to reprint the board.

Prices: one intraday snapshot, about 1:30 pm ET Nov 4 (UBER after its Q3 print, +7.4%),
except ETN $354 (user, same afternoon) and STRL $345.91 (Nov 2 close, latest available).
Fundamentals: stockanalysis statistics pages (Oct 27 to Nov 1 updates; CRDO from its
financials pages; TER pre-print with MarketBeat's post-print $412.64 consensus target).
net_cash: stockanalysis Net Cash ($B; CRDO from its Aug 1 balance sheet; SMTC not pulled).
rev90: Yahoo EPS trend, next-year EPS now vs 90 days ago (CIEN current year; UBER
-0.32% post-print per Yahoo Finance, Nov 4; None = no data). ntm_eps / fpe_hist:
stockanalysis quarterly ratios (GOOGL NTM EPS = Yahoo Q4'26 + 3/4 of 2027).
guide_below (GD gate, revision 18, 3% band from 6:42 pm CT, checked Nov 4): BKNG out (bookings and
room nights ~4 points of growth below the Street per Cantor, adjusted revenue +0-2%, EBITDA flat).
Inside the band and kept: AVGO Q4 revenue $34.8B vs $35.0B (-0.6%, Sep 2); UBER Q4 EPS $0.95-0.99 vs
~$1.00 (-3.0% on Yahoo Finance's figure; Reuters cited $1.06), bookings in line, EBITDA above (Nov 4). All others guided at or above consensus or give no numeric guidance
(GOOGL, FIX).
d, bear: per-name judgment inputs carried from revision 16 (UBER d = 25% after the Waymo unwind).
gp (revision 19, quick gate sweep Nov 5, 2026; details in references/roster.md):
  CRDO -0.5   A7 (D route): Q2 2026 three officers sold outside plans (Cheng, Laufman, Brennan); clears early Jun 2027.
  ALAB -0.5   A7 (D route): 12-month net insider selling 2.03% of 173.5M shares (officers 1.54%); under 1.5% ~late May 2027.
  FIX  -0.5   A7: Q1 2026 George (Feb 23), Reed (Feb 24, Mar 3), Lane (Feb 25) sold with no plan footnote; boxes unchecked where shown.
  AMAT -0.5   A7: Q2 2026 Dickerson (Jun 15-16, 29-30), Raja (Jun 18), Deane (Jun 15) sold with the 10b5-1 box unchecked; clears Jul 2027.
  GOOGL -0.5  #19(b): Q3 EPS $2.12 vs $2.94 consensus (-28%; -9% ex the $0.55 equity-investment loss); blackout to the next print.
  STX  -0.25  A7 (D route; A1 out on 2026 exchangeable-note share settlements): Q3 2026 Teh non-plan, Romano/Morris sell-to-cover
              without the issuer footnote (paperwork-driven, minor); clears Sep 2027.
  MTSI -0.25  A7: net selling 1.87% incl. 10% owner Ocampo (0.28% without); under 1.5% ~Dec 10, 2026 (moderate stepped down).
  AVGO -0.25  A7: Q4 2025 Tan (Dec 18; not under a plan per MarketBeat), Brazeal (Dec 26) and Spears (Dec 31) sold with no plan
              footnote; moderate, stepped down because it clears Dec 31, 2026. March/June sales are documented sell-to-cover.
  MPWR -0.25  A7: Q1 2026 Feb 6 RSU-release sales by Hsing, Xiao, Sciammas and Blegen at one price carry only a tax label
              ("to cover taxes upon the release of restricted stock units"), which A7 doesn't accept as issuer-required; minor.
              Q2 2026 could make it -0.5: Hsing (May 18) and Tseng (May 22) show no plan; Xiao's May 6 filing not found.
  No points: MU (G route, A1 out at +1.61% diluted WASO; three-officer cluster is a G4 watch flag, 5-9% of holdings each).
  Checked clear (Nov 5, 9:37 am CT pass): ANET (Ullal plan Nov 14, 2025; Duda plan Mar 11, 2026), TSEM (only the CEO sells,
  on a pre-arranged order; Form 4s filed), ASML (AFM: CEO and CFO sales run through discretionary management mandates;
  other board members not pulled), SMTC (D route; Oct 2025 convert exchanges rolled out of the 12-month window Oct 14),
  #19 on the Nov 3-5 prints (ALAB, ANET, UBER and MTSI all beat).
ye_close (YT, revision 21): Dec 31, 2025 closes. digrin month-end prices (unadjusted): TER, CRDO, ALAB, FIX, SMTC, MPWR,
  TSEM, MTSI, GEV, VRT, ANET, UBER (TER matches bullfincher's implied base; TSEM matches tsem-research's verified
  year-end close). Live price / (1 + YTD) on financhle, Nov 5: NVDA, AVGO, LRCX, ASML, AMAT, GOOGL, META, MU
  (financhle implies MPWR 921.82 vs digrin's 906.36; same tier). YTD is measured at the board price, not today's.
cycle on non-triggered names (revision 21 CW): the ratios-page ROIC readings tested for CG. FIX, VRT and GEV
  (booking-cycle names, rescore=False): stockanalysis annual ROIC, latest reading vs the average of all shown
  readings (latest plus up to five fiscal years). FIX 103.20 vs 44.02 (2.3x); VRT 43.82 vs 20.20 (2.2x;
  vcpscanner's quarterly series gives 2.8x); GEV 50.73 (FY25, no TTM shown) vs 11.86 (4.3x; FY22 was -16.30).
  NVDA (added Nov 5): clear on A1 (shares -1.04% YoY), A7 (net selling ~0.03%; at most two officers in any quarter),
  #19 (Q2 FY27 beat), GD (Q3 guide $108B vs ~$104B) and legal (China SAMR finding is preliminary, no remedy order).
"""
from recovery_score import score, LINE

INPUTS = {
'AVGO': dict(price=327.88, high=481.57, target=530.14, eg=64.53, opm=48.81, ocf_margin=45.62, fcf_margin=44.22, roic=30.68, debt_ebitda=1.13, rev90=-0.0077, ntm_eps=16.743, fpe_hist=[24.7, 31.24, 32.17, 44.02, 39.55, 29.43, 34.84, 28.55, 26.24, 25.4, 26.1, 18.77, 20.72, 14.89, 14.5, 11.74, 13.57, 15.04, 16.91, 17.43], d=0.1, bear=0.25, pb=0.1, ix=0.1, po=0, net_cash=-35.44, gp=-0.25, ye_close=346.09),
'GOOGL': dict(price=291.26, high=402.62, target=406.55, eg=19.09, opm=33.32, ocf_margin=38.11, fcf_margin=4.19, roic=23.79, debt_ebitda=0.79, rev90=0.0251, ntm_eps=14.68, fpe_hist=[25.62, 28.53, 25.08, 29.41, 24.5, 19.15, 17.23, 22.05, 20.65, 23.53, 22.22, 21.69, 21.14, 21.38, 20.39, 17.89, 17.77, 18.73, 23.98, 26.61], d=0.15, bear=0.2, pb=0.2, ix=0.2, po=0, net_cash=114.77, gp=-0.5, ye_close=313.0),
'VST': dict(price=119.06, high=217.92, target=208.77, eg=35.24, opm=19.79, ocf_margin=26.65, fcf_margin=11.76, roic=9.72, debt_ebitda=3.09, rev90=-0.0824, ntm_eps=None, fpe_hist=None, d=0.15, bear=0.25, pb=0.1, ix=0, po=-0.2, net_cash=-20.07),
'CEG': dict(price=247.01, high=403.95, target=339.25, eg=21.0, opm=15.05, ocf_margin=13.46, fcf_margin=0.94, roic=7.43, debt_ebitda=3.04, rev90=None, ntm_eps=None, fpe_hist=None, d=0.15, bear=0.25, pb=0, ix=0, po=0, net_cash=-24.0),
'CRDO': dict(price=135.34, high=302.52, target=284.05, eg=82.35, opm=31.74, ocf_margin=31.45, fcf_margin=27.57, roic=38.21, debt_ebitda=0.0, rev90=0.0875, ntm_eps=None, fpe_hist=None, d=0.15, bear=0.4, pb=0, ix=0, po=0, net_cash=0.738, gp=-0.5, ye_close=143.89),
'GEV': dict(price=822.05, high=1159, target=1190.82, eg=30.48, opm=8.22, ocf_margin=43.64, fcf_margin=38.87, roic=50.73, debt_ebitda=0.7, rev90=0.0181, ntm_eps=None, fpe_hist=None, d=0.15, bear=0.3, pb=0, ix=0, po=-0.1, net_cash=12.62, cycle=dict(roic_now=50.73, roic_avg=11.86, rescore=False), ye_close=653.57),
'RMBS': dict(price=82.73, high=170.66, target=140.14, eg=25.66, opm=36.74, ocf_margin=43.56, fcf_margin=39.31, roic=37.18, debt_ebitda=0.06, rev90=None, ntm_eps=3.395, fpe_hist=[31.45, 41.76, 29.14, 32.37, 39.11, 25.27, 21.24, 22.57, 18.48, 27.75, 30.39, 34.41, 30.95, 35.61, 29.05, 20.41, 15.57, 13.57, 21.77, 20.25], d=0.3, bear=0.25, pb=0, ix=0, po=0, net_cash=0.757),
'KLAC': dict(price=150.21, high=301.71, target=232.38, eg=29.44, opm=41.69, ocf_margin=30.49, fcf_margin=27.76, roic=66.75, debt_ebitda=1.01, rev90=0.0732, ntm_eps=6.188, fpe_hist=[35.74, 63.32, 35.01, 32.72, 30.73, 27.35, 21.49, 20.69, 26.01, 30.5, 28.87, 24.39, 20.28, 24.99, 21.98, 17.6, 12.38, 13.43, 16.26, 19.7], d=0.15, bear=0.35, pb=0, ix=0, po=0, net_cash=-1.25),
'AMAT': dict(price=366.81, high=732.45, target=627.83, eg=36.0, opm=31.22, ocf_margin=27.24, fcf_margin=18.22, roic=35.64, debt_ebitda=0.72, rev90=0.1039, ntm_eps=17.635, fpe_hist=[35.9, 34.46, 33.48, 25.46, 19.32, 16.31, 19.89, 20.07, 23.51, 24.51, 21.59, 17.34, 23.61, 17.72, 16.75, 13.19, 13.37, 12.78, 16.24, 17.07], d=0.15, bear=0.35, pb=0, ix=0, po=0, net_cash=1.89, gp=-0.5, cycle=dict(roic_now=11.50, roic_avg=10.91), ye_close=256.98),
'CDNS': dict(price=328.98, high=416.39, target=411.76, eg=17.56, opm=29.94, ocf_margin=32.14, fcf_margin=28.71, roic=17.09, debt_ebitda=1.2, rev90=0.0181, ntm_eps=8.589, fpe_hist=[46.11, 35.09, 40.58, 47.52, 44.9, 37.79, 44.38, 40.52, 48.14, 52.42, 48.22, 43.5, 45.63, 42.17, 37.24, 40.23, 39.09, 44.03, 54.88, 48.11], d=0.15, bear=0.2, pb=0, ix=0, po=0, net_cash=-1.27),
'MPWR': dict(price=1269.58, high=1690, target=1799.8, eg=32.24, opm=28.72, ocf_margin=25.15, fcf_margin=17.91, roic=31.71, debt_ebitda=0.02, rev90=0.153, ntm_eps=30.495, fpe_hist=[53.98, 50.81, 45.68, 49.54, 42.45, 34.41, 37.05, 57.91, 58.65, 52.92, 53.24, 38.82, 45.22, 37.75, 28.1, 26.83, 31.38, 50.16, 60.78, 64.17], d=0.15, bear=0.3, pb=0, ix=0, po=0, net_cash=1.39, gp=-0.25, ye_close=906.36),
'LRCX': dict(price=222.3, high=432.72, target=364.03, eg=35.37, opm=36.95, ocf_margin=29.01, fcf_margin=25.03, roic=79.14, debt_ebitda=0.36, rev90=0.1959, ntm_eps=10.275, fpe_hist=[33.29, 50.2, 34.36, 36.1, 28.61, 23.7, 18.96, 20.29, 23.1, 31.65, 31.13, 27.5, 22.94, 25.81, 20.55, 13.75, 10.29, 12.42, 15.58, 19.75], d=0.15, bear=0.35, pb=0, ix=0, po=0, net_cash=3.7, cycle=dict(roic_now=25.73, roic_avg=16.62), ye_close=171.17),
'FIX': dict(price=1079.17, high=2067, target=1916.88, eg=41.55, opm=16.78, ocf_margin=24.0, fcf_margin=19.46, roic=103.2, debt_ebitda=0.15, rev90=0.0857, ntm_eps=63.539, fpe_hist=[31.09, 44.87, 37.51, 31.59, 33.64, 27.42, 17.61, 25.84, 26.91, 24.39, 28.71, 22.34, 21.18, 22.98, 21.48, 19.18, 17.95, 17.31, 18.38, 21.51], d=0.15, bear=0.35, pb=0, ix=0, po=-0.2, net_cash=1.85, gp=-0.5, cycle=dict(roic_now=103.20, roic_avg=44.02, rescore=False), ye_close=933.29),
'META': dict(price=634.56, high=790, target=848.38, eg=12.54, opm=37.78, ocf_margin=55.08, fcf_margin=11.86, roic=29.62, debt_ebitda=0.95, rev90=-0.0322, ntm_eps=32.939, fpe_hist=[21.81, 17.16, 18.87, 22.59, 25.72, 28.95, 22.74, 23.96, 25.31, 24.73, 24.3, 20.78, 18.71, 22.41, 21.97, 16.39, 15.08, 13.63, 17.93, 24.69], d=0.24, bear=0.25, pb=0, ix=0.2, po=-0.1, net_cash=-32.39, ye_close=660.07),
'TER': dict(price=251.13, high=478.23, target=412.64, eg=56.61, opm=30.74, ocf_margin=23.77, fcf_margin=17.94, roic=38.24, debt_ebitda=0.06, rev90=0.143, ntm_eps=10.529, fpe_hist=[41.56, 63.19, 47.16, 38.03, 35.15, 26.98, 24.89, 32.34, 36.06, 42.23, 38.64, 32.71, 28.78, 36.36, 33.68, 25.2, 18.26, 16.49, 24.0, 26.09], d=0.2, bear=0.35, pb=0, ix=0, po=0, net_cash=0.417, cycle=dict(roic_now=12.07, roic_avg=8.54), ye_close=193.56),
'MTSI': dict(price=222.06, high=409.68, target=390.33, eg=42.48, opm=18.19, ocf_margin=23.38, fcf_margin=17.59, roic=14.5, debt_ebitda=1.43, rev90=None, ntm_eps=8.251, fpe_hist=[51.91, 50.26, 41.48, 32.49, 37.27, 24.73, 39.73, 35.74, 38.54, 34.98, 34.53, 32.48, 28.78, 23.34, 20.51, 17.04, 15.12, 20.69, 29.77, 27.42], d=0.2, bear=0.35, pb=0, ix=0, po=0, net_cash=0.249, gp=-0.25, ye_close=171.28),
'ASML': dict(price=1500.87, high=1976, target=2141.09, eg=45.21, opm=38.55, ocf_margin=56.58, fcf_margin=52.69, roic=92.13, debt_ebitda=0.12, rev90=0.1102, ntm_eps=None, fpe_hist=None, d=0.15, bear=0.3, pb=0, ix=0, po=0, net_cash=12.28, cycle=dict(roic_now=31.68, roic_avg=18.27), ye_close=1069.85),
'UBER': dict(price=71.54, high=100.1, target=100.86, eg=30.91, opm=12.13, ocf_margin=18.87, fcf_margin=18.32, roic=19.18, debt_ebitda=1.87, rev90=-0.0032, ntm_eps=None, fpe_hist=None, d=0.25, bear=0.25, pb=0.2, ix=0, po=0, net_cash=-4.74, ye_close=81.71),
'VRT': dict(price=204.12, high=376.23, target=333.0, eg=40.93, opm=19.96, ocf_margin=29.18, fcf_margin=25.52, roic=37.58, debt_ebitda=1.19, rev90=0.042, ntm_eps=7.547, fpe_hist=[49.07, 40.78, 32.39, 35.14, 34.0, 20.09, 34.24, 34.33, 34.55, 35.79, 23.29, 21.45, 19.07, 12.11, 13.29, 9.2, 8.77, 21.19, 20.82, 24.28], d=0.15, bear=0.4, pb=0, ix=0, po=-0.1, net_cash=-0.2276, cycle=dict(roic_now=43.82, roic_avg=20.20, rescore=False), ye_close=162.01),
'BE': dict(price=197.16, high=345.85, target=284.77, eg=121.27, opm=14.33, ocf_margin=18.04, fcf_margin=11.4, roic=27.24, debt_ebitda=4.38, rev90=0.1333, ntm_eps=None, fpe_hist=None, d=0.25, bear=0.45, pb=0.1, ix=0, po=0, net_cash=-0.2999),
'CIEN': dict(price=300.3, high=637.51, target=219.29, eg=None, opm=6.52, ocf_margin=16.9, fcf_margin=13.95, roic=4.41, debt_ebitda=3.48, rev90=0.0963, ntm_eps=10.389, fpe_hist=[48.34, 80.95, 47.15, 50.46, 35.03, 28.89, 36.12, 25.69, 22.29, 20.82, 17.72, 14.15, 15.71, 15.88, 19.52, 29.51, 22.64, 17.28, 20.78, 17.88], d=0.25, bear=0.45, pb=0, ix=0, po=0, net_cash=-0.262),
'ETN': dict(price=354.0, high=459.96, target=485.47, eg=16.3, opm=18.17, ocf_margin=16.48, fcf_margin=13.09, roic=10.61, debt_ebitda=3.07, rev90=0.0298, ntm_eps=15.147, fpe_hist=[30.29, 26.79, 23.84, 28.81, 28.7, 22.55, 28.24, 29.02, 29.07, 30.49, 24.54, 22.83, 23.1, 20.7, 19.46, 16.77, 16.35, 20.12, 23.9, 21.16], d=0.15, bear=0.3, pb=0, ix=0, po=-0.1, net_cash=-20.63),
'STRL': dict(price=345.91, high=993.74, target=836.71, eg=41.98, opm=18.13, ocf_margin=17.38, fcf_margin=14.01, roic=41.69, debt_ebitda=0.43, rev90=None, ntm_eps=26.265, fpe_hist=[21.94, 43.02, 30.12, 26.2, 34.17, 26.81, 14.09, 27.37, 25.27, 19.73, 22.15, 19.14, 17.03, 15.14, 11.03, 9.89, 6.77, 7.33, 9.57, 12.06], d=0.2, bear=0.45, pb=0, ix=0, po=-0.2, net_cash=0.128),
# Photonics / connectivity sweep, added 4:20 pm CT: Nov 4 closes (ALAB, TSEM, ANET as quoted by the
# user's council; SMTC $110.96, StockStory had $111.19 that afternoon). Highs: Yahoo 52-week intraday highs,
# except SMTC's $197.20 (StockStory). TSEM: +19.5% 90-day estimates per Investing.com (Nov 2), target =
# MarketBeat consensus $311, NTM EPS ~6.0 (26x forward at the Nov 2 close). ANET: stockanalysis lists only a
# 5-year EPS forecast (17.23%) and a $112.98 target that sits below the price, so the target is Yahoo's $243.59.
# ALAB: no usable P/E history (IPO Mar 2024), target only.
'ALAB': dict(price=223.27, high=499.48, target=382.68, eg=63.64, opm=22.75, ocf_margin=27.98, fcf_margin=23.02, roic=62.97, debt_ebitda=0.15, rev90=0.4128, ntm_eps=None, fpe_hist=None, d=0.15, bear=0.40, pb=0, ix=0, po=0, net_cash=1.21, gp=-0.5, ye_close=166.36),
'SMTC': dict(price=110.96, high=197.20, target=217.07, eg=79.5, opm=12.03, ocf_margin=18.29, fcf_margin=16.45, roic=14.15, debt_ebitda=2.81, rev90=None, ntm_eps=5.409, fpe_hist=[42.28, 49.56, 40.53, 37.75, 30.89, 17.96, 46.27, 40.67, 37.98, 57.03, 69.92, 23.42, 43.78, 38.29, 16.13, 11.17, 18.21, 17.75, 22.4, 30.33], d=0.15, bear=0.40, pb=0, ix=0, po=0, ye_close=73.69),
'TSEM': dict(price=148.80, high=319.94, target=311.0, eg=64.07, opm=16.16, ocf_margin=50.64, fcf_margin=17.58, roic=14.84, debt_ebitda=0.23, rev90=0.195, ntm_eps=6.0, fpe_hist=[68.83, 59.3, 43.6, 29.66, 19.36, 17.19, 24.42, 20.98, 20.94, 17.74, 15.0, 12.29, 17.85, 19.11, 18.08, 18.21, 20.1, 21.58, 19.58, 19.17], d=0.15, bear=0.40, pb=0, ix=0, po=0, net_cash=1.34, cycle=dict(roic_now=4.58, roic_avg=3.78), ye_close=117.42),
'ANET': dict(price=178.48, high=217.41, target=243.59, eg=17.23, opm=42.05, ocf_margin=53.0, fcf_margin=52.49, roic=21.23, debt_ebitda=0.02, rev90=0.1704, ntm_eps=4.62, fpe_hist=[45.02, 34.69, 40.86, 48.79, 39.4, 31.06, 46.87, 44.61, 43.76, 38.73, 33.56, 28.88, 27.32, 28.89, 23.53, 26.65, 24.65, 38.25, 44.18, 30.99], d=0.15, bear=0.30, pb=0, ix=0, po=0, net_cash=8.24, ye_close=131.03),
# BKNG added 4:48 pm CT (user: "add BKNG (5.73) to the board—leave DASH off"): Nov 4 close $170.97 per the
# user's council (StockStory had $172.45 that afternoon, +12.5% after Q3). High: $229.07, the Jun 30, 2025
# quarter-end close (split-adjusted; the 2025 closing peak is a little higher, ~1.9-2.0 years either way).
# rev90 predates the weak Q4 guide (adj. revenue +0-2%, EBITDA flat; $900M FTC revenue hit): a 3-5% estimate
# cut would score it 5.25-5.40.
'BKNG': dict(price=170.97, high=229.07, target=232.71, eg=16.60, opm=34.85, ocf_margin=34.92, fcf_margin=33.78, roic=92.45, debt_ebitda=1.96, rev90=0.0049, ntm_eps=11.127, fpe_hist=[14.64, 16.64, 15.73, 20.8, 22.64, 26.47, 21.82, 24.45, 22.68, 22.35, 20.73, 20.64, 20.17, 19.4, 20.36, 16.86, 15.11, 16.32, 26.41, 26.57], d=0.15, bear=0.25, pb=0, ix=0, po=0, net_cash=-3.41, guide_below=True),
# Memory sweep, added Nov 5 (user: "add MU and STX"): Nov 4 closes per 24/7 Wall St (MU $795.23, its first close
# under $800 since July; STX $557.06). Highs: Yahoo 52-week intraday highs. d 20% / bear 45% for memory cycle
# risk (harsher than chip equipment's 15% / 35%). eg: stockanalysis's 3-year forecast is paywalled and its MU/STX
# statistics pages were stale (FY2025), so eg is entered at the 35% cap; consensus EPS more than doubles from
# FY26 to FY28 for both, so any 3-year figure clears the cap.
# MU: FY26 (Sep 3, 2026) from the stockanalysis financials page: revenue $133.19B, operating margin 74.59%, OCF
# $89.68B, FCF margin 44.27%; ROIC 41.11% and Debt/EBITDA 0.05 from the ratios page. Target $1,562 (stockanalysis,
# Oct 29). NTM EPS 176.6 = $884.79 / 5.01 forward P/E (ratios page, Oct 30). rev90: Yahoo FY28 EPS 206.89 vs
# 162.94. FQ1 guide $61.5B / $38.15 vs $57.93B / $35.92 consensus (AskTraders, Sep 30). Softest input: peak EPS
# x a 12x median P/E; on the target alone MU scores 7.36.
# STX: TTM to Oct 2, 2026: revenue ~$13.8B, OCF $4.83B, FCF $4.16B (30.13%); operating margin is FY26's 34.65%
# (TTM not shown); ROIC 31.66% and Debt/EBITDA 0.85 from the ratios page (Oct 26). Target $1,045 (stockanalysis,
# Oct 29, 26 analysts). NTM EPS ~40 (stockanalysis FY27 average 39.98). rev90: Yahoo FY28 EPS 57.44 vs 45.14.
# FQ2 guide $4.80B / $9.20 EPS vs ~$8.54 consensus before the print (24/7 Wall St, Yahoo). fpe_hist median 21.5x is
# inflated by the FY23-24 earnings trough; on the target alone STX scores 7.07.
# Checked and off: SNDK dead money at $1,037.40 (2.703 years vs its $2,335 Jun 25 closing high; on at $1,038.45+,
# ~7.3); WDC dead money at $323.83 (3.01 years vs $799.87; needs $355.73).
# Cycle guard (revision 20, Nov 5): cyclical-industry names (memory and storage, semiconductor equipment and
# foundry, commodity producers) whose latest stockanalysis quarterly-ratios ROIC is at least 2x the average of its
# latest 20 readings are scored on through-cycle numbers (scorer docstring). Triggered:
#   MU  ROIC 41.11 vs 6.87 average (6.0x), k = 0.25 (floor; raw 0.17). FY22-26 operating margin 31.57, -23.00, 5.19,
#       26.14, 74.59 (avg 22.90); OCF margin 49.36, 10.03, 33.88, 46.89, 67.33 (avg 41.50); FCF margin 10.12, -39.36,
#       0.48, 4.46, 44.27 (avg 3.99). Mid-cycle NTM EPS 44.2.
#   STX ROIC 31.66 vs 8.63 average (3.7x), k = 0.273. FY22-26 operating margin 16.79, -1.68, 6.44, 21.05, 34.65 (avg
#       15.45); OCF margin 14.21, 12.76, 14.01, 11.90, 30.13 (avg 16.60); FCF margin 10.94, 8.48, 10.14, 8.99, 25.46
#       (avg 12.80). Mid-cycle NTM EPS 10.9.
# Tested, not triggered (latest vs 20-reading average): LRCX 25.73 vs 16.62 (1.5x), ASML 31.68 vs 18.27 (1.7x),
#   TER 12.07 vs 8.54 (1.4x), TSEM 4.58 vs 3.78 (1.2x), AMAT 11.50 vs 10.91 (1.1x).
'MU': dict(price=795.23, high=1255.0, target=1562.0, eg=35.0, opm=74.59, ocf_margin=67.33, fcf_margin=44.27, roic=41.11, debt_ebitda=0.05, rev90=0.2697, ntm_eps=176.6, fpe_hist=[6.64, 9.83, 10.35, 13.62, 10.15, 11.11, 11.99, 11.01, 12.78, 26.19, 48.88, 203.0, 203.0, 203.0, 203.0, 203.0, 11.93, 6.53, 8.89, 9.2], d=0.20, bear=0.45, pb=0, ix=0, po=0, cycle=dict(roic_now=41.11, roic_avg=6.87, opm_avg=22.90, ocf_avg=41.50, fcf_avg=3.99), ye_close=285.41),
'STX': dict(price=557.06, high=1145.0, target=1045.0, eg=35.0, opm=34.65, ocf_margin=35.0, fcf_margin=30.13, roic=31.66, debt_ebitda=0.85, rev90=0.2725, ntm_eps=40.0, fpe_hist=[33.69, 25.67, 23.03, 24.23, 14.86, 9.93, 10.74, 16.24, 21.91, 31.8, 60.03, 114.98, 59.0, 21.61, 21.36, 11.01, 7.67, 9.87, 13.0, 10.38], d=0.20, bear=0.45, pb=0, ix=0, po=0, gp=-0.25, cycle=dict(roic_now=31.66, roic_avg=8.63, opm_avg=15.45, ocf_avg=16.60, fcf_avg=12.80)),
# NVDA added Nov 5 (user: "Add NVDA"). Price $200.30, the Nov 4 close (InvestSmart; StatMuse's last Nov 4 hourly bar
# $200.24). High $239.24, the Oct 6, 2026 record close (stockanalysis history); $203.35 is the 15% line, so a 1.5% rally
# takes it out of the universe. Fundamentals: stockanalysis statistics (Nov 1): TTM revenue $302.97B, operating margin
# 65.21%, OCF $134.36B (44.35%), FCF margin 41.92%, ROIC 92.03%, Debt/EBITDA 0.19, net cash $23.61B, 3-year EPS growth
# 64.78%, target $328.95. rev90: Yahoo FY28 EPS 15.91 vs 12.81 90 days ago. NTM EPS 12.095 = $204.64 / 16.92 forward P/E
# (ratios page, Oct 30); Yahoo's Q4 FY27 + 3/4 FY28 gives 14.68 (scores 9.34). fpe_hist median 35.25x is the FY22-27
# range, when the multiple still priced the ramp; on the target alone NVDA scores 7.53, still first.
# CG: fabless, exempt; ROIC 92.0 sits below its 20-reading average of 101.0, so it would not trigger anyway.
# d 15% (hyperscaler concentration, OpenAI commitment), bear 30% (AI-capex cycle). PO 0: China is already out of guidance,
# and chip-equipment names carry no export-control points either.
# PB +0.1 (holding): Pelosi bought 20 $100 calls (Jan 2027) on Dec 30, 2025 and exercised 50 $80 calls into 5,000 shares on
# Jan 16, filed Jan 23 (window to Jan 23, 2027); $200.30 is above the $187.10 Dec 30 close, so no buy boost. No later
# sale found. IX +0.2: #1 in SPY (7.77%, Oct 23) and QQQ (8.75%, Feb 13 file; stockanalysis has no newer one).
# GP 0: no quarter in the 12-month window had three officer sellers (Q4 2025 Kress, Shoquist; Q1 2026 Kress, Puri;
# Q2 none; Q3 Kress, Teter); ~6.2M shares sold in all, mostly director Mark Stevens, ~0.03% of ~24.3B shares.
# Next print Nov 17 after the close (NVIDIA IR; call 5 pm ET): re-check #19 and GD.
'NVDA': dict(price=200.30, high=239.24, target=328.95, eg=64.78, opm=65.21, ocf_margin=44.35, fcf_margin=41.92, roic=92.03, debt_ebitda=0.19, rev90=0.242, ntm_eps=12.095, fpe_hist=[58.95, 45.52, 32.82, 33.7, 40.13, 52.57, 61.17, 50.26, 26.95, 31.19, 35.1, 38.52, 41.66, 36.24, 26.83, 35.4, 32.7, 26.73, 24.97, 20.82], d=0.15, bear=0.30, pb=0.1, ix=0.2, po=0, net_cash=23.61, ye_close=186.51),
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
        gp = (f"  GP {r['gp']:+.2f}" if r['gp'] else "") + (f"  CG x{r['cg']:.2f}" if r['cg'] else "")
        gp += (f"  CW {r['cw']:+.1f}" if r['cw'] else "") + (f"  YT {r['yt']:+.1f} ({r['ytd']*100:+.0f}%)" if r['yt'] else "")
        print(f"{tag}{i:>2} {k:5} {r['final']:5.2f}  Q {r['quality']:4.1f}  12m {r['ret_12m']*100:6.1f}%  yrs {r['years']:4.2f}{gp}")
    for k, r in off:
        print(f"OFF    {k:5} {r['excluded']}")
