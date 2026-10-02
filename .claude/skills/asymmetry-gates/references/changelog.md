# #18 — Rule-change log

Rule changes normally take effect at a scheduled or post-print re-test; an explicit user request can authorize calibration between re-tests. Record the change, rationale, safeguard check, universe impact and adoption basis. Apply changes to the full relevant universe and re-screen before upgrading any name. Earlier entries retain the historical #18 checks that applied at their adoption. Pending items are proposals — they bind nothing until adopted.

## Adopted configuration — Oct 2, 2026 (user-requested balanced calibration)

Authorization and timing: the user explicitly requested a slightly more lenient stock skill because the screen was too negative. This authorizes a framework calibration now and supersedes the prior timing restriction and failing-name veto for this edit. Policy adoption is not a market-data re-test or trade authorization. `roster.md` remains the Sep 28 evidence snapshot; use current data at the next screen before changing any status or tranche eligibility.

Changes (old → new):

- #9: next-FY organic growth ≥15% → ≥12%; fwd 3Y revenue CAGR ≥15% retained. A modest near-term slowdown need not invalidate a durable growth profile.
- #11/#14: every #9/#11 shortfall meant zero capital → an optional starter for exactly one narrow failed gate with all of A verified, #12/#13 passed and #19 clear. #9 starter floors: 3Y ≥12%, next-FY organic ≥10%. #11 starter: exactly one component may miss, bounded by P/E ≤40, PEG ≤2.25 or FCF yield ≥1.25%; the other two must meet full-core thresholds. Core valuation and #10 unchanged.
- #14/#16: min 5% of sleeve → 5% standard target with smaller entry tranches; starters exempt, capped at ≤2.5% of sleeve at cost AND ≤0.5% of portfolio per name, max two and ≤5% of sleeve in aggregate. All existing name/factor caps remain. Starter is tranche 1; no scaling until full qualification and the next clean print. This permits a measured entry without turning every near-pass into a full position.
- #17: two consecutive estimate cuts → materiality applies to both (>5% in the same metric), additions freeze and full re-test. Exit on a breached hard gate or written exit condition; otherwise monitor using the affected estimate as a numeric stabilization baseline. Adds resume only after a later print confirms eligibility and the estimate is at or above that baseline. Smaller cumulative cuts >5% still trigger review. Avoid automatic exits driven solely by ordinary estimate adjustments.
- #18: currently failing names and named historical exclusions could veto a class-wide change → written safeguard and universe-impact checks, with an explicit user-requested calibration path. Keep F routing and prohibit one-name waivers or mid-screen rule edits to obtain a preferred verdict.
- #19: revenue miss >1% → >2%; adjusted EPS/EBITDA miss >1% → >3%; any own-midpoint miss → below guidance low end, or >1% below midpoint if no range; next-quarter guide miss >2% → >3%. Lesser misses become documented watch items. Material misses still block entry; two consecutive material-miss prints still exit held names.
- Sync `SKILL.md` and gate-linked trigger instructions to the revised framework. Preserve standalone per-name exit thresholds, pending P7/P8 and historical evidence. Explain the positive case alongside risks, fetch the live framework as well as its supporting files, and prevent an older live version from rolling back a newer bundled calibration. Label an unverified near-pass "unresolved starter" with zero capital until evidence closes.

Rationale: the hard structural floors already exclude weak cash engines and excessive leverage. Combining them with zero tolerance for small quarterly misses and zero-capital near-passes can exclude otherwise qualified opportunities without distinguishing the severity of a shortfall. The change makes limited imperfections actionable at limited size while preserving the reasons to reject a structurally weak business. The numeric bands express the user's risk preference; they are not backed by a new performance study or backtest.

#18 safeguard check: A1–A8, the 6% trailing FCF-margin floor, leverage/guarantee accounting, #10, full-core #11 thresholds, written #15 exits, existing #16 name/factor caps and all F rules are unchanged. Unverified A evidence, unknown cap headroom, material #19 misses, simultaneous #9/#11 failures, multiple #11-component failures and #10-only shortfalls cannot receive starter capital. Two starters together consume at most 5% of sleeve at cost and 1% of total portfolio, within existing caps.

