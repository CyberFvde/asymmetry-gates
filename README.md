# asymmetry-gates

Rules-based equity screen (gates A–F, rules #1–#19, F signal sleeve) packaged as an Agent Skill.
Source of truth for the rules, the roster and the #15 kill triggers. Keep this repo private — the roster is a position book.

The Oct 2, 2026 calibration keeps structural and concentration safeguards, permits tightly capped starters for narrow growth/valuation shortfalls, and treats small earnings misses as watch items. See the adopted entry in `references/changelog.md` inside the skill. The roster remains historical until re-screened with current data.

## Layout

    .claude/skills/asymmetry-gates/
    ├── SKILL.md                 # when it triggers + how to run a screen
    └── references/
        ├── framework.md         # the rules (change only via a #18 changelog entry)
        ├── triggers.md          # #15 kill triggers, incl. the shared "AI capex 2027" trigger
        ├── roster.md            # dated roster, top-10, what changed — edited every re-test
        └── changelog.md         # #18 log: adopted + pending rule changes with rationale

## Use it

- Claude.ai / Claude app: zip `.claude/skills/asymmetry-gates/` (folder name = skill name) and upload under Customize → Skills. Re-upload after edits.
- Claude Code / Cowork: open this repo as the working directory — project skills under `.claude/skills/` load automatically; invoke with `/asymmetry-gates` or just ask for a screen.
- ChatGPT: in a Project or Custom GPT, paste `SKILL.md` into the instructions and attach the four `references/*.md` files as knowledge (or point it at the raw file URLs if the repo is public). Ask it to read `framework.md` before any screen.

## Editing rules

- `roster.md`: update at every screen; bump the date in the header; keep the "What changed" block.
- `triggers.md`: write a name's #15 line before its first tranche.
- `framework.md`: first add a #18 entry to `changelog.md` (change, rationale, safeguard check, full-universe impact, adoption basis and required re-tests), then apply the text. Explicit user-requested calibration can occur between re-tests; it does not refresh the roster.
- Whoever edits (you, Claude, GPT) commits the full file, not a diff, and checks the roster header date first.
