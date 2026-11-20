"""TSM on the Nov 19, 2026 close and the SL three-risk lens across the board (revision 27). Run Nov 19, 2026.

Two parts, kept apart on purpose:
  1. TSM, scored on fresh inputs pulled Nov 19, 2026 (about 6:50 pm CT).
  2. The 22 board names on the last complete pull in the repo (Nov 6 closes, Nov 4 fundamentals), run through
     the same lens. Fresh Nov 19 closes for all 22 could not be pulled in this session (page fetches returned
     snapshots dated Aug 28 to Nov 18), so part 2 shows how each name's score moves under the three risks. It
     is not a Nov 19 ranking. Rerun it on the next full data pull.

TSM inputs and sources (Nov 19, 2026):
  price 352.09 close (stockanalysis, Yahoo). high 485.80, record close Oct 5, 2026 (macrotrends, 24/7 Wall St).
  ye_close 303.89 (24/7 Wall St, Nov 16). target 586.69, 21 analysts (stockanalysis forecast page).
  stockanalysis statistics page, updated Nov 13: operating margin 57.96%, OCF 95.08B / revenue 155.16B =
  61.28%, FCF margin 29.95%, ROIC 60.30%, Debt / EBITDA 0.23, net cash 100.36B, EPS growth forecast (3Y)
  42.41%, gross margin 65.85% (ID pass), shares +0.01% YoY, buyback yield -0.01%, dividend 4.49.
  rev90: Yahoo EPS trend, 2027 EPS 23.39 now vs 21.28 ninety days ago = +9.9%.
  ntm_eps: 352.09 / 16.96 forward P/E (stockanalysis) = 20.76. No forward P/E history is shown for the ADR, so
  fair value uses the target leg alone, like ASML.
  cycle (foundry is a CG industry): stockanalysis quarterly ROIC, latest 20 readings Q4 2021 to Q3 2026,
  latest 66.30 vs average 43.29 = 1.53x, so CW -1.0 and no CG rescoring. Five-fiscal-year (FY21-25) average
  margins: operating 45.92, OCF 64.3, FCF 22.08.
  CC: 2025 20-F, Customer A 19% and Customer B 17% of net revenue -> minor, -0.25.
  RE: stockanalysis forecast, FY2026 110.63 (40 analysts), base FY2027 149.53; FY2025 66.25 x 1.4241^3 =
  FY2028 191.34 (single source). Entry multiple 352.09 / 23.39 (Yahoo 2027 EPS in USD) = 15.05. 25.2% -> +0.25.
  PB none found (Trump's Aug 2026 278-T has no TSM line; no Pelosi buy found). IX none (not in the S&P 500 or
  Nasdaq-100). PO 0 (US-Taiwan investment deal and new China export limits offset; not scored). BB 0 (share
  count flat). HT open. GP 0: #7 and #19 were clear on the Oct 24 deep check and were not re-pulled.
  d 0.15 and bear 0.30 are judgment inputs.

Lens inputs (judgment, recorded so they can be argued with): ai = share of revenue tied to the AI
accelerator and data-center build; e1 / e2 = cut to next-year / following-year EPS if SemiAnalysis's Nov 13,
2026 forecast is right (accelerator capex 2027 -19%, 2028 -28%; Nvidia compute revenue -22% / -39%; Broadcom
custom chips -11% over five years; chip area 2026-30 -17%; HBM 2028 -30%; power 2030 -34%).

Adjustments recorded in chat on Nov 16-17, 2026 and applied here: NVDA d 0.25 / bear 0.40 (CEO exit); CC
CRDO -1.0, ALAB -1.0, RMBS -0.25; HT TSEM -0.25; GP RMBS -1.0 (legal flag); GOOGL kept on the dead-money test.
"""
import contextlib
import io
import sys

with contextlib.redirect_stdout(io.StringIO()):
    from board_2026_11_06_close_re import CC as CC6, ESTIMATES as EST6, INPUTS as NOV6, RE as RE6
from recovery_score import LINE, cc_points, lens, return_estimate

TSM = dict(price=352.09, high=485.80, target=586.69, eg=42.41, opm=57.96, ocf_margin=61.28, fcf_margin=29.95,
           roic=60.30, debt_ebitda=0.23, rev90=23.39 / 21.28 - 1, ntm_eps=352.09 / 16.96, fpe_hist=None,
           d=0.15, bear=0.30, pb=0, ix=0, po=0, net_cash=100.36, ye_close=303.89,
           cycle=dict(roic_now=66.30, roic_avg=43.2925, opm_avg=45.92, ocf_avg=64.3, fcf_avg=22.08),
           cc=cc_points(direct=(0.19, 0.17)), bb=0.0)
TSM_RE = dict(base_eps=149.53, prior_eps=110.63, out_years=[66.25 * 1.4241 ** 3], dividend=4.49,
              entry_pe=352.09 / 23.39)
TSM["re_ret"] = return_estimate(TSM["price"], **TSM_RE)["ret"]

