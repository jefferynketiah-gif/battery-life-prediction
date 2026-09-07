# Data Card: MIT/Stanford Battery Cycle Life Dataset

*A data card answers one question before you write any code: "can I trust
this data, and what are its blind spots?" Skipping this is how people
build models that look great and fail in the real world.*

## Source
- Severson, K.A., Attia, P.M., Jin, N. et al. "Data-driven prediction of
  battery cycle life before capacity degradation." *Nature Energy* 4,
  383–391 (2019).
- Official host: https://data.matr.io/1/
- Mirror (easier format for beginners): Kaggle — search
  "MIT Battery Degradation Dataset" or the GitHub repo
  `rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation`

## What it actually is
124 commercial lithium-ion cells (LFP chemistry, 1.1 Ah, 18650 format),
each charged with one of many different fast-charging protocols and
discharged the same way, cycled until failure. Collected in **3 separate
batches** over several months (2017).

## How it was collected (why this matters)
- One initial slow (C/10) reference cycle per cell, then repeated fast
  charge / fixed discharge cycles until the cell died.
- Every cycle recorded: voltage, current, capacity, temperature over time.
- Different cells got different charging protocols on purpose — this is
  what makes "does charging speed affect lifespan" answerable at all.

## Known limitations (write these BEFORE you model, not after)
1. **Single chemistry/format** — all cells are LFP/graphite, 1.1 Ah. A
   model trained here may not generalize to other battery chemistries
   (e.g. NMC, used in most EVs). This must be stated as a limitation, not
   discovered by an embarrassed reviewer later.
2. **Batch effects** — <cite index="7-1">the 3 collection batches have measurably different statistical
   properties, which makes models trained on early batches generalize
   poorly to later ones</cite>. This directly shapes how we must split
   train/test data (batch-aware, not random — more on this in modeling).
3. **Small sample size** — 124 cells is small by ML standards. This limits
   how complex a model we can justify; a documented reason we lean toward
   simpler models first.
4. **Censored observations** — a small number of cells (2 of 46 in the
   first batch we processed) did not reach true failure before the
   experiment ended, so their true `cycle_life` is unknown/missing rather
   than zero or invalid. We drop these for our first-pass model rather
   than guessing a value - a deliberate, documented decision, not a
   silent data-cleaning step. (Proper handling of this would use
   survival-analysis techniques - noted as a future improvement in the
   retrospective.)

## Baseline reality check
<cite index="7-1">Published analysis on this exact dataset found that a simple linear
regression on a small number of hand-engineered features still
outperforms more complex/deep-learning approaches</cite>, largely because
of the batch effects above. **Implication for us:** our own baseline
matters more than usual here — if our fancy model can't beat a simple
linear model, that's a real, honest, reportable finding, not a failure.