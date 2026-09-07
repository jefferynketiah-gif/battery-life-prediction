# Evaluation: Curve-Based Feature (Phase 2)

## What we tested
We tested whether `Qdlin_variance_10_100` (the variance in discharge voltage curve shape between cycles 10 and 100) alone could predict cycle life.

## Results
* **Model MAE:** 211.3 cycles
* **Baseline MAE:** 233.5 cycles
* **Improvement:** ~22.2 cycles

## Honest Verdict: Promising but Not Conclusive
The model achieved an MAE of 211.3 cycles, an improvement over the dummy baseline. However, the fold-to-fold standard deviation was 58.4 cycles—larger than the improvement itself. This means the performance gain could plausibly be due to which cells happened to land in which fold, rather than a guaranteed real effect. With only 44 cells, our confidence in this exact number is limited.

Our overall verdict is that this result is promising but not conclusive. The strong, consistent correlation (-0.59, holding even after removing outliers) gives us real reason to trust the underlying electrochemical relationship is genuine. However, the modeling result itself needs more data—ideally Batches 2 and 3 from the same dataset—before we would call this a settled, production-ready tool.