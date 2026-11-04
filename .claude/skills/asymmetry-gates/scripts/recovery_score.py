"""Recovery-board scorer (revision 16). See references/recovery-board.md.

Usage:
    from recovery_score import score
    score(price=135.34, high=302.52, target=284.05, d=.15, bear=.40, g=.35,
          fpe_now=18.6, fpe_at_high=41)
"""
import math


def score(price, high, target=None, d=0.15, bear=0.25, g=0.20,
          fpe_now=None, fpe_at_high=None, force=None,
          pb=0.0, ix=0.0, po=0.0, penalty_k=0.15):
    """Return a dict with the final score and its parts, or the exclusion reason."""
    below = 1 - price / high
    to_high = high / price - 1
    if below < 0.15:
        return {"excluded": "less than 15% below the high", "below": below}
    g = min(g, 0.35)
    years = math.log(1 + to_high) / math.log(1 + g)
    if years > 5:
        return {"excluded": "more than 5 years to the high", "years": years}

    # Target weight: full target at 15% below, full high at 25%, blended between.
    w = min(1.0, max(0.0, (0.25 - below) / 0.10))
    if fpe_now and fpe_at_high and fpe_at_high / fpe_now > 2:
        w = 1.0
    if force == "target":
        w = 1.0
    elif force == "record":
        w = 0.0
    t_up = (target / price - 1) if target else to_high
    upside = w * t_up + (1 - w) * to_high
    disc = w * max(0.20, d) + (1 - w) * d

    asym = min(10.0, max(0.0, 3 * upside * (1 - disc) / bear))
    time_pts = max(0.0, 10 - 2 * years)
    bear_pen = 0.25 * max(0.0, (bear * 100 - 15) / 10)
    base = (asym + time_pts) / 2 - bear_pen
    time_pen = penalty_k * max(0.0, years - 1) ** 2
    pb = min(pb, 0.3)
    ix = min(ix, 0.2)
    po = max(-0.2, min(0.2, po))
    final = base - time_pen + pb + ix + po
    return {
        "final": round(final, 2), "base": round(base, 2), "asym": round(asym, 2),
        "time": round(time_pts, 2), "years": round(years, 2), "upside": round(upside, 3),
        "w": round(w, 2), "time_penalty": round(-time_pen, 2), "pb": pb, "ix": ix, "po": po,
        "dm_2yr": years > 2,
    }


if __name__ == "__main__":
    # Nov 4, 2026 intraday examples
    print("AVGO", score(327.88, 481.57, d=.10, bear=.25, g=.3688, force="record", pb=.1, ix=.1))
    print("CRDO", score(135.34, 302.52, 284.05, d=.15, bear=.40, g=.35, fpe_now=18.6, fpe_at_high=41))
