---
name: asymmetry-gates
description: Tony's equity screen for core stocks, durable compounders, milestone-based early businesses and a separate power/commodity signal sleeve, with stricter fintech standards. Use for stock screens, re-tests, rankings, gate checks, capital eligibility, sizing, kill triggers, entry blackouts, roster upkeep and framework edits; also when reviewing pasted stock analyses or evaluating a theme-led investment case.
---

# Asymmetry Gates

A rules-based screen for finding investable opportunities while surviving the name you're wrong about. A–E preserves strict core quality; G evaluates proven compounders on per-share economics; H admits only small, funded early transitions with a fixed quality destination. Fintech receives stricter treatment. PH makes prolonged price underperformance affect capital eligibility even when fundamentals pass. Every position carries written, numeric kill triggers before it gets capital. Assess both the opportunity and the risk; passing a gate needs no additional invented hurdle, and an empty shortlist is acceptable when the evidence warrants it. A durable theme merits research, not an assumption of indefinite stock-price growth.

## Files

- `references/framework.md` — the rules (sources, A–F, #1–#19). Read first, every time. Don't paraphrase gates from memory; the thresholds are exact.
- `references/triggers.md` — written #15 kill triggers per name, plus the shared "AI capex 2027" factor trigger. Read before ranking or adding capital.
- `references/roster.md` — dated roster: status of every name, current top-10, what changed. Read when the user asks about a held or previously screened name; update it at the end of every screen.
- `references/changelog.md` — #18 rule-change log: adopted changes with dates, pending proposals with rationale. Read whenever a rule change or interpretation comes up.
- `references/stage-paths.md` — full G/H substitution, valuation, funding, sizing, milestone and promotion tests. Read for compounder or early-transition candidates.
- `references/fintech.md` — stricter FT routing, growth, normalized cash and financial-risk checks. Read first for fintech/payments and material embedded finance.
- `references/price-health.md` — closing ATH age, drawdown, benchmark-relative returns and sustained recovery tests. Read every screen; a stale impaired chart can block new capital.

## Source of truth and sync

The bundled `references/` files are a snapshot. The live copy is the GitHub repo (`github.com/CyberFvde/asymmetry-gates`, skill at `.claude/skills/asymmetry-gates/`; change the path here if the repo lives elsewhere).

- Start of a screen: if a GitHub tool or fetch is available, read the repo's `framework.md`, `roster.md`, `triggers.md` and `changelog.md`, plus the selected route's supporting files. Use the live reference set if its framework is at least as recent as the bundled version, comparing same-day revision markers/changelog rather than dates alone. If the live framework is older, use the newer bundled reference set and state that the live rules need syncing; do not roll back a calibration or mix incompatible versions. If no fetch is available, use the bundled copies. State the chosen framework version, source and roster header date. A roster from an older framework is historical evidence, not a current verdict; re-test before changing status or sizing.
- End of a screen: if a GitHub tool is available and the live repo contains the chosen framework, commit the updated `roster.md` (plus `triggers.md`/`changelog.md` if they changed) with a message like `roster: Sep 23 re-test — MU 3(c) cleared`. Otherwise output each changed file in full so the user can sync it; never output a partial diff of the roster or overwrite live files using an incompatible ruleset. Reconcile any newer live roster evidence before syncing.
- `framework.md` and route/overlay rule changes require a #18 changelog entry; commit changed rules and the log together.
- Two models share this repo. Don't overwrite a roster whose header date is newer than the data you're holding — re-read, then merge.

## How to run a screen

1. Load `framework.md` and `price-health.md`. Identify sector and stage before applying gates: FT overlay first for fintech; F for levered power/IPPs and commodity names; A–E for strict core; G for an evidenced, cash-generating compounder; H for a funded early transition. Read the selected supporting file. Prefer A–E when it qualifies; never use G/H to evade FT/F/PH routing or an unidentified failure.
2. Pull data in this order of preference: Capital IQ consensus via the S&P connector for NTM OCF/FCF/capex/margins; stockanalysis Statistics and Forecast pages for fwd P/E, PEG, 3Y CAGRs, next-FY estimates, PT and analyst count; company guidance only as a fallback, flagged. Non-US listings are screenable through stockanalysis quote pages (e.g. `quote/krx/005930`). Search for the latest print vs consensus separately — #19 can't be run from a statistics page.
3. For A–E, run A → B → C → D and stop that route at the first A fail. Record its reason; do not waive it. If the business belongs to G/H, run that entire route independently and disclose which core tests it substitutes; a first-failure roster entry never proves the other gates passed. F follows F1–F5; FT applies its additional checks without a lenient-route bypass.
4. Run #19 on the most recent print (revenue vs consensus, adjusted EPS/EBITDA vs consensus, own-guidance low end or midpoint if no range, next-quarter guide vs consensus), using current materiality. H uses its documented revenue, cash-burn and milestone substitutions when earnings comparisons are meaningless; F uses F3's sector metrics. If the next print is inside five trading days, re-test after it, not before.
5. Classify A–E as **core**, **conditional core** (named missing evidence, zero capital), **waiver** (#10), **ballast** (only #12 fails), **starter** (#14a), **unresolved starter**, **alert**, **blackout** or **out**. Separately classify **G-compounder/G-watch** and **H-early/H-watch**; watch means zero new capital. Append the PH verdict: warning, impaired, recovery or unverified when applicable; PH-impaired/unverified blocks capital and removes the name from the investable ranking. H is speculative, never core before actual graduation evidence. Fintech shortfalls receive no funded starter. Treat minor misses as watch items; missing required evidence is unresolved rather than silently passed.
6. Before capital: verify written #15 company/factor triggers and cap headroom. For A–E/G/H, #16 name caps remain 25% of sleeve at cost/10% of portfolio; relevant AI-capex exposure remains ≤50%/20% in aggregate. #14a starters use ≤2.5%/0.5% per name, max two/5% of sleeve total. G/H use their smaller initial/total caps in `stage-paths.md`; combined starters/G/H plus A–E PH-recovery positions ≤20% of sleeve at cost AND ≤4% of portfolio, counting each position once. F uses its own separate caps/F5 accounting. Unknown headroom blocks capital. Core, starter, G and H additions must satisfy their specific print/checkpoint conditions; route switches retain cost basis.
7. Rank verified, PH-eligible core/waiver/ballast by gate strength and asymmetry; show G compounders, capped starters and speculative H names separately, then unresolved/watch names. Show PH-impaired names as turnaround watch items with numeric recovery conditions. Apply the user's lower fintech priority among otherwise comparable qualifiers. Don't rank an unverified projection above verified evidence. State what unlocks or expands capital, and distinguish eligibility from a trade instruction.
8. Update `roster.md` with the date and a "what changed" block. Never change a rule inside a screen — propose it in `changelog.md` under #18.

## Things that go wrong (learned the hard way)

- "Next-FY" is the fiscal year after the last completed one. A June-FYE company reporting in July has FY+1 as next-FY, not FY+2. Check the forecast table's period-ending dates.
- The stockanalysis Forecast table's historical "Free Cash Flow" row uses a narrower definition than OCF − cash PP&E (it ran ~$1B/yr low for KLAC, roughly dividends paid). Use the Statistics page or the company's cash-flow statement for trailing FCF, and don't compare the FY+1 estimate to the forecast row's history 1:1.
- Post-split numbers: KLAC (10:1, Jun 2026) and LRCX (10:1, Oct 2024) report small per-share figures. Sanity-check EPS against revenue and share count before calling a miss.
- Convert-for-equity exchanges and contingent stock earnouts are issuance under core A1. G/H instead require their disclosed maximum dilution, funding and per-share tests; issuance alone never establishes qualification there.
- JV-funded fabs (SNDK/Kioxia) keep cash PP&E artificially low. The gate stays cash PP&E; JV commitments and guarantees go into #4 at disclosed maximum and JV-inclusive capex goes into #15.
- Conflicting forward P/E across sources (AMD: 42.6 vs 32.5; VRT: 33–43): stockanalysis governs. Say so rather than picking the friendlier number.
- For jurisdictions without 10b5-1, verify insider trades through applicable local and SEC filings; missing insider evidence remains unfunded. Read transaction codes and footnotes: required sell-to-cover, issuer withholding and gifts are not discretionary conviction signals.
- A big pullback is not an entry signal and a big run is not an exit signal. Price enters core #11/#12, #14a's narrow band, G/H's per-share valuation, PH's sustained underperformance/recovery checks and #16's trim rule. For early businesses, contracts, cash runway and achieved milestones matter more than sector enthusiasm. Never give an impaired multi-year chart a clean capital verdict from fundamentals alone.
- When the user pastes someone else's table, verify the numbers before ranking on them; two of the last three pastes mislabeled next-FY growth or used an unsourced sector figure.

## Output format

Lead with the verdict, then the gate detail, then the ranking. Keep it phone-readable.

```
**[TICKER / COMPANY] — [route + status + PH]** One-line verdict. Why it could work; verified facts versus forecasts; material failures or watch items; numeric entry ceiling and eligible size; what unlocks capital. PH: ATH date/age, drawdown, benchmark return gap and recovery checks. For H: funded runway, maximum dilution, next milestone and fixed quality deadline. For FT: normalized cash/risk check. Next catalyst.

**Ranking (gate strength first, then C-metrics)**
1. TICKER — status; 2–3 numbers that decide the slot.
...

**Starters / watchlist:** ticker (shortfall, eligible size or missing evidence, numeric next step), ...
**Compounders / early transitions:** ticker (G/H verdict and route-specific evidence), ...
**Outside the list:** ticker (material gate that fails), ...
Standing caveat (concentration, shared trigger) if relevant.
```

Cite the figures you pulled. Never say a name "decided" or "chose" anything based on a prior assistant suggestion — check the human's own words in past chats before attributing a decision.
