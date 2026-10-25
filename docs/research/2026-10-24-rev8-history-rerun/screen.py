"""Non-AI-capex open-universe screen, revision 8 (Oct 24, 2026).

Headline hard gates from stockanalysis statistics/forecast fields, plus the framework C
(revision 6) return estimate. Issuance in the last 12 months, insiders (#7), #19, PH and
full G5/H4 models are checked separately for survivors (see README.md in this folder).

Usage: python3 -I screen.py batch_*.json
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from d_return import d_return

SCREEN = (2026, 10)                       # screen month
FT = {"HOOD", "COIN", "IBKR", "TW", "VIRT", "CME", "CBOE", "SCHW", "ICE", "NDAQ", "MKTX",
      "MELI", "SE", "GRAB", "DLO", "PAGS", "STNE", "NU", "XP", "TOST", "AFRM", "SOFI",
      "FUTU", "GLXY", "CRCL", "XYZ", "MA"}
F = {"CCJ", "KAP", "KAP.L", "UEC", "NXE", "UUUU", "DNN", "PDN",          # commodity producers: F only
     "NEM", "AEM", "KGC", "GFI", "AU", "WPM", "FNV", "PAAS", "AGI", "RGLD", "CDE", "HL",
     "VST", "CEG"}   # IPPs route to F (roster, Sep 28)
EXCL = {"NU", "KNSL", "KSPI", "AXP"}                               # banks/insurers: logged only
MONTHS = {m: i + 1 for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}

def g(d, k):
    v = d.get(k)
    try:
        return None if v is None else float(v)
    except (TypeError, ValueError):
        return None

def fcf_margin(d):
    m = g(d, "fcf_margin_pct")
    if m is None and g(d, "fcf_ttm_bn") is not None and g(d, "revenue_ttm_bn"):
        m = round(g(d, "fcf_ttm_bn") / g(d, "revenue_ttm_bn") * 100, 1)
    return m

def fy_end(label):
    """(year, month) of the 'this year' fiscal period from labels like 'FY2027 (Jun 2027)'."""
    if not label:
        return None
    m = re.search(r"\(([A-Z][a-z]{2})[a-z]*[\s-]*(?:\d{1,2},\s*)?(\d{4}|\d{2})\)", label)
    if m and m.group(1) in MONTHS:
        y = int(m.group(2)); y = y + 2000 if y < 100 else y
        return y, MONTHS[m.group(1)]
    m = re.search(r"(\d{4})", label)
    return (int(m.group(1)), 12) if m else None

def months_out(end):
    return (end[0] - SCREEN[0]) * 12 + end[1] - SCREEN[1]

def base_year(d):
    """Framework C base year: first FY ending >= 6 months after the screen.
    Returns dict(base_eps, seed, path0, base_rev_g, next_rev_g, label) or None."""
    end = fy_end(d.get("next_fy_label")) or (SCREEN[0], 12)
    e0, e1 = g(d, "next_fy_eps"), g(d, "following_fy_eps")
    r0, r1 = g(d, "next_fy_rev_growth_pct"), g(d, "following_fy_rev_growth_pct")
    # Gate-defined next-FY (framework: the fiscal year after the last completed one). When the
    # 'this year' column has not ended yet it is next-FY; once it has ended, next-FY is the following year.
    yr_after = (e1 / e0 - 1) * 100 if (e0 and e1 and e0 > 0) else None
    if months_out(end) > 0:
        gate = dict(gate_next_rev=r0, gate_after_rev=r1, gate_next_eps=None, gate_after_eps=yr_after)
    else:
        gate = dict(gate_next_rev=r1, gate_after_rev=None, gate_next_eps=yr_after, gate_after_eps=None)
    if months_out(end) >= 6:          # 'this year' already qualifies (e.g. Jun-2027 FY)
        base, seed = e0, None
        path0 = e1
        return dict(base_eps=base, seed=(e1 / e0 - 1) if (e0 and e1 and e0 > 0) else None,
                    path0=path0, base_rev_g=r0, next_rev_g=r1, base_is="this-year", **gate)
    seed = (e1 / e0 - 1) if (e0 and e1 and e0 > 0) else None
    return dict(base_eps=e1, seed=seed, path0=None, base_rev_g=r1, next_rev_g=None, base_is="next-year", **gate)

def fwd3_rev(b, d=None):
    if d is not None and g(d, "rev_growth_3y_pct") is not None:
        return g(d, "rev_growth_3y_pct")
    a, c = b["base_rev_g"], b["next_rev_g"]
    if a is None:
        return None
    c = c if c is not None else 0.85 * a
    third = 0.85 * c
    return (((1 + a / 100) * (1 + c / 100) * (1 + third / 100)) ** (1 / 3) - 1) * 100

def ret_estimate(d, b):
    price, base = g(d, "price"), b["base_eps"]
    if not (price and base and base > 0 and b["seed"] is not None):
        return None
    div = (g(d, "dividend_yield_pct") or 0) / 100
    inp = dict(price=price, div_yield=div, base_eps=base,
               eps_path=[b["path0"], None, None], seed_growth=b["seed"],
               consensus_shares=1, fdso0=1, fdso_growth=[0, 0, 0, 0], median_fwd_pe=None)
    r = d_return(inp, restate=False)
    r["stress"] = d_return(inp, cut=0.05, restate=False)["ret"]
    r["method"] = "fade"
    e3 = g(d, "eps_growth_3y_pct")
    if e3 is not None and e3 > -50:
        alt = dict(inp, eps_path=[base * (1 + e3 / 100) ** k for k in (1, 2, 3)])
        ra = d_return(alt, restate=False)
        if ra["ret"] < r["ret"]:
            ra["stress"] = d_return(alt, cut=0.05, restate=False)["ret"]
            ra["method"] = "3Y-forecast"
            r = ra
    # price at which the estimate equals 25% (only exists when the exit cap binds)
    cagr = r["eps_cagr"] / 100
    cap = 35.0 if cagr >= 0.25 else 30.0
    exit_eps = r["exit_eps"]
    # Below the cap the exit multiple equals the entry multiple, so the estimate is EPS CAGR + yield
    # at any lower price: a 25% price exists only when EPS CAGR + yield >= 25%.
    r["p25"] = round(exit_eps * cap / (1.25 - div) ** 3, 2) if cagr + div >= 0.25 else None
    return r

def core(d, ft, b):
    fails = []
    sh, bb = g(d, "shares_yoy_pct"), g(d, "buyback_yield_pct")
    fcfm, fcf, nc, mc = fcf_margin(d), g(d, "fcf_ttm_bn"), g(d, "net_cash_bn"), g(d, "market_cap_bn")
    f3 = fwd3_rev(b, d)
    if sh is None:
        fails.append("A1?")
    elif not (sh <= 0.5 or (sh <= 1.5 and (bb or 0) > 0 and (f3 or 0) >= 25)):
        fails.append(f"A1 shares {sh:+.1f}%")
    if not ((bb or 0) > 0 or ((nc or 0) > 0 and (sh if sh is not None else 9) <= 0.5)):
        fails.append("A2")
    floor = 8 if ft else 6
    if fcfm is None or fcfm < floor:
        fails.append(f"A3a FCF {fcfm if fcfm is not None else 'n/a'}%")
    ocf, capex = g(d, "ocf_ttm_bn"), g(d, "capex_ttm_bn")
    if ocf and capex is not None and ocf > 0 and abs(capex) / ocf > 0.5:
        fails.append(f"A3c capex/OCF {abs(capex)/ocf:.0%}")
    if fcf and fcf > 0 and nc is not None and -nc / fcf > 2.5:
        fails.append(f"A4 {(-nc/fcf):.1f}x")
    nf = b["gate_next_rev"]            # gate-defined next-FY, not the return base year
    lo3, lonf = (15, 15) if ft else (15, 12)
    if (f3 or 0) < lo3 or (nf is not None and nf < lonf):
        fails.append(f"#9 fwd3 {f3:.1f}%/next {nf}%" if f3 is not None else "#9 n/a")
    pe, peg = g(d, "fwd_pe"), g(d, "peg")
    fy = (fcf / mc * 100) if (fcf and mc) else None
    std = pe and peg and fy and pe <= 38 and peg <= 2.0 and fy >= 1.5
    hv = pe and peg and fy and (f3 or 0) >= 25 and peg <= 1.65 and pe <= 45 and fy >= 1.15
    if not (std or hv):
        fails.append(f"#11 PE {pe} PEG {peg} FCFy {round(fy, 2) if fy else None}")
    return fails, f3, fy

def p12(d, fy):
    """#12 (revision 8): consensus PT >= +20% (>=5 analysts) OR NTM FCF yield >= 5%.
    The 200DMA void on the PT leg was removed in revision 8; `void` is kept only as a report flag."""
    up, n, p, ma = g(d, "pt_upside_pct"), g(d, "analysts"), g(d, "price"), g(d, "ma200")
    void = False
    ok = (up is not None and up >= 20 and (n or 0) >= 5) or (fy is not None and fy >= 5)
    return ok, void

def route_g(d, b, f3):
    fails = []
    fcfm, sh, fcf, nc = fcf_margin(d), g(d, "shares_yoy_pct"), g(d, "fcf_ttm_bn"), g(d, "net_cash_bn")
    ocf, capex = g(d, "ocf_ttm_bn"), g(d, "capex_ttm_bn")
    if fcfm is None or fcfm < 6: fails.append("G2 FCF<6%")
    if ocf and capex is not None and ocf > 0 and abs(capex) / ocf > 0.5: fails.append("G2 capex")
    if sh is None or sh > 3: fails.append(f"G3 shares {sh}")
    nf = b["gate_next_rev"]
    if (f3 or 0) < 10 or (nf is not None and nf < 10): fails.append("G2 growth")
    if fcf and fcf > 0 and nc is not None and -nc / fcf > 2.5: fails.append("G2 leverage")
    return fails

def route_d(d, b):
    fails = []
    mc, fcfm, de = g(d, "market_cap_bn"), fcf_margin(d), g(d, "debt_to_equity")
    rev, ocf, oi, ebitda, nc = (g(d, k) for k in ("revenue_ttm_bn", "ocf_ttm_bn", "operating_income_ttm_bn",
                                                    "ebitda_ttm_bn", "net_cash_bn"))
    if (mc or 0) < 10: fails.append("D0 cap<$10B")
    d2a = fcfm is not None and fcfm >= 6
    d2c = bool(rev and ocf and ocf / rev >= 0.20 and (oi or -1) > 0 and ebitda and ebitda > 0
               and (nc is None or nc >= 0 or -nc / ebitda <= 2.5))
    if not d2a and not d2c: fails.append("D2 cash" + ("" if fcfm is None else f" FCF {fcfm}%"))
    if de is not None and de > 1.99: fails.append(f"D3 D/E {de}")
    # D4 (revision 8): revenue leg OR EPS leg; one metric clears all three legs
    gr3 = g(d, "rev_growth_3y_pct")
    a, c = b["gate_next_rev"], b["gate_after_rev"]     # next-FY and the year after it
    rev_leg = (gr3 or 0) >= 20 and (a is None or a >= 20) and (c is None or c >= 20)
    e3 = g(d, "eps_growth_3y_pct")
    ea, ec = b["gate_next_eps"], b["gate_after_eps"]
    eps_leg = (e3 or 0) >= 20 and (ea is None or ea >= 20) and (ec is None or ec >= 20) and (gr3 or 0) >= 10
    if not (rev_leg or eps_leg):
        fails.append(f"D4 growth rev3y {gr3} (next {a}, after {c}) eps3y {e3}")
    elif not rev_leg and ea is None:
        fails.append("D4? EPS leg needs next-FY EPS growth vs the last completed FY (not in the batch)")
    pe, peg = g(d, "fwd_pe"), g(d, "peg")
    if not (pe and peg and pe <= 45 and peg <= 1.65): fails.append(f"D5a PE {pe} PEG {peg}")
    return fails

def hurdle(d, r):
    """Revision 8 primary-list guardrail: return >=20% OR base-year EPS CAGR >=20% OR fwd 3Y revenue CAGR >=20%."""
    rev3 = g(d, "rev_growth_3y_pct")
    doors = []
    if r and r["ret"] >= 20: doors.append("ret")
    if r and r["eps_cagr"] >= 20: doors.append("eps")
    if rev3 is not None and rev3 >= 20: doors.append("rev")
    return doors

def main(paths):
    rows = []
    for p in paths:
        rows += json.load(open(p))
    seen = set()
    for d in rows:
        t = d["ticker"]
        if t in seen:
            continue
        seen.add(t)
        mc, adv = g(d, "market_cap_bn"), g(d, "avg_dollar_volume_mn")
        floor = "" if (mc is None or mc >= 2.5) and (adv is None or adv >= 25) else " [BELOW FLOOR]"
        if t in EXCL:
            print(f"{t}: excluded (bank/insurer)"); continue
        b = base_year(d)
        r = ret_estimate(d, b)
        doors = hurdle(d, r)
        rs = (f"hurdle={'+'.join(doors) or 'FAIL'} | ret {r['ret']}% [{r['method']}] (EPS CAGR {r['eps_cagr']}%, {r['entry']}x->{r['exit_mult']}x, stress {r['stress']}%, "
              f"25% at {'<=$'+str(r['p25']) if r['p25'] else 'no price'})") if r else (f"hurdle={'+'.join(doors) or 'FAIL'} | ret n/a (no positive base EPS)")
        if t in F:
            print(f"{t}{floor}: F-route only | {rs}"); continue
        ft = t in FT
        c, f3, fy = core(d, ft, b)
        ok12, void = p12(d, fy)
        gg = route_g(d, b, f3) if not ft else ["FT1 bars G"]
        dd = route_d(d, b) if not ft else ["FT1 bars D"]
        if not ft and not any(x.startswith("A1") for x in c):
            dd = ["D scope: no A1 issuance failure"]   # D is only for A1/G3 failures on issuance
        early = (g(d, "fcf_ttm_bn") or 0) <= 0 or (g(d, "operating_income_ttm_bn") or 0) <= 0
        h = "FT1 bars H" if ft else ("review" if early else "n/a (cash engine)")
        print(f"{t}{floor}{' [FT]' if ft else ''}: core={'PASS-headline' if not c else '; '.join(c)} | "
              f"#12={'ok' if ok12 else 'fail'}{' (PT void)' if void else ''} | G={'cand' if not gg else '; '.join(gg)} | "
              f"D={'cand' if not dd else '; '.join(dd)} | M={'scope' if (mc or 0) >= 500 else '-'} | H={h} | {rs}")

if __name__ == "__main__":
    main(sys.argv[1:])
