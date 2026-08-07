"""
app.py - Streamlit deployment for battery cycle life prediction

WHAT THIS DOES:
Loads our trained model and gives anyone a simple web page where they can
enter a battery cell's early-cycle curve-variance value and get a
predicted cycle life back - no code, no notebook required.

HOW TO RUN LOCALLY:
1. pip install streamlit joblib scikit-learn
2. Make sure battery_model.pkl (from the modeling notebook) is in the
   same folder as this file.
3. In a terminal: streamlit run app.py
4. It opens automatically in your browser at localhost:8501
"""

import streamlit as st
import joblib
import numpy as np
import os

# Load the trained model once, when the app starts
# Model lives in ../models/ relative to this app.py file, matching our
# project structure (models/ folder at the project root)
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "../models/battery_model.pkl")
model = joblib.load(model_path)

st.title("🔋 Battery Cycle Life Predictor")
st.write(
    "Predicts a lithium-ion cell's total cycle life using only its "
    "first 100 cycles of data - based on how much the discharge "
    "capacity curve's shape changes between cycle 10 and cycle 100."
)

st.divider()

# The input - the ONE feature our final model actually uses
qdlin_variance = st.number_input(
    "Qdlin variance (cycle 10 vs cycle 100)",
    min_value=0.0,
    max_value=0.001,
    value=0.00007,
    step=0.00001,
    format="%.6f",
    help="Variance of the point-by-point difference between the "
         "discharge capacity curves at cycle 10 and cycle 100."
)

if st.button("Predict cycle life"):
    prediction = model.predict(np.array([[qdlin_variance]]))[0]
    st.metric("Predicted cycle life", f"{prediction:.0f} cycles")

    st.caption(
        "⚠️ This model's typical error is around ±210 cycles, and it "
        "was trained on only 44 cells from a single battery batch. "
        "Treat this as an early screening signal, not a precise "
        "guarantee - see the project's evaluation writeup for full "
        "details and limitations."
    )

st.divider()
st.caption(
    "Built as part of a full CRISP-DM data science project. "
    "See the [project repo](#) for the complete methodology, "
    "including features that did NOT work and why."
)
