# 🔋 Battery Early-Cycle Life Prediction

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://battery-life-prediction-jrshn3l6arajecjsmbq45y.streamlit.app/)

**Can we predict how many charge cycles a lithium-ion battery will survive, using only its first ~100 cycles of data?**

## 📌 The 'Why' Behind the Project
Battery manufacturers currently wait months to know a cell's true cycle life. This project explores whether early-cycle electrochemical signals (specifically, discharge capacity curve variance) can predict total cycle life fast enough to act as a highly efficient QA screening tool.

*Read the full problem framing:* [`docs/01_business_understanding.md`](docs/01_business_understanding.md)

## 🚀 Status: Deployed
The initial modeling phase is complete, and a working prototype is live. 
👉 **[Test the Predictive Model Here](https://battery-life-prediction-jrshn3l6arajecjsmbq45y.streamlit.app/)**

## 📂 Project Structure
- `app/` — The live deployed Streamlit application.
- `models/` — Saved trained model (`battery_model.pkl`).
- `docs/` — Problem framing, data cards, and evaluation writeups.
- `notebooks/` — Step-by-step exploration and analysis.
- `src/` — Reusable code (data loading, feature engineering, modeling).
- `data/` — Raw and processed datasets (excluded from version control).

## 👨‍🔬 Author Background
Written by Jeffery Nketiah, applying hands-on electrochemistry and battery research experience (CNRS, PEPR FRISBI) to a real applied ML problem.

## 📊 Methodology & Insights (CRISP-DM)

This project was developed using the CRISP-DM framework, emphasizing rigorous evaluation over blindly tuning models.

### Phase 1: The Failure of "Simple" Features
Initially, the project tested 4 standard electrochemical features (e.g., capacity fade, internal resistance at cycle 100) across 44 battery cells using 5-fold cross-validation[cite: 3]. 
* **Result:** Linear and Ridge regression models failed to meaningfully beat a dummy baseline (MAE ~233 cycles)[cite: 3]. 
* **Takeaway:** Simple summary statistics and raw capacity values lack the signal necessary for early-cycle prediction[cite: 3].

### Phase 2: Engineering Electrochemical Features (The Solution)
Following the negative results of Phase 1, the feature engineering strategy pivoted to align with published electrochemistry research (Severson et al., 2019)[cite: 3]. Instead of raw point-values, the model evaluates the **variance in discharge voltage curve shape** between cycles 10 and 100[cite: 3]. 
* **Result:** This single, highly sophisticated feature successfully captures the early degradation signals, bringing the model's typical error down to ~±210 cycles. 

### ⚠️ Limitations & Future Scope
The current model was trained on 44 cells from a single battery batch[cite: 3]. While it serves as a powerful proof-of-concept for curve-variance feature engineering, it should be treated as an early screening signal rather than a universal guarantee. Future iterations will aim to ingest broader datasets across different solid electrolytes and cell chemistries.