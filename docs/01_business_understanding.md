# Business Understanding

## 1. The problem, in plain language
Lithium-ion battery manufacturers need to know how many charge cycles a
battery will survive before it degrades too much to use. The only fully
reliable way to know this is to cycle the battery until it actually fails —
which takes **months**.

**Decision this affects:** Should a battery cell design/batch be approved for
production, or does it need rework? Right now, that decision waits on months
of testing per batch.

## 2. Why this matters (the "so what")
Every month spent waiting on a full cycle-life test is a month of delayed
product iteration, delayed manufacturing scale-up, and higher R&D cost.
If we can predict a cell's total cycle life from just its **first ~100
cycles** (roughly 1-2 weeks of testing instead of months), QA teams could
flag likely failures early and make go/no-go decisions dramatically faster.

## 3. What "good enough" looks like
We are not trying to hit 100% accuracy — we're trying to beat the current
alternative, which is "wait months and find out for certain." So success
means:
- The model's prediction error (in cycles) is small enough to be a *useful
  early signal*, even if imperfect.
- We can clearly state the tradeoff: e.g. "predicts cycle life within ±150
  cycles, using data available ~10x faster than waiting for the full test."
- We compare against a naive baseline (see docs/05_evaluation.md later) so
  the improvement is honest, not just "the model has a good R²."

## 4. Who would use this, and how
A battery R&D or QA engineer, as an early screening tool — not a final
replacement for full testing, but a way to prioritize which cells to
watch closely or retest first.

---
*Template note: for any future project, answer these same 4 questions
first. If you can't answer #3 (what does "good enough" mean), you're not
ready to model yet — go find out what the real threshold is.*
