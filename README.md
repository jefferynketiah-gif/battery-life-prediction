# Battery Early-Cycle Life Prediction

Can we predict how many charge cycles a lithium-ion battery will survive, using only its first ~100 cycles of data?

**[Try the live model](https://battery-life-prediction-jrshn3l6arajecjsmbq45y.streamlit.app/)**

## Why this project

Battery manufacturers wait months to learn a cell's true cycle life. This project tests whether early-cycle electrochemical signals can predict total cycle life fast enough to work as a QA screening tool.

Full problem framing: `docs/01_business_understanding.md`

## Data

124 commercial LFP/graphite cells from the MIT/Stanford battery degradation dataset (Severson et al., *Nature Energy*, 2019), cycled to failure under varying fast-charging protocols. This analysis uses Batch 1 (46 cells, 44 after removing censored observations).

Full details and limitations: `docs/02_data_card.md`

## Methodology

Developed using CRISP-DM, with evaluation by 5-fold cross-validation against a dummy baseline throughout.

### Phase 1: Simple features failed

Four standard features (capacity at cycles 10 and 100, capacity fade, internal resistance at cycle 100) were tested with linear and Ridge regression.

**Result:** No model beat the dummy baseline of predicting the mean (MAE 233.5 cycles). Linear regression scored 267.1; Ridge scored 233.6.

**Why:** EDA showed both candidate features had weak, outlier-driven correlations with cycle life — capacity fade dropped from -0.33 to 0.08 once two extreme cells were removed, and internal resistance correlated in the opposite direction to what the physics predicts.

Full writeup: `docs/05_evaluation.md`

### Phase 2: Curve-shape feature engineering

Following the negative result, feature engineering shifted to the approach used in the source paper: the variance in discharge capacity curve shape (`Qdlin`) between cycles 10 and 100, rather than point values.

This feature correlated at -0.59 across all cells, strengthening to -0.625 after removing the two most extreme cells — the opposite pattern to Phase 1's features, indicating a relationship that holds throughout the normal range rather than being propped up by outliers.

**Result:** Using this feature alone, MAE fell to 211.3 cycles, beating the baseline by about 22 cycles. Including it alongside the Phase 1 features performed worse (233.6), indicating the weaker features were actively degrading the model.

Full writeup: `docs/05b_evaluation_v2.md`

## Limitations

- **The improvement is not conclusive.** Fold-to-fold standard deviation was 58.4 cycles — larger than the 22-cycle improvement over baseline. With 44 cells, this result is promising but needs more data to confirm.
- **Single batch, single chemistry.** All cells are LFP/graphite from one batch. Generalization to other chemistries or batches is untested, and the source dataset's batches are known to differ statistically.
- **Censored observations dropped.** Two cells did not reach failure during the experiment; these were excluded rather than handled with survival analysis.
- **The app's curve visualization is illustrative.** It is generated mathematically from the entered variance value, not plotted from a cell's measured data.

## Next steps

- Ingest Batches 2 and 3 to test generalization and expand the sample.
- Handle censored cells with survival analysis rather than exclusion.
- Test additional curve-shape features (minimum, skew) beyond variance.
- Test against other cell chemistries where data is available.

## Project structure

```
app/         Streamlit application
data/        Processed datasets (raw data excluded from version control)
docs/        Problem framing, data card, evaluation writeups
models/      Trained model (battery_model.pkl)
notebooks/   Exploration and analysis, in order
src/         Data extraction and feature engineering scripts
```

## Author

Jeffery Nketiah — applying hands-on electrochemistry and battery research experience (CNRS, PEPR FRISBI) to an applied ML problem.
