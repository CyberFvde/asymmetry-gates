"""Hard-gate triage of a ticker list across A-E, G, M, D and H (revision 7 + amendments).
Triage only: flags the first failing hard tests from stockanalysis statistics/forecast fields.
Issuance in the last 12 months, insiders, #19 and full models are NOT checked here.
Usage: python3 -I triage.py stats.json
"""
import json, sys

F_ROUTE = {"UUUU"}            # commodity -> F only
def g(d, k):
    v = d.get(k)
    return None if v is None else float(v)

def core(d):
    fails = []
    sh, bb, gr3 = g(d,"shares_yoy_pct"), g(d,"buyback_yield_pct"), g(d,"rev_growth_3y_pct")
    fcfm, fcf, nc = g(d,"fcf_margin_pct"), g(d,"fcf_ttm_bn"), g(d,"net_cash_bn")
    if sh is None: fails.append("A1?")
    elif not (sh <= 0.5 or (sh <= 1.5 and (bb or 0) > 0 and (gr3 or 0) >= 25)): fails.append(f"A1 shares {sh:+.1f}%")
    if not ((bb or 0) > 0 or ((nc or 0) > 0 and (sh or 9) <= 0.5)): fails.append("A2")
    if fcfm is None or fcfm < 6: fails.append(f"A3a FCF {fcfm if fcfm is not None else 'n/a'}%")
    if fcf and fcf > 0 and nc is not None and -nc / fcf > 2.5: fails.append(f"A4 {(-nc/fcf):.1f}x")
    nf = g(d,"next_fy_rev_growth_pct")
    if (gr3 or 0) < 15 or (nf is not None and nf < 12): fails.append("#9")
    pe, peg, mc = g(d,"fwd_pe"), g(d,"peg"), g(d,"market_cap_bn")
    fy = (fcf / mc * 100) if (fcf and mc) else None
    eps3 = g(d,"eps_growth_3y_pct")
    std = pe and peg and fy and pe <= 38 and peg <= 2.0 and fy >= 1.5
    hv = pe and peg and fy and ((eps3 or 0) >= 30 or (gr3 or 0) >= 25) and peg <= 1.65 and pe <= 45 and fy >= 1.15
    if not (std or hv): fails.append(f"#11 PE {pe} PEG {peg} FCFy {round(fy,2) if fy else None}")
    return fails

def route_g(d):
    fails = []
    fcfm, sh, gr3, nf = g(d,"fcf_margin_pct"), g(d,"shares_yoy_pct"), g(d,"rev_growth_3y_pct"), g(d,"next_fy_rev_growth_pct")
    fcf, nc = g(d,"fcf_ttm_bn"), g(d,"net_cash_bn")
    if fcfm is None or fcfm < 6: fails.append("G2 FCF<6%")
    if sh is None or sh > 3: fails.append(f"G3 shares {sh}")
    if (gr3 or 0) < 10 or (nf is not None and nf < 10): fails.append("G2 growth")
    if fcf and fcf > 0 and nc is not None and -nc / fcf > 2.5: fails.append("G2 leverage")
    return fails

def route_d(d):
    fails = []
    mc, fcfm, de = g(d,"market_cap_bn"), g(d,"fcf_margin_pct"), g(d,"debt_to_equity")
    rev, ocf, oi, ebitda, nc = g(d,"revenue_ttm_bn"), g(d,"ocf_ttm_bn"), g(d,"operating_income_ttm_bn"), g(d,"ebitda_ttm_bn"), g(d,"net_cash_bn")
    if (mc or 0) < 10: fails.append("D0 cap<$10B")
    d2a = fcfm is not None and fcfm >= 6
    d2c = (rev and ocf and ocf / rev >= 0.20 and (oi or -1) > 0 and ebitda and ebitda > 0
           and (nc is None or nc >= 0 or -nc / ebitda <= 2.5))
    if not d2a and not d2c: fails.append("D2 cash" + ("" if fcfm is None else f" FCF {fcfm}%"))
    if de is not None and de > 1.99: fails.append(f"D3 D/E {de}")
    gr3, nf, ff = g(d,"rev_growth_3y_pct"), g(d,"next_fy_rev_growth_pct"), g(d,"following_fy_rev_growth_pct")
    if (gr3 or 0) < 25 or (nf is not None and nf < 20) or (ff is not None and ff < 20): fails.append("D4 growth")
    pe, peg = g(d,"fwd_pe"), g(d,"peg")
    if not (pe and peg and pe <= 45 and peg <= 1.65): fails.append(f"D5a PE {pe} PEG {peg}")
    sh = g(d,"shares_yoy_pct")
    if sh is not None and sh > 8: fails.append(f"D1? trailing shares {sh:+.1f}% (forward model needed)")
    return fails

def main(path):
    data = json.load(open(path))
    for d in data:
        t = d["ticker"]
        if t in F_ROUTE:
            print(f"{t}: F-route only"); continue
        c, gg, dd = core(d), route_g(d), route_d(d)
        mc = g(d,"market_cap_bn") or 0
        early = (g(d,"fcf_ttm_bn") or 0) <= 0 or (g(d,"operating_income_ttm_bn") or 0) <= 0
        print(f"{t}: core={'PASS-headline' if not c else ';'.join(c[:3])} | G={'cand' if not gg else ';'.join(gg)} | "
              f"D={'cand' if not dd else ';'.join(dd)} | M={'scope' if mc>=500 else '-'} | H={'review' if early else 'n/a-cash engine'}")

if __name__ == "__main__":
    main(sys.argv[1])
