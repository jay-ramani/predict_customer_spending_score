import os
from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Customer Segmentation", layout="centered")
st.title("Customer Segmentation (KMeans)")
st.caption("Pick a saved model from /models, enter values, and predict the cluster.")

MODELS_DIR = Path("models")
if not MODELS_DIR.exists():
    st.error("models/ folder not found. Create it and put your saved model files inside.")
    st.stop()

# Find model files
model_files = sorted(list(MODELS_DIR.glob("*.joblib")) + list(MODELS_DIR.glob("*.pkl")))
if not model_files:
    st.error("No model files found in models/. Add *.joblib or *.pkl files.")
    st.stop()

selected_file = st.selectbox(
    "Choose a model file",
    options=model_files,
    format_func=lambda p: p.name
)

@st.cache_resource
def load_artifact(path: str):
    return joblib.load(path)

artifact = load_artifact(str(selected_file))

# Support either "artifact is pipeline" OR "artifact is dict with pipeline/features"
if hasattr(artifact, "predict"):
    pipeline = artifact
    # If it's just a pipeline, you must manually define features here:
    st.warning("This model file is a raw pipeline. Feature list is not stored. Add features to the saved artifact for easier use.")
    features = st.text_input("Enter feature names (comma-separated)", "annual_income,spending_score")
    features = [f.strip() for f in features.split(",") if f.strip()]
    model_name = selected_file.stem
else:
    pipeline = artifact.get("pipeline")
    features = artifact.get("features", [])
    model_name = artifact.get("model_name", selected_file.stem)

if pipeline is None or not features:
    st.error("This model artifact is missing 'pipeline' or 'features'. Re-save the model including these fields.")
    st.stop()

st.subheader("Model")
st.write(f"**{model_name}**")
st.write("**Features:**", ", ".join(features))

st.subheader("Inputs")
user_inputs = {}
for f in features:
    user_inputs[f] = st.number_input(f, value=0.0, step=1.0)

if st.button("Predict Cluster", type="primary"):
    X_row = pd.DataFrame([[user_inputs[f] for f in features]], columns=features)
    pred = pipeline.predict(X_row)
    cluster_id = int(pred[0])
    st.success(f"Predicted cluster: **{cluster_id}**")
    st.dataframe(X_row)