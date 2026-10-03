# asymmetry-gates

Rules-based equity screen (A–E core, F signal sleeve, G compounders, H early transitions, stricter FT and price-health PH overlays) packaged as an Agent Skill.
Source of truth for the rules, the roster and the #15 kill triggers. Keep this repo private — the roster is a position book.

The Oct 2, 2026 revisions add an evidenced compounder route, a small funded/milestone-based early route with a fixed quality deadline, tougher fintech standards, and a price-health check that makes stale ATHs with prolonged relative weakness affect capital eligibility. They retain the first calibration's capped near-passes and material-miss rules for eligible names. See the adopted entries in `references/changelog.md` inside the skill. The roster now separates an Oct 2 targeted re-screen from historical Sep 28 entries. The [March contest research board](docs/research/2026-10-02-march-contest/README.md) keeps speculative contest seeds and option sensitivities separate from skill capital qualification.

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

- `roster.md`: update at every screen; bump the date in the header; keep the "What changed" block.
- `triggers.md`: write a name's #15 line before its first tranche.
- `framework.md`: first add a #18 entry to `changelog.md` (change, rationale, safeguard check, full-universe impact, adoption basis and required re-tests), then apply the text. Explicit user-requested calibration can occur between re-tests; it does not refresh the roster.
- Whoever edits (you, Claude, GPT) commits the full file, not a diff, and checks the roster header date first.
