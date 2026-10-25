"""Ticker table for the revision 8 history rerun.
Usage: python3 -I report.py overrides.json batch_*.json > table.md
overrides.json: {"TICKER": {"prior": "...", "verdict": "...", "h": "..."}}
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import screen as s

BATCH = {"batch_software.json": "Software/platforms", "batch_infra.json": "Infra/power",
         "batch_semis.json": "Semis", "batch_other.json": "Other sectors"}

def short(fails, n=3):
    return "; ".join(fails[:n]) + (" …" if len(fails) > n else "") if fails else "pass"

def price(d):
    p = s.g(d, "price"); cur = d.get("currency")
    unit = (cur + " ") if cur and cur not in ("USD",) and not d.get("price_currency") else ""
    return f"{unit}{p:,.2f}" if p is not None else "n/a"

def main(ovr_path, paths):
    ovr = json.load(open(ovr_path))
    print("| Ticker | Lane | Oct 23 close | Next print | Core A–E headline fails | #12 | 3Y return est. (stress) | Prior verdict | Revision 8 verdict | H line |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for p in paths:
        lane = BATCH.get(os.path.basename(p), p)
        for d in sorted(json.load(open(p)), key=lambda r: r["ticker"]):
            t = d["ticker"]; o = ovr.get(t, {})
            b = s.base_year(d); r = s.ret_estimate(d, b)
            ret = f"{r['ret']}% ({r['stress']}%)" if r else "n/a"
            if t in s.F:
                core, twelve = "F route only", ""
            else:
                ft = t in s.FT
                c, f3, fy = s.core(d, ft, b)
                core = ("[FT] " if ft else "") + short(c)
                twelve = "ok" if s.p12(d, fy)[0] else "fail"
            if "h" in o:
                h = o["h"]
            elif t in s.FT:
                h = "FT1 bars H"
            elif t in s.F:
                h = "F name, no H"
            elif (s.g(d, "fcf_ttm_bn") or 0) <= 0 or (s.g(d, "operating_income_ttm_bn") or 0) <= 0:
                h = "H-review: cash floor not met; H4 model not built, so H-watch at best"
            else:
                h = "H n/a: cash engine exists; H does not waive growth or valuation"
            print(f"| {t} | {lane} | {price(d)} | {d.get('next_earnings') or 'n/a'} | {core} | {twelve} | {ret} | "
                  f"{o.get('prior', '')} | {o.get('verdict', 'MISSING')} | {h} |")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
