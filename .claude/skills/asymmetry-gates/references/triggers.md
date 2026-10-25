# #15 — Written kill triggers (policy sync Oct 24, 2026, revision 8; per-name evidence Sep 28, 2026)

Rules: numeric, dated where possible, written before the first tranche. A tripped trigger means immediate re-test (or out, where stated), never a price-based exit. Every semi/AI-infra name carries the shared factor trigger below in addition to its own line.

Per-name figures and status notes below remain historical until a fresh screen. Generic gate checks use the current `framework.md`, selected G/H/M/D route and FT/PH overlays. Standalone company-specific kill thresholds remain in force unless separately changed and logged. The Oct 15 policy calibration does not automatically clear a trigger, upgrade a name or authorize capital. Standalone company-specific #15 triggers remain binding even when a generic gate now has a carve-out. P7/P8 remain pending. PH-impaired names freeze additions and require a route re-test; the price-health flag alone is not a new automatic sell trigger.

## Required records for new G/H/M/D entries

No G/H/M/D entry has been verified by a policy edit. Write a per-name record only after a fresh screen: route, evidence date, fully diluted share baseline/limits, numeric cash/leverage or runway floors, valuation entry ceiling, named business risks, dated review and explicit exit action. G records include deal FCF/share recovery deadlines and any insider-cluster context. H records also include 6/12/24-month delivered-milestone targets, cash-burn ceilings, funded recovery contingencies and the original ≤5-year A–E/G quality deadline. M records also include the recovery fiscal year and its FCF-margin consensus at entry, lease-inclusive net debt/EBITDA, NTM capex/OCF and the maximum pending deal shares. D records also include the entry FDSO baseline with each convert/preferred/warrant's terms, the maximum base-case FDSO path for years 1–3, every trailing-12-month raise with purpose and conversion premium, the D2 floors and any recovery year, and the HWM yardstick figures used. Follow `stage-paths.md`; do not replace the destination deadline whenever the thesis slips. Applicable shared-factor triggers and #16 accounting still apply.

## Shared factor trigger — "AI capex 2027"

Applies to every semi/AI-infra name in A–E: currently AVGO, KLAC, AMAT; extends to NVDA, ADI, LRCX, ASML, MU, Samsung, TSM on entry. Also applies to any M name whose capex is mainly data-center/AI infrastructure (revision 6).

Anchors (confirm at the October re-test): CY27 WFE consensus ~$190B (KLA, Jul 28, 2026 call); top-5 hyperscaler 2027 capex ~$1.3T (NVDA CFO, Aug 26, 2026 — an estimate of customer spend, not orders); AMAT CY26 WFE growth >30%; MU FY27 capex guide (late-Sept 2026 print); Samsung capex run-rate ₩51.9T.

Tripwires — any one trips:
- A. WFE: any of AMAT/LRCX/KLAC/ASML puts CY27 WFE >10% below the anchor (≤$171B), or two of the four cut at consecutive prints.
- B. Hyperscaler capex: MSFT/GOOGL/AMZN/META/ORCL aggregate FY27 capex guide or consensus cut >10% vs anchor, or two of the five guide capex flat-to-down at a print.
- C. Memory: DRAM contract pricing down QoQ two straight quarters (TrendForce), or MU/Samsung/Hynix raise capex >20% above prior guide (a supply response is the margin-peak signal, not a bullish one).
- D. Orders: any of AMAT/LRCX/KLAC guides next-quarter revenue down >10% QoQ or reports book-to-bill <1.

