"""Route D return (framework C, revision 6 method, restated for projected dilution).

Usage: python3 d_return.py inputs.json
inputs.json: {"TICKER": {"price":..,"div_yield":0,"base_eps":..,"eps_path":[e1,e2,e3] or null entries,
                "consensus_shares":..,"fdso0":..,"fdso_growth":[g1,g2,g3,g4],"median_fwd_pe":null|x,
                "seed_growth":..}}
eps_path holds consensus EPS for the three FYs after the base year; null = fade (85% of prior growth).
fdso_growth: projected FDSO growth for base year, then each of the three following years.
"""
import json, sys

def growths(base, eps_path, seed):
    """Uncut yearly EPS growth: consensus where usable, else 85% of the prior year's growth."""
    out, prev_g, e = [], seed, base
    for x in eps_path:
        g = (x / e - 1) if x is not None else 0.85 * prev_g
        out.append(g)
        e *= 1 + g
        prev_g = g
    return out

def path(base, eps_path, seed, cut=0.0):
    out, e = [], base
    for g in growths(base, eps_path, seed):
        e *= 1 + g - cut
        out.append(e)
    return out

def d_return(d, cut=0.0, restate=True):
    price, base = d["price"], d["base_eps"]
    eps = path(base, d["eps_path"], d["seed_growth"], cut)
    shares = d["fdso0"]
    hair = [1.0]
    for g in d["fdso_growth"]:
        shares *= 1 + g
        hair.append(min(1.0, d["consensus_shares"] / shares) if restate else 1.0)
    base_r = base * hair[1]
    exit_eps = eps[-1] * hair[4]
    cagr = (exit_eps / base_r) ** (1 / 3) - 1
    entry = price / base_r
    cap = 35.0 if cagr >= 0.25 else 30.0
    exit_mult = min(entry, cap)
    if d.get("median_fwd_pe"):
        exit_mult = min(exit_mult, d["median_fwd_pe"])
    r = (exit_eps * exit_mult / price) ** (1 / 3) - 1 + d.get("div_yield", 0.0)
    return dict(entry=round(entry, 2), exit_mult=round(exit_mult, 2), base_eps=round(base_r, 3),
                exit_eps=round(exit_eps, 3), eps_cagr=round(cagr * 100, 1), ret=round(r * 100, 1))

if __name__ == "__main__":
    data = json.load(open(sys.argv[1]))
    for t, d in data.items():
        print(t, "base", d_return(d), "| stress -5pt", d_return(d, cut=0.05),
              "| no dilution restatement", d_return(d, restate=False))