# name: (ai, e1, e2)
LENS = {
    "TSM": (0.33, 0.05, 0.12),   # AI accelerators high-teens % of 2025 revenue, rising; paid per wafer
    "NVDA": (0.90, 0.15, 0.30),  # two-thirds of the chip-area cut; price cuts on top
    "AVGO": (0.60, 0.04, 0.08),  # custom chips cut 11% over five years
    "CRDO": (0.95, 0.15, 0.25), "ALAB": (0.90, 0.12, 0.22),
    "TER": (0.50, 0.08, 0.15), "TSEM": (0.30, 0.05, 0.10), "RMBS": (0.40, 0.05, 0.10),
    "SMTC": (0.35, 0.06, 0.12), "MTSI": (0.35, 0.05, 0.10), "MPWR": (0.30, 0.05, 0.10),
    "KLAC": (0.35, 0.04, 0.10), "LRCX": (0.35, 0.05, 0.12), "AMAT": (0.30, 0.04, 0.10), "ASML": (0.30, 0.03, 0.08),
    "ANET": (0.45, 0.06, 0.12), "VRT": (0.75, 0.10, 0.20), "FIX": (0.40, 0.06, 0.15), "GEV": (0.25, 0.03, 0.08),
    "CDNS": (0.20, 0.02, 0.04),
    "GOOGL": (0.0, 0.0, 0.0), "META": (0.0, 0.0, 0.0),  # AI spenders: a capex cut helps cash flow; no credit taken
    "UBER": (0.0, 0.0, 0.0),
}
BOARD = ["NVDA", "TER", "CRDO", "TSEM", "AVGO", "FIX", "KLAC", "RMBS", "GOOGL", "META", "SMTC", "LRCX", "UBER",
         "ALAB", "MPWR", "GEV", "CDNS", "ASML", "AMAT", "MTSI", "VRT", "ANET"]
LATER = {"NVDA": dict(d=0.25, bear=0.40), "CRDO": dict(cc=-1.0), "ALAB": dict(cc=-1.0), "RMBS": dict(cc=-0.25, gp=-1.0),
         "TSEM": dict(ht=-0.25)}
CASES = ("today", "rates", "semi", "peak")


def run(name, inputs, re_args=None, fpe_est=None, keep=False):
    ai, e1, e2 = LENS[name]
    c = inputs.get("cycle") or {}
    k_cycle = c["roic_avg"] / c["roic_now"] if c.get("roic_now") and 0 < c.get("roic_avg", 0) < c["roic_now"] else None
    avgs = dict(opm=c["opm_avg"], ocf=c["ocf_avg"], fcf=c["fcf_avg"]) if "opm_avg" in c else None
    return lens(inputs, ai=ai, e1=e1, e2=e2, k_cycle=k_cycle, avgs=avgs, fpe_est=fpe_est, re_args=re_args, keep=keep)


def cell(r):
    if "final" in r:
        return f"{r['final']:5.2f}{'*' if not r['on_board'] else ' '}"
    why = r["excluded"]
    return {"no": " nofv ", "le": " <20% ", "fa": " est  ", "de": " dead ", "gu": " guide"}.get(why[:2], "  off ")


if __name__ == "__main__":
    t = run("TSM", TSM, re_args=TSM_RE, fpe_est=19.0)
    print(f"Line {LINE}. * = under the line. Cases stack: rates, then SemiAnalysis right, then capex peak.")
    print("nofv = no fair value (deep drop, estimates not rising, no P/E history); est = falling-estimates block; "
          "dead = dead money; <20% = Market Mondays block. Entry gates apply to the today column only.")
    print("TSM, Nov 19, 2026 close $352.09")
    print("  " + " | ".join(f"{c} {cell(t[c])}" for c in CASES))
    r = t["today"]
    print(f"  quality {r['quality']} asym {r['asym']} speed {r['speed']} 12m {r['ret_12m']:.1%} bear {r['bear_penalty']} "
          f"cw {r['cw']} yt {r['yt']} cc {r['cc']} re {r['re']} (estimate {TSM['re_ret']:.1%}) below {r['below']:.1%} ytd {r['ytd']:.1%}")
    print("\nBoard names, Nov 6 closes (last complete pull), same lens. Not a Nov 19 ranking.")
    rows = []
    for k in BOARD:
        inp = dict(NOV6[k], **LATER.get(k, {}))
        if "cc" not in inp and k in CC6:
            inp["cc"] = cc_points(**CC6[k])
        re_args = dict(RE6[k], fpe_hist=inp.get("fpe_hist")) if k in RE6 else None
        if k in EST6:
            inp["re_ret"] = EST6[k]["ret"]
        res = run(k, inp, re_args=re_args, keep=(k == "GOOGL"))
        rows.append((k, inp["price"], res))
    key = lambda x: -(x[2]["today"].get("_raw", -99))
    for k, px, res in sorted(rows, key=key):
        why = "" if "final" in res["today"] else "  " + res["today"]["excluded"]
        print(f"  {k:5} ${px:<8} " + " | ".join(cell(res[c]) for c in CASES) + why)
