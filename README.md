# asymmetry-gates

Policy revision: **Oct 20, 2026, revision 6**. FT remains the Oct 2 revision 2 overlay (only its route names were synced for M); the roster retains its independent Oct 2 evidence date.

Rules-based equity screen (A–E core, F signal sleeve, G compounders, H early transitions, M mega-cap platforms, stricter FT and price-health PH overlays) packaged as an Agent Skill.
Source of truth for the rules, the roster and the #15 kill triggers. Keep this repo private — the roster is a position book.

The Oct 15 #18 calibration targets 25%+ annualized returns in a concentrated, high-asymmetry growth sleeve. It adds a bounded de minimis A1 acquisition/earnout carve-out, a physical-franchise 3a(Q2) branch, a narrowly evidenced Form 4 footnote fallback, and a guidance-only #19(d) watch exemption. Core #11 uses either the complete 38×/PEG 2.0/1.5%-yield standard path or the growth-qualified 45×/PEG 1.65/1.15%-yield alternative; #14a keeps exactly-one-component near-passes within its 48×/2.50/1.0% bands. G/H still require actual cash or funded milestones and a fixed quality destination; FT stays stricter. PH permits a disclosed low-dividend price-return fallback and 10-close recovery with its trend, relative-return and full-route checks. These are preference settings, not a backtested forecast or return promise.

The Oct 20 revision 6 calibration (user request) fixes the 3-year return math and loosens three things. Returns now use forward EPS (base year = first FY ending ≥6 months out), consensus growth with an 85% fade for missing or unverified years, an exit multiple capped at the lower of today's multiple and 30× (35× for 25%+ EPS growers), plus dividends, with no separate buyback add. Placement on a screen's primary ranked list needs a ≥20% base-case estimate (was ≥25% on the old, inflated math); gate eligibility is unchanged by it. #14a's #9 near-pass band drops from 12% to 10% 3Y revenue growth. New route M admits ≥$500B platforms whose FCF is depressed by growth capex at starter size, with OCF, leverage, growth, OCF-yield valuation and a fixed FCF-recovery clock in place of A2/A3/#9/#11, and a +1.5% dilution ceiling that does not require buybacks. On Oct 20 evidence AMZN still fails M's recovery test (consensus FCF margin ~−1% in 2027, ~3% in 2028).

Sizing is at cost unless stated otherwise, and every paired limit applies with AND: starter ≤5.0% sleeve/1.25% portfolio per name (max three, ≤12.5% sleeve aggregate); G initial 5.0%/1.25%, total/name 12.5%/3.0% (max three, aggregate 25%/6.0%); H initial 2.5%/0.60%, total/name 5.0%/1.25% (max two, aggregate 10%/2.5%); M initial 2.5%/0.60%, total/name 5.0%/1.25% (max two, aggregate 10%/2.5%). Combined starters/G/H/M/new-entry PH-recovery ≤35%/8%; existing verified A–E Core recovery holdings are excluded from this non-core budget while retaining PH addition restrictions and ordinary name/factor accounting. Shared AI-capex exposure ≤60%/25%. The hard name limit stays 25% sleeve at cost/10% portfolio; a 40% sleeve market weight triggers a trim to 32.5% at the next re-test. Written #15 triggers, maximum vendor-financing/leverage exposure, funding and earned-add conditions remain.

See the adopted entry in `.claude/skills/asymmetry-gates/references/changelog.md` for rationale, full-universe impact and required next-run re-tests, especially TSM, VRT, CDNS, ANET, AMD, LRCX and NVDA. The roster remains byte-for-byte the Oct 2 targeted re-screen plus historical Sep 28 entries; the calibration upgrades no stocks. Draft PR #3's separate revision 4 changes are not included: #12/G3/G5/H4 remain 5%/3%/12%/20% as on merged main. The [March contest research board](docs/research/2026-10-02-march-contest/README.md) keeps speculative contest seeds and option sensitivities separate from skill capital qualification.

