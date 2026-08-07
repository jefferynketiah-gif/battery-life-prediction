# Evaluation: Baseline Models (Phase 1)

## What we tested
Using 4 hand-engineered features (`capacity_at_cycle_10`,
`capacity_at_cycle_100`, `capacity_fade_10_to_100`,
`internal_resistance_at_100`) from 44 battery cells, evaluated with
5-fold cross-validation.

## Results

| Model | Average MAE (cycles) |
|---|---|
| Dummy baseline (always predict the mean) | 233.5 |
| Linear Regression (all 4 features) | 267.1 |
| Ridge Regression (all 4 features) | 233.6 |
| Linear Regression (reduced, 3 features) | 263.9 |

## Honest verdict
**None of our models meaningfully beat the dummy baseline.** Ridge tied
it almost exactly; both linear regression variants performed worse.

## Why, most likely
1. **Weak individual features.** Our EDA (see
   `docs/02_data_card.md` and `01_data_understanding.ipynb`) already
   showed both `capacity_fade_10_to_100` and `internal_resistance_at_100`
   have weak, largely outlier-driven correlations with cycle life
   (-0.33/0.08 and 0.158/0.338 respectively).
2. **Redundant features destabilizing linear regression.**
   `capacity_at_cycle_10` and `capacity_at_cycle_100` are highly similar,
   which likely caused unstable coefficient estimates.
3. **Small sample size.** With 44 cells split 5 ways, each fold trains on
   ~35 examples - not much signal for a model to learn from, even if the
   features were stronger.
4. **We used simple summary statistics, not curve-shape features.**
   Published research on this exact dataset (Severson et al., 2019) found
   that the strongest predictor was the *variance in discharge voltage
   curve shape* between cycles 10 and 100 - a more sophisticated feature
   than any raw capacity or resistance value. We have not yet built this.

## Conclusion for this phase
This is a legitimate negative result, not a failed project: it
rigorously demonstrates that simple, "obvious" features are insufficient
for this problem - a finding consistent with prior published research on
this exact dataset. This motivates the next phase: engineering a
curve-shape-based feature grounded in the actual electrochemistry, rather
than continuing to tune models on features already shown to be weak.

**Next:** see `docs/05b_evaluation_v2.md` (after curve-based feature
engineering).
