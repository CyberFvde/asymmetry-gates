# Framework — forward-leaning (v. Sep 11, 2026)

Forward numbers set the bar; trailing numbers are floors only. The floors are what keep FN/CLS/FPS out — forward-only is the "potential" loophole. Price never votes: exits are defined by #15/#17/#19, entries by gates, and neither a drawdown nor a YTD gain is an input anywhere except #11/#12 and the #16 trim rule.

## Sizing principle

A hard cap, at cost: 25% of the sleeve per name, no exceptions. A 25% position that drops 40% costs the sleeve 10%, which #15/#17 can recover from; a 60% position that does the same ends the strategy. It's a cap on cost basis — a winner may grow to 35% at market before you trim back to 30% at the next re-test, so you're bounding the tail, not selling compounding. Conviction sizes tranches, never caps.

## Sources and definitions

- stockanalysis Statistics/Forecast pages: fwd P/E, PEG, 3Y revenue/EPS CAGR, next-FY estimates, PT, analyst count. Non-US listings via stockanalysis quote pages (KRX, AMS, etc.) are approved for #11/#12 and share statistics; local consensus (KRX) or Capital IQ for #19. (Adopted Sep 11, 2026.)
- NTM OCF/FCF/capex/margins: Capital IQ consensus via the S&P connector; if unavailable, stockanalysis Forecast consensus (S&P MI) plus guidance, flagged. Company guidance only as fallback; vague capex guidance ("elevated," "growing") defaults to trailing capex ×1.25.
- Consensus requires ≥5 analysts.
- Capex, universe-wide, no switching by name: cash PP&E. Company FCF = OCF − cash PP&E. Lease-inclusive and JV-inclusive capex are tracked and live in #15 as kill triggers, not gates.
- "Next-FY" = the fiscal year after the last completed fiscal year. NTM = blended; state the basis.
- Conflicting figures across sources: stockanalysis governs for #11/#12; Capital IQ governs for #3.

## A. Structural — hard, no exceptions

1. Diluted WASO ≤ +0.5% YoY (≤ +1.5% only if buybacks active AND fwd growth ≥25%). Any issuance in trailing 12 months OR announced/pending (convert, secondary, ATM, stock-funded deal) = out. Contingent consideration payable in shares is pending issuance while outstanding; convert-for-equity exchanges are issuance. SBC-driven WASO growth is tested by the ≤0.5% number. (Adopted Sep 11, 2026.)
2. Gross buybacks >0 in the last 4Q, OR net cash with share count ≤ +0.5%.
3. Cash engine: (a) trailing-4Q FCF margin ≥6% — floor, never waived; (b) NTM consensus FCF ≥ trailing-4Q FCF; (c) guided/consensus capex ≤50% of NTM OCF. (b)(c) waivable only via 3a.
   - 3a. Platform-scale exception. Eligibility: Q1 NTM OCF ≥$50B; Q2 NTM OCF margin ≥35% AND gross margin ≥60%; Q3 revenue up in each of the last 5 FYs AND fwd 3Y CAGR ≥10%. Conditions: (i) NTM OCF ≥ trailing OCF; (ii) NTM FCF margin ≥15%; (iii) NTM FCF ≥75% of pre-ramp FY high-water; (iv) capex ≤75% of NTM OCF; (v) net debt/NTM FCF ≤2.5×; (vi) FY+2 consensus FCF > high-water at entry, and actual must clear it by the 5th re-test. High-water number and lease-inclusive kill line go in #15.
