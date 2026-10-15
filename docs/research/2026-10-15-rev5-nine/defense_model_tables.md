
## Explicit annual H3/H4 sensitivities (researcher assumptions, not consensus)

The reproducible model is `defense_model.py`, with full inputs/outputs in `defense_model.json`. All dollar and share totals below are millions. These are annual buckets ending Oct 15, 2027–2031. The first buckets use fiscal-year evidence as proxies, not a verified NTM roll. Cash starts from the last reported balance adjusted for known transactions: AVAV $547.384M after campus and paid holdback; KRMN $54.741M after Walker financing/purchase and an assumed $2M fee. Neither is asserted to be actual Oct 15 cash.

Anchors: AVAV issuer FY27 revenue $2.125–$2.225B; vendor FY27 $2.20B, FY28 $2.54B and FY27 FCF −$89.19M ([forecast](https://stockanalysis.com/stocks/avav/forecast/)). KRMN issuer FY26 revenue $730–$745M / capex $35–$38M and vendor FY26/FY27 revenue $741.30M/$948.84M ([forecast](https://stockanalysis.com/stocks/krmn/forecast/)). AVAV base Y1 company FCF is calibrated to the vendor forecast; later cash forecasts are entirely our estimates.

OCF = EBIT − cash interest − 25% cash tax on positive EBIT after interest + D&A + assumed noncash SBC − incremental working-capital use. Company FCF = OCF − all cash PP&E. Funding cash further deducts capitalized software, award-tax cash settlements and finance-lease principal. Noncash SBC addback is assumed at 2% of revenue for AVAV and 0.5% for KRMN; award-tax cash settlement is separately funded, and ordinary dilution is modeled. D&A assumptions and all operating margins are explicit in JSON. Bear working capital adds cash-collection/stranded-inventory stress of $100/$40/$20/$0/$0M for AVAV and $20/$20/$10/$0/$0M for KRMN on top of the incremental-revenue requirement; this prevents lower sales from mechanically becoming a stronger cash case. Operating rent remains in operating expenses. Terminal EV uses unlevered cash FCF after software/award cash costs; add retained cash once and subtract notes, drawn revolvers and remaining finance leases. No dividends, repurchases or further M&A are assumed; future capacity additions are assumed funded through modeled cash PP&E rather than new finance leases. This annual H3/H4 path does not apply H2’s 25% overrun buffer or prove quarterly liquidity: the separate H2 stress remains binding.

| Name / scenario | FY31 value | 5Y annualized return | Conditional 20% hurdle ceiling | FY31 company FCF margin | FY31 net debt / company FCF | Funding / cap flags |
|---|---:|---:|---:|---:|---:|---|
| AVAV bear | $14.09 | -34.9% | $5.66 | 4.0% | 2.58× | first24 gap=False; cap breach=False |
| AVAV base | $181.34 | 8.5% | $72.88 | 12.9% | -1.53× | first24 gap=False; cap breach=False |
| AVAV bull | $437.18 | 29.4% | $175.69 | 17.9% | -1.95× | first24 gap=False; cap breach=False |
| KRMN bear | $11.65 | -17.3% | $4.68 | 8.8% | 6.57× | first24 gap=False; cap breach=False |
| KRMN base | $61.11 | 15.2% | $24.56 | 16.7% | -0.12× | first24 gap=False; cap breach=False |
| KRMN bull | $123.46 | 32.6% | $49.62 | 19.5% | -1.05× | first24 gap=False; cap breach=False |

### AVAV: annual assumptions and cash/share bridge

| Case / year | Revenue | EBIT margin | Cash PP&E | ΔWC use | Company FCF | Cash after other uses | Mandatory note principal | Optional note principal | New equity $ | End cash | End debt + finance leases | FD shares |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bear 2027 | 1980.0 | -2.0% | 178.2 | 100.5 | -159.9 | -214.3 | 0.0 | 0.0 | 0.0 | 328.3 | 747.5 | 55.88 |
| bear 2028 | 2000.0 | 0.0% | 140.0 | 43.0 | -23.0 | -63.0 | 0.0 | 0.0 | 0.0 | 265.3 | 747.5 | 57.49 |
| bear 2029 | 2100.0 | 3.0% | 126.0 | 35.0 | 33.2 | -8.8 | 0.0 | 0.0 | 0.0 | 256.5 | 747.5 | 59.14 |
| bear 2030 | 2205.0 | 5.0% | 110.2 | 15.8 | 89.0 | 44.9 | 747.5 | 0.0 | 159.1 | 50.0 | 337.0 | 63.50 |
| bear 2031 | 2315.2 | 6.0% | 115.8 | 16.5 | 93.1 | 46.8 | 0.0 | 0.0 | 0.0 | 73.4 | 313.6 | 65.33 |
| base 2027 | 2200.0 | 0.5% | 176.0 | 96.8 | -89.2 | -149.7 | 0.0 | 0.0 | 0.0 | 392.9 | 747.5 | 55.36 |
| base 2028 | 2540.0 | 8.0% | 152.4 | 10.2 | 193.0 | 142.2 | 0.0 | 0.0 | 0.0 | 535.1 | 747.5 | 56.42 |
| base 2029 | 2921.0 | 11.0% | 146.1 | 11.4 | 288.0 | 229.6 | 0.0 | 0.0 | 0.0 | 764.6 | 747.5 | 57.50 |
| base 2030 | 3300.7 | 13.0% | 132.0 | 11.4 | 376.4 | 310.4 | 747.5 | 0.0 | 0.0 | 327.6 | 0.0 | 58.61 |
| base 2031 | 3696.8 | 15.0% | 147.9 | 11.9 | 477.9 | 404.0 | 0.0 | 0.0 | 0.0 | 731.6 | 0.0 | 59.73 |
| bull 2027 | 2225.0 | 2.0% | 166.9 | 5.0 | 39.5 | -21.7 | 0.0 | 0.0 | 0.0 | 520.9 | 747.5 | 54.84 |
| bull 2028 | 2700.0 | 10.0% | 148.5 | 9.5 | 260.5 | 206.5 | 0.0 | 0.0 | 0.0 | 727.4 | 747.5 | 55.36 |
| bull 2029 | 3375.0 | 15.0% | 151.9 | 13.5 | 450.6 | 383.1 | 0.0 | 0.0 | 0.0 | 1110.5 | 747.5 | 55.89 |
| bull 2030 | 4050.0 | 19.0% | 162.0 | 13.5 | 644.6 | 563.6 | 747.5 | 0.0 | 0.0 | 926.6 | 0.0 | 56.43 |
| bull 2031 | 4860.0 | 21.0% | 170.1 | 16.2 | 870.7 | 773.5 | 0.0 | 0.0 | 0.0 | 1700.2 | 0.0 | 56.97 |

### KRMN: annual assumptions and cash/share bridge

| Case / year | Revenue | EBIT margin | Cash PP&E | ΔWC use | Company FCF | Cash after other uses | Mandatory note principal | Optional note principal | New equity $ | End cash | End debt + finance leases | FD shares |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bear 2027 | 800.0 | 15.0% | 48.0 | 40.5 | 16.8 | 7.8 | 13.2 | 0.0 | 0.0 | 50.0 | 953.1 | 136.99 |
| bear 2028 | 920.0 | 16.0% | 50.6 | 62.0 | 13.8 | 4.2 | 8.6 | 0.0 | 0.0 | 50.0 | 943.9 | 141.10 |
| bear 2029 | 1012.0 | 17.0% | 50.6 | 42.2 | 48.5 | 38.4 | 8.6 | 14.9 | 0.0 | 59.8 | 910.3 | 145.33 |
| bear 2030 | 1093.0 | 18.0% | 49.2 | 28.3 | 77.4 | 66.9 | 8.6 | 29.1 | 0.0 | 88.9 | 867.5 | 149.69 |
| bear 2031 | 1180.4 | 19.0% | 47.2 | 30.6 | 103.7 | 92.8 | 8.6 | 42.1 | 0.0 | 131.0 | 811.8 | 154.18 |
| base 2027 | 948.8 | 20.0% | 38.0 | 41.5 | 89.4 | 79.6 | 13.2 | 33.2 | 0.0 | 88.0 | 919.2 | 134.33 |
| base 2028 | 1167.1 | 22.0% | 46.7 | 43.6 | 135.8 | 124.9 | 8.6 | 58.2 | 0.0 | 146.1 | 847.4 | 135.67 |
| base 2029 | 1400.5 | 24.0% | 49.0 | 46.7 | 194.4 | 182.4 | 8.6 | 86.9 | 0.0 | 233.0 | 746.9 | 137.03 |
| base 2030 | 1652.6 | 25.0% | 49.6 | 50.4 | 249.8 | 236.5 | 8.6 | 113.9 | 0.0 | 346.9 | 619.3 | 138.40 |
| base 2031 | 1917.0 | 26.0% | 57.5 | 52.9 | 321.0 | 306.4 | 8.6 | 148.9 | 0.0 | 495.8 | 456.8 | 139.78 |
| bull 2027 | 1000.0 | 22.0% | 40.0 | 38.8 | 116.5 | 106.5 | 13.2 | 46.7 | 0.0 | 101.4 | 905.8 | 133.66 |
| bull 2028 | 1300.0 | 25.0% | 45.5 | 45.0 | 196.1 | 184.5 | 8.6 | 88.0 | 0.0 | 189.4 | 804.2 | 134.33 |
| bull 2029 | 1690.0 | 27.0% | 50.7 | 58.5 | 288.9 | 275.4 | 8.6 | 133.4 | 0.0 | 322.8 | 657.1 | 135.00 |
| bull 2030 | 2197.0 | 28.0% | 65.9 | 76.0 | 387.9 | 371.9 | 8.6 | 181.6 | 0.0 | 504.4 | 461.9 | 135.68 |
| bull 2031 | 2746.2 | 29.0% | 82.4 | 82.4 | 534.5 | 515.8 | 8.6 | 253.6 | 0.0 | 758.0 | 194.6 | 136.36 |

AVAV assumptions: annual ordinary dilution 3%/2%/1% bear/base/bull on an assumed 52M economic starting-share allowance, plus a conservative constant 2.319M conversion reserve. Model share limits: **60M at 24 months; 85M at deadline**. The reserve is intentionally conservative: principal is still paid $747.5M cash in 2030 even though normal net settlement issues only conversion value above principal. Make-whole terms and all awards are not fully verified, so these proposed monitoring caps are not a verified contractual maximum. Revolver use is limited to the reported $336.981M commitment; any later assumed equity is priced $60, unavailable as present H2 liquidity. The annual base company FCF crosses 6% in Y2, has positive OCF throughout, and terminal capex/OCF and net leverage satisfy numeric cash tests; it still requires current and forward organic-demand / insider / legal / G5 validation.

KRMN assumptions: beginning notes include $100M Walker debt, plus $102.139M finance leases. Annual note rate 6%, finance lease 7.29%, revolver 7%; scheduled term principal $8.64M annually plus $4.516M other notes in Y1; finance-lease principal $5.009M annually. Half available cash FCF after mandatory note principal is used for optional deleveraging, with a $50M minimum cash balance. These capital-allocation choices are assumptions, not promises. Ordinary share dilution 3%/1%/0.5% bear/base/bull on a 133M starting allowance; model caps **145M at 24 months; 175M at deadline**. Later equity, if required, is priced $15 and does not count toward current funding. Base company FCF already clears 6% in Y1 and the terminal cash/capex/leverage metrics fit a prospective G destination; actual completed-year cash evidence and the remaining G tests must still be earned.

**Interpretation:** both base operating transitions can reach several numeric G cash-quality targets, but this particular base valuation sensitivity does not clear H4’s 20% hurdle at the Oct14 price. The printed conditional ceilings are outputs of *assumed* 18×/25×/30× bear/base/bull unlevered-FCF multiples, not fully supported intrinsic entry ceilings: profitable-peer validation is incomplete. A different supported operating/multiple case could change that judgment. Do not call either a proven universal valuation failure or an approved H entry. The previous “no annual model” gap is partly addressed by this transparent researcher model; input support, current funding/legal/insider evidence and full route qualification remain unresolved.

A separate failed-commercialization / invalidated-transition case sets equity to **zero** (−100%). At maximum initial H size that is a loss of 0.60% of portfolio / 2.5% of sleeve, or 1.25% / 5% at the total per-name caps. Annual ending balances do not prove intra-year funding sufficiency; the separate H2 slower-revenue stress and current-balance/covenant reconciliation remain required. No probabilities or guaranteed drawdown limits are assigned. H5 unknown means **$0 new capital** regardless of these model values.
