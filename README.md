# Battery Early-Cycle Life Prediction

**Can we predict how many charge cycles a lithium-ion battery will survive,
using only its first ~100 cycles of data?**

## Why this project
Battery manufacturers currently wait months to know a cell's true cycle
life. This project explores whether early-cycle electrochemical signals
(voltage curves, capacity fade, internal resistance) can predict total
cycle life fast enough to be a useful QA screening tool.

Full problem framing: [`docs/01_business_understanding.md`](docs/01_business_understanding.md)

## Status
🚧 In progress — currently on: data acquisition & exploration.

## Project structure
- `docs/` — problem framing, data card, evaluation writeup, retrospective
- `notebooks/` — exploration and analysis, in order (01, 02, 03...)
- `src/` — reusable code (data loading, feature engineering, modeling)
- `app/` — deployed demo (Streamlit)
- `data/` — raw and processed data (not committed — see data/README.md)
- `models/` — saved trained models

## Author's background
Written by [Your Name], applying hands-on electrochemistry and battery
research experience (CNRS, PEPR FRISBI) to a real applied ML problem.
