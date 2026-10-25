"""Build the ticker-by-ticker markdown table for the non-AI audit from screen.py's logic.
Usage: python3 -I report.py overrides.json data/*.json > table.md
overrides.json: {"TICKER": {"verdict": "...", "h": "..."}} for deep-checked names.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import screen as s

SEEDS = {"HWM", "FTAI", "HEI", "TDG", "UBER", "DASH", "MELI", "SE", "CPNG", "LLY", "VRTX", "ARGX",
         "ISRG", "AXON", "RHM.DE", "CRWD", "PANW", "FTNT", "ZS", "HOOD", "COIN", "RKLB", "ASTS", "CCJ"}

def fmt_price(d):
    p = s.g(d, "price")
    cur = (d.get("currency") or "")
    unit = "" if not cur or cur.startswith("Price/PT USD") or cur.startswith("USD") or "price/statistics USD" in cur else cur.split()[0] + " "
    return f"{unit}{p:,.2f}" if p is not None else "n/a"

def short(fails, n=3):
    return "; ".join(fails[:n]) + (" …" if len(fails) > n else "") if fails else "pass"

def main(ovr_path, paths):
    ovr = json.load(open(ovr_path)) if os.path.exists(ovr_path) else {}
    rows, seen = [], set()
    for p in paths:
        for d in json.load(open(p)):
            if d["ticker"] in seen:
                continue
            seen.add(d["ticker"]); rows.append(d)
    print("| Ticker | Lane | Oct 23 close | Core A–E (headline fails) | #12 | G | D | Growth door (rev 8) | 3Y return est. (method; stress) | Verdict | H line |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for d in sorted(rows, key=lambda r: (str(r.get("lane")), r["ticker"])):
        t = d["ticker"]; lane = str(d.get("lane", "")).split("-")[0]
        tag = "" if t in SEEDS else " [NEW DISCOVERY]"
        b = s.base_year(d); r = s.ret_estimate(d, b)
        ret = f"{r['ret']}% ({r['method']}; {r['stress']}%)" if r else "n/a (no positive base-year EPS)"
        o = ovr.get(t, {})
        if t in s.EXCL:
            print(f"| {t}{tag} | {lane} | {fmt_price(d)} | excluded (bank/insurer) | | | | | | Excluded | |"); continue
        if t in s.F:
            print(f"| {t}{tag} | {lane} | {fmt_price(d)} | F route only | | | | n/a (F) | {ret} | {o.get('verdict', 'Tier 3: F route')} | F name, no H |"); continue
        ft = t in s.FT
        c, f3, fy = s.core(d, ft, b)
        ok12, void = s.p12(d, fy)
        gg = s.route_g(d, b, f3) if not ft else ["FT1 bars G"]
        dd = s.route_d(d, b) if not ft else ["FT1 bars D"]
        if not ft and not any(x.startswith("A1") for x in c):
            dd = ["D scope: no A1 issuance failure"]
        twelve = "ok" if ok12 else ("fail (PT void)" if void else "fail")
        if ft:
            hline = "FT1 bars H"
        elif (s.g(d, "fcf_ttm_bn") or 0) <= 0 or (s.g(d, "operating_income_ttm_bn") or 0) <= 0 or (s.fcf_margin(d) or 0) < 6:
            hline = o.get("h", "H-review: cash floor not met; H4 model not built, so H-watch at best")
        else:
            hline = o.get("h", "H n/a: cash engine already exists; H does not waive growth or valuation")
        verdict = o.get("verdict")
        doors = s.hurdle(d, r)
        if not verdict:
            gate_ok = (not c) or (not gg) or (not dd)
            if gate_ok and doors:
                verdict = "Deep check needed"
            elif gate_ok:
                rv = s.g(d, "rev_growth_3y_pct")
                verdict = (f"Tier 3: below 20% growth hurdle (rev {rv}%, EPS {r['eps_cagr'] if r else 'n/a'}%)")
            else:
                verdict = "Tier 3: " + (c[0] if c else (gg[0] if gg else dd[0])).split(" ")[0]
        print(f"| {t}{tag} | {lane} | {fmt_price(d)} | {short(c)} | {twelve} | {'cand' if not gg else short(gg, 2)} | "
              f"{'cand' if not dd else short(dd, 2)} | {'+'.join(o.get('doors', doors)) or 'none'} | {ret} | {verdict} | {hline} |")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
