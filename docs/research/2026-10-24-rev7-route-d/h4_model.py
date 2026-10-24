"""H4 five-year per-share model (stage-paths.md H4, shared valuation convention).

Year-five equity value = terminal EV/EBITDA x year-5 EBITDA - year-5 net debt (converts not
converted at principal, leases, other claims) ; per share = equity / year-5 fully diluted shares.
Annualized return = (per-share value / entry price)^(1/5) - 1 (no dividends).
Usage: python3 -I h4_model.py h4_inputs.json
"""
import json, sys

def run(s, price):
    ev = s["ev_ebitda"] * s["ebitda_y5"]
    eq = max(0.0, ev - s["net_debt_y5"])
    ps = eq / s["fd_shares_y5"]
    r = (ps / price) ** (1 / 5) - 1 if ps > 0 else -1.0
    return dict(ev_bn=round(ev, 1), equity_bn=round(eq, 1), per_share=round(ps, 2), ann_return=round(r * 100, 1))

if __name__ == "__main__":
    data = json.load(open(sys.argv[1]))
    for t, d in data.items():
        print(t)
        for name, s in d["scenarios"].items():
            print("  ", name, run(s, d["price"]))
        # entry ceiling for a 20% base-case return
        b = run(d["scenarios"]["base"], d["price"])
        if b["per_share"] > 0:
            print("   base-case 20% entry ceiling:", round(b["per_share"] / 1.2 ** 5, 2))
