"""Run the board through the SL lens from a dated data pull (CSV). Added Nov 19, 2026.

Usage:  python3 board_from_pull.py <pull.csv> [--lens csv]

CSV columns (NA = not found; missing values fall back to the Nov 6 inputs in the repo and print as stale):
  ticker, price, price_date, ye_close, high, target, eps_next_now, eps_next_90d, fwd_pe, pe_price, eg, opm,
  ocf_margin, fcf_margin, roic, debt_ebitda, net_cash, guide_gap_pct, fpe_est, ai, e1, e2, notes
- high: the 10-year closing high. When given it replaces the stored one.
- rev90 = eps_next_now / eps_next_90d - 1 (same fiscal year for both).
- NTM EPS = pe_price / fwd_pe, where pe_price is the price the forward P/E was computed at (price if blank).
- guide_gap_pct below -3 sets the guide-down gate.
- fpe_est: a sourced normal forward P/E for a name with no 20-quarter history. Stress cases only.
- ai, e1, e2: lens inputs. Used only with --lens csv, each on its own where given; anything left NA keeps the
  estimate in board_2026_11_19_lens.py.
"""
import contextlib
import csv
import io
import sys

with contextlib.redirect_stdout(io.StringIO()):
    import board_2026_11_19_lens as b
from recovery_score import LINE, cc_points, return_estimate


def num(x):
    try:
        return float(str(x).replace(",", "").replace("$", "").replace("%", ""))
    except Exception:
        return None


def main(path, lens_from_csv=False):
    rows = {r["ticker"].strip().upper(): r for r in csv.DictReader(open(path))}
    out = []
    for k in ["TSM"] + b.BOARD:
        base = dict(b.TSM) if k == "TSM" else dict(b.NOV6[k], **b.LATER.get(k, {}))
        r = rows.get(k, {})
        stale = []
        for f in ("price", "target", "ye_close", "high", "eg", "opm", "ocf_margin", "fcf_margin", "roic",
                  "debt_ebitda", "net_cash"):
            v = num(r.get(f))
            if v is None:
                stale.append(f)
            else:
                base[f] = v
        a, c = num(r.get("eps_next_now")), num(r.get("eps_next_90d"))
        if a and c:
            base["rev90"] = a / c - 1
        else:
            stale.append("rev90")
        pe = num(r.get("fwd_pe"))
        if pe:
            base["ntm_eps"] = (num(r.get("pe_price")) or base["price"]) / pe
        else:
            stale.append("fwd_pe")
        g = num(r.get("guide_gap_pct"))
        if g is not None:
            base["guide_below"] = g < -3.0
        if "cc" not in base and k in b.CC6:
            base["cc"] = cc_points(**b.CC6[k])
        re_args = dict(b.TSM_RE) if k == "TSM" else (dict(b.RE6[k], fpe_hist=base.get("fpe_hist")) if k in b.RE6 else None)
        if re_args:
            if k == "TSM":
                re_args["entry_pe"] = base["price"] / (a or 23.39)  # 2027 EPS in USD (Yahoo); 23.39 on Nov 19
            base["re_ret"] = return_estimate(base["price"], **re_args)["ret"]
        saved = b.LENS[k]
        ai, e1, e2 = num(r.get("ai")), num(r.get("e1")), num(r.get("e2"))
        src = "repo"
        if lens_from_csv and (ai, e1, e2) != (None, None, None):
            # Each sourced value replaces the repo estimate on its own; the others stay as recorded.
            b.LENS[k] = tuple(v if v is not None else old for v, old in zip((ai, e1, e2), saved))
            src = "csv"
        fpe_est = num(r.get("fpe_est")) or (19.0 if k == "TSM" else None)
        res = b.run(k, base, re_args=re_args, fpe_est=fpe_est, keep=(k == "GOOGL"))
        b.LENS[k] = saved
        out.append((k, base["price"], r.get("price_date", "NA"), res, stale, src))
    key = lambda x: -(x[3]["semi"].get("_raw", -99))
    print(f"Line {LINE}. * = under the line. Sorted by the rates + SemiAnalysis column. Lens inputs: "
          f"{'CSV where given, else repo' if lens_from_csv else 'repo estimates'}.")
    print("Columns: today | +rates | +SemiAnalysis | +capex peak")
    for k, px, dt, res, stale, src in sorted(out, key=key):
        why = "" if "final" in res["today"] else " [" + res["today"]["excluded"] + "]"
        tag = (" lens:csv" if src == "csv" else "") + (f"  stale: {','.join(stale)}" if stale else "")
        print(f"{k:5} ${px:<9} {dt:<8} " + " | ".join(b.cell(res[c]) for c in b.CASES) + why + tag)


if __name__ == "__main__":
    main(sys.argv[1], lens_from_csv="--lens" in sys.argv)
