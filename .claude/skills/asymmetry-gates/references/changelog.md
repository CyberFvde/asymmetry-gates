# #18 — Rule-change log (policy Oct 28, 2026, revision 9)

Rule changes normally take effect at a scheduled or post-print re-test; an explicit user request can authorize calibration between re-tests. Record the change, rationale, safeguard check, universe impact and adoption basis. Apply changes to the full relevant universe and re-screen before upgrading any name. Earlier entries retain the historical #18 checks that applied at their adoption. Pending items are proposals — they bind nothing until adopted.

## Adopted configuration: Oct 28, 2026, revision 9 (H4a dilution budget)

### Authorization, scope and adoption basis

Explicit user request dated Oct 28, 2026 (17:27 CT): "can you add an iren dilution blocker to our asymmetry gates or eh does it matter because we have dilution blockers already." Shown that core A1, M and D already exclude IREN and that H is the only open route, he chose (17:33 CT) "the most lenient cap that would've blocked evil diluters like iren." Scope: route H only. The user approved the diff at 18:08 CT ("accept the PR").

### Change summary (old to new)

- **New H4a:** trailing 12-month share growth + undrawn ATM/equity-program capacity at the screen price + maximum pending deal shares ≤50% of current shares. Converts excluded (H4/D1(a) already price them). Unknown components mean H-watch unless a sourced upper bound clears 50%; a verified breach means out of H. Re-run at every H7 review: >50% freezes adds; a raise that crosses 50% breaches H7's share-count limits.
- **Not changed:** A1, M1, D1–D7 (D1(c) already caps ATM proceeds at 5% of market cap a year, D1(b) projects the ATM pace and D2 requires a cash engine), H2's exclusion of unopened ATM capacity from funding, H4's 20% hurdle and written share ceilings, H6 caps.
- **Syncs:** `stage-paths.md` (header, scope note, H4a), `framework.md` (header, H summary), `SKILL.md` and `README.md` policy lines, `roster.md` (dated impact section).

### Rationale and calibration

- **Gap closed.** H was the only route with no numeric dilution ceiling: it required a written maximum share count but set no limit on its size, and undrawn ATM capacity counted as neither funding (H2) nor future dilution. A serial issuer with a loaded ATM could reach H-early on an optimistic model.
- **Why a combined budget, not a trailing cap.** IREN's trailing growth is +41.6%, so the loosest trailing cap that blocks it is 40%, and it stops binding once the 2025–26 raises roll off while the ATM stays loaded. Adding undrawn capacity keeps the test on the live risk.
- **Why 50%.** IREN totals ~76.5% today. The literal loosest level that blocks it (~75%) is knife-edge; at 50% IREN stays blocked even if trailing growth halves while ~$3.5B of ATM remains. 50% still admits PL, ASTS, QBTS, RGTI, NBIS and RKLB to an H model.

### Structural and solvency safeguard check

H4a only removes eligibility; it relaxes nothing. H1–H7, A7 insider limits, #19 and PH still apply to every name that passes it. Known cost: a genuine early-stage company funding a contracted buildout through a large ATM can now fail H; it can re-qualify once issued shares and remaining capacity fall under the budget.

### Universe impact (H-watch names; Oct 26 closes; subagent research Oct 28, sources in the roster section)

| Name | Trailing 12M | Undrawn ATM | Pending deal | Total | Verdict |
|---|---|---|---|---|---|
| RDW | +73.6% (cover) | 16.8% | 0% | ~90.4% | **Out of H (H4a)** |
| IREN | +41.6% | 34.9% (~$3.5B) | 0% | ~76.5% | **Out of H (H4a)**; was H-watch + #19 blackout |
| IONQ | +50.0% | 0% | 16.0% (Elisity + pre-funded warrants) | ~66.0% | **Out of H (H4a)** |
| PL | +18.2% (cover) | 27.5% | 0% | ~45.7% | Passes, close; in-the-money 2030 notes (~10.6%) stay in H4 |
| ASTS | +39.7% | ≤3.4% (stale bound) | 0% | ≤43.1% | Passes on the upper bound |
| QBTS | +40.1% | 0% | 0% | ~40.1% | Passes |
| RGTI | +32.4% | 0% | 0% | ~32.4% | Passes; warrant count unverified |
| RKLB | ~+20.6% incl. Sept ATM | 0% | 7.1% (Iridium at 0.40) | ~27.7% | Passes |
| NBIS | +13.4% | 4.5% | 0% | ~17.9% | Passes; converts (~25–30%) stay in H4 |
| KTOS | +15.1% | 0% | 0.2% | ~15.3% | Passes |
| AVAV | +1.8% (cover; stockanalysis +52.1% conflicts) | 0% | 0% | ~1.8% | Passes; verify share history |
| KRMN | ~+0.2% | 0% | 0% | ~0.2% | Passes |

No name was upgraded. Passing H4a changes no verdict on its own; every passer still needs H1–H7.

## Adopted configuration: Oct 24, 2026, revision 8 (insider cap, growth bars, #12 void and #17 estimate-cut rule removed)

### Authorization, scope and adoption basis

Explicit user request dated Oct 24, 2026 (20:14 CT), after the non-AI open-universe screen found one Tier 1 name: "lower the growth to 20% a year either revenue or eps, that way it gives candidates 2 tries to enter and raise the insider net % to 1.5% redo." Asked which bar he meant, he chose "anything you think will add more candidates" and applied the 1.5% cap to all routes. At 21:09 CT he added: drop #12's 200DMA void on the price-target leg (option 4 of four offered) and re-run every name it blocked. At 21:14 CT: "You can get rid of #17 too so rerun everything that was kicked by #17". This is a between-screen calibration under #18; the non-AI screen was re-run under it the same day.

### Change summary (old to new)