4. Net debt/NTM FCF ≤2.5×, pro forma announced deals (target's net debt included). Off-balance-sheet guarantees, residual-value guarantees, JV guarantees and vendor financing count as debt at disclosed maximum exposure.
5. Top-2 share or structural oligopoly, AND NTM gross margin ≥ last FY. Mix carve-out: compression allowed up to 250bp, plus 100bp per 10 points of NTM gross-profit-dollar growth above 15%, capped at 600bp; requires NTM operating margin not down >150bp AND company-attributed mix with segment margins stable. Beyond that = out.
6. Core end-market growing faster than GDP.
7. Insider net selling ≤0.5% of shares out per 12 months; no quarter with ≥3 officers selling outside 10b5-1. Regulatory: out if (a) antitrust/regulatory liability found AND a structural remedy ordered (divestiture/breakup; still out while on appeal), or (b) the company discloses a reasonably-possible loss >5% of NTM FCF. Investigation without complaint, closed inquiries, or behavioral remedies only = watch item, not out. Non-US filers with no 10b5-1 regime: verify through the local disclosure system (DART for Korea, TDnet for Japan, RNS for the UK); if unverifiable, the name is alert-only regardless of other gates. (Adopted Sep 11, 2026.)
8. AI tailwind or neutral; disintermediation risk → #10 only, with a #15 trigger. Disintermediation = a third party can bypass the company's position in the chain (TTD-type); competitive or execution risk stays standard with #15.

## B. Growth

9. Standard: fwd 3Y revenue CAGR ≥15% AND next-FY growth ≥15% (no back-end-loaded hockey sticks; inorganic growth excluded from the next-FY test). R45 floor.
10. Exception (waives only #9): next-FY AND fwd 3Y growth ≥10%, NTM FCF yield ≥5%, PEG <1, net buyback ≥2%, 3Y EPS CAGR ≥20%, plus all of A.

## C. Valuation / asymmetry

11. Fwd P/E ≤35 AND PEG ≤2.0 AND NTM FCF yield ≥1.5%. Fail → alert-only.
12. Consensus PT ≥ +20% OR NTM FCF yield ≥5%. PT leg void if price is >20% below the 200DMA (targets lag drawdowns).
13. One dated catalyst inside 12 months, named. Earnings within 5 trading days = re-test after the print, not before. Price reaction to a print doesn't vote; only gates, #17 and #19 do.

## D. Provisional / exception

14. Fail exactly one gate, and only #9 or #11 → alert, numeric trigger, zero capital. A-fails are never provisional. A name routed "#10 only" by #8 that passes all of A and C and fails exactly one #10 leg is an alert with that leg as the numeric trigger. (Adopted Sep 11, 2026; per #18's second check, Lyft — the name failing the gate at adoption — stays excluded until it clears the leg, then takes alert status on the next re-test.)
   - 14b. Platform alert (class rule, zero capital): a 3a-eligible name passing all of A except 3a(ii)–(iv), plus #11 on FCF yield, during a capex ramp, with net cash ≥2× the NTM FCF shortfall vs high-water and #5/#7 clean. Numeric re-entry trigger in #15; re-test after each print; no capital until 3a passes outright. Net-debt names don't qualify.
15. Written kill triggers, numeric, at entry — kept in `triggers.md`. Any 3a name carries its high-water mark. Every semi/AI-infra name carries the shared "AI capex 2027" factor trigger in addition to its own.

## E. Portfolio

16. Sizing. Min 5% of sleeve. Max 25% of sleeve per name at cost and ≤10% of total portfolio, no exceptions — conviction sizes tranches, never caps. Winners may run to 35% at market; trim to 30% at the next re-test. Entries in three tranches tied to re-tests: tranche 1 at entry (#19 clear), tranche 2 after the next print clears #19, tranche 3 after the following print. One ballast slot: wide moat, passes all of A (3a counts), fails only #12. Ballast is a consolation slot, not a quality tier — a name passing #12 is core, never ballast. Exits are defined by #15/#17/#19 only — never by a price level, ATH, or "fair respect."
   - Aggregate factor cap (adopted Sep 11, 2026): names carrying the shared "AI capex 2027" trigger (currently AVGO, KLAC, AMAT; NVDA, ADI, LRCX, ASML, MU, Samsung, TSM on entry) ≤50% of the sleeve at cost and ≤20% of total portfolio in aggregate. If the group is already over on adoption, the cap phases in through tranche freezes — no forced sales. Winners running the group past 50% at market are handled by the 35%/30% per-name trim, not by a group sale.
17. Re-run quarterly. Revision trigger: consensus NTM revenue or EPS cut >5% between re-tests → immediate re-test; two consecutive cuts → out. Guidance cut = same. Thesis doesn't vote. Macro doesn't vote either — it shows up here or in #19 or not at all.
18. Rule changes only at a scheduled or post-print re-test, with written rationale, applied to the full universe. Rejected if it readmits FN/CLS/FPS/CEG/VST into A–E, or if the name it affects is currently failing the gate being changed. Levered power/IPPs never get A–E exceptions; they route to F. Log every adopted and pending change in `changelog.md`.
19. Entry blackout — recent miss (class rule, entry only). No new capital in a name whose most recent print did any of: (a) revenue (or gross bookings where revenue isn't guided) >1% below consensus; (b) adjusted EPS or EBITDA >1% below consensus; (c) revenue/GB or EBITDA below the company's own guidance midpoint, any amount; (d) next-quarter revenue/GB guide midpoint >2% below consensus. Blackout lifts on the next print that clears all four; first tranche after a lift ≤50% of target, completed after the following print. Names already held: one trigger = alert + #17 check; two consecutive = out. A quality/valuation case never overrides #19.

## F. Signal sleeve — separate from A–E; ≤10% of portfolio, ≤3% per name, max 3 names

- F1. Quality floor (numeric class floor): trailing FCF margin ≥10%; EBITDA margin ≥30%; net debt/EBITDA ≤3.25× and interest coverage ≥3.5×; ROIC ≥ WACC; fwd P/E ≤15 and PEG ≤0.75; EV/EBITDA ≤11; 3Y EPS CAGR ≥25%; top-2/oligopoly; end-market > GDP; no issuance/converts in trailing 12 months, gross buybacks >0 in the last 4Q; PT ≥+25% with ≥15 analysts, or FCF yield ≥4%.
- F2. Signal (entry trigger, within 30 days of the Form 4): open-market purchase by CEO/CFO/founder ≥$2M AND ≥5% of existing holding, OR ≥3 insiders buying in 90 days; 10b5-1, option exercises and grants don't count. Politician disclosures are a tie-breaker only — never a trigger — and only if their purchase price ≤ current price.
- F3. Sector metrics override #19 here: IPPs/commodity names use adjusted EBITDA and FCF-before-growth vs own guidance midpoint, not GAAP revenue/EPS.
- F4. Kill triggers, written at entry: signaling insider sells any shares within 12 months → out; net debt/EBITDA >3.5×; adjusted EBITDA guide cut; 12 months with no improvement in the named thesis metric → out. Max hold 24 months without a re-qualifying signal.
- F5. No cross-contamination: F names never count toward #16, never get A–E exceptions; #18 applies to F's own rules.

## Adopted readings (Sep 11, 2026) — not separate rules, applied inside the numbered gates

- #3(c): trailing capex/OCF is the floor test; the gate is decided on the NTM guide. A name at 49% trailing with a capex guide due inside two weeks re-tests after the print (#13 timing rule).
- #4: a bond-funded equity commitment into a customer (AMD→Anthropic, NVDA→OpenAI) is vendor financing at disclosed maximum.
- #9: for a company whose fiscal year just ended, next-FY is FY+1; the year after is not the test.
- #11/#12: where sources disagree on a forward multiple, stockanalysis governs; say so in the write-up.

Rule text for the earnout/exchange, non-US #7, #10-only alert, aggregate cap and listings changes now sits inside A1, #7, #14, #16 and Sources respectively. History and rationale: changelog.md.
