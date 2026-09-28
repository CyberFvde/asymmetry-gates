# #18 — Rule-change log

Rule changes take effect only at a scheduled or post-print re-test, with written rationale, applied to the full universe. Each entry records: the change, the rationale, the two #18 admissibility checks (does it readmit FN/CLS/FPS/CEG/VST into A–E? is any affected name currently failing the gate being changed?), and the adoption date. Pending items are proposals — they bind nothing until adopted.

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
3. Run the two #18 checks explicitly.
4. Set the adoption re-test (scheduled quarterly or a named post-print).
5. On adoption, move the entry to "Adopted" with the date and update framework.md.
