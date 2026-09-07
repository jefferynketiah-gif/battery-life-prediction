"""
app.py - Streamlit deployment for battery cycle life prediction

WHAT THIS DOES:
Loads our trained model and gives anyone a simple web page where they can
enter a battery cell's early-cycle curve-variance value and get a
predicted cycle life back - with an interactive visualization of the 
underlying discharge curve degradation.
"""

import streamlit as st
import joblib
import numpy as np
import os
import matplotlib.pyplot as plt

# --- PAGE CONFIGURATION & CUSTOM CSS ---
st.set_page_config(page_title="Battery Cycle Life Predictor", page_icon="🔋", layout="centered")

st.markdown("""
    <style>
    /* Clean, modern styling for the main button */
    .stButton>button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        padding: 0.6rem 1rem;
        font-weight: 600;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white;
        border-color: #1d4ed8;
    }
    /* Styling for the prediction output box */
    .prediction-box {
        background-color: #eff6ff;
        border-left: 6px solid #2563eb;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    </style>
""", unsafe_allow_html=True)

# --- LOAD MODEL ---
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "../models/battery_model.pkl")

@st.cache_resource
def load_model():
    return joblib.load(model_path)

model = load_model()

# --- MAIN UI ---
st.title("🔋 Battery Cycle Life Predictor")
st.write(
    "Predicts a lithium-ion cell's total cycle life using only its "
    "first 100 cycles of data—based on how much the discharge "
    "capacity curve's shape changes between cycle 10 and cycle 100."
)

st.divider()

# Layout: Input and button side-by-side
col1, col2 = st.columns([2, 1])

with col1:
    qdlin_variance = st.number_input(
        "Qdlin variance (cycle 10 vs cycle 100)",
        min_value=0.0,
        max_value=0.001,
        value=0.00007,
        step=0.00001,
        format="%.6f",
        help="Variance of the point-by-point difference between the discharge capacity curves at cycle 10 and cycle 100."
    )

with col2:
    st.write("") 
    st.write("")
    predict_clicked = st.button("Predict Cycle Life")

# --- PREDICTION & VISUALIZATION LOGIC ---
if predict_clicked:
    prediction = model.predict(np.array([[qdlin_variance]]))[0]
    
    # Render the result box
    st.markdown(f"""
        <div class="prediction-box">
            <h3 style="margin-bottom: 0px; color: #1e3a8a;">Predicted Lifespan:</h3>
            <h1 style="margin-top: 0px; color: #2563eb;">{prediction:.0f} cycles</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.subheader("📊 Electrochemical Degradation Profile")
    st.write(
        "Visualizing how the discharge capacity profile (`Qdlin`) shifts "
        "between Cycle 10 and Cycle 100 based on this cell's variance metric:"
    )

    # Generate a professional Matplotlib degradation chart
    fig, ax = plt.subplots(figsize=(10, 4.5))
    voltage = np.linspace(2.0, 3.5, 500)
    
    # Representative baseline curve (Cycle 10) and degraded curve (Cycle 100) scaled to user variance
    cycle_10 = 1.1 - 0.1 * np.exp(-5 * (voltage - 2.5)**2)
    degradation_factor = qdlin_variance * 40000 
    cycle_100 = cycle_10 - (0.01 + degradation_factor * 0.04) * np.sin(np.pi * (voltage - 2.0) / 1.5)

    ax.plot(voltage, cycle_10, label="Cycle 10 (Baseline)", color="#2563eb", linewidth=2.5)
    ax.plot(voltage, cycle_100, label="Cycle 100 (Degraded)", color="#dc2626", linewidth=2.5, linestyle="--")
    
    ax.set_xlabel("Voltage (V)", fontsize=11, fontweight='bold')
    ax.set_ylabel("Discharge Capacity (Ah)", fontsize=11, fontweight='bold')
    ax.set_title(f"Discharge Curve Shape Evolution (Variance: {qdlin_variance:.6f})", fontsize=12, fontweight='bold')
    ax.legend(frameon=True, facecolor='#f8fafc', edgecolor='none')
    ax.grid(True, linestyle=":", alpha=0.6)
    
    # Clean visual framing
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    st.pyplot(fig)

st.write("")

# --- DISCLAIMERS & LINKS ---
with st.expander("ℹ️ Model Limitations & Methodology"):
    st.write(
        "⚠️ **Typical error:** ±210 cycles. \n\n"
        "This model was trained on 44 cells from a single battery batch. "
        "Treat this as an early screening signal, not a precise guarantee."
    )
    st.write(
        "Built as part of a full CRISP-DM data science project. "
        "See the [GitHub Repository](https://github.com/jefferynketiah-gif/battery-life-prediction) for the complete methodology, "
        "including features that did NOT work and why."
    )