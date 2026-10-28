"""Revision 11 dead-money (DM) and ATH-reclaim (NR) checks.

Usage: python3 -I dm_nr.py inputs.json

Each ticker in inputs.json:
  price, ath_close, div_yield (decimal), base_eps (consensus, base year = first FY ending
  >= 6 months after the screen date), seed_growth (base-year EPS growth over the current FY),
  eps_path: consensus EPS for base+1 .. base+5 (null = fade at 85% of the prior year's growth),
  median_fwd_pe: five-year median forward P/E or null, sf: true if the name is a verified
  self-funding compounder (SF safe harbor inputs recorded in the README table).

Method (price-health.md, revision 11):
  DM: framework C's three-year return with the five-year median forward P/E replacing the
      30x/35x cap when available (exit = lower of entry and that cap). Base must be >= the DM
      floor; the stress case (every forward year's EPS growth cut 5 points, exit re-capped on the
      stressed path) must leave the three-year value plus dividends at or above today's price.
  NR: five-year EPS path, exit multiple = the five-year median forward P/E (re-rating to the
      company's own norm is allowed in either direction); with no median, framework C's rule
      (lower of entry and 30x, or 35x when the EPS CAGR is >= 25%). Base-case year-5 value
      must reach the split-adjusted closing ATH.
"""
import json
import sys

DM_FLOOR = 0.08
STRESS_CUT = 0.05
NR_YEARS = 5
SF_NR_YEARS = 7


def growths(base, eps_path, seed, years):
    out, prev_g, e = [], seed, base
    path = list(eps_path) + [None] * (years - len(eps_path))
    for x in path[:years]:
        g = (x / e - 1) if x is not None else 0.85 * prev_g
        out.append(g)
        e *= 1 + g
        prev_g = g
    return out


def eps_path(base, eps_path_, seed, years, cut=0.0):
    out, e = [], base
    for g in growths(base, eps_path_, seed, years):
        e *= 1 + g - cut
        out.append(e)
    return out


def cap(entry, cagr, median):
    if median:
        return min(entry, median)
    return min(entry, 35.0 if cagr >= 0.25 else 30.0)


def dm(d, cut=0.0):
    price, base = d["price"], d["base_eps"]
    eps = eps_path(base, d["eps_path"], d["seed_growth"], 3, cut)
    cagr = (eps[-1] / base) ** (1 / 3) - 1
    entry = price / base
    exit_mult = cap(entry, cagr, d.get("median_fwd_pe"))
    r = (eps[-1] * exit_mult / price) ** (1 / 3) - 1 + d.get("div_yield", 0.0)
    return dict(ret=r, exit_mult=exit_mult, eps_cagr=cagr, entry=entry)


def nr(d, years=NR_YEARS):
    price, base, ath = d["price"], d["base_eps"], d["ath_close"]
    entry = price / base
    eps = eps_path(base, d["eps_path"], d["seed_growth"], 15)
    med = d.get("median_fwd_pe")
    reclaim = None
    for t in range(1, 16):
        cagr = (eps[t - 1] / base) ** (1 / t) - 1
        mult = med if med else min(entry, 35.0 if cagr >= 0.25 else 30.0)
        if eps[t - 1] * mult >= ath and reclaim is None:
            reclaim = t
    cagr_n = (eps[years - 1] / base) ** (1 / years) - 1
    mult_n = med if med else min(entry, 35.0 if cagr_n >= 0.25 else 30.0)
    value_n = eps[years - 1] * mult_n
    return dict(value=value_n, mult=mult_n, ok=value_n >= ath, reclaim_year=reclaim,
                gap=ath / price - 1)


def fmt(t, d):
    if d.get("base_eps") is None or d["base_eps"] <= 0:
        return f"{t:8s} base EPS not meaningful: route model (G5/H4) required"
    b, s = dm(d), dm(d, STRESS_CUT)
    n5, n7 = nr(d, NR_YEARS), nr(d, SF_NR_YEARS)
    dm_ok = b["ret"] >= DM_FLOOR and s["ret"] >= 0
    return (f"{t:8s} entry {b['entry']:5.1f}x exitDM {b['exit_mult']:5.1f}x | DM base {b['ret']*100:5.1f}% "
            f"stress {s['ret']*100:6.1f}% -> {'pass' if dm_ok else 'BLOCK'} | ATH gap {n5['gap']*100:6.1f}% "
            f"NR exit {n5['mult']:5.1f}x y5 value {n5['value']:9.2f} vs ATH {d['ath_close']:9.2f} "
            f"-> {'pass' if n5['ok'] else 'BLOCK'} | y7 {'pass' if n7['ok'] else 'block'} | "
            f"reclaim yr {n5['reclaim_year'] or '>15'}")


if __name__ == "__main__":
    data = json.load(open(sys.argv[1]))
    for t, d in data.items():
        if t.startswith("_"):
            continue
        print(fmt(t, d))