## Layout

    non-ai-screen-audit.md       # full 111-ticker open-universe non-AI-capex gate audit (Oct 15, 2026)
    .claude/skills/asymmetry-gates/
    ├── SKILL.md                 # when it triggers + how to run a screen
    └── references/
        ├── framework.md         # the rules (change only via a #18 changelog entry)
        ├── stage-paths.md       # G/H/M funding, valuation, milestones and caps
        ├── fintech.md           # stricter FT routing and cash/risk checks
        ├── price-health.md      # ATH age, relative performance and recovery
        ├── triggers.md          # #15 kill triggers, incl. the shared "AI capex 2027" trigger
        ├── roster.md            # dated roster, top-10, what changed — edited every re-test
        └── changelog.md         # #18 log: adopted + pending rule changes with rationale

## Non-AI-Capex Diversification Watchlist (Oct 15, 2026 Open-Universe Screen)

Full ticker-by-ticker gate math across 111+ non-AI-capex candidates (9 lanes) is documented in [`non-ai-screen-audit.md`](non-ai-screen-audit.md), with per-name `#15` kill/entry conditions in [`.claude/skills/asymmetry-gates/references/triggers.md`](.claude/skills/asymmetry-gates/references/triggers.md).

Revision 6 note: the 3Y IRR figures below come from the legacy method and are overstated. Corrected estimates (non-AI audit, section 0) put UBER ~16%, HWM ~11%, LLY ~15%, and only ARGX above the 20% guardrail (~22.5%); KOG.OL is unresolved. Gate tiers and triggers are unchanged until a fresh re-test, but check HWM's Standard Core PEG before any entry: its PEG 1.29 implies ~28% growth, and on ~15% forward consensus growth it is ~2.4, above the 2.0 cap.

- **Tier 1 — Gate Passes (Ready Now; legacy `≥25%` 3Y IRR label):**
  - **UBER** (Lane 2 Seed — Waiver `#10` + `#15`): Actionable Now at `$69.62–$71.50` (Buy **`≤ $84.00`**; legacy `~31.5%` 3Y IRR, ~16% on revision 6 math).
  - **HWM** (Lane 1 Seed — Rev 5 Standard Core at `$216.84` / `#14a` Starter at `$231.27`): **Standard Core (`38×` Rev 5) trigger `≤ $221.65–$224.58`**; **Legacy `35×` trigger `≤ $204.15–$206.80`**; **`#14a` Starter (`48×` Rev 5) ceiling `≤ $279.84`** (legacy `~27.8%` 3Y IRR, ~11% on revision 6 math).
  - **LLY** (Lane 4 Seed — `#16` Ballast Slot Pass Now at `$1,142.85`): **Full Core Pass trigger `≤ $1,107.36`** (`+20.0%` PT upside; `0.3551% ≤ 0.50%` Lilly Endowment net selling across 126 Form 4s, `0` discretionary officer sales; legacy `~26.5%` 3Y IRR, ~15% on revision 6 math).
