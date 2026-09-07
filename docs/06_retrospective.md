# Retrospective

## What surprised me

The internal resistance result. Physically, rising internal resistance is a
sign of a cell aging - it impedes current flow, causes voltage drop across
a load, converts stored energy into heat, and shortens runtime before
failure. So I expected a negative correlation with cycle life. Instead the
data showed a weak *positive* one.

My first reaction was to assume I had extracted the data wrong - that a bug
in my process had reversed the relationship. That instinct turned out to be
worth examining rather than acting on immediately. The extraction was
correct; the sample was just small (44 cells) and the signal weak enough
that a wrong-direction correlation was plausible noise. Learning to sit with
"the physics says one thing and this small sample says another" - and to
report that honestly rather than assume my code was broken - was probably
the most useful thing I took from this project.

## What I would do differently

Not much about the sequence. I tested the simple features (capacity fade,
internal resistance) before moving to the curve-shape feature, and although
they failed, that failure is what justified the pivot. If I ran this again
I would still test them first, because knowing what *doesn't* carry signal
is part of knowing what does.

What I would change is the project setup. I started with files scattered
flat in a general projects folder and had to restructure everything later
before pushing to GitHub. Setting up the folder structure and version
control on day one would have saved real time.

## The hardest part

Accepting that the first two features and the initial exploratory charts
were not enough to build a working model on. There was a stretch where the
histogram and both scatter plots were done, the correlations were computed,
and the honest answer was still "none of this predicts anything." Moving
from that to engineering a better feature - rather than tuning models on
weak inputs - was the turning point of the project.

## What I would do with more time

- **Add Batches 2 and 3.** 44 cells is the core limitation. The current
  improvement over baseline (22 cycles) is smaller than the fold-to-fold
  standard deviation (58.4), so more data is the single highest-value
  next step.
- **Handle censored cells properly.** Two cells never reached failure and
  were dropped. Survival analysis would use them rather than discard them.
- **Test other curve-shape features.** Variance was the first one tried;
  minimum and skew of the difference curve are worth testing too.
- **Wire the app's chart to real data.** It currently generates an
  illustrative curve from the variance value rather than plotting a real
  cell's measured curves.

## What I can do now that I could not before

Work consistently through a full project rather than stopping at the first
result that looks good. Concretely: extract data from a nested HDF5 research
file, check whether a correlation is real or driven by outliers, compare a
model against a baseline before believing it, version-control a project, and
deploy a model as a working app - including diagnosing a production failure
from deployment logs.