Action when tripped, same day:
1. Immediate re-test of every name in the group, not just the reporter. Exit only if a hard gate or a written exit condition is breached; otherwise keep a monitoring alert. (#17's estimate-cut freeze was removed in revision 8; record each name's consensus changes as monitoring notes.)
2. Tranche freeze across the group: no tranche 2/3 in any semi name until the re-test clears. The #16 aggregate cap (≤60% of sleeve at cost AND ≤25% of portfolio) applies at all times, tripped or not; the tripwires and maximum-exposure vendor-financing treatment are unchanged.
3. No forced exits — exits stay by gates only (#16). The trigger removes the add-on-the-dip reflex; it does not override #15/#19.

## Per-name triggers

- **UBER**: AV operator direct at scale in a top-5 U.S. metro without Uber as demand layer; Mobility GB growth <10% two straight quarters; #7(b) tripped by the FTC/22-state ROSCA case; any equity component added to the Delivery Hero financing (A1).
  - Status Sep 28: AV leg met on a literal reading — Waymo own-app in LA and Dallas/Houston (Feb 2026), Tesla own-app paid rides in Dallas/Houston (Apr 2026, small geofences). Re-test run Sep 28, passes. "At scale" definition proposed (changelog P7). DH still all cash.
- **AVGO**: AI bookings growth negative two straight quarters; top-3 XPU customer publicly dual-sourcing or in-housing at scale; non-GAAP op margin <62%; gross margin <70% → carve-out re-check; contingent residual-value guarantees (Apollo/Blackstone XPV platform) >10% of NTM FCF or any disclosed loss on the platform → immediate re-test; FY27 AI revenue target ($115B) cut at any print → immediate re-test; buybacks zero for 4Q with shares >+1.5%.
  - Status Sep 28: XPV leg TRIPPED — 10-Q filed Sep 10 discloses backstop max potential liability ~$29B (undiscounted, nothing paid) vs NTM FCF ~$49B+. Re-test run Sep 28: gates pass with the backstop and the $42B customer convertible-note facility in #4 at max (2.17×). Trigger text unchanged; threshold rewrite proposed (changelog P8).
- **APP** (core headline, #19(c) blackout from the Q2 adj EBITDA miss vs guide low end; lifts at the Nov 4 print only if all four legs clear; window after ≤$400.07): a third officer selling outside 10b5-1 in a quarter where Foroughi also sells outside a plan trips #7; a disclosed reasonably-possible loss in Talbot v. AppLovin above 5% of NTM FCF → out (A7 regulatory clause); revenue below own guidance midpoint two straight quarters; gaming vertical growth <20% YoY two straight quarters, or consumer/e-commerce spend down QoQ in Q3/Q4 when seasonally it should be up; adjusted EBITDA margin <75%; any Apple/Google policy change restricting SDK data.
- **MSFT (3a)**: high-water FY24 FCF $74B; lease-inclusive capex >85% of NTM OCF or company FCF <$55.6B → out.
  - Status Sep 28: TRIPPED — stockanalysis FY27 FCF consensus $32.34B < $55.6B. MSFT out; re-entry when FY27/FY28 consensus FCF ≥ $55.6B.
- **GOOGL (14b)**: re-entry only if FY27 consensus FCF ≥$40B AND capex ≤75% of NTM OCF.
- **CDNS**: re-test the full 12-month/maximum-pending share consideration and total WASO at the next screen under current A1; the historical Feb 23, 2027 roll-off remains relevant only if the new ≤0.50% aggregate carve-out does not apply. No early clearance is assumed. Entry class still depends on every current gate, including #9/#11 and any #14a eligibility, not the Sep 28 valuation figures alone.
- **NVDA** (write-up required before tranche 1): GM <70% → carve-out re-check; custom-XPU share loss — any top-4 hyperscaler states accelerator mix shifting majority to in-house silicon; hyperscaler capex tripwire B; China SAMR/DOJ — watch items until a structural remedy is ordered, then out per #7(a); OpenAI commitment counted under #4 as vendor financing at disclosed maximum — any write-down or disclosed loss on it → immediate re-test; Huang 10b5-1 volume vs the 1.5% line (revision 8) checked each quarter.
- **KLAC**: CY27 WFE below the ~$190B anchor (shared A); process-control intensity (KLA revenue / WFE) down two straight quarters; China mix >35% of revenue; gross margin <60%; FY27 EPS consensus cut >5% from $5.45.
- **AMAT**: shared A/D; China >35% of revenue; any new BIS action beyond the settled $253M; non-GAAP gross margin <49%; capex >50% of NTM OCF (currently 33%); NTM FCF yield <1.5% at the next re-test.
- **ADI** (historical conditional core): verify Q4 FY26 guide vs consensus under current #19(d) and FY27 organic growth under current #9 before entry; Alif deal — any stock component (A1); industrial/auto book-to-bill <1; gross margin <64%.
- **LRCX** (historical thin core): PT upside <20% → re-check #12's FCF-yield alternative; if #12 alone fails, assess the single ballast slot. NTM FCF yield <1.5% → re-check #11 and any #14a eligibility; shared A/D; China >35% of revenue.
- **ASML** (historical conditional core): verify 2027 organic growth under current #9 before entry; EUV order intake down two straight quarters; China DUV export restrictions expanding to installed-base servicing; PT upside <20% → re-check both #12 legs.
- **MU** (conditional core): FY27 capex guide >50% of NTM OCF → A3 fail, out (3a unavailable — FY23 revenue decline fails the five-year test); HBM share loss — any top-2 GPU/XPU customer publicly moving HBM4 allocation away; DRAM contract pricing down QoQ two straight quarters; diluted WASO >+0.5% with no buyback (A1/A2); shared C.
- **Samsung (005930.KS)** (conditional core): #7 verified via DART or stays alert; July print vs KRX consensus (#19); foundry segment losses widening two straight quarters; HBM4 qualification slip at NVDA/AMD; capex >50% of NTM OCF (currently 26%); any treasury-share cancellation reversal or related-party transaction >5% of NTM FCF (governance); shared C.
- **SNDK** (conditional, outside top-10): #1/#2 (share count, buyback) unverified; Kioxia JV guarantees in #4 at max exposure; JV-inclusive capex >50% of NTM OCF → re-test; NAND contract pricing down QoQ two straight quarters; contracted-revenue floor ($93.9B) reduced at any print → immediate re-test; #5 oligopoly call re-confirmed at each re-test.
- **UBER-class (Lyft)**: same AV trigger as UBER, applied to Lyft's top-5 metros; #7(b) — the Sept 30, 2026 bellwether trial: any 10-Q disclosure of a reasonably-possible loss >5% of NTM FCF (~$55M) → out; 3Y EPS CAGR ≥20% clears that #10 leg, but all entry checks still apply. One failing #10 leg can be an unfunded alert under current #14; no #14a bypass. Any new convert (A1).
- **ANET** (core headline, Oct 24 history rerun; window ≤$192.17 where the high-velocity PEG 1.65 binds; entry Oct 26 or after a clean Nov 3 print): A5 re-test if NVIDIA's lead in data-center Ethernet widens or gross margin falls more than 250bp below FY25's 64.6% non-GAAP; net insider selling >1.5% or a quarter with ≥3 officers selling outside 10b5-1 (Ullal, Duda and Breithaupt all sell under plans). Earlier rule note: re-test both complete current #11 paths (standard P/E ≤38, or high-velocity P/E ≤45 only with its growth/PEG/yield prerequisites); a narrow single-component shortfall may qualify for #14a only after every other entry check is verified. Gross margin compression beyond the carve-out; cloud-titan concentration >50% of revenue with any single customer down >20% YoY.
- **AMD** (alert): #11 on the stockanalysis basis re-enters; the up-to-$5B Anthropic commitment counted under #4 at maximum — any write-down → re-test; data-center GPU share loss two straight quarters.
- **VRT** (blackout): Q3 print must clear all four #19 legs, documenting any (d)-only exemption; an actual (a)–(c) miss is not exempt; UtilityInnovation earnout must be cash (A1); insider three-officer test each quarter; net debt/NTM FCF post-deal ≤2.5×.
- **TSM** (out on A3(c), Oct 24 history rerun): 2026 capex guide $60–64B puts NTM capex/OCF at 54–58% on consensus. 3a is closed by Q3 (2023 revenue NT$ −4.5%) until FY2028 reports. Re-entry trigger: NTM consensus capex ≤50% of NTM OCF (FY28 consensus reaches 48.8%); Arizona/Japan ramp costs pushing GM <55% → re-test.
- **Any 3a name**: high-water mark on entry.
- **Any M name** (revision 6, written before tranche 1): recovery fiscal year and its FY+2 consensus FCF margin at entry; out if that year's actual FCF margin is <6% when reported (no clock reset), if consensus for it falls <3% at two consecutive re-tests, if trailing-4Q OCF margin <18%, if net debt incl. leases/guarantees >1.5× trailing EBITDA, or on any financing/survival/transformative issuance. NTM cash capex >125% of NTM OCF freezes additions and forces an M re-test. Hyperscaler-type capex carries the full shared "AI capex 2027" trigger above, including tripwire B.
- **Any D name** (revision 7, written before tranche 1): FDSO baseline and the maximum base-case FDSO path for years 1–3; out on any issuance failing D1(c), actual trailing-4Q FDSO growth >10% or above the written path (excluding settlement of instruments in the entry baseline), trailing-4Q FCF margin <3% (D2(a) names) or a recovery year's actual FCF margin <6% when reported (no clock reset), for D2(c) names trailing-4Q OCF margin <15%, GAAP operating income ≤0 two quarters running, net debt >3.5× trailing EBITDA, stressed funding <18 months or recovery-year FCF consensus <3% at two consecutive re-tests, net debt >3.0× NTM FCF, book debt-to-equity ≥2.5×, or two consecutive prints with a material #19 trigger. Freeze additions and re-test if the D return falls <20% or the stress case <15%, next-FY organic growth consensus <20%, projected FDSO growth >8% a year, or capex/OCF rises above the level written at entry. Semi/AI-infra D names carry the full shared "AI capex 2027" trigger.

## Non-AI Diversification: watchlist and trigger prices (Oct 24, 2026 re-screen, revision 8)

Gate math: [`non-ai-screen-audit.md`](../../../../non-ai-screen-audit.md). Quotes are Oct 23 closes. Windows have no 200-day floor since revision 8 removed #12's void; ceilings are PT ÷ 1.2 unless #11/D5(a) binds lower. The Oct 15 list (UBER/HWM/LLY Tier 1 and the PODD…ASTS Tier 2 triggers) is superseded; its legacy 25% trigger prices have no basis under revision 6. Its per-name #15 drafts (HWM Alcoa/Grenfell exposure, LLY CVR/milestone leverage, PODD, NBIX and others) stay in the audit's Oct 15 history section for reuse.

### Tier 1: DASH (core A–E; #15 written before tranche 1)
- **Entry window:** ≤ $214.48 (PT $257.37 ÷ 1.2). Not within 5 trading days of the Nov 4 print (#13); after it, entry needs a fresh #19 check.
- **Kill / re-test triggers:**
  - Diluted WASO > +0.5% YoY, or any equity/convertible issuance, or a stock-funded deal above A1's de minimis carve-out.
  - Trailing-4Q FCF margin < 6%, or NTM consensus FCF below trailing FCF (A3); net debt incl. the $2.75B 2030 notes and leases > 2.5× NTM FCF.
  - Next-FY revenue consensus < 12% or forward 3Y revenue CAGR < 15% (#9).
  - US food-delivery share loss to Uber Eats or a new entrant for two straight quarters, or GAAP gross margin below the prior FY on a trailing basis (A5).
  - Net insider selling > 1.5% of shares over 12 months, or ≥ 3 officers selling outside 10b5-1 plans in one quarter (A7).
  - A8 re-test if a third party (robotaxi/robot-delivery operator or AI agent) starts routing orders around DASH at scale; if A8 then applies, DASH becomes a #10 alert with net buyback yield ≥ 2% as the trigger.
  - Governing return < 20% and forward revenue CAGR < 20% at a re-test freezes additions (revision 8 guardrail).

### Tier 1: RDDT (core A–E; A8 neutral by the user's call, Oct 25; #15 written before tranche 1)
- **Entry window:** ≤ $177.46 (PT ÷ 1.2). Entry from Nov 6, after the Oct 29 print clears #19 (#13).
- **Kill / re-test triggers:**
  - Diluted WASO > +1.5% YoY, or > +0.5% if buybacks stop or forward 3Y revenue CAGR falls below 25% (A1's band); any equity/convertible issuance, or a stock-funded deal above A1's de minimis carve-out.
  - Trailing-4Q FCF margin < 6%, or NTM consensus FCF below trailing FCF (A3); net debt incl. leases > 2.5× NTM FCF.
  - Next-FY revenue consensus < 12% or forward 3Y revenue CAGR < 15% (#9).
  - GAAP gross margin below the prior FY on a trailing basis (A5).
  - Net insider selling > 1.5% of shares over 12 months, or ≥ 3 officers selling outside 10b5-1 plans in one quarter (A7).
  - **A8 re-test** if US DAUq (logged-in, or total US DAUq once the split is dropped) falls YoY for two straight quarters, if US DAUq stops being disclosed, or if the Google data-licensing deal is not renewed or renews at a lower annual value. If A8 then applies, RDDT becomes a #10 alert with net buyback yield ≥ 2% (≈ $555M trailing-4Q buybacks) as the trigger.
  - Governing return < 20% and forward revenue CAGR < 20% at a re-test freezes additions (revision 8 guardrail).

### Tier 2: near-pass, exact unlocks
- **ARGX (core headline pass):** show that the Q3 2026 executive sales (Gubitz, Moorthy, Borgions, Lemmen, Wilk, DelGiacco) ran under discretionary management mandates or were non-discretionary (AFM/FSMA notices; A7 three-officer test); then window ≤ $957.16 (PT $1,148.59 ÷ 1.2). **#15 at entry:** Vyvgart net sales growth below consensus two straight quarters or FcRn class share loss to Imaavy/IMVT-1402; diluted WASO > +0.5%; net insider selling > 1.5% or a confirmed ≥3-officer discretionary quarter; opex above guidance without matching sales.
- **RHM.DE (D-watch):** window ≤ €1,309.01 (PT ÷ 1.2) once (1) Q2 sales vs consensus and a clean Nov 5 print clear #19; (2) an A5 share source is recorded. D4 passes on EPS; D5(b) 25.3%/20.3% on one basis. No entry Oct 29–Nov 12 (#13). **#15 at entry:** FY2026 recovery-year FCF margin < 6% when reported (no clock reset); trailing-4Q FCF negative; net debt > 3.0× NTM FCF; D/E ≥ 2.5×; next-FY EPS growth consensus < 20%.
- **KOG.OL (core headline pass):** clean Oct 29 Q3 print (#19), Oslo Newsweb directors'-dealings sweep (#7), A3(b) NTM FCF ≥ trailing; then window ≤ NOK 332.04 (PT NOK 398.45 ÷ 1.2). **#15 at entry:** Defence & Aerospace book-to-bill < 1.0 two straight quarters; EBIT margin below the prior FY for two straight quarters; any share issuance.
- **LLY (core except #12):** PT leg at ≤ $1,109.63, or the #16 ballast slot; entry from Nov 6 after a clean Oct 29 print. Lilly Endowment plus insiders > 1.5% net selling, or a ≥3-officer discretionary quarter, trips #7.

### Alert and Rule B (zero capital)
- **NBIX / KRYS:** G3 re-test at the Nov 2 prints (diluted shares ≤ +3.0% YoY on SEC counts); G5 refresh (Oct 15 ceilings $175 / ~$275).
- **HWM:** core gates pass on headline (no #12 void); core-eligible at ≤ $270.46 if the Oct 29 print clears #19 and like-for-like PEG ≤ 2.0; below the 20% growth door, so not a list name (yardstick line 21.1%).
- **AXON:** D window ≤ $317.6 (D5(c) stress binds; D5(b) ≤ $370.6) after D1(c), D2 recovery-year, A7 and #19 checks.
- **DKNG:** PH-impaired; G headline candidate once PH-recovery verifies.
- **UBER:** #10 waiver; below the growth door on consensus (sleeve-plan line governs).
- **HALO (added after the next-FY correction):** core gates pass on headline (derived PEG ~0.83, A4 ~2.4× trailing FCF, #12 on FCF yield 5.7%); below every growth door (15.2% return). Re-test at the Nov 5 print; A4 > 2.5× on NTM FCF trips it.
