---
name: asymmetry-gates
description: Tony's multi-gate equity screening framework (gates A–F, rules #1–#19, F signal sleeve) for AI-infrastructure and asymmetry names — AVGO, UBER, NVDA, KLAC, AMAT, MU, Samsung and peers. Use this skill whenever the user asks to screen, re-test, rank, gate-check, or "run" a stock or list of stocks, asks whether a name "passes," "is in the club," is "Uber level or higher," or "worth looking at," asks about tranches, sizing, kill triggers (#15), entry blackouts (#19), roster updates, or rule changes (#18) — even if they never name the framework. Also use it when they paste stock numbers or someone else's analysis and ask "agree or disagree," and when a pullback or rally is offered as a reason to buy or sell (price never votes here; gates do).
---

# Asymmetry Gates

A rules-based screen. Its edge is surviving the name you're wrong about, so the structural gates (A) are hard, price never votes, and every position carries written, numeric kill triggers before it gets capital.

## Files

- `references/framework.md` — the rules (sources, A–F, #1–#19). Read first, every time. Don't paraphrase gates from memory; the thresholds are exact.
- `references/triggers.md` — written #15 kill triggers per name, plus the shared "AI capex 2027" factor trigger. Read before ranking or adding capital.
- `references/roster.md` — dated roster: status of every name, current top-10, what changed. Read when the user asks about a held or previously screened name; update it at the end of every screen.
- `references/changelog.md` — #18 rule-change log: adopted changes with dates, pending proposals with rationale. Read whenever a rule change or interpretation comes up.

## Source of truth and sync

The bundled `references/` files are a snapshot. The live copy is the GitHub repo (`github.com/CyberFvde/asymmetry-gates`, skill at `.claude/skills/asymmetry-gates/`; change the path here if the repo lives elsewhere).

- Start of a screen: if a GitHub tool or fetch is available, read the repo's `roster.md`, `triggers.md` and `changelog.md` and use them over the bundled copies. If not, use the bundled copies and state which version you used (the date in the roster header).
- End of a screen: if a GitHub tool is available, commit the updated `roster.md` (plus `triggers.md`/`changelog.md` if they changed) with a message like `roster: Sep 23 re-test — MU 3(c) cleared`. If not, output each changed file in full so the user can commit it; never output a partial diff of the roster.
- `framework.md` changes only through a changelog entry under #18; commit both in the same change.
- Two models share this repo. Don't overwrite a roster whose header date is newer than the data you're holding — re-read, then merge.

## How to run a screen

1. Load `framework.md`. Identify which rule-set applies: A–E for core names, F for the signal sleeve (levered power/IPPs and commodity names route to F, never A–E).
2. Pull data in this order of preference: Capital IQ consensus via the S&P connector for NTM OCF/FCF/capex/margins; stockanalysis Statistics and Forecast pages for fwd P/E, PEG, 3Y CAGRs, next-FY estimates, PT and analyst count; company guidance only as a fallback, flagged. Non-US listings are screenable through stockanalysis quote pages (e.g. `quote/krx/005930`). Search for the latest print vs consensus separately — #19 can't be run from a statistics page.
3. Run gates in order A → B → C → D and stop at the first A fail. A-fails are never provisional and no valuation case reopens them.
4. Run #19 on the most recent print (four legs: revenue vs consensus, adjusted EPS/EBITDA vs consensus, own-guidance midpoint, next-quarter guide vs consensus). If the next print is inside five trading days, re-test after it, not before.
5. Classify: **core** (passes A–C, #9 standard), **conditional core** (passes on headline numbers with named open items — zero capital until they close), **waiver** (#10), **ballast** (fails only #12), **alert** (#14 — fails exactly one of #9/#11, numeric trigger, zero capital), **blackout** (#19), **out**.
6. Before any tranche: confirm the name's #15 triggers are written in `triggers.md`, confirm the shared factor trigger is applied if it's a semi/AI-capex name, and check #16 caps: 25% of sleeve at cost and 10% of portfolio per name, and the aggregate cap for semi/AI-capex names (≤50% of sleeve at cost, ≤20% of portfolio, adopted Sep 11, 2026).
7. Rank by gate strength first (verified core → conditional core → waiver → alert → out), asymmetry (C-metrics) second. State what unlocks capital for anything conditional.
8. Update `roster.md` with the date and a "what changed" block. Never change a rule inside a screen — propose it in `changelog.md` under #18.

## Things that go wrong (learned the hard way)

- "Next-FY" is the fiscal year after the last completed one. A June-FYE company reporting in July has FY+1 as next-FY, not FY+2. Check the forecast table's period-ending dates.
- The stockanalysis Forecast table's historical "Free Cash Flow" row uses a narrower definition than OCF − cash PP&E (it ran ~$1B/yr low for KLAC, roughly dividends paid). Use the Statistics page or the company's cash-flow statement for trailing FCF, and don't compare the FY+1 estimate to the forecast row's history 1:1.
- Post-split numbers: KLAC (10:1, Jun 2026) and LRCX (10:1, Oct 2024) report small per-share figures. Sanity-check EPS against revenue and share count before calling a miss.
- Convert-for-equity exchanges (LITE, 2026) and contingent stock earnouts (CRDO/DustPhotonics) are issuance under A1. SBC-driven WASO growth is tested by the ≤0.5% number, not by the issuance clause.
- JV-funded fabs (SNDK/Kioxia) keep cash PP&E artificially low. The gate stays cash PP&E; JV commitments and guarantees go into #4 at disclosed maximum and JV-inclusive capex goes into #15.
- Conflicting forward P/E across sources (AMD: 42.6 vs 32.5; VRT: 33–43): stockanalysis governs. Say so rather than picking the friendlier number.
- Non-US filers have no 10b5-1 regime. Verify #7 through local filings (DART for Korea); if it can't be verified, the name is alert-only.
- A big pullback is not an entry signal and a big run is not an exit signal. The only price-aware rules are #11/#12 (forward multiples, PT vs 200DMA) and the 35%/30% trim rule in #16.
- When the user pastes someone else's table, verify the numbers before ranking on them; two of the last three pastes mislabeled next-FY growth or used an unsourced sector figure.

## Output format

Lead with the verdict, then the gate detail, then the ranking. Keep it phone-readable.

```
**[TICKER] — [status]** One-line verdict. Passing gates by number with the key figures; failing or thin gates named with the number and threshold; open items and what closes them; next catalyst.

**Ranking (gate strength first, then C-metrics)**
1. TICKER — status; 2–3 numbers that decide the slot.
...

**Outside the list:** ticker (gate that fails), ...
Standing caveat (concentration, shared trigger) if relevant.
```

Cite the figures you pulled. Never say a name "decided" or "chose" anything based on a prior assistant suggestion — check the human's own words in past chats before attributing a decision.
