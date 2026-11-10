"""Recovery-board scorer (revision 21). See references/recovery-board.md.

Score = 50% quality + 25% asymmetry + 25% speed (12-month return), then the
bear penalty, PB / IX / PO points and the GP gate-fail penalty. Cyclical names at
a peak are scored on through-cycle numbers (CG cycle guard, revision 20) and lose CW
cycle-warning points; names up more than 25% this year lose YT points (revision 21).
Distance to the high only decides the universe (15% minimum) and the dead-money cut.

Usage:
    from recovery_score import score
    score(price=135.34, high=302.52, target=284.05, eg=82.35, opm=31.74,
          ocf_margin=31.45, fcf_margin=27.57, roic=38.21, debt_ebitda=0,
          rev90=0.0875, d=.15, bear=.40)
"""
import math
import statistics

LINE = 4.46        # fixed Nov 4, 2026: UBER's post-print score (4.51) less the 0.05 band
MAX_YEARS = 2.7    # fixed Nov 4, 2026: CRDO (2.68 years) sets the dead-money line
SPEED_TOP = 75.0   # 12-month return (%) that earns the full 10 speed points
DEEP = 0.35        # drawdown past which an analyst target needs rising estimates
NOISE = -0.02      # estimate dips smaller than 2% don't raise the risk discount
CG_TRIGGER = 2.0   # cycle guard: current ROIC at least this multiple of its 20-reading average
CG_FLOOR = 0.25    # cycle guard: mid-cycle EPS is never cut below 25% of NTM EPS
CW_WARN = 1.5      # cycle warning: ROIC at least this multiple of its average costs CW_WARN_PTS
CW_WARN_PTS = -1.0
CW_HOT_PTS = -1.5  # at the CG trigger (2x, or average <= 0)
YT_TIERS = ((1.00, -2.0), (0.50, -1.5), (0.25, -1.0))  # YTD price return above x -> points


def _lin(x, lo, hi):
    return max(0.0, min(10.0, 10.0 * (x - lo) / (hi - lo)))


def quality(eg, opm, ocf_margin, fcf_margin, roic, debt_ebitda, rev90, net_cash=None):
    """Six factors, 0-10 each, averaged. Percent inputs in percent; rev90 as a fraction.

    eg: consensus 3-year EPS growth forecast; opm: TTM operating margin;
    cash = average of TTM OCF and FCF margins, capped at operating margin + 10 points
    (stops customer prepayments, e.g. GEV, from passing as quality); roic: stockanalysis
    method (EBIT after actual tax over average debt + equity - cash); debt_ebitda: stockanalysis
    Debt / EBITDA (0 when there is no debt); rev90: 90-day change in next-year consensus EPS
    (None = no data, scored neutral); net_cash: stockanalysis Net Cash ($B). Positive net cash
    scores the debt factor 10 (Nov 4 addendum: convert cash sitting on the balance sheet
    is not leverage).
    """
    cash = min((ocf_margin + fcf_margin) / 2, opm + 10)
    f = {
        "growth": _lin(eg, 0, 30) if eg is not None else None,
        "margin": _lin(opm, 0, 40),
        "cash": _lin(cash, 0, 30),
        "roic": _lin(roic, 0, 30) if roic is not None else None,
        "debt": 10.0 if (debt_ebitda <= 0.5 or (net_cash is not None and net_cash > 0))
        else _lin(4.0 - debt_ebitda, 0, 3.5),
        "revisions": _lin(rev90 * 100, -10, 10) if rev90 is not None else 5.0,
    }
    vals = [v for v in f.values() if v is not None]
    return sum(vals) / len(vals), f


