"""Reproduce the combined all-share sensitivity cases; no network or trades."""
import json
from pathlib import Path

data = json.loads((Path(__file__).parent / 'combined-data.json').read_text())
seeds = data['seeds']
portfolio = data['paper_portfolio']
assert sum(portfolio['cash_weights_pct'].values()) == 100
assert len({s['ticker'] for s in seeds}) == len(seeds) == 10
assert all(s['currency'] == 'USD' and not s['skill_capital_verified'] for s in seeds)
assert portfolio['option_premium_pct'] == portfolio['borrowed_margin'] == 0
assert all(s['paper_weight_pct'] == portfolio['cash_weights_pct'][s['ticker']] for s in seeds)
returns = {}
for case in ('bear', 'base', 'bull'):
    ending_value = sum(s['paper_weight_pct'] * s['prices'][case] / s['close'] for s in seeds)
    returns[case] = ending_value - 100
    assert abs(returns[case] - portfolio['simultaneous_scenario_returns_pct'][case]) < 1e-8
    for s in seeds:
        assert abs((s['prices'][case] / s['close'] - 1) * 100 - s['returns_pct'][case]) < 1e-8
hwm = next(s for s in seeds if s['ticker'] == 'HWM')
assert abs(hwm['prices']['base'] - 6.46 * 35) < 1e-8
variant = returns['base'] + hwm['paper_weight_pct'] * (6.46 * 40 - hwm['prices']['base']) / hwm['close']
assert abs(variant - data['hwm_multiple_sensitivity']['basket_base_return_pct_at_40x']) < 1e-8
space = sum(s['paper_weight_pct'] for s in seeds if s['ticker'] in ('PL', 'RKLB', 'ASTS'))
assert space == portfolio['space_cost_pct'] == 23
print(json.dumps({'end_assumed': data['model_end_assumed'], 'primary_returns_pct': returns,
                  'hwm_40x_variant_base_pct': variant, 'space_pct': space,
                  'gpcr_only_wipeout_loss_pct': portfolio['cash_weights_pct']['GPCR']}, indent=2))
