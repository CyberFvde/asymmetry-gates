---
name: "fades-sig"
description: "Tony's dip-buy system: 2x funds on giants at 30% down, plain shares of jumpier stars at 40% down, plain gold at 20% down, bitcoin at 50% down, sell fully at a new closing high, with a vehicle check (2x fund, LEAPS or shares) before each leveraged trade. Use when reviewing, rerunning or updating it."
---

# Fades Sig: buy 30% down, exit at the high

Tony's 2x single-stock fund system. Rewritten Nov 10, 2026. The first version (Nov 9, 2026) was a 9Sig-style 90/10 plan that trimmed funds back to target weights. Tony clarified that his real rule is a full exit at a new high, so this version replaces it. Format every answer as headers plus short bullets, plain English, no em dashes. End investing answers with "Not financial advice."

## Core rules
- Entry: buy when the stock closes far enough below its closing high. Tier 1 (giants): 30% or more, bought through the daily 2x fund. Tier 2 (jumpier stars): 40% or more, bought as plain shares.
- Run the price and return screen at every buy, not only the quality gates. A great company at too high a price can sit for years (Microsoft took 16 years to pass its 2000 high; Adobe has not passed its 2021 high as of Nov 2026).
- One buy per name per episode: the whole slot goes in at that name's line (-30% for Tier 1, -40% for Tier 2). No money is held back for deeper levels. Tony chose all-in on Nov 10, 2026.
- Exit: sell the entire position when the stock (not the fund) makes a new closing high. Sell the next trading day. No trimming to a target weight.
- Never sell into a downtrend, except for the forced exits under Universe and the emergency line under Caps. Those override this rule.
- Between trades: hold cash, or use it for another star name that is 30% down.
- 2x funds for Tier 1 only. Tier 2 is bought as plain shares (changed Nov 11, 2026). The settings that stayed under Tony's 50% limit were tested with Tier 2 in plain shares; with Tier 2 in 2x funds the same settings fell about 56% in 2022. A giant whose 2x fund is under $50M is not bought through that fund. Options: only deep in-the-money LEAPS calls, and only when the vehicle check below picks them (changed Nov 11, 2026; the rule used to be no options).
- Leverage follows the discount: about 0x at highs, and between about 1.4x and 2.0x once all the cash is spent, depending on how much of it went to giants.
- Protection swaps (added Nov 11, 2026 after GPT's no-hindsight test). A 2x position is swapped into plain shares of the same stock, at full value, at the next session's open, when either of these happens first: (a) 12 months have passed since entry with no new closing high, or (b) the position is down 60% from the amount first invested. No trim and no top-up. The shares stay plain until the normal new-high exit. This is not an exit from the stock, so it does not break the never-sell-into-a-downtrend rule.
- 12-month switch history (dropped earlier on Nov 11, 2026, then restored as the rule above). Tested by GPT the same day and it did not help: it cost about 3 points a year in 2016 to 2026 and about 1 point in 2000 to 2010, with no change in the worst drop. Dropped: the candidate settings were tested without it. What stays is a plain 12-month business check: rerun the holding gates on any position that has gone 12 months without a new closing high, and sell only on a deal-breaker or a confirmed soft miss. The rest of this bullet is the old rule, kept for reference. Original rule: a 2x position held 12 months without a new closing high gets a holding review. If the business still passes the holding gates, swap the 2x fund for plain shares of the same stock. If the business has failed, sell. Do not go back to 2x on that name before a new closing high. The switch cuts leverage in half, so it also halves the rebound from there. It is not a forced exit, so the no-rebuy rule does not apply to it. A 2x fund loses roughly 17 to 27% a year while a stock sits flat.

## Universe
- Star names only, and only while each passes the asymmetry-gates board on that date. The list is "stocks of this caliber", not a fixed set.
- Tiers are not fixed (Tony, Nov 11, 2026). A name's tier comes from the gates and its ranking score on that date, and it can move up or down. NVDA only became a giant after ChatGPT (2023 on); before that it would have been Tier 2 or off the list.
- Tier 1 (giants) as of Nov 11, 2026: AAPL, MSFT, GOOGL, AMZN, NVDA. NVDA's buy line is about $167.47.
- Proposed written test for giant status, so a backtest can apply it date by date (Claude's proposal, Tony to confirm): passes the gates, is a top-10 index holding, and its worst drop in the current era is under 45%. Everything else that passes is Tier 2. On this test NVDA is Tier 2 through 2022 (it fell 56% in 2018) and Tier 1 from the ChatGPT era on (worst drop since then about 37%).
- AVGO moved to Tier 2 on Nov 11, 2026 (GPT's 54-mix test ran it as Tier 2): it fell about 49% in 2020 and about 42% in 2025, so it behaves like the jumpier names.
- Tier 2 (jumpier stars, added Nov 10, 2026): AVGO, META, ANET, TSM, PANW, CRWD, LLY and others of that caliber that pass. Tony added META on Nov 11, 2026. Tony says he is biased toward cyber names, so run CRWD and PANW through the dilution gate with extra care (heavy stock-based pay).
- Tier 2 2x funds exist (AVGX for AVGO, METU or FBL for META, TSMX or TSMU for TSM, PALU for PANW, CRWL for CRWD, ELIL or LLYX for LLY, ANEL for ANET) but are not used for new buys since Nov 11, 2026. Tier 2 is bought as plain shares. One exception: AVGX already held rides to AVGO's next new closing high.
- Small-fund rule: if the 2x fund is under $50M in size, buy plain shares of that stock in the slot. Sizes seen in Nov 2026: ANEL about $13M, LLYX about $39M, CRWL about $39M, TSMU about $65M, TSMX about $113M. Check the spread too, since size alone doesn't prove a fund trades well. Plain shares bought at -40% still gain about 67% back to the high with no decay and no closure risk.
- Tier 1 funds: AAPU (AAPL), MSFU (MSFT), GGLL (GOOGL), AMZU (AMZN), NVDL or NVDU (NVDA). Before each first buy, check AUM, fees and that the fund still targets 2x.
- Gold and bitcoin are also names in the plan (added Nov 10, 2026). Same idea as the stocks: buy only after a big drop, sell everything at a new closing high.
- Gold: trigger is 20% below its closing high. Its two worst drops of the last decade were about -27% (2026, so far) and -21% (2022). Vehicle: plain gold through a low-cost fund such as GLDM, no leverage. GPT's Nov 10, 2026 test found leveraged gold did no better than plain gold (about 37.5% vs 37.1% a year for the whole plan, same drawdown), so the leverage only adds decay and note risk. SHNY (3x gold note from BMO, about $76M in size) is not used. Capped at 10% of the account (cut from 15% on Nov 11, 2026). Gold from -20% back to its high is +25% per trade, about 2.5 points on the account at a 10% slot, however long it takes. Status Nov 10, 2026: gold near $4,053, about 22 to 26% below its January 2026 high, so the trigger has fired.
- Bitcoin: trigger is 50% below its closing high, bought through a plain spot bitcoin fund such as IBIT with no leverage. Capped at 10% of the account (cut from 15% on Nov 11, 2026: Tony says he understands bitcoin least of all the names, and gold second least). Why -50%: bitcoin fell at least that far in all four of its big drops of the last decade (2018 about -84%, 2021 about -53%, 2022 about -77%, 2026 about -52%), and it lines up with the stocks' -30% once bitcoin's bigger swings are counted. The second-worst-drop rule would give -75%, which may never fire again. After the -50% line bitcoin fell another 54 to 68% twice, so expect that. Status Nov 10, 2026: about $73,700, 41% below the $126,080 high of Oct 6, 2025. The -50% line is about $63,040.
- UBRL (UBER) is the one position left outside the tiers. It is sold in full at UBER's next new closing high, then Tony decides whether UBER stays. The NVDL already held counts as NVDA's Tier 1 slot. NVDU is about 0.1%/yr cheaper than NVDL; NVDL is much larger.
- Buy gates and hold gates are separate (agreed with GPT and Gemini, Nov 11, 2026). Valuation, target-price, entry-timing and price screens only block new buys. They never force a sale. A stock that rises can fail a price screen while the business is fine.
- Forced exits respond to new bad news after the buy, never to information that was already known at the buy.
- Deal-breakers, sell right away even below the high: (1) confirmed financing distress or dilution past the approved limit, (2) financial statements shown to be materially unreliable, not just an allegation, (3) default, funding failure or a breach of the written leverage limit, (4) a documented lasting loss of the business advantage, not an ordinary margin dip.
- Softer miss: ordinary growth, margin or cash-flow slippage. Sell only after two earnings reports in a row confirm it.
- A guidance cut alone is not a deal-breaker. It blocks new buys and triggers a review. It forces a sale only if it breaks a threshold written down for that company in advance.
- No rebuy after a deal-breaker exit until the name makes a new closing high. A new high only unlocks the name. It still needs a fresh dip to its line.
- Gold and bitcoin carry no leverage and no gate, so they wait for their new highs.
- Do not assume from memory which names passed the gates in a past year. Check with the data known on that date.
- UBER check, Nov 10, 2026: Pelosi's spouse bought 200 UBER calls on May 29, 2026 ($50 strike, expiring Mar 19, 2027) and no sale has been disclosed since. Trump's filings show UBER buys early in 2026 and a sale on May 22, 2026. Uber's CEO bought 141,000 shares near $71 in Sept 2026. Waymo moved to end its Uber partnership, and Uber signed Rivian, Nvidia and Zoox robotaxi deals. UBER closed $66.71 on Nov 2, 2026, about 33% below its $100.10 record close. Politician and insider buys are a signal, not a gate.

## Vehicle check before every leveraged trade (added Nov 11, 2026)
- Bottom line (Tony): whatever is used has to be expected to beat simply holding the shares after all costs. If no leveraged vehicle clears that, buy plain shares.
- Tony asks Claude to run this check before each trade.
- Costs to count. A 2x fund: about 10 to 13% a year (roughly a 1% fee plus the swap financing that is not in the expense ratio), plus daily-reset decay of about the stock's yearly swing squared (9 points at 30% swings, 20 points at 45%). A deep in-the-money LEAPS call: time value of about 4 to 6% a year at a strike near half the share price and about 9% a year at roughly 2x exposure, no daily decay, plus the bid-ask gap going in and out. Plain shares: none.
- Check 1, fund size: under $50M, do not use the fund. Under about $100M, the 15% cap applies.
- Check 2, distance and speed: how far the stock is from a new closing high and how long that is likely to take. A rebound expected within about a year favors the 2x fund. A trade likely to run past about 16 months, or one needing 40% or more with no clear trigger, favors LEAPS or plain shares. Evidence: on 17 past giant trades the 2x fund at an 11% cost won the 12 fast ones, and LEAPS won the 5 that took longer than about 16 months.
- Check 3, option prices: look at implied volatility on the real LEAPS chain. Right after a crash it runs high and LEAPS cost more, which leans toward the 2x fund or shares. At normal levels LEAPS are fine.
- Then build the scenario table for that stock: back to its high in 6, 12 and 24 months, flat for a year, and down another 30%, each for shares, the 2x fund and LEAPS. Pick a leveraged vehicle only if it beats shares in the outcomes Tony thinks most likely and he accepts its loss in the down case.
- LEAPS rules: strike about half to two-thirds of the share price (delta about 0.85 or higher), the longest listed expiry and at least 18 months, limit orders near the middle of the bid and ask. Size by share exposure, not dollars paid: one contract controls about 100 shares times delta. When under about 6 months remain and the stock is not back at its high, roll to a later expiry or convert to shares. A LEAPS call loses everything if the stock is below the strike at expiry.
- The protection swaps still apply to any 2x fund position (12 months without a new high, or down 60%).
- Limits: LEAPS figures here come from a pricing formula, not real quotes, and no backtest has used real option prices.
- First use, UBER on Nov 11, 2026: UBER closed $70.68, 29% below its $100.10 record, needing 42% for a new high. UBRL held only about $20M, so it fails check 1. One-month implied volatility was about 35%. A modeled 2-year $35-strike call cost about $39.50 (about 1.7x, about 4% a year to hold). Modeled outcomes for shares, UBRL and that call: back to the high in 6 months +42%, +77%, +71%; in 12 months +42%, +56%, +69%; in 24 months +42%, +21%, +65%; flat for a year 0%, -22%, -5%; down to $50 in a year -29%, -61%, -54%. Read: LEAPS over UBRL. Still to do before acting: check the real chain and expiry, and ask the CPA about the tax side of switching out of UBRL.

## Position sizing
- Budget per name: Tier 1 gets a 25% slot (raised from 20% on Nov 11, 2026 after GPT's 54-mix test). Tier 2 gets a 10% slot. Bitcoin gets up to 10% (cut from 15% on Nov 11, 2026). Gold gets up to 10%.
- A Tier 1 slot drops to 15% when the small-fund cap applies, and to whatever cash is left after that.
- Tier 2 names together: max 40% of the account.
- Giants' reserve: Tier 2, gold and bitcoin together can use at most 60% of the account. The other 40% is held for Tier 1: one full giant slot and most of a second.
- The total never goes above 100% of the account, so five 25% giant slots cannot all fill. Within those limits the first signal gets the cash. Same-day ties go to the name ranked higher on the asymmetry-gates board that day. The Nov 11, 2026 tests broke ties by a fixed list order, and reversing that order moved one top mix by about 3.5 points a year.
- These limits only block new buys. They never force a sale.
- One-day wipeout risk: a daily 2x fund goes to about zero if its stock falls 50% in one day. Apple fell about 52% on Sept 29, 2000. This is why the jumpier names get small slots.
- All of a name's budget goes in at the first rung (-30%). History of this choice on Nov 10, 2026: 50 / 50, then 75 / 25, then all-in after Gemini's 2016 to 2026 estimate (all-in about 18.9% a year, 85 / 15 about 18.4%, 75 / 25 about 17.3%, 50 / 50 about 15.1%).
- Each buy = the full slot, or whatever cash and cap room is left if that is smaller. A partly filled slot is not topped up later in the same episode. This is how the Nov 11, 2026 test ran.
- Positions left over from the first version count toward that name's budget.
- Size the tranches off the account value on the day the first rung fires, and keep those dollar amounts for that episode.
- Any fund under about $100M AUM is capped at 15% of the account (a closure forces a sale). Judge fund size from before the stock's drop, or by average daily trading volume, because a falling fund can shrink under $100M on the day the buy fires.
- Why a ladder and not all-in at -30%: the first name to hit -30% can be the one that keeps falling. AMZN in 2022 fell another 37% past that line, about -65% on a 2x fund. Rough replays across the five names, by size of the first buy: deep 2022-style drop, 50% first buy = account low about -18% and about +81% after the exits, 75% = about -24% and +72%, all-in = about -30% and +63%. Shallow 2025-style drop, 50% = about +46%, 75% = about +59%, all-in = about +72%. Shallow drops are more common (deeper rungs fire in roughly one episode out of three or four), so a bigger first buy earns more on average. The price of all-in: nothing is left to buy lower, and one name that keeps falling can cost about 13% of the account (a 20% slot down 65%). These are estimates, not a backtest.

## Tranche ladder (regime-aware)
1. Window: last 10 years of daily closes (or since IPO). Measure drops from closing highs, not intraday highs.
2. Regime start: the latest of (a) 10 years ago, (b) the first year of sustained positive GAAP net income and positive free cash flow, (c) a user-flagged structural break (major merger, business-model change). Tony counts NVDA's regime from the ChatGPT era (2023 on). Drops from before the current regime don't count.
3. List every drawdown of 20% or more inside the regime, including the current one at its depth so far.
4. Rung 1 = -30%.
5. Rung 2 = the second-deepest drawdown, rounded toward zero to the nearest 5%. Rung 3 = the deepest drawdown, rounded the same way.
6. Drop any rung that is not at least 5 points deeper than the rung before it.
7. Rung price = closing high x (1 + rung).
8. A rung fires once per episode. It re-arms after the stock makes a new closing high.
9. If a rung fires within about 2 weeks before that name's earnings and options are pricing an unusually big move, buy two-thirds of the tranche now and the rest after the print if guidance holds.

## Ladders as of Nov 10, 2026
| Name | Regime | Two worst drawdowns | Rungs | Split |
|---|---|---|---|---|
| AAPL | full decade | -39% (2018-19), -33% (2025) | -30 / -35 | all at -30 |
| MSFT | full decade | -38% (2022), -28% (2020) | -30 / -35 | all at -30 |
| GOOGL | full decade | -44% (2022), -31% (2020) | -30 / -40 | all at -30 |
| AMZN | full decade | -56% (2022), -34% (2018) | -30 / -55 | all at -30 |
| AVGO | full decade | -48% (2020), -42% (2025) | -30 / -40 / -45 | all at -30 |
| NVDA (legacy) | since 2023 | -37% (2025), -27% (2024) | -30 / -35 | no new buys |
| UBER (legacy) | since 2023 (first profitable year) | -31%, -31% | -30 | no new buys |

- The deeper rungs are kept as reference levels only (how far each name has fallen before). No money waits for them.
- AAPL, MSFT and AMZN drawdowns are from memory. Confirm them with a fresh pull on the next rerun and add rung prices.
- Closing highs as of Nov 9, 2026 (10-year, from the asymmetry-gates board): NVDA $239.24, AVGO $481.57, GOOGL $402.62, UBER $100.10. Pull AAPL, MSFT and AMZN highs on the next rerun.
- Status on Nov 9, 2026: AVGO about -39%, GOOGL about -29%, UBER about -31% (UBER $68.59), NVDA about -26% from their highs.
- Full-decade drawdowns kept for reference: NVDA 2018 -56%, 2020 about -38%, 2022 -66%, 2024 about -27%, 2025 about -37%. AVGO 2018 -27%, 2020 -48%, 2022 -35%, 2025 -42%. GOOGL 2018 -23%, 2020 -31%, 2022 -44%, 2025 about -30%. UBER 2024 -28% and -31%.

## Cash
- Idle cash: 80% in SGOV or a money market fund, 20% in JAAA (changed from 50 / 50 on Nov 11, 2026). JAAA can lose value and get harder to sell in a panic, which is when buys fire.
- Spend the SGOV or money market half first when a rung fires. JAAA has dipped 2 to 3% in selloffs, which is when rungs fire.
- Cash is now most of the account at highs, so JAAA's extra yield (about 1.2 points over SGOV in late 2026) matters more than it did at 10% cash.
- No long-duration bond funds such as AGG.
- Return expectations (set Nov 10, 2026). Look-back, 2016 to 2026: GPT's test of the five-stock core, all-in at -30%, made about 25.8% a year with a worst drop of about 29%, against 27.85% and about 35% for simply holding the five stocks. Gemini's estimate was lower, about 19%. GPT's later test with gold, bitcoin and both tiers: 2016 to 2026 about 37.1% a year with a worst drop of about 42%; Tier 1 plus gold and bitcoin only, about 30.5% and 31%; every stock at -30% with 20% slots, about 50.2% and 50%. Same rules in 2000 to 2010: about 1.2% a year with a worst drop of about 47%. Use the good decade as the upside and the bad decade as the stress test, not the forecast. Going forward (revised Nov 11, 2026 after GPT and Gemini pushed back): 15 to 20% a year is the goal, 25% is the stretch, and 30% needs another decade like the last one. For money he must count on, budget 10% and keep flat and losing years in the picture. The tested numbers for the current rules are in the next section. Tony's goal is 25%, or 30% if realistic, in a small high-risk account. The look-back flatters the plan: the five names were picked knowing they won, every dip recovered fast, and the gates were not applied.

## Limit, goal and test results (Nov 11, 2026)
- Status: these settings are the best candidate so far, still under test. They have not shown they beat simply holding the same stocks.
- Tony's limit: the whole account should not fall more than 50% from its peak. Goal: 25% a year, 30% if realistic. He is not living off the account yet, so withdrawals are not modeled. Revisit the settings when he is.
- Test window: March 2009 to Nov 9, 2026 is the base case (Tony's call: he does not expect a pre-2008 style market again). 2008 is kept as a stress check, and it fails (see below).
- Candidate settings, from GPT's 54-mix test: Tier 1 at -30% with 25% slots in 2x funds, Tier 2 at -40% with 10% slots in plain shares, gold 10%, bitcoin 10%, no 12-month swap, no cap on 2x funds.
- Look-back result with every Tier 2 buy in plain shares: 35.4% a year, worst account drop 43.5% (Aug to Dec 2022) with bitcoin capped at 10%. The earlier runs with bitcoin at 15% made 36.1% with a 45.1% worst drop, and the other figures in this section come from those runs. GPT and Claude both reproduced it, and Claude rebuilt every stock trade from the raw prices. A tested 45% drop is not a ceiling on future losses.
- Runners-up: 15% Tier 2 slots made 37.2% with a 48.8% worst drop, only 1.2 points inside the limit. 20% Tier 1 slots made 32.3% with a 40.0% worst drop.
- Start date matters: the candidate made about 29% a year from Jan 2010, 30% from June 2009 and 39% from Jan 2016.
- Benchmark, holding the same 12 stocks as plain shares. Version A: equal weights among the stocks listed at the time, rebalanced each January, about 36% a year with a 34% worst drop. Version B: 12 equal starting slices, unlisted names waiting in cash, never rebalanced, about 33% a year with a 43% worst drop. Either way the dip rules roughly tied on return with an equal or deeper drop.
- The benchmark does not test the gates. Both sides use today's stock list, picked with hindsight.
- Tier 2 in 2x funds breaks the limit: same settings, 40.8% a year with a 55.8% worst drop.
- Caps of 70 or 80% on 2x funds (share of account value, new buys only) cost about 2 to 3 points a year and did not change the worst drop in this window. Not used.
- 2008 stress: all 54 mixes failed, losing 66 to 75% inside 2008 (GPT). The candidate lost 74.6%. Started at the Oct 2007 top, it still made about 25% a year through 2026, after a 74.8% drop.
- What it took to pass 2008: a 30% cap on 2x funds (share of account value, new buys only, no trimming). 2008 drop about 43%, look-back return about 29% a year. Not adopted, since Tony scoped 2008 out. If it is ever added, use this definition.
- Forward return: no look-back makes one dependable. 15 to 20% a year is Claude's guess after cutting the look-back by a third to a half, and GPT calls even that optimistic. For money he must have, the budgeting number stays 10%.
- Limits of the test: today's stock list was used for the whole period, the gates were not applied, the 2x funds are simulated at a 6% yearly cost, taxes and trading costs are left out, and only one deep bear market (2022) falls inside the window.
- Gold and bitcoin check (Claude, Nov 11, 2026): removing gold left the look-back unchanged (36.4% a year against 36.1%); its 2013 buy sat 7 years for a 35% gain. Removing bitcoin cost about 2 points a year (34.0%, worst drop 41.1%); all four closed bitcoin trades at least doubled, which is a thin record. Tony chose to cap both at 10%.
- Credit-spread rule (tested by GPT on Nov 11, 2026, not adopted): at a Tier 1 signal, buy plain shares instead of the 2x fund when the high-yield bond spread is above 6% and higher than 3 months earlier. It cost about 1.5 points a year and cut the 2008 drop from about 75% to about 58%, with no change to the 2022 drop. Parked because the rule is not intuitive to Tony. Claude could not rerun this test.
- Kelly check (from Fortune's Formula): with four 25% Tier 1 slots, giants' 2x funds can reach 100% of the account. On a rough model (a win makes about 90%, a miss loses about 60%) that is about full Kelly if 8 of 10 dip buys recover within 2 years. Half Kelly would be about 55%. No change made.
- Trigger basis: a buy fires on a closing price at or below the line and is bought the next trading day. That is what the tests measured. NVDA touched its $167.47 line intraday on Nov 10, 2026 (low $165.89) and closed at $168.89. Tony counts that buy as fired; if bought, the NVDA slot is filled until a new closing high above $239.24.
- Split test (Claude, Nov 11, 2026, bitcoin at 10%): settings chosen using only March 2009 to 2017, then checked on 2018 to Nov 2026. The candidate ranked 2nd of 54 on the first stretch (32.5% a year, 28.4% worst drop) and made 37.7% with a 43.5% worst drop on the second. The ranking of the 54 mixes was stable across the two stretches (rank correlation 0.84), so the candidate is not a fluke of fitting. Holding the same stocks made 36.3% then 35.6%, with smaller worst drops (19% and 34%), so the rules still have not shown they beat holding. These years were already examined, so this is a stability check, not a clean unseen test.
- Holding a 2x fund for a year at a 6% yearly cost: a stock compounding 15% with 30% yearly swings gives about 14% on the fund, 20% gives about 24%, and 25% gives about 35%. With 45% swings, 20% gives about 11% and 25% gives about 20%. The fund only beats plain shares when the stock compounds more than about 16% (30% swings) or 30% (45% swings). The plan's edge is the rebound from the dip to the high, which is why 2x is used only on dips.
- Reading list closed Nov 11, 2026: The Most Important Thing, Mastering the Market Cycle, Fortune's Formula, Thinking in Bets, Poor Charlie's Almanack, Buffett's letters, The Little Book of Valuation, Fooled by Randomness. GPT's verdict: add only Pardo's The Evaluation and Optimization of Trading Strategies; the next gain comes from testing, not more books.
- Gates note (Tony, Nov 11, 2026): the IRR bar stays at 20%, and names at 25% or more earn a ranking boost. To be added to the asymmetry-gates rankings on his go.
- Exit-rule test (Gemini's idea, from The Art of Execution; run by Claude on Nov 11, 2026). Rule: at a new closing high, swap a giant's 2x fund into plain shares and keep holding, then swap back into the 2x fund at the next close 30% below the high. Trim version: at that swap, also cut the position back to its 25% slot and send the extra to reserve. Tier 2, gold and bitcoin still sell at their highs.
- Why it could work: after the candidate's 16 giant exits, the stock rose over the next 12 months 15 times, by 37% on average.
- Results since 2009, return and worst drop, candidate against the trim version: from March 2009, 35.4% and 43.5% against 40.6% and 45.6%. From 2010, 28.2% against 29.9%. From 2016, 37.7% against 41.2%. From 2018, 37.7% against 37.6%. From 2022, 40.6% against 40.4%. The trim version won 7 of 9 start dates and tied 2, with the worst drop within about 2 points. It also beat holding the same stocks in most windows, the first version to do so. Average reserve fell from about 45% to about 11%.
- Results in the bad decades: with positions held into the 2007 top (start 2003), the candidate lost 69% in 2008, the trim version 72% and the no-trim version 86%. From 2000 to 2026 the candidate made 15.5% a year with a 64.4% worst drop, and the trim version made 16.7% with a 70.5% worst drop. Correction: Claude first reported 11.4% for the trim version. GPT's audit found the cause, and Claude confirmed it: Apple's 2x fund was wiped out on Sept 29, 2000, and Claude's code left that dead zero-dollar position in place, so the rule could never buy Apple again. With the position cleared at Apple's next new high, as the candidate does, both engines give 16.7% and 70.5%. So the trim version beat the candidate on return in every period tested, and its worst drop was 2 to 6 points deeper. Neither version stays under 50% in a 2008-size crash.
- The no-trim version never sells, so cash never returns. From 2009 it held four giants only and ended 72% in Apple. Not recommended.
- Status: rejected on Nov 11, 2026 after GPT's no-hindsight test (see below). Before that test it was the strongest idea for the next version. It reverses Tony's rule of being out at highs, and every result uses today's hindsight stock list. It needs the no-hindsight test first. Claude's swap code matched an independent rebuild of the Apple leg from raw prices to the dollar, and GPT reproduced all three periods on Nov 11, 2026 after the wipeout fix.
- Full test battery on the trim version (Claude, Nov 11, 2026; Tony wants thorough testing before adopting). Every monthly start from March 2009 to Dec 2023 (178 starts): it beat the candidate in 108, with a median edge of only 0.4 points a year; its worst drop across all starts was 46.2% against 45.9%, and never past 50%. Rolling 5-year windows (51): it won 40, median edge 2.8 points, worst 5-year return 15.0% a year against 13.4%. With each giant removed in turn: edge of 5 to 7 points every time, so it does not depend on one stock; worst drop reached 48.3% without Apple. Slot sizes of 15 to 30%: edge of 4.5 to 6 points. Fund cost of 9% and 12%: edge holds (39.5% and 38.5% against 34.2% and 33.0%). Reversed tie order: 36.5% against 32.2%, worst drop 47.3%. Held into the 2000 top (start Feb 1999): same 55.5% drop as the candidate in 2000, then 70.6% against 64.4% in 2008.
- Where the trim version lags: big rebound years, because it has less cash to deploy. It trailed the candidate by 17 points in 2016, 36 points in 2025 and 17 points in 2026 so far, and by 10 to 19 points a year on short windows starting late 2022 or early 2023. It led in 12 of 18 calendar years and had one losing year (2022) against three.
- Still untested, and required before adopting: a no-hindsight universe (for example the five largest US companies by market value at each year start, including ones that later fell), and a check of the 6% cost assumption against real 2x fund prices since 2022.
- No-hindsight test (GPT, Nov 11, 2026, provisional; Claude could not check it because the file did not attach). Tier 1 was replaced by the five largest US-listed companies by market value each Jan 1, including ones that later fell. Since March 2009: candidate 26.2% a year with a 64.9% worst drop, swap rule 13.2% and 55.0%, holding the rotating five 18.6% and 45.1%. Since Jan 2000: candidate 12.3% and 82.2%, swap rule 10.0% and 75.5%, holding 8.0% and 63.5%. Cisco, GE, Citi and PetroChina each lost over 99% in their 2x funds in both 2000-start runs. Provisional because the yearly rankings are not fully verified as known on each Jan 1, and delisted funds need an assumed liquidation rule.
- What it means: the swap rule's edge was hindsight, so it is rejected. The candidate still beat holding the same list on return, but its worst drop broke the 50% limit even after 2009, and a fallen giant held in a 2x fund until a new high can lose nearly everything. That test had no gates, no deal-breaker exits and no 12-month check, so those rules are the main protection and they are still untested.
- Real 2x fund costs (GPT, Nov 11, 2026): fitted yearly drag during each fund's actual 2x period was NVDL 12.8%, GGLL 10.5%, AAPU 9.7%, MSFU 10.1% and AMZU 11.0%, against the 6% used in every test here. At a 12% cost the candidate's hindsight look-back falls from 35.4% to 33.0% a year. Use 10 to 12% in future tests.
- Protection test (GPT, Nov 11, 2026, same provisional no-hindsight list, 11% cost on 2x; Claude could not check the file). Since Jan 2000: no protection 10.8% a year with an 85.5% worst drop and four positions losing 99%; 12-month swap 13.0% and 63.9%; 60% loss swap 12.8% and 70.5%; both 13.3% and 61.0%, with no 99% losses under any of the three. Holding the rotating five made 8.0% with a 63.5% worst drop. Since March 2009: no protection 23.4% and 65.1%; 12-month swap 22.6% and 65.2%; 60% loss swap 23.0% and 62.5%; both 22.8% and 62.6%; holding 18.6% and 45.1%.
- What it means: both swaps together removed the near-wipeouts (Cisco, GE, Citi, PetroChina) and added about 2.5 points a year since 2000 for about half a point since 2009. The 12-month swap looked bad earlier only because every hand-picked stock recovered, so Claude's advice to drop it was wrong. No version gets the worst drop under 50%. Since 2009 the drop barely moves with the swaps, so it comes from how much is in 2x funds at once, which makes sizing the next thing to test on this list.
- Most honest return figures so far: about 23% a year since 2009 and about 13% since 2000, on a no-hindsight list with real fund costs and both swaps. The mechanical top-five list is not Tony's gates, so his own picks could do better or worse.
- LEAPS check (Claude, Nov 11, 2026, formula prices, not real quotes): deep in-the-money LEAPS cost about 4 to 6% a year to hold with no daily-reset decay, against 10 to 13% plus decay for a 2x fund. On the candidate's 17 past giant trades the 2x fund at an 11% cost still won 12, averaging 137% a trade against 128% for LEAPS and 78% for plain shares. LEAPS won the 5 trades that took longer than about 16 months. The plan stays with 2x funds for the dip and no options.

## Caps
- Semis (NVDA + AVGO funds): 50% of the account. Any fund under about $100M AUM: 15%. Gold: 10%. Bitcoin: 10%. Tier 2 together: 40%. Tier 2, gold and bitcoin together: 60%.
- A cap only blocks new buys. Check caps before every buy, and send no new money to a name or group that is over its cap.
- No forced selling below a high because of a cap. Tony chose this on Nov 10, 2026.
- Emergency line: if semis pass 60% of the account, sell back down to 60%. This is the one sale allowed below a high.

## Transition from the first version (Nov 2026)
- First-version targets were NVDL 30%, GGLL 30%, AVGX 15%, UBRL 15%, cash 10%, with NVDL staged at 20% and cash at 20% until NVDA's Nov 17 print.
- Positions bought under the first version (NVDL, GGLL, AVGX, UBRL) ride until each stock's next new closing high, then are sold in full.
- The remaining 2.5% dip tranches from the first version still fire at the old triggers: NVDA $143.54, AVGO $288.94, GOOGL $281.83. UBER's fired at $70.07.
- Cash that was staged for NVDL stays reserved for NVDA through its Nov 17, 2026 report. NVDA's buy line is about $167.47 (30% below its $239.24 high). If NVDA has not closed there after the report, that cash is free for gold, as long as gold is still 20% or more below its record close (the zone starts near $4,255). Tony agreed Nov 10, 2026.
- Gold is bought as plain gold, so there is no decay while it goes sideways.
- No other new buys in a name that is already above its budget.
- After each exit, a name re-enters only through its ladder.

## Fund math worth remembering
- From a rung back to the high the stock gains 1/(1 + rung) - 1: +43% from -30%, +67% from -40%, +122% from -55%.
- A daily 2x fund roughly squares that multiple, then loses to volatility and financing: multiple = (1/(1 + rung))^2 x exp(-(vol^2 + about 5.6%) x years).
- From -30% at about 40% volatility: about 1.8x if the round trip takes 6 months, about 1.65x at 1 year, about 1.3x at 2 years.
- After a rung fires the stock can keep falling. From -30% to -50% is another 29% on the stock and about 49% on that tranche.
- Decay in a daily 2x fund comes from each stock's own volatility. Holding several funds doesn't diversify it away.
- Max-growth leverage per name, for reference: L* = 0.5 + (ln(1 + expected stock CAGR) - borrow cost) / volatility^2. Borrow cost = risk-free rate + about 1.5% (about 5.75% in late 2026).
- Reality check from NVDL: NVDA rose about 10x over NVDL's life; a frictionless 2x would have made about 100x; NVDL made about 17x. Part of that gap is lower leverage, since NVDL and the Direxion funds (GGLL, AAPU, MSFU, AMZU) all launched at 1.5x and moved to 2x in 2024 (GPT, Nov 11, 2026).

## Known costs of this system
- It sits out runs that never dip 30%. NVDA: out near $38 in May 2023, no -30% entry until about $105 in April 2025. AVGO: out near $68 in mid-2023, back in near $175 in 2025.
- These names tend to fall together (2020, 2022, 2025, late 2026), so cash can wait two years between entries and rotation targets are rare outside those windows.
- Held from the highs, the first version's basket lost an estimated 74 to 87% in a 2022-style crash across three models (Claude, Gemini, GPT). This version never holds 2x at a high, so that figure does not apply to it, but nothing here is proven until the backtest is run.

## Taxes
- Every exit is a full sale, often inside a year, so gains are short-term in a taxable account.
- Tony plans to trade tax-free with his CPA (Puerto Rico Act 60 or other routes). Until that is live, set tax aside from each exit before sizing the next buys.
- Act 60 as of Nov 2026: applications filed by Dec 31, 2026 keep the 0% rate, later filings get 4%. Benefits start only in a tax year where he is a bona fide Puerto Rico resident. Gains built before the move don't get the full break. CPA to confirm.

## Open items
- Rerun the test with the gates applied using the data known on each date, including companies that later failed, on later periods, after costs, against holding the same eligible stocks. Compare both return and worst drop. GPT's Nov 11, 2026 test used real daily prices but today's stock list and no gates.
- Settle whether the dip rules beat holding the same list, using fixed IPO and rebalancing rules for the benchmark.
- Confirm AAPL, MSFT and AMZN drawdowns and closing highs with fresh data.
- Tony to confirm: the gate-failure default, the JAAA and SGOV split, the NVDL staging cash, and whether NVDA and UBER stay after their exits.

## Data sources
- Drawdown history: portfolioslab.com/symbol/TICKER (Worst Drawdowns table; check it isn't stale, and fill recent drops from dated news if missing).
- Volatility: alphaquery 180-day historical volatility (close-to-close).
- Prices and closes: stockanalysis.com/stocks/TICKER/history/ (dated closes); stockscan.io as backup.
- Growth: consensus 3-year EPS growth, capped at 35% (same as the board).
- Fund AUM, fees and leverage target: issuer pages (Direxion, GraniteShares, Defiance), stockanalysis ETF pages.
- Cash funds: issuer pages for JAAA and SGOV yields.

## When asked to review or rerun
- Pull fresh closes and recompute each name's drawdown from its closing high.
- Report: rungs fired, exits due at new closing highs, budget used per name, cash split, cap status and current leverage.
- Check for regime changes (profitability flips, big mergers) and recalibrate those ladders.
- Check each universe name against the asymmetry-gates board and flag any that fail.
- Flag any fund whose AUM fell, that announced closure, or that changed its leverage target.
- Re-run each quarter, after each earnings print, and after any regime change.