def score(price, high, target, eg, opm, ocf_margin, fcf_margin, roic, debt_ebitda,
          rev90=None, ntm_eps=None, fpe_hist=None, d=0.15, bear=0.25,
          pb=0.0, ix=0.0, po=0.0, max_years=MAX_YEARS, net_cash=None, guide_below=False, gp=0.0,
          cycle=None, ye_close=None):
    """Return the final score and its parts, or the reason the name is off the board.

    guide_below: True when the latest guidance midpoint (revenue, EPS or EBITDA) came in more than
    3% below consensus at the print (GD gate, revision 18); names that give no numeric guidance pass.
    gp: gate-fail penalty (revision 19), the sum of tier points for verified fails on the name's best
    route: -0.25 minor, -0.5 moderate, -1.0 severe, capped at -1.5. See recovery-board.md.
    cycle: cycle-guard inputs (revision 20) for names in cyclical industries (memory and storage,
    semiconductor equipment and foundry, commodity producers): dict(roic_now, roic_avg) from the
    stockanalysis quarterly ratios ROIC row (latest reading and the average of the latest 20), plus
    opm_avg, ocf_avg, fcf_avg (simple averages of the last five fiscal-year margins). When roic_now is at
    least 2x roic_avg (or roic_avg <= 0), k = max(0.25, roic_avg / roic_now): ROIC is scaled by k, the
    margin and cash factors use the five-year averages, and NTM EPS in the multiple leg is scaled by k.
    CW (revision 21): the same ratio sets cycle-warning points: -1.0 at 1.5x, -1.5 at the 2x trigger (or
    average <= 0). cycle["rescore"] = False applies CW without the CG rescoring (booking-cycle names:
    power and electrical equipment, construction contractors; annual readings, see recovery-board.md).
    ye_close: prior year-end close. YT (revision 21): YTD price return = price / ye_close - 1; above 25%
    -1.0, above 50% -1.5, above 100% -2.0.
    ntm_eps + fpe_hist (the last 20 quarterly forward P/Es) give the multiple leg;
    leave them None when there is no usable 5-year history (spin-offs, loss years).
    """
    if guide_below:
        return {"excluded": "guide-down: latest guidance midpoint below consensus (out until the next print)"}
    cg = None
    cw = 0.0
    if cycle:
        now, avg = cycle["roic_now"], cycle["roic_avg"]
        if avg <= 0 or now >= CG_TRIGGER * avg:
            cw = CW_HOT_PTS
            if cycle.get("rescore", True):
                cg = CG_FLOOR if avg <= 0 else max(CG_FLOOR, min(1.0, avg / now))
                roic = roic * cg
                opm, ocf_margin, fcf_margin = cycle["opm_avg"], cycle["ocf_avg"], cycle["fcf_avg"]
                if ntm_eps:
                    ntm_eps = ntm_eps * cg
        elif now >= CW_WARN * avg:
            cw = CW_WARN_PTS
    ytd = price / ye_close - 1 if ye_close else None
    yt = next((pts for cut, pts in YT_TIERS if ytd is not None and ytd > cut), 0.0)
    below = 1 - price / high
    if below < 0.15:
        return {"excluded": "less than 15% below the high", "below": round(below, 3)}
    g = min(0.35, (eg if eg is not None else 35.0) / 100)
    years = math.log(high / price) / math.log(1 + g)
    if years > max_years:
        return {"excluded": f"dead money: {years:.2f} years to the high at consensus growth",
                "years": round(years, 2)}

    q, factors = quality(eg, opm, ocf_margin, fcf_margin, roic, debt_ebitda, rev90, net_cash)

    # Fair value 12 months out: half revision-adjusted target, half multiple-based value.
    tgt = target * (1 + rev90) if (rev90 is not None and rev90 < 0) else target
    use_target = not (below > DEEP and not (rev90 is not None and rev90 > 0))
    mult12 = fair_pe = None
    if ntm_eps and fpe_hist:
        fair_pe = min(statistics.median(fpe_hist), 2 * (eg if eg is not None else 35.0))
        mult12 = ntm_eps * fair_pe * (1 + g)
    if mult12 is not None:
        fv12 = 0.5 * tgt + 0.5 * mult12 if use_target else mult12
    elif use_target:
        fv12 = tgt
    else:
        return {"excluded": "no fair value: deep drawdown without rising estimates, no P/E history",
                "below": round(below, 3)}
    fv0 = fv12 / (1 + g)

    dd = d + 0.10 if (rev90 is not None and rev90 <= NOISE) else d
    up0 = fv0 / price - 1
    up12 = fv12 / price - 1
    asym = max(0.0, min(10.0, 3 * up0 * (1 - dd) / bear))
    speed = _lin(up12 * 100, 0, SPEED_TOP)
    bear_pen = 0.25 * max(0.0, (bear * 100 - 15) / 10)
    pb = min(pb, 0.3)
    ix = min(ix, 0.2)
    po = max(-0.2, min(0.2, po))
    gp = max(-1.5, min(0.0, gp))
    final = 0.5 * q + 0.25 * asym + 0.25 * speed - bear_pen + pb + ix + po + gp + cw + yt
    return {
        "final": round(final, 2), "on_board": final >= LINE, "quality": round(q, 2),
        "asym": round(asym, 2), "speed": round(speed, 2), "ret_12m": round(up12, 3),
        "fair_value_12m": round(fv12, 2), "fair_pe": fair_pe and round(fair_pe, 1),
        "target_used": use_target, "years": round(years, 2), "below": round(below, 3),
        "factors": {k: (round(v, 1) if v is not None else None) for k, v in factors.items()},
        "pb": pb, "ix": ix, "po": po, "gp": gp, "cg": cg and round(cg, 3),
        "cw": cw, "yt": yt, "ytd": ytd if ytd is None else round(ytd, 3),
        "bear_penalty": round(-bear_pen, 2), "_raw": final,
    }