#18 universe-impact check: growth and valuation near-passes and names with minor quarterly misses may change eligibility on fresh evidence; apply the same bands to every relevant name, including prior exclusions. FN/CLS/FPS still cannot bypass A's cash-flow/quality floors, and CEG/VST and other levered power/IPPs still route to F. A past A-fail is not cleared by this edit. Historical ANET/HWM-type valuation alerts may merit a starter review, but no ticker is promoted here. Counterexamples: P/E 38 with otherwise clean #11 can be starter-eligible; P/E 38 plus PEG 2.2 cannot; net debt/NTM FCF 2.7× remains out; any below-low-end guidance miss remains a blackout. These are illustrative policy cases, not current screens.

Adoption re-test: the configuration is effective Oct 2 under explicit user direction. At the next full-universe screen, verify current A, growth/valuation data, all #19 comparisons, written triggers and portfolio headroom, then update the roster's date and "what changed" block. No current-stock reclassification is claimed by this calibration.

## Adopted — Sep 3, 2026

- #16: hard 25%-of-sleeve-at-cost / 10%-of-portfolio cap; 35% run / 30% trim rule; three-tranche entries tied to re-tests; "exits by gates only, never by price level" made explicit. Rationale: bound the tail of the one you're wrong about without selling compounding.
- #4: off-balance-sheet guarantees, residual-value guarantees and vendor financing count as debt at disclosed maximum exposure. Rationale: AVGO's XPV platform exposure.
- AVGO #15: XPV guarantee, FY27 AI-target cut, GM <70% triggers added.
- Admissibility: no FN/CLS/FPS/CEG/VST readmission; no affected name failing the changed gates.

## Adopted — Sep 11, 2026 (all of P1–P5; P6 recorded)

Timing basis under #18: the Sep 8–11 screens were post-print re-tests of KLAC (Jul 28), AMAT (Aug 13), ADI (Aug 19) and NVDA (Aug 26), so adoption at this cycle is inside the rule. Rule text has been written into framework.md (A1, #7, #14, #16, Sources). Open action from adoption: measure the semi/AI-capex group's current cost basis against the 50%/20% cap before the next semi tranche; if over, the cap phases in through tranche freezes. P2 is adopted with Lyft excluded until it clears the 3Y-EPS-CAGR leg (second #18 check).

The proposals as written and adopted:

### P1. Aggregate factor cap (new rule, #16)

Change: semi/AI-capex names in aggregate ≤50% of the sleeve at cost and ≤20% of total portfolio. "Semi/AI-capex" = every name carrying the shared "AI capex 2027" trigger (currently AVGO, KLAC, AMAT; NVDA, ADI, LRCX, ASML, MU, Samsung, TSM on entry).

Rationale: the per-name caps bound single-name blowups; they don't bound the sleeve's exposure to one variable. Eight of the current top ten re-rate on the same 2027 WFE / hyperscaler-capex number. Without a group cap, a sleeve can be inside every #16 limit and still have 70%+ of cost basis on one factor. The shared #15 trigger says when the factor breaks; only a cap limits how much is exposed when it does.

#18 checks: does not readmit FN/CLS/FPS/CEG/VST (it only restricts). Affected names currently failing the gate being changed: none — verify current group cost basis vs the proposed 50%/20% before adoption; if the sleeve is already over, the cap phases in through tranche freezes rather than forced sales (exits stay by gates only).

Thresholds are proposals. The 50% number keeps room for UBER, APP-class and F-sleeve names; the 20% of total portfolio mirrors #16's 10%-per-name at 2×.

### P2. #8/#14 clarification — "#10-only" names

Change: a name routed "#10 only" by #8 that passes all of A and C and fails exactly one #10 leg is a #14 alert with that leg as the numeric trigger.

Rationale: #14 names #9 and #11 as the only provisional gates; for a name that can't use #9 at all, the equivalent single-gate fail is a #10 leg. Applied to Lyft (3Y EPS CAGR 19.64% vs 20%). Rejecting it makes Lyft "out" rather than "alert" — same capital (zero), different re-test cadence.

