# asymmetry-gates

Policy revision: **Oct 15, 2026, revision 5**. FT remains the unchanged Oct 2 revision 2 overlay; the roster retains its independent Oct 2 evidence date.

Rules-based equity screen (A–E core, F signal sleeve, G compounders, H early transitions, stricter FT and price-health PH overlays) packaged as an Agent Skill.
Source of truth for the rules, the roster and the #15 kill triggers. Keep this repo private — the roster is a position book.

The Oct 15 #18 calibration targets 25%+ annualized returns in a concentrated, high-asymmetry growth sleeve. It adds a bounded de minimis A1 acquisition/earnout carve-out, a physical-franchise 3a(Q2) branch, a narrowly evidenced Form 4 footnote fallback, and a guidance-only #19(d) watch exemption. Core #11 uses either the complete 38×/PEG 2.0/1.5%-yield standard path or the growth-qualified 45×/PEG 1.65/1.15%-yield alternative; #14a keeps exactly-one-component near-passes within its 48×/2.50/1.0% bands. G/H still require actual cash or funded milestones and a fixed quality destination; FT stays stricter. PH permits a disclosed low-dividend price-return fallback and 10-close recovery with its trend, relative-return and full-route checks. These are preference settings, not a backtested forecast or return promise.

Sizing is at cost unless stated otherwise, and every paired limit applies with AND: starter ≤5.0% sleeve/1.25% portfolio per name (max three, ≤12.5% sleeve aggregate); G initial 5.0%/1.25%, total/name 12.5%/3.0% (max three, aggregate 25%/6.0%); H initial 2.5%/0.60%, total/name 5.0%/1.25% (max two, aggregate 10%/2.5%). Combined starters/G/H/new-entry PH-recovery ≤35%/8%; existing verified A–E Core recovery holdings are excluded from this non-core budget while retaining PH addition restrictions and ordinary name/factor accounting. Shared AI-capex exposure ≤60%/25%. The hard name limit stays 25% sleeve at cost/10% portfolio; a 40% sleeve market weight triggers a trim to 32.5% at the next re-test. Written #15 triggers, maximum vendor-financing/leverage exposure, funding and earned-add conditions remain.

See the adopted entry in `.claude/skills/asymmetry-gates/references/changelog.md` for rationale, full-universe impact and required next-run re-tests, especially TSM, VRT, CDNS, ANET, AMD, LRCX and NVDA. The roster remains byte-for-byte the Oct 2 targeted re-screen plus historical Sep 28 entries; the calibration upgrades no stocks. Draft PR #3's separate revision 4 changes are not included: #12/G3/G5/H4 remain 5%/3%/12%/20% as on merged main. The [March contest research board](docs/research/2026-10-02-march-contest/README.md) keeps speculative contest seeds and option sensitivities separate from skill capital qualification.

## Layout

    .claude/skills/asymmetry-gates/
    ├── SKILL.md                 # when it triggers + how to run a screen
    └── references/
        ├── framework.md         # the rules (change only via a #18 changelog entry)
        ├── stage-paths.md       # G/H funding, valuation, milestones and caps
        ├── fintech.md           # stricter FT routing and cash/risk checks
        ├── price-health.md      # ATH age, relative performance and recovery
        ├── triggers.md          # #15 kill triggers, incl. the shared "AI capex 2027" trigger
        ├── roster.md            # dated roster, top-10, what changed — edited every re-test
        └── changelog.md         # #18 log: adopted + pending rule changes with rationale

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
