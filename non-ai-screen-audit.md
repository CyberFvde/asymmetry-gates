# Open-Universe Non-AI-Capex Diversification Screen Audit (`asymmetry-gates`)

**Repository Baseline:** `https://github.com/CyberFvde/asymmetry-gates` — **Policy Revision 5 (`f6171aa`, October 15, 2026)**  
**Screen Scope:** Open-Universe Discovery across 9 Non-AI-Capex Lanes (24 Seed Anchors + 87+ `[NEW DISCOVERY]` Expansion Candidates = **111+ Total Audited Securities**)  
**Discovery Guardrails:** Market Cap >= $2.5B | Liquidity >= $25M ADV | Plausible mathematical path to >= 25% annualized 3Y IRR (3Y EPS/FCF CAGR + net buyback yield +/- multiple normalization)  

---

## 1. Executive Summary & Policy Revision 5 Gate Thresholds

Every candidate across all 9 lanes was audited with **zero rule softening** against the exact numeric thresholds in `SKILL.md`, `framework.md`, `stage-paths.md`, `fintech.md`, `price-health.md`, `triggers.md`, `README.md`, and `changelog.md`:

- **Stage A (Hard Disqualification Gates):**
  - **`A1` (Dilution & Issuance):** Diluted WASO <= `+0.50%` YoY (`<= +1.50%` ONLY if gross buybacks > 0 in last 4Q AND forward revenue growth >= 25%). Any financing/survival issuance (convertible note, secondary, ATM, convert-for-equity exchange, transformative stock M&A) in TTM or pending = **OUT** regardless of size. *Rev 5 Carve-out:* De minimis stock-settled bolt-ons, acqui-hires, and contingent share earnouts may aggregate to `<= 0.50%` of diluted shares over TTM (including max pending payout) provided total diluted WASO stays within the `A1` ceiling.
  - **`A2` (Buybacks / Net Cash):** Gross share repurchases > 0 in last 4Q, OR net cash with diluted share count <= `+0.50%` YoY.
  - **`A3` (Cash Engine):** `(a)` Actual TTM Company FCF margin (`OCF - cash PP&E`, no SBC addbacks) >= `6.0%` (`8.0%` under `FT` overlay); `(b)` NTM consensus FCF >= TTM FCF; `(c)` guided/consensus capex <= `50%` of NTM OCF (qualitative "growing/elevated" capex guidance without a dollar range defaults to `1.25x` trailing cash PP&E).
  - **`A4` (Leverage):** Pro forma Net Debt / NTM FCF <= `2.50x` at maximum exposure (including target net debt, max earnouts/CVRs/milestones, off-balance-sheet/JV guarantees, redeemable noncontrolling interests, and vendor financing).
  - **`A5` (Moat & Gross Margin):** Top-2 share or structural oligopoly, AND NTM GM >= prior FY (or within the gross-profit-growth mix carve-out, capped at `-600bp`).
  - **`A6` (Secular Tailwind):** Core end-market growing faster than GDP; no balance-sheet banks or insurers.
  - **`A7` (`#7` Insiders, Endowments & Legal):** TTM insider net selling (Code `S` minus Code `P`, including `10b5-1`, sell-to-cover, and >10% holders/endowments such as Lilly Endowment) <= `0.50%` of shares out; AND no single quarter with >= 3 officers making discretionary open-market sales outside `10b5-1` (Rev 5 footnote fallback: if raw Form 4 footnotes unavailable, passes with watch note only if verified 12m net insider selling <= `0.15%` AND no C-suite officer disposed of >15% of holdings). Foreign filers without Form 4 must be verified via local PDMR registries (AMF, Oslo Newsweb, BaFin, AFM/FSMA, RNS) or remain alert-only (`$0` capital). Legal RPL > `5.0%` of NTM FCF or structural antitrust remedy = **OUT**.
  - **`A8` (AI Posture):** AI tailwind or neutral; third-party disintermediation risk (`UBER`, `LYFT`) routes to **`#10` Waiver only** with a written `#15` trigger.
- **Stage B (Growth):**
  - **`#9` (Core Growth):** Fwd 3Y revenue CAGR >= `15.0%` AND next-FY organic revenue growth >= `12.0%` (`>= 15.0%` for both under `FT1`).
  - **`#10` (Growth Waiver):** Next-FY AND fwd 3Y revenue growth >= `10.0%`, NTM FCF yield >= `5.0%`, PEG < `1.00`, net buyback yield >= `2.0%`, and fwd 3Y EPS CAGR >= `20.0%`.
- **Stage C–E (Valuation, Asymmetry, Starters & Blackout):**
  - **`#11` (Core Valuation — Rev 5):** Must pass one complete path (no mixing):
    - *Standard Core:* Fwd P/E <= `38.0x` AND PEG <= `2.00` AND NTM FCF yield >= `1.50%`.
    - *High-Velocity Core:* (Fwd 3Y EPS CAGR >= `30.0%` OR Fwd 3Y rev CAGR >= `25.0%`) AND PEG <= `1.65` AND Fwd P/E <= `45.0x` AND NTM FCF yield >= `1.15%`.
  - **`#12` (Asymmetry):** Consensus PT upside >= `+20.0%` (>= 5 analysts) OR NTM FCF yield >= `5.0%`. **PT leg is VOID if current price is >20% below the 200DMA.**
  - **`#14a` (Funded Starter — Rev 5):** All of Stage A verified, `#12/#13/#19` clear, and fails *only* `#9` (`3Y rev >= 12.0%` and `next-FY organic >= 10.0%` with full `#11` pass) OR fails *exactly one* component of `#11` (`P/E <= 48.0x`, `PEG <= 2.50`, `NTM FCF yield >= 1.00%`) with `#9` fully passed. Prohibited for `FT` and `#10`-only names.
  - **`#16` (Ballast Slot):** One ballast slot: wide moat, passes all of Stage A and `#9/#11/#19`, fails *only* `#12`.
  - **`#19` (Entry Blackout):** Most recent print missed consensus rev/GB by >2%, missed adj EPS/EBITDA by >3%, missed own guided low end, or guided next-Q midpoint >3% below pre-print consensus.
- **Stage Paths (`G`, `H`, `FT`, `F`) & Price Health (`PH`):**
  - **Route `G` (Proven Compounder):** Non-fintech, non-commodity/IPP; actual TTM FCF margin >= `6.0%`, 2 completed FYs of positive OCF, NTM FCF >= `90%` of TTM, Capex <= `50%` OCF, Net Debt/NTM FCF <= `2.5x`, next-FY & 3Y organic rev >= `10.0%`, 3Y FCF/sh CAGR >= `12.0%`, `G3` net dilution <= `3.00%` YoY, `G4` net insider selling <= `0.50%`, and `G5` 5Y base annualized return >= `12.0%` (`bear Y5 >= 60%`).
  - **Route `H` (Early Transition):** Non-fintech, non-commodity/IPP; `H1` achieved technical milestone + commercial revenue/contract, `H2` 24m cash runway with `25%` overrun buffer, `H3` <=5Y deadline to >=6% FCF margin, `H4` 5Y diluted model base return >= `20.0%/yr`, `H5` insider selling <= `0.50%`.
  - **Overlay `FT` (`fintech.md`):** No `#14a` starters, no Route `G` or `H`; `#9` requires >= `15%` on both legs; `FT2` strips client/segregated cash & credit books; `FT4` bars crypto-price, retail-volume-burst, or peak-NII rate dependence.
  - **Route `F` (Commodity/Uranium):** Mandatory for commodity producers (`CCJ`, `KAP.L`, `UEC`, `NXE`, `UUUU`); requires `F1` (`P/E <= 15x`, `PEG <= 0.75`, `EV/EBITDA <= 11x`, `EBITDA margin >= 30%`, `FCF margin >= 10%`, `3Y EPS >= 25%`, buybacks > 0, zero issuance) AND `F2` (open-market CEO/CFO/founder purchase >= `$2M` & >= `5%` holding within 30d, or >= 3 insiders buying in 90d).
  - **Overlay `PH` (`price-health.md`):** `PH-impaired` (ATH >= 3Y old AND drawdown >= `30%` AND 3Y total-return underperformance vs S&P 500 >= `20pp`) blocks all new capital unless in verified `PH-recovery`.

---

## 2. Ranked Top 25 Non-AI-Capex Table (Rule A Cutoff at #14 + Rule B Honorable Mentions #15–#30)

### Primary Ranked Table (#1 to #14 — Rule A Strict Quality & >=25% IRR Cutoff)

> **Rule A Enforcement:** Across all 111+ evaluated equities in Lanes 1–9, **exactly 14 stocks** legitimately clear both the `asymmetry-gates` business quality/balance-sheet architecture AND a mathematically plausible **>= 25% annualized 3-year IRR** (at current or near-pass trigger prices). Per Rule A, the primary table cuts off strictly at **#14** rather than padding Ranks #15–#25 with sub-25% IRR or structurally flawed names.

| Rank | Ticker | Company (`[NEW DISCOVERY]` Tag) | Lane | Tier & Route Status | Price (Oct 2026) | 3Y EPS / FCF CAGR | Net Buyback / Yield | Est. 3Y IRR | `A1` Dilution / `A3` FCF Margin / `A4` Leverage | `#11` Fwd P/E & PEG | Exact Dollar Buy Trigger |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :--- | :---: | :--- |
| **1** | **`UBER`** | Uber Technologies (Seed) | L2 | **Tier 1 Pass** (`#10` Waiver + `#15`) | `$71.50` (`$69.62` 9/28) | `30.9%` / `26.5%` | `+2.28%` | **`31.5%`** | `WASO -3.55%` / `FCF 19.4%` (`Capex 6.5%`) / `ND 1.50x` (w/ DH cash) | `17.0x` / `0.62` (`8.7%` FCF yld) | **Actionable Now (`<= $84.00`)** |
| **2** | **`HWM`** | Howmet Aerospace (Seed) | L1 | **Tier 1 Pass** (Rev 5 Core @ `$216.84` / `#14a` @ `$231.27`) | `$216.84` (`$231.27` 10/2) | `26.7%` / `24.5%` | `+1.10%` | **`27.8%`** | `WASO -1.05%` / `FCF 19.6%` (`Capex 19.4%`) / `ND 2.40x` (w/ `$1.14B` Alcoa) | `36.7x` / `1.29` (`2.5%` FCF yld) | **Actionable Now `<= $221.65–$224.58` (Rev 5 `38x`)**; Legacy `35x`: `<= $204.15–$206.80`; `#14a`: `<= $279.84` |
| **3** | **`LLY`** | Eli Lilly and Co. (Seed) | L4 | **Tier 1 Ballast Pass Now** (1-Step to Core on `#12`) | `$1,142.85` | `30.95%` / `32.0%` | `+1.12%` (bb+div) | **`26.5%`** | `WASO -0.68%` / `FCF 22.8%` (`Capex 20.4%`) / `ND 1.77x–2.21x` (max CVRs) | `27.4x` / `1.27` (`2.8%` FCF yld) | **Ballast Now (`<= $1,143`)**; **Full Core Trigger: `<= $1,107.36`** (`+20%` PT) |
| **4** | **`PODD`** | Insulet Corp **`[NEW DISCOVERY]`** | L4 | **Tier 2** (`1-Step Core / G-Watch` on `#12` 200DMA + capex fallback) | `$131.69` | `23.06%` / `25.0%` | `+1.19%` | **`28.4%`** | `WASO -1.77%` / `FCF 9.6%` (`Capex 34%` w/ `1.25x`) / `ND 1.09x–1.36x` | `19.1x` / `0.96` (`4.81%` adj yld) | **`<= $126.76`** (blended `5%` FCF yld) / **`<= $108.35`** (full `1.25x` capex) or Nov 4 Q3 print |
| **5** | **`NBIX`** | Neurocrine Biosciences **`[NEW DISCOVERY]`** | L4 | **Tier 2** (`G-Watch` — 17bp over Rev 5 `G3` `3.0%` cap) | `$143.18` | `40.9%` / `29.0%` | `0.0%` (`$300M` auth) | **`27.5%`** | `WASO +3.17%` (`17bp > G3`) / `FCF 25.8%` (`Capex 3.1%`) / `Net Cash` | `12.7x` / `0.31` (`7.8%` FCF yld) | **`<= $175.00`** once Oct 27 Q3 print brings YoY WASO `<= +3.00%` |
| **6** | **`KOG.OL`** | Kongsberg Gruppen **`[NEW DISCOVERY]`** | L5 | **Tier 2** (`1-Step Core Watch` — in `#19` blackout until Oct 29) | `NOK 308.00` | `34.8%` / `30.0%` | `+1.2%` | **`26.5%`** | `Shares flat` / `FCF ~18%` (`Capex 24%`) / `Net Cash` (`#7` Oslo Newsweb clean) | `33.4x` / `0.96` (`3.2%` FCF yld) | **Clean Oct 29 Q3 print** at **`<= NOK 350.30`** (`38x` Core; `<= NOK 322.66` at `35x`) |
| **7** | **`SAF.PA`** | Safran SA **`[NEW DISCOVERY]`** | L1 | **Tier 2** (`G-Watch` — testing `G5` entry zone) | `€314.90` (`€330.10` 10/2) | `24.85%` / `21.0%` | `+1.20%` | **`25.4%`** | `WASO +1.65%` (`G3 <=3%` pass) / `FCF 14.8%` (`Capex 22%`) / `Net Cash` | `26.2x` / `1.05` (`3.5%` FCF yld) | **`<= €310.00–€323.00`** (`G5` `12.0%` 5Y base return ceiling) |
| **8** | **`ARGX`** | argenx SE (Seed) | L4 | **Tier 2** (`G-Watch` — awaits FY26 2nd pos OCF yr Feb 2027) | `$810.00` | `32.75%` / `35.0%` | `-1.80%` | **`28.5%`** | `WASO +1.80%` (`G3` pass) / `FCF 19.5%` (`Capex <5%`) / `Net Cash -$5.1B` | `29.7x` / `0.85` (`1.9%` FCF yld) | **`<= $785.00`** (`G5` ceiling) after Feb 2027 FY26 2nd positive OCF yr + AFM sweep |
| **9** | **`ATI`** | ATI Inc. **`[NEW DISCOVERY]`** | L1 | **Tier 2** (`#14a / G-Watch` — 10bp shy of `10%` FY27 rev floor) | `$189.50` | `32.26%` / `28.5%` | `+1.80%` | **`26.8%`** | `WASO -1.80%` / `FCF 9.9%` (`Capex 28%`) / `ND 2.45x <= 2.50x` | `36.4x` / `1.13` (`2.3%` FCF yld) | **`<= $175.00`** + FY27 organic rev consensus `>= 10.0%` (currently `9.9%`) |
| **10** | **`WWD`** | Woodward, Inc. **`[NEW DISCOVERY]`** | L1 | **Tier 2** (`#14a / G-Watch` — awaits Nov FY27 FCF rollover) | `$331.62` | `19.2%` / `18.5%` | `+1.12%` | **`25.6%`** (at `$305`) | `WASO -1.12%` / `FCF 9.0%` (`Capex 23.5%`) / `ND 2.19x` (on FY27E FCF) | `32.4x` / `1.69` (`2.1%` FCF yld) | **`<= $305.00`** + Nov FY27 FCF guide `>= $377M` (curing `A3b`/`A4`) |
| **11** | **`HEI`** | HEICO Corporation (Seed) | L1 | **Tier 2** (`G-Watch` — above `G5` ceiling; redeemable NCI check) | `$302.45` | `18.61%` / `18.0%` | `0.0%` | **`25.1%`** (at `$275`) | `WASO +0.35%` / `FCF 19.2%` (`Capex 7.5%`) / `ND 1.88x` (`2.55x` w/ `$618M` NCI) | `44.0x` / `2.36` (`2.3%` FCF yld) | **`<= $275.00` (NCI-adj) to `$296.00`** (`G5` `12%` 5Y base return ceiling) |
| **12** | **`CART`** | Maplebear / Instacart **`[NEW DISCOVERY]`** | L2 | **Tier 2** (`#10 / #14a Watch` — 50bp shy of `#10` `20%` EPS floor) | `$49.40` | `19.50%` / `18.5%` | `+4.20%` | **`25.2%`** (at `$48.50`) | `WASO -4.20%` / `FCF 20.5%` (`Capex 5.5%`) / `Net Cash -$851M` | `18.5x` / `0.95` (`6.2%` FCF yld) | **`<= $48.50`** + 3Y EPS CAGR `>= 20.0%` (`#10`) or 3Y rev `>= 12.0%` (`#14a`) |
| **13** | **`KRYS`** | Krystal Biotech **`[NEW DISCOVERY]`** | L4 | **Tier 2** (`G-Watch` — fails Core `A1` no buyback & `#12` PT `+18.2%`) | `$331.80` | `24.60%` / `28.0%` | `-1.46%` | **`26.0%`** (at `$275`) | `WASO +1.46%` (`G3` pass) / `FCF ~34%` (`Capex <8%`) / `Net Cash -$750M` | `40.8x` / `0.93` (`2.6%` FCF yld) | **`<= $275.00`** (`G5` ceiling; `#12` clears at `<= $326.75` + Form 4 check) |
| **14** | **`ADMA`** | ADMA Biologics **`[NEW DISCOVERY]`** | L4 | **Tier 2** (`G-Watch` — borderline `$2.44B` cap, `A1` `+1.15%`, `#9` `12.7%`) | `$10.20` | `22.26%` / `24.0%` | `-1.15%` | **`25.5%`** (at `$9.50`) | `WASO +1.15%` (`G3` pass) / `FCF ~22%` (`Capex 14.8%`) / `Net Cash` | `14.5x` / `0.65` (`4.8%` FCF yld) | **`<= $9.50`** (`G5` ceiling once Mkt Cap `>= $2.5B` & 12m Form 4s verified) |

---

### Rule B — Honorable Mentions / Single-Gate Blocker & Valuation Watchlist (#15 to #30)

> **Rule B Enforcement:** The 16 candidates below represent elite franchises, category monopolies, or high-velocity inflection plays blocked by `#11`/`G5` Valuation, `A1` Dilution, `FT1` Growth Floors, `A7` Officer Roll-Offs, or `H2/H4` Transition Caps. Each has an exact dollar trigger price where both its blocking gate(s) and the `>= 25%` 3Y IRR hurdle are resolved.

| HM Rank | Ticker | Company (`[NEW DISCOVERY]` Tag) | Lane | Current Tier & Route | Price (Oct 2026) | 3Y Rev / EPS CAGR | Est. 3Y IRR @ Spot (`@ Trigger`) | Specific Gate Blocker(s) | Exact Dollar Buy Trigger & Unlock Condition |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| **15** | **`TW`** | Tradeweb Markets **`[NEW DISCOVERY]`** | L7 | **Tier 2** (`A–E + FT`) | `$111.08` (`$102.22` 10/2) | `12.1%` / `15.0%` | `14.5%` (**`25.4%`**) | `FT1` bars `#14a` starters; misses `#9` (`12.1% < 15%`), `#10` (`15% < 20%`), `#12` (`4.4%` FCF yld) | **`<= $82.00`** (`>=5.0%` FCF yield & `25%+` IRR) + print guiding `>=15%` org rev or `>=20%` EPS |
| **16** | **`SCHW`** | Charles Schwab **`[NEW DISCOVERY]`** | L7 | **Tier 2** (`A–E + FT`) | `$96.70` | `13.0%` / `22.7%` | `21.5%` (**`25.0%`**) | Passes `#10` (`22.7%` EPS) & `#11` (`P/E 14.9x`), but **Hard `A7` Fail** (4 officers sold non-plan in Q1/Q3 2026) | **`<= $95.00`** after **Q3 2027** (`12m` officer-sale roll-off) + clean bank-sweep `FT2` FCF |
| **17** | **`ISRG`** | Intuitive Surgical (Seed) | L4 | **Tier 2** (`G-Watch`) | `$391.95` | `14.1%` / `15.1%` | `14.8%` (**`25.0%`**) | Fails **both** `#9` (`14.11% < 15%`) and `#11` (`PEG 2.25 > 2.0` — cannot combine two `#14a` shortfalls) | **`<= $339.00`** (`G5` `12%` base return ceiling) or **`<= $348.40`** (`PEG <= 2.00` for `#14a` starter) |
| **18** | **`FTNT`** | Fortinet (Seed) | L6 | **Tier 2** (`G-Watch`) | `$80.19` | `10.7%` / `10.7%` | `12.8%` (**`25.0%`**) | Fails `#9` (`10.67%`), `#11` (`PEG 2.34`), `#12` (`PT +11.8%`, `FCF yld 4.3%`), & `G5` (`8.98%` return) | **`<= $72.24`** (`G5` `12.0%` base return ceiling; **`<= $69.00`** for `5.0%` `#12` FCF yield) |
| **19** | **`REGN`** | Regeneron Pharma **`[NEW DISCOVERY]`** | L4 | **Tier 2** (`G-Watch`) | `$735.20` | `11.4%` / `15.7%` | `17.5%` (**`25.0%`**) | Passes `#11` (`P/E 12.0x`) & `#12` (`8.59%` FCF yld), but fails `#9/#10` & `G5` (`8.1%` return at `$735`) | **`<= $617.00`** (`G5` `12.0%` base return ceiling, provided FY27 organic rev holds `>= 10%`) |
| **20** | **`CVLT`** | Commvault Systems **`[NEW DISCOVERY]`** | L6 | **Tier 2** (`G-Watch`) | `$152.00` | `11.1%` / `18.6%` | `15.5%` (**`25.0%`**) | Passes `A1–A7` & `#11` (`P/E 28.6x`), fails `#9` (`11.07%`), `#10` (`18.6%`), `#12` (`+5.6%` PT), & `G5` | **`<= $131.50`** (`G5` `12.0%` base return ceiling) |
| **21** | **`CRS`** | Carpenter Technology **`[NEW DISCOVERY]`** | L1 | **Tier 3 / 2** (`G-Watch`) | `$375.00` | `11.0%` / `21.1%` | `21.8%` (**`25.2%`**) | Passes `A1–A7`, `#11` (`P/E 28.5x`), `#12` (`+53.5%` PT), but `#9` 3Y rev `10.97% < 12%` `#14a` floor | **`<= $335.00`** (`G5` ceiling once next-FY organic rev confirms `>= 10.0%`) |
| **22** | **`CRWD`** | CrowdStrike Holdings (Seed) | L6 | **Tier 2 / 3** (`G-Watch`) | `$436.32` | `20.5%` / `23.2%` | `15.8%` (**`25.5%`**) | Fails Core `A1/A2` (`WASO +1.26%` w/ `0.09%` buyback), `#11` (`P/E 76.2x`, `PEG 3.29`), `#12`, & `G5` | **`<= $265.24`** (`G5` `12.0%` base return ceiling at `25x` terminal P/FCF) |
| **23** | **`KAP.L`** | Kazatomprom GDR **`[NEW DISCOVERY]`** | L9 | **Tier 2** (`Route F`) | `$62.50` | `14.5%` / `16.5%` | `19.5%` (**`25.5%`**) | Only uranium miner passing `F1` valuation (`P/E 10.8x`, `EV/EBITDA 7.28x`), but lacks `F1` buyback/`25%` EPS & `F2` insider buy | **`<= $52.00`** (`>=25%` 3Y IRR incl. ~6% div) + `F2` `$2M+` insider buy + 1Q token share buyback |
| **24** | **`DASH`** | DoorDash, Inc. (Seed) | L2 | **Tier 3** (`A1` / `G5` Fail) | `$191.99` | `17.3%` / `42.2%` | `28.4%` (**`29.5%`**) | Fails `A1` (Q2 10-Q diluted WASO `+1.82% > +1.50%` cap on Deliveroo/SevenRooms stock), `G5` (`<12%`), & `#8/#10` (`3.7%` FCF yld) | **`<= $155.00`** (`G5 >= 12%` & `>=5.0%` FCF yield) + YoY diluted WASO `<= +1.50%` |
| **25** | **`MELI`** | MercadoLibre, Inc. (Seed) | L3 | **Tier 3** (`A3b/FT2/A5` Fail) | `$1,696.56` | `32.0%` / `31.5%` | `29.2%` (**`31.0%`**) | Fails `A3b` (FY26E FCF `-1.9%` vs TTM), `FT2/A3a` (`~3.3% < 6%` ex-credit FCF margin), & `A5` (`-858bp` GM compression `> -600bp` cap) | **`<= $1,450.00`** + `FT2` ex-credit FCF margin `>= 8.0%`, `A3b >= 100%`, & GM compression `<= 600bp` |
| **26** | **`SE`** | Sea Limited (Seed) | L3 | **Tier 3** (`A1/A2` + `FT1` Fail) | `$95.19` | `20.5%` / `34.0%` | `27.5%` (**`29.0%`**) | Fails `A1` (`WASO +2.70%` YoY from converts/SBC) & `A2` (`0` buybacks), and `FT1` prohibits Route G for Monee fintech arm | **`<= $80.00`** + active share buybacks bringing YoY diluted WASO `<= +0.50%` (`A1/A2`) |
| **27** | **`KRMN`** | Karman Holdings **`[NEW DISCOVERY]`** | L1 | **Tier 2** (`H-Watch` Only) | `$30.14` | `21.3%` / `27.8%` | `22.5%` (**`26.0%`**) | Passes Rev 5 `A1` bolt-on carve-out (`0.154%`), but fails `A3a` (`-$27.7M` TTM FCF), `A4` (`9.5x`), `#12` void (`-55%` vs 200d), & 3 ICFR weaknesses | **`<= $24.56`** (`H4` `20%` 5Y return ceiling) + remediation of 3 ICFR material weaknesses |
| **28** | **`MDGL`** | Madrigal Pharma **`[NEW DISCOVERY]`** | L4 | **Tier 2** (`H-Watch` Only) | `$499.00` | `~65.0%` / N/A | `17.0%` (**`25.0%`**) | Fails `A1/G3` (`+11%` shares) & `A3a/G2` (`-$80M+` FCF during Rezdiffra launch); fails `H4` (`<20%` 5Y return) at `$499` | **`<= $397.00`** (`H4` `20.0%` 5Y base return ceiling) + `H3/H5` documentation |
| **29** | **`AVAV`** | AeroVironment **`[NEW DISCOVERY]`** | L5 | **Tier 2 / 3** (`H-Watch` / Core Fail) | `$120.60` | `16.5%` / `24.0%` | `8.5%` (**`25.0%`**) | Fails `A1` (`+6.27%` WASO; ESAero stock deal `1.33% > 0.50%` cap), `A3a` (`-$25.0M` TTM FCF), `#12` void, & `H4` (`8.5%` return) | **`<= $72.88`** (`H4` `20.0%` 5Y base return ceiling) + ICFR & class-action resolution |
| **30** | **`ASTS`** | AST SpaceMobile (Seed) | L8 | **Tier 2** (`H-Watch` Only) | `$42.14` | `>100%` / Neg->Pos | `5.0%` (**`25.0%`**) | Blocked by `#19a` Q2 rev miss (`-8.64%`), `#17` FY27 cut (`-10.6%`), `H2` (`$1.71B` 24m stressed gap), `H4` (`$104.86` hurdle), & `H5` (`1.45%` strategic sales) | **`<= $22.00`** after clean Q3 print (`#19a` exit) + non-dilutive Ex-Im/FirstNet `H2` funding |

---

## 3. Three-Tier Classification Summary (All 111+ Evaluated Securities)

### Tier 1: Gate Passes — Ready Now (3 Stocks)
1. **`UBER` (Lane 2 Seed — Waiver `#10` + `#15` Pass):** Actionable Now at `$69.62–$71.50` (Buy up to **`$84.00`**). Est. 3Y IRR: **`31.5%`**.
2. **`HWM` (Lane 1 Seed — Policy Rev 5 Standard Core Pass at `$216.84` / `#14a` Starter at `$231.27`):** Actionable Now up to **`$221.65–$224.58`** (Rev 5 `38x` Core ceiling; Legacy `35x` ceiling: **`$204.15–$206.80`**; `#14a` Starter ceiling: **`$279.84`**). Est. 3Y IRR: **`27.8%`**.
3. **`LLY` (Lane 4 Seed — E16 Ballast Slot Pass Now at `$1,142.85` / 1-Step to Full Core):** Actionable Now in the **Ballast Slot** (`<= 4%` initial / `8%` max); converts to **Full Core Pass at `<= $1,107.36`** (`+20.0%` PT upside). Est. 3Y IRR: **`26.5%`**.

### Tier 2: Near-Pass Watchlist — Blocked by Valuation, Single Gate, or Dated Print (23 Stocks)
- **Lane 1 (6):**
  - `SAF.PA` `[NEW DISCOVERY]` (`G-watch`): Buy **`<= €310.00–€323.00`** (`G5` `12%` base return ceiling; spot `~€314.90`).
  - `HEI` (Seed, `G-watch`): Buy **`<= $275.00` (NCI-adjusted) to `$296.00`** (`G5` `12%` base return ceiling; spot `$302.45`).
  - `WWD` `[NEW DISCOVERY]` (`#14a / G-watch`): Buy **`<= $305.00`** + Nov FY27 FCF guide `>= $377M` (spot `$331.62`).
  - `ATI` `[NEW DISCOVERY]` (`#14a / G-watch`): Buy **`<= $175.00`** + FY27 organic rev consensus `>= 10.0%` (spot `$189.50`).
  - `CRS` `[NEW DISCOVERY]` (`G-watch` borderline): Buy **`<= $335.00`** + next-FY organic rev `>= 10.0%` (spot `$375.00`).
  - `KRMN` `[NEW DISCOVERY]` (`H-watch` only): Buy **`<= $24.56`** (`H4` `20%` return ceiling) + ICFR remediation (spot `$30.14`).
- **Lane 2 (1):**
  - `CART` `[NEW DISCOVERY]` (`#10 / #14a watch`): Buy **`<= $48.50`** + `>= 20.0%` 3Y EPS CAGR or `>= 12.0%` 3Y rev CAGR (spot `$49.40`).
- **Lane 3 (0):** Zero Tier 1 or Tier 2 survivors (`FT1` bars `#14a`/G/H for fintech arms of `MELI`/`SE`, and standalone e-commerce names fail `A3`/`PH`).
- **Lane 4 (8):**
  - `PODD` `[NEW DISCOVERY]` (`1-Step Core / G-watch`): Buy **`<= $126.76`** (blended `5%` FCF yield) / **`<= $108.35`** (full `1.25x` capex fallback) or Nov 4 Q3 print (spot `$131.69`).
  - `NBIX` `[NEW DISCOVERY]` (`G-watch`): Buy **`<= $175.00`** once Oct 27 Q3 print brings YoY diluted WASO `<= +3.00%` (currently `+3.17%`, spot `$143.18`).
  - `ARGX` (Seed, `G-watch`): Buy **`<= $785.00`** post-Feb 2027 FY26 2nd positive OCF year + AFM/FSMA insider sweep (spot `$810.00`).
  - `ISRG` (Seed, `G-watch` / `#14a`): Buy **`<= $339.00`** (`G5` ceiling) or **`<= $348.40`** (`PEG <= 2.00` for `#14a`, spot `$391.95`).
  - `REGN` `[NEW DISCOVERY]` (`G-watch`): Buy **`<= $617.00`** (`G5` ceiling, spot `$735.20`).
  - `KRYS` `[NEW DISCOVERY]` (`G-watch`): Buy **`<= $275.00`** (`G5` ceiling; `#12` clears at `<= $326.75`, spot `$331.80`).
  - `ADMA` `[NEW DISCOVERY]` (`G-watch`): Buy **`<= $9.50`** (`G5` ceiling once Mkt Cap `>= $2.5B` & Form 4s verified, spot `$10.20`).
  - `MDGL` `[NEW DISCOVERY]` (`H-watch` only): Buy **`<= $397.00`** (`H4` `20%` return ceiling, spot `$499.00`).
- **Lane 5 (2):**
  - `KOG.OL` `[NEW DISCOVERY]` (`1-Step Core Watch` in `#19` blackout): Buy **`<= NOK 350.30`** (`38x` Core; `<= NOK 322.66` at `35x`) on clean Oct 29 Q3 print (spot `NOK 308.00`).
  - `AVAV` `[NEW DISCOVERY]` (`H-watch` distant): Buy **`<= $72.88`** (`H4` `20%` return ceiling) + ICFR remediation (spot `$120.60`).
- **Lane 6 (3):**
  - `FTNT` (Seed, `G-watch`): Buy **`<= $72.24`** (`G5` ceiling) / **`<= $69.00`** (`5.0%` `#12` FCF yield, spot `$80.19`).
  - `CVLT` `[NEW DISCOVERY]` (`G-watch`): Buy **`<= $131.50`** (`G5` ceiling, spot `$152.00`).
  - `CRWD` (Seed, `G-watch` distant): Buy **`<= $265.24`** (`G5` ceiling, spot `$436.32`).
- **Lane 7 (2):**
  - `TW` `[NEW DISCOVERY]` (`A–E + FT` watch): Buy **`<= $82.00`** (`>=5.0%` FCF yield & `25%+` IRR) + print guiding `>= 15%` org rev or `>= 20%` EPS (spot `$111.08`).
  - `SCHW` `[NEW DISCOVERY]` (`A–E + FT` watch): Buy **`<= $95.00`** after **Q3 2027** (`A7` 12m officer-sale roll-off, spot `$96.70`).
- **Lane 8 (1):**
  - `ASTS` (Seed, `H-watch` only): Buy **`<= $22.00`** after clean Q3 print (`#19a` exit) + non-dilutive `H2` `$1.71B` gap funding (spot `$42.14`).
- **Lane 9 (1):**
  - `KAP.L` `[NEW DISCOVERY]` (`Route F` watch): Buy **`<= $52.00`** + `F2` `$2M+` insider buy + 1Q token buyback (spot `$62.50`).

### Tier 3: Hard Gate Fails (78 Stocks — With Exact Disqualifying Gate Codes)
- **Lane 1 (8):** `FTAI` (`A1`, `A2`, `A3a` `-40.8%` FCF margin, `A3c` `>100%` engine capex, `A4` `>6.0x`, `#12` PT void `-30.8%` vs 200DMA); `TDG` (`A4/G2` `14.3x–15.9x` Net Debt/FCF, `#9` `9.96% < 10%`, `<25% IRR`); `LOAR` (`A1` `+4.8%` WASO, `A2`, `A4` `7.10x`); `CW` (`#9/#10/G2` `8.8%` rev, `#11` PEG `2.15`, `#12` PT void `-26.0%` vs 200DMA, `<25% IRR`); `GE` (`#9/#10/G2` 3Y rev `9.94% < 10%`, `#11` PEG `2.14`, `<25% IRR`); `RTX` (`A1` `+0.81%`, `A2` no buybacks, `A3b`, `A4` `3.03x`, `#9` `7.65%`, `#11` PEG `2.55`, `#12`, `<25% IRR`); `AAR` (`A1` `+12.4%` equity raise, `A2`, `A3a` `1.0%` FCF margin, `A3c` `83.3%`, `A4` `5.80x`, `#9` `8.38%`); `MTU.DE` (`A3a/G2` `4.8% < 6%` FCF margin on GTF payments, `#9`, `#12`, `<25% IRR`).
- **Lane 2 (7):** `DASH` (`A1` Q2 10-Q WASO `+1.82% > 1.50%`, `G5` `<12%`, `#8/#10` FCF yield `3.7% < 5%`); `BKNG` (`#9/#10/G2` 3Y rev `8.79% < 10%`, `<25% IRR`); `ABNB` (`#9` `10.42%` + `#12` PT `+8.5%` & FCF yield `4.7%`, `PH-warning`, `<25% IRR`); `EXPE` (`#9/#10/G2` 3Y rev `8.00% < 10%`, `<25% IRR`); `LYFT` (`#8->#10` 3Y EPS `19.64% < 20%`, `#7b` live bellwether trial RPL, `PH-impaired`); `MMYT` (`A1` `+2.1%` WASO, `#11` P/E `72.97x`, PEG `4.05`, FCF yield `0.90%`, `<25% IRR`); `TCOM` (`#9/#10/G2` 3Y rev `8.60% < 10%`, `#12` PT void `-24.2%` vs 200DMA, `#7` ADR, `<25% IRR`).
- **Lane 3 (10):** `MELI` (`A3b` `-1.9%`, `FT2/A3a` `~3.3% < 6%` normalized FCF margin, `A5` GM `-858bp > -600bp` cap, `FT1` blocks G/`#14a`); `SE` (`A1` WASO `+2.70%`, `A2` 0 buybacks, `FT1` blocks G, `PH-warning`); `CPNG` (`A3a` `0.29%` FCF margin, `A3c` `93%` Capex/OCF, `#9` `10.5%`, `#11` P/E `49.1x`, `PH-impaired`); `DLO` (`PH-impaired`, `FT2/A3a` `4.8%` float-adjusted FCF margin, `A5` GM compression); `PAGS` (`#9` `6.5% < 15%` FT floor, `PH-impaired`, `<25% IRR`); `STNE` (`#9` `11.5% < 15%` FT floor, `A4/FT2` `$3.27B` credit debt, `PH-impaired`, `<25% IRR`); `GRAB` (`A3a` `-$160M` TTM FCF, `A3c`, `PH-impaired`); `PDD` (`A1/A2` `+0.71%` shares w/ 0 buybacks, `#9` `9.42%`, `#12` PT void `-20.2%` vs 200DMA, `PH-impaired`, `<25% IRR`); `GLBE` (`A7` `0.74% > 0.50%` insider selling, `PH-impaired`); `TOST` (`PH-impaired` `-24.7pp` 3Y gap, `FT3/A7b` FTC complaint).
- **Lane 4 (15):** `VRTX` (`#9` `11.11%`, `#10` EPS `8.50%`, `#11` PEG `2.68`, `#12` PT `+15.1%`, `<25% IRR`); `TMDX` (`A1` `+1.53%` w/ 0 buybacks, `A3b/A3c` aviation fleet capex `>45–55%` OCF, `#11` PEG `>2.5`, `#12` PT void `-21.2%` vs 200DMA, `<25% IRR`); `LNTH` (`#9/#10/G2` 3Y rev `~3.5% < 10%`, `<25% IRR`); `HALO` (`A1` convertible notes, `A7` insider sales, `G5` 2028–30 ENHANZE patent cliff); `EXEL` (`A7` insider sales `>0.5%`, `#9` `12.59%`, `#10` `18.02%`, 2030 patent cliff, `<25% IRR`); `AXSM` (`A1/G3` `+4.44%` shares, `A3a/G2` `-$95M` TTM FCF, `#11` P/E `798x`); `MIRM` (`A1/G3` `+8.5%` convert/equity dilution, `A3a/G2` FCF `<6%`, `A4`, `#11`); `DXCM` (`PH-impaired`, `A3b`, `#9` `11.49%`, `#10` PEG `1.43`, `#12`, `<25% IRR`); `BSX` (`A1` Penumbra ~27% stock M&A, `A4` `>2.5x`, `#9/G2` `5.53%` rev, `#12` PT void `-28.5%` vs 200DMA, `<25% IRR`); `PRCT` (Mkt Cap `$1.10B < $2.5B` floor, `A1` `+9.0%`, `A3a` `-$75M` FCF, `H4`); `ALNY` (`#19` blackout, `A1` `+2.4%` shares & converts, `#12` PT void `-24.1%` vs 200DMA); `IDXX` (`#9/G2` `8.8%` rev, `#11` PEG `2.39`, `<25% IRR`); `RMD` (`#9/G2` `5.30%` rev, `PH-warning`, `<25% IRR`); plus pre-revenue clinical biotechs `VKTX`, `GPCR`, `ALT` (hard fail `H1` commercial revenue floor).
- **Lane 5 (12):** `AXON` (`A3a/G2` TTM Company FCF margin `4.14% < 6.0%` floor, `A1/G3` `+3.1%` WASO & `18.5%` SBC/Rev + converts, `A4` `8.7x` TTM FCF, `#11` P/E `45.56x`, PEG `1.71`, FCF yield `0.39%`); `RHM.DE` (`A3a/G2` TTM FCF margin `3.4–3.8% < 6.0%` & H1 FCF `-€1.62B`, `A3c` capex `>55%` OCF, `A1` `+1.08%`, `#12` PT void `-26.2%` vs 200DMA); `MSI` (`A4` `2.54x > 2.5x`, `#9/G2` `9.08%` rev, `#11` PEG `2.31`, `<25% IRR`); `KTOS` (`A1/G3` `$1.0B` Mar 2026 equity offering `+15.14%` shares, `A3a/G2` `-$93.5M` FY26E FCF, `#11`, `#12` PT void `-37.5%` vs 200DMA); `DRS` (`A1/A2` `+1.1%` w/ 0 buybacks, `#9/G2` `8.5%` rev, `#11` PEG `3.07`, `<25% IRR`); `SAAB-B.ST` (`#12` PT `+4.76% < 20%` & FCF yield `2.21% < 5%`, `G5`, `<25% IRR`); `BAESY` (`A3b` NTM FCF `<` advance-inflated TTM FCF, `#9/G2` `8.8%` rev, `#12`, `<25% IRR`); `LDOS` (`A3b`, `#9/G2` `5.17%` rev, `<25% IRR`); `ESLT` (`A1/A2`, `#9` `12.19%`, `#11` P/E `38.15x > 38x`, `#12` PT `+14.2%`, `<25% IRR`); `LHX` (`A4` `~3.6x > 2.5x`, `#9/G2` `7.51%` rev, `#12` PT void, `<25% IRR`); `NOC` (`A4` `~3.5x > 2.5x`, `#9/G2` `5.93%` rev, `#11` PEG `2.64`, `#12` PT void, `<25% IRR`); `GD` (`A1` `+0.95%` WASO, `A3b`, `#9/G2` `5.21%` rev, `<25% IRR`); `LMT` (`A2` buybacks paused under Jan 7 EO, `A3b` NTM FCF `$6.71B < $8.73B` TTM, `A4` `3.01x` w/ Ultra Maritime, `#9/G2` `6.38%`, `<25% IRR`); `TYL` (`#9/G2` `9.37%` rev, `#10` `15.21%` EPS, `#11` PEG `2.15`, `<25% IRR`).
- **Lane 6 (9 + 1 Acquired):** `PANW` (`A1/G3` `+20.8%` YoY shares from CyberArk stock deal, `#11` P/E `41.9x` & PEG `2.67`, `#12` PT `+18.3%`, `G5`, `<25% IRR`); `ZS` (`PH-impaired`, `A1/A2` `$1.725B` Jul 2025 convert & `+1.26%` WASO w/ 0 buybacks, `#12` PT void `-32.0%` vs 200DMA); `NET` (`A1/A2` `+2.02%` shares & converts, `#11` P/E `219.5x`, PEG `4.41`, FCF yield `0.30%`, `#12` PT `+9.6%`, `<25% IRR`); `OKTA` (`PH-impaired`, `A1` `+2.90%` shares, `#9/G2` `8.63%` rev, `<25% IRR`); `S` (`PH-impaired`, `A1/G3` `+3.28%` shares, `A3a/G2` `4.18% < 6%` FCF margin, `#11` P/E `63.2x`, `#12`); `CHKP` (`A1` `$1.75B` H1 2026 convert issuance, `#9/G2` `5.91%` rev, `<25% IRR`); `QLYS` (`#9/G2` `7.21%` rev, `#11` PEG `2.52`, `<25% IRR`); `TENB` (`PH-impaired`, Mkt Cap `$2.11B < $2.5B`, `#9/G2` `7.36%` rev, `<25% IRR`); `RBRK` (`A1/G3` `+6.63%` shares & `30%` SBC/Rev, `#11` P/E `~145x`, `#12` PT `+7.3%`, `<25% IRR`); `VRNS` (`A1/G3` `+3.13%` shares & `$528M` converts, `#11` P/E `>85x`, `#12` PT `+6.1%`, `PH-warning`, `<25% IRR`). *Corporate Action:* `CYBR` (acquired by `PANW` Feb 11, 2026).
- **Lane 7 (9):** `HOOD` (`A1` `$2.2B` 0% convert Jun 25, 2026, `A3a/FT2` `4.44% < 8%` FCF margin, `FT4`, `#11` P/E `39.9x` & PEG `2.14`, `<25% IRR`); `COIN` (`#9/#10` `3.5%` rev, `#11` P/E `179.8x` & PEG `15.72`, `A1` converts/Deribit M&A/SBC, `A3b`, `FT3`, `FT4`, `<25% IRR`); `IBKR` (`A1` Up-C share creep, `#9/#10` `10.5%` rev / `12.0%` EPS, `#11` PEG `2.92`, `#12`, `FT2/FT4` NII rate sensitivity, `<25% IRR`); `VIRT` (`#9/#10` `6.2%` rev, `A4` `3.47x`, `FT2/FT3/FT4` HFT market-making volatility dependency, `<25% IRR`); `CME` (`#9/#10` `7.5%` rev / `9.2%` EPS, `#11` PEG `4.74`, `#12` PT `+2.6%`, `<25% IRR`); `CBOE` (`#9/#10` `8.4%` rev / `11.5%` EPS, `#11` PEG `2.15`, `#12` PT `+5.5%`, `<25% IRR`); `FUTU` (`#9/#10` `12.5%` rev / `9.3%` EPS, `A3b/FT2` client cash FCF drop, `#7` foreign filer, `#12` PT void `-22.6%` vs 200DMA, `<25% IRR`); `ICE` (`A4` `3.83x > 2.5x` Net Debt/FCF, `#9/#10` `11.2%` rev / `10.4%` EPS, `#12` PT `+9.8%`, `<25% IRR`); `NDAQ` (`A4` `2.67x > 2.5x` TTM FCF, `#9/#10` `9.8%` rev / `14.9%` EPS, `#12` PT `+18.2%`, `<25% IRR`).
- **Lane 8 (8):** `RKLB` (`H5` `1.33% > 0.50%` insider selling across 62 Form 4s, `A1` `$1.944B` ATM `29.3M` sh + `42.4M` sh IRDM M&A, `A3a` `-$325.6M` TTM FCF, `H4` ceiling `~$21`, Oct 14 Neutron slip to 2027, `#12` PT void `-27.3%` vs 200DMA); `PL` (`A1/G3` `$120M` ATM + `$460M` convert + `+18.2%` WASO, `A3b/G2` FY27E FCF `-$29.1M`, `#19d` `-9.9%` Q3 guide miss, `H4` `-2.4%/yr` return, `#12` PT void `-48.1%` vs 200DMA); `LUNR` (Mkt Cap `$1.91B < $2.5B`, `A1`, `A3a` neg FCF, `A4`, `H3/H4`, `#12` PT void); `RDW` (`A1/G3` `$566.2M` equity/preferred issuance, `A3a/G2` `-$67.4M` FY26E FCF, `H2/H3/H4`, `#12` PT void); `BKSY` (Mkt Cap `$0.76B < $2.5B`, `A1`, `A3a` `-$42.5M` FCF, `A4`, `H3/H4`); `IRDM` (Pending M&A target being acquired by `RKLB`; standalone fails `A4` `5.56x > 2.5x` & `#9` `6.0%` rev); `MDA.TO` (`A1/G3` `+30.2%` 3Y share dilution, `A3b/A3c` constellation capex swings, `#7` TSX filer); `SATS` (`A1`, `A3a` `>$1.5B` FCF burn, `A4` `>$20B` net debt, `#9` `-4.5%` rev, `PH-warning`).
- **Lane 9 (8):** `CCJ` (`F1` Fwd P/E `59.9x–97x > 15x`, EV/EBITDA `66.4x > 11x`, EBITDA margin `23% < 30%`, `0` buybacks, `F2` no insider buy, `#12` PT void `-22.9%` vs 200DMA, `<25% IRR`); `LEU` (`A1` ATMs/converts, `A3a/G2` neg FCF, `#11` P/E `48x–59x` & EV/EBITDA `174x`, `H3/H4`, `#12` PT void `-38.8%` vs 200DMA); `BWXT` (`A1` `$1.1B` convert Nov 2025, `A4` `7.0x > 2.5x` Net Debt/FCF, `#9` `8.5%` rev, `#11` PEG `2.22`, `<25% IRR`); `NXE` (`F1` pre-revenue, neg FCF/EBITDA, convert/equity dilution, `0` buybacks, `F2` fail); `UEC` (`F1` `-$107M` TTM FCF, ATM/stock M&A dilution, `0` buybacks, `F2` fail, `#12` PT void); `UUUU` (`PH-impaired` `-96.5%` vs ATH, `F1` `-$120.4M` FCF + `$800M` ATMs + `80.7M` sh M&A + `$700M` convert, `F2` fail); `OKLO` (`H1` no licensed commercial reactor, `A1` dilution, `A3a` `-$275M` FCF, `H3/H4`); `SMR` (`H1` no commercial plant, `A1` `>100%` YoY dilution, `A3a` neg FCF, `PH-warning`).

### Explicit Structural Exclusions Log (8 Tickers — Logged Separately)
- **Pure-Play Banks & Balance-Sheet Insurers (`#6` & `fintech.md` Structural Exclusion):**
  - `NU` (Nu Holdings — `$18.42`, `$89.6B` cap): Consumer credit/NIM balance sheet (`-$2.75B` GAAP OCF distorted by loan originations).
  - `KNSL` (Kinsale Capital — `$364.86`, `$8.45B` cap): Balance-sheet E&S P&C insurer carrying long-tail loss reserves (also `<15%` 3Y rev CAGR).
  - `KSPI` (Kaspi.kz — `$82.10`, `$15.9B` cap): ~50% of profit from balance-sheet consumer lending/banking + Kazakh sovereign/FX risk.
  - `AXP` (American Express — `$343.39`, `$235.6B` cap): `$200B+` card loan/deposit balance sheet & NII (also fails `#9` `10.1%` rev & `#10` `14.5%` EPS).
- **AI-Adjacent Power/Grid/Cooling Overlaps (Mandate Exclusion — Overlaps Existing AI Book):**
  - `VRT` (Vertiv — `$261.97`, `$100.2B` cap): Direct AI data-center thermal/power play; also fails `#11` (`PEG 1.91 > 1.65` HV ceiling; `P/E 44.3x > 38x` std ceiling) & `A1` (`+1.0%` WASO). Rev 5 trigger: `<= $215.00`.
  - `ETN` (Eaton — `$427.50`, `$158.8B` cap): AI/electrical grid overlap; also fails `A4` (`Net Debt/FCF 5.89x > 2.5x`), `#9/#10` (`10.8%` rev / `13.2%` EPS), & `#11` (`PEG 2.05`).
  - `GEV` (GE Vernova — `$996.80`, `$249.7B` cap): AI gas turbine/grid overlap; also fails Core `#9` (`13.5% < 15%` 3Y rev) & Standard `#11` (`P/E 38.4x–47.8x > 38x`). Rev 5 Core trigger: `<= $810.00`.
  - `PWR` (Quanta Services — `$686.00`, `$99.3B` cap): AI/grid EPC overlap; also fails `#11` (`PEG 1.71 > 1.65` HV ceiling & `P/E 39.5x > 38x` std ceiling) & `A1` (`+0.82%` M&A share creep). Rev 5 trigger: `<= $635.00`.

---

## 4. Complete Batch-by-Batch & Ticker-by-Ticker Gate Math (Lanes 1–9)



# Batch 1 Deep-Dive Gate Audit: Lanes 1, 2 & 3 (34 Tickers)
**Framework:** `CyberFvde/asymmetry-gates` (**Policy Revision 5**, effective Oct 15, 2026)  
**Benchmark Date:** Mid-October 2026 (Oct 2, 2026 theme-sweep baseline + Oct 13–15, 2026 re-test updates; S&P 500 3Y Total Return benchmark `+87.315%`)  

---

## Executive Summary & Tier Roster Across All 34 Candidates

### Tier 1 — Gate Pass (Actionable Now)
1. **`UBER` (Uber Technologies — Lane 2 Seed):** **Tier 1 Waiver (`#10`) Pass — Actionable Now at `$69.62–$71.50` (Buy up to `$84.00`).** Routed to `#10` by `#8` (AV disintermediation risk) with a standing `#15` autonomous-vehicle trigger. Passes every `A1–A7` hard gate (`WASO -3.55%` YoY, `$6.9B` TTM buybacks, `~1.5x` pro forma Net Debt/NTM FCF including all-cash `$13.7B` Delivery Hero deal, CEO Khosrowshahi open-market purchase of `141k` shares on Sep 10, Q2 `#19` beat) and clears all six `#10` waiver legs (`11.3%` FY26 rev, `13.62%` 3Y rev CAGR, `30.94%–32.7%` 3Y EPS CAGR, `0.62` PEG `< 1.0`, `8.7%` NTM FCF yield `>= 5.0%`, `2.28%` net buyback yield `>= 2.0%`). **Estimated 3Y IRR: `~31.5%/yr` (`>= 25%` hurdle cleared).**
2. **`HWM` (Howmet Aerospace — Lane 1 Seed):** **Tier 1 Standard Core Pass (on mid-Oct pullback to `$216.84`, Fwd P/E `36.70x <= 38.0x`) / Tier 1 `#14a` Starter Pass (up to `$231.27`, Fwd P/E `39.67x <= 48.0x`).** Clears all `A1–A7` gates (`WASO -0.99%` to `-1.10%` YoY, `$1.07B` TTM buybacks, `19.64%` TTM FCF margin, `19.4%` Capex/OCF, `2.40x–2.43x` max pro forma Net Debt/NTM FCF including full `$1,141M` Alcoa guarantee + `$76M` LoC + `$43M` surety, `0.022%` 12m net insider selling, max 2 non-plan officers/qtr, `#9` `15.85%` 3Y rev CAGR & `18–19%` organic FY26 growth, `#12` `+50.8%` PT upside, `PH-clear`).
   - **Dual Buy Trigger Specification:**
     - **Policy Rev 5 Standard Core Trigger (`P/E <= 38x`):** **`$221.65`** (at `$5.83` Oct 2 NTM EPS) to **`$224.58`** (at `$5.91` Oct 14 NTM EPS). *At the Oct 14 close of `$216.84` (`36.70x`), `HWM` is inside the Rev 5 Standard Core buy zone!*
     - **Legacy Policy Rev 3 Trigger (`P/E <= 35x`):** **`$204.15–$206.80`**.
     - **Policy Rev 5 `#14a` Starter Ceiling (`P/E <= 48x`):** **`$279.84–$283.68`**.
     - **Operational Note:** Q3 2026 earnings print is **Oct 29, 2026** (verify `#19` post-print for Tranche 2; gas turbines are `13%` of revenue, `+38%` YoY — below the `20%` `#16` AI-capex sleeve threshold). **Estimated 3Y IRR: `~27.8%/yr` at `$216.84` (`>= 25%` hurdle cleared).**

---

### Tier 2 — Near-Pass Watchlist (With Exact Dollar Buy Triggers)
1. **`SAF.PA` (`Safran SA` — Lane 1 `[NEW DISCOVERY]`):** **Tier 2 Route G (`G-watch`) — Exact Buy Trigger: `<= €310.00–€323.00` (vs. `€330.10` Oct 2 close / `~€314.90` mid-Oct spot).** Out of Core `A–E` on `A1` (2027/2028 Oceanes convert dilution) and `#9` (`12.15%` 3Y rev CAGR `< 15%`), but passes `G1–G4` (`~0.001%` AMF insider net selling, `#19` H1 beat + raised FY guide, `PH-clear`). Under merged Policy Rev 5, `G5` retains the **12.0% 5Y base annualized return hurdle** (`10.6%/yr` at `€330.10`, clearing `12.0%/yr` at `<= €310–€323`). **Estimated 3Y IRR at `€314.90`: `~25.4%/yr`.**
2. **`HEI` (HEICO Corp — Lane 1 Seed):** **Tier 2 Route G (`G-watch`) — Exact Buy Trigger: `<= $275.00` (conservative, deducting `$618M` redeemable NCI) to `$296.00` (`G5` 12% base return ceiling vs. `$302.45` spot).** Fails Core on **two** gates (`#9` 3Y rev CAGR `13.52% < 15%` AND `#11` Fwd P/E `44.0x > 38x` / PEG `2.36 > 2.0`), disqualifying it from `#14a` Starter. Under Route G, watch `G2` pro forma Net Debt/NTM FCF (`~2.55x > 2.5x` if `$618M` redeemable NCI is included in debt; `~1.88x` excluding NCI). **Estimated 3Y IRR at `$275`: `~25.1%/yr` (`~21.3%/yr` at `$302.45`).**
3. **`WWD` (Woodward, Inc. — Lane 1 `[NEW DISCOVERY]`):** **Tier 2 `#14a` / Route G Watch — Exact Buy Trigger: `<= $305.00` AND Nov FY27 NTM FCF guide `>= $377M` (vs. `$331.62` spot).** Fails Core `#9` (`13.32%` 3Y rev CAGR `< 15%`) and currently trips `A3b`/`A4` on unrolled FY26 consensus FCF (`$338.47M = 89.89%` of `$376.53M` TTM FCF; Net Debt/FCF `2.69x > 2.5x`). Because FY26 ended Sep 30, the November FY27 guidance print will roll NTM FCF to FY27E (`~$415M+`), which would simultaneously cure `A3b` (`>100%`) and `A4` (`~2.19x <= 2.5x`), unlocking `#14a` Starter / Route G. **Estimated 3Y IRR at `$305`: `~25.6%/yr`.**
4. **`ATI` (ATI Inc. — Lane 1 `[NEW DISCOVERY]`):** **Tier 2 `#14a` Starter Watch — Exact Buy Trigger: `<= $175.00` with FY27 organic revenue consensus `>= 10.0%` (vs. `$189.50` spot, `9.9%` FY27 rev consensus).** Passes `A1–A7` (`WASO -1.8%` YoY, Net Debt/NTM FCF `2.45x <= 2.5x`), `#11` High-Velocity Core (`32.26%` 3Y EPS CAGR `>= 30%`, Fwd P/E `36.4x <= 45x`, PEG `1.13 <= 1.65`), and `#12` (`+33.3%` PT upside), but misses `#9` (`10.12%` 3Y rev CAGR `< 15%`, FY27 `+9.9%` sitting 10bp below the `10.0%` `#14a` Starter floor). **Estimated 3Y IRR: `~26.8%/yr`.**
5. **`CART` (Maplebear / Instacart — Lane 2 `[NEW DISCOVERY]`):** **Tier 2 `#14a` Starter / `#10` Waiver Watch — Exact Buy Trigger: `<= $48.50` (vs. `$49.40` spot).** Passes `A1–A7` (`WASO -4.2%` YoY on aggressive buybacks, `$851M` net cash, `~20%` FCF margin) and `#12` via the **NTM FCF yield leg (`~6.2% >= 5.0%`)** even though PT upside is `+17.8%` (`$58.21` PT). Fails Core `#9` (`11.2%` 3Y rev CAGR `< 15%`, FY27 `+10.5% < 12%`), putting it 50bp shy of `#10` Waiver (`3Y EPS CAGR ~19.5%` vs `>= 20.0%` required) or actionable at `<= $48.50` where PT upside clears `+20%` and 3Y IRR clears `25%`. **Estimated 3Y IRR at `$48.50`: `~25.2%/yr`.**
6. **`KRMN` (Karman Holdings — Lane 1 `[NEW DISCOVERY]`):** **Tier 2 Route H (`H-watch`) ONLY — Exact Buy Trigger: `<= $24.56` (`H4` 20% 5Y base return ceiling vs. `$30.14` spot) AND remediation of 3 material weaknesses / CFO transition.** Hard fail for Core/G (`A2` no buybacks with `$913.8M` debt+leases, `A3a` TTM FCF `-$27.67M` / `-4.69%` margin, `A4` `~9.5x`, `#12` PT leg void at `-55.1%` below `$67.12` 200DMA), though Rev 5 `A1` bolt-on carve-out cleared (`0.154%` stock issued for Five Axis + Seemann).

---

### Tier 3 — Hard Gate Fails (26 Tickers — Disqualified)
- **Lane 1 (9 Fails):** `FTAI` (`A1`, `A3a`, `A3c`, `A4`, `PH` >20% below 200DMA), `TDG` (`A4`/`G2` `15.9x` Net Debt/FCF, `#9` `<10%`), `LOAR` (`A1`, `A2`, `A4` `~7.1x`, `#11` P/E `42.8x`), `CRS` (`#9` 3Y rev `10.97%` & next-FY `<10%`, `<25% IRR`), `CW` (`#9/#10/G2` 3Y rev `~8.8% < 10%`, `#11` PEG `2.15`, `<25% IRR`), `GE` (`#9/#10/G2` 3Y rev `9.94% < 10%`, `<25% IRR`), `RTX` (`A1`, `A2`, `A3b`, `A4`, `#9/#10/G2` `7.65%`, `#11` PEG `2.55`), `AAR` / `AIR` (`A1`, `A2`, `A3a` `1.0%` FCF margin, `A4`, `#9` `8.38%`), `MTU.DE` / `MTX` (`A3a` `<6%` FCF margin, `#9` `<15%`, `#12` PT `<20%` & FCF yield `<5%`, `<25% IRR`).
- **Lane 2 (7 Fails):** `DASH` (`A1` diluted WASO `+1.82%` YoY on Q2'26 10-Q `438.82M` vs `430.96M` > `+1.5%` ceiling, `G5` `<12%` 5Y return, `#8/#10` FCF yield `3.7% < 5%` if AV delivery disintermediation applies), `BKNG` (`#9/#10/G2` 3Y rev `8.79% < 10%`, `<25% IRR`), `ABNB` (`#9` `12.87% < 15%` + `#12` PT `+8.5% < 20%` & FCF yield `4.7% < 5%` -> 2 Core fails, `<25% IRR`), `EXPE` (`#9/#10/G2` 3Y rev `8.0% < 10%`), `LYFT` (`#8 -> #10` fail on 3Y EPS `19.64% < 20%`, `#7b` live bellwether sexual-assault trial RPL, `PH-impaired`), `MMYT` (`A1`, `#11` Fwd P/E `72.97x` & PEG `4.05`), `TCOM` (`#9/#10/G2` 3Y rev `8.6% < 10%`, `#12` PT void at `-24.2%` below 200DMA, `#7` China ADR).
- **Lane 3 (10 Fails — 0 Survivors):** `MELI` (`A3b` `-1.9%`, `FT2/A3a` normalized FCF margin `~3.3% < 6%`, `A5` GM `-858bp > -600bp` cap, `FT1` blocks G/`#14a`), `SE` (`A1` diluted WASO `+2.70%` YoY, `A2` no buybacks, `FT1` blocks G, `PH-warning`), `CPNG` (`A3a` `0.29%` FCF margin, `A3c` `93%` Capex/OCF, `#9` `10.5%`, `#11` P/E `49.1x`, `PH-impaired`), `DLO` (`PH-impaired`, `FT2/A3b` float-adjusted FCF, `A5` margin compression), `PAGS` (`#9` `6.5% < 15%` FT floor, `#12`, `PH-impaired`), `STNE` (`#9` `11.5% < 15%` FT floor, `A4/FT2` `$3.27B` credit debt, `PH-impaired`), `GRAB` (`A3a` negative TTM FCF `-$160M`, `A3c`, `PH-impaired`), `PDD` (`A1/A2` no buybacks with shares `+0.71%`, `#9` `9.42% < 10%`, `#12` PT void `-20.2%` below 200DMA, `PH-impaired`), `GLBE` (`A7` `0.74% > 0.50%` insider selling, `PH-impaired`), `TOST` (`PH-impaired`, `FT3/A7b` unquantified FTC complaint liability).

---

## Master Audit Comparison Table (All 34 Tickers)

| Ticker | Lane | Price / Mkt Cap | 200DMA (% vs 200d) | 3Y ATH / DD / `PH` Status | 3Y Rev / Next-FY Org | 3Y EPS / FCF CAGR | Est. 3Y IRR % | `A1` WASO YoY / SBC % Rev | `A3` TTM FCF% / Capex/OCF | `A4` Net Debt / NTM FCF | `#11` Fwd P/E / PEG / FCF Yld | `#12` PT Upside | Tier & Exact Buy Trigger / Failed Gates |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`HWM`** | L1 | `$216.84` / `$88.5B` (`$231.27` Oct 2) | `$248.48` (`-12.7%`, valid) | `$292.65` (Aug '26) / `-25.9%` / `PH-clear` | `15.85%` / `+18.5%` | `26.7%` / `24.5%` | **`27.8%`** (Pass) | `-1.05%` / `0.9%` | `19.64%` / `19.4%` | `2.40x` (incl `$1.14B` Alcoa) | `36.7x` / `1.29` / `2.49%` | `+50.8%` (`$327`) | **Tier 1 Pass** (`<=$221.65` Rev 5 38x; `<=$206.80` old 35x) |
| **`FTAI`** | L1 | `$163.10` / `$16.8B` | `$235.67` (`-30.8%`, **VOID**) | `$280.55` (Jul '26) / `-41.9%` / `PH-clear` | `24.8%` / `+22.0%` | `36.5%` / `N/A` | **`29.5%`** (Pass) | **`+1.44%`** / `1.8%` | **`-40.8%`** / **`>100%`** | **`>6.0x`** (`$3.16B` ND) | `19.8x` / `0.54` / `Neg` | `+118%` (Void) | **Tier 3 Fail** (`A1`, `A3a`, `A3c`, `A4`, `#12` void) |
| **`HEI`** | L1 | `$302.45` / `$41.8B` | `$322.22` (`-6.1%`, valid) | `$374.67` (Aug '26) / `-19.3%` / `PH-clear` | **`13.52%`** / `+14.0%` | `18.61%` / `18.0%` | **`21.3%`** (`25.1%` @ `$275`) | `+0.35%` / `1.1%` | `19.2%` / `7.5%` | `1.88x` (**`2.55x`** w/ NCI) | **`44.0x`** / **`2.36`** / `2.3%` | `+28.0%` (`$387`) | **Tier 2 (`G-watch`)** — Buy `<= $275–$296` (Core fails `#9`+`#11`) |
| **`TDG`** | L1 | `$1,100` / `$61.3B` | `$1,244` (`-11.6%`, valid) | `$1,451` (May '26) / `-24.2%` / `PH-clear` | **`9.96%`** / `+11.2%` | `14.5%` / `14.0%` | **`18.4%`** (Fail) | `-0.35%` / `1.9%` | `19.28%` / `12.3%` | **`15.9x`** (`$30.71B` ND) | `26.5x` / `1.83` / `3.15%` | `+37.1%` (`$1,508`) | **Tier 3 Fail** (`A4`/`G2` `15.9x` leverage, `#9` `<10%`, `<25% IRR`) |
| **`WWD`** | L1 | `$331.62` / `$19.6B` | `$363.63` (`-8.8%`, valid) | `$436.44` (Jun '26) / `-24.0%` / `PH-clear` | **`13.32%`** / `+12.5%` | `19.2%` / `18.5%` | **`22.4%`** (`25.6%` @ `$305`) | `-1.12%` / `1.2%` | `8.98%` / `23.5%` | **`2.69x`** (FY26E) / `2.19x` (FY27E) | `32.4x` / `1.69` / `2.1%` | `+24.5%` (`$413`) | **Tier 2 Watch** — Buy `<= $305` + Nov FY27 FCF guide `>=$377M` |
| **`LOAR`** | L1 | `$61.60` / `$5.85B` | `$67.10` (`-8.2%`, valid) | `$97.31` (Nov '24) / `-36.7%` / `PH-clear` | `25.4%` / `+22.0%` | `31.6%` / `28.0%` | **`24.2%`** (Borderline) | **`+4.8%`** / `2.4%` | `18.1%` / `18.5%` | **`7.10x`** (`$842M` ND) | **`42.8x`** / `1.35` / `1.85%` | `+43.2%` (`$88.20`) | **Tier 3 Fail** (`A1` dilution, `A2` no buybacks, `A4` `7.1x`) |
| **`CRS`** | L1 | `$375.00` / `$18.6B` | `$442.90` (`-15.3%`, valid) | `$498.50` (Jul '26) / `-24.8%` / `PH-clear` | **`10.97%`** / **`~9.5%`** | `21.06%` / `22.0%` | **`21.8%`** (`25.2%` @ `$335`) | `-0.59%` / `1.1%` | `11.61%` / `26.5%` | `1.35x` (`$515M` ND) | `28.5x` / `1.35` / `2.25%` | `+53.5%` (`$575.50`) | **Tier 3 / Tier 2 Watch** (`#9` 3Y rev `10.97%`, `<25% IRR`; `G` `<= $335`) |
| **`ATI`** | L1 | `$189.50` / `$25.5B` | `$169.78` (`+11.6%`, valid) | `$214.00` (Aug '26) / `-11.4%` / `PH-clear` | **`10.12%`** / **`9.9%`** (FY27) | `32.26%` / `28.5%` | **`26.8%`** (Pass) | `-1.80%` / `1.0%` | `9.85%` / `28.0%` | `2.45x` (`$1.41B` ND) | `36.4x` / `1.13` / `2.25%` | `+33.3%` (`$252.67`) | **Tier 2 `#14a` Watch** — Buy `<= $175` if FY27 org rev `>=10.0%` |
| **`CW`** | L1 | `$500.00` / `$18.5B` | `$675.51` (`-26.0%`, **VOID**) | `$735.00` (Jul '26) / `-32.0%` / `PH-clear` | **`8.80%`** / **`+9.2%`** | `14.5%` / `14.0%` | **`15.5%`** (Fail) | `-1.40%` / `0.9%` | `16.2%` / `14.5%` | `0.85x` (`$530M` ND) | `31.2x` / **`2.15`** / `3.37%` | `+48.7%` (Void) | **Tier 3 Fail** (`#9/#10/G2` rev `<10%`, `#11` PEG `2.15`, `#12` void) |
| **`GE`** | L1 | `$309.56` / `$332B` | `$323.85` (`-4.4%`, valid) | `$381.22` (Aug '26) / `-18.8%` / `PH-clear` | **`9.94%`** / `+10.5%` | `17.5%` / `16.5%` | **`17.8%`** (Fail) | `-1.65%` / `0.8%` | `17.8%` / `16.0%` | `0.95x` (`~$8.2B` ND) | `37.5x` / **`2.14`** / `2.65%` | `+24.0%` (`$384`) | **Tier 3 Fail** (`#9/#10/G2` 3Y rev `9.94% < 10%`, `#11` PEG, `<25% IRR`) |
| **`RTX`** | L1 | `$184.68` / `$246B` | `$194.91` (`-5.2%`, valid) | `$225.49` (Aug '26) / `-18.1%` / `PH-clear` | **`7.65%`** / **`+7.3%`** | `10.1%` / `11.0%` | **`11.8%`** (Fail) | **`+0.81%`** / `0.6%` | `12.8%` / `21.0%` | **`3.03x`** (`$30.55B` ND) | `25.7x` / **`2.55`** / `4.09%` | `+18.5%` (`<20%`) | **Tier 3 Fail** (`A1`, `A2`, `A3b`, `A4`, `#9`, `#11`, `#12`, `<25% IRR`) |
| **`AAR` (`AIR`)** | L1 | `$100.00` / `$3.85B` | `$117.34` (`-14.8%`, valid) | `$154.00` (Jun '26) / `-35.1%` / `PH-clear` | **`8.38%`** / **`+8.5%`** | `16.15%` / `18.0%` | **`18.2%`** (Fail) | **`+12.4%`** / `0.8%` | **`1.00%`** / `83.3%` | **`5.80x`** (`$874M` ND) | `16.7x` / `1.35` / `3.90%` | `+54.5%` (`$154.50`) | **Tier 3 Fail** (`A1`, `A2`, `A3a` `1.0%`, `A3c`, `A4`, `#9` `8.38%`) |
| **`KRMN`** | L1 | `$30.14` / `$4.00B` | `$67.12` (`-55.1%`, **VOID**) | `$115.29` (Jan '26) / `-73.9%` / `PH-clear` | `21.25%` / `+24.7%` | `27.8%` / `35.0%` | **`22.5%`** (`26%` @ `$24.56`) | `+0.158%` (Pass) / `3.2%` | **`-4.69%`** / `>100%` | **`9.52x`** (`$914M` ND) | `38.6x` / `1.39` / `2.40%` | `+193%` (Void) | **Tier 3 Core/G Fail** (`A2`, `A3a`, `A4`, `#12`); **Tier 2 `H-watch` `<=$24.56`** |
| **`SAF.PA`** | L1 | `€314.90` / `€131B` (`€330.10` Oct 2) | `€338.50` (`-7.0%`, valid) | `€365.80` (Aug '26) / `-13.9%` / `PH-clear` | **`12.15%`** / `+13.0%` | `24.85%` / `21.0%` | **`25.4%`** (Pass @ `€315`) | **`+1.65%`** (Conv) / `0.5%` | `14.8%` / `22.0%` | `Net Cash` (`-0.4x`) | `26.2x` / `1.05` / `3.45%` | `+21.1%` (`€381.50`) | **Tier 2 (`G-watch`)** — Buy `<= €310–€323` (`G5` 12% base return) |
| **`MTU.DE`** | L1 | `€350.70` / `€19.1B` | `€362.10` (`-3.1%`, valid) | `€394.50` (Jul '26) / `-11.1%` / `PH-clear` | **`10.8%`** / `+11.5%` | `16.4%` / `18.0%` | **`17.9%`** (Fail) | `+0.20%` / `0.4%` | **`4.8%`** / `38.0%` | `0.90x` (`€650M` ND) | `18.2x` / `1.11` / `2.15%` | **`+17.8%`** (`€413`) | **Tier 3 Fail** (`A3a` `<6%` GTF cash drain, `#9`, `#12`, `<25% IRR`) |
| **`UBER`** | L2 | `$71.50` / `$147B` (`$69.62` Sep 28) | `$74.32` (`-3.8%`, valid) | `$93.60` (Oct '25) / `-23.6%` / `PH-clear` | **`13.62%`** / **`+11.3%`** (`#10` Pass) | `30.94%` / `26.5%` | **`31.5%`** (Pass) | **`-3.55%`** / `3.8%` | `19.4%` / `6.5%` | `1.50x` (w/ `$13.7B` DH) | `17.0x` / `0.62` / **`8.70%`** | `+41.5%` (`$101.24`) | **Tier 1 Waiver (`#10`) Pass** — Actionable Now (`<= $84.00`) |
| **`DASH`** | L2 | `$191.99` / `$83.6B` | `$185.16` (`+3.7%`, valid) | `$285.50` (Oct '25) / `-32.8%` / `PH-clear` | `17.34%` / `+24.0%` | `42.19%` / `32.0%` | **`28.4%`** (Gross) | **`+1.82%`** (10-Q) / `7.6%` | `13.1%` / `14.0%` | `Net Cash` (`-0.8x`) | `27.8x` / `0.65` / `3.70%` | `+42.4%` (`$273.32`) | **Tier 3 Fail** (`A1` WASO `+1.82%` > `1.5%`, `G5` `<12%`, `#8/#10` FCF `<5%`) |
| **`BKNG`** | L2 | `$5,112` / `$166B` (or `$159` split-adj) | `$5,810` (`-12.0%`, valid) | `$6,285` (Jul '26) / `-18.7%` / `PH-clear` | **`8.79%`** / **`+8.89%`** | `17.45%` / `15.5%` | **`19.8%`** (Fail) | `-4.16%` / `1.9%` | `34.8%` / `4.5%` | `0.36x` (`$3.41B` ND) | `14.4x` / `0.82` / `5.95%` | `+29.9%` (`$6,641`) | **Tier 3 Fail** (`#9/#10/G2` 3Y rev `8.79% < 10%` floor, `<25% IRR`) |
| **`ABNB`** | L2 | `$165.67` / `$97.7B` | `$144.63` (`+14.5%`, valid) | `$219.94` (Feb '21) / `-24.7%` / **`PH-warn`** | **`10.42%`** / **`+10.4%`** | `16.46%` / `14.0%` | **`16.5%`** (Fail) | `-3.80%` / `11.5%` | `38.2%` / `1.5%` | `Net Cash` (`-$9.57B`) | `28.1x` / `1.71` / `4.70%` | **`+8.5%`** (`$179.77`) | **Tier 3 Fail** (`#9` `<15%` + `#12` PT `<20%` & FCF `<5%`, `G5` `<12%`) |
| **`CART`** | L2 | `$49.40` / `$12.8B` | `$42.59` (`+16.0%`, valid) | `$56.40` (Aug '26) / `-12.4%` / `PH-clear` | **`11.20%`** / **`+10.5%`** | `19.50%` / `18.5%` | **`24.4%`** (`25.2%` @ `$48.50`) | `-4.20%` / `9.2%` | `20.5%` / `5.5%` | `Net Cash` (`-$851M`) | `18.5x` / `0.95` / **`6.20%`** | **`+17.8%`** (`$58.21`) | **Tier 2 `#14a` / `#10` Watch** — Buy `<= $48.50` (clears `#12` on FCF `6.2%`) |
| **`EXPE`** | L2 | `$262.00` / `$31.4B` | `$254.50` (`+2.9%`, valid) | `$295.00` (Jul '26) / `-11.2%` / `PH-clear` | **`8.00%`** / **`+8.2%`** | `20.90%` / `16.0%` | **`21.5%`** (Fail) | `-5.80%` / `2.8%` | `18.5%` / `16.5%` | `0.65x` (`$1.9B` ND) | `11.6x` / `0.58` / `9.50%` | `+22.1%` (`$320`) | **Tier 3 Fail** (`#9/#10/G2` 3Y rev `8.00% < 10%` floor, `<25% IRR`) |
| **`LYFT`** | L2 | `$15.02` / `$6.05B` | `$15.87` (`-5.4%`, valid) | `$78.20` (Mar '21) / `-80.8%` / **`PH-imp`** | **`13.20%`** / `+12.3%` | **`19.64%`** / `18.0%` | **`23.8%`** (Borderline) | `-4.94%` / `5.4%` | `16.4%` / `8.5%` | `Net Cash` (`-$502M`) | `11.8x` / `0.60` / **`18.7%`** | `+32.1%` (`$19.84`) | **Tier 3 / Re-test** (`#8->#10` EPS `19.64% < 20%`, `#7b` trial, `PH-imp`) |
| **`MMYT`** | L2 | `$105.00` / `$11.6B` | `$98.50` (`+6.6%`, valid) | `$124.00` (Jul '26) / `-15.3%` / `PH-clear` | `20.34%` / `+21.5%` | `32.78%` / `28.0%` | **`18.5%`** (Mult drag) | **`+2.10%`** / `3.8%` | `14.2%` / `12.0%` | `Net Cash` (`-$420M`) | **`72.97x`** / **`4.05`** / **`0.90%`** | `+24.8%` (`$131`) | **Tier 3 Fail** (`A1` dilution, `#11` P/E `73x` & PEG `4.05` & FCF `0.9%`) |
| **`TCOM`** | L2 | `$38.00` / `$23.9B` | `$50.12` (`-24.2%`, **VOID**) | `$69.50` (Oct '25) / `-45.3%` / `PH-clear` | **`8.60%`** / **`+8.5%`** | `12.5%` / `11.0%` | **`16.4%`** (Fail) | `-3.96%` / `2.4%` | `24.5%` / `8.0%` | `Net Cash` (`-$7.7B`) | `10.0x` / `0.80` / `8.50%` | `+53.8%` (Void) | **Tier 3 Fail** (`#9/#10/G2` 3Y rev `8.6% < 10%`, `#12` void, `#7` ADR) |
| **`MELI`** | L3 | `$1,696.56` / `$86.0B` | `$1,837.61` (`-7.7%`, valid) | `$2,613.63` (Jun '25) / `-35.1%` / `PH-clear` | `32.02%` / `+28.0%` | `31.5%` / `24.0%` | **`29.2%`** (Pass) | `0.00%` / `0.9%` | **`3.3%` (`FT2`)** / `32%` | `1.85x` (ex-credit) | `29.5x` / `0.94` / **`1.6%` (`FT2`)** | `+38.5%` (`$2,350`) | **Tier 3 Fail** (`A3b` `-1.9%`, `FT2/A3a` `3.3% < 6%`, `A5` GM `-858bp`) |
| **`SE`** | L3 | `$95.19` / `$56.5B` | `$102.89` (`-7.5%`, valid) | `$366.99` (Oct '21) / `-74.1%` / **`PH-warn`** | `20.5%` / `+19.0%` | `34.0%` / `28.0%` | **`27.5%`** (Pass) | **`+2.70%`** / `3.9%` | `9.2%` (`FT2`) / `15%` | `Net Cash` (`-$4.8B`) | `21.5x` / `0.63` / `4.1%` | `+34.5%` (`$128`) | **Tier 3 Fail** (`A1` WASO `+2.70%`, `A2` no buybacks, `FT1` blocks G) |
| **`CPNG`** | L3 | `$14.40` / `$25.9B` | `$17.92` (`-19.6%`, valid) | `$69.00` (Mar '21) / `-79.1%` / **`PH-imp`** | **`10.5%`** / **`+11.2%`** | `67.0%` / `45.0%` | **`24.0%`** (Borderline) | `+0.85%` / `1.2%` | **`0.29%`** / **`93.0%`** | `0.60x` (`-$1.2B` ND) | **`49.1x`** / `0.73` / **`0.39%`** | `+62.5%` (`$23.45`) | **Tier 3 Fail** (`A3a` `0.29%`, `A3c` `93%`, `#9`, `#11` P/E `49x`, `PH-imp`) |
| **`DLO`** | L3 | `$14.80` / `$4.35B` | `$13.95` (`+6.1%`, valid) | `$64.69` (Aug '21) / `-77.1%` / **`PH-imp`** | `32.5%` / `+35.0%` | `26.0%` / `22.0%` | **`26.4%`** (Pass) | `-1.20%` / `1.8%` | **`4.8%` (`FT2`)** / `12%` | `Net Cash` (`-$450M`) | `14.7x` / `0.57` / `4.2%` (`FT2`) | `+27.0%` (`$18.80`) | **Tier 3 Fail** (`PH-impaired`, `FT2/A3a/A3b` float-adj FCF, `A5` GM) |
| **`PAGS`** | L3 | `$9.60` / `$3.05B` | `$10.85` (`-11.5%`, valid) | `$62.83` (Feb '21) / `-84.7%` / **`PH-imp`** | **`6.50%`** / **`+6.8%`** | `11.5%` / `10.0%` | **`14.2%`** (Fail) | `-2.10%` / `1.4%` | `8.5%` (`FT2`) / `28%` | `Net Debt` (Credit) | `6.4x` / `0.56` / `8.5%` | `+21.1%` (`$11.63`) | **Tier 3 Fail** (`#9` `6.5% < 15%` FT floor, `A5`, `PH-impaired`, `<25% IRR`) |
| **`STNE`** | L3 | `$11.65` / `$2.75B` | `$13.80` (`-15.6%`, valid) | `$95.12` (Feb '21) / `-87.8%` / **`PH-imp`** | **`11.5%`** / **`+12.0%`** | `15.5%` / `14.0%` | **`19.5%`** (Fail) | `-3.40%` / `1.9%` | `9.2%` (`FT2`) / `22%` | **`>3.0x`** (`$1.69B` ND) | `5.4x` / `0.35` / `9.0%` | `+32.2%` (`$15.40`) | **Tier 3 Fail** (`#9` `<15%` FT floor, `A4/FT2` credit debt, `PH-imp`, `<25% IRR`) |
| **`GRAB`** | L3 | `$3.15` / `$12.1B` | `$3.65` (`-13.7%`, valid) | `$18.11` (Nov '21) / `-82.6%` / **`PH-imp`** | `18.5%` / `+20.5%` | `38.0%` / `N/A` | **`23.5%`** (Fail) | `+0.90%` / `6.8%` | **`-4.29%`** / **`>100%`** | `Net Cash` (`-$4.5B`) | `17.5x` / `0.46` / **`Neg`** | `+77.1%` (`$5.58`) | **Tier 3 Fail** (`A3a` `-$160M` TTM FCF, `A3c`, `FT4`, `PH-impaired`) |
| **`PDD`** | L3 | `$75.38` / `$104.7B` | `$94.50` (`-20.2%`, **VOID**) | `$202.82` (Feb '21) / `-62.8%` / **`PH-imp`** | **`9.42%`** / **`+9.8%`** | `9.99%` / `10.0%` | **`11.5%`** (Fail) | **`+0.71%`** / `2.1%` | `24.2%` / `4.0%` | `Net Cash` (`-$38B`) | `7.8x` / `0.78` / `11.5%` | `+38.0%` (Void) | **Tier 3 Fail** (`A1/A2` no buyback, `#9` `9.42%`, `#12` void, `PH-imp`) |
| **`GLBE`** | L3 | `$39.31` / `$6.65B` | `$35.57` (`+10.5%`, valid) | `$81.69` (Sep '21) / `-51.9%` / **`PH-imp`** | `24.5%` / `+26.0%` | `36.0%` / `28.0%` | **`26.2%`** (Pass) | `+0.45%` / `4.5%` | `15.8%` / `6.0%` | `Net Cash` (`-$410M`) | `28.5x` / `0.79` / `2.8%` | `+24.6%` (`$49.00`) | **Tier 3 Fail** (`A7` `0.74% > 0.50%` insider sales, `PH-impaired`) |
| **`TOST`** | L3 | `$29.79` / `$16.9B` | `$29.78` (`0.0%`, valid) | `$65.22` (Nov '21) / `-54.3%` / **`PH-imp`** | `21.0%` / `+22.5%` | `35.0%` / `30.0%` | **`27.0%`** (Pass) | `+0.95%` / `4.8%` | `9.5%` / `10.0%` | `Net Cash` (`-$1.4B`) | `24.5x` / `0.70` / `3.6%` | `+24.2%` (`$37.00`) | **Tier 3 Fail** (`PH-impaired` `-24.7pp` 3Y gap, `FT3/A7b` FTC complaint) |

---

## Detailed Ticker-by-Ticker Gate Audits

### LANE 1: Aerospace Aftermarket, Engine Leasing, PMA Parts & Specialty Aero Alloys (15 Tickers)

#### 1. `HWM` — Howmet Aerospace Inc. (Seed) — **TIER 1 PASS (Actionable Now at `$216.84`)**
- **1. Market Data & Price Health (`PH`):**
  - **Mid-Oct Spot Price:** `$216.84` (Oct 14 re-test; Oct 2 close was `$231.27`) | **Market Cap:** `~$88.5B` (`~408M` diluted shares).
  - **200DMA:** `$248.48` (`-12.7%` below rising 200DMA at `$216.84`; `-6.9%` at `$231.27` — inside the `-20%` threshold, so `#12` PT leg is **valid**).
  - **3Y ATH & Drawdown:** `$292.65` on `2026-08-18` (age `0.16y < 3.0y`), drawdown `-25.9%` (`-20.97%` on Oct 2), 3Y Total Return `+413.39%` (`+326.08pp` vs S&P 500 TR `+87.32%`). **Status: `PH-clear`.**
- **2. 25% 3-Year IRR Math:**
  - **3Y Revenue CAGR:** `15.85%` (FY26E `+22.5%` total / `+18–19%` organic; FY27E `+13.67%`).
  - **3Y EPS / FCF CAGR:** `26.7%` EPS CAGR (`24.5%` FCF/sh CAGR) + `~1.2%` Net Buyback Yield (`$1.07B` TTM repurchases) + `0.0%` multiple expansion (holding `~36.7x` Fwd P/E) = **`~27.8%` Estimated 3Y Annualized IRR (`>= 25%` plausible: YES).**
- **3. Dilution Gate (`A1` & `G3`):**
  - **YoY Diluted WASO:** `-0.99%` to `-1.10%` YoY (active buybacks `$1.07B` TTM). **SBC:** `~$82M` (`0.90%` of revenue, `4.6%` of FCF). Zero converts, ATMs, secondaries, or stock-settled M&A. **Status: `A1` & `A2` PASS.**
- **4. Capex & FCF Gate (`A3a/b/c`):**
  - **TTM Company FCF:** `$1.79B` (`19.64%` margin `>= 6.0%` floor).
  - **NTM FCF vs TTM FCF:** Blended NTM FCF `$2.21B` (FY26E `$1.934B`, FY27E `$2.304B`) = `123.5%` of TTM FCF (`>= 100%`).
  - **Capex / NTM OCF:** `19.4%` (`<= 50%` cap). **Status: `A3a/b/c` PASS.**
- **5. Leverage (`A4`) & Moat/Margin (`A5`):**
  - **Pro Forma Net Debt / NTM FCF:** Net debt `$4.10B` + max Alcoa tax/environmental guarantee `$1,141M` + letters of credit `$76M` + surety bonds `$43M` = `$5.36B` max debt / `$2.21B` blended NTM FCF = **`2.40x–2.43x` (`<= 2.50x` ceiling)**.
  - **Moat & Gross Margin (`A5`):** Structural sole-source monopoly/duopoly in single-crystal turbine airfoils and aero fasteners; NTM GM `36.0%` vs FY25 `34.2%` (`+180bp` expansion). **Status: `A4` & `A5` PASS.**
- **6. Insiders & Legal (`#7` / `A7`):**
  - **12m Net Insider Selling:** `0.022%` of shares out (`<= 0.50%`); max 2 non-plan officers selling in any quarter.
  - **Legal RPL:** Grenfell Tower civil litigation disclosed without a quantified RPL exceeding `5%` of NTM FCF (`~$110M` threshold — monitored via `#15` trigger). **Status: `A7` PASS.**
- **7. Valuation (`#11`), Asymmetry (`#12`) & Print (`#19`):**
  - **Multiples at `$216.84`:** Fwd P/E **`36.70x`** (`<= 38.0x` Rev 5 Standard Core ceiling!), PEG **`1.29`** (`<= 2.00`), NTM FCF yield **`2.49%`** (`>= 1.50%`).
  - **Asymmetry (`#12`):** Consensus PT `$327.00–$328.70` (`+50.8%` upside `>= +20%`, 22 analysts).
  - **Print (`#19`):** Aug 6 Q2 2026 print beat all 4 legs. Next print: **Oct 29, 2026**.
- **8. Final Tier Classification & Exact Dollar Buy Trigger:**
  - **Tier 1 (Gate Pass — Ready Now under Policy Rev 5 Standard Core at `$216.84`).**
  - **Exact Dollar Buy Triggers:**
    - **Policy Rev 5 Standard Core (`P/E <= 38x`):** **`<= $221.65`** (on `$5.83` Oct 2 NTM EPS) to **`<= $224.58`** (on `$5.91` Oct 14 NTM EPS).
    - **Legacy Policy Rev 3 Core (`P/E <= 35x`):** **`<= $204.15–$206.80`**.
    - **Policy Rev 5 `#14a` Starter Ceiling (`P/E <= 48x`):** **`<= $279.84–$283.68`**.

---

#### 2. `FTAI` — FTAI Aviation Ltd. (Seed) — **TIER 3 FAIL (`A1`, `A3a`, `A3c`, `A4`, `#12` Void)**
- **1. Market Data & `PH`:** `$163.10` | Market Cap `$16.75B` | 200DMA `$235.67` (**`-30.8%` below 200DMA -> voids `#12` PT leg**) | ATH `$280.55` (Jul 2026, DD `-41.9%`, `PH-clear` by age).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `24.8%`, Next-FY organic `+22.0%`, 3Y EPS CAGR `36.5%`, Buyback `-1.4%` dilution = **`~29.5%` Est. 3Y IRR** (plausible on paper, but funded by heavy debt and asset capex).
- **3. Dilution (`A1`):** Shares `+1.44%` YoY (`102.71M` shares) with zero common buybacks (`A2` fail) and history of preferred/equity & senior note issuances. **Fails `A1` & `A2`.**
- **4. Capex & FCF (`A3a/b/c`):** TTM OCF `-$439.76M`, TTM Capex `-$522.41M` (CFM56/V2500 engine module acquisitions), TTM Company FCF **`-$962.18M` (`-40.8%` FCF margin < `6%` floor)**; Capex/OCF `>100%` (`> 50%` cap). **Hard Fail on `A3a` & `A3c`.**
- **5. Leverage (`A4`) & Moat (`A5`):** Total debt `$3.50B`, Cash `$337.2M`, Net Debt `$3.16B` (`8.65x` Debt/Equity; `>6.0x` NTM adjusted FCF `> 2.5x` ceiling). **Hard Fail on `A4`.**
- **6. Insiders & Legal (`#7`):** Short-seller accounting/depreciation allegations (Muddy Waters / Snowcap) and post-investigation volatility.
- **7. Valuation (`#11`) & Asymmetry (`#12`):** Fwd P/E `19.8x`, PEG `0.54`, PT `$355.60` (`+118%`), but **PT leg is VOID** (`-30.8%` below 200DMA) and FCF yield is negative (`#12` fail).
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `A1`, `A2`, `A3a`, `A3c`, `A4`, `#12`).**

---

#### 3. `HEI` — HEICO Corporation (Seed) — **TIER 2 NEAR-PASS WATCHLIST (`G-watch` at `<= $275–$296`)**
- **1. Market Data & `PH`:** `$302.45` | Market Cap `$41.75B` | 200DMA `$322.22` (`-6.1%`, PT valid) | ATH `$374.67` (`2026-08-14`, DD `-19.28%`, 3Y TR `+88.33%`, gap `+1.01pp`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `13.52%`, Q3 FY26 organic growth `+14.0%`, 3Y EPS CAGR `18.61%`, Buyback `0.0%` = **`~21.3%` Est. 3Y IRR at `$302.45`** (`~25.1%` IRR if bought at `$275.00`).
- **3. Dilution (`A1` & `G3`):** Diluted WASO `+0.35%` YoY (`<= 0.50%` Core, `<= 3.0%` G3), SBC `1.1%` of rev. Passes `A1`/`G3`, though `A2` notes net debt without buybacks (waived in Route G).
- **4. Capex & FCF (`A3` & `G2`):** TTM FCF `~$945M` (`19.2%` margin `>= 6%`), NTM FCF `~$1.12B` (`>100%` of TTM), Capex/OCF `~7.5%` (`<= 50%`). **Passes `A3`/`G2`.**
- **5. Leverage (`A4` & `G2`) & Moat (`A5`):** Balance sheet Net Debt `$2.11B` (`1.88x` NTM FCF), **BUT** HEICO carries **`$618M` of redeemable noncontrolling interest (mezzanine equity)** from 80%-owned subsidiaries. Including the `$618M` NCI liability pushes pro forma Net Debt/NTM FCF to **`~2.55x` (`> 2.50x` cap)**! Dominant FAA PMA aftermarket moat (`A5`/`G1` pass, op margin `25.1%`).
- **6. Insiders & Legal (`#7` / `G4`):** Mendelson family net buyers/holders (`<0.1%` net selling), zero legal RPL issues. **Passes `A7`/`G4`.**
- **7. Valuation (`#11` / `G5`) & Asymmetry (`#12`):** Fwd P/E **`44.0x`** (`> 38x` Standard Core), PEG **`2.36`** (`> 2.00`), PT `$387–$391.70` (`+28%`). Fails Core on **two** gates (`#9` `13.52% < 15%` AND `#11` P/E & PEG), blocking `#14a` Starter. Under **Route G (`G5`)**, 12% 5Y base return ceiling is **`$296.00`** (`$275.00` after deducting `$618M` NCI).
- **8. Final Tier & Trigger:** **Tier 2 (`G-watch`) — Exact Buy Trigger: `<= $275.00` (NCI-adjusted) to `$296.00` (`G5` ceiling).**

---

#### 4. `TDG` — TransDigm Group Incorporated (Seed) — **TIER 3 FAIL (`A4`/`G2`, `#9`, `<25% IRR`)**
- **1. Market Data & `PH`:** `$1,100.00` | Market Cap `$61.3B` (`55.28M` shares) | 200DMA `$1,244.00` (`-11.6%`, valid) | ATH `$1,451.00` (May 2026, DD `-24.2%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `9.96%`, Next-FY organic `+11.2%`, 3Y EPS CAGR `14.5%`, Special dividend/yield `~3.5%` = **`~18.4%` Est. 3Y IRR (`< 25%` hurdle).**
- **3. Dilution (`A1`):** Shares `-0.35%` YoY, SBC `1.9%` of rev (`10.0%` of FCF). Passes `A1`.
- **4. Capex & FCF (`A3`):** TTM OCF `$2.20B`, Capex `$271M` (`12.3%` of OCF `<= 50%`), TTM FCF `$1.93B` (`19.28%` margin on `$10.01B` rev), NTM FCF `$2.15B`. Passes `A3`.
- **5. Leverage (`A4` & `G2`) & Moat (`A5`):** Total Debt **`$33.49B`**, Cash `$2.78B`, **Net Debt `$30.71B` = `15.9x` TTM FCF / `14.3x` NTM FCF** (catastrophically above the `2.5x` `A4` and `G2` ceiling due to LBO-style debt-funded special dividends). Sole-source aftermarket moat (`>50%` EBITDA margin) passes `A5`, but leverage is a hard disqualifier.
- **6. Insiders & Legal (`#7`):** `<0.2%` net selling; recurring DoD OIG price-gouging inquiries.
- **7. Valuation (`#11`) & Asymmetry (`#12`):** Fwd P/E `26.5x`, PEG `1.83`, FCF yield `3.15%`, PT `$1,508` (`+37.1%`). Fails `#9` (`9.96% < 15%` Core and `< 10%` `#10`/`G2` floor).
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `A4`/`G2` `14.3x–15.9x` Net Debt/FCF, `#9/#10/G2` 3Y rev `9.96% < 10%`, `<25% IRR`).**

---

#### 5. `WWD` — Woodward, Inc. (`[NEW DISCOVERY]`) — **TIER 2 NEAR-PASS WATCHLIST (`<= $305.00` + Nov FY27 FCF Guide)**
- **1. Market Data & `PH`:** `$331.62` | Market Cap `$19.6B` | 200DMA `$363.63` (`-8.8%`, valid) | ATH `$436.44` (`2026-06-25`, DD `-24.02%`, 3Y TR `+172.62%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `13.32%`, Next-FY organic `+12.5%`, 3Y EPS CAGR `19.2%`, Buyback `1.1%` = **`~22.4%` Est. 3Y IRR at `$331.62`** (`~25.6%` at `$305.00`).
- **3. Dilution (`A1`):** Diluted WASO `-1.12%` YoY (active buybacks), SBC `1.2%` of rev. Passes `A1` & `A2`.
- **4. Capex & FCF (`A3` & `G2`):** TTM FCF `$376.53M` (`8.98%` margin `>= 6%`), Capex/OCF `23.5%`. Unrolled FY26 consensus FCF (`$338.47M`) was `89.89%` of TTM (missing `A3b` `100%` and `G2` `90%` by 11bp), but FY26 ended Sep 30 — November's FY27 FCF guide (`~$415M` consensus) rolls NTM FCF above `$377M`.
- **5. Leverage (`A4`) & Moat (`A5`):** Net Debt `~$909M` = `2.69x` unrolled FY26E FCF (`> 2.5x`), dropping to **`2.19x` (`<= 2.5x`)** on FY27E FCF rollover. Duopoly aero fuel/combustion controls moat (`A5` pass).
- **6. Insiders & Legal (`#7`):** `<0.15%` net insider selling, clean legal.
- **7. Valuation (`#11`) & Asymmetry (`#12`):** Fwd P/E `32.4x <= 38x`, PEG `1.69 <= 2.0`, FCF yield `2.1%`, PT `$413` (`+24.5%`). Single Core fail in `#9` (`13.32%` 3Y rev vs `15%`, inside `#14a` `12%` starter band).
- **8. Final Tier & Trigger:** **Tier 2 (`#14a` / `G-watch`) — Exact Buy Trigger: `<= $305.00` once Nov print confirms FY27 NTM FCF `>= $377M`.**

---

#### 6. `LOAR` — Loar Holdings Inc. (`[NEW DISCOVERY]`) — **TIER 3 FAIL (`A1`, `A2`, `A4`, `#11`)**
- **1. Market Data & `PH`:** `$61.60` | Market Cap `$5.85B` | 200DMA `$67.10` (`-8.2%`, valid) | ATH `$97.31` (Nov 2024, DD `-36.7%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `25.4%`, Next-FY organic `+15.0%` (`+29.8%` total w/ M&A), 3Y EPS CAGR `31.6%`, Buyback `0.0%`, Multiple compression (`42.8x -> 35x` = `-6.5%/yr`) = **`~24.2%` Est. 3Y IRR.**
- **3. Dilution (`A1` & `A2`):** Post-IPO/secondary/M&A diluted WASO **`+4.8%` YoY** (`> 0.5%` / `1.5%` / `3.0%` ceilings), zero buybacks with net debt (`A2` fail), SBC `2.4%` of rev. **Hard Fail on `A1`, `A2` & `G3`.**
- **4. Capex & FCF (`A3`):** TTM Rev `$586.17M`, TTM FCF `~$106M` (`18.1%` margin), NTM FCF `~$118.65M`, Capex/OCF `18.5%`. Passes `A3`.
- **5. Leverage (`A4`) & Moat (`A5`):** Cash `$122.43M`, Total Debt `$964.85M`, **Net Debt `$842.41M` = `7.10x` NTM FCF** (`> 2.5x` cap, plus recent acquisition debt). Niche aftermarket component moat (`A5` pass), but **Hard Fail on `A4`/`G2`.**
- **6. Insiders & Legal (`#7`):** Private equity / sponsor secondary offerings.
- **7. Valuation (`#11`) & Asymmetry (`#12`):** Fwd P/E **`42.8x`** (`> 38x` Standard Core; passes High-Velocity P/E `<= 45x` on `31.6%` EPS CAGR & PEG `1.35 <= 1.65`), PT `$88.20` (`+43.2%`).
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `A1`, `A2`, `A4`, `G2`, `G3`).**

---

#### 7. `CRS` — Carpenter Technology Corporation (`[NEW DISCOVERY]`) — **TIER 3 / TIER 2 BORDERLINE (`#9`, `<25% IRR`)**
- **1. Market Data & `PH`:** `$375.00` | Market Cap `$18.58B` (`49.56M` shares) | 200DMA `$442.90` (`-15.3%`, valid) | ATH `$498.50` (Jul 2026, DD `-24.8%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `10.97%`, TTM rev growth `+8.59%` (next-FY `~9.5%–10.5%`), 3Y EPS CAGR `21.06%`, Buyback `+0.59%` = **`~21.8%` Est. 3Y IRR at `$375`** (`~25.2%` at `$335`).
- **3. Dilution (`A1`):** Shares `-0.59%` YoY (active buybacks), SBC `1.1%` of rev. Passes `A1` & `A2`.
- **4. Capex & FCF (`A3`):** TTM FCF `$362.3M` (`11.61%` margin on `$3.12B` rev), NTM FCF `~$420M`, Capex/OCF `26.5%`. Passes `A3`.
- **5. Leverage (`A4`) & Moat (`A5`):** Total Debt `$690.7M`, Net Debt `~$515M` = **`1.23x` NTM FCF (`<= 2.5x`)**. Specialty VIM/VAR aerospace alloy oligopoly with ATI/Howmet; GM `30.58%`, Op margin `22.27%` expanding. Passes `A4` & `A5`.
- **6. Insiders & Legal (`#7`):** `<0.2%` net selling, clean legal.
- **7. Valuation (`#11`) & Asymmetry (`#12`):** Fwd P/E `28.5x <= 38x`, PEG `1.35 <= 2.0`, FCF yield `2.25% >= 1.5%`, PT `$575.50` (`+53.5%`). Fails Core `#9` (`10.97%` 3Y rev `< 15%`, below `#14a` `12.0%` 3Y rev floor!). Only eligible via Route G (`G2` requires `>= 10.0%` next-FY & 3Y rev) at `G5` ceiling `<= $335.00`.
- **8. Final Tier & Trigger:** **Tier 3 on Core/`#14a` (`#9` 3Y rev `10.97% < 12%` starter floor, `<25% IRR`); Tier 2 `G-watch` at `<= $335.00` if next-FY organic rev `>= 10.0%`.**

---

#### 8. `ATI` — ATI Inc. (`[NEW DISCOVERY]`) — **TIER 2 `#14a` STARTER WATCH (`<= $175.00` + FY27 Rev `>= 10%`)**
- **1. Market Data & `PH`:** `$189.50` | Market Cap `$25.5B` | 200DMA `$169.78` (`+11.6%` above 200DMA, valid) | ATH `$214.00` (Aug 2026, DD `-11.4%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `10.12%` (FY26E `$5.14B` `+12.1%`, FY27E `$5.65B` `+9.9%`), 3Y EPS CAGR `32.26%`, Buyback `+1.8%`, Multiple normalization (`36.4x -> 30x` = `-6.2%/yr`) = **`~26.8%` Est. 3Y IRR (`>= 25%` plausible: YES).**
- **3. Dilution (`A1`):** Shares `-1.80%` YoY (active buybacks), SBC `1.0%` of rev. Passes `A1` & `A2`.
- **4. Capex & FCF (`A3`):** TTM Rev `$4.72B`, TTM FCF `~$465M` (`9.85%` margin), FY26 guided FCF `$550M–$600M` (`$575M` midpoint `> TTM`), Capex/OCF `28.0%`. Passes `A3`.
- **5. Leverage (`A4`) & Moat (`A5`):** Cash `$783M`, Debt `$2.19B`, Net Debt `$1.41B` = **`2.45x` NTM FCF (`<= 2.50x` cap, tight)**. Oligopoly titanium/nickel specialty melt moat (`A5` pass).
- **6. Insiders & Legal (`#7`):** `<0.2%` net selling, clean legal.
- **7. Valuation (`#11`) & Asymmetry (`#12`):** Clears **High-Velocity Core `#11`** (`32.26%` 3Y EPS CAGR `>= 30%`, Fwd P/E `36.4x <= 45x`, PEG `1.13 <= 1.65`, FCF yield `2.25% >= 1.15%`) and `#12` (`$252.67` PT = `+33.3%` upside). However, fails `#9` (`10.12%` 3Y rev CAGR `< 15%`, and `< 12%` `#14a` 3Y floor; FY27 rev `+9.9%` is 10bp shy of `G2` `10.0%` floor).
- **8. Final Tier & Trigger:** **Tier 2 (`G-watch` / `#14a` Watch) — Exact Buy Trigger: `<= $175.00` once FY27 organic revenue consensus ticks `>= 10.0%` and 3Y rev `>= 12.0%` (or `G5` clears 12% return).**

---

#### 9. `CW` — Curtiss-Wright Corporation (`[NEW DISCOVERY]`) — **TIER 3 FAIL (`#9/#10/G2`, `#11` PEG, `#12` Void, `<25% IRR`)**
- **1. Market Data & `PH`:** `$500.00` | Market Cap `$18.48B` (`36.93M` shares) | 200DMA `$675.51` (**`-26.0%` below 200DMA -> voids `#12` PT leg**) | ATH `$735.00` (Jul 2026, DD `-32.0%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `~8.8%` (next-FY `+9.2%`), 3Y EPS CAGR `14.5%`, Buyback `+1.4%` = **`~15.5%` Est. 3Y IRR (`< 25%`).**
- **3. Dilution (`A1`):** Shares `-1.40%` YoY, active buybacks. Passes `A1` & `A2`.
- **4. Capex & FCF (`A3`):** TTM FCF `~$567M` (`16.2%` margin on `$3.50B` rev), Capex/OCF `14.5%`. Passes `A3`.
- **5. Leverage (`A4`) & Moat (`A5`):** Net Debt `~$530M` (`0.85x` NTM FCF), naval nuclear propulsion & defense electronics moat (`A5` pass).
- **6. Insiders & Legal (`#7`):** Clean.
- **7. Valuation (`#11`) & Asymmetry (`#12`):** Fwd P/E `31.21x`, PEG **`2.15` (`> 2.00` fail)**, FCF yield `3.37%` (`< 5.0%`), PT `$743.38` (`+48.7%` upside **VOID** due to price `-26.0%` below 200DMA -> `#12` fail!). Also fails `#9/#10/G2` (`3Y rev 8.8% < 10%` floor).
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `#9/#10/G2` `<10%` rev growth, `#11` PEG `2.15`, `#12` PT leg void & FCF yield `<5%`, `<25% IRR`).**

---

#### 10. `GE` — GE Aerospace (`[NEW DISCOVERY]`) — **TIER 3 FAIL (`#9/#10/G2` 3Y Rev `9.94% < 10%`, `#11` PEG, `<25% IRR`)**
- **1. Market Data & `PH`:** `$309.56` | Market Cap `~$332B` | 200DMA `$323.85` (`-4.4%`, valid) | ATH `$381.22` (`2026-08-05`, DD `-18.80%`, 3Y TR `+262.14%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR **`9.94%`**, Next-FY organic `+10.5%`, 3Y EPS CAGR `17.5%`, Buyback `+1.65%` = **`~17.8%` Est. 3Y IRR (`< 25%`).**
- **3. Dilution (`A1`):** Shares `-1.65%` YoY (multi-billion buybacks), SBC `0.8%` of rev. Passes `A1` & `A2`.
- **4. Capex & FCF (`A3`):** TTM FCF margin `17.8%`, NTM FCF `~$8.8B > TTM`, Capex/OCF `16.0%`. Passes `A3`.
- **5. Leverage (`A4`) & Moat (`A5`):** Net Debt/NTM FCF `~0.95x` (including Sep `$12B` CPP deal consideration check), dominant narrowbody/widebody jet engine monopoly/duopoly with CFM/LEAP/GE9X (`A5` pass).
- **6. Insiders & Legal (`#7`):** Clean (`<0.1%` net selling).
- **7. Valuation (`#11`) & Asymmetry (`#12`):** Fwd P/E `37.5x`, PEG **`2.14` (`> 2.00` fail)**, PT `$384` (`+24.0%`). Crucially, vendor 3Y revenue CAGR is **`9.94%` (`< 10.0%`)**, which fails `#9` (`15%`), `#14a` (`12%`), `#10` (`10%`), and Route `G2` (`10%`).
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `#9/#10/G2` 3Y rev CAGR `9.94% < 10.0%` floor, `#11` PEG `2.14`, `<25% IRR`).**

---

#### 11. `RTX` — RTX Corporation (`[NEW DISCOVERY]`) — **TIER 3 FAIL (`A1`, `A2`, `A3b`, `A4`, `#9`, `#11`, `#12`, `<25% IRR`)**
- **1. Market Data & `PH`:** `$184.68` | Market Cap `$246B` | 200DMA `$194.91` (`-5.2%`, valid) | ATH `$225.49` (`2026-08-18`, DD `-18.10%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `7.65%` (FY26 `+8.5%`, FY27 `+7.3%`), 3Y EPS CAGR `10.1%`, Buyback `0.0%` = **`~11.8%` Est. 3Y IRR (`< 25%`).**
- **3. Dilution (`A1` & `A2`):** Diluted WASO **`+0.81%` YoY** with **zero buybacks** and `$30.55B` net debt (`A1` and `A2` fail).
- **4. Capex & FCF (`A3`):** NTM FCF `$10.07B` **`<` TTM FCF `$11.41B`** (`A3b` fail).
- **5. Leverage (`A4`):** Net Debt `$30.55B` / `$10.07B` NTM FCF = **`3.03x` (`> 2.50x` cap — `A4` & `G2` fail)**.
- **6. Insiders & Legal (`#7`):** DOJ/SEC settlements paid down (`~$280M` remaining), GTF powder-metal recall compensation.
- **7. Valuation (`#11`) & Asymmetry (`#12`):** Fwd P/E `25.7x`, PEG **`2.55` (`> 2.50` fail)**, PT upside `+18.5% < 20%` and FCF yield `4.09% < 5.0%` (`#12` fail).
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `A1`, `A2`, `A3b`, `A4`, `#9`, `#11`, `#12`, `<25% IRR`).**

---

#### 12. `AAR` (`AIR`) — AAR Corp. (`[NEW DISCOVERY]`) — **TIER 3 FAIL (`A1`, `A2`, `A3a`, `A3c`, `A4`, `#9`)**
- **1. Market Data & `PH`:** `$100.00` | Market Cap `$3.85B` (`39.69M` shares) | 200DMA `$117.34` (`-14.8%`, valid) | ATH `$154.00` (Jun 2026, DD `-35.1%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR **`8.38%`**, 3Y EPS CAGR `16.15%`, Buyback `0.0%` = **`~18.2%` Est. 3Y IRR (`< 25%`).**
- **3. Dilution (`A1` & `A2`):** Equity offering diluted share count **`+12.4%` YoY** to fund MRO acquisitions (`Triumph Product Support` / `HAECO`), with net debt `$873.9M` and no active buybacks (`A1`, `A2`, `G3` fail).
- **4. Capex & FCF (`A3`):** TTM OCF `$199.4M`, TTM FCF **`$33.2M` (`1.00%` FCF margin on `$3.31B` rev `< 6.0%` floor)**; Capex/investments consume `83.3%` of OCF (`> 50%`). **Hard Fail on `A3a` & `A3c`.**
- **5. Leverage (`A4`):** Net Debt `$873.9M` (`978.4M` debt - `$104.5M` cash) = **`26.3x` TTM FCF / `~5.8x` NTM FCF (`> 2.5x` cap — `A4` fail)**.
- **6. Insiders & Legal (`#7`):** Past DOJ FCPA resolution settled; clean recent Form 4s.
- **7. Valuation (`#11`) & Asymmetry (`#12`):** Fwd P/E `16.7x`, PEG `1.35`, PT `$154.50` (`+54.5%`), but fails `#9/#10/G2` (`8.38%` 3Y rev `< 10%` floor).
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `A1`, `A2`, `A3a`, `A3c`, `A4`, `#9`, `<25% IRR`).**

---

#### 13. `KRMN` — Karman Holdings Inc. (`[NEW DISCOVERY]`) — **TIER 3 CORE/G FAIL (`A2`, `A3a`, `A4`, `#12`); TIER 2 `H-watch` (`<= $24.56`)**
- **1. Market Data & `PH`:** `$30.14` (Oct 14 close) | Market Cap `$4.00B` (`132.53M` diluted WASO) | 200DMA `$67.12` (**`-55.1%` below 200DMA -> voids `#12` PT leg**) | ATH `$115.29` (`2026-01-28`, DD `-73.86%`, `PH-short-history` / `PH-clear` by age).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `21.25%` (FY26 guide `$712M–$727M` `+24.7%` organic), 3Y EPS CAGR `27.8%` = **`~22.5%` Est. 3Y IRR at `$30.14`** (`~26.0%` at `$24.56` `H4` ceiling).
- **3. Dilution (`A1`):** Under Policy Rev 5's `<= 0.50%` bolt-on stock carve-out, `KRMN` issued `204,244` shares (`0.154%` of diluted WASO) for Five Axis + Seemann Composites, keeping total YoY diluted WASO at **`+0.158%` (`<= 0.50%` — `A1` PASS!)**. However, zero buybacks with net debt fails `A2`.
- **4. Capex & FCF (`A3`):** TTM Company FCF **`-$27.67M` (`-4.69%` margin < `6%` floor)** and FY25 OCF `-$22.12M` (fails `A3a` and `G2`, routing to **Route H** turnaround/inflection). FY26E FCF `$96M` (`13.2%` margin).
- **5. Leverage (`A4` & `H2`):** Pro forma Net Debt `$811.7M` notes + `$102.1M` finance leases (including `$95M` all-cash Walker Marine deal) = `$913.8M` (`9.52x` FY26E FCF — fails `A4`/`G2` `2.5x`, though inside `H2` `3.5x` EBITDA covenant).
- **6. Insiders & Legal (`#7`):** `0.0%` officer Open-market selling (Sep 2025 sponsor secondary by Trive Capital excluded from officer test), **BUT** J Capital short report (Sep 24, 2026), 3 disclosed material weaknesses in ICFR, and Sep 21 CFO departure create severe governance/accounting risk.
- **7. Valuation (`#11` / `H4`) & Asymmetry (`#12`):** Fwd P/E `38.6x`, PEG `1.39`, PT `$88.20` (**VOID** at `-55.1%` below 200DMA). Under **Route H (`H4`)**, 5Y base annualized return at `$30.14` is `15.2%` (`< 20.0%` `H4` minimum hurdle; `20%` return ceiling is **`$24.56`**).
- **8. Final Tier & Trigger:** **Tier 3 Fail for Core/G (`A2`, `A3a`, `A4`, `#12`); Tier 2 `H-watch` at `<= $24.56` (requires ICFR remediation).**

---

#### 14. `SAF.PA` — Safran SA (`[NEW DISCOVERY]`) — **TIER 2 NEAR-PASS WATCHLIST (`G-watch` at `<= €310–€323`)**
- **1. Market Data & `PH`:** `€314.90` mid-Oct (`€330.10` Oct 2 close) | Market Cap `€131.1B` | 200DMA `€338.50` (`-7.0%`, valid) | ATH `€365.80` (Aug 2026, DD `-13.9%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `12.15%`, Next-FY organic `+13.0%`, 3Y EPS CAGR `24.85%`, Buyback `+1.2%` = **`~25.4%` Est. 3Y IRR at `€314.90` (`>= 25%` plausible: YES).**
- **3. Dilution (`A1` & `G3`):** 2027/2028 Oceanes convertible bond dilution pushed diluted share count `+1.65%` YoY (failing Core `A1`, but clearing **Route G `G3` `<= 3.0%`** backed by `€5B` buyback program cancelling shares).
- **4. Capex & FCF (`A3` & `G2`):** TTM FCF margin `14.8%` (`>= 6%`), NTM FCF `~€4.5B > TTM`, Capex/OCF `22.0%`. Passes `A3`/`G2`.
- **5. Leverage (`A4` & `G2`) & Moat (`A5` & `G1`):** Net Cash position (`-0.4x` NTM FCF), 50/50 CFM/LEAP narrowbody engine monopoly with GE (`>35,000` CFM56/LEAP installed base, multi-decade shop-visit annuity — passes `G1`/`A5`).
- **6. Insiders & Legal (`#7` & `G4`):** Verified via French AMF PDMR filings: 12m net insider selling `~0.001%` (`<= 0.5%`), zero legal RPL. Passes `A7`/`G4`.
- **7. Valuation (`#11` / `G5`), Asymmetry (`#12`) & Print (`#19`):** Fwd P/E `26.2x`, PEG `1.05`, PT `€381.50` (`+21.1%` upside), H1 2026 print beat & raised FY guide (`#19` clear). Fails Core `#9` (`12.15%` 3Y rev `< 15%`) + `A1` (2 Core fails -> routes to **Route G**). Under Policy Rev 5 (`G5` 12.0% 5Y base return hurdle), `SAF.PA` returned `10.6%/yr` at `€330.10`, making **`€310.00–€323.00`** the exact 12% `G5` entry ceiling!
- **8. Final Tier & Trigger:** **Tier 2 (`G-watch`) — Exact Buy Trigger: `<= €310.00–€323.00` (currently testing the top of this buy zone at `~€314.90`!).**

---

#### 15. `MTU.DE` (`MTX`) — MTU Aero Engines AG (`[NEW DISCOVERY]`) — **TIER 3 FAIL (`A3a`, `#9`, `#12`, `<25% IRR`)**
- **1. Market Data & `PH`:** `€350.70` | Market Cap `€19.12B` | 200DMA `€362.10` (`-3.1%`, valid) | ATH `€394.50` (Jul 2026, DD `-11.1%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `10.8%`, Next-FY organic `+11.5%`, 3Y EPS CAGR `16.4%`, Buyback `0.0%` = **`~17.9%` Est. 3Y IRR (`< 25%`).**
- **3. Dilution (`A1`):** Shares `+0.20%` YoY.
- **4. Capex & FCF (`A3a`):** Ongoing Pratt & Whitney PW1100G (GTF) fleet inspection compensation payments have depressed TTM Company FCF to `~€410M` (**`4.8%` FCF margin `< 6.0%` `A3a` & `G2` floor**).
- **5. Leverage (`A4`) & Moat (`A5`):** Net Debt `~€650M` (`~0.9x` normalized FCF), 18% GTF program partner & independent MRO leader.
- **6. Insiders & Legal (`#7`):** Clean BaFin directors' dealings.
- **7. Valuation (`#11`) & Asymmetry (`#12`):** Fwd P/E `18.2x`, PEG `1.11`, **PT `€413.35` (`+17.8% < 20%` required) AND NTM FCF yield `2.15% < 5.0%` -> fails `#12` on both legs**, plus fails `#9` (`10.8% < 15%`).
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `A3a`/`G2` `<6%` FCF margin, `#9` `<15%`, `#12` `<20%` PT & `<5%` FCF yield, `<25% IRR`).**

---

### LANE 2: Global Mobility, Local Commerce & Travel Toll-Booths (9 Tickers)

#### 16. `UBER` — Uber Technologies, Inc. (Seed) — **TIER 1 WAIVER (`#10`) PASS (Actionable Now at `$69.62–$71.50`)**
- **1. Market Data & Price Health (`PH`):**
  - **Spot Price:** `$71.50` (Sep 28 re-test baseline `$69.62`) | **Market Cap:** `~$147B` (`~2.06B` diluted shares).
  - **200DMA:** `$74.32–$75.15` (`-3.8%` to `-6.3%` below 200DMA — well inside `-20%`, so `#12` PT leg is **valid**).
  - **3Y ATH & Drawdown:** `$93.60` (Oct 2025, age `1.0y < 3.0y`), drawdown `-23.6%`, `PH-clear`.
- **2. 25% 3-Year IRR Math:**
  - **3Y Revenue CAGR:** `13.62%` (FY26E `+11.3%`).
  - **3Y EPS / FCF CAGR:** `30.94%–32.7%` EPS CAGR (`26.5%` FCF/sh CAGR) + `2.28%` Net Buyback Yield (`$6.9B` TTM repurchases) + `0.0%` multiple change (`17.0x` Fwd P/E) = **`~31.5%` Estimated 3Y Annualized IRR (`>= 25%` hurdle cleared: YES).**
- **3. Dilution Gate (`A1` & `A2`):**
  - **YoY Diluted WASO:** **`-3.55%` YoY** (period-end shares `-2.28%` YoY), backed by `$6.9B` TTM share repurchases. **SBC:** `~$1.9B` (`3.8%` of rev, `18.8%` of TTM FCF). Delivery Hero Taiwan/foodpanda deals (`$13.7B` aggregate consideration) are **100% cash-settled** (`0` shares issued). **Status: `A1` & `A2` PASS.**
- **4. Capex & FCF Gate (`A3a/b/c`):**
  - **TTM Company FCF:** `$10.12B` (`19.4%` margin `>= 6.0%` floor).
  - **NTM FCF vs TTM FCF:** NTM FCF `~$12.4B` (`122.5%` of TTM FCF `>= 100%`).
  - **Capex / NTM OCF:** `~6.5%` (`<= 50%` cap). **Status: `A3a/b/c` PASS.**
- **5. Leverage (`A4`) & Moat/Margin (`A5`):**
  - **Pro Forma Net Debt / NTM FCF:** Including the `$13.7B` all-cash Delivery Hero acquisition, pro forma Net Debt / NTM FCF is **`~1.50x` (`<= 2.50x` ceiling)**.
  - **Moat & Gross Margin (`A5`):** Global #1 mobility & local delivery network across 70+ countries; NTM GM expanding alongside high-margin `$1.5B+` advertising run-rate. **Status: `A4` & `A5` PASS.**
- **6. Insiders & Legal (`#7` / `A7`):**
  - **Insiders:** Net buyers/clean — CEO Dara Khosrowshahi **purchased `141,000` shares (`~$10M`) in the open market on Sep 10, 2026**; zero quarters with `>= 3` officers making discretionary sales.
  - **Legal (`#7b`):** Driver classification & MDL reserves accrued on balance sheet; no unaccrued RPL `> 5%` of NTM FCF (`~$620M`). **Status: `A7` PASS.**
- **7. Disintermediation (`#8`), Waiver (`#10`), Asymmetry (`#12`) & Print (`#19`):**
  - **Routed to `#10` by `#8`:** Autonomous Vehicle (AV / Waymo / Tesla Robotaxi) disintermediation risk routes `UBER` to the **`#10` High-FCF-Yield Waiver** with a standing `#15` AV fleet-utilization trigger.
  - **Clears all 6 legs of `#10`:** (1) Next-FY & 3Y rev `>= 10%` (`11.3%` & `13.62%`), (2) NTM FCF yield `>= 5.0%` (**`8.70%`**), (3) PEG `< 1.0` (**`0.62`** at `17.0x` Fwd P/E), (4) Net buyback yield `>= 2.0%` (**`2.28%`**), (5) 3Y EPS CAGR `>= 20%` (**`30.94%–32.7%`**), and (6) all of Section A.
  - **Asymmetry (`#12`) & Print (`#19`):** Consensus PT `$100.86–$101.24` (`+41.5%` upside, 50 analysts) AND `8.70%` FCF yield (`>= 5.0%`); Q2 2026 print beat all four `#19` legs.
- **8. Final Tier Classification & Exact Dollar Buy Trigger:**
  - **Tier 1 (`#10` Waiver Pass — Actionable Now at `$69.62–$71.50`; Buy Trigger Ceiling `<= $84.00` where PT upside remains `>= +20%` and FCF yield `>= 7.2%`).**

---

#### 17. `DASH` — DoorDash, Inc. (Seed) — **TIER 3 FAIL (`A1` Diluted WASO `+1.82%` YoY, `G5` `<12%`, `#8/#10`)**
- **1. Market Data & `PH`:** `$191.99` | Market Cap `$83.6B` (`438.82M` diluted WASO) | 200DMA `$185.16` (`+3.7%`, valid) | ATH `$285.50` (`2025-10-15`, DD `-32.8%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `17.34%` (Q2'26 `+36%` total / `+24%` organic ex-Deliveroo), 3Y EPS CAGR `42.19%`, Diluted WASO drag `-1.82%/yr`, Multiple compression (`27.8x -> 22x` = `-7.5%/yr`) = **`~28.4%` gross / `~22.5%` net of SBC & dilution.**
- **3. Dilution (`A1` & `G3`):** Per **Note 12 of DoorDash's Q2 2026 Form 10-Q (ended June 30, 2026)**, Three-Month Diluted WASO rose from **`430,958k` (Q2 2025) to `438,818k` (Q2 2026) = `+1.824%` YoY**, breaching both the `+0.50%` standard `A1` ceiling AND the `+1.50%` high-growth buyback exception ceiling! Driven by **`$1.2B–$1.3B` guided FY26 SBC** (`7.6%` of revenue, `58.4%` of TTM FCF) plus May 2025 `$2.5B` 0% Convertible Senior Notes due 2030 and Oct 2025 £2.9B Deliveroo acquisition integration. **Hard Fail on `A1`.**
- **4. Capex & FCF (`A3`):** TTM FCF `$2.14B` (`13.1%` margin on `$16.34B` rev), NTM FCF `~$3.1B`, Capex/OCF `14.0%`. Passes `A3`.
- **5. Leverage (`A4`) & Moat (`A5`):** Net Cash position (`~$5.5B` cash vs `$2.5B` converts), #1 US restaurant delivery share (`67%`). Passes `A4` & `A5`.
- **6. Insiders & Legal (`#7`):** Heavy 10b5-1 sales by CEO Tony Xu, COO Adarkar, and Stanley Tang trust (`~0.35%` of shares out).
- **7. Valuation (`#11` / `G5`), Disintermediation (`#8`) & Print (`#19`):** Fwd P/E `27.8x`, PEG `0.65`, NTM FCF yield `3.70%`, PT `$273.32` (`+42.4%`).
  - **Why Route G Fails (`G5`):** Even though `G3` permits `<= 3.0%` ordinary dilution, `DASH` trades at `~39x` TTM FCF (`~98x` FCF net of `$1.25B` SBC) and `~27x` NTM FCF. Using a peer/mature terminal multiple (`16x–18x` FCF, in line with `UBER`/`BKNG`), 5Y base annualized return is only **`~4.5%–6.8%/yr` (`< 12.0%` `G5` minimum)**.
  - **Why `#8` / `#10` Fails:** If `#8` (autonomous robot/drone/AV delivery disintermediation) routes `DASH` to `#10`-only alongside `UBER` and `LYFT`, `DASH` fails `#10` on NTM FCF yield (`3.70% < 5.0%`) and net buyback yield (`-1.82%` diluted WASO vs `>= +2.0%` shrinkage required).
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `A1` `+1.82%` YoY diluted WASO on Q2'26 10-Q, `G5` `<12%` 5Y return, and `#8/#10` FCF yield & buyback failure).**

---

#### 18. `BKNG` — Booking Holdings Inc. (`[NEW DISCOVERY]`) — **TIER 3 FAIL (`#9/#10/G2` 3Y Rev `8.79% < 10%`, `<25% IRR`)**
- **1. Market Data & `PH`:** `$5,112` (or `$159` split-adj) | Market Cap `$166.5B` | 200DMA `$5,810` (`-12.0%`, valid) | ATH `$6,285` (Jul 2026, DD `-18.7%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR **`8.79%`** (next-FY `+8.89%`), 3Y EPS CAGR `17.45%`, Net Buyback Yield `+4.16%` = **`~19.8%` Est. 3Y IRR (`< 25%`).**
- **3. Dilution (`A1`):** Shares `-4.16%` YoY (world-class cannibal buybacks), SBC `1.9%` of rev. Passes `A1` & `A2`.
- **4. Capex & FCF (`A3`):** TTM FCF `$9.54B` (`34.8%` margin), NTM FCF `$10.2B`, Capex/OCF `4.5%`. Passes `A3`.
- **5. Leverage (`A4`) & Moat (`A5`):** Net Debt `$3.41B` (`$20.92B` debt - `$17.21B` cash) = `0.36x` NTM FCF; #1 global OTA moat (`A4` & `A5` pass).
- **6. Insiders & Legal (`#7`):** Clean Form 4s; EU DMA gatekeeper fines manageable (`<5%` FCF).
- **7. Valuation (`#11`) & Asymmetry (`#12`):** Fwd P/E `14.4x`, PEG `0.82`, FCF yield `5.95%`, PT `+29.9%`. Fails `#9` (`15%`), `#14a` (`12%`), `#10` (`10%`), and Route `G2` (`10%`) because **both next-FY (`8.89%`) and 3Y revenue CAGR (`8.79%`) are below the absolute `10.0%` floor**.
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `#9/#10/G2` revenue growth `8.79% < 10.0%` floor, `<25% IRR`).**

---

#### 19. `ABNB` — Airbnb, Inc. (`[NEW DISCOVERY]`) — **TIER 3 FAIL (`#9` + `#12` Dual Fail, `PH-warning`, `<25% IRR`)**
- **1. Market Data & `PH`:** `$165.67` | Market Cap `$97.7B` (`589.6M` shares) | 200DMA `$144.63` (`+14.5%`, valid) | ATH `$219.94` (Feb 2021, age `5.6y >= 3.0y`, DD `-24.7%` `< 30%` -> **`PH-warning`**).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `10.42%–12.87%` (next-FY `+10.4%`), 3Y EPS CAGR `16.46%`, Buyback `+3.80%`, Multiple compression (`28.1x -> 24x` = `-5.1%/yr`) = **`~16.5%` Est. 3Y IRR (`< 25%`).**
- **3. Dilution (`A1`):** Shares `-3.80%` YoY (`$3.5B+` buybacks offsetting `11.5%` SBC/rev). Passes `A1` & `A2`.
- **4. Capex & FCF (`A3`):** TTM FCF `$4.86B` (`38.2%` margin), Capex/OCF `1.5%`. Passes `A3`.
- **5. Leverage (`A4`) & Moat (`A5`):** Net Cash `$9.57B` (`$12.07B` cash vs `$2.50B` debt), #1 alternative accommodations moat. Passes `A4` & `A5`.
- **6. Insiders & Legal (`#7`):** Chesky/Gebbia/Blecharczyk 10b5-1 sales (`~0.35%` of shares out); IRS `$1.3B+` transfer-pricing dispute watch.
- **7. Valuation (`#11`) & Asymmetry (`#12`):** Fwd P/E `28.1x`, PEG `1.71`, NTM FCF yield `4.70%` (`< 5.0%`), **Consensus PT `$179.77` (`+8.5%` upside `< +20.0%` required) -> fails `#12` on both PT and FCF yield legs!** Combined with `#9` fail (`10.42%–12.87% < 15%`), `ABNB` has **two Core gate failures (`#9` + `#12`)**, disqualifying it from `#14a` Starter, fails `#10` (`PEG 1.71 > 1.0`, `3Y EPS 16.46% < 20%`, `FCF yield 4.7% < 5%`), and fails `G5` (`<12%` 5Y base return after `11.5%` SBC deduction).
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `#9` + `#12` dual Core fail, `G5` `<12%`, `<25% IRR`).**

---

#### 20. `CART` — Maplebear Inc. / Instacart (`[NEW DISCOVERY]`) — **TIER 2 `#14a` / `#10` WATCH (`<= $48.50`)**
- **1. Market Data & `PH`:** `$49.40` | Market Cap `$12.8B` | 200DMA `$42.59` (`+16.0%`, valid) | ATH `$56.40` (Aug 2026, DD `-12.4%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `11.20%` (FY26E `$4.26B` `+13.8%`, FY27E `$4.71B` `+10.5%`), 3Y EPS CAGR `19.50%`, Net Buyback Yield `+4.20%` = **`~24.4%` Est. 3Y IRR at `$49.40` (`~25.2%` at `<= $48.50`).**
- **3. Dilution (`A1`):** Shares `-4.20%` YoY via aggressive `$1.5B+` share repurchase program; SBC `9.2%` of rev. Passes `A1` & `A2`.
- **4. Capex & FCF (`A3`):** TTM Rev `$3.99B`, TTM FCF `~$818M` (`20.5%` margin), NTM FCF `~$880M`, Capex/OCF `5.5%`. Passes `A3`.
- **5. Leverage (`A4`) & Moat (`A5`):** Net Cash `$851M` (`-$0.97x` NTM FCF), #1 US digital grocery marketplace & retail media network (`~75%` gross margin). Passes `A4` & `A5`.
- **6. Insiders & Legal (`#7`):** Clean (`<0.3%` non-10b5-1 selling); FTC inquiry resolved (`$60M` settlement paid).
- **7. Valuation (`#11`) & Asymmetry (`#12`):** Fwd P/E `18.5x <= 38x`, PEG `0.95 <= 1.0`, **NTM FCF yield `6.20% >= 5.0%` (clears `#12` via the 5% FCF yield leg even though PT `$58.21` is `+17.8%`!)**. Fails Core `#9` (`11.2%` 3Y rev `< 15%` Core and `80bp` shy of `#14a` `12.0%` 3Y rev floor) and sits `50bp` shy of `#10` Waiver (`3Y EPS CAGR 19.5%` vs `>= 20.0%` required; all other 5 legs of `#10` pass!).
- **8. Final Tier & Trigger:** **Tier 2 (`#10` / `G-watch`) — Exact Buy Trigger: `<= $48.50` (where PT upside hits `+20.0%`, `G5` clears `12%`, and 3Y IRR clears `25%`, or upon 3Y EPS CAGR ticking `>= 20.0%` for `#10` Waiver).**

---

#### 21. `EXPE` — Expedia Group, Inc. (`[NEW DISCOVERY]`) — **TIER 3 FAIL (`#9/#10/G2` 3Y Rev `8.0% < 10%`, `<25% IRR`)**
- **1. Market Data & `PH`:** `$262.00` | Market Cap `$31.4B` (`120M` shares) | 200DMA `$254.50` (`+2.9%`, valid) | ATH `$295.00` (Jul 2026, DD `-11.2%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR **`8.00%`**, 3Y EPS CAGR `20.9%`, Buyback `+5.8%`, Multiple normalization (`11.6x -> 10x`) = **`~21.5%` Est. 3Y IRR (`< 25%`).**
- **3–7. Gate Summary:** Passes `A1–A7` (`WASO -5.8%`, `18.5%` FCF margin, `0.65x` Net Debt/FCF), `#11` (`11.6x` P/E, `0.58` PEG), and `#12` (`9.5%` FCF yield & `+22.1%` PT), **BUT** fails `#9/#10/G2` because 3Y revenue CAGR is **`8.00%` (`< 10.0%` floor)**.
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `#9/#10/G2` 3Y rev CAGR `8.00% < 10.0%` floor, `<25% IRR`).**

---

#### 22. `LYFT` — Lyft, Inc. (`[NEW DISCOVERY]`) — **TIER 3 / RE-TEST (`#8->#10` 3Y EPS `19.64% < 20%`, `#7b` Trial, `PH-impaired`)**
- **1. Market Data & `PH`:** `$15.02` | Market Cap `$6.05B` (`402.5M` diluted WASO) | 200DMA `$15.87` (`-5.4%`, valid) | ATH `$78.20` (Mar 2021, age `5.5y >= 3.0y`, DD `-80.8% >= 30%`, 3Y TR gap `< -20pp` -> **`PH-impaired`**).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `13.20%` (FY26E `+16.6%`, FY27E `+12.3%`), 3Y EPS CAGR `19.64%`, Buyback `+4.94%` = **`~23.8%` Est. 3Y IRR.**
- **3–7. Repo Verification (`roster.md`):** Shares `-4.94%` YoY (`402.5M` vs `424.0M` WASO; `$450M` 0% 2030 convert rolled off 12m `A1` window on Sep 5, 2026), Net Cash `$502M`, TTM FCF `$1.11B` (`16.4%` margin), FY26E FCF `$1.13B` (`A3b` thin), PT `$19.84` (`+32.1%`), Q2 `#19` clear. Routed to `#10`-only by `#8` (AV disintermediation): **fails `#10` 3Y EPS CAGR leg (`19.64%` vs `>= 20.0%` required, by 36bp)**, faces live **`#7b` state bellwether sexual-assault trial RPL risk (`> $55M` = out)**, and is **`PH-impaired`**.
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `PH-impaired`, `#10` 3Y EPS `19.64% < 20%`, `#7b` bellwether trial RPL risk; re-test after Nov 5 print).**

---

#### 23. `MMYT` — MakeMyTrip Limited (`[NEW DISCOVERY]`) — **TIER 3 FAIL (`A1`, `#11` P/E `72.97x` & PEG `4.05`, `<25% IRR`)**
- **1. Market Data & `PH`:** `$105.00` | Market Cap `$11.6B` | 200DMA `$98.50` (`+6.6%`, valid) | ATH `$124.00` (Jul 2026, DD `-15.3%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `20.34%`, 3Y EPS CAGR `32.78%`, Dilution `-2.1%`, Multiple compression (`72.97x -> 40x` = `-18.2%/yr`) = **`~18.5%` Est. 3Y IRR (`< 25%`).**
- **3–7. Gate Summary:** Diluted WASO **`+2.10%` YoY** with no net buyback shrinkage (`A1` fail); **Fwd P/E `72.97x` (`> 45x` High-Velocity & `> 48x` Starter ceiling), PEG `4.05` (`> 1.65` / `2.50` ceiling), NTM FCF yield `0.90%` (`< 1.00%` floor) -> fails all three `#11` components!**
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `A1`, `#11` P/E `72.97x` / PEG `4.05` / FCF yield `0.90%`, `<25% IRR`).**

---

#### 24. `TCOM` — Trip.com Group Limited (`[NEW DISCOVERY]`) — **TIER 3 FAIL (`#9/#10/G2`, `#12` Void, `#7` China ADR)**
- **1. Market Data & `PH`:** `$38.00` | Market Cap `$23.9B` (`629.71M` shares) | 200DMA `$50.12` (**`-24.2%` below 200DMA -> voids `#12` PT leg**) | ATH `$69.50` (Oct 2025, DD `-45.3%`, `PH-clear` by age).
- **2. 25% 3Y IRR Math:** Forward 3Y Rev CAGR **`8.60%`**, 3Y EPS CAGR `12.5%`, Buyback `+3.96%` = **`~16.4%` Est. 3Y IRR (`< 25%`).**
- **3–7. Gate Summary:** Shares `-3.96%` YoY, Net Cash `$7.7B`, TTM FCF margin `24.5%`, Fwd P/E `10.0x`, FCF yield `8.50%` (clears `#12` FCF leg while PT `$58.44` is void). Fails **`#9/#10/G2` on 3Y forward revenue CAGR (`8.60% < 10.0%` floor)** and China ADR `#7` insider verification gap.
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `#9/#10/G2` 3Y rev `8.60% < 10.0%` floor, `<25% IRR`).**

---

### LANE 3: EM E-Commerce, Logistics & Non-Bank Payment Ecosystems (10 Tickers — All Subject to Overlay `FT` Except `CPNG` & `PDD`)

#### 25. `MELI` — MercadoLibre, Inc. (Seed — Overlay `FT`) — **TIER 3 FAIL (`A3b`, `FT2/A3a`, `A5`, `FT1`)**
- **1. Market Data & `PH`:** `$1,696.56` | Market Cap `$86.0B` | 200DMA `$1,837.61` (`-7.7%`, valid) | ATH `$2,613.63` (`2025-06-30`, DD `-35.09%`, `PH-clear`).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `32.02%`, Next-FY organic `+28.0%`, 3Y EPS CAGR `31.5%`, Buyback `0.0%` = **`~29.2%` Est. 3Y IRR (`>= 25%` plausible: YES).**
- **3. Dilution (`A1`):** Diluted WASO `0.00%` YoY (`50.7M` shares), SBC `0.9%` of rev. Passes `A1`.
- **4. Capex & Normalized Fintech FCF (`A3a/b/c` & `FT2`):** Under **Overlay `FT` (`FT2`)**, Mercado Pago credit-book originations and customer deposit liability inflows must be stripped from operating cash flow. On an `FT2` normalized basis, **TTM Company FCF margin is `~3.3%` (`< 6.0%` `A3a` floor)**, and even on a published basis, **NTM FCF is `-1.9%` below TTM FCF (`A3b` fail)** due to fulfillment center buildouts (`32%` Capex/OCF) and credit card portfolio expansion.
- **5. Leverage (`A4`) & Moat/Margin (`A5`):** LatAm e-commerce + fintech leader, **BUT** credit-provisioning and shipping mix compressed **Gross Margin by `-858bp` YoY, breaching the `-600bp` hard ceiling of the `#5` (`A5`) gross-margin mix carve-out!**
- **6–8. Final Tier:** Because `FT1` prohibits `#14a` Starters and Route G/H for fintech/hybrid lenders, `MELI` is a **Tier 3 Hard Gate Fail (`A3b`, `FT2/A3a` `3.3% < 6.0%` normalized FCF margin, `A5` `-858bp` GM compression).**

---

#### 26. `SE` — Sea Limited (Seed — Overlay `FT`) — **TIER 3 FAIL (`A1` WASO `+2.70%`, `A2`, `FT1`, `PH-warning`)**
- **1. Market Data & `PH`:** `$95.19` | Market Cap `$56.5B` | 200DMA `$102.89` (`-7.5%`, valid) | ATH `$366.99` (`2021-10-19`, age `4.95y >= 3.0y`, DD `-74.06% >= 30%`, 3Y TR `+116.59%`, gap `+29.27pp > -20pp` -> **`PH-warning`**).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `20.5%`, 3Y EPS CAGR `34.0%`, Dilution `-2.7%` = **`~27.5%` Est. 3Y IRR.**
- **3. Dilution (`A1` & `A2`):** Verified on Oct 2 re-test: **Diluted WASO grew `+2.70%` YoY** (period-end shares `+2.32%` YoY) with **zero share buybacks (`A2` fail)** and `3.9%` SBC/rev. **Hard Fail on `A1` & `A2`.**
- **4–8. Final Tier:** SeaMoney consumer/SME lending triggers **Overlay `FT` (`FT1`)**, which **blocks Route G** (where `<= 3.0%` dilution would otherwise be tested). **Tier 3 (Hard Gate Fail: `A1` `+2.70%` diluted WASO, `A2` no buybacks, `FT1` blocks Route G, `PH-warning`).**

---

#### 27. `CPNG` — Coupang, Inc. (Seed) — **TIER 3 FAIL (`A3a`, `A3c`, `#9`, `#11`, `PH-impaired`)**
- **1. Market Data & `PH`:** `$14.40` | Market Cap `$25.88B` | 200DMA `$17.92` (`-19.6%`, valid by 40bp) | ATH `$69.00` (Mar 2021, age `5.6y >= 3.0y`, DD `-79.1% >= 30%`, 3Y TR gap `< -20pp` -> **`PH-impaired`**).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `10.5%`, 3Y EPS CAGR `67.0%`, Multiple compression (`49.1x -> 28x`) = **`~24.0%` Est. 3Y IRR.**
- **3–7. Gate Summary:** TTM OCF `$1.43B` minus TTM Capex `-$1.33B` = **TTM Company FCF `$100M` on `$34.5B` revenue (`0.29%` FCF margin `< 6.0%` `A3a` floor)** and **Capex/OCF = `93.0%` (`> 50.0%` `A3c` cap)**! Also fails `#9` (`10.5%` 3Y rev `< 15%`), `#11` (Fwd P/E **`49.13x > 48.0x`**), and **`PH-impaired`**.
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `A3a` `0.29%` FCF margin, `A3c` `93.0%` Capex/OCF, `#9` `10.5%`, `#11` P/E `49.1x`, `PH-impaired`).**

---

#### 28. `DLO` — dLocal Limited (`[NEW DISCOVERY]` — Overlay `FT`) — **TIER 3 FAIL (`PH-impaired`, `FT2/A3a/A3b`, `A5`)**
- **1. Market Data & `PH`:** `$14.80` | Market Cap `$4.35B` | 200DMA `$13.95` (`+6.1%`, valid) | ATH `$64.69` (Aug 2021, age `5.1y >= 3.0y`, DD `-77.1% >= 30%`, 3Y TR gap `< -20pp` -> **`PH-impaired`**).
- **2. 25% 3Y IRR Math:** 3Y Rev CAGR `32.5%`, 3Y EPS CAGR `26.0%`, Buyback `+1.2%` = **`~26.4%` Est. 3Y IRR.**
- **3–7. Gate Summary:** Under **Overlay `FT` (`FT2`)**, stripping merchant settlement funds payable from OCF reduces normalized TTM FCF margin to `~4.8%` (`< 6.0%` `A3a` floor) and NTM FCF `<` TTM FCF (`A3b` fail), while EM take-rate compression breaches `A5` gross margin stability and **`PH-impaired`** blocks all new capital.
- **8. Final Tier:** **Tier 3 (Hard Gate Fail: `PH-impaired`, `FT2/A3a/A3b`, `A5`).**

---

#### 29. `PAGS` — PagSeguro Digital Ltd. (`[NEW DISCOVERY]` — Overlay `FT`) — **TIER 3 FAIL (`#9` `6.5% < 15%`, `PH-impaired`, `<25% IRR`)**
- **1. Market Data & `PH`:** `$9.60` | Market Cap `$3.05B` | 200DMA `$10.85` (`-11.5%`, valid) | ATH `$62.83` (Feb 2021, age `5.6y`, DD `-84.7%`, **`PH-impaired`**).
- **2–8. Gate Summary:** 3Y Rev CAGR **`6.50%` (`< 15.0%` `FT1` mandatory floor and `< 10.0%` `#10` floor)**, 3Y IRR `~14.2%` (`< 25%`), and **`PH-impaired`**. **Tier 3 Hard Gate Fail (`#9`, `PH-impaired`, `<25% IRR`).**

---

#### 30. `STNE` — StoneCo Ltd. (`[NEW DISCOVERY]` — Overlay `FT`) — **TIER 3 FAIL (`#9` `<15%`, `A4/FT2`, `PH-impaired`, `<25% IRR`)**
- **1. Market Data & `PH`:** `$11.65` | Market Cap `$2.75B` (`230.6M` shares) | 200DMA `$13.80` (`-15.6%`, valid) | ATH `$95.12` (Feb 2021, age `5.6y`, DD `-87.8%`, **`PH-impaired`**).
- **2–8. Gate Summary:** 3Y Rev CAGR **`11.5%` (`< 15.0%` `FT1` mandatory floor — no `#14a` or Route G allowed under `FT1`)**, Total Debt `$3.27B` vs Cash `$1.58B` (`$1.69B` net debt funding credit book -> fails `A4/FT2` on normalized FCF), 3Y IRR `~19.5%` (`< 25%`), and **`PH-impaired`**. **Tier 3 Hard Gate Fail (`#9`, `A4/FT2`, `PH-impaired`, `<25% IRR`).**

---

#### 31. `GRAB` — Grab Holdings Limited (`[NEW DISCOVERY]` — Overlay `FT`) — **TIER 3 FAIL (`A3a` Negative FCF, `A3c`, `FT4`, `PH-impaired`)**
- **1. Market Data & `PH`:** `$3.15` | Market Cap `$12.05B` | 200DMA `$3.65` (`-13.7%`, valid) | ATH `$18.11` (Nov 2021, age `4.9y`, DD `-82.6%`, **`PH-impaired`**).
- **2–8. Gate Summary:** TTM OCF `-$60M`, Capex `-$100M`, **TTM Company FCF `-$160M` (`-4.29%` margin on `$3.73B` rev `< 6.0%` `A3a` floor)**, fails `FT4` (requires 2 completed FYs of positive normalized FCF), Diluted shares `+0.90%` YoY (`6.8%` SBC/rev), and **`PH-impaired`**. **Tier 3 Hard Gate Fail (`A3a`, `A3c`, `FT4`, `PH-impaired`).**

---

#### 32. `PDD` — PDD Holdings Inc. (`[NEW DISCOVERY]`) — **TIER 3 FAIL (`A1/A2`, `#9`, `#12` Void, `PH-impaired`, `<25% IRR`)**
- **1. Market Data & `PH`:** `$75.38` | Market Cap `$104.7B` | 200DMA `$94.50` (**`-20.2%` below 200DMA -> voids `#12` PT leg**) | ATH `$202.82` (`2021-02-17`, age `5.62y`, DD `-62.83%`, 3Y TR gap `-111.69pp` -> **`PH-impaired`**).
- **2–8. Gate Summary:** Verified in repo (`concurrent_pr_audit.md` / `price_health_results.csv`): **Zero share buybacks (`A2` fail)** with basic/period-end shares **`+0.70%–0.72%` YoY (`A1` fail)**, **3Y Rev CAGR `9.42%` & 3Y EPS CAGR `9.99%` (`< 10.0%` `#9/#10/G2` floor)**, 3Y IRR `~11.5%` (`< 25%`), and **`PH-impaired`**. **Tier 3 Hard Gate Fail (`A1`, `A2`, `#9/#10/G2`, `PH-impaired`, `<25% IRR`).**

---

#### 33. `GLBE` — Global-E Online Ltd. (`[NEW DISCOVERY]` — Overlay `FT`) — **TIER 3 FAIL (`A7` Insider Selling `0.74%`, `PH-impaired`)**
- **1. Market Data & `PH`:** `$39.31` | Market Cap `$6.65B` | 200DMA `$35.57` (`+10.5%`, valid) | ATH `$81.69` (`2021-09-01`, age `5.08y`, DD `-51.88%`, 3Y TR gap `-86.98pp` -> **`PH-impaired`**).
- **2–8. Gate Summary:** Verified in repo (`fintech.md` / `price_health_results.csv`): **12m net insider selling is `0.74%` of shares outstanding (`> 0.50%` `A7` hard ceiling)** and **`PH-impaired`** (`-86.98pp` 3Y relative return gap vs S&P 500). **Tier 3 Hard Gate Fail (`A7`, `PH-impaired`).**

---

#### 34. `TOST` — Toast, Inc. (`[NEW DISCOVERY]` — Overlay `FT`) — **TIER 3 FAIL (`PH-impaired`, `FT3/A7b` FTC Complaint)**
- **1. Market Data & `PH`:** `$29.79` | Market Cap `$16.9B` | 200DMA `$29.78` (`0.0%`, valid) | ATH `$65.22` (`2021-11-02`, age `4.91y`, DD `-54.32%`, 3Y TR gap `-24.71pp <= -20.0pp` -> **`PH-impaired`**).
- **2–8. Gate Summary:** Verified in repo (`fintech.md` / `concurrent_pr_audit.md`): Fails **`PH-impaired`** (`4.91y` ATH age, `54.32%` drawdown, `-24.71pp` 3Y TR gap vs S&P 500, no `PH-recovery` 10-day streak above rising 200DMA) AND fails **`FT3` / `A7b`** due to an active FTC draft complaint where management discloses that reasonably possible loss "cannot be estimated" (`FT1` also blocks `#14a` and Route G). **Tier 3 Hard Gate Fail (`PH-impaired`, `FT3/A7b`).**

---

# Batch 2 (Lanes 4, 5, and 6) Open-Universe Non-AI-Capex Diversification Screen — Policy Revision 5 (`f6171aa`)

All 52 evaluated securities across **Lane 4 (Obesity, Metabolic, Rare Disease Biopharma & High-Velocity Medtech)**, **Lane 5 (Public Safety, Municipal GovTech & Autonomous/NATO Rearmament Defense)**, and **Lane 6 (Cybersecurity & Identity Consolidators)** have been rigorously audited against the `CyberFvde/asymmetry-gates` framework (**Policy Revision 5**, commit `f6171aa`) and cross-referenced against the repository's verified SEC/Oslo/AMF filing audits, `price_health_results.csv`, `insider-evidence.json`, and live StockAnalysis consensus feeds.

---

## Executive Triage Summary (Batch 2: Lanes 4–6)

### 1. Tier 1 — Immediate Capital-Eligible (Core / `#10` Waiver / `#14a` Starter / Ballast)
* **`LLY` (Eli Lilly — Lane 4 Seed):** **Ballast Slot Pass TODAY** (and **1-Step to Full Core Pass at `<= $1,107.36`**).
  * Passes every Stage A gate (`A1` WASO `-0.68%` YoY; `A2` `$6.17B` TTM buybacks; `A3a` TTM FCF margin `22.83%`; `A3b` NTM FCF `$28.81B` > TTM `$18.19B`; `A3c` NTM Capex/OCF `20.43%` despite manufacturing buildout; `A4` pro forma Net Debt/NTM FCF `1.77x` base / `2.00x–2.21x` at max exposure including Atai, Merida, InnoCare, CVRs & milestones `<= 2.5x`; `A5` Wide moat & `~83%+` GM; `A6` secular GLP-1/incretin tailwind; `A7`/`#7` verified across 126 Form 4s at **`0.3551%` net selling** from Lilly Endowment with **0 discretionary officer sales**—all 5 officer sales 10b5-1 flagged).
  * Passes `#9` (3Y Rev CAGR `20.49%`, FY26 Next-FY `+35.8%`), `#11` on both Standard and High-Velocity tracks (Fwd P/E `27.41x`, PEG `1.27`, 3Y EPS CAGR `30.95%`, NTM FCF yield `2.83%`), `#19` (Q2 EPS `$8.38` vs `$6.40`, rev `$22.97B` vs `$20.82B`), and `PH-clear` (`$1,142.85` vs 200DMA `$1,073.81`, `-10.74%` DD).
  * **Why Ballast vs. Core:** Fails **only `#12`** because consensus PT upside is `+16.27%` (`$1,328.83` vs `>= +20.0%` hurdle) and NTM FCF yield is `2.83%` (`< 5.0%`). Eligible immediately for the single **Ballast Slot** (`<= 4%` initial / `8%` max) and converts to **Full Core Pass at `<= $1,107.36`** (where PT `$1,328.83` = `+20.0%`). Plausible `>= 25%` 3Y IRR (`~26.5%` annualized: `30.95%` EPS CAGR + `0.62%` buyback + `0.5%` div, modest P/E normalization from `27.4x` to `25x`).

---

### 2. Tier 2 — Near-Pass Watchlist (1 Gate or Price-Trigger Away from Capital Eligibility)

1. **`NBIX` (`[NEW DISCOVERY]` Neurocrine Biosciences — Lane 4):** **Route G Near-Pass (`G-watch` on 17 bps `G3` WASO excess under Rev 5).**
   * **Policy Rev 5 Nuance:** In unmerged Policy Rev 4 (`d28bdc4`), `G3` ordinary dilution was relaxed to `<= 3.5%`, making `NBIX` (`+3.17%` YoY diluted WASO) immediately capital-eligible under Route G (`$143.18` vs `G5` entry ceiling `$175.00`, 5Y base return `14.5%/yr`, bear `74%`). However, **merged Policy Rev 5 (`f6171aa`) retained the `<= 3.0%` `G3` cap**, leaving `NBIX` **17 bps above `G3`** (`+3.17%` vs `3.00%`).
   * All other gates pass with huge headroom: Fwd P/E `12.66x`, PEG `0.31`, PT `$207.29` (`+44.8%`), Next-FY organic rev `+27.0%` ex-Soleno, 3Y Rev CAGR `16.70%`, TTM FCF `$870.4M` (`25.8%` margin, Capex/OCF `3.08%`), NTM FCF `129%` of TTM (`~7.78%` yield), Net Cash (`~0x` debt), `#7`/`G4` `0.494%` net insider selling, `#19` clear, `PH-clear` (`-2.77%` vs 200DMA `$147.26`). Plausible `>= 25%` 3Y IRR (`~27.5%`).
   * **Exact Buy Trigger:** Q3 print (`~Oct 27, 2026`) showing YoY diluted WASO `<= +3.00%` (via `$300M+` buyback offset) at price **`<= $175.00`** (and `#7` recount post-Oct 6 `<= 0.50%`).

2. **`PODD` (`[NEW DISCOVERY]` Insulet Corp — Lane 4):** **Core / Route G Near-Pass (`1-Step Watch` on `#12` 5.0% Cash-Yield Floor & `A5` GAAP GM).**
   * Price `$131.69`, `PH-clear` (`-62.68%` DD from Sep 2025 ATH `$352.82`, age `1.06 yrs < 3.0 yrs`). Because price is **`-31.90%` below 200DMA (`$193.38`)**, the `#12` consensus PT leg (`$171.91`, `+30.5%`) is **VOID** under Rule `#12`, requiring NTM FCF yield `>= 5.0%` (or `>= 4.5%` `#14a` starter).
   * Raw blended NTM FCF is `$469.75M` (`5.145%` yield, passing `#12`), **but** consensus FY26 capex (`$151M`) contradicts management guidance ("increasing vs FY25 `$191.6M`"). Applying the mandatory Rule `A3b`/`A3c` **`x1.25` capex fallback** (`$271.88M`) reduces NTM FCF to `$439.53M` (`4.814%` yield on blended capex) or `$375.73M` (`4.115%` yield on full-NTM capex), dropping it below the `5.0%` Core floor. In addition, `A5` GAAP H1 GM was `69.8%` (after `$33.6M` MDC cannula field-correction notices) vs FY25 `71.63%` (`71.81%` adjusted).
   * Passes `A1` (WASO `-1.77%` Q2 / `-1.19%` H1; 2026 converts redeemed all-cash Aug 2025), `A4` (`1.09x–1.36x` incl. `$97M` Costa Rica seller-loan guarantee), `#7` (**net insider buying `-0.0178%`** across 46 Form 4s; 0 officer sales; CEO bought 5,400 sh), `#9` (3Y rev `16.15%`, FY26 `+21.38%`), `#11` (Fwd P/E `19.09x`, PEG `0.96`), `#19` clear. Plausible `>= 25%` 3Y IRR (`~28.4%`).
   * **Exact Buy Trigger:** **`<= $126.76`** (blended capex fallback `5.0%` yield; `<= $140.84` for `4.5%` `#14a` starter once `A5` GAAP GM clears) or **`<= $108.35`** (full-NTM `x1.25` capex fallback `5.0%` yield), OR Q3 print (`Nov 4, 2026`) quantifying FY26/27 capex with NTM FCF `>= $456.5M` and H1'27 GAAP GM `>= 71.63%`. Provisional `G5` ceiling: **`$184.58`**.

3. **`KOG.OL` (`[NEW DISCOVERY]` Kongsberg Gruppen — Lane 5):** **Core Near-Pass (Blocked ONLY by `#19` Earnings Blackout until Oct 29, 2026).**
   * Price `NOK 308.00`, `PH-clear` (requires post-Apr 22, 2026 Kongsberg Maritime `KMAR` 1:1 demerger distribution adjustment on historical prices).
   * Passes `A1`/`A2` (flat shares YoY; watch Zone 5 minority buyout currency), `A3` (TTM FCF `~NOK 6.03B`, blended NTM FCF `NOK 9.90B`, Capex/OCF `~24%`), `A4` (Net Cash), `#7` (**verified clean via Oslo Børs Newsweb PDMR sweep**), `#9` (Next-FY rev `+36.4%`, 3Y CAGR `~22.5%`), `#11` (Fwd P/E `33.41x <= 38.0x`, PEG `0.96`, 3Y EPS CAGR `~34.8%`), and `#12` (PT `+28.5%`, 11 analysts). Plausible `>= 25%` 3Y IRR (`~26.5%`).
   * **Why Blocked Today:** In **`#19` Blackout** after Q2 continuing revenue (`-3.4%`) and EBITDA (`-8.8%` / EBIT `-5.0%`) missed post-demerger consensus.
   * **Exact Buy Trigger:** Clean Q3 print on **`Oct 29, 2026`** (clearing `#19` and confirming standalone FY27 defense/discovery FCF) at **`<= NOK 350.30`** (Rev 5 Core `38.0x` P/E ceiling; `<= NOK 322.66` at `35.0x`).

4. **`ARGX` (argenx SE — Lane 4 Seed):** **Route G Near-Pass (`G-watch` pending FY26 2nd positive OCF year in Feb 2027 & local AFM insider sweep).**
   * Price `~$810.00`, `PH-clear` (`-4.87%` vs 200DMA `$851.50`), Fwd P/E `29.74x`, PEG `0.85`, PT `$1,152` (`+42.2%`), 3Y Rev CAGR `30.39%`, 3Y EPS CAGR `32.75%`, TTM FCF `$849M` (`~19.5%` margin), Net Cash `-$5.1B`. Plausible `>= 25%` 3Y IRR (`~28.5%`).
   * Fails Core `A1`/`A2` (diluted WASO `+1.8%` from options/RSUs with zero buybacks), and under Route G (`G2`), requires **two completed positive-OCF fiscal years** (FY24 OCF was negative; FY25 was positive #1; FY26 completes in Feb 2027 as positive #2), plus Dutch AFM / Belgian FSMA insider register verification (`#7` alert-only).
   * **Exact Buy Trigger:** FY26 full-year print (Feb 2027) confirming 2nd positive OCF year + clean AFM/FSMA PDMR sweep at `G5` entry ceiling **`<= $785.00`**.

5. **`FTNT` (Fortinet — Lane 6 Seed):** **Route G Near-Pass (`G-watch` on Price vs. `G5` Ceiling).**
   * Price `$80.19`, `PH-clear` (`-1.74%` vs 200DMA `$81.61`), WASO `-3.85%` YoY (`$2.24B` H1 buybacks), TTM FCF `$2.43B` (`35.8%` margin, `4.04%` yield), Net Cash `-$1.18B`, `#7`/`G4` `0.145%` net selling (Xie brothers 10b5-1), `#19` clear.
   * Fails Core `#9` (3Y Rev CAGR `10.67% < 15.0%` and `< 12.0%` `#14a`), `#10` (3Y EPS `10.71% < 20%`), `#11` (PEG `2.34 > 2.0`), and `#12` (PT `$89.65 = +11.8% < 20%`, NTM FCF yield `~4.3% < 5.0%`). Passes `G1`–`G4` under Route G, but at `$80.19` its 5Y `G5` base return is `8.98%/yr` (`< 12.0%` hurdle).
   * **Exact Buy Trigger:** **`<= $72.24`** (`G5` `12.0%` base return ceiling at `22x` terminal P/FCF; or `<= $69.00` to also clear `#12` `5.0%` NTM FCF yield).

6. **`REGN` (`[NEW DISCOVERY]` Regeneron — Lane 4):** **Route G Near-Pass (`G-watch` on Price vs. `G5` Ceiling).**
   * Price `$735.20`, `PH-clear` (`-0.11%` vs 200DMA `$736.04`), Fwd P/E `12.02x`, PEG `1.00`, NTM FCF `$6.31B` (`8.59%` yield -> passes `#12` on cash yield), WASO `-2.39%` YoY (`$3.90B` buybacks), Net Cash `-$14.85B`, `#7` `0.017%` net selling, `#19` clear.
   * Fails Core `#9` (3Y Rev CAGR `11.36% < 15%`, FY27E `+8.7%`) and `#10` (3Y EPS `15.69% < 20%`). Under Route G, 5Y base return at `$735.20` is `8.1%/yr` (`< 12%`).
   * **Exact Buy Trigger:** **`<= $617.00`** (`G5` `12.0%` return ceiling, subject to FY27 organic revenue holding `>= 10%` under `G2`).

7. **`ISRG` (Intuitive Surgical — Lane 4 Seed):** **Route G / Core Near-Pass (2 simultaneous `#14a` shortfalls: `#9` 3Y Rev `14.11%` & `#11` PEG `2.25`).**
   * Price `$391.95`, `PH-clear` (`-12.36%` vs 200DMA `$447.22`), WASO `-1.11%` YoY, TTM FCF `$3.22B` (`29.21%` margin), Net Cash `-$5.22B`, Fwd P/E `34.69x` (passes Rev 5 `<= 38.0x`!). However, fails **both** `#9` (3Y Rev `14.11% < 15.0%`) and `#11` (PEG `2.25 > 2.0`), and Rule `#14a` prohibits combining two near-pass bands.
   * **Exact Buy Trigger:** **`<= $339.00`** (Route G `G5` `12%` return ceiling), OR **`<= $348.40`** (where PEG drops `<= 2.00` for `#14a` starter on `#9` alone).

8. **`KRYS` (`[NEW DISCOVERY]` Krystal Biotech — Lane 4):** **Route G / High-Velocity Near-Pass (Blocked by `A1` no buybacks with `+1.46%` shares & `#12` PT `+18.2% < 20%`).**
   * Price `~$331.80`, `PH-clear` (`+9.28%` vs 200DMA `$303.61`), 3Y Rev CAGR `31.96%`, 3Y EPS CAGR `24.60%`, Fwd P/E `40.84x` (passes High-Velocity `<= 45.0x`), PEG `0.93` (`<= 1.65`), TTM FCF `~$258M` (`2.63%` yield), Net Cash `~$750M`. Fails Core `A1` (`+1.46%` YoY shares without buybacks) and `#12` (PT `$392.11 = +18.2% < 20%`).
   * **Exact Buy Trigger:** **`<= $275.00`** (Route G `G5` `12%` return ceiling after 12m Form 4 verification; `#12` `+20%` PT leg clears at `<= $326.75`).

9. **`ADMA` (`[NEW DISCOVERY]` ADMA Biologics — Lane 4):** **Route G Near-Pass (`G-watch` on Mkt Cap `$2.44B` floor, `A1` `+1.15%` shares, `#9` `12.65%` 3Y Rev).**
   * Price `~$10.20`, Mkt Cap `~$2.44B` (borderline `$2.5B` floor), `PH-clear` (`-11.15%` vs 200DMA `$11.48`), Fwd P/E `14.5x`, PEG `0.65`, PT `$19.70` (`+93%`), 3Y Rev `12.65%`, 3Y EPS `22.26%`, TTM FCF `$116.47M` (`~22%` margin, `4.77%` yield), Net Cash. Fails Core `A1` (`+1.15%` shares without `>=25%` rev growth) and `#9` (`12.65% < 15%`).
   * **Exact Buy Trigger:** **`<= $9.50`** (`G5` ceiling once 12m Form 4s verified and market cap sustained `>= $2.5B`, or `#14a` starter if buybacks bring WASO `<= +0.5%`).

10. **`CVLT` (`[NEW DISCOVERY]` Commvault Systems — Lane 6):** **Route G Near-Pass (`G-watch` on Price vs. `G5` Ceiling; fails Core `#9` & `#12`).**
    * Price `~$152.00`, `PH-clear` (`+30.76%` vs 200DMA `$116.24`), WASO `-3.23%` YoY, TTM FCF `$258.45M` (`~25%` margin, Capex/OCF `2.35%`, `3.92%` yield), Net Cash `~$300M`, Fwd P/E `28.58x`, PEG `1.54`. Fails Core `#9` (3Y Rev `11.07% < 15%` and `< 12%` `#14a`), `#10` (3Y EPS `18.61% < 20%`), and `#12` (PT `$160.55 = +5.6% < 20%`, FCF yield `~4.2% < 5.0%`).
    * **Exact Buy Trigger:** **`<= $131.50`** (Route G `G5` `12%` return ceiling).

11. **`CRWD` (CrowdStrike — Lane 6 Seed):** **Route G Distant Watch (`G-watch` on extreme valuation; fails Core `A1`, `A2`, `#11`, `#12`, `G5`).**
    * Price `$436.32`, `PH-clear` (`-1.18%` vs 200DMA `$441.52`), 3Y Rev `20.53%`, 3Y EPS `23.2%`, TTM FCF `$1.30B` (`27.0%` margin, `1.21%` yield), Net Cash `-$4.62B`. Fails Core `A1`/`A2` (diluted WASO `+1.26%` YoY with negligible `0.09%` buybacks and `<25%` rev growth; SBC `21.5%` rev), `#11` (Fwd P/E `76.2x`, PEG `3.29`, FCF yield `1.21% < 1.5%`), `#12` (PT `+15.8% < 20%`), and `G5` (`-2.2%/yr` 5Y base return at `$436.32`).
    * **Exact Buy Trigger:** **`<= $265.24`** (`G5` `12.0%` base return ceiling at `25x` terminal P/FCF).

12. **`MDGL` (`[NEW DISCOVERY]` Madrigal Pharmaceuticals — Lane 4):** **Route H Watch (`H-watch` on `H4` 20% return hurdle).**
    * Price `~$499.00`, `PH-clear` (`-3.39%` vs 200DMA `$516.50`), Rezdiffra MASH commercial ramp (`~65%` 3Y rev CAGR), TTM FCF negative (`-$80M+`, fails `A3a`/`G2`), Shares `+11%` YoY (fails `A1`/`G3`). Passes `H1` (commercial drug) and `H2` (funded runway), but fails `H4` (`>= 20%/yr` 5Y base return after dilution) at `$499`.
    * **Exact Buy Trigger:** **`<= $397.00`** (`H4` `20%` annualized return ceiling once `H3`/`H5` documentation completed).

13. **`AVAV` (`[NEW DISCOVERY]` AeroVironment — Lane 5):** **Route H Distant Watch (Fails `A1` ESAero stock M&A `1.33% > 0.50%` & `A3a`/`G2` negative FCF `-$25.03M`; `H4` fails at `$120.60`).**
    * Price `$120.60`, `PH-clear` by age (`-70.57%` DD from Oct 2025 ATH `$409.83`, `-40.07%` below 200DMA `$201.24`). Diluted WASO `+6.27%` YoY (`+52.13%` total shares incl. BlueHalo; March 16, 2026 **ESAero acquisition issued 671,078 shares = `1.33–1.35%`**, exceeding Rev 5's `0.50%` bolt-on carve-out -> **fails `A1`**). Actual TTM Company FCF is **`-$25.03M`** (`-1.25%` margin; FY27E FCF `-$89.19M` -> **fails `A3a`/`G2`**). Under Route H, 5Y base return is only `8.5%/yr` (`< 20%`), plus two securities class actions and two material weaknesses.
    * **Exact Buy Trigger:** **`<= $72.88`** (conditional `H4` `20%` return ceiling, plus remediation of material weaknesses and class-action RPL).

---

### 3. Corporate Action / Delisted Exclusion Log
* **`CYBR` (`[NEW DISCOVERY]` CyberArk Software — Lane 6):** **ACQUIRED / DELISTED.** Palo Alto Networks (`PANW`) completed the acquisition of CyberArk on **February 11, 2026** (`$45.00` cash + `2.2005` `PANW` shares per `CYBR` share; `~$25B` EV). Logged as a completed corporate action exclusion (and the direct driver of `PANW`'s `+20.8%` YoY share count dilution failure under `A1`/`G3`).

---

## Master Quantitative Audit Table — Batch 2 (Lanes 4, 5, and 6)

| Ticker | Lane & Tag | Price / Mkt Cap | Price Health (`PH` / 200DMA / DD%) | 3Y Rev / Next-FY / 3Y EPS / Est. 3Y IRR | `A1` / `A2` / `G3` Dilution & SBC% | `A3` FCF Margin, `A3b` NTM>=TTM, `A3c` Capex/OCF | `A4` Net Debt / NTM FCF | `#11` Fwd P/E, PEG, FCF Yield & `#12` PT% | Policy Rev 5 Verdict & Exact Buy Trigger |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`LLY`** | L4 Seed | `$1,142.85` / `$1,018.7B` | **`PH-clear`** (`+6.4%` vs `$1,073.81`; `-10.7%` DD) | `20.5%` / `+35.8%` / `30.95%` / **`~26.5%` (PASS)** | **PASS** (WASO `-0.68%`; `$6.17B` buybacks; SBC `1.8%` rev; cash M&A) | **PASS** (TTM `22.83%`; NTM `$28.81B > $18.19B`; Capex/OCF `20.43%`) | **PASS** (`1.77x` base; `2.00–2.21x` max incl. CVRs/milestones) | **PASS `#11`** (P/E `27.41x`, PEG `1.27`, Yield `2.83%`); **FAIL `#12`** (PT `+16.27%`) | **TIER 1 BALLAST PASS NOW** (`#7` `0.355%` net, 0 disc officers). **Core Trigger: `<= $1,107.36`**. |
| **`NBIX`** | L4 `[NEW]` | `$143.18` / `$14.4B` | **`PH-clear`** (`-2.8%` vs `$147.26`; `-16.8%` DD) | `16.7%` / `+27.0%` / `40.9%` / **`~27.5%` (PASS)** | **FAIL `A1` & `G3` by 17bp** (WASO `+3.17%` vs `3.0%` Rev 5 `G3` cap; SBC `9.5%`) | **PASS** (TTM `$870.4M` = `25.8%`; NTM `129%` of TTM; Capex/OCF `3.08%`) | **PASS** (Net Cash `~0x` debt) | **PASS `#11` & `#12`** (P/E `12.66x`, PEG `0.31`, Yield `7.78%`, PT `+44.8%`) | **TIER 2 (`G-watch`)**: 17bp over Rev 5 `G3` (`3.0%`). **Trigger: WASO `<= +3.0%` on Oct 27 at `<= $175.00`**. |
| **`PODD`** | L4 `[NEW]` | `$131.69` / `$9.13B` | **`PH-clear`** (`-31.9%` vs `$193.38` **voids PT**; `-62.7%` DD, 1.06y) | `16.15%` / `+21.4%` / `23.06%` / **`~28.4%` (PASS)** | **PASS** (WASO `-1.77%` Q2; `$300M` ASR; 2026 converts cash-redeemed; SBC `3.8%`) | **PASS `A3`** (TTM `9.62%`; NTM `$439.5M > $293.7M` on `x1.25` capex; Capex/OCF `34%`) | **PASS** (`1.09x–1.36x` incl. `$97M` guarantee) | **PASS `#11`** (P/E `19.09x`, PEG `0.96`); **FAIL `#12`** (`4.81%` / `4.11%` fallback yield `<5%`, PT void) | **TIER 2 (`1-Step Watch`)**: `#7` net buying (`-0.018%`). **Trigger: `<= $126.76` (blended) / `<= $108.35` (full `x1.25`) or Nov 4 capex/GM guide**. |
| **`ARGX`** | L4 Seed | `$810.00` / `$48.5B` | **`PH-clear`** (`-4.9%` vs `$851.50`; `-16.1%` DD) | `30.39%` / `+34.0%` / `32.75%` / **`~28.5%` (PASS)** | **FAIL Core `A1`/`A2`** (WASO `+1.8%` w/ 0 buybacks; passes `G3 <=3%`; SBC `7.5%`) | **PASS Core `A3` / Wait `G2`** (TTM `$849M` = `19.5%`; needs FY26 2nd pos OCF yr for `G2`) | **PASS** (Net Cash `-$5.1B`) | **PASS `#11` & `#12`** (P/E `29.74x`, PEG `0.85`, Yield `1.90%`, PT `+42.2%`) | **TIER 2 (`G-watch`)**: Needs FY26 2nd pos OCF yr (Feb '27) + AFM insider sweep. **Trigger: `<= $785.00`**. |
| **`ISRG`** | L4 Seed | `$391.95` / `$139.5B` | **`PH-clear`** (`-12.4%` vs `$447.22`; `-35.8%` DD) | `14.11%` / `+14.5%` / `15.08%` / `~14.8%` (`<25%`) | **PASS** (WASO `-1.11%` YoY; active buybacks; SBC `6.2%` rev) | **PASS** (TTM `$3.22B` = `29.21%`; Capex/OCF `~22%`) | **PASS** (Net Cash `-$5.22B`) | **FAIL `#9` (`14.11%`) + `#11` (PEG `2.25 > 2.0`)** (P/E `34.69x`, Yield `2.6%`, PT `+24%`) | **TIER 2 (`G-watch`)**: Cannot combine two `#14a` shortfalls (`#9` + `#11`). **Trigger: `<= $339.00` (`G5`) or `<= $348.40` (PEG `<=2.0`)**. |
| **`REGN`** | L4 `[NEW]` | `$735.20` / `$79.5B` | **`PH-clear`** (`-0.1%` vs `$736.04`; `-38.8%` DD) | `11.36%` / `+18.6%` (FY27 `+8.7%`) / `15.69%` / `~17.5%` | **PASS** (WASO `-2.39%` YoY; `$3.90B` buybacks; SBC `~6%` rev) | **PASS** (TTM `$3.76B` = `24.21%`; NTM `$6.31B`; Capex/OCF `14.5%`) | **PASS** (Net Cash `-$14.85B`; `-$6.35B` at max milestones) | **FAIL `#9` (`11.36%`) & `#10`**; **PASS `#11` & `#12`** (P/E `12.02x`, PEG `1.00`, Yield `8.59%`) | **TIER 2 (`G-watch`)**: Price above `G5` ceiling (`8.1%` base return at `$735`). **Trigger: `<= $617.00`**. |
| **`KRYS`** | L4 `[NEW]` | `$331.80` / `$9.82B` | **`PH-clear`** (`+9.3%` vs `$303.61`; `-7.8%` DD) | `31.96%` / `+33.0%` / `24.60%` / `~22.5%` | **FAIL Core `A1`/`A2`** (Shares `+1.46%` w/ 0 buybacks; passes `G3`; SBC `11%`) | **PASS** (TTM `~$258M` = `~34%` margin; Capex/OCF `<8%`) | **PASS** (Net Cash `~$750M`) | **PASS HV `#11`** (P/E `40.84x <=45`, PEG `0.93 <=1.65`, Yield `2.63%`); **FAIL `#12`** (PT `+18.2%`) | **TIER 2 (`G-watch`)**: Fails Core `A1` & `#12`. **Trigger: `<= $275.00` (`G5` ceiling; `#12` clears at `<= $326.75`)**. |
| **`ADMA`** | L4 `[NEW]` | `$10.20` / `$2.44B` | **`PH-clear`** (`-11.2%` vs `$11.48`; `-56.9%` DD) | `12.65%` / `+16.0%` / `22.26%` / `~21.0%` | **FAIL Core `A1`** (Shares `+1.15%` YoY w/ `<25%` rev growth; passes `G3`) | **PASS** (TTM `$116.5M` = `~22%` margin; Capex/OCF `14.8%`) | **PASS** (Net Cash) | **FAIL Core `#9` (`12.65%`)**; **PASS `#11` & `#12`** (P/E `14.5x`, PEG `0.65`, Yield `4.77%`, PT `+93%`) | **TIER 2 (`G-watch`)**: Sub-`$2.5B` cap (`$2.44B`) & `A1`/`#9`. **Trigger: `<= $9.50` (`G5` w/ Mkt Cap `>=$2.5B`)**. |
| **`MDGL`** | L4 `[NEW]` | `$499.00` / `$11.1B` | **`PH-clear`** (`-3.4%` vs `$516.50`; `-16.1%` DD) | `~65.0%` / `+55.0%` / N/A / `~17.0%` | **FAIL `A1` & `G3`** (Shares `+11.0%` YoY from equity/warrants; SBC `~16%`) | **FAIL `A3a` & `G2`** (TTM FCF negative `-$80M+` during Rezdiffra launch) | **PASS `H2`** (Net Cash runway `>24m` buffered) | **FAIL `#11`** (Fwd P/E `51.89x`, PEG N/A, FCF negative) | **TIER 2 (`H-watch`)**: Evaluated under Route H; fails `H4` `20%` return at `$499`. **Trigger: `<= $397.00`**. |
| **`VRTX`** | L4 Seed | `$496.50` / `$125.8B` | **`PH-clear`** (`+4.5%` vs `$475.25`; `-4.5%` DD) | `11.11%` / `+9.8%` / `8.50%` / `~11.0%` (`<25%`) | **PASS** (WASO `-0.85%` YoY; active buybacks; `$4.9B` Alpine cash M&A) | **PASS** (TTM FCF `~$3.88B` = `~33%` margin; Capex/OCF `~8%`) | **PASS** (Net Cash `-$6.1B`) | **FAIL `#9` (`11.11%`), `#11` (PEG `2.68 > 2.50`), & `#12`** (PT `+15.1%`, Yield `3.09%`) | **TIER 3 HARD FAIL** (`#9` 3Y rev `11.11%`, `#10` EPS `8.50%`, `#11` PEG `2.68`, `#12` PT `+15.1%`). |
| **`TMDX`** | L4 `[NEW]` | `$77.50` / `$2.66B` | **`PH-clear`** (`-21.2%` vs `$98.38` **voids PT**; `-56.3%` DD, 2.1y) | `18.81%` / `+22.0%` / `8.31%` / `~16.5%` (`<25%`) | **FAIL `A1` & `A2`** (Shares `+1.53%` YoY w/ 0 buybacks & net debt; SBC `~7%`) | **FAIL `A3b`/`A3c`** (Aviation jet fleet capex spikes `>45–55%` OCF; NTM FCF `<` TTM) | **PASS** (`~1.5x` FCF) | **FAIL `#11` (PEG `>2.5`) & `#12`** (PT `+28.7%` **VOID** `>20%` below 200DMA; Yield `~2.5% <5%`) | **TIER 3 HARD FAIL** (`A1`, `A2`, `A3b`/`A3c` jet fleet capex, `#11` PEG, `#12` PT void + low FCF yield). |
| **`LNTH`** | L4 `[NEW]` | `$100.02` / `$6.54B` | **`PH-clear`** (`+13.8%` vs `$87.88`; `-21.2%` DD) | `~3.5%` / `+2.0%` / `~6.5%` / `~8.5%` (`<25%`) | **PASS** (Buybacks active; share count stable `~65.3M`) | **PASS** (TTM FCF `$387.8M` = `24.5%` margin; Yield `5.93%`) | **PASS** (Net Cash) | **FAIL `#9`, `#10`, & `G2`** (3Y rev `~3.5% < 10%`); P/E `14.27x`, PEG `1.80`, PT `+7.3%` | **TIER 3 HARD FAIL** (`#9`, `#10`, & `G2` 3Y revenue growth `~3.5% < 10%` floor as Pylarify matures). |
| **`HALO`** | L4 `[NEW]` | `$105.00` / `$11.9B` | **`PH-clear`** (`+31.1%` vs `$80.08`; `-6.3%` DD) | `18.21%` / `+19.0%` / `42.12%` / `~24.0%` | **FAIL `A1`** (Convertible senior notes outstanding; Shares `-4.21%` via buybacks) | **PASS** (TTM FCF `$806.2M` = `~62%` margin; Capex/OCF `1.5%`) | **PASS** (`~1.3x` FCF) | **PASS `#11` & `#12`** (P/E `19.5x`, PEG `0.46`, Yield `7.2%`, PT `+3.6%`) | **TIER 3 HARD FAIL** (`A1` convertible notes, `A7` insider selling, & `G5` ENHANZE 2028–30 patent cliff). |
| **`EXEL`** | L4 `[NEW]` | `$53.50` / `$13.26B` | **`PH-clear`** (`+8.0%` vs `$49.53`; `-8.5%` DD) | `12.59%` / `+11.5%` / `18.02%` / `~18.5%` (`<25%`) | **PASS `A1`/`A2`** (Shares `-4.5%` YoY via buybacks; 247.8M sh) | **PASS** (EV/FCF `11.73x` = `~8.5%` FCF yield; Capex/OCF `<5%`) | **PASS** (Net Cash) | **FAIL `#9` (`12.59%`) & `#10` (`18.02% <20%`)**; P/E `17.08x`, PEG `0.95`, PT `+2.6%` | **TIER 3 HARD FAIL** (`#7`/`A7` insider selling `>0.5%`, `#9` 3Y rev `<15%`, Cabometyx 2030 patent cliff). |
| **`AXSM`** | L4 `[NEW]` | `$165.00` / `$8.64B` | **`PH-clear`** (`-17.7%` vs `$200.36`; `-26.7%` DD) | `~36.0%` / `+38.0%` / N/A / `<20%` | **FAIL `A1` & `G3`** (Shares `+4.44%` YoY > `3.0%` `G3` cap; SBC `~18%` rev) | **FAIL `A3a` & `G2`** (TTM FCF negative `-$95M`) | **PASS** (`~0x` net debt) | **FAIL `#11`** (Fwd P/E `798.22x > 45x`, PEG N/A, FCF negative) | **TIER 3 HARD FAIL** (`A1`/`G3` `+4.44%` share dilution, `A3a`/`G2` negative FCF, `#11` P/E `798x`). |
| **`MIRM`** | L4 `[NEW]` | `$82.00` / `$5.32B` | **`PH-clear`** (`-17.8%` vs `$99.70`; `-36.9%` DD) | `~26.0%` / `+28.0%` / N/A / `<20%` | **FAIL `A1` & `G3`** (Shares `+8.5%` YoY from converts & equity raises) | **FAIL `A3a` & `G2`** (TTM FCF margin `< 6.0%` floor) | **FAIL `A4`** (Convert debt vs minimal FCF) | **FAIL `#11`** (P/E negative/N/A, PEG N/A); PT `$147.80` (`+80%`) | **TIER 3 HARD FAIL** (`A1`/`G3` `+8.5%` convert/equity dilution, `A3a`/`G2` FCF `<6%`, `#11`). |
| **`DXCM`** | L4 `[NEW]` | `$83.60` / `$31.5B` | **`PH-impaired`** (`+13.7%` vs `$73.51`; `-49.0%` DD, 4.9y, 3Y gap `<-80pp`) | `11.49%` / `+11.0%` / `20.72%` / `~14.5%` (`<25%`) | **PASS `A2`** (Shares `-2.61%` YoY; convert retirement) | **FAIL `A3b`** (NTM FCF `<` TTM FCF `$1.41B`) | **PASS** (Net Cash) | **FAIL `#9` (`11.49%`), `#10` (PEG `1.43 >=1.0`), & `#12`** (PT `+15.4%`, Yield `4.48% <5%`) | **TIER 3 HARD FAIL** (`PH-impaired` Hard Exclude, `A3b` FCF decline, `#9` rev `11.49%`, `#12`). |
| **`BSX`** | L4 `[NEW]` | `$43.20` / `$63.8B` | **`PH-clear`** (`-28.5%` vs `$60.41` **voids PT**; `-52.5%` DD) | `5.53%` / `+6.5%` / `6.74%` / `~10.0%` (`<25%`) | **FAIL `A1`** (Pending **Penumbra deal ~27% stock consideration**) | **PASS** (TTM FCF `$3.63B` = `17.3%` margin; Capex/OCF `20.0%`) | **FAIL `A4`** (Post-Penumbra pro forma `>2.5x`) | **FAIL `#9`, `#10`, `G2`** (`5.53%` rev); P/E `13.34x`, PEG `0.72`, PT `+37.5%` (void) | **TIER 3 HARD FAIL** (`A1` Penumbra ~27% stock deal, `#9`/`G2` 3Y rev `5.53% < 10%`, `A4`). |
| **`PRCT`** | L4 `[NEW]` | `$19.20` / **`$1.10B (<$2.5B)`** | **`PH-clear`** (`-12.7%` vs `$22.00`; `-81.2%` DD) | `~32.0%` / `+30.0%` / N/A / `<15%` | **FAIL `A1` & `G3`** (Shares `+9.0%` YoY equity raise) | **FAIL `A3a` & `G2`** (TTM FCF `-$75M`) | **PASS `H2`** (Net Cash) | **FAIL `#11` & `H4`** (P/E N/A, FCF negative, `H4` `<20%` return) | **TIER 3 HARD FAIL** (Market Cap `$1.10B < $2.5B` floor, `A1`, `A3a`/`G2` negative FCF, `H4` fail). |
| **`ALNY`** | L4 `[NEW]` | `$228.50` / `$30.6B` | **`PH-clear`** (`-24.1%` vs `$301.18` **voids PT**; `-50.9%` DD) | `30.72%` / `+32.0%` / `43.69%` / `~26.0%` | **FAIL `A1`** (Shares `+2.4%` YoY + convertible notes; SBC `14%` rev) | **PASS `A3a`** (TTM FCF `~$837M` = `2.74%` yield) | **PASS** (`~0.5x` FCF) | **FAIL `#12` & `#19` BLACKOUT** (PT `+62.2%` **VOID** at `-24.1%` vs 200DMA; Yield `2.74% <5%`) | **TIER 3 HARD FAIL** (`#19` Earnings Blackout, `A1` convert/share dilution, `#12` PT void + low FCF yield). |
| **`IDXX`** | L4 `[NEW]` | `$541.80` / `$42.7B` | **`PH-clear`** (`-7.1%` vs `$583.41`; `-14.0%` DD) | `~8.8%` / `+9.73%` / `~12.5%` / `~11.5%` (`<25%`) | **PASS** (Shares `-1.5%` YoY via buybacks) | **PASS** (TTM FCF `$1.31B` = `~31%` margin; Yield `3.07%`) | **PASS** (`~0.5x` FCF) | **FAIL `#9`/`G2` (`8.8% <10%`) & `#11` (PEG `2.39 >2.0`)**; P/E `33.09x`, PT `+29.5%` | **TIER 3 HARD FAIL** (`#9`, `#10`, & `G2` 3Y rev `8.8% < 10%` floor + `#11` PEG `2.39 > 2.0`). |
| **`RMD`** | L4 `[NEW]` | `$218.89` / `$32.1B` | **`PH-warning`** (`-3.0%` vs `$225.71`; `-26.4%` DD, 5.07y, 3Y gap `-32.6pp`) | `5.30%` / `+2.7%` / `8.98%` / `~9.5%` (`<25%`) | **PASS** (Shares `-0.87%` YoY; `#7` `0.07%` net selling) | **PASS** (TTM FCF `$1.65B` = `29.18%` margin; NTM `+1.8%` blend) | **PASS** (Net Cash `-$643M`) | **FAIL `#9`, `#10`, & `G2`** (`5.30%` 3Y rev `<10%`); P/E `18.11x`, PEG `1.38`, Yield `5.33%` | **TIER 3 HARD FAIL** (`#9`, `#10`, & `G2` 3Y rev `5.30% < 10%` & FY27 `+2.7%`; `PH-impaired` at `<=$208.15`). |
| **`KOG.OL`** | L5 `[NEW]` | `NOK 308.00` / `~$25.5B` | **`PH-clear`** (`+4.4%` vs `NOK 295` adj for `KMAR` demerger) | `~22.5%` / `+36.4%` / `~34.8%` / **`~26.5%` (PASS)** | **PASS** (Shares flat YoY; `#7` **verified clean on Oslo Newsweb**) | **PASS** (TTM FCF `NOK 6.03B`, NTM `NOK 9.90B`; Capex/OCF `~24%`) | **PASS** (Net Cash) | **PASS `#11` & `#12`** (P/E `33.41x <=38`, PEG `0.96`, PT `+28.5%`); **FAIL `#19` BLACKOUT** | **TIER 2 (`#19` Blackout Watch)**: Q2 rev `-3.4%`/EBITDA `-8.8%` miss. **Trigger: Clean Oct 29 print at `<= NOK 350.30`**. |
| **`AXON`** | L5 Seed | `$413.35` / `$33.5B` | **`PH-clear`** (`-16.8%` vs `$496.96`; `-52.5%` DD, 1.15y) | `30.71%` / `+28.0%` / `26.6%` / `~21.5%` | **FAIL `A1` & `G3`** (WASO `+3.1%` YoY; SBC `18.5%` rev / `>250%` FCF + M&A stock/converts) | **FAIL `A3a` & `G2`** (TTM Company FCF `$133.19M` = **`4.14%` margin `< 6.0%` floor!**) | **FAIL `A4`/`G2`** (Net Debt `$1.16B` = `8.7x` TTM FCF) | **FAIL `#11`** (Fwd P/E `45.56x > 45.0x` HV cap, PEG `1.71 > 1.65`, Yield `0.39% < 1.15%`); PT `+67.1%` | **TIER 3 HARD FAIL** (`A3a`/`G2` TTM FCF margin `4.14% < 6.0%` floor, `A1`/`G3` SBC & convert dilution, `A4`, `#11`). |
| **`RHM.DE`** | L5 Seed | `€956.00` / `~€41.8B` | **`PH-clear`** (`-26.2%` vs `€1,295` **voids PT**; `-50.7%` DD) | `~32.0%` / `+38.0%` / `~42.0%` / **`~31.0%`** | **FAIL `A1`** (WASO `+1.08%` from Loc Performance / convert; passes `G3`) | **FAIL `A3a`, `A3c`, & `G2`** (TTM FCF **`3.4–3.8%` margin `< 6.0%`**; H1 FCF `-€1.616B`; Capex `>55%` OCF) | **FAIL `A4`** (`>2.5x` on depressed FCF) | **PASS `#11`** (P/E `21.5x`, PEG `0.38`); **FAIL `#12`** (PT `+64.3%` **VOID** at `-26.2%` vs 200DMA; Yield `<2%`) | **TIER 3 HARD FAIL** (`A3a`/`G2` TTM FCF margin `3.4–3.8% < 6.0%` & H1 FCF `-€1.62B`, `A3c` capex `>50%`, `#12` PT void). |
| **`MSI`** | L5 `[NEW]` | `$442.00` / `$73.8B` | **`PH-clear`** (`+2.1%` vs `$432.97`; `-13.0%` DD) | `9.08%` / `+8.5%` / `12.34%` / `~11.5%` (`<25%`) | **PASS** (Shares `-1.2%` YoY via buybacks; SBC `~3.5%` rev) | **PASS** (TTM FCF `$2.40B` = `19.6%` margin; Capex/OCF `~11%`) | **FAIL `A4`** (Net Debt `$6.1B` = `2.54x > 2.5x` FCF) | **FAIL `#9`/`G2` (`9.08% <10%`), `#10`, & `#11` (PEG `2.31 >2.0`)**; P/E `28.5x`, PT `+21.0%` | **TIER 3 HARD FAIL** (`#9`/`#10`/`G2` 3Y rev `9.08% < 10%` floor, `A4` Net Debt/FCF `2.54x`, `#11` PEG `2.31`). |
| **`KTOS`** | L5 `[NEW]` | `$43.07` / `$6.55B` | **`PH-warning`** (`-37.5%` vs `$68.95` **voids PT**; `-97.3%` DD, 3Y `+98.5pp`) | `~19.5%` / `+20.5%` / `~32.0%` / `~14.5%` (`<25%`) | **FAIL `A1` & `G3`** (Shares **`+15.14%` YoY** from **`$1.0B` Mar 2026 equity offering**) | **FAIL `A3a` & `G2`** (Q2 FCF `-$28.2M`; FY26E FCF **`-$93.46M`**) | **PASS** (Post-raise Net Cash) | **FAIL `#11` & `#12`** (Fwd P/E `39.15x > 38x`, FCF negative, PT leg void at `-37.5%` vs 200DMA) | **TIER 3 HARD FAIL** (`A1`/`G3` `$1.0B` equity raise `+15.14%` dilution, `A3a`/`G2` negative FCF `-$93.5M`). |
| **`AVAV`** | L5 `[NEW]` | `$120.60` / `$6.05B` | **`PH-clear`** (`-40.1%` vs `$201.24` **voids PT**; `-70.6%` DD, 1.0y) | `~16.5%` / `+18.0%` / `~24.0%` / `~8.5%` (`<25%`) | **FAIL `A1` & `G3`** (WASO `+6.27%`; **ESAero stock deal `1.33% > 0.50%` Rev 5 cap**) | **FAIL `A3a` & `G2`** (TTM Company FCF **`-$25.03M` = `-1.25%` margin**; FY27E `-$89.2M`) | **FAIL `A4`** (Net Debt `$149.8M` vs neg FCF) | **FAIL `#11`, `#12`, & `H4`** (`H4` 5Y return `8.5% < 20%`; 2 material weaknesses & class actions) | **TIER 2/3 (`H-watch` / Core Hard Fail)**: Fails `A1`, `A3a`/`G2`, & `H4` (`8.5%`). **Conditional `H4` Trigger: `<= $72.88`**. |
| **`DRS`** | L5 `[NEW]` | `$36.50` / `$9.74B` | **`PH-clear`** (`-13.7%` vs `$42.28`; `-27.9%` DD) | `~8.5%` / `+8.0%` / `~13.5%` / `~13.0%` (`<25%`) | **FAIL `A1`/`A2`** (Shares `+1.1%` YoY w/ 0 buybacks) | **PASS** (TTM FCF `$363M` = `10.5%` margin; Capex/OCF `27.5%`) | **PASS** (Net Cash `~$250M`) | **FAIL `#9`/`G2` (`8.5% <10%`) & `#11` (PEG `3.07 >2.50`)**; P/E `26.43x`, PT `+46.4%` | **TIER 3 HARD FAIL** (`A1`/`A2`, `#9`/`#10`/`G2` 3Y rev `8.5% < 10%`, `#11` PEG `3.07 > 2.50`). |
| **`SAAB-B.ST`** | L5 `[NEW]` | `SEK 608.10` / `~$31.5B` | **`PH-clear`** (`+0.02%` vs `SEK 608.00`; `-18.8%` DD) | `~18.5%` / `+22.0%` / `~22.8%` / `~14.5%` (`<25%`) | **PASS** (Shares `+0.3%` YoY; `#7` Swedish PDMR unverified) | **PASS** (TTM FCF `~SEK 7.25B` = `2.21%` yield; Capex/OCF `~38%`) | **PASS** (Net Cash) | **PASS `#11`** (P/E `35.21x`, PEG `1.54`); **FAIL `#12` & `G5`** (PT `+4.76% <20%`, Yield `2.21% <5%`) | **TIER 3 HARD FAIL** (`#12` PT `+4.76% < 20%` & FCF yield `2.21% < 5.0%`, `G5` valuation fail). |
| **`BAESY`** | L5 `[NEW]` | `2,015p` (`$105`) / `~$79B` | **`PH-clear`** (`-0.5%` vs `2,025.9p`; `-6.3%` DD) | `~8.8%` / `+9.0%` / `~11.5%` / `~12.0%` (`<25%`) | **PASS** (Shares `-1.5%` YoY via buybacks; UK PDMR unverified) | **FAIL `A3b`** (NTM FCF `<` customer advance-inflated TTM FCF `£4.70B`) | **PASS** (`~1.4x` FCF) | **FAIL `#9`/`#10`/`G2` (`8.8% <10%`) & `#12`** (PT `+15.3% <20%`, NTM Yield `<5%`); P/E `20.63x` | **TIER 3 HARD FAIL** (`A3b` NTM FCF `<` advance-funded TTM FCF, `#9`/`G2` 3Y rev `8.8% < 10%`, `#12`). |
| **`LDOS`** | L5 `[NEW]` | `$118.50` / `$15.31B` | **`PH-clear`** (`-18.1%` vs `$144.61`; `-41.6%` DD) | `5.17%` / `+5.5%` / `4.42%` / `~9.5%` (`<25%`) | **PASS** (Shares `-3.02%` YoY via buybacks) | **FAIL `A3b`** (NTM FCF `<` TTM FCF) | **PASS** (`~1.8x` FCF) | **FAIL `#9`, `#10`, & `G2`** (3Y rev `5.17% <10%`, EPS `4.42% <20%`); P/E `9.89x`, PEG `1.82` | **TIER 3 HARD FAIL** (`A3b` FCF decline, `#9`/`#10`/`G2` 3Y rev `5.17% < 10%` & EPS `4.42%`). |
| **`ESLT`** | L5 `[NEW]` | `$701.50` / `$31.3B` | **`PH-clear`** (`-9.3%` vs `$773.74`; `-13.9%` DD) | `12.19%` / `+13.0%` / `~16.5%` / `~14.0%` (`<25%`) | **FAIL `A1`/`A2`** (Shares `>+0.5%` YoY w/ 0 buybacks; TASE unverified) | **PASS** (Debt/FCF `1.25x`; Yield `~2.2%`) | **PASS** (Net Cash `-$110.7M`) | **FAIL `#9` (`12.19%`), `#11` (P/E `38.15x >38.0x`), & `#12`** (PT `+14.2% <20%`, Yield `2.2% <5%`) | **TIER 3 HARD FAIL** (`A1`, `#9` 3Y rev `12.19%`, `#11` P/E `38.15x`, `#12` PT `+14.2%` & Yield `2.2%`). |
| **`LHX`** | L5 `[NEW]` | `$236.60` / `$44.26B` | **`PH-clear`** (`-23.8%` vs `$310.60` **voids PT**; `-37.5%` DD) | `7.51%` / `+7.0%` / `~10.8%` / `~12.5%` (`<25%`) | **PASS** (Buybacks active; 186.2M sh) | **PASS** (TTM FCF `~$2.81B` = `~13%` margin) | **FAIL `A4`** (Net Debt `~$11.5B` = **`~3.6x > 2.5x`**) | **FAIL `#9`, `#10`, & `G2`** (`7.51%` rev `<10%`); P/E `18.53x`, PEG `1.14`, PT `+35.6%` (void) | **TIER 3 HARD FAIL** (`A4` Net Debt/FCF `~3.6x > 2.5x`, `#9`/`#10`/`G2` 3Y rev `7.51% < 10%`). |
| **`NOC`** | L5 `[NEW]` | `$478.00` / `$67.9B` | **`PH-clear`** (`-20.1%` vs `$598.33` **voids PT**; `-37.8%` DD) | `5.93%` / `+5.8%` / `~6.2%` / `~10.5%` (`<25%`) | **PASS** (Buybacks active; 142.1M sh) | **PASS** (TTM FCF `~$3.62B` = `5.33%` yield) | **FAIL `A4`** (Net Debt `~$14.2B` = **`~3.5x > 2.5x`**) | **FAIL `#9`/`G2` (`5.93% <10%`) & `#11` (PEG `2.64 >2.50`)**; P/E `16.46x`, PT `+29.5%` (void) | **TIER 3 HARD FAIL** (`A4` Net Debt/FCF `~3.5x > 2.5x`, `#9`/`#10`/`G2` 3Y rev `5.93%`, `#11` PEG `2.64`). |
| **`GD`** | L5 `[NEW]` | `$330.09` / `$89.3B` | **`PH-clear`** (`-7.1%` vs `$355.21`; `-16.6%` DD) | `5.21%` / `+5.5%` / `~9.5%` / `~11.0%` (`<25%`) | **FAIL `A1`** (Diluted WASO `+0.95%` YoY `> +0.5%` cap) | **FAIL `A3b`** (NTM FCF `<` TTM FCF) | **PASS** (`~1.7x` FCF) | **FAIL `#9`, `#10`, & `G2`** (3Y rev `5.21% < 10%`); P/E `18.5x`, PEG `1.53–2.87`, PT `+25.0%` | **TIER 3 HARD FAIL** (`A1` WASO `+0.95%`, `A3b` FCF decline, `#9`/`#10`/`G2` 3Y rev `5.21% < 10%`). |
| **`LMT`** | L5 `[NEW]` | `$505.41` / `$119.5B` | **`PH-clear`** (`-10.2%` vs `$562.89`; `-25.3%` DD) | `6.38%` / `+7.9%` (FY27 `+5.6%`) / `~8.5%` / `~10.8%` | **FAIL `A2`** (2026 buybacks paused under Jan 7 EO) | **FAIL `A3b`** (Blended NTM FCF `$6.71B <` TTM `$8.73B`; GM `11.8%`) | **FAIL `A4`** (Pro forma `$20.20B` incl. `$3.45B` Ultra Maritime = **`3.01x > 2.5x`**) | **FAIL `#9`, `#10`, & `G2`** (3Y rev `6.38% < 10%`); P/E `16.9x`, PEG `0.88`, PT `+22.8%` | **TIER 3 HARD FAIL** (`A3b` NTM FCF `<` TTM, `A4` pro forma `3.01x > 2.5x`, `A2` buybacks paused, `#9`/`G2`). |
| **`TYL`** | L5 `[NEW]` | `$335.00` / `$14.3B` | **`PH-clear`** (`-2.3%` vs `$343.02`; `-47.2%` DD) | `9.37%` / `+9.8%` / `15.21%` / `~12.5%` (`<25%`) | **PASS** (Shares `-2.58%` YoY after 2026 convert settlement) | **PASS** (TTM FCF `~$610M` = `~26%` margin; Yield `4.26%`) | **PASS** (Net Cash) | **FAIL `#9`/`G2` (`9.37% <10%`), `#10` (`15.21% <20%`), & `#11` (PEG `~2.15 >2.0`)** | **TIER 3 HARD FAIL** (`#9`, `#10`, & `G2` 3Y rev `9.37% < 10%` floor & EPS `15.21% < 20%`). |
| **`FTNT`** | L6 Seed | `$80.19` / `$60.1B` | **`PH-clear`** (`-1.7%` vs `$81.61`; `-30.01%` DD) | `10.67%` / `+11.5%` / `10.71%` / `~12.8%` (`<25%`) | **PASS** (WASO `-3.85%` YoY; `$2.24B` H1 buybacks; SBC `4.2%` rev) | **PASS** (TTM FCF `$2.43B` = `35.8%` margin; Capex/OCF `11%`) | **PASS** (Net Cash `-$1.18B`) | **FAIL `#9` (`10.67%`), `#10`, `#11` (PEG `2.34`), & `#12`** (PT `+11.8%`, Yield `~4.3% <5%`) | **TIER 2 (`G-watch`)**: Passes `G1–G4` (`#7` `0.145%`); fails `G5` (`8.98%` base return at `$80.19`). **Trigger: `<= $72.24`**. |
| **`CVLT`** | L6 `[NEW]` | `$152.00` / `$6.6B` | **`PH-clear`** (`+30.8%` vs `$116.24`; `-22.1%` DD) | `11.07%` / `+12.0%` / `18.61%` / `~15.5%` (`<25%`) | **PASS** (Shares `-3.23%` YoY via buybacks; SBC `12%` rev) | **PASS** (TTM FCF `$258.5M` = `~25%` margin; Capex/OCF `2.35%`) | **PASS** (Net Cash `~$300M`) | **FAIL `#9` (`11.07%`), `#10` (`18.61%`), & `#12`** (PT `+5.6% <20%`, Yield `~4.2% <5%`); P/E `28.58x` | **TIER 2 (`G-watch`)**: Passes `G1–G3`; price above `G5` ceiling (`9.2%` base return). **Trigger: `<= $131.50`**. |
| **`CRWD`** | L6 Seed | `$436.32` / `$107.8B` | **`PH-clear`** (`-1.2%` vs `$441.52`; `-22.6%` DD) | `20.53%` / `+21.0%` / `23.2%` / `~15.8%` (`<25%`) | **FAIL Core `A1`/`A2`** (WASO `+1.26%` YoY w/ `0.09%` buybacks & `<25%` rev; SBC `21.5%`) | **PASS** (TTM FCF `$1.30B` = `27.0%` margin; Capex/OCF `11%`) | **PASS** (Net Cash `-$4.62B`) | **FAIL `#11` (P/E `76.2x`, PEG `3.29`, Yield `1.21% <1.5%`), `#12` (PT `+15.8%`), & `G5`** | **TIER 2/3 (`G-watch`)**: Fails Core `A1`, `#11`, `#12`, & `G5` (`-2.2%/yr` base return). **Trigger: `<= $265.24`**. |
| **`PANW`** | L6 Seed | `$176.21` / `$146.9B` | **`PH-clear`** (`+1.6%` vs `$173.44`; `-20.6%` DD) | `16.01%` / `+14%` org / `15.7%` / `~13.5%` (`<25%`) | **FAIL `A1` & `G3`** (Shares **`+20.8%` YoY** from **CyberArk stock deal** + Chronosphere) | **PASS** (TTM FCF `$4.13B` = `37.5%` margin; Capex/OCF `5%`) | **PASS** (Net Cash `-$1.9B`) | **FAIL `#11` (P/E `41.9x >38x`, PEG `2.67 >2.50`), `#12` (PT `+18.3%`, Yield `2.81%`), & `G5`** | **TIER 3 HARD FAIL** (`A1`/`G3` `+20.8%` CyberArk M&A share dilution, `#11` P/E `41.9x` & PEG `2.67`, `#12`, `G5` `$117.13`). |
| **`ZS`** | L6 Seed | `$145.65` / `$22.8B` | **`PH-impaired`** (`-32.0%` vs `$214.07` **voids PT**; `-60.5%` DD, 4.87y, 3Y `-91.8pp`) | `18.89%` / `+19.8%` / `21.0%` / `~19.5%` (`<25%`) | **FAIL `A1` & `A2`** (**`$1.725B` Jul 2025 convert issuance** + WASO `+1.26%` w/ 0 buybacks; SBC `22%`) | **PASS** (TTM FCF `$910.5M` = `27.8%` margin; FY27E `$1.08B` = `4.74%` yield) | **PASS** (Net Cash `-$1.88B`) | **PASS `#11`** (P/E `28.06x`, PEG `1.34`); **FAIL `#12`** (PT `+58.7%` **VOID** `>20%` below 200DMA; Yield `4.74% <5%`) | **TIER 3 HARD FAIL** (`PH-impaired` Hard Exclude, `A1` `$1.725B` July 2025 convert issuance, `#12` PT void). |
| **`CYBR`** | L6 `[NEW]` | **DELISTED** (Acq. by `PANW`) | **N/A** (Closed Feb 11, 2026) | N/A | N/A (`$45` cash + `2.2005` `PANW` sh per `CYBR` sh) | N/A | N/A | N/A | **CORPORATE ACTION EXCLUSION** (Acquired by `PANW` on Feb 11, 2026; no longer standalone). |
| **`NET`** | L6 `[NEW]` | `$260.00` / `$92.5B` | **`PH-clear`** (`+10.6%` vs `$235.00`; `-11.9%` DD) | `29.71%` / `+28.0%` / `34.95%` / `~14.0%` (`<25%`) | **FAIL `A1` & `A2`** (Shares `+2.02%` YoY w/ 0 buybacks + converts; SBC `24%`) | **PASS** (TTM FCF `~$274M` = `11.5%` margin) | **PASS** (Net Cash) | **FAIL `#11` (P/E `219.45x`, PEG `4.41`, Yield `0.30% <1.15%`) & `#12` (PT `+9.6% <20%`)** | **TIER 3 HARD FAIL** (`A1`/`A2` dilution/converts, `#11` P/E `219.5x`, PEG `4.41`, Yield `0.30%`, `#12`). |
| **`OKTA`** | L6 `[NEW]` | `$75.49` / `$13.2B` | **`PH-impaired`** (`-10.9%` vs `$84.74`; `-74.1%` DD, 5.64y, 3Y `-100.4pp`) | `8.63%` / `+9.0%` / `11.48%` / `~11.5%` (`<25%`) | **FAIL Core `A1`** (Shares `+2.90%` YoY; SBC `~20%` rev) | **PASS** (TTM FCF `$906M` = `30.5%` margin; Yield `6.97%`) | **PASS** (Net Cash `-$2.17B`) | **FAIL `#9`, `#10`, & `G2`** (3Y rev `8.63% < 10%`); P/E `20.13x`, PEG `1.88`, PT `+41.9%` | **TIER 3 HARD FAIL** (`PH-impaired` Hard Exclude, `A1` `+2.90%` dilution, `#9`/`#10`/`G2` 3Y rev `8.63% < 10%`). |
| **`S`** | L6 `[NEW]` | `$21.50` / `$7.1B` | **`PH-impaired`** (`+26.3%` vs `$17.02`; `-71.8%` DD, 4.9y, 3Y gap `<-80pp`) | `18.35%` / `+20.0%` / `46.67%` / `~18.5%` (`<25%`) | **FAIL `A1` & `G3`** (Shares **`+3.28%` YoY > `3.0%` `G3`**; SBC `24%` rev) | **FAIL `A3a` & `G2`** (TTM FCF `~$46M` on `$1.10B` rev = **`4.18%` margin `< 6.0%`**) | **PASS** (Net Cash `-$655.3M`) | **FAIL `#11` (P/E `63.2x >45x`, Yield `0.65% <1.15%`) & `#12` (PT `+13.9% <20%`)**; PEG `0.71` | **TIER 3 HARD FAIL** (`PH-impaired`, `A1`/`G3` `+3.28%` dilution, `A3a`/`G2` FCF margin `4.18% < 6%`, `#11`, `#12`). |
| **`CHKP`** | L6 `[NEW]` | `$159.40` / `$17.2B` | **`PH-clear`** (`-10.5%` vs `$178.00`; `-31.7%` DD) | `5.91%` / `+6.2%` / `9.15%` / `~10.5%` (`<25%`) | **FAIL `A1`** (**Issued `$1.75B` 0% 2030 convertible notes in H1 2026**; Shares `-1.24%`) | **PASS** (TTM FCF `$1.16B` = `42.5%` margin; Yield `6.69%`) | **PASS** (Net Cash `~$2.9B`) | **FAIL `#9`, `#10`, & `G2`** (3Y rev `5.91% < 10%`, EPS `9.15% < 20%`); P/E `15.14x`, PEG `1.80` | **TIER 3 HARD FAIL** (`A1` `$1.75B` H1 2026 convert issuance, `#9`/`#10`/`G2` 3Y rev `5.91% < 10%`). |
| **`QLYS`** | L6 `[NEW]` | `$88.24` / `$3.18B` | **`PH-clear`** (`-24.7%` vs `$117.13` **voids PT**; `-56.8%` DD, 2.78y) | `7.21%` / `+7.5%` / `6.23%` / `~10.0%` (`<25%`) | **PASS** (Shares `-2.90%` YoY via buybacks) | **PASS** (TTM FCF `$315M` = `~46%` margin; Yield `9.83%`) | **PASS** (Net Cash `-$548.9M`) | **FAIL `#9`/`#10`/`G2` (`7.21% <10%`) & `#11` (PEG `2.52 >2.50`)**; P/E `12.15x`, Yield `9.83%` | **TIER 3 HARD FAIL** (`#9`/`#10`/`G2` 3Y rev `7.21% < 10%` & EPS `6.23%`, `#11` PEG `2.52 > 2.50`). |
| **`TENB`** | L6 `[NEW]` | `$17.81` / **`$2.11B (<$2.5B)`** | **`PH-impaired`** (`-20.5%` vs `$22.39` **voids PT**; `-71.6%` DD, 4.45y, 3Y `-147.8pp`) | `7.36%` / `+8.0%` / `12.71%` / `~12.5%` (`<25%`) | **PASS** (Shares `-1.21%` YoY via buybacks) | **PASS** (TTM FCF `$270M` = `27%` margin; Yield `12.7%`) | **PASS** (Net Cash `-$39.8M`) | **FAIL `#9`, `#10`, & `G2`** (3Y rev `7.36% < 10%`); P/E `8.95x`, PEG N/A | **TIER 3 HARD FAIL** (`PH-impaired` Hard Exclude, `#9`/`#10`/`G2` 3Y rev `7.36% < 10%`, Cap `$2.11B < $2.5B`). |
| **`RBRK`** | L6 `[NEW]` | `$112.00` / `$23.2B` | **`PH-clear`** (`+3.0%` vs `$108.69`; `-10.4%` DD) | `23.54%` / `+26.0%` / N/A / `~16.5%` (`<25%`) | **FAIL `A1` & `G3`** (Shares **`+6.63%` YoY > `3.0%` `G3`**; SBC `~30%` rev + converts) | **PASS `A3a`** (TTM FCF `$303.9M` = `~23%` margin; Yield `1.31%`) | **PASS** (Net Cash) | **FAIL `#11` (P/E `~145x >45x`, Yield `1.31% <1.5%`) & `#12` (PT `+7.3% <20%`)**; PEG `0.41` | **TIER 3 HARD FAIL** (`A1`/`G3` `+6.63%` share dilution, `#11` P/E `~145x`, `#12` PT `+7.3% < 20%`). |
| **`VRNS`** | L6 `[NEW]` | `$48.50` / `$5.55B` | **`PH-warning`** (`+40.7%` vs `$34.47`; `-35.3%` DD, 5.5y) | `17.94%` / `+17.0%` / `58.28%` / `~15.0%` (`<25%`) | **FAIL `A1` & `G3`** (Shares **`+3.13%` YoY > `3.0%` `G3`**; SBC `~26%` rev + `$528M` converts) | **PASS `A3a`** (TTM FCF `~$115M` = `18%` margin; Yield `2.07%`) | **PASS** (Net Cash `-$383.2M`) | **FAIL `#11` (Fwd P/E `>85x`, GAAP loss `-$141.4M`) & `#12` (PT `+6.1% <20%`, Yield `2.07% <5%`)** | **TIER 3 HARD FAIL** (`A1`/`G3` `+3.13%` dilution & converts, `#11` P/E `>85x`, `#12` PT `+6.1% < 20%`). |

*(Note on Clinical-Stage Pre-Revenue Metabolic Biotechs also audited in Lane 4: **`VKTX`** [`$29.94`, `PH-clear`, H1 loss `-$286.3M`, WASO `+2.64%`], **`GPCR`** [`$27.67`, `PH-clear`, FCF `-$224.5M`], and **`ALT`** [`$2.735`, `PH-impaired` `-97.9%` DD, shares `+68.9%` YoY] all **Hard Fail Route H (`H1`)** due to zero commercial drug revenue or binding customer commitments).*

---

## Detailed Lane-by-Lane & Ticker-by-Ticker Breakdown

### Lane 4: Obesity, Metabolic, Rare Disease Biopharma & High-Velocity Medtech

1. **`LLY` (Eli Lilly — Seed) — TIER 1 BALLAST PASS NOW / CORE PASS AT `<= $1,107.36`**
   * **Price Health:** `$1,142.85`, 200DMA `$1,073.81` (`+6.43%` above rising 200DMA vs `$1,062.69` 20 sessions ago), ATH `$1,280.34` (`-10.74%` DD), **`PH-clear`**.
   * **Growth & `>=25%` 3Y IRR Case:** 3Y Rev CAGR `20.49%`, FY26 Next-FY `+35.8%`, 3Y EPS CAGR `30.95%`, buyback yield `~0.62%` (`$6.17B` TTM), dividend `~0.5%` -> **`~26.5%` annualized 3Y IRR (Plausible `>= 25%`)**.
   * **Stage A:** `A1`/`A2` Diluted WASO `-0.68%` YoY (`-0.62%` basic), SBC `~1.8%` rev, all M&A paid in cash. `A3` TTM FCF `$18.19B` (`22.83%` margin), NTM FCF `$28.809B` (`2.83%` yield), NTM Capex `$7.398B` / NTM OCF `$36.207B` = **`20.43% <= 50%`** (`A3c` passes easily despite aggressive GLP-1 manufacturing expansion). `A4` Net Debt/NTM FCF = `1.77x` base (`$50.96B` incl. Atai `$2.8B` + `$1B` CVR + `$2B` ID deals) and **`2.00x–2.21x` at maximum exposure** (`$57.5B–$63.6B` incl. Merida `$2.875B`, InnoCare `$3.25B`, Kelonia/Centessa milestones `<= 2.5x`). `A5` Wide moat, `~83%+` GM. `A7`/`#7` **Verified from 126 Form 4 filings (`insider-evidence.json`)**: Code-S sales `3,165,232` sh (Lilly Endowment), Code-P `0`, net selling = **`0.3551%` of `891.36M` shares (`<= 0.50%`)**; all 5 officer sales (Jonsson, Zakrowski, Hakim, Yuffa) are 10b5-1 plan sales (**`0` discretionary officer sales**).
   * **Stage C & Gate Verdict:** `#19` clear (Q2 EPS `$8.38` vs `$6.40`, rev `$22.974B` vs `$20.82B`). Passes `#11` on both Standard and High-Velocity tracks (Fwd P/E `27.41x`, PEG `1.27`, NTM FCF yield `2.83%`). Fails **only `#12`** (PT `$1,328.83` = `+16.27% < 20.0%`, FCF yield `2.83% < 5.0%`). **Capital-eligible immediately in the Ballast Slot; Full Core Pass at `<= $1,107.36`.**

2. **`NBIX` (`[NEW DISCOVERY]` Neurocrine Biosciences) — TIER 2 NEAR-PASS (`G-watch` on 17bp `G3` WASO excess under Rev 5)**
   * **Price Health:** `$143.18`, 200DMA `$147.26` (`-2.77%` vs 200DMA; PT leg valid), ATH `~$172` (`-16.8%` DD), **`PH-clear`**.
   * **Growth & `>=25%` 3Y IRR Case:** Next-FY (FY26) organic revenue `+27.0%` ex-Soleno (Ingrezza + Crenessity ramp), 3Y Rev CAGR `16.70%`, 3Y EPS CAGR `~40.9%` -> **`~27.5%` annualized 3Y IRR (Plausible `>= 25%`)**.
   * **Stage A / Route G:** TTM FCF `$870.4M` (`25.8%` margin; OCF `$898.1M` - Capex `$27.7M`, Capex/OCF `3.08%`), NTM FCF `129%` of TTM (`~$1.12B` = `7.78%` yield), Net Cash (`~0x` debt). `#7`/`G4` `0.494%` TTM net selling (6 bps inside `0.50%` cap). `#19` clear. Fwd P/E `12.66x`, PEG `0.31`, PT `$207.29` (`+44.8%`).
   * **Why Tier 2 under Policy Rev 5:** Diluted WASO is **`+3.17%` YoY** (SBC `~9.5%` rev). While unmerged Policy Rev 4 (`d28bdc4`) raised `G3` to `3.5%` to admit `NBIX`, **merged Policy Rev 5 (`f6171aa`) kept `G3` at `<= 3.0%`**, leaving `NBIX` **17 bps above `G3`**. **Exact Buy Trigger:** Q3 print (`~Oct 27, 2026`) bringing YoY diluted WASO `<= +3.00%` at **`<= $175.00`** (`G5` ceiling).

3. **`PODD` (`[NEW DISCOVERY]` Insulet Corp) — TIER 2 NEAR-PASS (`1-Step Watch` on `#12` 5.0% Cash-Yield Floor & `A5` GM)**
   * **Price Health:** `$131.69`, 200DMA `$193.38` (**`-31.90%` below 200DMA -> voids `#12` PT leg** of `$171.91` / `+30.5%`), ATH `$352.82` (2025-09-09, `-62.68%` DD, age `1.06 yrs < 3.0 yrs` -> **`PH-clear` by age**).
   * **Growth & `>=25%` 3Y IRR Case:** 3Y Rev CAGR `16.15%`, Next-FY (FY26) `+21.38%` (20–22% cc guide), 3Y EPS CAGR `23.06%`, buyback yield `1.19%` (`$300M` ASR), Fwd P/E `19.09x`, PEG `0.96` -> **`~28.4%` annualized 3Y IRR (Plausible `>= 25%`)**.
   * **Stage A & Gate Verdict:** `A1` WASO `-1.77%` YoY (Q2) / `-1.19%` (H1), 2026 converts redeemed all-cash Aug 2025. `A3` TTM FCF `$293.7M` (`9.62%` margin). Raw blended NTM FCF is `$469.75M` (`5.145%` yield), but management's qualitative capex guide ("increasing vs FY25 `$191.6M`") triggers the framework's **`x1.25` capex fallback** (`$271.88M`), reducing NTM FCF to `$439.53M` (**`4.814%` yield** on blended capex) or `$375.73M` (**`4.115%` yield** on full-NTM capex)—short of `#12`'s `5.0%` floor while the PT leg is void. `A4` `1.09x–1.36x` (incl. `$97M` Costa Rica seller-loan guarantee). `A5` FY25 GM `71.63%`, FY26E `71.81%` adj (H1 GAAP `69.8%` after `$33.6M` MDC cannula field-correction costs). `#7` **Net insider buying `-0.0178%`** (`-12,363` sh across 46 Form 4s; 0 officer sales; CEO bought 5,400 sh). `#19` clear.
   * **Exact Buy Trigger:** **`<= $126.76`** (blended capex fallback `5.0%` yield) / **`<= $108.35`** (full-NTM `x1.25` capex `5.0%` yield), or **`Nov 4, 2026`** print confirming NTM FCF `>= $456.5M` and GAAP GM recovery. Provisional `G5` ceiling: **`$184.58`**.

4. **`ARGX` (argenx SE — Seed) — TIER 2 NEAR-PASS (`G-watch` pending FY26 2nd positive OCF year & AFM insider sweep)**
   * `$810.00` (`-4.87%` vs 200DMA `$851.50`, `PH-clear`), 3Y Rev `30.39%`, 3Y EPS `32.75%`, Fwd P/E `29.74x`, PEG `0.85`, PT `$1,152` (`+42.2%`), TTM FCF `$849M` (`19.5%` margin), Net Cash `-$5.1B`. Fails Core `A1`/`A2` (diluted WASO `+1.8%` with zero buybacks), and `G2` requires two completed positive-OCF FYs (awaits FY26 completion in Feb 2027) + Dutch AFM/Belgian FSMA PDMR sweep. **Trigger: `<= $785.00` post-FY26 print.**

5. **`ISRG` (Intuitive Surgical — Seed) — TIER 2 NEAR-PASS (`G-watch` / Double `#14a` Shortfall)**
   * `$391.95` (`-12.36%` vs 200DMA `$447.22`, `PH-clear`), WASO `-1.11%`, TTM FCF `$3.22B` (`29.21%` margin), Net Cash `-$5.22B`, Fwd P/E `34.69x` (passes Rev 5 `<=38x`). Fails **both** `#9` (3Y Rev `14.11% < 15.0%`) and `#11` (PEG `2.25 > 2.0`), which cannot be combined under `#14a`. **Trigger: `<= $339.00` (`G5`) or `<= $348.40` (PEG `<= 2.0`).**

6. **`REGN` (`[NEW DISCOVERY]` Regeneron) — TIER 2 NEAR-PASS (`G-watch` on Price vs. `G5` Ceiling)**
   * `$735.20` (`-0.11%` vs 200DMA `$736.04`, `PH-clear`), Fwd P/E `12.02x`, PEG `1.00`, NTM FCF `$6.31B` (`8.59%` yield), WASO `-2.39%`, Net Cash `-$14.85B`, `#7` `0.017%`. Fails Core `#9` (3Y Rev `11.36% < 15%`, FY27E `+8.7%`) and `#10` (3Y EPS `15.69% < 20%`). Under Route G, `G5` base return at `$735.20` is `8.1%/yr` (`<12%`). **Trigger: `<= $617.00`.**

7. **`KRYS` (`[NEW DISCOVERY]` Krystal Biotech) — TIER 2 NEAR-PASS (`G-watch` / High-Velocity Watch)**
   * `$331.80` (`+9.28%` vs 200DMA `$303.61`, `PH-clear`), 3Y Rev `31.96%`, 3Y EPS `24.60%`, Fwd P/E `40.84x` (passes HV `<=45x`), PEG `0.93`, TTM FCF `~$258M` (`2.63%` yield), Net Cash `~$750M`. Fails Core `A1` (`+1.46%` shares w/ 0 buybacks) and `#12` (PT `$392.11 = +18.2% < 20%`). **Trigger: `<= $275.00` (`G5` ceiling; `#12` clears at `<= $326.75`).**

8. **`ADMA` (`[NEW DISCOVERY]` ADMA Biologics) — TIER 2 NEAR-PASS (`G-watch`)**
   * `$10.20`, Mkt Cap `$2.44B` (`PH-clear`, `-11.15%` vs 200DMA `$11.48`), 3Y Rev `12.65%`, 3Y EPS `22.26%`, Fwd P/E `14.5x`, PEG `0.65`, TTM FCF `$116.47M` (`4.77%` yield), PT `$19.70` (`+93%`). Fails Core `A1` (`+1.15%` shares w/ `<25%` rev growth) & `#9` (`12.65% < 15%`). **Trigger: `<= $9.50` (`G5` w/ Mkt Cap `>= $2.5B`).**

9. **`MDGL` (`[NEW DISCOVERY]` Madrigal Pharmaceuticals) — TIER 2 NEAR-PASS (`H-watch` on `H4` 20% return hurdle)**
   * `$499.00` (`PH-clear`, `-3.39%` vs 200DMA `$516.50`), Fwd P/E `51.89x`, TTM FCF negative (`-$80M+`), Shares `+11%` YoY. Fails `A1`/`G3` and `A3a`/`G2`; evaluated under Route H where `H4` 5Y return fails `20%` hurdle above **`$397.00`**.

10. **Lane 4 Tier 3 Hard Fails:**
    * **`VRTX` (Seed):** `$496.50` (`PH-clear`). Fails `#9` (`11.11%` 3Y rev), `#10` (`8.50%` 3Y EPS), `#11` (PEG `2.68 > 2.50`), `#12` (PT `+15.1% < 20%`, FCF yield `3.09% < 5%`), and `<25%` IRR.
    * **`TMDX` (`[NEW]`):** `$77.50` (`-21.22%` vs 200DMA `$98.38` -> **voids `#12` PT leg**). Fails `A1`/`A2` (`+1.53%` shares, 0 buybacks), `A3b`/`A3c` (aviation jet fleet capex `>45–55%` OCF, NTM FCF `<` TTM), `#11` (PEG `>2.5`), `#12` (PT void + FCF yield `~2.5% < 5%`).
    * **`LNTH` (`[NEW]`):** `$100.02` (`PH-clear`). Fails `#9`, `#10`, & `G2` (3Y rev `~3.5% < 10%` floor as Pylarify matures; PT `+7.3%`).
    * **`HALO` (`[NEW]`):** `$105.00` (`PH-clear`). Fails `A1` (convertible notes outstanding), `A7` (insider selling), and `G5` (ENHANZE 2028–30 patent cliff multiple compression).
    * **`EXEL` (`[NEW]`):** `$53.50` (`PH-clear`). Fails `#7`/`A7` (insider net selling `>0.5%`), `#9` (`12.59%` 3Y rev `<15%`), `#10` (`18.02%` EPS `<20%`), and `G5` (Cabometyx 2030 patent cliff).
    * **`AXSM` (`[NEW]`):** `$165.00` (`PH-clear`). Fails `A1`/`G3` (`+4.44%` YoY share dilution `>3.0%`), `A3a`/`G2` (negative TTM FCF `-$95M`), and `#11` (Fwd P/E `798.22x`).
    * **`MIRM` (`[NEW]`):** `$82.00` (`PH-clear`). Fails `A1`/`G3` (`+8.5%` YoY convert/equity dilution), `A3a`/`G2` (FCF margin `<6%`), and `#11` (negative/N/A P/E).
    * **`DXCM` (`[NEW]`):** `$83.60` (**`PH-impaired`**: `-49.0%` DD from Nov 2021 ATH `$164.00`, age `4.9 yrs`, 3Y gap `<-80pp`). Also fails `A3b` (NTM FCF `<` TTM `$1.41B`), `#9` (`11.49%` 3Y rev), and `#12` (PT `+15.4%`, Yield `4.48%`).
    * **`BSX` (`[NEW]`):** `$43.20` (`-28.49%` vs 200DMA `$60.41` -> voids PT). Fails `A1` (pending **Penumbra acquisition ~27% stock consideration**), `A4` (pro forma `>2.5x`), and `#9`/`#10`/`G2` (`5.53%` 3Y rev, `6.74%` 3Y EPS).
    * **`PRCT` (`[NEW]`):** `$19.20`, Mkt Cap **`$1.10B` (`< $2.5B` floor)**. Fails `A1`/`G3` (`+9%` share dilution), `A3a`/`G2` (negative FCF `-$75M`), and `H4`.
    * **`ALNY` (`[NEW]`):** `$228.50` (`-24.13%` vs 200DMA `$301.18` -> **voids `#12` PT leg** of `$370.55` / `+62.2%`). Fails **`#19` Blackout**, `A1` (`+2.4%` shares + converts), and `#12` (PT void + FCF yield `2.74% < 5.0%`).
    * **`IDXX` (`[NEW]`):** `$541.80` (`PH-clear`). Fails `#9`, `#10`, & `G2` (3Y rev `~8.8% < 10%` floor) and `#11` (PEG `2.39 > 2.0`).
    * **`RMD` (`[NEW]`):** `$218.89` (`PH-warning`: `-26.39%` DD, age `5.065 yrs`, 3Y gap `-32.64pp`). Fails `#9`, `#10`, & `G2` (3Y rev `5.30% < 10%`, FY27 `+2.7%`, 3Y EPS `8.98% < 20%`).

---

### Lane 5: Public Safety, Municipal GovTech & Autonomous/NATO Rearmament Defense

1. **`KOG.OL` (`[NEW DISCOVERY]` Kongsberg Gruppen) — TIER 2 NEAR-PASS (Blocked ONLY by `#19` Earnings Blackout until Oct 29, 2026)**
   * **Price Health:** `NOK 308.00` (`PH-clear`; historical series adjusted for Apr 22, 2026 Kongsberg Maritime `KMAR` 1:1 demerger distribution).
   * **Growth & `>=25%` 3Y IRR Case:** Next-FY continuing rev `+36.4%` (Q2 rev `NOK 10.389B` `+31%`, EBIT margin `16.1%`), 3Y Rev CAGR `~22.5%`, 3Y EPS CAGR `~34.8%`, Fwd P/E `33.41x <= 38.0x`, PEG `0.96`, PT `+28.5%` (11 analysts) -> **`~26.5%` annualized 3Y IRR (Plausible `>= 25%`)**.
   * **Stage A & Gate Verdict:** Passes `A1` (flat shares YoY), `A3` (TTM FCF `NOK 6.03B`, blended NTM FCF `NOK 9.90B`, Capex/OCF `~24%`), `A4` (Net Cash), `#7` (**verified clean via Oslo Børs Newsweb PDMR sweep**), `#9`, `#11`, and `#12`. Blocked **only by `#19` Blackout** (Q2 continuing rev `-3.4%` and EBITDA `-8.8%` vs consensus). **Unlocks after clean Oct 29, 2026 Q3 print at `<= NOK 350.30` (`38x` P/E ceiling).**

2. **`AVAV` (`[NEW DISCOVERY]` AeroVironment) — TIER 2/3 (`H-watch` / Core Hard Fail)**
   * `$120.60` (`-40.07%` vs 200DMA `$201.24` -> voids PT; `-70.57%` DD from Oct 2025 ATH `$409.83`, age `1.0 yr` -> `PH-clear` by age).
   * **Hard Fails Core & Route G:** Diluted WASO `+6.27%` YoY (`+52.13%` total shares incl. BlueHalo; March 16, 2026 **ESAero stock consideration = `671,078` shares = `1.33–1.35%`**, exceeding Rev 5's `0.50%` bolt-on carve-out -> **fails `A1`**). Actual TTM Company FCF is **`-$25.03M`** (`-1.25%` margin: OCF `$58.82M` - Capex `$83.85M`; FY27E FCF `-$89.19M` -> **fails `A3a` & `G2`**).
   * **Route H Audit:** Passes `H1` (`$1.46B` funded backlog) and `H2` (`$917.2M` liquidity vs `$623.6M` buffered 24m need), but `H4` 5Y base return is only **`8.5%/yr` (`< 20%` hurdle)** at `$120.60`, plus two securities class actions and two material weaknesses. **Conditional `H4` Trigger: `<= $72.88`.**

3. **Lane 5 Tier 3 Hard Fails:**
   * **`AXON` (Seed):** `$413.35` (`-16.82%` vs 200DMA `$496.96`, `PH-clear`). Despite `30.71%` 3Y rev growth, **hard fails `A3a` and `G2`** because TTM Company FCF is only **`$133.19M` (`4.14%` FCF margin `< 6.0%` floor**; P/FCF `252.8x` = `0.39%` yield), **fails `A1`/`G3`** (WASO `+3.1%` YoY; SBC `18.5%` of rev / `>250%` of FCF + stock M&A/converts), **fails `A4`** (Net Debt `$1.16B` = `8.7x` TTM FCF), and **fails `#11`** (Fwd P/E `45.56x > 45.0x` HV cap, PEG `1.71 > 1.65`, FCF yield `0.39% < 1.15%`). Mature S&P 500 incumbent cannot use Route H to bypass `G2`.
   * **`RHM.DE` (Rheinmetall — Seed):** `€956.00` (`-26.18%` vs 200DMA `€1,295.00` -> **voids `#12` PT leg** of `€1,571` / `+64.3%`). **Hard fails `A3a`, `A3c`, and `G2`**: TTM Company FCF margin is **`3.4%–3.8%` (`< 6.0%` floor)** and H1 operating FCF plunged to **`-€1.616B`** due to ammunition factory capex (`>55%` of OCF) and working-capital inventory build; also fails `A1` (`+1.08%` WASO) and `#12` (PT leg void + FCF yield `<2%`).
   * **`MSI` (`[NEW]`):** `$442.00` (`PH-clear`). Fails `#9`, `#10`, `#14a`, & `G2` (3Y rev `9.08% < 10%` floor, 3Y EPS `12.34% < 20%`), `A4` (Net Debt `$6.1B` / FCF `$2.40B` = `2.54x > 2.5x`), and `#11` (PEG `2.31 > 2.0`).
   * **`KTOS` (`[NEW]`):** `$43.07` (`PH-warning`; `-37.53%` vs 200DMA `$68.95` voids PT). **Hard fails `A1` and `G3`** (**`+15.14%` YoY share dilution** from **`$1.0B` March 2026 equity offering**), **hard fails `A3a` and `G2`** (Q2 FCF `-$28.2M`, FY26E FCF **`-$93.46M`**), and fails `#11` (Fwd P/E `39.15x > 38.0x`).
   * **`DRS` (`[NEW]`):** `$36.50` (`PH-clear`). Fails `A1`/`A2` (`+1.1%` shares w/ 0 buybacks), `#9`/`#10`/`G2` (3Y rev `~8.5% < 10%`), and `#11` (PEG `3.07 > 2.50`).
   * **`SAAB-B.ST` (`[NEW]`):** `SEK 608.10` (`PH-clear`). Fails `#12` (PT `SEK 637.07` = `+4.76% < 20%` and FCF yield `2.21% < 5.0%`) and `G5` (5Y valuation ceiling).
   * **`BAESY` / `BA.L` (`[NEW]`):** `2,015p` (`PH-clear`). Fails `A3b` (NTM FCF `<` customer advance-inflated TTM FCF `£4.70B`), `#9`/`#10`/`G2` (3Y rev `~8.8% < 10%`), and `#12` (PT `+15.3% < 20%`).
   * **`LDOS` (`[NEW]`):** `$118.50` (`PH-clear`). Fails `A3b` (NTM FCF `<` TTM FCF) and `#9`/`#10`/`G2` (3Y rev `5.17% < 10%`, 3Y EPS `4.42% < 20%`).
   * **`ESLT` (`[NEW]`):** `$701.50` (`PH-clear`). Fails `A1`/`A2` (share dilution `>+0.5%` w/ 0 buybacks), `#9` (3Y rev `12.19% < 15%`), `#11` (Fwd P/E `38.15x > 38.0x`), and `#12` (PT `+14.2% < 20%`, FCF yield `~2.2% < 5.0%`).
   * **`LHX` (`[NEW]`):** `$236.60` (`-23.83%` vs 200DMA `$310.60` -> voids PT). Fails `A4` (Net Debt `~$11.5B` = `~3.6x > 2.5x` FCF) and `#9`/`#10`/`G2` (3Y rev `7.51% < 10%`).
   * **`NOC` (`[NEW]`):** `$478.00` (`-20.11%` vs 200DMA `$598.33` -> voids PT). Fails `A4` (Net Debt `~$14.2B` = `~3.5x > 2.5x` FCF), `#9`/`#10`/`G2` (3Y rev `5.93% < 10%`), and `#11` (PEG `2.64 > 2.50`).
   * **`GD` (`[NEW]`):** `$330.09` (`PH-clear`). Fails `A1` (WASO `+0.95% > +0.5%`), `A3b` (NTM FCF `<` TTM FCF), and `#9`/`#10`/`G2` (3Y rev `5.21% < 10%`).
   * **`LMT` (`[NEW]`):** `$505.41` (`PH-clear`). Fails `A3b` (blended NTM FCF `$6.71B <` TTM `$8.73B`), `A4` (pro forma Net Debt `$20.20B` incl. `$3.45B` Ultra Maritime = **`3.01x > 2.5x`**), `A2` (2026 buybacks paused under Jan 7 EO), and `#9`/`#10`/`G2` (3Y rev `6.38% < 10%`).
   * **`TYL` (`[NEW]`):** `$335.00` (`PH-clear`). Fails `#9`, `#10`, `#14a`, & `G2` (3Y rev `9.37% < 10%` floor, 3Y EPS `15.21% < 20%`, PEG `~2.15 > 2.0`).

---

### Lane 6: Cybersecurity & Identity Consolidators

1. **`FTNT` (Fortinet — Seed) — TIER 2 NEAR-PASS (`G-watch` on Price vs. `G5` Ceiling)**
   * **Price Health:** `$80.19`, 200DMA `$81.61` (`-1.74%` vs 200DMA; PT leg valid), ATH `$114.57` (`-30.01%` DD), **`PH-clear`**.
   * **Stage A & Route G:** WASO **`-3.85%` YoY** (`$2.24B` H1 buybacks), SBC `4.2%` rev (`~11%` FCF), TTM FCF `$2.43B` (`35.8%` margin, `4.04%` yield), Capex/OCF `11%`, Net Cash `-$1.18B`, `#7`/`G4` `0.145%` net selling (Xie brothers 10b5-1), `#19` clear.
   * **Why Tier 2:** Fails Core `#9` (3Y Rev `10.67% < 15.0%` and `< 12.0%` `#14a`), `#10` (3Y EPS `10.71% < 20%`), `#11` (PEG `2.34 > 2.0`), and `#12` (PT `$89.65 = +11.8% < 20%`, NTM FCF yield `~4.3% < 5.0%`). Under Route G, passes `G1`–`G4`, but at `$80.19` its 5Y `G5` base return is `8.98%/yr` (`< 12.0%` hurdle). **Exact Buy Trigger: `<= $72.24` (`G5` `12%` return ceiling).**

2. **`CVLT` (`[NEW DISCOVERY]` Commvault Systems) — TIER 2 NEAR-PASS (`G-watch` on Price vs. `G5` Ceiling)**
   * `$152.00` (`+30.76%` vs 200DMA `$116.24`, `PH-clear`), WASO `-3.23%` YoY, TTM FCF `$258.45M` (`~25%` margin, Capex/OCF `2.35%`, `3.92%` yield), Net Cash `~$300M`, Fwd P/E `28.58x`, PEG `1.54`. Fails Core `#9` (3Y Rev `11.07% < 15%` and `< 12%` `#14a`), `#10` (3Y EPS `18.61% < 20%`), and `#12` (PT `$160.55 = +5.6% < 20%`, FCF yield `~4.2% < 5.0%`). **Exact Buy Trigger: `<= $131.50` (`G5` `12%` return ceiling).**

3. **`CRWD` (CrowdStrike — Seed) — TIER 2/3 (`G-watch` on extreme valuation)**
   * `$436.32` (`-1.18%` vs 200DMA `$441.52`, `PH-clear`), 3Y Rev `20.53%`, 3Y EPS `23.2%`, TTM FCF `$1.30B` (`27.0%` margin, `1.21%` yield), Net Cash `-$4.62B`. Fails Core `A1`/`A2` (WASO `+1.26%` YoY w/ `0.09%` buybacks and `<25%` rev growth; SBC `21.5%` rev), `#11` (Fwd P/E `76.2x`, PEG `3.29`, FCF yield `1.21% < 1.5%`), `#12` (PT `+15.8% < 20%`), and `G5` (`-2.2%/yr` 5Y base return). **Exact Buy Trigger: `<= $265.24` (`G5` `12%` return ceiling).**

4. **`CYBR` (`[NEW DISCOVERY]` CyberArk Software) — CORPORATE ACTION / DELISTED EXCLUSION**
   * Acquired by Palo Alto Networks (`PANW`) on **February 11, 2026** (`$45.00` cash + `2.2005` `PANW` shares per `CYBR` share).

5. **Lane 6 Tier 3 Hard Fails:**
   * **`PANW` (Seed):** `$176.21` (`PH-clear`). **Hard fails `A1` and `G3`** (**`+20.8%` YoY share dilution**: `833.8M` vs `690.0M` from the transformative **CyberArk stock acquisition** + Chronosphere), **fails `#11`** (Fwd P/E `41.9x > 38.0x`, PEG `2.67 > 2.50`), **fails `#12`** (PT `+18.3% < 20%`, FCF yield `2.81% < 5.0%`), and fails `G5` (`$117.13` ceiling).
   * **`ZS` (Seed):** `$145.65` (**`PH-impaired` Hard Exclude**: `-60.50%` DD from Nov 2021 ATH `$368.78`, age `4.87 yrs`, 3Y gap `-91.77pp`; `-31.96%` below 200DMA `$214.07` -> **voids `#12` PT leg**). Also **hard fails `A1`** (**`$1.725B` 0% 2028 convertible notes issued July 2025** + WASO `+1.26%` w/ 0 buybacks) and `#12` (PT void + FY27E FCF yield `4.74% < 5.0%`).
   * **`NET` (`[NEW]`):** `$260.00` (`PH-clear`). **Hard fails `A1`/`A2`** (`+2.02%` share dilution w/ 0 buybacks + converts; SBC `24%` rev), **hard fails `#11`** (Fwd P/E **`219.45x`**, PEG **`4.41`**, FCF yield **`0.30%`**), and **fails `#12`** (PT `+9.6% < 20%`).
   * **`OKTA` (`[NEW]`):** `$75.49` (**`PH-impaired` Hard Exclude**: `-74.13%` DD from Feb 2021 ATH `$291.78`, age `5.64 yrs`, 3Y gap `-100.38pp`). Also fails `A1` (`+2.90%` YoY share dilution) and `#9`/`#10`/`G2` (3Y rev `8.63% < 10%`, 3Y EPS `11.48% < 20%`).
   * **`S` (`[NEW]`):** `$21.50` (**`PH-impaired` Hard Exclude**: `-71.8%` DD from Nov 2021 ATH `~$76.30`, age `4.9 yrs`, 3Y gap `<-80pp`). Also **hard fails `A1` & `G3`** (`+3.28%` YoY share dilution `> 3.0%`; SBC `24%` rev), **hard fails `A3a` & `G2`** (TTM FCF `~$46M` on `$1.10B` rev = **`4.18%` margin `< 6.0%` floor**), **fails `#11`** (Fwd P/E `63.2x`, Yield `0.65%`), and **fails `#12`** (PT `+13.9% < 20%`).
   * **`CHKP` (`[NEW]`):** `$159.40` (`PH-clear`). **Hard fails `A1`** (**issued `$1.75B` 0% 2030 convertible senior notes in H1 2026**) and **fails `#9`/`#10`/`G2`** (3Y rev `5.91% < 10%`, 3Y EPS `9.15% < 20%`).
   * **`QLYS` (`[NEW]`):** `$88.24` (`-24.66%` vs 200DMA `$117.13` -> voids PT; `PH-clear` by age `2.78 yrs`). Fails `#9`/`#10`/`G2` (3Y rev `7.21% < 10%`, 3Y EPS `6.23% < 20%`) and `#11` (PEG `2.52 > 2.50`).
   * **`TENB` (`[NEW]`):** `$17.81`, Mkt Cap **`$2.11B` (`< $2.5B` floor)** (**`PH-impaired` Hard Exclude**: `-71.58%` DD, age `4.45 yrs`, 3Y gap `-147.82pp`; `-20.46%` vs 200DMA voids PT). Also fails `#9`/`#10`/`G2` (3Y rev `7.36% < 10%`).
   * **`RBRK` (`[NEW]`):** `$112.00` (`PH-clear`). **Hard fails `A1` & `G3`** (**`+6.63%` YoY share dilution `> 3.0%`**; SBC `~30%` rev + converts), **fails `#11`** (Fwd P/E `~145x`, FCF yield `1.31% < 1.5%`), and **fails `#12`** (PT `+7.3% < 20%`).
   * **`VRNS` (`[NEW]`):** `$48.50` (`PH-warning`). **Hard fails `A1` & `G3`** (**`+3.13%` YoY share dilution `> 3.0%`**; SBC `~26%` rev + `$528.4M` converts), **fails `#11`** (Fwd P/E `>85x`, GAAP loss `-$141.4M`), and **fails `#12`** (PT `+6.1% < 20%`, FCF yield `2.07% < 5.0%`).

---

# Batch 3 Open-Universe Non-AI-Capex Diversification Screen Report
**Framework Baseline:** `CyberFvde/asymmetry-gates` Policy Revision 5 (Merged Commit `f6171aa`, October 15, 2026)  
**Scope:** Lane 7 (Crypto, Retail Brokerage & Electronic Market Infrastructure — 11 Tickers), Lane 8 (Space Launch, D2D & Defense Space Systems — 9 Tickers), Lane 9 (Uranium, Nuclear Fuel Cycle & Enrichment — 9 Tickers), and Explicit Structural Exclusions Log (8 Tickers) = **37 Total Tickers Audited**.

---

## Executive Summary & Batch 3 Headline Findings

1. **Tier 1 (Full Gate Pass + ≥25% Plausible 3Y IRR):** **0 Tickers** across Lanes 7, 8, and 9.
2. **Tier 2 (Near-Pass Watchlist / Actionable Conditional Triggers):** **4 Tickers** (`TW`, `SCHW`, `KAP.L`, `ASTS` [`H-watch`]):
   - **`TW` (Tradeweb Markets — `[NEW DISCOVERY]`, Lane 7):** Cleanest balance sheet (`$1.91B` net cash), `PH-clear`, passes `A1` (`+0.13%` shares YoY), `A3a/b/c` (`$1.14B` TTM FCF, ~50% margin), `A4`, `A5` (`Wide` moat), `A7`, and `#11` (`Fwd P/E 25.51x ≤ 38`, `PEG 1.62 ≤ 2.0`, `FCF yield ~4.4%`). **Sole blocker:** Under `FT1` (`fintech.md`), Fintech/Electronic Brokerages are **barred from `#14a` starters** and must clear the full `#9` growth gate (`≥15%` 3Y Rev CAGR AND `≥15%` next-FY organic growth) or `#10` (`≥20%` 3Y EPS/FCF CAGR + `Wide` moat). Consensus sits at `11.73%–12.14%` 3Y Rev CAGR and `14.30%–14.96%` 3Y EPS CAGR. **Buy Trigger:** Pullback to **≤ $82.00** (`≥5.0%` NTM FCF yield for `#12` + `25%+` 3Y IRR via multiple re-rating) **AND** a quarterly print accelerating organic revenue guide to `≥15%` (or NTM EPS CAGR revision to `≥20%` under `#10`).
   - **`SCHW` (Charles Schwab — `[NEW DISCOVERY]`, Lane 7):** Valuation passes `#11` (`Fwd P/E 14.9x`, `PEG 1.35`) and EPS growth clears `#10` (`22.72%` 3Y EPS CAGR ≥ 20% with `Wide` moat), with PT `$121.86` (`+26%` vs `$95.94–$96.70`). **Blockers:** Hard `A7` fail (4 officers including both Co-Chairmen made code-`S` open-market discretionary sales outside `10b5-1` in Q1 and Q3 2026) + `FT2/FT3` bank-sweep deposit sorting adjustments. **Buy Trigger:** Roll-off of Q1/Q3 2026 discretionary officer sales (`12-month` clean Form 4 window after **Q3 2027**) at **≤ $95.00**.
   - **`KAP.L` (Kazatomprom GDR — `[NEW DISCOVERY]`, Lane 9):** World's lowest-cost Tier-1 ISR uranium producer (`Wide` cost moat), `PH-clear` (`~$62.50`, `-15.1%` vs 200DMA `$73.59`), net cash, and **only uranium producer passing `F1` valuation ceilings** (`Fwd P/E 10.8x ≤ 15`, `EV/EBITDA 7.28x ≤ 11`, `EBITDA margin ~52% ≥ 30%`, `FCF margin ~24% ≥ 10%`). **Blockers:** Fails `F1` growth/buyback sub-tests (`3Y EPS CAGR ~14–18% < 25%` due to Kazakh MET tax step-up & sulfuric acid constraints; `0` gross share buybacks in last 4Q; `<15` English-language consensus analysts on GDR) and lacks an `F2` qualifying open-market insider purchase (`≥$2M` & `≥5%` holding increase within 30d; sovereign Samruk-Kazyna 75% holder + foreign-filer disclosure gap). **Buy Trigger:** Qualifying `F2` CEO/CFO open-market purchase + 1Q token buyback + pullback to **≤ $52.00** (`≥25%` 3Y EPS/dividend IRR).
   - **`ASTS` (AST SpaceMobile — Seed, Lane 8):** Designated `H-watch` (`stage-paths.md`) with real commercial D2D spectrum/MNO contracts (`H1` close), but currently blocked by **5 concurrent gates**: (1) `#19a` active earnings blackout (Q2 rev `$31.52M` vs `$34.50M` est = `-8.64%` miss) & `#17` revision cut (FY27E rev cut `-10.6%` to `$581.65M`), (2) `>20%` below 200DMA (`$42.14` vs `$80.28` = `-47.5%`, voiding `#12` PT leg), (3) `H2` 24-month stressed funding gap (`$5.02B` buffered need vs `$3.31B` usable cash even after July `$1.15B` convert), (4) `H4` 5Y hurdle (`$104.86/sh` requires `~$2.18B–$2.35B` FY30 FCF at 22–25x), and (5) `H5` insider/10%-holder sales (`1.45%` if Rakuten `3.04M` + American Tower `2.29M` strategic sales count) + W.D. Tex. securities class action. **Buy Trigger:** Clean Q3 2026 print lifting `#19a` blackout + non-dilutive Ex-Im/FirstNet funding closing the `$1.71B` `H2` gap + entry **≤ $22.00**.
3. **Why Every Other Candidate Fails Hard Gates (Tier 3):**
   - **Lane 7 (`FT` Overlay):** `FT1` strictly bans `#14a` starters and Route G/H for Fintech/Crypto/Brokers. `HOOD` fails `A1` (`$2.2B` 0% convertible senior notes closed Jun 25, 2026), `A3a/FT2` (`4.44%` ex-client-cash FCF margin), `FT4` (retail options/crypto/rate sensitivity), and `#11` (`P/E 39.9x > 38`, `PEG 2.14 > 2.0`). `COIN` fails `#9/#10` (`3.49%` 3Y rev CAGR), `#11` (`Fwd P/E 179.8x`, `PEG 15.72`), `A1` (converts + Deribit/Bitstamp stock M&A + SBC), `A3b`, and `FT4`. `IBKR` fails `A1` (Up-C share creep), `#9` (`<15%` 3Y rev CAGR), and `FT2/FT4` (segregated cash OCF distortion & rate spread dependence). `CME`, `CBOE`, `ICE`, `NDAQ` fail `#9/#10` (8–11% rev CAGR, 9–15% EPS CAGR) and `#12` (`<20%` PT upside & `<5%` FCF yield), with `ICE` (`3.83x`) and `NDAQ` (`2.67x`) also failing `A4` (`≤2.5x` Net Debt/FCF). `FUTU` trades `-22.6%` below 200DMA (voiding `#12` PT leg) and fails `#9/#10`, `A3b/FT2`, and `#7`.
   - **Lane 8 (Space/Defense):** `RKLB` is a hard `H5` fail (`62` Form 4s = `8,880,247` shares sold / `0` bought = `1.3285% > 0.50%`, roll-off ~Jul 7, 2027), plus `A1` (`$1.944B` ATM `29.3M` sh Sep 15, 2026 + `~42.4M` sh Iridium M&A), `A3a` (`-$325.6M` TTM FCF), Oct 14 8-K Neutron slip to 2027, and `H4` (`$147.26/sh` 5Y hurdle requires `$4.36B` FCF; indicative ceiling `~$21`). `PL` (`-48.1%` vs 200DMA) fails `A1/G3` (`$120M` ATM + `$460M` converts + `+18.2%` WASO), `A3b/G2` (FY27E FCF `-$29.1M`), `#19d` guide miss (`-9.9%`), and `H4` (base 5Y model `$12.51/sh` = `-2.4%/yr`; indicative ceiling `$8–$9`). `IRDM` is a pending M&A target being acquired by `RKLB` (closing mid-2027) and fails `A4` (`5.56x` Net Debt/FCF) and `#9`. `MDA.TO` fails `A1` (`+30%` 3Y share dilution) and `A3a/G2` (lumpiness in working-capital/satellite capex FCF). `LUNR`, `RDW`, `BKSY`, `SATS` fail `A1` and `A3a/G2` (and `$2.5B` cap floor for `LUNR`/`BKSY`).
   - **Lane 9 (Uranium/Nuclear):** Under `stage-paths.md`, commodity producers (`CCJ`, `KAP.L`, `UEC`, `NXE`, `UUUU`) **must** use Route `F` (no G/H bypass). `CCJ` fails `F1` (`Fwd P/E 59.9x–97x > 15`, `EV/EBITDA 66.4x > 11`, `EBITDA margin ~23% < 30%`) and `F2` (no insider buy). `UUUU` is `PH-impaired` (`96.45%` below 2007 ATH, `-50.8%` vs 200DMA) and fails `F1` (`-$120.4M` TTM FCF, `$300M` ATM + `$500M` new ATM Oct 13 + `14.81M` sh ASM deal + `65.85M` sh pending VAC deal + `$700M` converts) and `F2`. `NXE` and `UEC` fail `F1` (negative FCF/EPS, share issuance) and `F2`. Equipment/enrichment/SMR names (`LEU`, `BWXT`, `OKLO`, `SMR`) all fail `A1` (`BWXT` `$1.1B` converts Nov 2025 + `A4` `~7.0x` Net Debt/FCF; `LEU`, `OKLO`, `SMR` heavy ATMs/converts/equity raises and negative FCF `A3a/G2` + `H1/H3/H4` failures).

---

## Master Summary Table — Batch 3 (All 37 Tickers)

| Lane | Ticker | Status / Tag | Route | Price (Oct 2026) | Mkt Cap | vs 200DMA (`#12` PT Leg) | `PH` Status | 3Y Rev / EPS CAGR | Est 3Y IRR (Plausible?) | Primary Blocking Gates | Tier | Exact Dollar Buy Trigger / Indicative Ceiling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **L7** | **`HOOD`** | Seed | `A–E` (`FT`) | `$101.08` (`$112.74` 10/2) | `$90.8B` | `+7.2%` (`200DMA $94.33`) | `PH-clear` | `21.3%` / `24.0%` | `15.8%` (No — mult. compression) | `A1` (`$2.2B` convert 6/25/26), `A3a/FT2` (`4.44%` FCF margin), `FT4`, `#11` (`PE 39.9`, `PEG 2.14`) | **Tier 3** | **Ceiling ≤ $68.00** + 4Q post-convert roll-off + `≥8%` ex-client FCF margin |
| **L7** | **`COIN`** | Seed | `A–E` (`FT`) | `$183.00` | `$45.8B` | `-1.3%` (`200DMA $185.41`) | `PH-clear` | `3.5%` / `1.4%` | `-8.5%` (No — cycle peak multiple) | `#9/#10` (`3.5%` rev), `#11` (`PE 179.8`, `PEG 15.72`), `A1` (converts/M&A/SBC), `A3b`, `FT4` | **Tier 3** | **Ceiling ≤ $65.00** (Structural `FT4` / `A1` fail; requires crypto winter reset + SBC halt) |
| **L7** | **`IBKR`** | `[NEW DISCOVERY]` | `A–E` (`FT`) | `$88.15` | `$148.8B` (econ.) / `$39.6B` (Cl A) | `+7.3%` (`200DMA $82.12`) | `PH-clear` | `10.5%` / `12.0%` | `10.2%` (No — NII rate headwind) | `A1` (Up-C share creep), `#9/#10` (`<15%` rev / `<20%` EPS), `FT2/FT3` (segregated cash), `FT4` | **Tier 3** | **Ceiling ≤ $58.00** (`Fwd P/E ≤ 22x` + `A1` freeze + `≥15%` organic commission growth) |
| **L7** | **`TW`** | `[NEW DISCOVERY]` | `A–E` (`FT`) | `$111.08` (`$102.22` 10/2) | `$25.9B` | `+2.6%` (`200DMA $108.28`) | `PH-clear` | `12.1%` / `15.0%` | `14.5%` (Modest — `FT1` bars `#14a`) | `#9` (`12.1% < 15%` `FT1` floor; no `#14a` starter), `#10` (`15.0% < 20%`), `#12` (`PT +13%`, `FCF yld 4.4%`) | **Tier 2** | **Buy ≤ $82.00** (`≥5.0%` FCF yield & `25%+` 3Y IRR) + print guiding `≥15%` organic rev |
| **L7** | **`VIRT`** | `[NEW DISCOVERY]` | `A–E` (`FT`) | `$54.20` | `$8.61B` | `+7.0%` (`200DMA $50.67`) | `PH-clear` | `6.2%` / `8.5%` | `9.5%` (No — VIX/retail burst tied) | `#9/#10` (`6.2%` rev), `FT2/FT3` (broker-dealer trading liab.), `FT4` (PFOF/volatility burst dependency) | **Tier 3** | **Ceiling ≤ $34.00** (Structural `FT4` market-maker exclusion under `fintech.md`) |
| **L7** | **`CME`** | `[NEW DISCOVERY]` | `A–E` (`FT`) | `$285.59` | `$97.5B` | `+4.2%` (`200DMA $274.10`) | `PH-clear` | `7.5%` / `9.2%` | `11.0%` (No — mature compounder) | `#9` (`7.5% < 15%`), `#10` (`9.2% < 20%`), `#11` (`PEG 4.74 > 2.0`), `#12` (`PT +2.6%`, `FCF yld 4.3%`) | **Tier 3** | **Ceiling ≤ $195.00** (Fails `#9/#10` structurally; max 11–13% IRR at current multiple) |
| **L7** | **`CBOE`** | `[NEW DISCOVERY]` | `A–E` (`FT`) | `$304.41` | `$31.5B` | `+5.5%` (`200DMA $288.50`) | `PH-clear` | `8.4%` / `11.5%` | `11.8%` (No — mature exchange) | `#9` (`8.4% < 15%`), `#10` (`11.5% < 20%`), `#11` (`PEG 2.15 > 2.0`), `#12` (`PT +5.5% < 20%`), `FT4` (0DTE vol) | **Tier 3** | **Ceiling ≤ $210.00** (Fails `#9/#10` growth gates under `FT1`) |
| **L7** | **`FUTU`** | `[NEW DISCOVERY]` | `A–E` (`FT`) | `$102.17` | `$14.4B` | **`-22.6%`** (`200DMA $131.94` — **voids `#12` PT**) | `PH-clear` | `12.5%` / `9.3%` | `12.0%` (No — client cash FCF drop) | `#9/#10` (`12.5%` rev / `9.3%` EPS), `A3b/FT2` (FY26E FCF `$1.42B < $5.19B` TTM), `#7` (foreign filer), `FT3/FT4` | **Tier 3** | **Ceiling ≤ $72.00** + reclaim `> -20%` vs 200DMA + `≥15%` organic rev acceleration |
| **L7** | **`ICE`** | `[NEW DISCOVERY]` | `A–E` (`FT`) | `$156.19` | `$87.7B` | `-6.8%` (`200DMA $167.59`) | `PH-clear` | `11.2%` / `10.4%` | `11.5%` (No — levered 10% grower) | `A4` (`Net Debt/FCF = 3.83x > 2.5x`), `#9` (`11.2% < 15%`), `#10` (`10.4% < 20%`), `#12` (`PT +9.8% < 20%`) | **Tier 3** | **Ceiling ≤ $110.00** + debt paydown below `$12.7B` (`≤2.5x` FCF) |
| **L7** | **`NDAQ`** | `[NEW DISCOVERY]` | `A–E` (`FT`) | `$91.96` | `$52.7B` | `+4.3%` (`200DMA $88.20`) | `PH-clear` | `9.8%` / `14.9%` | `14.2%` (No — sub-15% growth) | `A4` (`Net Debt/FCF = 2.67x > 2.5x`), `#9` (`9.8% < 15%`), `#10` (`14.9% < 20%`), `#12` (`PT +18.2%`, `FCF yld 3.7%`) | **Tier 3** | **Ceiling ≤ $68.00** + `~$350M` debt paydown (`≤2.5x` FCF) + EPS CAGR `≥20%` (`#10`) |
| **L7** | **`SCHW`** | `[NEW DISCOVERY]` | `A–E` (`FT`) | `$96.70` | `$163.3B` | `-1.7%` (`200DMA $98.34`) | `PH-clear` | `13.0%` / `22.7%` | `21.5%` (Close — `#10` EPS pass) | **`A7` Hard Fail** (4 officers incl. both Co-Chairmen code-`S` open-market sales Q1/Q3 2026), `FT2/FT3` sweep cash | **Tier 2** | **Buy ≤ $95.00** after **Q3 2027** (`A7` 12-month officer sale roll-off) + clean sweep NIM |
| **L8** | **`RKLB`** | Seed | `H` (fails `A–E/G/H`) | `$59.18` (10/14) | `$39.6B` (econ.) | **`-27.3%`** (`200DMA $81.43` — **voids `#12` PT**) | `PH-clear` | `39.7%` / Neg->Pos | `-18.2%` (No — `H4` ceiling `~$21`) | **`H5` Hard Fail** (`1.33% > 0.5%` net insider sales), `A1` (`$1.94B` ATM + `42.4M` sh IRDM deal), `A3a`, `H4` (`$147.26` hurdle), Neutron 2027 slip | **Tier 3** | **Indicative Ceiling ≤ $21.00** (`H4` 20%/yr 5Y math) + wait until **Jul 7, 2027** (`H5` roll-off) |
| **L8** | **`ASTS`** | Seed | `H-watch` | `$42.14` (10/14) | `$16.4B` (econ.) | **`-47.5%`** (`200DMA $80.28` — **voids `#12` PT**) | `PH-clear` | `>100%` / Neg->Pos | `-5.0%` to `+12%` (Dilution drag) | `#19a` Blackout (Q2 `-8.64%` rev miss), `#17` (`-10.6%` FY27 cut), `H2` (`$1.71B` stressed gap), `H4` (`$104.86` hurdle), `H5`/litigation | **Tier 2** | **Buy ≤ $22.00** after clean Q3 print (`#19a` exit) + non-dilutive Ex-Im/FirstNet `H2` funding |
| **L8** | **`PL`** | `[NEW DISCOVERY]` | `H` (fails `A–E/G/H`) | `$14.13` (10/14) | `$5.51B` | **`-48.1%`** (`200DMA $27.25` — **voids `#12` PT**) | `PH-clear` | `25.9%` / Neg->Pos | `-2.4%` (`H4` 5Y base `$12.51/sh`) | `A1/G3` (`$120M` ATM + `$460M` convert + `+18.2%` WASO), `A3b/G2` (FY27E FCF `-$29.1M`), `#19d` (`-9.9%` Q3 guide miss), `H4` | **Tier 3** | **Indicative Ceiling ≤ $5.03–$8.50** + clean Q3 print + positive FY27 FCF trajectory |
| **L8** | **`LUNR`** | `[NEW DISCOVERY]` | `H` (fails Cap/`A–E/H`) | `$11.02` | `$1.91B` | **`-45.5%`** (`200DMA $20.21` — **voids `#12` PT**) | `PH-clear` | `~35%` / Neg | `-10.0%` (No — dilution & burn) | **Mkt Cap `< $2.5B` floor**, `A1` (heavy equity/warrant dilution), `A3a/G2` (negative FCF), `A4` (`$114.1M` net debt vs neg FCF), `H3/H4` | **Tier 3** | **Ceiling ≤ $5.50** (Also disqualified until Market Cap organically exceeds `$2.5B` without dilution) |
| **L8** | **`RDW`** | `[NEW DISCOVERY]` | `H` (fails `A–E/G/H`) | `$8.62` (`$10.88` 10/2) | `$2.2B–$2.7B` | **`-22.0%`** (`200DMA $11.05` — **voids `#12` PT**) | `PH-clear` | `27.8%` / Neg | `-6.5%` (No — FCF burn & issuance) | `A1/G3` (`$566.2M` equity issuance & preferred conversion), `A3a/G2` (H1 FCF `-$44.9M`, FY26E `-$67.4M`), `H2/H3/H4/H5` unresolved | **Tier 3** | **Ceiling ≤ $4.50** + 4Q post-issuance roll-off + positive FCF conversion |
| **L8** | **`BKSY`** | `[NEW DISCOVERY]` | `H` (fails Cap/`A–E/H`) | `$20.81` | `$0.76B` | **`-24.7%`** (`200DMA $27.64` — **voids `#12` PT**) | `PH-clear` | `~22%` / Neg | `-8.0%` (No — sub-scale & dilutive) | **Mkt Cap `< $2.5B` floor (`$760M`)**, `A1` (equity raises), `A3a/G2` (negative FCF `-$42.5M`), `A4` (`$109.7M` net debt), `H3/H4` | **Tier 3** | **Disqualified (`< $2.5B` Mkt Cap floor)**; fundamental value ceiling `≤ $9.00` |
| **L8** | **`IRDM`** | `[NEW DISCOVERY]` | `A–E` (M&A Target) | `$45.96` | `$5.00B` | `+21.7%` (`200DMA $37.77`) | `PH-clear` | `6.0%` / `8.5%` | `Capped` (Pending RKLB buyout) | **Pending M&A Target** (RKLB acquiring for `$27` cash + `0.40 RKLB` sh); standalone fails `A4` (`Net Debt/FCF = 5.56x > 2.5x`) and `#9` (`6%` rev) | **Tier 3** | **No standalone entry** (Merger arb tied to `RKLB` collar; standalone require `Net Debt/FCF ≤ 2.5x` & `≤ $28`) |
| **L8** | **`MDA.TO`** | `[NEW DISCOVERY]` | `A–E` / `G` | `US$27.45` (`C$40.50`) | `US$4.44B` | `-12.8%` (`200DMA US$31.49`) | `PH-clear` | `28.5%` / `25.0%` | `18.5%` (Dilution & capex drag) | `A1/G3` (`+30.2%` 3Y share count expansion to `~162M` sh), `A3b/A3c` (Telesat/AURORA constellation working-capital & capex swings), `#7` (TSX filer) | **Tier 3** | **Ceiling ≤ US$21.00 (C$31.00)** + 4 consecutive quarters of `≤0.5%` net dilution & `Capex/OCF ≤ 35%` |
| **L8** | **`SATS`** | `[NEW DISCOVERY]` | `H` (Distressed) | `$24.50` | `$6.8B` | `-18.5%` (`200DMA $30.05`) | `PH-warning` | `-4.5%` / Neg | `-25.0%` (No — distressed debt) | `A1` (convertible/spectrum debt-for-equity dilution), `A3a` (`>$1.5B` FCF burn), `A4` (`>$20B` net debt), `#9` (shrinking revenue), `H2/H3/H4` | **Tier 3** | **Uninvestable under framework** (Distressed telecom/satellite balance sheet) |
| **L9** | **`CCJ`** | Seed | `F` (Mandatory) | `$81.50` (`$85.18` 10/2) | `$35.5B` | **`-22.9%`** (`200DMA $105.66` — **voids `#12` PT**) | `PH-clear` | `12.6%` / `28.0%` | `6.5%` (No — `60x–97x` P/E compression) | **`F1` Hard Fail** (`Fwd P/E 59.9x–97x > 15`, `EV/EBITDA 66.4x > 11`, `EBITDA margin ~23% < 30%`, `0` buybacks) & **`F2` Fail** (no insider buy) | **Tier 3** | **Route F Ceiling ≤ $24.00** (`Fwd P/E ≤ 15x`, `EV/EBITDA ≤ 11x`) + `F2` `$2M+` CEO/CFO buy + token buyback |
| **L9** | **`LEU`** | `[NEW DISCOVERY]` | `H-watch` / `A–E` | `$120.00` | `$2.65B` | **`-38.8%`** (`200DMA $196.16` — **voids `#12` PT**) | `PH-clear` | `14.0%` / `-5.0%` | `-8.0%` (No — `174x` EV/EBITDA) | `A1` (ATMs/converts/equity issuance), `A3a/G2` (negative FCF from Piketon HALEU capex), `#11` (`Fwd P/E 48x–59x`, `EV/EBITDA 174x`), `H3/H4` | **Tier 3** | **Ceiling ≤ $48.00** + 4Q halt to ATM dilution + binding commercial HALEU FCF visibility |
| **L9** | **`BWXT`** | `[NEW DISCOVERY]` | `A–E` / `G` | `$138.50` | `$12.8B` | `0.0%` (`200DMA $138.50`) | `PH-clear` | `8.5%` / `12.5%` | `9.8%` (No — `27x` P/E on 12% EPS) | **`A1` Hard Fail** (`$1.1B` convertible senior notes Nov 2025), **`A4` Fail** (`Net Debt $1.4B / FCF ~$200M = 7.0x > 2.5x`), `#9` (`8.5%` rev), `#11` (`PEG 2.22`) | **Tier 3** | **Ceiling ≤ $88.00** + pay down Net Debt below `$550M` (`≤2.5x` FCF) + convert retirement |
| **L9** | **`KAP.L`** | `[NEW DISCOVERY]` | `F` (Mandatory) | `$62.50` | `$16.3B` | `-15.1%` (`200DMA $73.59`) | `PH-clear` | `14.5%` / `16.5%` | `19.5%` (Close — passes `F1` P/E & EBITDA!) | Passes `F1` valuation (`PE 10.8 ≤ 15`, `EV/EBITDA 7.28 ≤ 11`, `EBITDA margin 52%`, `FCF margin 24%`), fails `F1` (`EPS CAGR < 25%`, `0` buybacks) & `F2` | **Tier 2** | **Buy ≤ $52.00** (`≥25%` 3Y IRR incl. ~6% div) + `F2` qualifying insider buy + 1Q token share buyback |
| **L9** | **`NXE`** | `[NEW DISCOVERY]` | `F` (Mandatory) | `$8.50` | `$5.60B` | **`-22.0%`** (`200DMA $10.90` — **voids `#12` PT**) | `PH-clear` | `N/A` (Pre-rev) | `-10.0%` (No — Rook I capex burn) | **`F1` Hard Fail** (Pre-revenue developer, negative FCF/EBITDA, convertible notes & equity dilution, `0` buybacks) & **`F2` Fail** | **Tier 3** | **Uninvestable until Rook I commercial production** + `F1` (`P/E ≤ 15`, `FCF margin ≥ 10%`) + `F2` buy |
| **L9** | **`UEC`** | `[NEW DISCOVERY]` | `F` (Mandatory) | `$8.65` | `$4.05B` | **`-33.1%`** (`200DMA $12.93` — **voids `#12` PT**) | `PH-clear` | `~35%` / Neg | `-12.0%` (No — `-$107M` TTM FCF) | **`F1` Hard Fail** (`TTM FCF -$107M`, negative forward EPS/EBITDA, ATM & stock-settled M&A dilution, `0` buybacks) & **`F2` Fail** | **Tier 3** | **Ceiling ≤ $3.80** once profitable (`F1` `P/E ≤ 15x`, `FCF margin ≥ 10%`, zero ATM dilution, `F2` buy) |
| **L9** | **`UUUU`** | `[NEW DISCOVERY]` | `F` (Mandatory) | `$8.34` (10/14) | `$2.80B` | **`-50.8%`** (`200DMA $16.94` — **voids `#12` PT**) | **`PH-impaired`** | `~25%` / Neg | `-22.0%` (No — massive dilution) | **`PH-impaired`** (`96.45%` below `$235` 2007 ATH), **`F1` Fail** (`FCF -$120.4M`, `$300M` ATM + `$500M` ATM + `80.7M` sh M&A + `$700M` convert), **`F2` Fail** | **Tier 3** | **Hard Disqualified (`PH-impaired` + `F1/F2` fail)**; fundamental ceiling `≤ $2.50` |
| **L9** | **`OKLO`** | `[NEW DISCOVERY]` | `H` (Pre-rev SMR) | `$30.10` | `$5.90B` | **`-47.8%`** (`200DMA $57.61` — **voids `#12` PT**) | `PH-clear` | `N/A` (`$1.2M` TTM) | `-18.0%` (No — pre-rev until 2028) | `H1` Fail (No NRC-licensed operating commercial reactor yet), `A1` (substantial post-SPAC equity dilution), `A3a` (`-$275M` TTM FCF), `H3/H4` | **Tier 3** | **Ceiling ≤ $11.00** after NRC COL approval (`H1`) + binding PPA FCF visibility (`H3/H4`) |
| **L9** | **`SMR`** | `[NEW DISCOVERY]` | `H` (Pre-rev SMR) | `$8.40` | `$2.60B` | **`-28.1%`** (`200DMA $11.68` — **voids `#12` PT**) | `PH-warning` | `N/A` (Pre-commercial) | `-20.0%` (No — `>100%` share dilution) | `H1` Fail (No commercial plant deployed), `A1` (`>100%` YoY share count expansion via ATMs/secondaries), `A3a` (negative FCF), `H3/H4` | **Tier 3** | **Ceiling ≤ $3.25** after binding commercial FID (`H1`) and halt to equity offerings |
| **Excl** | **`NU`** | Bank Exclusion | `Excluded` (`#6`) | `$18.42` | `$89.6B` | `+6.2%` (`200DMA $17.34`) | `PH-clear` | `27.8%` / `29.4%` | `23.5%` (Excluded credit book) | **Explicit `#6` & `fintech.md` Structural Exclusion** (Balance-sheet consumer bank / NIM / credit provisioning; OCF `-$2.75B` distorted by loan originations) | **Excluded** | **Structural Policy Exclusion** (`#6`: No balance-sheet banks/lenders) |
| **Excl** | **`KNSL`** | Insurer Exclusion | `Excluded` (`#6`) | `$364.86` | `$8.45B` | `-11.0%` (`200DMA $410.17`) | `PH-clear` | `13.2%` / `14.8%` | `15.2%` (Excluded + `#9/#10` fail) | **Explicit `#6` Structural Exclusion** (Balance-sheet E&S property/casualty insurer carrying long-tail loss reserve risk); also `<15%` 3Y rev CAGR | **Excluded** | **Structural Policy Exclusion** (`#6`: No balance-sheet insurers) |
| **Excl** | **`KSPI`** | Bank Exclusion | `Excluded` (`#6`) | `$82.10` | `$15.9B` | `-6.3%` (`200DMA $87.64`) | `PH-clear` | `18.5%` / `15.5%` | `18.0%` (Excluded Kazakh bank) | **Explicit `#6` & `fintech.md` Structural Exclusion** (Balance-sheet consumer lending/banking accounts for ~50% of profit) + emerging-market FX/sovereign risk | **Excluded** | **Structural Policy Exclusion** (`#6`: No balance-sheet banks/lenders) |
| **Excl** | **`AXP`** | Card Bank Exclusion | `Excluded` (`#6`) | `$343.39` | `$235.6B` | `+0.9%` (`200DMA $340.36`) | `PH-clear` | `10.1%` / `14.5%` | `13.5%` (Excluded + `#9/#10` fail) | **Explicit `#6` & `fintech.md` Structural Exclusion** (`$200B+` card loan/deposit balance sheet & NII) + fails `#9` (`10.1% < 15%`) & `#10` (`14.5% < 20%`) | **Excluded** | **Structural Policy Exclusion** (`#6`: Closed-loop card bank with balance-sheet credit risk) |
| **Excl** | **`VRT`** | AI-Capex Overlap | `A–E` (`Excluded`) | `$261.97` | `$100.2B` | `+19.1%` (`200DMA $220.00`) | `PH-clear` | `26.6%` / `32.5%` | `17.5%` (`P/E 44.3` compression) | **Mandate Exclusion (Direct AI-Datacenter Capex Pure-Play)** + fails `#11` (`PEG 1.91 > 1.65` HV ceiling; `P/E 44.3 > 38` std ceiling) + `A1` (`+1.0%` WASO) | **Excluded** | **Mandate Exclusion (AI-Capex Overlap)**; under Rev 5 needs `≤ $215.00` (`PEG ≤ 1.65`, `P/E ≤ 38`) |
| **Excl** | **`ETN`** | AI-Grid Overlap | `A–E` (`Excluded`) | `$427.50` | `$158.8B` | `+9.1%` (`200DMA $391.93`) | `PH-clear` | `10.8%` / `13.2%` | `9.8%` (No — `26.7x` P/E on 13% EPS) | **Mandate Exclusion (AI/Electrical Grid Overlap)** + fails `A4` (`Net Debt $20.6B / FCF $3.5B = 5.89x > 2.5x`), `#9/#10` (`10.8%` rev / `13.2%` EPS), `#11` (`PEG 2.05`) | **Excluded** | **Mandate Exclusion** + fails `A4` (`5.89x` leverage), `#9/#10`, and `#11` (`≤ $260.00` fundamental ceiling) |
| **Excl** | **`GEV`** | AI-Power Overlap | `A–E` (`Excluded`) | `$996.80` | `$249.7B` | `+17.3%` (`200DMA $850.00`) | `PH-clear` | `13.5%` / `35.0%` | `19.2%` (`P/E 43x` compression) | **Mandate Exclusion (AI Gas Turbine / Electrification Overlap)** + fails `#11` (`Fwd P/E 38.4x–47.8x > 38` std; `3Y rev 13.5% < 15%` requires `#14a` starter) | **Excluded** | **Mandate Exclusion (AI Power Overlap)**; under Rev 5 qualifies only as `#14a` starter or `≤ $810.00` |
| **Excl** | **`PWR`** | AI-Grid Overlap | `A–E` (`Excluded`) | `$686.00` | `$99.3B` | `+15.3%` (`200DMA $595.00`) | `PH-clear` | `21.5%` / `30.7%` | `18.8%` (`PEG 1.71 > 1.65` HV) | **Mandate Exclusion (AI/Grid EPC Overlap)** + fails `#11` (`PEG 1.71 > 1.65` HV ceiling & `Fwd P/E 39.5x > 38` std), `A1` (`+0.82%` YoY shares from M&A) | **Excluded** | **Mandate Exclusion (AI-Grid Overlap)**; under Rev 5 needs pullback to `≤ $635.00` (`PEG ≤ 1.65`) |

---

## Detailed 8-Point Audit by Lane & Ticker

### LANE 7: Crypto, Retail Brokerage & Electronic Market Infrastructure (Overlay `FT` Applies)

> **Critical Framework Rule (`fintech.md` — `FT1` through `FT4`):**  
> - **`FT1` (Quality-First Entry):** Only Routes `A–E` apply. **Route G, Route H, and `#14a` Starters are strictly prohibited for Fintech/Brokerage/Crypto.** Every candidate must clear the full `#9` growth gate (`≥15%` 3Y Rev CAGR AND `≥15%` next-FY organic growth) or `#10` (`≥20%` 3Y EPS/FCF CAGR + `Wide` moat + `≥7%` rev floor), AND full `#11` valuation (`Fwd P/E ≤ 38`, `PEG ≤ 2.0`, `NTM FCF yield ≥ 1.5%`, or High-Velocity `Fwd P/E ≤ 45`, `PEG ≤ 1.65` if 3Y EPS `≥30%` / Rev `≥25%`).  
> - **`FT2` (Operating Cash vs Client Cash):** Segregated customer cash, sweep deposits, margin payables/receivables, and clearing collateral must be stripped from OCF/FCF and Net Cash.  
> - **`FT3` (Funding & Regulatory):** No reliance on fragile short-term funding or unresolved enforcement threat to core revenue.  
> - **`FT4` (Rate & Retail-Volume Normalization):** The 3Y return thesis cannot depend on crypto/retail-trading volume bursts or Peak NII rate spreads.

---

#### 1. `HOOD` — Robinhood Markets, Inc. (Seed — Route `A–E` + `FT`)
1. **Market Data & Price Health (`PH`):** Price `$101.08` (Oct 15; `$112.74` on Oct 2 sweep), Market Cap `$90.8B`, 200DMA `$94.33` (`+7.2%` above 200DMA; `#12` PT leg remains valid), 3Y/All-Time Closing High `$152.46` (2025-10-09, age 1.0 yr, drawdown `33.7%` Oct 15 / `26.1%` Oct 2). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `21.28%`, Next-FY Organic Rev Growth `~22.5%`, Fwd 3Y EPS CAGR `24.01%`, Net Buyback Yield `-1.2%` (dilutive share creep + convert overhang), Multiple Normalization `-7.0%/yr` (from `39.9x` Fwd P/E to `32.0x` normalized brokerage multiple) = **Est. 3Y Annualized IRR: `15.8%`** (Fails `≥25%` plausibility hurdle without retail options/crypto volume blow-off).
3. **Dilution Gate (`A1`):** **HARD FAIL (`A1`).** Closed **`$2.2B` of `0.00%` convertible senior notes due 2029 on June 25, 2026** (violates `A1` ban on new convertible debt in TTM); diluted shares increased `+1.2%` YoY to `~899M`; SBC is `~9.5%` of revenue (`>40%` of normalized corporate FCF). Also executed Bitstamp/WonderFi M&A.
4. **Capex & FCF Gate (`A3a/b/c`, `FT2–FT4`):** **HARD FAIL (`A3a` / `FT2` / `FT4`).** Reported TTM OCF (`$245M`) and FCF (`$219M`, `4.44%` margin < `8.0%` `A3a` floor) are heavily distorted by customer segregated cash, margin receivables, and securities lending collateral (`FT2`). Fails `FT4` because transaction revenues (options, crypto, equities) and net interest income (margin + cash sweep spreads) are acutely sensitive to retail trading bursts and Fed rate cuts.
5. **Leverage (`A4`) & Moat/Margin (`A5`):** Corporate cash exceeds corporate debt (`$2.2B` 2029 converts), passing `A4` on a corporate-only basis after stripping `$6B+` customer cash/payables (`FT2`). Moat: `Narrow` (retail UX/scale, but low switching costs vs IBKR/SCHW); NTM Gross Margin `~84%` (stable).
6. **Insiders & Legal (`#7` / `A7`):** TTM net insider selling `~0.35%` of shares out (`≤0.5%`, largely `10b5-1` sales by Baiju Bhatt / Vlad Tenev); no 3-officer non-plan cluster (`A7` pass); recurring regulatory/SEC/FINRA scrutiny on crypto/options gamification (`FT3` watch).
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **FAIL (`#11`).** Fwd P/E `39.91x > 38.0x` standard ceiling and PEG `2.14 > 2.00` standard ceiling (does not qualify for High-Velocity `#11` because 3Y Rev `21.28% < 25%` and 3Y EPS `24.01% < 30%`; `#14a` starter barred by `FT1`). Consensus PT `$134.38` (`+32.9%` vs `$101.08`, passing `#12` PT leg). Latest print (`#19`) clean.
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `A1`, `A3a`, `FT2`, `FT4`, `#11`).** **Indicative Buy Trigger:** **≤ $68.00** (`Fwd P/E ≤ 27x`, `PEG ≤ 1.45`) **after June 26, 2027** (4Q roll-off of the June 2026 `$2.2B` convertible note issuance) AND verified corporate ex-client-cash FCF margin `≥8.0%`.

---

#### 2. `COIN` — Coinbase Global, Inc. (Seed — Route `A–E` + `FT`)
1. **Market Data & Price Health (`PH`):** Price `$183.00`, Market Cap `$45.8B`, 200DMA `$182.86–$185.41` (`-1.3%` vs 200DMA; `#12` PT leg valid), 3Y/Lifetime High `$419.78` (2025-07-18, age 1.2 yr, drawdown `56.4%`, 3Y gap `0.0%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `3.49%` (StockAnalysis consensus across FY25–FY28 cycle), Next-FY Organic Rev Growth `~4.0%`, Fwd 3Y EPS CAGR `1.39%`, Net Buyback Yield `-2.1%` (dilutive SBC & convert/M&A issuance), Multiple Normalization `-10.0%/yr` (`Fwd P/E 179.75x` compression) = **Est. 3Y Annualized IRR: `-8.5%`** (Implausible without a new crypto bubble).
3. **Dilution Gate (`A1`):** **HARD FAIL (`A1`).** Multiple tranches of convertible senior notes (`$1.27B` 2026/2028/2030 converts), stock-settled M&A (Deribit `$2.9B` cash+stock deal), and massive SBC (`~$850M–$900M/yr` = `~15%` of `$6.04B` TTM revenue) driving continuous diluted WASO expansion (`+2.5%/yr`).
4. **Capex & FCF Gate (`A3a/b/c`, `FT2–FT4`):** **HARD FAIL (`A3b` / `FT2` / `FT4`).** TTM Net Income is `-$987.8M` (with `$699.6M` EBITDA); reported operating cash flow is heavily swung by custodial/USDC client cash flows (`FT2`), NTM FCF is projected below prior-cycle TTM peaks (`A3b` fail), and earnings are 100% hostage to spot crypto volume and USDC interest-rate spreads (`FT4` hard fail).
5. **Leverage (`A4`) & Moat/Margin (`A5`):** Corporate cash `$8.79B` vs total debt `$6.67B` (`$2.12B` net cash ex-client custodial assets, passing `A4`). Moat: `Narrow` (US institutional custody & Base L2, but retail fee compression pressure); NTM GM `~85%`.
6. **Insiders & Legal (`#7` / `A7`):** Persistent insider selling by CEO Brian Armstrong and officers (`~0.40%` TTM via `10b5-1`); ongoing SEC/regulatory litigation over staking/unregistered securities (`FT3` fail).
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#9`, `#10`, `#11`, `#12`).** Fwd P/E `179.75x` (vs `≤38x` limit), PEG `15.72` (vs `≤2.0` limit), 3Y Rev CAGR `3.49%` (vs `≥15%` `FT1` floor). Consensus PT `$205.00–$224.44` (`+12%` to `+22.6%`, borderline `#12`).
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `#9`, `#10`, `#11`, `A1`, `A3b`, `FT2`, `FT3`, `FT4`).** **Indicative Buy Trigger:** Structurally excluded by `FT4` (crypto cycle dependency); would require **≤ $65.00**, net share count reduction (`A1`), and recurring non-trading subscription FCF `>75%` of total FCF.

---

#### 3. `IBKR` — Interactive Brokers Group, Inc. (`[NEW DISCOVERY]` — Route `A–E` + `FT`)
1. **Market Data & Price Health (`PH`):** Price `$88.15`, Market Cap `$148.8B` total economic (`~1.70B` IBG LLC shares; `$39.64B` Class A public float), 200DMA `$82.12` (`+7.3%` above 200DMA), 3Y High `~$96.50` (drawdown `~8.7%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `~10.5%` (TTM Rev `$6.84B`; commission growth `+18%` offset by modeled Fed rate cuts on `$4.5B+` NII), Next-FY Organic Rev Growth `~9.5%`, Fwd 3Y EPS CAGR `~12.0%`, Net Buyback Yield `-0.8%` (IBG Holdings Up-C exchange creep), Multiple Normalization `-1.0%/yr` (`Fwd P/E 35.0x` -> `34.0x`) = **Est. 3Y Annualized IRR: `10.2%`** (Well below `25%` target).
3. **Dilution Gate (`A1`):** **FAIL (`A1`).** Confirmed in the Oct 2 repository sweep (`fintech.md`): Class A share count expands YoY via Up-C redemptions/exchanges and employee Stock Incentive Plan grants without offsetting buybacks (`0` share repurchases).
4. **Capex & FCF Gate (`A3a/b/c`, `FT2–FT4`):** **FAIL (`FT2` / `FT4`).** Under `FT2`, IBKR's GAAP OCF (`$5B+`) is dominated by `$100B+` of segregated client cash, margin loans, and securities lending payables/receivables; normalized corporate after-tax earnings/FCF is `~$3.8B` (`~55%` margin), which is high quality, **but fails `FT4`** because `>60%` of revenue/pre-tax profit is Net Interest Income (NII) on client cash sweeps and margin balances exposed to benchmark rate cuts.
5. **Leverage (`A4`) & Moat/Margin (`A5`):** Zero corporate long-term debt (`$15B+` firm equity capital cushion, `A4` pass). Moat: `Wide` (lowest-cost global automated execution/margin platform; `~71%` pre-tax margin).
6. **Insiders & Legal (`#7` / `A7`):** Founder Thomas Peterffy (`~75%` economic owner via IBG Holdings) executes scheduled `10b5-1` Rule 144 sales (`<0.5%` of total economic shares); no `A7` violation; clean legal RPL.
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **FAIL (`#9`, `#10`, `#11` PEG, `#12`).** Fwd P/E `35.04x ≤ 38x`, but PEG `~2.92 > 2.00` (`35.04 / 12.0`); 3Y Rev CAGR `~10.5% < 15%` (`#9` fail under `FT1`) and 3Y EPS CAGR `~12.0% < 20%` (`#10` fail). Consensus PT `$103.18–$105.19` (`+17.1%` to `+19.3% < 20%`, failing `#12` as NTM corporate FCF yield is `~2.6% < 5.0%`).
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `A1`, `#9`, `#10`, `#11` PEG, `#12`, `FT4`).** **Indicative Buy Trigger:** **≤ $58.00** (`Fwd P/E ≤ 22x`, `≥20%` PT upside) + stabilization of post-rate-cut NII allowing `≥15%` organic revenue growth.

---

#### 4. `TW` — Tradeweb Markets Inc. (`[NEW DISCOVERY]` — Route `A–E` + `FT`)
1. **Market Data & Price Health (`PH`):** Price `$111.08` (Oct 15; `$102.22` Oct 2 sweep), Market Cap `$25.9B` (`$23.7B` Oct 2), 200DMA `$108.28` (`+2.6%` Oct 15 / `-5.6%` Oct 2), 3Y/Lifetime High `$149.02` (2025-04-03, age 1.5 yr, drawdown `25.5%` Oct 15 / `31.4%` Oct 2). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `12.14%` (`11.73%` on Oct 2 sweep), Next-FY Organic Rev Growth `~12.5%`, Fwd 3Y EPS CAGR `14.96%` (`14.30%` on Oct 2), Net Buyback Yield `-0.13%` (essentially flat shares + `0.4%` dividend), Multiple Normalization `0.0%/yr` (`Fwd P/E 25.51x`) = **Est. 3Y Annualized IRR: `14.5%`–`15.2%`** at `$111.08` (Requires entry at `≤$82.00` for `25%+` 3Y IRR).
3. **Dilution Gate (`A1`):** **PASS (`A1`).** YoY diluted share count change is `+0.13%` (`≤0.5%` threshold); SBC is modest (`~6%` of revenue) and offset by share buybacks; no convertible notes, ATMs, or dilutive equity offerings in TTM.
4. **Capex & FCF Gate (`A3a/b/c`, `FT2–FT4`):** **PASS (`A3a/b/c`, `FT2–FT4`).** TTM Company FCF is **`$1.14B`** (`~51%` FCF margin ≥ `8%`), NTM FCF `~$1.22B > TTM FCF` (`A3b` pass), Capex/OCF `<8%` (`A3c` pass). Unlike retail brokers, TW is an institutional fixed-income/rates/credit electronic marketplace with zero client sweep deposits (`FT2/FT3` clean) and secular electronification tailwinds across all rate regimes (`FT4` pass).
5. **Leverage (`A4`) & Moat/Margin (`A5`):** **PASS (`A4`, `A5`).** Net Cash **`$1.91B`** (`$2.00B` cash vs `$93.6M` lease debt; `Net Debt/FCF = -1.68x ≤ 2.5x`). Moat: `Wide` (institutional liquidity network effects in US Treasuries, IRS, ETFs, and credit); NTM Gross Margin `~94%` (expanding).
6. **Insiders & Legal (`#7` / `A7`):** **PASS (`#7` / `A7`).** Controlled by LSEG (`~51%` voting stake); officer Form 4 net selling `<0.15%` of shares out; zero `A7` cluster; clean legal RPL.
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **PASS (`#11`), FAIL (`#9` / `#10` under `FT1`, `#12`).** Fwd P/E `25.51x ≤ 38.0x`, PEG `1.62 ≤ 2.00`, NTM FCF yield `4.4% ≥ 1.5%`. **However**, `FT1` prohibits `#14a` starters (which would otherwise allow `≥12%` 3Y rev CAGR), so TW fails `#9` (`12.14% < 15.0%` 3Y Rev CAGR) and `#10` (`14.96% < 20.0%` 3Y EPS CAGR). At `$111.08`, consensus PT `$125.53` is `+13.0% < 20%` and FCF yield is `4.4% < 5.0%` (`#12` fail at Oct 15 price, though `+22.8%` at Oct 2 `$102.22`).
8. **Final Tier & Buy Trigger:** **Tier 2 (Near-Pass Watchlist — Best-in-Class Institutional Market Infrastructure).** **Exact Dollar Buy Trigger:** **≤ $82.00** (unlocks `≥5.0%` NTM FCF yield to pass `#12` unconditionally and `25.4%` 3Y IRR via re-rating to `26x` P/E) **PLUS** a quarterly print guiding organic revenue growth to `≥15.0%` (`#9`) or NTM 3Y EPS CAGR to `≥20.0%` (`#10`).

---

#### 5. `VIRT` — Virtu Financial, Inc. (`[NEW DISCOVERY]` — Route `A–E` + `FT`)
1. **Market Data & Price Health (`PH`):** Price `$54.20`, Market Cap `$8.61B`, 200DMA `$50.67` (`+7.0%` above 200DMA), 3Y High `~$57.50` (drawdown `~5.7%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `~6.2%` (TTM Rev `$3.26B`), Next-FY Organic Rev Growth `~5.0%`, Fwd 3Y EPS CAGR `~8.5%` (TTM Net Income `$518.2M`, EPS `$6.03`), Net Buyback Yield `+3.5%` (plus `~3.0%` div), Multiple Normalization `-2.5%/yr` = **Est. 3Y Annualized IRR: `9.5%`**.
3. **Dilution Gate (`A1`):** **PASS (`A1`).** Active net share cannibal (`-3.5%/yr` YoY share count reduction via buybacks); low SBC (`<3%` of revenue).
4. **Capex & FCF Gate (`A3a/b/c`, `FT2–FT4`):** **HARD FAIL (`FT2` / `FT3` / `FT4`).** As a principal high-frequency market maker, Virtu carries `$21B+` of gross trading assets/cash against `$19B+` of short-term broker-dealer trading liabilities, repo lines, and securities loaned (`FT2/FT3`), and its net trading revenue is structurally dependent on retail order-flow (PFOF) and volatility bursts (`FT4` hard fail).
5. **Leverage (`A4`) & Moat/Margin (`A5`):** Corporate long-term debt `~$1.8B` vs `~$518M` normalized earnings (`~3.47x > 2.5x`, failing `A4` even before trading liabilities). Moat: `Narrow` (scale in HFT/execution, but zero recurring revenue visibility).
6. **Insiders & Legal (`#7` / `A7`):** Insider selling `<0.3%` (`#7/A7` pass); ongoing SEC market-structure/PFOF rule-making exposure.
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **FAIL (`#9`, `#10`).** Fwd P/E `~9.5x`, PEG `~1.12`, PT `$63.60–$71.40` (`+17%` to `+31%`), but fails `#9` (`6.2% < 15%` 3Y Rev CAGR) and `#10` (`8.5% < 20%` 3Y EPS CAGR and lacks `Wide` moat).
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `#9`, `#10`, `A4`, `FT2`, `FT3`, `FT4`).** **Indicative Ceiling:** **≤ $34.00** (Structurally excluded under `FT4` principal market-making volatility dependency).

---

#### 6. `CME` — CME Group Inc. (`[NEW DISCOVERY]` — Route `A–E` + `FT`)
1. **Market Data & Price Health (`PH`):** Price `$285.59`, Market Cap `$97.5B`, 200DMA `$274.10` (`+4.2%` above 200DMA), 3Y/Lifetime High `~$295.00` (drawdown `~3.2%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `7.5%`, Next-FY Organic Rev Growth `~7.0%`, Fwd 3Y EPS CAGR `9.2%`, Dividend/Return Yield `+3.8%` (regular + variable annual dividend; `0%` buyback), Multiple Normalization `-2.0%/yr` (`Fwd P/E 23.4x` -> `22.0x`) = **Est. 3Y Annualized IRR: `11.0%`** (Mature defensive monopoly; cannot reach `25%` IRR).
3. **Dilution Gate (`A1`):** **PASS (`A1`).** Share count virtually unchanged (`+0.1%` YoY; `360.5M` shares); SBC `<2%` of revenue (`<3%` of FCF).
4. **Capex & FCF Gate (`A3a/b/c`, `FT2–FT4`):** **PASS (`A3a/b/c`, `FT2–FT4`).** TTM Company FCF **`$4.21B`** (`~62%` FCF margin ex-clearinghouse performance bonds under `FT2`), NTM FCF `~$4.45B > TTM`, Capex `<3%` of OCF (`~$90M`). Passes `FT4` (interest-rate, Treasury, energy, and equity futures clearing thrives in both rate hikes and rate cuts).
5. **Leverage (`A4`) & Moat/Margin (`A5`):** **PASS (`A4`, `A5`).** Corporate Net Debt **`$1.59B`** (`$3.4B` debt vs `$1.8B` corporate cash; `Net Debt/FCF = 0.38x ≤ 2.5x`). Moat: `Wide` (unassailable clearinghouse open-interest monopoly in SOFR/Treasury/S&P futures); NTM GM `~88%`.
6. **Insiders & Legal (`#7` / `A7`):** **PASS (`#7` / `A7`).** TTM net insider sales `<0.05%` of shares out; clean legal RPL.
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#9`, `#10`, `#11` PEG, `#12`).** Fwd P/E `23.4x ≤ 38x`, **but PEG `4.74 > 2.00` (`#11` fail)**; 3Y Rev CAGR `7.5% < 15%` (`#9` fail) and 3Y EPS CAGR `9.2% < 20%` (`#10` fail). Consensus PT `$292.94` (`+2.6% < 20%`) and NTM FCF yield `4.3% < 5.0%` (**fails both legs of `#12`**).
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `#9`, `#10`, `#11` PEG, `#12`).** **Indicative Ceiling:** **≤ $195.00** (Even at `$195`, 3Y EPS CAGR `9.2% < 20%` fails `#9/#10` under `FT1`).

---

#### 7. `CBOE` — Cboe Global Markets, Inc. (`[NEW DISCOVERY]` — Route `A–E` + `FT`)
1. **Market Data & Price Health (`PH`):** Price `$304.41`, Market Cap `$31.47B`, 200DMA `$288.50` (`+5.5%` above 200DMA), 3Y/Lifetime High `~$312.00` (drawdown `~2.4%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `8.4%`, Next-FY Organic Rev Growth `~8.0%`, Fwd 3Y EPS CAGR `11.5%`, Net Buyback + Div Yield `+1.8%`, Multiple Normalization `-1.5%/yr` (`Fwd P/E 22.8x` -> `21.8x`) = **Est. 3Y Annualized IRR: `11.8%`**.
3. **Dilution Gate (`A1`):** **PASS (`A1`).** Share count `-0.4%` YoY via steady buybacks; SBC `<2.5%` of net revenue; no converts or equity offerings.
4. **Capex & FCF Gate (`A3a/b/c`, `FT2–FT4`):** **PASS (`A3a/b/c`), WATCH (`FT4`).** TTM Company FCF **`$1.87B`** (`~45%` of net transaction/data revenue), NTM FCF `ge TTM`, Capex `<5%` of OCF. Watch on `FT4` due to heavy concentration in SPX/VIX 0DTE retail options volume.
5. **Leverage (`A4`) & Moat/Margin (`A5`):** **PASS (`A4`, `A5`).** Net Cash **`$774.2M`** (`Net Debt/FCF = -0.41x ≤ 2.5x`). Moat: `Wide` (exclusive SPX and VIX index options licensing moat).
6. **Insiders & Legal (`#7` / `A7`):** **PASS (`#7` / `A7`).** Minimal insider selling (`<0.10%`); clean legal RPL.
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#9`, `#10`, `#11` PEG, `#12`).** Fwd P/E `21.0x–23.0x ≤ 38x`, **but PEG `2.15 > 2.00` (`#11` fail)**; 3Y Rev CAGR `8.4% < 15%` (`#9` fail) and 3Y EPS CAGR `11.5% < 20%` (`#10` fail). Consensus PT `$321.18–$322.33` (`+5.5% < 20%`, failing `#12` PT leg).
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `#9`, `#10`, `#11` PEG, `#12`).** **Indicative Ceiling:** **≤ $210.00** (Structural slow-growth exchange compounder; fails `#9/#10` under `FT1`).

---

#### 8. `FUTU` — Futu Holdings Limited (`[NEW DISCOVERY]` — Route `A–E` + `FT`)
1. **Market Data & Price Health (`PH`):** Price `$102.17` (Oct 2 sweep; `$112.26` Oct 15), Market Cap `$14.4B–$15.8B`, 200DMA `$131.94` (**`-22.6%` below 200DMA on Oct 2 / `-14.9%` on Oct 15 — at `>20%` below 200DMA, `#12` PT leg is voided!**), 3Y/Lifetime High `$199.04` (2025-10-31, age 0.9 yr, drawdown `48.7%`, 3Y gap `0.0%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `12.53%` (verified Oct 2 StockAnalysis sweep), Next-FY Organic Rev Growth `~13.0%`, Fwd 3Y EPS CAGR `9.29%` (pressured by lower HIBOR/Fed rate spreads on client cash), Net Buyback Yield `+0.5%`, Multiple Normalization `+2.2%/yr` (`Fwd P/E 11.2x` -> `12.0x`) = **Est. 3Y Annualized IRR: `12.0%`**.
3. **Dilution Gate (`A1`):** **PASS (`A1`).** Share count slightly down YoY (`-0.5%`) via ADR buyback authorization; low SBC (`<3%` of revenue).
4. **Capex & FCF Gate (`A3a/b/c`, `FT2–FT4`):** **HARD FAIL (`A3b` / `FT2` / `FT3` / `FT4`).** Verified in `fintech.md` (Oct 2 sweep): TTM reported FCF (`$5.19B` USD) is artificially inflated by segregated client cash inflows (`FT2`), while consensus FY26E normalized FCF drops to `HK$11.1B` (`~$1.42B` USD < TTM, failing `A3b`). Also fails `FT3` (CSRC/mainland China cross-border brokerage regulatory risk) and `FT4` (HK/US retail momentum trading & HIBOR margin/cash spread sensitivity).
5. **Leverage (`A4`) & Moat/Margin (`A5`):** Corporate balance sheet is net cash ex-client margin loans/payables (`A4` pass). Moat: `Narrow` (leading HK/Singapore retail app Moomoo/Futubull, but subject to regulatory & commission competition); NTM GM `~81%`.
6. **Insiders & Legal (`#7` / `A7`):** **FAIL (`#7` Foreign Filer Blind Spot).** Cayman/HK foreign private issuer exempt from real-time SEC Form 4 officer reporting; CSRC cross-border regulatory overhang (`FT3`).
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **FAIL (`#9`, `#10`).** Fwd P/E `11.1x–11.5x ≤ 38x`, PEG `~1.20 ≤ 2.0`, PT `$145.00` (`+41.9%`), **but fails `#9` (`12.53% < 15.0%` 3Y Rev CAGR under `FT1`) and `#10` (`9.29% < 20.0%` 3Y EPS CAGR)**.
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `#9`, `#10`, `A3b`, `FT2`, `FT3`, `FT4`, `#7`).** **Indicative Ceiling:** **≤ $72.00** + sustained reclaim above `$106` (`-20%` vs 200DMA) + `≥15%` organic revenue growth.

---

#### 9. `ICE` — Intercontinental Exchange, Inc. (`[NEW DISCOVERY]` — Route `A–E` + `FT`)
1. **Market Data & Price Health (`PH`):** Price `$156.19`, Market Cap `$87.68B`, 200DMA `$167.59` (`-6.8%` below 200DMA; `#12` PT leg valid), 3Y/Lifetime High `~$178.00` (drawdown `~12.3%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `11.2%`, Next-FY Organic Rev Growth `~8.5%`, Fwd 3Y EPS CAGR `10.4%`, Net Buyback + Div Yield `+1.2%` (buybacks paused/reduced for Black Knight debt deleveraging), Multiple Normalization `0.0%/yr` (`Fwd P/E 17.8x`) = **Est. 3Y Annualized IRR: `11.6%`**.
3. **Dilution Gate (`A1`):** **PASS (`A1`).** Share count `+0.2%` YoY (`~561M` shares; post-Black Knight M&A shares now past 12-month window); SBC `<3%` of revenue.
4. **Capex & FCF Gate (`A3a/b/c`, `FT2–FT4`):** **PASS (`A3a/b/c`, `FT2–FT4`).** TTM Company FCF **`$5.08B`** (`~52%` of net revenue ex-clearing margin), NTM FCF `~$5.35B > TTM`, Capex `<6%` of OCF. Diversified across Brent/TTF energy futures, NYSE, fixed-income data, and mortgage tech (`FT4` pass).
5. **Leverage (`A4`) & Moat/Margin (`A5`):** **HARD FAIL (`A4`).** Post-Black Knight acquisition, Net Debt is **`$19.46B`** against `$5.08B` TTM FCF (`~$5.35B` NTM FCF) = **`3.64x–3.83x Net Debt / FCF > 2.50x` hard ceiling**. Moat: `Wide` (energy futures clearing & mortgage software network effects); NTM GM `~78%`.
6. **Insiders & Legal (`#7` / `A7`):** **PASS (`#7` / `A7`).** CEO Jeffrey Sprecher `10b5-1` sales `<0.15%` of shares out; clean legal RPL.
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#9`, `#10`, `#12`).** Passes `#11` (`Fwd P/E 17.5x–18.0x ≤ 38x`, `PEG 0.62–1.70 ≤ 2.0`), **but fails `#9` (`11.2% < 15.0%` 3Y Rev CAGR under `FT1`), fails `#10` (`10.4% < 20.0%` 3Y EPS CAGR), and fails `#12`** (Consensus PT `$168.00–$175.00` = `+7.6%` to `+12.0% < 20%`).
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `A4`, `#9`, `#10`, `#12`).** **Indicative Ceiling:** **≤ $110.00** + `$6.1B` debt paydown to bring `Net Debt/NTM FCF ≤ 2.50x`.

---

#### 10. `NDAQ` — Nasdaq, Inc. (`[NEW DISCOVERY]` — Route `A–E` + `FT`)
1. **Market Data & Price Health (`PH`):** Price `$91.96`, Market Cap `$52.7B` (`558.98M` diluted shares), 200DMA `$88.20` (`+4.3%` above 200DMA), 3Y/Lifetime High `~$95.50` (drawdown `~3.7%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `9.8%`, Next-FY Organic Rev Growth `~9.0%`, Fwd 3Y EPS CAGR `14.9%`, Net Buyback + Div Yield `+1.3%` (deleveraging post-Adenza), Multiple Normalization `-2.0%/yr` (`Fwd P/E 21.16x` -> `19.8x`) = **Est. 3Y Annualized IRR: `14.2%`**.
3. **Dilution Gate (`A1`):** **PASS (`A1`).** Adenza acquisition (`$10.5B` cash + `85.6M` shares to Thoma Bravo) closed Nov 2024 (outside TTM window); TTM share count `-0.6%` YoY via buybacks; SBC `<4%` of net revenue.
4. **Capex & FCF Gate (`A3a/b/c`, `FT2–FT4`):** **PASS (`A3a/b/c`, `FT2–FT4`).** TTM Company FCF **`$1.95B`** (`~41%` of net revenue), NTM FCF `~$2.10B > TTM`, Capex `<6%` of OCF (`~$130M`). Over `75%` of revenue is recurring FinTech/RegTech (Verafin, AxiomSL, Calypso) and Index/Data (`FT4` pass).
5. **Leverage (`A4`) & Moat/Margin (`A5`):** **FAIL (`A4`).** Net Debt **`$5.20B`** vs `$1.95B` TTM FCF = **`2.67x > 2.50x` (`~2.48x` on `$2.10B` NTM FCF — right on the `2.50x` knife-edge)**. Moat: `Wide` (US equity/options listing duopoly + RegTech switching costs); NTM GM `~72%`.
6. **Insiders & Legal (`#7` / `A7`):** **PASS (`#7` / `A7`).** Officer net sales `<0.10%` of shares out; Thoma Bravo lock-up orderly; clean legal RPL.
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#9`, `#10`, `#12`).** Passes `#11` (`Fwd P/E 21.16x ≤ 38x`, `PEG 1.76 ≤ 2.0`, `EV/FCF 31.23x` = `3.2%` yield), **but fails `#9` (`9.8% < 15.0%` 3Y Rev CAGR under `FT1`), fails `#10` (`14.9% < 20.0%` 3Y EPS CAGR), and fails `#12`** (Consensus PT `$108.69` = `+18.2% < 20.0%`, and NTM FCF yield `3.7% < 5.0%`).
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `A4`, `#9`, `#10`, `#12`).** **Indicative Ceiling:** **≤ $68.00** + `$350M` debt paydown (`Net Debt/FCF ≤ 2.5x`) + acceleration of FinTech/Adenza cross-sell to `≥20%` EPS CAGR (`#10`).

---

#### 11. `SCHW` — The Charles Schwab Corporation (`[NEW DISCOVERY]` — Route `A–E` + `FT`)
1. **Market Data & Price Health (`PH`):** Price `$96.70` (Oct 2 sweep; `$95.94` Oct 15), Market Cap `$163.3B`, 200DMA `$98.34` (`-1.7%` below 200DMA; `#12` PT leg valid), 3Y/Lifetime High `$113.65` (2026-08-24, age 0.1 yr, drawdown `14.9%`, 3Y gap `0.0%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `12.96%` (verified Oct 2 StockAnalysis sweep), Next-FY Organic Rev Growth `~13.5%`, Fwd 3Y EPS CAGR `22.72%` (**clears `#10` `≥20%` EPS CAGR hurdle as high-cost Bank Supplemental Funding is paid off!**), Net Buyback + Div Yield `+2.3%`, Multiple Normalization `-3.5%/yr` (`Fwd P/E 14.9x` -> `13.5x`) = **Est. 3Y Annualized IRR: `21.5%`** at `$96.70` (**`25.2%` at `≤$88.00`**).
3. **Dilution Gate (`A1`):** **PASS (`A1`).** Share count `-0.8%` YoY (`~1.70B` diluted shares; resumed share buybacks after paying down FHLB/retail CD advances); SBC `<3%` of revenue.
4. **Capex & FCF Gate (`A3a/b/c`, `FT2–FT4`):** **WATCH (`FT2` / `FT3`).** Normalized corporate free cash flow is `$7.8B+` (`~32%` margin, `A3a/b/c` pass), **but `FT2` and `FT3` require caution** because ~50% of revenue is Schwab Bank Net Interest Income earned on client sweep cash (`~$400B` bank deposits), which experienced client cash-sorting and HTM bond unrealized losses in 2023–2024.
5. **Leverage (`A4`) & Moat/Margin (`A5`):** Corporate parent debt is modest relative to `$7.8B` normalized cash earnings (`A4` pass ex-bank deposits), and Moat is `Wide` (`$10T+` client assets, lowest-cost custodial/RIA platform).
6. **Insiders & Legal (`#7` / `A7`):** **HARD FAIL (`A7`).** Verified directly in the Oct 2 repository sweep (`fintech.md`): **Four named executive officers — including both Co-Chairmen (Charles Schwab and Walter Bettinger) — executed open-market code-`S` discretionary sales outside `10b5-1` plans in Q1 2026 and Q3 2026**, violating the `A7` 3-officer discretionary selling rule (`≥3` officers selling outside `10b5-1` within 12 months).
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **PASS (`#10`, `#11`, `#12`).** Clears `#10` growth exception (`3Y EPS CAGR 22.72% ≥ 20%`, `3Y Rev 12.96% ≥ 7%`, `Wide` moat), clears `#11` (`Fwd P/E 14.9x ≤ 38x`, `PEG 1.35 ≤ 2.0`), and clears `#12` (`Consensus PT $121.86` = `+26.0% ≥ 20%`).
8. **Final Tier & Buy Trigger:** **Tier 2 (Near-Pass Watchlist — Blocked by `A7` Discretionary Officer Cluster).** **Exact Dollar Buy Trigger:** **≤ $88.00–$95.00** **after Q3 2027** (when the Q1/Q3 2026 non-`10b5-1` officer sales roll off the trailing 12-month `A7` window).

---

### LANE 8: Space Launch, Direct-to-Device & Defense Space Systems (Routes `A–E`, `G`, or `H`)

> **Critical Framework Rule (`stage-paths.md` — Routes `G` & `H`):**  
> - **Route G (Capital-Intensive Compounder):** Requires TTM FCF margin `≥6%`, two positive OCF FYs, NTM FCF `≥90%` of TTM, Capex `≤50%` of NTM OCF, Net Debt/NTM FCF `≤2.5x`, next-FY & 3Y organic rev `≥10%`, 3Y FCF/sh CAGR `≥12%`, `G3` ordinary dilution `≤3%` (no ATMs/converts), `G5` 5Y base return `≥12%/yr` & bear `≥60%` of entry.  
> - **Route H (Exceptional Commercial-Transition Exception):** Requires `H1` achieved commercial product + binding commercial demand, `H2` 24-month stressed funding + `25%` buffer without new equity, `H3` fixed `≤5Y` quality destination (`FCF margin ≥8%`, `Capex ≤35% OCF`, `Net Debt/FCF ≤2.5x`, `≤0.5%` dilution), `H4` `≥20%/yr` 5Y base return (`2.488x` entry price) after explicit dilution/capex & `≥50%` bear floor, and `H5` annual net insider sales `≤0.50%` of shares out & no `<3 officer` cluster.

---

#### 1. `RKLB` — Rocket Lab Corporation (Seed — Route `A–E` / `G` / `H`)
1. **Market Data & Price Health (`PH`):** Price `$59.18` (Oct 14 close; `$65.91` Oct 2), Market Cap **`$39.56B` economic** (`668.43M` economic diluted shares including `29.3M` Sep 15 ATM shares + `~42.4M` Iridium M&A collar shares; `$35.3B` basic on `596.4M` sh), 200DMA `$81.43` (**`-27.3%` below 200DMA — `>20%` below voids `#12` PT leg!**), 3Y/Lifetime High `$150.23` (2026-05-27, age 0.4 yr, drawdown `60.6%`, 3Y gap `0.0%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `39.71%` (`$602M` FY25 -> `$1.64B` FY28E standalone, or `$2.5B+` pro forma with Iridium), Next-FY Organic Rev Growth `~36.0%`, Fwd 3Y EPS/FCF CAGR `Neg -> Pos`, Net Buyback Yield `-8.5%/yr` (ATM + Iridium stock issuance + SBC), Multiple Normalization `-28.0%/yr` (`~24x` EV/Sales compression) = **Est. 3Y Annualized IRR: `-18.2%`** (Verified in commit `3914533`: under `H4`, a `20%/yr` 5Y return from `$59.18` requires **`$147.26/sh`** in Year 5 = **`$108.97B`** Mkt Cap on `740M` shares = **`$4.36B` FCF at 25x** vs plausible `$660M` pro forma FCF = `-18.2%/yr`).
3. **Dilution Gate (`A1`, `G3`, `H3/H4`):** **HARD FAIL (`A1`, `G3`, `H3`).** Completed **`$1.944B` ATM equity offering (`29.3M` shares at `~$66.35` closed Sep 15, 2026)** + announced **Iridium (`IRDM`) acquisition on Jun 28, 2026** issuing **`~42.4M` RKLB shares** (`0.40 RKLB` per IRDM share below `$67.50` collar) plus `$2.861B` cash and assuming `$1.775B` guaranteed term loan. YoY share count `+19.3%` before Iridium (`+27.8%` pro forma).
4. **Capex & FCF Gate (`A3a/b/c`, `G2`, `H1/H2/H3`):** **HARD FAIL (`A3a`, `G2`, `H3`).** TTM Company FCF is **`-$325.6M`** (`OCF -$166.0M` minus `$159.6M` capex = `-46.2%` margin on `$704.9M` TTM rev; FY26E FCF `-$398.3M`, FY27E FCF `-$256.8M`). Furthermore, **on Oct 14, 2026 after-close (Form 8-K), RKLB announced Neutron's first launch slipped from Q4 2026 into 2027** due to Stage 2 carbon-composite tank-dome laminate voids (`H1/H3` setback).
5. **Leverage (`A4`) & Moat/Margin (`A5`):** Pre-deal cash `~$2.78B` (after Sep ATM) vs `$137M` debt, **but pro forma for the Iridium buyout (`$2.861B` cash out + `$1.775B` debt assumed), pro forma Net Debt is `~$1.99B`** (`A4` fail while RKLB standalone FCF is negative). Moat: `Narrow` (Electron small-launch leader & SDA prime space systems; Neutron unproven); TTM GM `34.4%`.
6. **Insiders & Legal (`#7` / `A7` / `H5`):** **HARD FAIL (`#7` / `A7` / `H5`).** Directly verified from 62 Form 4s in commit `3914533`: trailing 12-month open-market insider sales = **`8,880,247` shares sold / `0` bought = `1.489%` of basic shares (`1.3285%` of `668.43M` economic shares) > `0.50%` hard cap!** CEO Peter Beck sold `5,810,722` shares (`0.87%` alone, Dec 15, 2025 & Jul 6, 2026), CFO Adam Spice sold `1,865,653` shares (Jan 5, 2026), COO Frank Klein sold `100,000` shares. **Roll-off date: ~July 7, 2027.**
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#11`, `#12`, `H4`).** Negative FCF & EPS through FY27E; `>20%` below 200DMA voids `#12` PT leg (`$98.12` consensus PT voided); Oct 14 8-K Neutron delay to 2027 creates event/estimate revision risk (`#17/#19`).
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `H5`, `A1/G3`, `A3a/G2`, `H3`, `H4`, `#12`).** **Indicative Ceiling:** **≤ $21.00** (per commit `3914533` `H4` 20%/yr 5Y model on `$660M` FY30 pro forma FCF at 25x across `740M` shares) **AND after July 7, 2027** (`H5` insider sale roll-off) + successful Neutron orbital flight (`H1`).

---

#### 2. `ASTS` — AST SpaceMobile, Inc. (Seed — Route `H-watch`)
1. **Market Data & Price Health (`PH`):** Price `$42.14` (Oct 14 close; `$65.34` Oct 2), Market Cap **`$16.40B` economic** (`389.11M` economic shares across Class A/B/C + LLC units; `$12.23B` public float), 200DMA `$80.28` (**`-47.5%` below 200DMA — voids `#12` PT leg!**), 3Y/Lifetime High `$133.09` (2026-05-28, age 0.4 yr, drawdown `68.3%`, 3Y gap `0.0%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `>100%` (from `$57.5M` TTM to `$581.7M` FY27E and `$1.4B+` FY28E), Next-FY Organic Rev Growth `>150%`, Fwd 3Y EPS/FCF CAGR `Neg -> Pos`, Net Buyback Yield `-6.0%/yr` (converts/ATM dilution to fund 45–60 Block 2 BlueBird satellites), Multiple Normalization `-15.0%/yr` = **Est. 3Y Annualized IRR: `-5.0%` to `+12.0%`** at `$42.14` (Under `H4`, `$42.14` requires **`$104.86/sh`** in 5Y = **`$46.1B–$49.8B`** diluted Mkt Cap on `440M–475M` shares = **`$2.18B–$2.35B` FY30 FCF** at 22–25x).
3. **Dilution Gate (`A1`, `G3`, `H3/H4`):** **FAIL (`A1`, `G3`, `H2/H4`).** Issued **`$1.15B` convertible senior notes in July 2026** (`$1.02B` net cash after capped calls/retirement) + ATM usage (`+14.5%` YoY share expansion).
4. **Capex & FCF Gate (`A3a/b/c`, `G2`, `H2/H3`):** **FAIL (`A3a`, `G2`, `H2`).** TTM Company FCF is **`-$1.174B`** (`OCF -$543.5M` minus `$630.6M` satellite capex; H1 2026 FCF `-$606.8M`). **Fails `H2` 24-month stressed funding test:** Verified in commit `3914533`, 24-month stressed burn (`1.25x` operating burn + committed Block 2 launch/manufacturing capex + `$160M` Ligado obligations) requires **`$5.02B`**, leaving a **`~$1.71B` funding gap** vs `$3.31B` usable pro forma cash.
5. **Leverage (`A4`) & Moat/Margin (`A5`):** Pro forma Cash `~$3.31B` vs Debt `~$2.19B` (`$1.12B` net cash today, but consumed within 15–18 months by constellation capex). Moat: `Narrow` (pioneering D2D cellular broadband patents + AT&T/Verizon/Vodafone MNO agreements + 850 MHz/Ligado spectrum, competing with SpaceX Starlink D2D).
6. **Insiders & Legal (`#7` / `A7` / `H5`):** **FAIL (`H5` / `A6` Legal).** Officer/director net sales are tiny (`56.5k` sh = `0.015%`), **but 10% strategic holders Rakuten (`3.04M` sh) and American Tower (`2.29M` sh) sold `5.33M` shares (`1.45% > 0.50%`)**, and ASTS faces an **active W.D. Texas federal securities class action** filed mid-2026 over Block 2 satellite manufacturing/launch timeline disclosures (`H5/A6` blocker).
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#19a` Active Blackout, `#17`, `#12`).** **Active `#19a` Earnings Blackout:** Q2 2026 revenue of `$31.52M` missed consensus `$34.50M` by **`-8.64%`** (`>5%` hard miss), and FY27E consensus revenue was cut **`-10.6%`** from `$650.78M` to `$581.65M` (`#17` fail). Also `-47.5%` below 200DMA voids `#12` PT leg.
8. **Final Tier & Buy Trigger:** **Tier 2 (`H-watch` — Blocked by `#19a` Blackout, `#17`, `H2` Funding Gap, `H4`, `H5`/Litigation).** **Exact Dollar Buy Trigger:** **≤ $22.00** (where `H4` 5Y `$54.74/sh` target is achievable on `~$1.1B` FY30 FCF) **AND** (1) a clean Q3 2026 beat-and-raise exiting `#19a` blackout, plus (2) non-dilutive Ex-Im Bank / FirstNet / MNO prepayments closing the `$1.71B` `H2` funding gap.

---

#### 3. `PL` — Planet Labs PBC (`[NEW DISCOVERY]` — Route `A–E` / `G` / `H`)
1. **Market Data & Price Health (`PH`):** Price `$14.13` (Oct 14 close; `$20.51` Oct 2), Market Cap `$5.51B` (`~390M` diluted shares including Q2 ATM/converts), 200DMA `$27.25` (**`-48.1%` below 200DMA — voids `#12` PT leg!**), 3Y/Lifetime High `$51.40` (2026-05-28, age 0.4 yr, drawdown `72.5%`, 3Y gap `0.0%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `25.92%` (`$378.5M` TTM -> `$755M` FY29E), Next-FY Organic Rev Growth `~24.0%`, Fwd 3Y EPS/FCF CAGR `Pos -> Neg -> Pos` (FY27E FCF `-$29.08M`), Net Buyback Yield `-6.5%/yr` (WASO `+18.2%` YoY), Multiple Normalization `-15.0%/yr` = **Est. 3Y Annualized IRR: `-2.4%`** (Verified in commit `3914533`: explicit 5Y `H4` base model yields `$12.51/sh` in Year 5 = `-2.4%/yr` vs `20%` hurdle).
3. **Dilution Gate (`A1`, `G3`, `H3`):** **HARD FAIL (`A1`, `G3`, `H3`).** Basic shares rose `+11.54%` YoY (`309.4M` -> `345.1M`) and diluted WASO rose **`+18.2%` YoY (`390.0M`)**, driven by a **`$120M` ATM equity raise** in Q2 FY27 plus **`$460M` convertible senior notes (`38.49M` underlying shares)**.
4. **Capex & FCF Gate (`A3a/b/c`, `G2`, `H3`):** **HARD FAIL (`A3a`, `A3b`, `G2`).** While TTM Company FCF is `$24.67M` (`6.52%` margin < `8.0%` `A3a` floor), FY25 OCF was `-$14.4M` (failing `G2` two-positive-FY-OCF test) and **consensus FY27E FCF drops to `-$29.08M`** due to Pelican/Tanager constellation capex (`$84M–$95M`, failing `A3b` and `G2` `NTM FCF ≥ 90% TTM`).
5. **Leverage (`A4`) & Moat/Margin (`A5`):** Cash `$670.5M` vs Debt `$409.5M` (`$261.0M` net cash, passing `A4`). Moat: `Narrow` (daily global optical/hyperspectral Earth-imaging archive + `$734.5M` RPO backlog, but heavy satellite replacement capex cycle); TTM GM `57.8%`.
6. **Insiders & Legal (`#7` / `A7` / `H5`):** **PASS (`#7`, `A7`, `H5`).** 24 Form 4s over TTM show net insider sales of `1,004,358` shares (`0.29% ≤ 0.50%`), mostly tax-withholding/10b5-1 by founders Will Marshall and Robbie Schingler; clean legal RPL.
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#11`, `#12`, `#19d`, `H4`).** **Active `#19d` Guide Miss Blackout:** Q2 FY27 revenue beat (`$102.5M`), but Q3 FY27 revenue guidance of `$101M–$105M` (mid `$103M`) **missed consensus `$114.3M` by `-9.9%`** (and because PL does not guide positive full-year FCF, the `#19d` quarterly timing exemption cannot apply). `-48.1%` below 200DMA voids `#12` PT leg.
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `A1/G3`, `A3a/A3b/G2`, `#19d` Blackout, `#12`, `H4`).** **Indicative Ceiling:** **≤ $5.03** (pure `H4` 20%/yr 5Y math) or **≤ $8.00–$9.00** (Route G 12–15% compounder once FY27/28 FCF turns sustainably positive and ATM/convert dilution rolls off).

---

#### 4. `LUNR` — Intuitive Machines, Inc. (`[NEW DISCOVERY]` — Route `H` / Fails Market Cap Floor)
1. **Market Data & Price Health (`PH`):** Price `$11.02`, Market Cap **`$1.91B`** (**Fails `#2` `$2.5B` Market Cap Minimum Floor!**), 200DMA `$20.21` (**`-45.5%` below 200DMA — voids `#12` PT leg!**), 3Y/Lifetime High `~$24.95` (drawdown `~55.8%`). **`PH-clear`** (on price structure, though disqualified by cap floor).
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `~35.0%` (NASA CLPS & Near Space Network contracts), Next-FY Organic Rev Growth `~30.0%`, Fwd 3Y EPS/FCF CAGR `Negative`, Net Buyback Yield `-12.0%/yr` (warrant exercises, PIPE/ATM offerings), Multiple Normalization `-10.0%/yr` = **Est. 3Y Annualized IRR: `-10.0%`**.
3. **Dilution Gate (`A1`, `G3`, `H3`):** **HARD FAIL (`A1`, `G3`).** Massive share count expansion (`>25%` YoY) from public/private warrant redemptions, Class C/A exchanges, and equity offerings.
4. **Capex & FCF Gate (`A3a/b/c`, `G2`, `H2/H3`):** **HARD FAIL (`A3a`, `G2`, `H3`).** Negative TTM and NTM Operating and Free Cash Flow (`~$60M–$90M/yr` cash burn on lunar lander R&D and infrastructure).
5. **Leverage (`A4`) & Moat/Margin (`A5`):** **FAIL (`A4`).** Net Debt **`$114.1M`** (`$367.3M` cash vs `$481.5M` debt/liabilities) against negative FCF (`A4` fail). Moat: `Narrow` (NASA CLPS/NSNS contractor, but mission-failure single-point risk).
6. **Insiders & Legal (`#7` / `A7` / `H5`):** Heavy insider/sponsor selling post-deSPAC (`>0.5%` of float, failing `#7/H5`).
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#2` Mkt Cap, `#11`, `#12`, `H4`).** Negative earnings/FCF (`#11` fail); `-45.5%` below 200DMA voids `#12` PT leg (`$18.17` PT voided).
8. **Final Tier & Buy Trigger:** **Tier 3 (Disqualified by `#2` `<$2.5B` Market Cap Floor + Hard Gate Fail on `A1`, `A3a`, `A4`, `#7/H5`, `#12`).** **Indicative Ceiling:** **≤ $5.50** (and must organically exceed `$2.5B` market cap with positive FCF).

---

#### 5. `RDW` — Redwire Corporation (`[NEW DISCOVERY]` — Route `H` / `A–E`)
1. **Market Data & Price Health (`PH`):** Price `$8.62` (Oct 15; `$10.88` Oct 2 sweep), Market Cap `$2.2B–$2.7B`, 200DMA `$11.05` (**`-22.0%` below 200DMA on Oct 15 / `-1.5%` Oct 2 — voids `#12` PT leg on Oct 15!**), 3Y/Lifetime High `$25.90` (2026-05-28, age 0.4 yr, drawdown `66.7%` Oct 15 / `58.0%` Oct 2). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `27.79%`, Next-FY Organic Rev Growth `~25.0%`, Fwd 3Y EPS/FCF CAGR `Negative` (FY26E FCF `-$67.37M`), Net Buyback Yield `-15.0%/yr` (`$566.2M` equity/preferred issuance), Multiple Normalization `-8.0%/yr` = **Est. 3Y Annualized IRR: `-6.5%`**.
3. **Dilution Gate (`A1`, `G3`, `H3`):** **HARD FAIL (`A1`, `G3`).** Verified in `defense_space.md`: issued **`$566.2M` of equity & Bain/AE Industrial preferred stock conversions** in TTM to fund space-infrastructure M&A (Hera Systems / Edge Autonomy) and working capital.
4. **Capex & FCF Gate (`A3a/b/c`, `G2`, `H2/H3`):** **HARD FAIL (`A3a`, `G2`, `H2`, `H3`).** Verified in `defense_space.md`: H1 2026 FCF was **`-$44.89M`** and consensus FY26E FCF is **`-$67.37M`** (`A3a` and `G2` fail; `H2/H3` destination unverified).
5. **Leverage (`A4`) & Moat/Margin (`A5`):** **FAIL (`A4`).** Positive net debt + preferred obligations against negative `-$67.4M` NTM FCF (`A4` fail). Moat: `Narrow` (ROSA solar arrays & VLEO spacecraft platforms, ~20–25% gross margin).
6. **Insiders & Legal (`#7` / `A7` / `H5`):** PE sponsor (AE Industrial Partners) & preferred conversion overhang (`H5` unverified/watch).
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#11`, `#12`, `H4`).** Negative FCF and GAAP EPS (`#11` fail); `-22.0%` below 200DMA voids `#12` PT leg.
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `A1/G3`, `A3a/G2`, `A4`, `#11`, `#12`, `H2–H4`).** **Indicative Ceiling:** **≤ $4.50** + 4Q roll-off of the `$566.2M` equity issuance + positive FCF inflection (`≥8%` margin).

---

#### 6. `BKSY` — BlackSky Technology Inc. (`[NEW DISCOVERY]` — Route `H` / Fails Market Cap Floor)
1. **Market Data & Price Health (`PH`):** Price `$20.81`, Market Cap **`$722M–$807M`** (**Hard Fail on `#2` `$2.5B` Market Cap Minimum Floor!**), 200DMA `$27.64` (**`-24.7%` below 200DMA — voids `#12` PT leg!**), 3Y High `~$33.00` (drawdown `~37%`). **`PH-clear`** (disqualified by `$2.5B` cap floor).
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `~22.0%` (`$109.7M` TTM rev), Next-FY Organic Rev Growth `~20.0%`, Fwd 3Y EPS/FCF CAGR `Negative` (TTM Net Loss `-$70.1M`, FCF `-$42.5M`), Net Buyback Yield `-8.0%/yr` (equity raises), Multiple Normalization `-5.0%/yr` = **Est. 3Y Annualized IRR: `-8.0%`**.
3. **Dilution Gate (`A1`, `G3`):** **HARD FAIL (`A1`, `G3`).** Repeated equity/PIPE offerings and warrant dilution (`>10%` YoY share growth).
4. **Capex & FCF Gate (`A3a/b/c`, `G2`):** **HARD FAIL (`A3a`, `G2`).** TTM Company FCF is **`-$42.5M`** (`-38.7%` FCF margin on `$109.7M` rev) due to Gen-3 satellite constellation capex.
5. **Leverage (`A4`) & Moat/Margin (`A5`):** **HARD FAIL (`A4`).** Net Debt **`$109.7M`** (`$126M` cash vs `$236M` debt) against `-$42.5M` FCF. Moat: `None/Narrow` (sub-scale optical EO vs Planet Labs & Maxar).
6. **Insiders & Legal (`#7` / `A7`):** Sponsor/insider dilution overhang.
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#2` Mkt Cap `< $2.5B`, `#11`, `#12`).**
8. **Final Tier & Buy Trigger:** **Tier 3 (Disqualified by `#2` `< $2.5B` Market Cap Floor + `A1`, `A3a`, `A4`, `#11`, `#12`).** **Indicative Ceiling:** Disqualified until Market Cap `≥ $2.5B`; fundamental ceiling `≤ $9.00`.

---

#### 7. `IRDM` — Iridium Communications Inc. (`[NEW DISCOVERY]` — Pending M&A Target / Route `A–E`)
1. **Market Data & Price Health (`PH`):** Price `$45.96`, Market Cap `$5.00B` (`105.96M` shares), 200DMA `$37.77` (`+21.7%` above 200DMA), 3Y High `~$62.00` (drawdown `~25.9%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** **Capped by Pending Acquisition:** On **June 28, 2026**, Rocket Lab (`RKLB`) signed a definitive agreement to acquire `IRDM` for **`$27.00` in cash + `0.40` RKLB shares per IRDM share** (subject to a `$67.50` RKLB collar; at RKLB `$59.18`, implied deal value is `$27.00 + $23.67 = $50.67/sh`, closing expected mid-2027). Standalone 3Y Rev CAGR is `~6.0%` (`$894M` TTM rev) and 3Y EPS CAGR is `~8.5%` = **Standalone 3Y IRR `~9.0%`**.
3. **Dilution Gate (`A1`):** **PASS (`A1` standalone).** Share count `-5.2%` YoY prior to the RKLB merger agreement.
4. **Capex & FCF Gate (`A3a/b/c`):** **PASS (`A3a/b/c` standalone).** TTM Company FCF **`$288.0M`** (`32.2%` FCF margin on `$894M` rev; capex holiday until NEXT constellation replacement in 2030s).
5. **Leverage (`A4`) & Moat/Margin (`A5`):** **HARD FAIL (`A4` standalone).** Net Debt **`$1.60B`** (`$1.775B` term loan vs `$175M` cash) against `$288M` FCF = **`5.56x Net Debt / FCF > 2.50x` hard ceiling**. Moat: `Wide` (global L-band satellite safety/aviation/DoD spectrum monopoly).
6. **Insiders & Legal (`#7` / `A7`):** Clean (`<0.2%` net sales); subject to standard merger proxy approvals.
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **FAIL (`#9`, `#10`, `#12`, Pending Buyout).** Standalone fails `#9` (`6.0% < 15%` 3Y Rev CAGR), `#10` (`8.5% < 20%` EPS CAGR), and `A4` (`5.56x` leverage); upside is capped by the RKLB merger consideration (`$50.67` at current RKLB price = `+10.2%`).
8. **Final Tier & Buy Trigger:** **Tier 3 (Pending M&A Target being acquired by `RKLB` + Standalone `A4`, `#9`, `#10` Fail).** **Indicative Ceiling:** No standalone thesis unless the RKLB merger terminates AND `IRDM` trades **≤ $28.00** while paying down debt below `$720M` (`≤2.5x` FCF).

---

#### 8. `MDA.TO` (`MDA`) — MDA Space Ltd. (`[NEW DISCOVERY]` — Route `A–E` / `G`)
1. **Market Data & Price Health (`PH`):** Price `US$27.45` (`C$40.50`), Market Cap `US$4.44B` (`~162M` shares), 200DMA `US$31.49` (`C$43.70`; `-12.8%` below 200DMA; `#12` PT leg valid), 3Y/Lifetime High `~US$36.00` (drawdown `~23.8%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `~28.5%` (scaling from `C$1.08B` FY24 to `C$1.87B+` on `C$4.6B+` AURORA digital satellite backlog for Telesat Lightspeed, Globalstar/Apple, and Canadarm3), Next-FY Organic Rev Growth `~30.0%`, Fwd 3Y EPS CAGR `~25.0%`, Net Buyback Yield `-3.5%/yr` (share count creep), Multiple Normalization `-3.0%/yr` (`Fwd P/E 22.4x` -> `20.5x`) = **Est. 3Y Annualized IRR: `18.5%`**.
3. **Dilution Gate (`A1`, `G3`):** **HARD FAIL (`A1`, `G3`).** Confirmed in the Oct 2 repository sweep (`defense_space.md`): share count expanded **`+30.2%` over the trailing 3Y** (and `>3%` YoY to `~162M` diluted shares via equity issuances, SatixFy/supply-chain M&A, and option dilution).
4. **Capex & FCF Gate (`A3a/b/c`, `G2`):** **FAIL (`A3a/A3c` / `G2` working-capital & capex lumpiness).** While operating cash flow is buoyed by customer prepayments on Telesat Lightspeed and Globalstar contracts, heavy Montreal high-volume satellite manufacturing expansion capex (`C$180M–C$220M/yr`) compresses normalized FCF margin near the `6–8%` border and pushes `Capex/OCF > 35%` (`A3c`).
5. **Leverage (`A4`) & Moat/Margin (`A5`):** **PASS (`A4`).** Net Cash **`~US$19.5M`** (`US$398M` cash vs `US$378.5M` debt, `A4` pass). Moat: `Narrow` (Canadarm space robotics monopoly + AURORA software-defined LEO satellite platform, but fixed-price satellite manufacturing execution risk); Gross Margin `~27–30%`.
6. **Insiders & Legal (`#7` / `A7`):** Canadian TSX/NYSE dual-listed (`SEDI` insider filings rather than SEC Form 4; Northern Private Capital sponsor overhang reduced).
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** Passes `#11` (`Fwd P/E 22.4x ≤ 38x`, `PEG ~0.89 ≤ 2.0`) and `#12` (`Consensus PT US$46.12 / C$66.50` = `+68.0%` upside), **but blocked by `A1/G3` dilution and `A3c` capex intensity**.
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `A1`/`G3` Dilution + `A3c` Capex Intensity).** **Indicative Buy Trigger:** **≤ US$21.00 (C$31.00)** (`25%+` 3Y IRR) **AND** 4 consecutive quarters of `≤0.5%` YoY share dilution (`A1`) + completion of Montreal facility expansion (`Capex/OCF ≤ 35%`).

---

#### 9. `SATS` — EchoStar Corporation (`[NEW DISCOVERY]` — Route `H` / Distressed)
1. **Market Data & Price Health (`PH`):** Price `$24.50`, Market Cap `$6.80B`, 200DMA `$30.05` (`-18.5%` below 200DMA), 3Y/Lifetime High `$80.00+` (`>70%` multi-year drawdown). **`PH-warning` / `PH-impaired`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `-4.5%` (shrinking Dish Pay-TV, HughesNet satellite broadband, and Boost Wireless), Fwd 3Y EPS/FCF CAGR `Deeply Negative`, Net Buyback Yield `-15.0%/yr` (distressed convertible/spectrum debt exchanges) = **Est. 3Y Annualized IRR: `-25.0%`**.
3. **Dilution Gate (`A1`, `G3`):** **HARD FAIL (`A1`, `G3`).** Massive distressed debt-for-equity/convertible exchanges and PIPEs to stave off bankruptcy maturities.
4. **Capex & FCF Gate (`A3a/b/c`, `G2`, `H2`):** **HARD FAIL (`A3a`, `G2`, `H2`).** Burning `>$1.5B/yr` in negative FCF.
5. **Leverage (`A4`) & Moat/Margin (`A5`):** **HARD FAIL (`A4`, `A5`).** Over **`$20B+` in Net Debt** against negative FCF and shrinking legacy Pay-TV/satellite revenue (`No Moat`).
6. **Insiders & Legal (`#7` / `A7`):** Creditor litigation over spectrum drop-down transactions (`A6` fail).
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#9`, `#10`, `#11`, `#12`, `H1–H4`).**
8. **Final Tier & Buy Trigger:** **Tier 3 (Uninvestable Distressed Balance Sheet — Hard Fail on `A1`, `A3a`, `A4`, `A5`, `A6`, `#9`, `#11`).**

---

### LANE 9: Uranium, Nuclear Fuel Cycle & Enrichment Bottlenecks (Route `F` for Commodity Producers; `A–E`/`G`/`H` for Equipment/Enrichment/SMRs)

> **Critical Framework Rule (`stage-paths.md` — Route `F` Commodity Cyclicals):**  
> - **Mandatory Routing:** All commodity uranium/mining producers (`CCJ`, `KAP.L`, `UEC`, `NXE`, `UUUU`) **must** be evaluated under **Route F (`F1` + `F2`)**. They **cannot** bypass Route F via Route G or Route H.  
> - **`F1` Quantitative Gate (ALL required):** TTM FCF margin `≥10%` (`OCF - capex`), EBITDA margin `≥30%`, Net Debt/EBITDA `≤3.25x`, Interest coverage `≥3.5x`, ROIC `≥ WACC`, **Fwd P/E `≤15.0x`**, **PEG `≤0.75`**, **EV/EBITDA `≤11.0x`**, 3Y EPS CAGR `≥25%`, **zero equity issuance/ATMs/converts in last 4Q**, **gross buybacks `>0` in last 4Q**, and PT `≥+25%` (`≥15` analysts) OR NTM FCF yield `≥4.0%`.  
> - **`F2` Insider Buying Trigger (REQUIRED):** Open-market purchase in last 90 days of `≥$2.0M` AND `≥5%` of holding by CEO/CFO/COO/Chair/founder, OR `≥3` insiders buying open-market in 90 days (entry within 30 days of Form 4).

---

#### 1. `CCJ` — Cameco Corporation (Seed — Route `F` Mandatory)
1. **Market Data & Price Health (`PH`):** Price `$81.50` (Oct 15; `$85.18` Oct 2 sweep), Market Cap `$35.5B–$37.1B`, 200DMA `$105.66` (**`-22.9%` below 200DMA on Oct 15 / `-19.4%` Oct 2 — voids `#12` PT leg on Oct 15!**), 3Y/Lifetime High `$134.09` (2026-01-28, age 0.7 yr, drawdown `39.2%` Oct 15 / `36.5%` Oct 2). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `12.6%`, Next-FY Organic Rev Growth `~14.0%`, Fwd 3Y EPS CAGR `~28.0%` (as legacy uranium contracts roll into `$80–$90/lb` LT realizations + 49% Westinghouse JV contribution), Net Buyback Yield `0.0%` (`0.15%` div), Multiple Normalization `-22.0%/yr` (from `59.9x–97x` Fwd P/E down toward `25x` normalized multiple) = **Est. 3Y Annualized IRR: `6.5%`** (Extreme multiple compression drag).
3. **Dilution Gate (`F1` / `A1`):** **FAIL (`F1` Buyback Rule).** Share count is flat (`435.4M` shares, `+0.1%` YoY; Nov 2022 Westinghouse equity raise is past the 4Q window), **but `F1` requires `>0` gross share buybacks in the last 4 quarters (`CCJ` repurchased `$0`)**.
4. **Capex & FCF Gate (`F1` / `A3a`):** **FAIL (`F1` EBITDA Margin).** TTM Company FCF is `~$680M` (`~26%` of consolidated C$3.5B rev, clearing `≥10%` `F1` FCF margin), **but consolidated GAAP EBITDA margin is `~23.0% < 30.0%` `F1` floor** (diluted by fuel services / Westinghouse accounting).
5. **Leverage (`F1` / `A4`) & Moat/Margin (`A5`):** **PASS (`F1` Leverage & Moat).** Net Debt **`$224.2M`** (`$999.2M` debt vs `$775.0M` cash; `Net Debt/EBITDA = 0.35x ≤ 3.25x`). Moat: `Wide` (Tier-1 Cigar Lake & McArthur River high-grade Athabasca mines + UF6 conversion + 49% Westinghouse).
6. **Insiders & Legal (`F2` / `#7`):** **HARD FAIL (`F2`).** **Zero qualifying open-market insider purchases** (`≥$2M` & `≥5%` holding increase by CEO Tim Gitzel/CFO, or `≥3` insiders in 90 days).
7. **Valuation (`F1`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`F1` Valuation Ceilings).** Verified in commit `f6171aa` (`power_platforms.md`): **Fwd P/E is `59.92x–97.0x` (vs `≤15.0x` `F1` ceiling!)**, **PEG is `2.14–3.21` (vs `≤0.75` `F1` ceiling!)**, and **EV/EBITDA is `66.37x–68.3x` (vs `≤11.0x` `F1` ceiling!)**. Also `-22.9%` below 200DMA voids `#12` PT leg (`$118.42` PT voided).
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `F1` Valuation [`P/E 59.9x > 15`, `EV/EBITDA 66.4x > 11`, `PEG > 0.75`], `F1` EBITDA Margin `<30%`, `F1` Zero Buybacks, and `F2` No Insider Buy).** **Exact Route F Buy Trigger:** **≤ $24.00** (`Fwd P/E ≤ 15.0x`, `EV/EBITDA ≤ 11.0x`) + qualifying `$2M+` CEO/CFO open-market purchase (`F2`) + token share buyback.

---

#### 2. `LEU` — Centrus Energy Corp. (`[NEW DISCOVERY]` — Route `H-watch` / `A–E`)
1. **Market Data & Price Health (`PH`):** Price `$120.00`, Market Cap `$2.65B`, 200DMA `$196.16` (**`-38.8%` below 200DMA — voids `#12` PT leg!**), 3Y/Lifetime High `~$310.00` (drawdown `~61.3%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `~14.0%` (`$442M` TTM SWU broker/enrichment rev; DOE HALEU task orders ramp late 2028+), Next-FY Organic Rev Growth `~10.0%`, Fwd 3Y EPS CAGR `-5.0%` (margin compression as legacy Russian TENEX SWU contracts face waivers/tariffs and Piketon centrifuge capex ramps), Net Buyback Yield `-8.0%/yr` (ATM/convert dilution), Multiple Normalization `-18.0%/yr` (`Fwd P/E 48x–59x`, `EV/EBITDA 174x`) = **Est. 3Y Annualized IRR: `-8.0%`**.
3. **Dilution Gate (`A1`, `G3`, `H3`):** **HARD FAIL (`A1`, `G3`, `H3`).** Executed repeated ATM equity offerings (`$200M+` ATM program) and convertible senior note issuances over the last 12 months (`+18%` YoY share count expansion) to co-fund Piketon, Ohio centrifuge manufacturing.
4. **Capex & FCF Gate (`A3a/b/c`, `G2`, `H3`):** **HARD FAIL (`A3a`, `A3b`, `G2`, `H3`).** TTM and NTM Company FCF are turning **negative** as multi-hundred-million-dollar Piketon HALEU/LEU cascade construction capex ramps (`Capex/OCF > 100%`), with full commercial cascade cash generation beyond the 5-year `H3` horizon.
5. **Leverage (`A4`) & Moat/Margin (`A5`):** Cash `~$1.1B` (raised via ATMs/converts) vs `~$650M` debt/customer advances (`$449M` net cash today, `A4` pass today but earmarked for Piketon capex). Moat: `Narrow` (only NRC-licensed US HALEU producer, but historically reliant on reselling Russian TENEX SWU).
6. **Insiders & Legal (`#7` / `A7` / `H5`):** Insider sales `<0.5%` (`H5` pass); geopolitical/import-waiver regulatory risk on Russian TENEX supply through 2027.
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#9`, `#10`, `#11`, `#12`, `H3/H4`).** Fwd P/E `39.3x–59.3x > 38.0x`, EV/EBITDA `174.16x`, 3Y Rev CAGR `<15%`, and `-38.8%` below 200DMA voids `#12` PT leg (`$249.91` PT voided).
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `A1/G3`, `A3a/A3b/G2`, `#9`, `#11`, `#12`, `H3/H4`).** **Indicative Ceiling:** **≤ $48.00** + 4Q halt to ATM dilution + binding DOE/utility fixed-margin HALEU offtake contracts proving `H3/H4` within 5 years.

---

#### 3. `BWXT` — BWX Technologies, Inc. (`[NEW DISCOVERY]` — Route `A–E` / `G`)
1. **Market Data & Price Health (`PH`):** Price `$138.50`, Market Cap `$12.8B` (`91.6M` shares), 200DMA `$138.50` (`0.0%` at 200DMA; `#12` PT leg valid), 3Y/Lifetime High `~$152.00` (drawdown `~8.9%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `~8.5%` (`$2.75B` TTM rev -> `$3.5B` FY28E across US Navy Virginia/Columbia-class submarine reactors, CANDU life extensions, and medical isotopes), Next-FY Organic Rev Growth `~8.0%`, Fwd 3Y EPS CAGR `~12.5%`, Net Buyback + Div Yield `+0.7%`, Multiple Normalization `-2.5%/yr` (`Fwd P/E 27.4x` -> `25.0x`) = **Est. 3Y Annualized IRR: `9.8%`** (Steady naval defense compounder, far below `25%` IRR).
3. **Dilution Gate (`A1`, `G3`):** **HARD FAIL (`A1`, `G3`).** Issued **`$1.1B` of convertible senior notes in November 2025** (within the trailing 12-month `A1` and `G3` prohibition window on new convertible debt!).
4. **Capex & FCF Gate (`A3a/b/c`, `G2`):** **PASS (`A3a/b/c`, `G2`).** TTM Company FCF `~$235M` (`~8.5%` FCF margin ≥ `8.0%` `A3a` / `≥6.0%` `G2`), NTM FCF `~$270M > TTM`, Capex `~32%` of OCF (`≤35%` `A3c`).
5. **Leverage (`A4` / `G2`) & Moat/Margin (`A5`):** **HARD FAIL (`A4` / `G2`).** Net Debt **`$1.40B`** against `~$235M` TTM FCF (`~$270M` NTM FCF) = **`5.19x–5.96x Net Debt / FCF > 2.50x` hard ceiling** (fails both `A4` and `G2`!). Moat: `Wide` (sole-source US Navy nuclear propulsion reactor manufacturer + NRC Category I fuel license).
6. **Insiders & Legal (`#7` / `A7`):** **PASS (`#7` / `A7`).** TTM net insider sales `<0.15%` of shares out; clean legal RPL.
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#9`, `#10`, `#11` PEG).** Fwd P/E `26.7x–28.1x ≤ 38x`, **but PEG `2.22 > 2.00` (`#11` fail)**; 3Y Rev CAGR `8.5% < 15%` (`#9` fail; `<10%` `G2` fail) and 3Y EPS CAGR `12.5% < 20%` (`#10` fail). Consensus PT `$223.20` (`+61.2%` upside).
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `A1/G3` Nov 2025 `$1.1B` Convertible Notes, `A4/G2` `5.2x+` Net Debt/FCF, `#9/#10`, `#11` PEG).** **Indicative Ceiling:** **≤ $88.00** (`PEG ≤ 1.40`, `25%+` 3Y IRR) + debt paydown below `$675M` (`≤2.5x` FCF) + roll-off of Nov 2025 convert issuance.

---

#### 4. `KAP.L` — NAC Kazatomprom JSC GDR (`[NEW DISCOVERY]` — Route `F` Mandatory)
1. **Market Data & Price Health (`PH`):** Price `$62.50` (`$62.00–$63.00` LSE GDR), Market Cap `$16.3B` (`259.36M` GDR equivalents), 200DMA `$73.59` (`-15.1%` below 200DMA; `#12` PT leg remains valid since within `-20%`), 3Y/Lifetime High `~$79.50` (drawdown `~21.4%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `~14.5%`, Next-FY Organic Rev Growth `~15.0%`, Fwd 3Y EPS CAGR `~16.5%` (high uranium prices partially offset by Kazakhstan's tiered Mineral Extraction Tax [MET] hike taking effect 2026+ and sulfuric acid / JV partner production allocations), Dividend Yield `+6.0%` (`0%` buybacks), Multiple Normalization `-1.5%/yr` (`Fwd P/E 10.8x`) = **Est. 3Y Annualized IRR: `19.5%`** at `$62.50` (**`25.5%` at `≤$52.00`**).
3. **Dilution Gate (`F1` / `A1`):** **FAIL (`F1` Buyback Sub-Gate).** Zero share dilution in last 5 years (`259.36M` constant shares; `0%` SBC), **but `F1` explicitly requires `>0` gross share buybacks in the last 4 quarters**, whereas Kazatomprom returns capital exclusively via cash dividends (`~75%` of FCF payout policy) and repurchased `0` shares.
4. **Capex & FCF Gate (`F1` / `A3a`):** **PASS (`F1` FCF & EBITDA Margins).** TTM Company FCF is `~$1.05B` (`~24%` FCF margin ≥ `10%` `F1` floor) and TTM EBITDA margin is `~52%` (`≥30%` `F1` floor).
5. **Leverage (`F1` / `A4`) & Moat/Margin (`A5`):** **PASS (`F1` Leverage & Moat).** Net Cash **`~$420M`** (`Net Debt/EBITDA = -0.2x ≤ 3.25x`; interest coverage `>25x ≥ 3.5x`; ROIC `~32% >> WACC`). Moat: `Wide` (world's largest, lowest-cost first-quartile In-Situ Recovery [ISR] uranium producer accounting for ~23% of global primary supply).
6. **Insiders & Legal (`F2` / `#7`):** **HARD FAIL (`F2` & `#7` Foreign Filer).** Fails `F2`: **zero open-market insider purchases** (`≥$2M` & `≥5%` holding increase) in the last 90 days (75% state-owned by Kazakhstan sovereign wealth fund Samruk-Kazyna; exempt from US SEC Form 4 reporting + sovereign/East-West transport geopolitical risk).
7. **Valuation (`F1`), Asymmetry (`#12`), Print (`#19`):** **PASSES `F1` Valuation (`Fwd P/E 10.8x ≤ 15.0x`, `EV/EBITDA 7.28x ≤ 11.0x`, `PEG ~0.65 ≤ 0.75`, `FCF yield ~6.4% ≥ 4.0%`), FAILS `F1` 3Y EPS CAGR (`~16.5% < 25.0%` floor).** Consensus PT `$79.51` (`+27.2%` upside, though `<15` Western analysts cover the LSE GDR, requiring the `≥4.0%` FCF yield leg under `F1`, which it passes at `6.4%`).
8. **Final Tier & Buy Trigger:** **Tier 2 (Near-Pass Watchlist — Only Uranium Producer Clearing `F1` Valuation & Margin Ceilings).** **Exact Dollar Buy Trigger:** **≤ $52.00** (unlocks `≥25%` 3Y EPS + dividend IRR) **AND** a qualifying `F2` open-market management purchase + token 1Q share buyback (`F1`).

---

#### 5. `NXE` — NexGen Energy Ltd. (`[NEW DISCOVERY]` — Route `F` Mandatory)
1. **Market Data & Price Health (`PH`):** Price `$8.50`, Market Cap `$5.60B`, 200DMA `$10.90` (**`-22.0%` below 200DMA — voids `#12` PT leg!**), 3Y/Lifetime High `~$12.50` (drawdown `~32.0%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Pre-revenue single-asset mine developer (Rook I / Arrow deposit in Athabasca Basin; CNSC federal permitting & 4-year shaft/mill construction means **zero commercial uranium revenue or positive FCF within the next 3 years**; `C$2.2B+` capex required) = **Est. 3Y Annualized Operating IRR: `-10.0%`** (pure uranium spot/NAV option).
3. **Dilution Gate (`F1` / `A1`):** **HARD FAIL (`F1` / `A1`).** Issued convertible debentures (`$250M` 9.0% converts to buy physical uranium + prior Queen's Road converts) and continuous ATM/equity offerings (`+8%` YoY share dilution) with `0` buybacks.
4. **Capex & FCF Gate (`F1` / `A3a`):** **HARD FAIL (`F1` / `A3a`).** Pre-revenue (`$0` revenue, negative EBITDA, negative TTM FCF `~$120M` burn, and `C$2.2B` construction capex ahead). Even if evaluated under Route H, `NXE` fails `H1` (no operating mine/product) and `f6171aa` explicitly bans commodity resource companies from Route G/H.
5. **Leverage (`F1`) & Moat/Margin (`A5`):** Cash `$683M` vs Debt `$435M` (`$247M` net cash today, but `C$2.2B` Rook I capex requires `>$1.5B` project debt/equity). Moat: `Narrow` (tier-1 undeveloped Arrow orebody, zero current production).
6. **Insiders & Legal (`F2` / `#7`):** **HARD FAIL (`F2`).** No qualifying `$2M+` open-market insider purchase in last 90 days; high CEO compensation/options dilution.
7. **Valuation (`F1`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`F1` across every metric, `#12`).** Negative EPS, negative EBITDA, negative FCF, and `-22.0%` below 200DMA voids `#12` PT leg.
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `F1` Pre-Revenue/Negative FCF/Dilution, `F2` No Insider Buy, `#12`).** **Buy Trigger:** Uninvestable under framework until Rook I reaches commercial production (`~2029–2030`) and clears `F1` (`P/E ≤ 15x`, `FCF margin ≥ 10%`) + `F2`.

---

#### 6. `UEC` — Uranium Energy Corp. (`[NEW DISCOVERY]` — Route `F` Mandatory)
1. **Market Data & Price Health (`PH`):** Price `$8.65`, Market Cap `$4.05B`, 200DMA `$12.93` (**`-33.1%` below 200DMA — voids `#12` PT leg!**), 3Y/Lifetime High `~$14.20` (drawdown `~39.1%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `~35%` off a tiny base (`<$100M` TTM rev as Wyoming/Texas ISR hub-and-spoke restarts scale slowly), Fwd 3Y EPS/FCF CAGR `Negative / Sub-scale`, Net Buyback Yield `-7.5%/yr` (ATM & stock-settled M&A dilution) = **Est. 3Y Annualized IRR: `-12.0%`**.
3. **Dilution Gate (`F1` / `A1`):** **HARD FAIL (`F1` / `A1`).** Serial equity issuer via ATM programs and stock-settled M&A (Rio Tinto Sweetwater / Anfield / UEX acquisitions; shares expanded `>10%` YoY and `>50%` over 3Y) with `0` buybacks.
4. **Capex & FCF Gate (`F1` / `A3a`):** **HARD FAIL (`F1` / `A3a`).** TTM Company FCF is **`-$107.0M`** (negative OCF and negative EBITDA; fails `F1` `≥10%` FCF margin and `≥30%` EBITDA margin).
5. **Leverage (`F1`) & Moat/Margin (`A5`):** Net Cash **`$492.5M`** (`$495M` cash/inventory vs `$2.5M` debt). Moat: `None` (small-scale higher-cost US ISR assets vs Kazatomprom/Cameco).
6. **Insiders & Legal (`F2` / `#7`):** **HARD FAIL (`F2`).** Zero qualifying `$2M+` open-market insider purchases in last 90 days.
7. **Valuation (`F1`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`F1` across all valuation/profitability metrics, `#12`).** Negative Fwd P/E, negative EV/EBITDA, negative FCF yield, and `-33.1%` below 200DMA voids `#12` PT leg.
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `F1` Negative FCF/EBITDA/EPS & Serial ATM Dilution, `F2` No Insider Buy, `#12`).** **Indicative Ceiling:** **≤ $3.80** once profitable (`Fwd P/E ≤ 15x`, `FCF margin ≥ 10%`, 4Q zero ATM issuance, and `F2` insider buy).

---

#### 7. `UUUU` — Energy Fuels Inc. (`[NEW DISCOVERY]` — Route `F` Mandatory)
1. **Market Data & Price Health (`PH`):** Price `$8.34` (Oct 14 close), Market Cap `$2.80B`, 200DMA `$16.94` (**`-50.8%` below 200DMA — voids `#12` PT leg!**), All-Time Split-Adjusted Closing High **`$235.00` (2007-04-13, age 19.5 yrs, drawdown `96.45%`!)**, 3Y High `$26.08` (2026-01-27, 3Y drawdown `68.0%`, 3Y-to-Lifetime Gap `-74.85 pp`). **`PH-impaired` (Hard Disqualification under `price-health.md`!)**.
2. **25% 3-Year IRR Math:** Fwd 3Y Rev CAGR `~25%` off `$105.7M` TTM rev, Fwd 3Y EPS/FCF CAGR `Negative` (`-$120.4M` TTM FCF), Net Buyback Yield `-25.0%/yr` (massive ATM + stock M&A + convert dilution) = **Est. 3Y Annualized IRR: `-22.0%`**.
3. **Dilution Gate (`F1` / `A1`):** **HARD FAIL (`F1` / `A1`).** Directly verified in commit `3914533` (`chips_power.md`):
   - Sold **`~$300M` of common stock under its ATM** across Q1–Q3 2026 (`14.74M` sh in H1 + `13.68M` sh in Q3);
   - Issued **`14.81M` shares (`~$169M`)** on Aug 28, 2026 to acquire Australian Strategic Materials (`ASM`);
   - Filed a **new `$500M` ATM prospectus supplement on October 13, 2026**;
   - Signed a pending deal on Oct 1, 2026 to issue up to **`65.85M` shares** for Vulcan Elements (`VAC`);
   - Issued **`$700M` of `0.75%` convertible senior notes due 2031** in October 2025;
   - Zero share buybacks in the last 4 quarters (`F1` fail).
4. **Capex & FCF Gate (`F1` / `A3a`):** **HARD FAIL (`F1` / `A3a`).** Verified in commit `3914533`: TTM OCF is **`-$62.46M`**, Capex is `$57.96M`, and TTM Company FCF is **`-$120.4M` (`-113.9%` FCF margin vs `≥10%` `F1` floor!)**; TTM EBITDA is `-$71.7M` (`-67.8%` margin vs `≥30%` `F1` floor).
5. **Leverage (`F1`) & Moat/Margin (`A5`):** Cash `$1.10B` vs Debt `$684.5M` (`$415.5M` net cash, raised via converts/ATMs, but `Net Debt/EBITDA` and interest coverage fail `F1` due to negative EBITDA/EBIT `-$84.95M`). Moat: `None` (White Mesa Mill processing uranium/REE ore at `-5.6%` gross margin).
6. **Insiders & Legal (`F2` / `#7`):** **HARD FAIL (`F2`).** CEO Mark Chalmers bought `50,000` shares (`~$0.97M`) on Jul 7, 2026 — **fails `F2` (`<$2.0M` minimum AND `>90` days old / `>30` days past Form 4)** — while 5 insiders sold `419,652` shares in TTM.
7. **Valuation (`F1`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`PH-impaired`, `F1`, `F2`, `#12`).**
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Disqualified: `PH-impaired` + `F1` `-113.9%` FCF Margin & Serial Dilution + `F2` Fail + `#12` Fail).** **Indicative Ceiling:** Uninvestable until `PH-recovery` + `F1/F2` compliance (`≤ $2.50`).

---

#### 8. `OKLO` — Oklo Inc. (`[NEW DISCOVERY]` — Route `H` Pre-Revenue SMR)
1. **Market Data & Price Health (`PH`):** Price `$30.10`, Market Cap `$5.90B`, 200DMA `$57.61` (**`-47.8%` below 200DMA — voids `#12` PT leg!**), 3Y/Lifetime High `~$75.00` (drawdown `~59.9%`). **`PH-clear`**.
2. **25% 3-Year IRR Math:** Pre-revenue fast-fission microreactor developer (`$1.2M` TTM grant/service baseline; first commercial Aurora powerhouse targeted late 2027/2028 at earliest; zero positive FCF within 3–5 years) = **Est. 3Y Annualized Operating IRR: `-18.0%`**.
3. **Dilution Gate (`A1`, `G3`, `H3`):** **HARD FAIL (`A1`, `G3`).** Substantial YoY share count expansion (`>25%` YoY) via post-SPAC equity offerings and ATM raises to build its `$2.46B` cash reserve.
4. **Capex & FCF Gate (`A3a/b/c`, `G2`, `H1/H3`):** **HARD FAIL (`A3a`, `G2`, `H1`, `H3`).** TTM Company FCF is **`-$275.0M`**; **fails `H1`** because Oklo does not yet have an NRC-licensed operating commercial Aurora reactor (prior combined license application was denied without prejudice in 2022 and re-submitted; non-binding LOIs predominate over binding commercial take-or-pay PPAs), and **fails `H3/H4`** (`≤5Y` quality destination with `≥8%` FCF margin and `20%/yr` 5Y return).
5. **Leverage (`A4`) & Moat/Margin (`A5`):** Net Cash **`$2.46B`** (`A4` pass today). Moat: `None` (unproven commercial reactor licensing & HALEU fuel supply bottleneck).
6. **Insiders & Legal (`#7` / `A7` / `H5`):** Post-SPAC sponsor/insider sales (`H5` watch).
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#11`, `#12`, `H1`, `H3`, `H4`).** `-47.8%` below 200DMA voids `#12` PT leg (`$82.44` PT voided).
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `H1` No Licensed Commercial Product, `A1` Equity Dilution, `A3a` `-$275M` FCF Burn, `H3/H4`, `#12`).** **Indicative Ceiling:** **≤ $11.00** after NRC Combined License approval (`H1`) and binding multi-year commercial PPAs (`H3/H4`).

---

#### 9. `SMR` — NuScale Power Corporation (`[NEW DISCOVERY]` — Route `H` Pre-Commercial SMR)
1. **Market Data & Price Health (`PH`):** Price `$8.40`, Market Cap `$2.60B`, 200DMA `$11.68` (**`-28.1%` below 200DMA — voids `#12` PT leg!**), 3Y/Lifetime High `~$32.00` (drawdown `~73.8%`). **`PH-warning`**.
2. **25% 3-Year IRR Math:** Pre-commercial SMR developer (after UAMPS CFPP cancellation, reliant on RoPower Romania FEED study and prospective datacenter MOUs; negative FCF for next 3–5 years) = **Est. 3Y Annualized Operating IRR: `-20.0%`**.
3. **Dilution Gate (`A1`, `G3`, `H3`):** **HARD FAIL (`A1`, `G3`, `H3`).** Share count expanded **`>100%` over recent cycles** via massive ATM equity programs, secondary offerings, and Fluor stake monetization to raise `~$1.0B` cash.
4. **Capex & FCF Gate (`A3a/b/c`, `G2`, `H1/H3`):** **HARD FAIL (`A3a`, `G2`, `H1`, `H3`).** Deeply negative TTM and NTM FCF; **fails `H1`** (while NuScale holds an NRC Design Certification for its 50/77 MWe module, it has **zero deployed commercial plants and zero binding post-FID utility construction contracts** after the UAMPS cancellation) and **fails `H3/H4`**.
5. **Leverage (`A4`) & Moat/Margin (`A5`):** Net Cash `~$1.0B` (`A4` pass today, raised via heavy equity dilution). Moat: `Narrow` (NRC Standard Design Approval, but economics challenged by `$9,000+/kW` LCOE escalation vs gas/large nuclear).
6. **Insiders & Legal (`#7` / `A7` / `H5`):** Fluor/insider equity overhang and securities litigation history post-UAMPS cancellation (`H5/A6` fail).
7. **Valuation (`#11`), Asymmetry (`#12`), Print (`#19`):** **HARD FAIL (`#11`, `#12`, `H1`, `H3`, `H4`).** `-28.1%` below 200DMA voids `#12` PT leg (`$12.96` Hold PT voided).
8. **Final Tier & Buy Trigger:** **Tier 3 (Hard Gate Fail: `H1` No Binding Post-FID Commercial Plant, `A1` `>100%` Share Dilution, `A3a` Negative FCF, `H3/H4`, `#12`).** **Indicative Ceiling:** **≤ $3.25** after a binding post-FID utility construction contract (`H1`) and 4Q halt to ATM dilution.

---

## Explicit Structural Exclusions Log (8 Tickers)

### Part A: Pure-Play Balance-Sheet Banks, Lenders & Insurers (Excluded by Policy Gate `#6` & `fintech.md`)

| Ticker | Company | Market Data & `PH` Status | 3Y Rev / EPS CAGR & IRR Math | Dilution (`A1`), FCF (`A3/FT2`), Leverage (`A4`), Moat (`A5`), Insiders (`#7`) | Valuation (`#11`) & Asymmetry (`#12`) | Structural Exclusion & Gate Verdict |
|---|---|---|---|---|---|---|
| **`NU`** | Nu Holdings Ltd. | Price `$18.42`, Mkt Cap `$89.6B`, 200DMA `$17.34` (`+6.2%`), **`PH-clear`** | 3Y Rev `27.8%`, 3Y EPS `29.4%`, IRR `~23.5%` | `A1` Pass (`+0.5%` sh); **OCF `-$2.75B` (`FT2` fail — distorted by consumer loan book originations)**; `$21.5B` net cash (bank deposits); `Wide` LatAm digital bank moat; Cayman foreign filer (`#7`) | `Fwd P/E 21.8x ≤ 38x`, `PEG 0.72 ≤ 1.65`, PT `$22.05` (`+19.7%` — 3¢ shy of `+20%` `#12`) | **EXCLUDED (`#6` & `fintech.md`):** Pure-play consumer credit card & personal-loan balance-sheet bank in Brazil/Mexico/Colombia (`NIM` & credit-loss provisioning drive earnings). |
| **`KNSL`** | Kinsale Capital Group | Price `$364.86`, Mkt Cap `$8.45B`, 200DMA `$410.17` (`-11.0%`), **`PH-clear`** | 3Y Rev `13.2%`, 3Y EPS `14.8%`, IRR `~15.2%` | `A1` Pass (`-0.25%` sh); TTM OCF `$1.05B` (`FT2` insurance float / unpaid loss reserves); Debt `$184M` vs Cash/Inv `$1.2B+`; `Wide` E&S underwriting moat (`~76%` combined ratio); `#7/A7` Pass | `Fwd P/E 16.4x ≤ 38x`, `PEG 1.19 ≤ 2.0`, PT `$454.90` (`+24.7%` `#12` pass), **but 3Y Rev `13.2% < 15%` (`#9`) & EPS `14.8% < 20%` (`#10`)** | **EXCLUDED (`#6`):** Pure-play E&S property & casualty balance-sheet insurer carrying casualty loss-reserve tail risk; also fails full `#9/#10` (`#14a` barred for financials). |
| **`KSPI`** | Kaspi.kz JSC | Price `$82.10`, Mkt Cap `$15.9B`, 200DMA `$87.64` (`-6.3%`), **`PH-clear`** | 3Y Rev `18.5%`, 3Y EPS `15.5%`, Div `+7.5%`, IRR `~18.0%` | `A1` Pass (`0%` dilution); OCF `$1.17B` (`FT2` fail — ~50% of profit from Kaspi Bank BNPL/consumer lending); Net Debt `$1.32B` (incl. Hepsiburada M&A); `Wide` Kazakh super-app moat; `#7` Foreign Filer | `Fwd P/E 6.65x ≤ 38x`, `PEG 0.43 ≤ 2.0`, PT `$106.56` (`+29.8%` `#12` pass) | **EXCLUDED (`#6` & `fintech.md`):** Consumer lending/banking balance sheet generates ~50% of net income, plus Kazakh/Turkish (Hepsiburada) sovereign & FX risk. |
| **`AXP`** | American Express Co. | Price `$343.39`, Mkt Cap `$235.6B`, 200DMA `$340.36` (`+0.9%`), **`PH-clear`** | 3Y Rev `10.1%`, 3Y EPS `14.5%`, Buyback/Div `+3.2%`, IRR `~13.5%` | `A1` Pass (`-2.06%` YoY shares); Reported FCF `$20.2B` (`FT2` fail — `$200B+` card member loans & customer deposits); Net Debt `$11.98B` (`$62.8B` debt vs `$50.8B` cash); `Wide` closed-loop moat; `#7` Pass | `Fwd P/E 19.3x ≤ 38x`, `PEG 1.43 ≤ 2.0`, **fails `#9` (`10.1% < 15%`), fails `#10` (`14.5% < 20%`), fails `#12` (`PT $376.43 = +9.6% < 20%`)** | **EXCLUDED (`#6` & `fintech.md`):** Balance-sheet card lender (`$200B+` loan/receivable book & deposit funding); also fails `#9`, `#10`, and `#12` outright. |

---

### Part B: AI-Adjacent Power, Electrical Grid & Datacenter Cooling Overlaps (Excluded by Non-AI-Capex Diversification Screen Mandate + Audited Against Revision 5)

| Ticker | Company | Market Data & `PH` Status | 3Y Rev / EPS CAGR & IRR Math | Dilution (`A1`), FCF (`A3`), Leverage (`A4`), Moat (`A5`), Insiders (`#7`) | Valuation (`#11`) & Asymmetry (`#12`) | Mandate Exclusion & Rev 5 Gate Verdict |
|---|---|---|---|---|---|---|
| **`VRT`** | Vertiv Holdings Co | Price `$261.97`, Mkt Cap `$100.2B`, 200DMA `$220.00` (`+19.1%`), **`PH-clear`** | 3Y Rev `26.6%`, 3Y EPS `32.5%`, Buyback `-1.0%`, Mult Norm `-11%/yr` = **IRR `17.5%`** | **Fails `A1` (`+1.0%` YoY share dilution > `0.5%`)**; passes `A3a/b/c` (`$1.89B` TTM FCF, `18.5%` margin); passes `A4` (`Net Debt $1.07B / FCF = 0.57x ≤ 2.5x`); `Wide/Narrow` thermal/power moat; `#7` Pass | **Fails `#11`:** Qualifies for High-Velocity (`Rev 26.6% ≥ 25%`, `EPS 32.5% ≥ 30%`), `Fwd P/E 44.3x ≤ 45x`, **but `PEG 1.91 > 1.65` HV ceiling!** (**Only `#14a` starter eligible**); `#12` borderline (`PT $295 = +12.6% < 20%`, `FCF yld 1.9% < 5%`) | **MANDATE EXCLUSION (Pure-Play AI Datacenter Thermal/Power Capex)** + under Rev 5 fails `A1` (`+1.0%` WASO), `#11` Core (`PEG 1.91 > 1.65`), and `#12` (`<20%` PT upside). Needs **≤ $215.00**. |
| **`ETN`** | Eaton Corporation plc | Price `$427.50`, Mkt Cap `$158.8B`, 200DMA `$391.93` (`+9.1%`), **`PH-clear`** | 3Y Rev `10.8%`, 3Y EPS `13.2%`, Buyback/Div `+2.2%`, Mult Norm `-5.6%/yr` = **IRR `9.8%`** | Passes `A1` (`-1.33%` YoY shares); passes `A3a/b/c` (`$3.5B+` TTM FCF, `~14%` margin); **HARD FAILS `A4` (`Net Debt $20.6B / FCF $3.5B = 5.89x > 2.50x`!)**; `Wide` electrical switchgear moat; `#7` Pass | **Fails `#9` (`10.8% < 15%`), `#10` (`13.2% < 20%`), `#11` (`PEG 2.05 > 2.00`), and `#12` (`PT $474 = +10.9% < 20%`, `FCF yld 2.2% < 5%`)** | **MANDATE EXCLUSION (AI Datacenter Electrical Switchgear Overlap)** + under Rev 5 hard-fails `A4` (`5.89x` leverage), `#9/#10`, `#11` (`PEG 2.05`), and `#12`. Fundamental ceiling **≤ $260.00**. |
| **`GEV`** | GE Vernova Inc. | Price `$996.80`, Mkt Cap `$249.7B`, 200DMA `$850.00` (`+17.3%`), **`PH-clear`** | 3Y Rev `13.5%`, 3Y EPS `35.0%`, Buyback `+2.3%`, Mult Norm `-15%/yr` = **IRR `19.2%`** | Passes `A1` (`-2.33%` YoY shares); passes `A3a/b/c` (FCF surging toward `$11.5B–$12.5B` on gas turbine/grid downpayments); passes `A4` (Net Cash `~$8B+`); `Wide` heavy-duty gas turbine & HVDC grid moat; `#7` Pass | Qualifies for High-Velocity `#11` (`3Y EPS 35% ≥ 30%`, `Fwd P/E 43.1x ≤ 45.0x`, `PEG 1.33 ≤ 1.65`) & `#10` (`35% EPS ≥ 20%` + `Wide` moat) & `#12` (`PT $1,230 = +23.4%`), **but `43.1x` P/E leaves `<25%` 3Y IRR (`19.2%`)** | **MANDATE EXCLUSION (Already Covered in `power_platforms.md` / AI Gas Turbine & Grid Capex Overlap)**. Under Rev 5, requires pullback to **≤ $810.00** (`Fwd P/E ≤ 35x`) for a plausible `≥25%` 3Y IRR. |
| **`PWR`** | Quanta Services, Inc. | Price `$686.00`, Mkt Cap `$99.3B`, 200DMA `$595.00` (`+15.3%`), **`PH-clear`** | 3Y Rev `21.5%`, 3Y EPS `30.7%`, Buyback `-0.8%`, Mult Norm `-11%/yr` = **IRR `18.8%`** | **Fails `A1` (`+0.82%` YoY share count expansion > `0.50%` from bolt-on EPC acquisitions)**; passes `A3a/b/c` (`~$2.1B` TTM FCF, `~8.5%` margin); passes `A4` (`Net Debt $4.2B / FCF $2.1B = 2.0x ≤ 2.5x`); `Wide` utility grid EPC moat | **Fails `#11` Core:** Qualifies for HV (`3Y EPS 30.7% ≥ 30%`), `Fwd P/E 37.5x ≤ 45x`, **but `PEG 1.71 > 1.65` HV ceiling!** (**Only `#14a` starter eligible**); `#12` borderline (`PT $806 = +17.5% < 20%`, `FCF yld 2.1% < 5%`) | **MANDATE EXCLUSION (Already Covered in `power_platforms.md` / AI-Grid EPC Overlap)** + under Rev 5 fails `A1` (`+0.82%` M&A share creep), `#11` Core (`PEG 1.71 > 1.65`), and `#12` (`+17.5% < 20%`). Needs **≤ $635.00**. |

---

## Summary of Actionable Watchlist Triggers (`Tier 2` Candidates from Batch 3)

1. **`TW` (Tradeweb Markets — Lane 7 `[NEW DISCOVERY]`):**  
   - **Why It's #1 in Batch 3:** Zero debt (`$1.91B` net cash), `~51%` Company FCF margin (`$1.14B` TTM FCF), `Wide` institutional electronic fixed-income network moat, `+0.13%` YoY shares (`A1` pass), and `Fwd P/E 25.51x` / `PEG 1.62` (`#11` pass).  
   - **Exact Trigger:** Pullback to **≤ $82.00** (delivers `≥5.0%` NTM FCF yield for `#12` and `25.4%` 3Y IRR) **AND** a quarterly print guiding organic revenue growth to `≥15.0%` (`#9`) or NTM 3Y EPS CAGR to `≥20.0%` (`#10` under `FT1`).
2. **`SCHW` (Charles Schwab — Lane 7 `[NEW DISCOVERY]`):**  
   - **Why It's #2 in Batch 3:** Clears `#10` (`22.72%` 3Y EPS CAGR ≥ 20% with `Wide` `$10T+` custodial moat), `#11` (`Fwd P/E 14.9x`, `PEG 1.35`), and `#12` (`PT $121.86 = +26%`).  
   - **Exact Trigger:** Wait for the trailing 12-month roll-off of the Q1/Q3 2026 4-officer non-`10b5-1` discretionary sales (**post-Q3 2027**) and buy at **≤ $88.00–$95.00** (`≥25%` 3Y IRR).
3. **`KAP.L` (Kazatomprom GDR — Lane 9 `[NEW DISCOVERY]`):**  
   - **Why It's #3 in Batch 3:** Only commodity uranium producer on Earth that passes `F1` valuation and margin gates (`Fwd P/E 10.8x ≤ 15`, `EV/EBITDA 7.28x ≤ 11`, `EBITDA margin 52% ≥ 30%`, `FCF margin 24% ≥ 10%`, net cash).  
   - **Exact Trigger:** Pullback to **≤ $52.00** (`≥25%` 3Y EPS + `~6%` dividend IRR) **AND** a qualifying `F2` open-market CEO/CFO purchase (`≥$2M` & `≥5%` holding increase) + 1Q token share repurchase (`F1`).
4. **`ASTS` (AST SpaceMobile — Lane 8 Seed `H-watch`):**  
   - **Why It's on `H-watch`:** Direct-to-device cellular broadband satellite pioneer with binding AT&T, Verizon, and Vodafone commercial agreements (`H1`).  
   - **Exact Trigger:** (1) Clean Q3 2026 print lifting the `#19a` earnings-miss blackout (`-8.64%` Q2 miss), (2) non-dilutive Ex-Im/FirstNet financing closing the `$1.71B` `H2` 24-month stressed funding gap, (3) resolution of W.D. Tex. securities litigation (`H5`), and (4) entry at **≤ $22.00** (`H4` 20%/yr 5Y return math).
