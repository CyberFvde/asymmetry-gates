# Revision 8 history rerun: Oct 24, 2026

User request (Oct 24, after revision 8): "How about all the other ones that failed period can you check the history of our repo and run em again." Verdicts and the per-ticker table are in [table.md](table.md); the roster summary is in `roster.md` under "Oct 24, 2026: revision 8 history rerun".

## Universe

- Every ticker named in the roster, triggers and research history (208 tokens scanned), minus gate labels and minus the 136 names re-screened earlier the same evening in the [non-AI screen](../2026-10-24-non-ai-rev8/README.md): 98 names in `data/universe.json`.
- Added for completeness: CIEN, META and Samsung (named in the sleeve plan and triage), ABB, Winbond (2344.TW), ESMT (3006.TW), Etron (5351.TWO) from the semis/infra sweeps.
- SATS now trades as ECHO ([EchoStar notice](https://ir.echostar.com/node/33601)).
- Final count: 106 names in four batches.

## Files

- `data/batch_*.json`: stockanalysis statistics and forecast fields at Oct 23 closes, fetched with `?d=20261024`.
  - Currency fixes: TSM EPS per ADR in USD (5 common, USDTWD 32.5853); ASML EUR→USD 1.1202; ABB EPS USD→CHF; SK Hynix scaled to the forward P/E; NVO forecast EPS DKK→USD at 6.6595 (EUR peg); SIVE and KAP.L caps in USD.
  - Winbond, ESMT and Etron figures stay in TWD; the screen's $2.5B floor and D0 were checked by hand in USD.
- `screen.py`: headline hard gates (A–E, FT, G, D with revision 8 D4, M scope, H flag) and the framework C return (lower of the fade path and the 3Y EPS forecast path). Output: `results.txt`.
- `report.py` + `overrides.json`: builds `table.md`. Overrides carry the prior verdict, the revision 8 verdict and the H line.
- `deep/`: deep-check notes with source URLs for the names whose verdict could move: `us_platforms.md` (ANET, APP, TER), `enr.md`, `taiwan.md` (TSM, Winbond), `gfs_nvt.md`.

Run: `python3 -I screen.py data/batch_*.json` and `python3 -I report.py overrides.json data/batch_software.json data/batch_infra.json data/batch_semis.json data/batch_other.json`.

## Results

- **No name is ready for new capital today.** Every headline pass either prints within 5 trading days or failed a deep check.
- **New headline core:** ANET (all checked items pass; A5 conditional; window ≤$192.17, Oct 26 only, else after Nov 3), TER (#13 to Oct 27), STRL (#13 to Oct 28), APP (#19(c) blackout to the Nov 4 print).
- **Near-misses:** GEV (#14a-shaped on P/E 38.8; Oct 28), GNRC (A4 3.0x on trailing FCF; Oct 28).
- **Checked and out:** ENR (A3(b)), GFS (D4 on next-FY EPS +13.7%; D1(c)), NVT (A4 4.3–4.5x), Winbond (A1 convert; D1(c) 10% premium), TSM (A3(c), a downgrade).
- **Unchanged:** held/conditional core, D-watch, G-watch and M-watch names; everything else out with the gate named in `table.md`.

## Limits

- **Next-FY correction:** the first pass tested #9, G2 and D4 on the return base year. `screen.py` now uses the framework's next-FY (year after the last completed FY) and the year after it for D4. The same fix was applied to the non-AI screen; neither screen's tiers changed.
- Headline gates use stockanalysis fields. Its "buyback yield" is net share change, so A2 flags are not decisive; issuance and insider facts come from the roster or the deep checks.
- #13: prints between Oct 26 and Oct 30 block entry now (TER, CDNS, AMKR, HUBB, STRL, GEV, GNRC, KLAC, VRT, SKHY, ALGM, Samsung, NVT and others). Those verdicts are headline status plus "re-test after the print".
- Names carried from the roster with "unchanged" were not re-verified beyond the headline fields unless the deep checks say so.
- Out-year consensus beyond the forecast-page boxes was pulled only for deep-check names; other returns are mechanical.
