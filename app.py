# =========================================================
# IMPORTS
# =========================================================
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Car Mileage Prediction System",
    layout="centered"
)

st.title("🚗 Car Mileage Prediction System")
st.write("Predict City, Average, and Highway mileage")

# =========================================================
# PATHS
# =========================================================
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "cleaned_cars.csv"
MODEL_PATH = BASE_DIR / "models"

# =========================================================
# LOAD DATA (FOR DROPDOWNS)
# =========================================================
df = pd.read_csv(DATA_PATH)

# =========================================================
# LOAD MODELS & FEATURE LISTS (NO CACHE TO AVOID CONFUSION)
# =========================================================
city_model = joblib.load(
    MODEL_PATH / "city_mileage_prediction_final_model.pkl"
)
avg_model = joblib.load(
    MODEL_PATH / "avg_mileage_prediction_final_model.pkl"
)
highway_model = joblib.load(
    MODEL_PATH / "highway_mileage_prediction_final_model.pkl"
)

city_features = joblib.load(
    MODEL_PATH / "city_mileage_prediction_final_model_features.pkl"
)
avg_features = joblib.load(
    MODEL_PATH / "avg_mileage_prediction_final_model_features.pkl"
)
highway_features = joblib.load(
    MODEL_PATH / "highway_mileage_prediction_final_model_features.pkl"
)

# =========================================================
# USER INPUTS — CATEGORICAL
# =========================================================
st.header("🔧 Car Details")

col1, col2 = st.columns(2)

with col1:
    car_body_type = st.selectbox(
        "Car Body Type",
        sorted(df["car_body_type"].dropna().unique())
    )

    fuel_type = st.selectbox(
        "Fuel Type",
        sorted(df["fuel_type"].dropna().unique())
    )

    market_segment = st.selectbox(
        "Market Segment",
        sorted(df["market_segment"].dropna().unique())
    )

with col2:
    driveline_style = st.selectbox(
        "Driveline Style",
        sorted(df["driveline_style"].dropna().unique())
    )

    transmission_type = st.selectbox(
        "Transmission Type",
        sorted(df["transmission_type"].dropna().unique())
    )

# =========================================================
# USER INPUTS — NUMERIC
# =========================================================
st.subheader("📊 Numeric Specifications")

col3, col4 = st.columns(2)

with col3:
    torque = st.number_input("Torque (Nm)", min_value=50.0, step=5.0)
    hp = st.number_input("Horsepower (HP)", min_value=50.0, step=5.0)
    no_of_gears = st.number_input("Number of Gears", min_value=3, step=1)
    displacement = st.number_input("Engine Displacement (cc)", min_value=500.0, step=50.0)

with col4:
    cylinders = st.number_input("Cylinders", min_value=2, step=1)
    car_age = st.number_input("Car Age (years)", min_value=0, step=1)
    length = st.number_input("Car Length (in)", min_value=0.0, step=10.0)
    width = st.number_input("Car Width (in)", min_value=0.0, step=10.0)
    height = st.number_input("Car Height (in)", min_value=0.0, step=10.0)

# =========================================================
# SHARED FEATURE ENGINEERING
# =========================================================
def compute_engineered_features():
    car_volume = length * width * height
    power_index = hp / np.log1p(car_volume)
    return car_volume, power_index

# =========================================================
# GENERIC PIPELINE (USED BY ALL MODELS)
# =========================================================
def build_input(feature_list):
    """
    Builds input dataframe EXACTLY matching
    the feature list used during training.
    """
    X = pd.DataFrame(0, index=[0], columns=feature_list)

    # numeric
    numeric_map = {
        "displacement": displacement,
        "cylinders": cylinders,
        "hp": hp,
        "torque": torque,
        "no_of_gears": no_of_gears,
        "Car_Age": car_age,
    }

    for col, val in numeric_map.items():
        if col in X.columns:
            X[col] = val

    # engineered
    car_volume, power_index = compute_engineered_features()

    if "car_volume" in X.columns:
        X["car_volume"] = car_volume
    if "Power_Index" in X.columns:
        X["Power_Index"] = power_index

    # categorical → one-hot
    categorical_candidates = [
        f"car_body_type_{car_body_type}",
        f"fuel_type_{fuel_type}",
        f"market_segment_{market_segment}",
        f"driveline_style_{driveline_style}",
        f"transmission_type_{transmission_type}",
    ]

    for col in categorical_candidates:
        if col in X.columns:
            X[col] = 1

    return X

# =========================================================
# PREDICTION
# =========================================================
if st.button("🚀 Predict Mileage"):

    X_city = build_input(city_features)
    X_avg = build_input(avg_features)
    X_highway = build_input(highway_features)

    city_pred = city_model.predict(X_city.values)[0]
    avg_pred = avg_model.predict(X_avg.values)[0]
    highway_pred = highway_model.predict(X_highway.values)[0]

    st.success("✅ Prediction Complete")

    c1, c2, c3 = st.columns(3)
    c1.metric("🏙 City MPG", f"{city_pred:.2f}")
    c2.metric("⚖ Average MPG", f"{avg_pred:.2f}")
    c3.metric("🛣 Highway MPG", f"{highway_pred:.2f}")