- **Tier 2 — Primary Near-Pass Watchlist (legacy `≥25%` 3Y IRR at Trigger label, Rule A Top 14 Survivors):**
  - **PODD** (`[NEW DISCOVERY]`, Lane 4 — `1-Step Core / G-watch`, spot `$131.69`): **`≤ $126.76`** (blended `5.0%` FCF yield) / **`≤ $108.35`** (full `1.25×` capex fallback) or Nov 4 Q3 capex/GM guide.
  - **NBIX** (`[NEW DISCOVERY]`, Lane 4 — `G-watch`, spot `$143.18`): **`≤ $175.00`** once Oct 27 Q3 print reduces YoY diluted WASO `≤ +3.00%` (currently `+3.17%`, 17bp over merged Rev 5 `G3` cap).
  - **KOG.OL** (`[NEW DISCOVERY]`, Lane 5 — `1-Step Core Watch`, spot `NOK 308.00`): **`≤ NOK 350.30`** (`38×` Core; `≤ NOK 322.66` at `35×`) after a clean Oct 29, 2026 Q3 print exits `#19` blackout.
  - **SAF.PA** (`[NEW DISCOVERY]`, Lane 1 — `G-watch`, spot `~€314.90`): **`≤ €310.00–€323.00`** (`G5` `12.0%` 5Y base return ceiling).
  - **ARGX** (Lane 4 Seed — `G-watch`, spot `$810.00`): **`≤ $785.00`** after Feb 2027 FY26 2nd positive OCF year (`G2`) + AFM/FSMA insider verification.
  - **ATI** (`[NEW DISCOVERY]`, Lane 1 — `#14a / G-watch`, spot `$189.50`): **`≤ $175.00`** + FY27 organic rev consensus `≥ 10.0%`.
  - **WWD** (`[NEW DISCOVERY]`, Lane 1 — `#14a / G-watch`, spot `$331.62`): **`≤ $305.00`** + Nov FY27 FCF guide `≥ $377M` (curing `A3b`/`A4`).
  - **HEI** (Lane 1 Seed — `G-watch`, spot `$302.45`): **`≤ $275.00` (NCI-adjusted) to `$296.00`** (`G5` `12%` 5Y base return ceiling).
  - **CART** (`[NEW DISCOVERY]`, Lane 2 — `#10 / #14a watch`, spot `$49.40`): **`≤ $48.50`** + 3Y EPS CAGR `≥ 20.0%` (`#10`) or 3Y rev `≥ 10.0%` (`#14a`, revision 6; was 12.0%, recorded 11.2%, so re-test the #14a path with next-FY organic ≥10%).
  - **KRYS** (`[NEW DISCOVERY]`, Lane 4 — `G-watch`, spot `$331.80`): **`≤ $275.00`** (`G5` ceiling; `#12` clears at `≤ $326.75`).
  - **ADMA** (`[NEW DISCOVERY]`, Lane 4 — `G-watch`, spot `$10.20`): **`≤ $9.50`** (`G5` ceiling once Mkt Cap `≥ $2.5B` & Form 4s verified).
- **Tier 2 — Rule B Single-Gate / Valuation & Route H Watchlist:** **TW** (`≤ $82.00` + `≥15%` rev / `≥20%` EPS print), **SCHW** (`≤ $95.00` after Q3 2027 `A7` officer roll-off), **ISRG** (`≤ $339.00` `G5` / `≤ $348.40` `PEG ≤ 2.0`), **FTNT** (`≤ $72.24` `G5` / `≤ $69.00` `#12`), **REGN** (`≤ $617.00` `G5`), **CVLT** (`≤ $131.50` `G5`), **CRS** (`≤ $335.00` `G5`), **CRWD** (`≤ $265.24` `G5`), **KAP.L** (`≤ $52.00` + `F2` insider buy + 1Q buyback), **KRMN** (`H-watch ≤ $24.56`), **MDGL** (`H-watch ≤ $397.00`), **AVAV** (`H-watch ≤ $72.88`), **ASTS** (`H-watch ≤ $22.00` after `#19a` exit + `H2` funding).

## Use it

- Claude.ai / Claude app: zip `.claude/skills/asymmetry-gates/` (folder name = skill name) and upload under Customize → Skills. Re-upload after edits.
- Claude Code / Cowork: open this repo as the working directory — project skills under `.claude/skills/` load automatically; invoke with `/asymmetry-gates` or just ask for a screen.
- ChatGPT: in a Project or Custom GPT, paste `SKILL.md` into the instructions and attach all `references/*.md` files as knowledge (or point it at the raw file URLs if the repo is public). Ask it to read `framework.md` and the applicable stage/sector references before a screen.

## Editing rules

- Before rule edits, read `SKILL.md`, this README and every file under `references/`; inspect the roster header date.
- `roster.md`: update at every fresh screen; bump the date in the header and keep the "What changed" block. A between-screen #18 calibration preserves the existing roster content/date and records required re-tests in the changelog.
- `triggers.md`: write a name's #15 line before its first tranche.
- `framework.md`: first add a #18 entry to `changelog.md` (change, rationale, safeguard check, full-universe impact, adoption basis and required re-tests), then apply the text. Explicit user-requested calibration can occur between re-tests; it does not refresh the roster.
- Whoever edits (you, Claude, GPT) commits the full file, not a diff, and checks the roster header date first.