- **A7 net insider selling (framework #7), G4 and H5 by reference:** ≤0.5% → **≤1.5%** of shares outstanding per 12 months (code S minus code P, 10b5-1 plan sales included). Unchanged: the ≥3-officer discretionary non-plan quarter test, the sell-to-cover reading, the bounded missing-footnote fallback (still ≤0.15%), G4's >25%-of-holdings cluster rule, local-registry verification for foreign filers, the regulatory vetoes. D, M and FT inherit the new limit through A7/#7.
- **Screen guardrail (framework C):** primary ranked-list placement needed a ≥20% base-case return estimate → now **any one of** a ≥20% base-case return, a ≥20% EPS CAGR on the method's base-year path, or a ≥20% forward 3Y revenue CAGR. Gate eligibility, tiers and entry ceilings still come from each route's gates; the return is still reported and ranks names.
- **D4:** forward 3Y revenue CAGR ≥25% plus ≥20% organic revenue growth in next-FY and the year after → **two ways to pass, one metric for all three legs:** revenue (3Y CAGR ≥20%, ≥20% in each of the next two FYs) or consensus EPS (3Y CAGR ≥20%, ≥20% in each of the next two FYs, plus forward 3Y revenue CAGR ≥10%). D7's freeze test follows the metric recorded at entry.
- **#12:** the price-target leg no longer goes void when the price is >20% below the 200DMA. #12 is now simply consensus PT ≥ +20% OR NTM FCF yield ≥5%.
- **#17:** the estimate-cut rule is removed: no automatic re-test on a >5% consensus NTM revenue/EPS cut, no add freeze after two consecutive cuts, no stabilization baseline. The quarterly re-run cadence stays. Cross-references in #13, #14a, #16, #19, `price-health.md` and the "AI capex 2027" action steps now point to #15/#19.
- **Not changed:** #9 (15%/12% revenue), #10, #11, D5 (25% dilution-restated return, 20% stress, HWM yardstick), G5's 12% and H4's 20% five-year hurdles, every cap.
- **Syncs:** `framework.md` (#7, #12, #17 and its cross-references, framework C guardrail, D summary), `price-health.md`, `stage-paths.md` (G4, D4, D7), `SKILL.md`, `README.md`, `triggers.md` headers and per-name insider lines.

### Rationale

- **Insider cap.** At 0.5% the cap removed founder-led growers whose officers sell steadily through 10b5-1 plans (CRDO 1.32%, RDDT 0.67%, RKLB ~1.33% on Oct 15 data) even with no discretionary cluster. Most of that selling is pre-scheduled diversification, which says less about the business than open-market cluster selling does. The three-officer discretionary test, which catches the informative pattern, stays as it was.
- **#12 void.** Its stated purpose was that price targets lag drawdowns, so a fast fall inflates paper upside. It used price as a stand-in for staleness and was never backtested, and it bound hardest on the user's own dip-buying levels (CRDO, BE, VRT, RHM, AXON, HWM, CIEN). #19 (blackout after a material miss) tests the deterioration directly; #17's estimate-cut re-test did too until it was removed the same evening (below). Known cost: a crash ahead of a print now passes #12 on targets that have not caught up.
- **#17.** The user asked to drop it after the #12 change. Estimate cuts still show up in the return estimate, the growth door, D4/D7 and #19 at the next print, so removing the separate freeze mainly ends the rule that blocked adds between prints. Known cost, together with the #12 change: a name whose estimates are being cut before a print now has no automatic pause; #19 acts only once the print lands, and D7's growth-consensus freeze still applies to D names.
- **Growth bars.** The screen's binding constraint was the return estimate: names with ≥20% revenue growth but slower or noisier EPS paths (LLY, ARGX, NBIX, KRYS) never reached the list. Revenue growth is harder to manufacture than EPS growth and less exposed to one-off EPS swings, so it is a fair second door. D4's EPS leg lets a self-funding grower with fast per-share earnings growth qualify even when revenue grows 10–20%; the 10% revenue floor keeps out margin-only or buyback-only stories.

### Structural and solvency safeguard check

Valuation (#11, D5(a)), #12's upside/yield test, A1–A6, A8, the cash floors, leverage tests, #13, #19 and PH are unchanged, so a name admitted by the looser growth bar still has to pass every quality and price gate. D still needs a 25% dilution-restated return and a stress case; G and H keep their five-year models. A heavier insider seller is now eligible: each such name gets a written #15 trigger at 1.5% and stays subject to the discretionary-cluster test. The guardrail change affects list placement only.

### Full-universe impact and required re-tests

| Names / class | Effect; what still decides status |
|---|---|
| **CRDO** | A7 1.32% now under 1.5% → back to D-watch, pending the Q2 2026 three-officer test (CEO and CLO outside plans confirmed; CTO Cheng's ~Jun 4 sale unconfirmed), DustPhotonics G3 accounting (earnout up to ~3.21M shares), #12 now passes with the void removed (PT $284.05) and #19 (Q1 FY27 GAAP GM below GAAP guide). |
| **RDDT** | A7 0.67% passes → core headline pass; A8 (Google AI Overviews referral risk) decides core vs #10 alert. |
| **RKLB** | H5 no longer the blocker at ~1.33% (Oct 15 data, refresh needed); H1–H4 still required. |
| **GLBE** | A7 0.74% passes; still PH-impaired. |
| **LLY, ARGX, NBIX, KRYS, SE, MELI, DLO** | Forward 3Y revenue CAGR ≥20% now qualifies list placement; route gates (#12 for LLY, G5 for NBIX/KRYS, A1/FT for SE/MELI/DLO, PH for DLO) still govern. |
| **RHM.DE** | D4 can pass on the EPS leg (next-FY FY26 +49–64% vs FY25's €22.73 continuing EPS, FY27 +42–49%, revenue CAGR 35%); D5(b) basis question unchanged. |
| **AXON, VRT, MU/SNDK** | AXON's D4 already passed; D5 still binds. VRT unchanged (revenue leg passes). Memory names may pass D4 on EPS where revenue fails; A5/D5 and cyclical-peak checks still apply. |
| **HWM** | #12 now passes (PT +74.6%), so core gates hold if the Oct 29 print clears #19 and PEG stays ≤2.0 like-for-like; still below both growth doors (15.95% revenue, 15.8% EPS), so not a list name; still the D5(d) yardstick. |
| **#12 void floors cited in dated sections** | No longer apply: HWM ~$199.5, KLAC $145.24, AVGO $294.43, CIEN $321.80 (CIEN's #12 now passes on PT +60%), BE $175.43, CRDO $144.69, VRT $215.26, APP (Sep). Buy windows lose their lower bound; the ceilings (PT ÷ 1.2, #11/D5(a)) stand. |
| **#17 freezes** | None in force: no current roster, sleeve-plan or screen name was frozen by an estimate-cut sequence (HWM's Oct 22 check found no cut; the Oct 15 ASTS entry listed #17 beside #19a, H2, H4 and H5, which still block it). Removing it changes no verdict today. |
| **AXON** | D window opens at ≤$317.6 (D5(c) stress binds; D5(b) ≤$370.6), subject to D1(c)/D2/A7/#19 checks. |
| **History rerun (106 names, Oct 24)** | Revision 8 applied to every name in the repo history outside the non-AI screen ([table](../../../../docs/research/2026-10-24-rev8-history-rerun/README.md)). No capital-ready name. New headline core: ANET (A5 conditional), TER and STRL (#13), APP (#19(c) to the Nov 4 print). TSM drops out of core on A3(c). ENR, GFS, NVT and Winbond fail on deep check. |
| **Screen next-FY correction (not a rule change)** | Both screens now read next-FY as framework.md defines it (the year after the last completed FY, so FY26 for December filers) instead of the return base year; D4's second leg is the year after that. No tier changed; HALO joins the non-AI Rule B; RHM's D4 is restated on FY26/FY27 and still passes. |

## Adopted amendment: Oct 24, 2026, revision 7 — separable optionality (SOTP) in return estimates

**Authorization:** the user asked (18:52 CT) that the gates give value to optionality such as Nebius's Avride robotaxi unit, "especially if Avride can grow."

**Change (framework C, applied to G5/H4/D5 by reference):** a separately reported or separately financed subsidiary, segment or stake that the main model does not already capture may add value to a return estimate, at the lower of (a) the latest third-party priced marker within 18 months × the parent's economic ownership and (b) disclosed revenue run-rate × the median listed-peer EV/revenue, less 25%. No outside price and no disclosed revenue means zero, recorded as unpriced upside. Base and bull cases only; ≤20% of base-case value; no double count with consensus; committed parent funding subtracted. It never counts toward #11/#12, cash, funding, leverage, dilution, insider or #19 tests and never cures a hard failure.

**Rationale:** the old method valued only what consensus earnings or the operating model captured, so a priced stake or an outside-funded venture counted for nothing. Requiring an outside price keeps the number from being the screener's own guess, and the haircut, cap and base/bull-only rule stop optionality from carrying a weak case.

**#18 checks:** gates, thresholds, caps and routes are unchanged; only return lines can rise. Counterexamples: a stake with no priced round in 18 months and no disclosed revenue adds nothing; a priced stake whose profits are already in consensus adds nothing; optionality cannot lift a name past a failed funding, dilution or #19 test. Known impacts (Oct 24 evidence, provisional): **NBIS** — Avride $0 today (Uber/Nebius committed up to $375M with no disclosed valuation; no disclosed revenue); ClickHouse stake up to ~28% (2025 figure, before later rounds) of a ~$15B 2026 valuation → ≤~$3.2B after the haircut, ≈≤$10/share today, ownership to verify; NBIS stays H-watch. **GOOGL** — Waymo's Feb 2, 2026 Series D at $126B post-money with Alphabet the majority investor (exact stake undisclosed) counts once the stake is sourced; small against Alphabet's size. **UBER** — listed or priced stakes count under (a). Other names: apply at their next screen.

## Adopted amendment: Oct 24, 2026, revision 7 — mandatory H check

**Authorization:** the user asked (17:27 CT) to "make it mandatory that things always be ran through J just in case"; read as H, the adjacent key, since no route J exists.

**Change (screen procedure):** before any non-FT, non-F name is labeled out, it also gets an H review, recorded as H-early, H-watch, out of H with the deciding H test, or H not applicable with the reason. Recorded in `SKILL.md` step 3, `framework.md` (G/H/M/D section), `stage-paths.md` (H) and the output format.

**Rationale:** NBIS and IREN were labeled out of D on Oct 24 without an H run, though H is the route built for funded, pre-profit build-outs. A first failure in one route says nothing about another.

**#18 checks:** procedural only. H1–H7 thresholds, H's scope (a business still building its cash engine; mature companies cannot use H to bypass current tests, per the Oct 2 and Oct 15 precedents for AMZN, ORCL and GFS), H caps and FT/F exclusions are unchanged. No name is upgraded by the change; it adds a recorded H result to every out verdict. Required re-tests: NBIS and IREN now; other recorded outs get their H line at their next screen.

## Adopted amendment: Oct 24, 2026, revision 7 — P14 strategic placements (D1(c))

**Authorization:** proposed earlier the same day as P14 after the five-name re-test; the user replied "Ya" (17:23 CT) to adopting it. Baseline: merged `main` at `909442b`.

**Change (D1(c)):** a sale of common stock, or of preferred converting 1:1 into common with no coupon, reset or liquidation preference above common, to an operating customer or supplier at or above the 5-day VWAP, for disclosed capex or capacity, is tested like a placement (purpose and non-survival) without the ≥30% conversion-premium requirement. Converts and preferred with a coupon, reset or senior liquidation preference keep the premium test. A discount, attached warrants or survival purpose still fails.

**Rationale:** the premium test targets cheap convertible financing. An at-market 1:1 preferred is a placement in economic terms, and D1(c) never required a premium on placements, so the two were treated inconsistently.

**#18 checks:** safeguards kept: the purpose and non-survival tests, D1(a)/(b) dilution limits (the placement's shares count in FDSO), D2–D5, caps. Counterexamples: a placement below the 5-day VWAP, one paired with warrants, or one funding survival still fails. Known impact (disclosed before adoption): LITE's Mar 2, 2026 NVIDIA preferred ($695.31 vs an approximate 5-day VWAP of $695.89 from daily typical prices, Feb 23–27, 2026; the deal price is almost certainly the contractual VWAP) now passes D1(c). LITE moves from out of D to D-watch; it still fails D5(b) at 21.8% governing on Oct 23 evidence. COHR's March NVIDIA investment needs its terms checked; COHR fails D2 regardless. No other recorded name is affected.

## Adopted configuration: Oct 24, 2026, revision 7 (route D, dilutive growth)

### Authorization, scope and adoption basis

Explicit user request dated Oct 24, 2026 authorizes this between-screen calibration under #18. The user asked to "adjust our gates repository" so that high-growth companies that "need the dilution" are accepted when their return after dilution stays above the 25% IRR floor "as long as it's a good company", with the bar that such names be "better and more exciting than HWM". He also asked that the rules "at least accept" LITE. #18 bars one-name waivers and changing a rule to obtain a verdict, so D is written class-wide on principle; LITE is an impact row below, not a design target, and the user was told before drafting that LITE stays out if it misses the 25% per-share return. Baseline: merged `main` at `1357629`, framework Oct 20 revision 6; FT stays Oct 2 revision 2 apart from route-name syncs. PR #11 (Oct 22 roster re-tests) was merged first at the user's request, so this branch builds on it. The calibration itself changes no roster entry; the five-name re-test the user asked for was run afterwards under revision 7 and is recorded in [docs/research/2026-10-24-rev7-route-d](../../../../docs/research/2026-10-24-rev7-route-d/README.md) and the Oct 24 roster section.

### Change summary (old to new)

- **New route D (`stage-paths.md`):** none → a capped class route for self-funding high-growth companies that fail core A1 or G3 on equity or equity-linked issuance. It replaces A1's WASO ceiling and 12-month issuance ban, A2, A3(b)/(c), #9 and #11 with D1–D5; it keeps A3(a)'s FCF floor (inside D2), A4, A5–A8, #12, #13, #15, #17, #19 and PH.
  - **D1 dilution, measured forward:** baseline = today's fully diluted share count, with every convert/preferred/warrant valued at the screen price under its settlement method (hedges only to their cap); settled legacy converts are sunk. Projected base-case FDSO growth ≤8% a year on average, ≤10% in any year, from SBC net of committed buybacks, converts at base-case prices, pending issuance at maximum and the trailing ATM pace. Every raise in the last 12 months must be non-survival, fund contracted capex/working capital, refinancing, buybacks or G3-tested acquisition consideration, carry ≥30% conversion premium if convertible, and ATM proceeds ≤5% of market cap.
  - **D2 cash:** trailing FCF margin ≥6%, or positive trailing FCF with a ≥6% FY+1 consensus recovery year (≥5 analysts, fixed at entry); NTM FCF consensus >0. **D2(c) capex-cycle quality branch** (added at the user's 13:01 CT follow-up, "you can loosen it if it's quality company like google"): negative FCF is allowed only with trailing OCF margin ≥20% and positive GAAP operating income, positive OCF in the last two FYs, consensus FY+2 FCF margin ≥6% (≥5 analysts, fixed recovery year), 24 months of capex-minus-OCF and maturities funded from cash and committed facilities with a 25% buffer (no ATMs or uncommitted raises), and net debt ≤2.5× trailing EBITDA in place of A4's FCF denominator. At most one of the two D slots may use it. Other negative-FCF issuers stay in H.
  - **D3 leverage:** A4's 2.5× maximum-exposure test unchanged, plus book debt-to-equity ≤1.99× (total debt incl. converts and leases ÷ shareholders' equity; stockanalysis governs; negative equity fails). The D/E cap was added at the user's follow-up request the same day (12:58 CT).
  - **D4 growth:** forward 3Y revenue CAGR ≥25% and ≥20% organic growth in next-FY and the year after.
  - **D5 valuation/return:** fwd P/E ≤45 and PEG ≤1.65; framework C return restated for projected dilution ≥25% base case; ≥20% with every forward year's EPS growth cut 5 points; and the HWM yardstick (beat HWM's latest framework C estimate by ≥5 points and its forward 3Y revenue CAGR).
  - **D6 size:** initial ≤2.5% sleeve/0.60% portfolio, total per name ≤5.0%/1.25%, max two D names, aggregate ≤10%/2.5%, inside the combined non-core budget (now #14a/G/H/M/D ≤35%/8%) and #16 name/factor caps.
  - **D7 exits:** written FDSO path and floors; out on a failed raise test, trailing FDSO growth >10% or above the written path, FCF margin <3% or a missed recovery year, net debt >3.0× NTM FCF, D/E ≥2.5×, or two consecutive material #19 prints; freeze on D return <20%, stress <15%, growth consensus <20% or projected dilution >8%.
- **Syncs:** framework intro, #14, #16, #18, Sources, G/H/M/D section, FT and PH lines; `price-health.md`, `fintech.md`, `triggers.md` (D record and generic "Any D name" line), `SKILL.md` and `README.md`. No other threshold changes.

### Rationale

- **Per-share math already prices dilution.** The return estimate works on per-share EPS, so a flat trailing share-count cap partly counts dilution twice. It also blocks names for a year after a one-time event: LITE's trailing diluted shares rose ~40% when legacy converts were equitized after the stock ran, which a buyer today does not pay for again. Measuring forward from today's fully diluted count, with each instrument's settlement terms, asks the question a new buyer actually faces.
- **Why the extra bars.** Dilution is reflexive: companies that fund growth with stock tend to issue more when the price falls, and growth forecasts miss more often than issuance plans. D therefore asks for more growth (25%/20% versus core's 15%/12%), a higher return (25% versus the 20% screen guardrail) with a growth-cut stress, actual positive FCF, and a purpose test on every recent raise. The user's 35%-growth/10%-dilution example compounds per share at 1.35/1.10 − 1 ≈ 22.7%, which this route would reject; at 35% growth the most dilution that still clears 25% is 8% a year, which set D1's cap.
- **Debt-to-equity cap.** The user asked for a maximum 1.99× debt-to-equity, the balance-sheet line he uses to separate neoclouds (a post he shared lists NBIS 1×, IREN 2×, CRWV 10×, unverified; 24/7 Wall St cites CoreWeave at 8.94 from its Q2 2026 report). Actual ratios are checked at each screen. It is an extra restriction on top of A4 and D2. Book D/E falls whenever a company sells stock, so it can flatter a heavy issuer; that is why it sits beside A4's cash-based leverage test and the FCF floor rather than replacing them.
- **Capex-cycle branch.** The user wants quality companies in a build-out admitted even while FCF is negative, using GOOGL as his example of quality. "Quality" is written as numbers that describe an established, profitable platform: high cash margins, operating profit, a dated FCF recovery and funding that does not rely on the next raise. A pre-profit issuer that funds capex with ATMs and converts does not meet it, whatever its debt-to-equity ratio.
- **HWM yardstick.** The user wanted D names to be better and more exciting than HWM. That is written as a measurable opportunity-cost test. On today's recorded figure (~15.4%) the 25% floor binds first, so the yardstick only matters if HWM's own estimate rises above ~20%.

### Structural and solvency safeguard check

A–E core, G, H and M thresholds are unchanged, including A1 for core, G3's 3% and the de minimis carve-out. D is a separate capped route like M. What it loosens: the trailing WASO ceiling and the 12-month issuance ban (replaced by forward dilution limits and a raise test), A2's buyback/net-cash requirement, A3(b)/(c) (replaced by positive NTM FCF on top of the A3(a) floor), #9 and #11 (replaced by stricter growth and a P/E/PEG cap plus a dilution-restated 25% return). The A3(a) recovery-year option is a loosening for thin-but-positive FCF names. D2(c) is a further loosening: it admits negative-FCF companies that meet M-style quality floors (OCF margin, operating profit, recovery clock) plus H2-style committed funding, limited to one name; its exits sit tighter than its entry floors. What it keeps: A4's 2.5× maximum-exposure leverage (with the added ≤1.99× book D/E), A5 top-two/margin, A6, A7 insider/legal vetoes, A8 disintermediation, #12, #13 timing, #15, #17, #19 and PH. FT and F names cannot use D. Loss paths: growth that misses while issuance continues, ATM dilution accelerating into a falling price, and multiple compression from a high entry. Bounds: max two names, ≤10% sleeve/≤2.5% portfolio aggregate, inside the 35%/8% non-core budget and the 60%/25% AI-capex factor cap with the full shared trigger. These are looser settings than core, chosen by the user, not a backtested result.

### Full-universe impact and required re-tests

Applies to every current, historical and queued name. Rows are rule sensitivities, not upgrades; each needs a full fresh D screen, PH, #19 and cap headroom before any status or sizing change. The five names the user asked about were re-tested under revision 7 on Oct 23–24 evidence in the research file linked above.

| Existing names / class | Possible effect at the next screen; unresolved or unchanged conditions |
|---|---|
| **LITE, CIEN, COHR, NBIS, IREN** | Re-tested Oct 24 after adoption (roster and research file). CIEN D-watch (#12 fails by $1.54; D5(b) depends on an unsourced 5Y median fwd P/E). LITE out on D1(c) to Mar 2, 2027 (NVIDIA's at-market convertible preferred) and borderline D5(b). COHR out on D2 (OCF margin 1.1%). NBIS and IREN out on D2(c) (operating losses, net debt/EBITDA 8.3× and ~51×) and D5(a). All five pass the 1.99× D/E cap. None is a trade instruction. |
| **CRDO** | A1 out on DustPhotonics stock plus contingent shares. D could apply if the earnout's maximum shares are counted, the deal meets G3's 24-month FCF/share test and D4/D5 pass on current consensus. |
| **MU, SNDK, SK Hynix** | MU's A1 issue is a WASO ceiling without buybacks; SNDK +6.9% shares; Hynix ADR-listing issuance. D needs ≥20% organic growth in next-FY and the following FY and a 25% 3Y revenue CAGR, which memory names off a peak-cycle base may miss; SNDK still faces A5 (five-player NAND), which D keeps. Hynix needs DART insider coverage. |
| **VRT** | A1/A2 (shares +1.06%, no buybacks) could move to D if D4's 25% 3Y revenue CAGR and ≥20% two-year growth hold; the #19(a) blackout still governs until a clean print. |
| **PLTR, CRWD, ZS, PANW** | PLTR may pass D1–D4 but fails D5's P/E ≤45 at recorded multiples. CRWD/ZS/PANW growth sits below D4's 25%; G remains their route. |
| **DASH, NBIX, CDNS, ARGX and other G3/A1 near-misses** | Growth below D4's 25%/20%, so D does not reach them; G3/A1 status unchanged. |
| **AAOI, ASTS, RKLB, KTOS, BE, LEU, OKLO, SMR, ORCL and other negative-FCF issuers** | Excluded from D by D2; H (or out) remains their route. |
| **HOOD, COIN and other FT names** | FT1 bars D. |
| **AMZN, MSFT, GOOGL, META** | Growth below D4; M or A–E/3a remains their route. |
| **HWM** | Becomes D5(d)'s yardstick; its own route status is unchanged and still decided at the Oct 29 re-test (PR #11). |

Required next-run ledger for any D candidate: full instrument list (converts, preferred, warrants, hedges with caps, ATM status) and an FDSO bridge at the screen price; three-year projected FDSO path; every trailing-12-month raise with date, size, purpose and premium; trailing and NTM company FCF; next-FY and FY+2 organic revenue consensus with analyst counts; the dilution-restated framework C return, its stress case and the HWM figures used; A5/A7 evidence; #19; PH; and current name/non-core/AI-factor cost headroom. This edit neither promotes a name nor places a trade.

## Adopted configuration: Oct 20, 2026, revision 6 (return-estimate fix and requested leniency)

### Authorization, scope and adoption basis

Explicit user request dated Oct 20, 2026 authorizes this between-screen calibration under #18: fix the non-AI audit's 3-year return math and make the framework "a little more lenient", citing high-quality names such as AMZN that the rules kept out. Offered three bounded options (20% return guardrail, wider #14a growth band, mega-cap platform route); the user chose all three. Baseline: merged `main` at `926e779`, framework Oct 15 revision 5; FT stays Oct 2 revision 2. The roster header (**Oct 2, 2026, revision 3 targeted re-screen**) is preserved byte-for-byte: no statuses, positions or rankings are refreshed. The audit's primary-list return figures are recomputed because they were arithmetic errors, not rule outputs; its gate verdicts are not re-screened here.

### Change summary (old to new)

- **Return estimate (framework C, new convention):** "3Y EPS/FCF CAGR + net buyback yield ± multiple normalization", applied in practice from the last completed FY and with today's multiple held flat → base EPS = consensus for the base year (the first FY ending ≥6 months after the screen; distinct from the gate-defined next-FY); growth = consensus for the next three FYs where ≥3 analysts cover a year or two sources agree within 10% on the same basis (a single unverified source only when it lowers the estimate), otherwise faded to 85% of the prior year's growth; this coverage standard applies only to the estimate, not to gate inputs; exit multiple = lower of entry multiple and 30× (35× when 3Y EPS CAGR ≥25%), and ≤ five-year median forward P/E when available; plus trailing dividend yield; no separate buyback add.
- **Screen guardrail:** primary ranked list required a ≥25% estimate → ≥20% base-case estimate under the corrected method. It decides primary-list placement only; gate eligibility, tiers and entry ceilings still come from route gates. The sleeve's 25%+ objective remains a portfolio aim and was never a per-name gate (SKILL.md, framework intro).
- **#14a (#9 near-pass):** fwd 3Y revenue CAGR ≥12% → ≥10%. Next-FY organic ≥10%, a complete #11 path, all of A, #12/#13/#19, written #15 triggers and starter caps are unchanged.
- **New route M (stage-paths.md):** mega-cap platform in a reinvestment cycle. Scope: market cap ≥$500B, revenue up five straight FYs, not FT/F. Replaces A1's WASO ceiling, A2, A3(a)–(c)/3a, A4's FCF denominator, #9 and #11 with: diluted WASO ≤ +1.5% without requiring buybacks (core allows +1.5% only with buybacks and ≥25% growth; A1 issuance bans and de minimis kept); trailing OCF margin ≥20%; positive OCF five FYs and trailing OCF ≥ last FY; NTM capex ≤125% of NTM OCF; consensus FY+2 FCF margin ≥6% with ≥5 analysts (FY+2 = second FY after the last completed FY; it rolls forward before entry and is fixed as the recovery clock at entry); net debt incl. leases/guarantees ≤1.0× EBITDA; fwd 3Y and next-FY organic revenue growth ≥10%; fwd P/E ≤38, PEG ≤2.0, NTM OCF yield ≥4% (Standard Core limits with OCF yield in place of FCF yield; no high-velocity path or #14a band). Keeps A1 bans, A5–A8 (A7 loss test on 5% of NTM OCF), #12, #13, #15, #17, #19, PH. Caps: initial 2.5% sleeve/0.60% portfolio, total 5.0%/1.25% per name, max two names, 10%/2.5% aggregate, inside the combined 35%/8% non-core budget; hyperscaler-type capex counts in the AI-capex factor cap. Exits written in M7.

### Rationale

- **Return math:** the audit's estimates had three errors. Per-share EPS consensus already reflects buybacks, so adding buyback yield counted them twice. Growth was anchored on a completed year (HWM: FY25 $3.77), so a past jump (HWM FY26 +42%, helped by the CAM acquisition) counted as future return. And today's multiple was held for three years, including ~37× for HWM. HWM's estimate falls from 27.8% to ~10.9%. Ranking on inflated returns admits names the sleeve can't expect to compound.
- **20% guardrail:** the user's growth account aims at 20%+; on corrected math no primary-list name reaches 25% (ARGX tops out near 22.5%), and even at 20% only ARGX passes. The guardrail ranks; it does not remove a gate-passing name's eligibility.
- **#14a band:** quality compounders growing 10–12% with a full core valuation were alert-only. Starter caps (≤5% sleeve per name, three names, 12.5% aggregate) bound the added risk.
- **M:** AMZN-type platforms failed A2/A3 during a capex cycle despite 20%+ OCF margins and low leverage. M admits them at starter size with a fixed FCF-recovery clock instead of waiving A3(a) for core.

### Structural and solvency safeguard check

A–E core is unchanged: A1–A8, A3(a)'s actual FCF floor (still never waived for core), #9's 15%/12% thresholds, #11's two complete paths, #12, #13 and #19. M is a separate capped route like G/H. It loosens one dilution test as well as the cash tests: diluted WASO may grow up to +1.5% without buybacks (core: +0.5%, or +1.5% only with buybacks and ≥25% growth), which matters for SBC-heavy platforms. It keeps A1's issuance bans, moat/margin, end-market, insider/legal and disintermediation tests, replaces the FCF tests with OCF, leverage and a fixed recovery deadline, and exits on a missed recovery year without a clock reset. M positions count in name caps, the combined 35%/8% non-core budget and, for hyperscaler-type capex, the 60%/25% AI-capex factor cap with the full shared trigger, so M cannot add uncapped AI-capex exposure. FT and F names cannot use M; G/H thresholds (G3 3%, G5 12%, H4 20%) are unchanged. The return estimate never replaces a route gate. These are looser settings: M admits companies with negative trailing FCF, and a capex cycle that fails to pay back is its main loss path.

### Full-universe impact and required re-tests

Applies to every current, historical and queued name. Rows are rule sensitivities, not upgrades; each needs a full fresh route screen, PH, #19 and cap headroom before any status or sizing change.

| Existing names / class | Possible effect at the next screen; unresolved or unchanged conditions |
|---|---|
| **AMZN** | Route M sensitivity on Oct 19–20 evidence, not an upgrade. Passes M0 ($2.83T; revenue $469.8B, $514.0B, $574.8B, $638.0B, $716.9B for FY21–FY25), M1's WASO ceiling (+0.90% vs +1.5%), M2(a) (TTM OCF $161.4B on revenue $775.7B through Q2 2026 = 20.8%, thin), M2(b) (OCF positive five FYs; TTM $161.4B ≥ FY25 $139.5B), M2(c) (NTM capex/OCF ~106% from marketscreener capex and FCF consensus, flagged), M3 (net debt incl. leases plus the 40% cash Globalstar leg ~$124–133B = 0.73–0.79× TTM EBITDA $168.9B), M4 (consensus revenue FY26 $828.6B, FY27 $949.3B, FY28 $1,099.1B: FY26 +15.6%, FY25–28 CAGR ~15.3%), M5 (fwd P/E 28.0, PEG 1.35, NTM OCF yield ~8.8%), #12 (PT +26.3%, 60 analysts) and #19 (Q2 beat; Q3 guide midpoint −2.2% vs consensus, inside (d)'s 3%). **Fails M2(d):** consensus FCF margin about −0.9% in FY27 and ~3.2% in FY28 (marketscreener; FY27 capex consensus $277.8B), so no 6% recovery year. After FY26 reports, the test year rolls to FY28, still ~3.2% today. Open items: Globalstar maximum shares including GSAT preferred and awards (41.3M = 0.38% if every common holder takes stock, 24.8M at the 60% stock floor, before preferred and awards), the Q2 10-Q contingency note for the FTC ad-pricing suit (M2(e) line ~5% of NTM OCF ≈ $12.4B), and plan status of Nov 2025 officer sales. Core stays out: A1 (the Sep 28 roster cited the pending Globalstar stock consideration, which may fit the de minimis carve-out once maximum shares are verified, but diluted WASO +0.90% with no buybacks also exceeds core's ceiling), A2 and A3(a). Under the Oct 15 #19(d) threshold (>3%), the −2.2% Q3 guide gap that the Sep 28 roster recorded as a blackout is now a watch item. #9 also looks passable on current consensus. Re-test after the Oct 29 print. |
| **MSFT, GOOGL, META** | ≥$500B with heavy AI capex. M applies only if they fail A2/A3 on capex; re-test M1–M5 with lease-inclusive leverage and FY+2 FCF consensus. MSFT's 3a high-water trigger and GOOGL's 14b re-entry trigger still govern the A–E/3a path. All count in the AI-capex factor cap. |
| **ORCL** | M0 scope can be met, but A1 financing issuance (equity/ATM) is kept by M1, so ORCL stays out. Negative FCF and leverage also likely fail M2/M3. |
| **TSM, NVDA, AVGO, LLY, Samsung and other ≥$500B names** | Use A–E/3a when they qualify; M is only for an A2/A3 capex failure. TSLA-type names likely fail M2(a) (OCF margin <20%). FT names (V, MA, JPM and similar) cannot use M; banks/insurers stay outside A6. |
| **CART, REGN, CVLT, FTNT, ISRG and other 10–12% 3Y growers** | #14a's #9 band may now apply when next-FY organic ≥10%, all of A is verified and a full #11 path passes. CART (3Y revenue 11.2%) is the clearest candidate; its `≤ $48.50` trigger came from the legacy 25% estimate and no longer has a basis. ISRG-type simultaneous #9/#11 shortfalls still cannot combine. |
| **HWM, ATI, UBER (gate inputs)** | The backward anchor also sits inside some gate inputs. HWM's stockanalysis PEG 1.29 implies ~28% growth; 37.2× on ~15% forward consensus growth is ~2.4, above Standard Core's 2.0. ATI's High-Velocity #11 path used a 32.3% 3Y EPS CAGR against ~16% forward. UBER's #10 waiver needs ≥20% 3Y EPS CAGR against ~16% forward. stockanalysis still governs #11/#12, but resolve each gap on a like-for-like basis before any entry or addition. |
| **ATI, CRS, MTU, WWD** | ATI and CRS still fail the next-FY ≥10% leg on recorded evidence; MTU fails A3(a); WWD's A3(b)/A4 issues are unchanged. |
| **BKNG, GE, TDG, RTX, LMT, EXPE, TCOM** | 3Y revenue growth below 10%, so the #14a change does not reach them; other recorded failures stand. |
| **TW, SCHW, MELI, SE and other FT names** | FT1 still bars #14a starters and G/H/M. |
| **Non-AI audit primary list (14 names)** | Recomputed estimates in the audit's section 0: ARGX ~22.5% (only pass); KOG.OL unresolved (post-demerger perimeter mix); UBER ~16.1%, ATI ~16.2%, LLY ~15.4%, PODD ~15.2%, WWD ~13.8%, CART ~13.2%, NBIX ~12.7%, SAF.PA ~12.0%, HWM ~10.9%, KRYS ~6.5%, ADMA ~4.6%, HEI ~−1.3% (legacy 25.1–31.5%). See the gate-input row above. Gate verdicts are unchanged and still need fresh re-tests. |
| **All other audit return figures (Rule B, tier lists, per-lane blocks)** | Still on the legacy method and overstated; recompute with framework C before ranking or quoting them. |

Required next-run ledger: consensus EPS path with analyst counts and five-year median forward P/E for every ranked name; for any M candidate, five completed FYs of OCF and revenue, NTM capex guide, FY+2 FCF consensus with analyst count, lease-inclusive net debt and trailing EBITDA, diluted WASO bridge including pending deal shares, A7 annual insider totals and AI-capex factor headroom. This edit neither updates the roster nor places a trade.

## Adopted configuration — Oct 15, 2026, revision 5 (concentrated growth calibration)

### Authorization, scope and adoption basis

Explicit human request dated Oct 15, 2026 authorizes this between-screen calibration under #18. Objective: target 25%+ annualized returns in a concentrated, high-asymmetry growth sleeve. This is a portfolio objective, not a new per-name return gate, a backtest result or a promised outcome. Wider entry valuations and larger allocations also increase valuation and concentration risk.

Baseline: merged `main` at `530e049`, framework Oct 2 revision 3; G/H and FT supporting rules Oct 2 revision 2. The Oct 3 revision 4 calibration remains in draft PR #3 and is not silently adopted: #12 stays 5%, G3 stays 3%, G5 stays 12%, H4 stays 20%. Revision 5 identifies this independent Oct 15 change without reusing the draft revision number. The roster header is **Oct 2, 2026 (revision 3 targeted re-screen; March contest research)**, with separately labeled Sep 28 history. Preserve that file byte-for-byte; no prices, dates, statuses, positions or rankings are refreshed here.

### Change summary (old → new)

- **A1:** retain diluted WASO ceilings +0.5%, or +1.5% only with active buybacks AND forward growth ≥25%. Immaterial stock-settled bolt-ons, acqui-hire grants and contingent share earnouts may aggregate to ≤0.50% of diluted shares over 12 months, including maximum pending payout without double counting, provided WASO stays within its applicable ceiling. Financing/survival issuance, ATMs, secondaries, converts/convert-for-equity exchanges and transformative stock deals remain prohibited; transaction labels and offsetting buybacks cannot hide a larger issuance. This does not waive a stricter written company-specific #15 trigger.
- **3a(Q2):** OCF margin ≥35% AND GM ≥60% → OCF margin ≥35% AND (GM ≥60% OR [GM ≥50% AND OCF margin ≥45% AND ROIC ≥20%]). Q1, Q3 and every 3a(i)–(vi) condition remain. Hardware gross margins alone no longer bar a sufficiently productive physical franchise.
- **A7 execution:** missing raw Form 4 footnotes for a minor Code-S sell-to-cover classification may pass with an explicit watch note when verified annual net sales ≤0.15% of shares AND no single C-suite officer disposed of >15% of holdings in the quarter. The fallback addresses unavailable automated footnote text only: unknown aggregate selling/holdings, known discretionary three-officer clusters, unverifiable local disclosure coverage and legal/regulatory failures are not excused. Annual Code-S selling still counts toward the unchanged 0.5% limit.
- **#19(d):** a next-quarter guide midpoint >3% below pre-print consensus may be watch-only if the same release raises or reaffirms BOTH full-year organic revenue AND company FCF guidance at/above comparable pre-print consensus AND at least three of the last four quarters each beat BOTH revenue and the applicable EPS/EBITDA consensus. This exemption cannot cure #19(a)–(c); unsupported exemption evidence leaves the guide miss blocked.
- **#11:** standard P/E ≤35 → ≤38, with PEG ≤2.0 and NTM FCF yield ≥1.5%. New complete high-velocity core alternative: (forward 3Y EPS CAGR ≥30% OR revenue CAGR ≥25%) AND PEG ≤1.65 AND P/E ≤45 AND NTM FCF yield ≥1.15%. Other core/FT gates remain. Do not combine fragments of the two alternatives.
- **#14a:** single #11 near-pass bands become P/E >38 to 48, PEG >2.0 to 2.50, or NTM FCF yield <1.5% down to 1.0%. Test both complete #11 alternatives first; a near-pass must have exactly one failed component relative to one applicable path, with its other components/prerequisites intact. No simultaneous growth/valuation band or mixed-path waiver. Entry ≤5.0% sleeve AND ≤1.25% portfolio per name, max three names/≤12.5% sleeve aggregate, instead of 2.5%/0.5%, max two/5%. Scaling still requires full qualification and the next clean print.
- **G6:** initial 2.5%/0.5% → 5.0% sleeve/1.25% portfolio; total per name 5%/1% → 12.5%/3.0%; max three, aggregate 15%/3% → 25%/6.0%. Full G cash, maximum-exposure leverage, dilution, valuation and earned-add tests remain.
- **H6:** initial 1.25%/0.25% → 2.5% sleeve/0.60% portfolio; total per name 2.5%/0.5% → 5.0%/1.25%; max two, aggregate 5%/1% → 10%/2.5%. Funded 24-month execution plus 25% overrun buffer, maximum shares, fixed quality deadline, achieved checkpoints and exits remain.
- **#16 shared budget:** #14a + G + H + new-entry PH-recovery becomes ≤35% sleeve at cost AND ≤8% portfolio, from 20%/4%, counted once. Existing verified A–E Core holdings entering PH-recovery do not consume this non-core budget; their full cost still counts toward ordinary name/factor limits and PH additions remain frozen/staged. Existing G/H/starters cannot manufacture headroom by relabeling as Core. Route switches preserve history/cost.
- **Winner/factor limits:** hard 25%-sleeve-at-cost/10%-portfolio per-name cap stays. Market-weight trim threshold 35% → 40% of sleeve; trim target 30% → 32.5% at the next re-test. Shared AI-capex factor cap 50% sleeve/20% portfolio → 60%/25%, at cost. Tripwires, maximum vendor-financing exposure and re-test/addition freezes remain; no forced group sale from market appreciation alone.
- **PH data:** if dividend-reinvested history is unavailable but full split-adjusted price history exists and verified trailing dividend yield is <1.5%, permit disclosed stock price return versus S&P 500 price return, on consistent dates/currency. Do not label that series total return, silently mix return bases, omit special distributions, or invent a lifetime ATH from incomplete history. Other mature-listing data gaps remain PH-unverified.
- **PH recovery:** 20 consecutive closes → 10 completed closes above contemporaneous 200DMA; rising 200DMA versus 20 sessions earlier OR 50DMA above 200DMA and rising; nonnegative 6-month relative return → nonnegative 3-month OR 6-month relative return; latest route print/checkpoint still must qualify. New-entry staging 2.5%/0.5% → 5.0% sleeve/1.25% portfolio or the smaller selected-route initial cap. Full sizing still waits for the following clean print/checkpoint. ATH-age/drawdown/three-year impairment thresholds are unchanged.

### Rationale

Remove automatic rejection of genuinely immaterial stock consideration, allow high-return capacity ramps to demonstrate 3a eligibility, bound a narrow footnote-data bottleneck with observable selling/holdings limits, and distinguish a documented conservative guide from a broad operating miss. Complete valuation alternatives, larger earned allocations and earlier evidenced PH recovery support the requested concentrated growth mandate; they do not establish that a stock or portfolio will earn 25%.

### Structural and solvency safeguard check

A3(a)'s actual 6% FCF-margin floor, remaining 3a conditions, A4's 2.5× maximum-exposure leverage including vendor/JV/residual guarantees, A2 buyback/net-cash test, A5/A6/A8, annual insider/legal vetoes, #12, #13 timing, #15 company exits, #17 estimate-cut reviews and #19(a)–(c) are retained. Only the requested A1, Q2, footnote and #19(d) exceptions change structural execution. Known failures cannot become missing-footnote passes. No liquidity from unopened ATMs or hypothetical raises enters H2. G3/G5/H4 remain at merged-main values, and G4/H5's separate governance/legal/funding tests still apply. FT retains 15%/15% growth, normalized company cash, stress/resilience and no funded starter/G/H bypass; it may use the new complete core #11 alternatives only after full FT qualification. F's signal, solvency, holding and separate-accounting rules remain. Every route/name/shared budget applies simultaneously; unknown headroom means zero new capital. A pre-existing #15 exit/re-test trigger is not rewritten into a generic softer gate.

### Full-universe impact and required re-tests

This applies to every current, historical and queued roster name, not only the requested examples. Rows below are rule sensitivities using dated repository evidence; they are not Oct 15 market checks or upgrades. Re-test the full applicable route, fresh PH, all #19 comparisons, #15 triggers and cap headroom before any status or sizing change.

| Existing names / class | Possible effect at the next screen; unresolved or unchanged conditions |
|---|---|
| **TSM** | New 3a(Q2) branch may remove the hardware-GM bottleneck. Verify NTM OCF margin ≥45%, GM ≥50%, ROIC ≥20%, Q1 OCF ≥$50B, Q3 history/growth and all six 3a conditions; historical 57.4% GM alone proves no pass. Alternatively re-test ordinary capex/OCF ≤50%. |
| **VRT** | Re-test valuation under both #11 paths and the new starter bands; verify acquisition/earnout exposure and insiders. The recorded actual revenue miss is #19(a), which the #19(d)-only guide exemption cannot cure. Re-measure the original miss/next clean print; do not auto-lift blackout. |
| **CDNS** | Reconcile 3.2M acquisition shares, diluted denominator, all 12-month/pending share consideration and WASO against the ≤0.50% carve-out. The number alone is not immaterial; a 3.2M numerator requires at least 640M diluted shares. If A1 later clears, re-test growth and PEG; PEG 2.2 is only a possible single-component starter with all other applicable tests passed. |
| **ANET** | Historical P/E 37.4 is within the new standard ≤38 component. Refresh PEG, NTM FCF yield, all A/#9/#12/#19 and factor budget before core eligibility. |
| **AMD** | Historical governing 42.6×/PEG 0.65 may fit the high-velocity alternative only with qualifying 3Y EPS/revenue growth and NTM yield ≥1.15%; otherwise assess a single PE starter with the other standard components intact. The Anthropic commitment still enters A4 at maximum exposure. |
| **LRCX** | Re-test the high-velocity growth/PEG prerequisites and true NTM FCF yield; historical trailing yield ~1.3% is not NTM evidence. Could satisfy velocity core at ≥1.15% or a single yield starter at ≥1.0%. PT/#12, print and written triggers still apply. |
| **NVDA** | A7 fallback may remove only a missing minor-sale footnote bottleneck after verified annual net selling ≤0.15% and C-suite quarter holdings tests. An unfinished annual sweep does not qualify. OpenAI maximum commitment, legal vetoes, #15 and cap headroom remain; new factor limit may permit later earned tranches. |
| **AVGO, AMAT, KLAC, MU, ADI, ASML, Samsung, SNDK; SK Hynix queue** | Re-test relevant #11/A7/3a sensitivity and 60%/25% group headroom. MU's five-year revenue-history failure is not cured by Q2. JV/vendor exposure and standalone company triggers remain; missing local disclosures do not gain a US Form 4 exemption. Historical status/thresholds in the roster remain dated. |
| **HWM, GEV, HEI, MRVL, TER and other valuation alerts** | Re-test both complete #11 paths, then an exactly-one-component starter where applicable. Historical quotes must not decide current bands; PE 48.01 remains outside the starter band, and PEG/yield plus PE failures cannot be combined. Growth, acquisition, cash and legal blockers still govern. |
| **PANW, NVT, CRWD, FTNT, REGN, ISRG, SYM, ENR and other G candidates** | Larger G allocations become available only after complete G1–G5 evidence, including full share/claim accounting and a sourced cash/share model. An incomplete G-watch is still unfunded. ISRG-like simultaneous growth/valuation failures do not become an A–E starter. Core #11 changes do not replace G5's retained 12% return hurdle. |
| **RKLB, ASTS, PL, AVAV, KTOS, RDW, IONQ, RGTI, QBTS; GPCR/VKTX/ALT** | H cap expansion is conditional on all funding, commercial, dilution, fixed-quality-path and milestone tests. Financing bans still bind A–E; H cannot count future uncommitted raises. Clinical progress without required commercial demand still fails H1. Contest research is not skill capital. |
| **ALGN, ZS, TENB, TOST, PDD, GLBE, ALT and other PH names; RMD/OKTA warnings** | Recompute the 10-close/trend/3-or-6-month recovery conjunction and latest full route. Technical recovery alone cannot cure TENB-like growth failure or ZS-like dilution. Old-high warnings alone remain non-blocking. Existing Core recovery positions gain budget relief, not automatic additions. |
| **STMN, KOG, PRX, ENR, Samsung and other foreign/data-limited listings** | Evaluate low-yield price-return fallback with verified yield, full ATH history, matching currency/dates and appropriate distribution adjustments. Non-US insider coverage, cash/organic growth and demerger-scope comparisons remain required; fallback does not imply a local-filings pass. |
| **MA, TOST, SE, MELI, HOOD, COIN, XYZ, SCHW, TW, PDD, GLBE, KSPI, FUTU and other FT names** | Apply new full core valuation alternatives only within full FT; no enlarged starter/G/H access. Growth, normalized cash, credit/regulatory and legal blockers remain; mandatory-sale classification alone does not grant capital. |
| **MSFT, GOOGL, AMZN, ORCL, META; LMT, RTX, GD, NOC, LHX, CW, GE, WWD, RHM, PRX and other structural/growth outs** | Re-test only genuinely affected gates; negative FCF, failed high-water/capex tests, excessive leverage, financing issuance, margin/disintermediation or growth failures are not erased by a larger PE limit or the 25% objective. #19(d) watch relief never cures actual #19(a)–(c) misses. |
| **VST, CEG, CCJ, NRG, TLN, COP, XOM, CVX, EOG, FANG, EQT, OXY and other F names** | F rules and F2 entry signals remain. No enlarged #16/G/H budget or #19(d) substitution through F5; PH may still stage a fully F-qualified recovery using its own limits/timing and separate accounting. |
| **CRDO, LITE, BWXT, PLTR, PWR, MTZ, BE, LEU, OKLO, SMR, AAOI and other issuers; COHR, CAT, TDG, ETN, FSLR, EME, FN, CLS, FPS, WYFI, RMBS, GFS and remaining outs/queues (STRL, DELL, TER, ESMT, Etron, Winbond, SIVE)** | Reconcile actual aggregate consideration where A1 is relevant; no financing/survival or >0.50% bolt-on escape. Other cash, leverage, share-count, end-market, top-two/margin, growth and #10 failures remain. Unscreened names stay unscreened until complete current evidence is gathered. |

Required next-run ledger: raw annual insider totals/quarterly officer holdings and any fallback watch note; complete 12-month/max-pending share bridge; Q1–Q3 and 3a(i)–(vi) cash/ROIC data; two-path #11 classification and exact starter component; four-quarter paired beat history and comparable FY organic/FCF guidance for any #19(d) exemption; full PH series/return basis and 10-close/trend/relative checks; and current name/route/non-core/AI-factor cost headroom. Reconcile later unmerged roster evidence before the next screen writes the book. Reconfirm shared factor anchors then. This edit neither updates the roster nor places a trade.

## Adopted configuration — Oct 2, 2026, revision 3 (price health and stale ATHs)

Authorization: the user explicitly asked that ALGN's long period without a new ATH be incorporated into the skill. Add PH to every route and each screen's output, without treating an old high alone as a permanent business-quality veto.

Change: prior price awareness was limited to valuation and sizing → record split-adjusted closing ATH date/age, drawdown, three-year total-return gap versus a preselected broad benchmark, close versus 200DMA and its 20-session trend. ATH age ≥3 years is a warning. All three of age ≥3 years, drawdown ≥30% and underperformance ≥20 percentage points make a name PH-impaired, with zero new capital even when its underlying financial route qualifies. Missing mature-listing evidence is PH-unverified. Short operating history is disclosed rather than fabricated; SPAC shell highs are excluded.

Recovery: ≥20 consecutive closes above contemporaneous 200DMA, rising 200DMA, nonnegative six-month relative total return, and latest route-specific print/checkpoint qualified. Permit only staged initial allocation ≤2.5% sleeve/0.5% portfolio or the smaller route cap; full sizing requires the following clean print/checkpoint with recovery intact. A new ATH is unnecessary. Recovery allocations in A–E/G/H join the same 20%-sleeve/4%-portfolio combined budget, counted once; F keeps separate accounting. Relabeling existing holdings above that combined cap phases in through group additions freezes while counting full cost basis, without a label-driven forced sale. Held names freeze additions and re-test; no automatic sale from price weakness alone.

Rationale: a fundamentals-only shortlist can hide years of market underperformance and capital tied up in an unproven turnaround. Combining stale highs with drawdown and relative returns makes the warning actionable, while the sustained recovery route preserves room for improving businesses. Thresholds are user-preference settings, not backtested timing evidence.

#18 safeguard check: no cash, funding, dilution, leverage or FT/F route test is waived; PH only restricts/throttles additions. Historical position/evidence dates remain intact. A verified recovery never admits a failing business. Selected-route failure/exit rules remain in force.

#18 universe-impact check: every route gets the same price-health review. ALGN is a requested example, not a pre-declared PH verdict; calculate current complete history and benchmark returns before reclassification. Counterexamples: a five-year-old ATH plus deep drawdown and persistent relative weakness blocks capital; an old high alone does not; verified trend/relative recovery can restore staged eligibility below the old ATH; an H issuer without three years of operating history cannot be assigned a fabricated three-year failure.

Adoption basis: configuration effective Oct 2, revision 3 at the user's request; perform current PH and financial re-tests before changing a ticker's eligibility. Revision 2's compounder/early/FT changes and revision 1's modest materiality changes remain in force as modified by the overlays.

## Adopted configuration — Oct 2, 2026, revision 2 (themes, early transitions, stricter fintech)

Authorization: the user asked to include strong theme businesses such as PANW/NVT, earlier businesses such as RKLB/ASTS only with a credible route to the required quality, and to be tougher on fintech/payments. This is a class-wide policy edit under #18, effective as configuration now; it is not a fresh market screen or an instruction to trade.

Changes:

- Add G in `stage-paths.md`: an existing cash engine (≥6% trailing FCF margin, NTM FCF ≥90% of trailing, capex/OCF ≤50%, maximum-exposure leverage ≤2.5×), quantified competitive evidence, ≥10% organic growth and ≥12% fully diluted FCF/share growth. Replace blanket issuance/buyback/top-two/P-E exclusions with defined capital-allocation, niche-quality and per-share valuation tests. Ordinary dilution ≤3%; stock-funded deals require a funded, pro forma path back to pre-deal standalone FCF/share within 24 months. Keep annual insider net-sales/legal vetoes; use documented sale-size/context rather than officer count alone in G/H. G initial cap 2.5% sleeve/0.5% portfolio, total 5%/1%, max three/aggregate 15%/3%.
- Add H: demonstrated technical/product progress plus real revenue or binding demand; 24 months of committed funding with a 25% cash-consumption buffer; a fixed ≤5-year deadline to positive company FCF, ≥6% FCF margin and full A–E or G qualification. Substitute present cash/leverage/earnings tests explicitly, model all capex/financing and dilution, require ≥20% base-case annualized return and show a zero-equity failure case. Initial cap 1.25% sleeve/0.25% portfolio, total 2.5%/0.5%, max two/aggregate 5%/1%. Add only after achieved checkpoints; exit on loss of the fixed quality path, critical failure, breached share limits or <12-month stressed runway. No repeated deadline resets.
- Add FT in `fintech.md`: original 15%/15% growth bar for standard qualification, full #10 alternative only, no funded #14a/G/H paths, normalized company cash excluding client/loan-funding distortions, two years of positive normalized FCF and evidenced financial/regulatory stress resilience. Rank lower among otherwise comparable qualifiers. This is a tougher preference, not a claim that every fintech company fails.
- Add a shared #14a/G/H budget ≤20% of sleeve at cost AND ≤4% of portfolio; existing #16 name/factor caps and F routing remain. Route switches preserve cost basis and tranche history.
- Adopt the signal interpretation corresponding to P11 in the separate Oct 2 roster PR: issuer-required, non-discretionary code-S sell-to-cover excluded from A7's officer-count test only, still counted in annual net selling; verified code-F withholding/delivery and bona fide code-G gifts are not market sales. Ambiguous tax descriptions remain unresolved. This is a policy interpretation, not a legal assertion about 10b5-1 coverage. Source for codes: [SEC Form 4 instructions](https://www.sec.gov/files/form4.pdf). TOST is not automatically promoted and still receives FT checks; a legal/cash failure remains binding for any other name. This adopted reading takes precedence over an older pending P11 entry if the separate roster branch is later merged.
- Update routing, selected-reference sync, same-day revision comparison, status labels and trigger requirements. Record the user's requested research queue without changing historical screen results. The earlier Oct 2 calibration remains the revision-1 history; revision 2 supplies its sector/stage exceptions.

Rationale: the old screen stopped at the first A failure, so an A1/A7-only rejection did not establish that the rest of the business or valuation was weak—or that it was sound. Proven compounders and capital-intensive early businesses need different, explicit tests. The new paths reward evidenced economics and funded progress rather than bullish theme labels, while preserving a demanding, less favored route for fintech.

#18 safeguard check: A1–A6/A8 remain strict for core; A7 changes only signal classification of verified mandatory transactions. G retains real cash-flow/leverage floors and a smaller risk budget. H's current-profit exemptions are bounded by verified funding, maximum dilution, fixed deadlines, small size and explicit failure exits. Annual net insider sales, structural-remedy vetoes, maximum-exposure accounting, core valuation thresholds, standard name/factor caps and all F rules remain. No fintech or commodity/IPP can relabel itself to use G/H.

#18 universe-impact check: PANW/NVT and peers become candidates for a full G review, not automatically capital-eligible. RKLB/ASTS and peers can be H candidates even while core A1/A3/A4 fail, but a theme, optional backlog or a bull-case-only cash path cannot qualify them. The listed fintech/payments names face FT; MA cannot use the general growth starter merely because its historical numbers narrowly miss standard growth. Other formerly excluded non-fintech businesses may qualify by the same complete G/H tests; there is no ticker blacklist. Counterexamples: profitable growth bought through dilution without FCF/share recovery fails G; a pre-profit firm with funded execution and an evidenced, attractively priced quality path can pass H; the same firm relying on an unopened ATM remains H-watch; unsupported NVT insider context remains G-watch.

Adoption re-test: policy effective Oct 2, revision 2 under explicit user direction. Re-screen every requested candidate with current source data and route-specific valuation, funding, insider verification, written triggers and portfolio headroom before a status/entry decision. No performance backtest or certainty of eventual success is claimed. Historical roster dates and prior price/gate calls remain historical. Pending P7/P8 are unchanged; other proposals from the separate roster PR are not silently adopted.

## Adopted configuration — Oct 2, 2026, revision 1 (user-requested balanced calibration)

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

## Pending: carried from closed drafts #6 and #3 (bind nothing until adopted)

Carried Oct 20, 2026 when drafts #6 and #3 were closed. P12/P13 keep their draft numbers (P9 to P11 were used on another branch). Q5 from #3 is folded into P12. Each needs its own #18 safeguard and universe-impact check, against the current revision 6 text, before adoption.

### P12. A7/G4/H5: whose sales count toward the 0.5% net-sales limit (from #6, Oct 15)

Proposal: count net open-market and registered-offering sales by officers, directors and Section 16 10% holders, including a sponsor or strategic holder with a board designee; a former insider's sales count only while it still files Form 4s. Rationale: the Oct 15 screen hit this four times (GFS/Mubadala, FPS/Neos, KRMN/Trive, ASTS/Rakuten and American Tower), and the current text does not say whether sponsor exits count. Counterexample to weigh: a sponsor's orderly exit from an otherwise qualified name would block capital for 12 months.

### P13. A1: Up-C pass-through issuance (from #6, Oct 15)

Proposal: issuance whose proceeds only buy existing economic units (Up-C or similar), with total economic shares unchanged, is tested on economic share count rather than as issuance; the selling holder's sales stay in A7. Rationale: FPS issued Class A shares to buy Neos units while total economic shares stayed flat. Counterexample: an Up-C deal that also issues primary shares for cash stays issuance. Re-check against revision 5's A1 de minimis text.

### Interpretation questions from #3 (Oct 2 rev 3 screen)

- **Q1. Dealer floor-plan repurchase obligations under A4/G2 (GNRC):** count a repossessed-product repurchase commitment with cost sharing but no credit indemnity at its disclosed balance like a guarantee, or exclude it?
- **Q2. G3 comparability after a year-ago loss (CRWD):** reported diluted WASO omits year-ago antidilutive shares; should a comparable basic-share series govern?
- **Q3. Associate dividends in A3(a) (PRX):** IFRS allows operating or investing classification; which basis governs company FCF?
- **Q4. Sales to the issuer by a parent under #7 (Naspers into the Prosus buyback):** do they count as insider net selling?
- **Q6. FT "narrow shortfall" yardstick:** the Oct 2 screen used #14a's then-12% floors to separate an unfunded FT alert (MA) from out (V, TW); revision 6 lowered that band to 10%.
- **Q7. Single-source forward FCF (PODD):** can a ≥5-analyst requirement be met when the source does not show its analyst count?

## How to log a change

1. Write the change as a rule edit (which number, old text → new text).
2. Rationale in two or three sentences, tied to a name or a failure mode.
3. Run the two current #18 checks explicitly: preserved safeguards and full-universe impact, including counterexamples and prior exclusions.
4. Set the adoption basis (scheduled quarterly, named post-print, or explicit user-requested calibration) and required fresh re-tests.
5. On adoption, move the entry to "Adopted" with the date and update framework.md.