#18 checks: readmits nothing; Lyft is the only affected name and it is failing the gate (#10) — under a strict reading that blocks adoption while Lyft fails. Adopt as a universe-wide clarification with Lyft explicitly excluded until it clears the leg, or reject.

### P3. A1 clarification — earnouts and exchanges

Change: contingent consideration payable in shares is pending issuance while outstanding; convert-for-equity exchanges are issuance.

Rationale: closes the "the deal already closed" loophole (CRDO) and the "we reduced debt, not raised equity" loophole (LITE). Both are new shares in holders' hands.

#18 checks: readmits nothing; affected names (CRDO, LITE) are already failing A1 on other facts, so the clarification changes their roll-off dates, not their status.

### P4. #7 mapping for non-US filers

Change: where no 10b5-1 regime exists, #7 is verified through the local disclosure system (DART for Korea, TDnet for Japan, RNS for the UK); if unverifiable, the name is alert-only regardless of other gates.

Rationale: Samsung passes every numeric gate; the framework had no way to run #7 on it. This keeps the gate rather than waiving it.

#18 checks: readmits nothing; Samsung is currently unverified, not failing.

### P5. Sources — listings

Change: stockanalysis quote pages for non-US listings are an approved source for #11/#12 and share statistics; KRX consensus (or Capital IQ) for #19.

Rationale: the framework text implied US-only; the data exists and is on the same S&P feed.

#18 checks: readmits nothing; no name affected.

### P6. Shared factor trigger (no rule change — record only)

The "AI capex 2027" trigger in triggers.md is a #15 entry, not a rule change, and is in force from Sep 11, 2026 for every semi/AI-infra name at or before its next tranche. Recorded here so the anchors get re-confirmed at the October re-test.

## Pending — proposed Sep 28, 2026 (bind nothing until adopted)

### P7. UBER #15 AV trigger — numeric "at scale"

Change (#15 text, UBER and UBER-class): "AV operator direct at scale in a top-5 U.S. metro" → "an AV operator's own-app service in a top-5 U.S. metro (NYC, LA, Chicago, DFW, Houston) with ≥500 vehicles or ≥100k paid rides/week, or UBER Mobility GB growth in that metro <5% YoY for two quarters."

Rationale: read literally the trigger has been met since before entry (Waymo LA since 2024; Waymo Dallas/Houston Feb 2026; Tesla Dallas/Houston Apr 2026), so it fires every screen and carries no information. A trigger has to be numeric (#15).

#18 checks: #15 text, not a gate — readmits nothing; UBER passes every gate at the Sep 28 re-test. Adopt at the ~Nov 3 post-print re-test or reject.

### P8. AVGO #15 XPV trigger — threshold

Change: "contingent residual-value guarantees >10% of NTM FCF … → immediate re-test" → "XPV backstop plus customer convertible-note facility pushing #4 (at max) above 2.0×, any amount paid under the backstop, any convertible note issued to AVGO, or any new XPV tranche → immediate re-test."

Rationale: the disclosed backstop (~$29B on the first $35B tranche; BofA models $370B of guarantees by mid-2029) is already ~60% of FY26 FCF, so the 10% line is permanently tripped. #4 at max is the gate that actually binds (2.17× on Sep 28), so the trigger should sit just inside it.

#18 checks: #15 text, not a gate — readmits nothing; AVGO passes #4 at the Sep 28 re-test. Adopt at the ~Dec 9–10 post-print re-test or reject.

## How to log a change

1. Write the change as a rule edit (which number, old text → new text).
2. Rationale in two or three sentences, tied to a name or a failure mode.
3. Run the two current #18 checks explicitly: preserved safeguards and full-universe impact, including counterexamples and prior exclusions.
4. Set the adoption basis (scheduled quarterly, named post-print, or explicit user-requested calibration) and required fresh re-tests.
5. On adoption, move the entry to "Adopted" with the date and update framework.md.
