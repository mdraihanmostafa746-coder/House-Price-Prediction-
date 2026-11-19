
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #08111f 0%, #101d30 100%);
        color: #f1f5f9;
    }

    [data-testid="stSidebar"] {
        background: #0b1525;
        border-right: 1px solid #26364c;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #f8fafc;
        letter-spacing: -1px;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #9aabc0;
        font-size: 16px;
        margin-bottom: 28px;
    }

    .section-card {
        background: #132238;
        border: 1px solid #263b55;
        padding: 22px;
        border-radius: 16px;
        margin-bottom: 18px;
    }

    .result-card {
        background: linear-gradient(120deg, #123b46, #164e63);
        border: 1px solid #28758a;
        padding: 28px;
        border-radius: 18px;
        text-align: center;
        margin-top: 20px;
    }

    .result-label {
        color: #b8dce5;
        font-size: 15px;
    }

    .result-price {
        color: #ffffff;
        font-size: 40px;
        font-weight: 800;
        margin: 8px 0;
    }

    .result-note {
        color: #c3dce4;
        font-size: 13px;
    }

    div.stButton > button {
        background: linear-gradient(90deg, #0e7490, #0891b2);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 25px;
        font-weight: 700;
        width: 100%;
    }

    div.stButton > button:hover {
        background: #0e7490;
        color: white;
        border: none;
    }

    div[data-testid="stMetric"] {
        background: #132238;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #263b55;
    }

    h2, h3 {
        color: #e2e8f0;
    }

    .footer {
        text-align: center;
        color: #71839a;
        font-size: 13px;
        margin-top: 45px;
        padding: 15px;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- LOAD MODEL ----------------

MODEL_PATH = Path(__file__).parent / "models" / "house_price_model.pkl"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    model = load_model()
except Exception as e:
    st.error(f"Could not load the trained model: {e}")
    st.stop()


# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown("## 🏡 House Predictor")
    st.caption("Machine Learning Web Application")

    st.divider()

    st.markdown("### About this project")
    st.write(
        "This application estimates house prices using "
        "a trained Linear Regression model."
    )

    st.divider()

    st.markdown("### Model Information")
    st.write("**Algorithm:** Linear Regression")
    st.write("**Features:** 8")
    st.write("**Training records:** 300")

    st.divider()

    st.markdown("### Technologies")
    st.write("Python · Pandas · Scikit-learn · Streamlit")

    st.divider()

    st.caption("Built as a Machine Learning project.")


# ---------------- MAIN HEADER ----------------

st.markdown(
    '<div class="main-title">Find Your House Value.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Enter the property details below to get an estimated house price.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- INPUT FORM ----------------

st.markdown("### 🏠 Property Information")
st.write("Provide the details of the house.")

with st.form("house_prediction_form"):

    col1, col2 = st.columns(2)

    with col1:
        overall_qual = st.number_input(
            "Overall Quality (1–10)",
            min_value=1,
            max_value=10,
            value=7,
            step=1
        )

        gr_liv_area = st.number_input(
            "Living Area (sq ft)",
            min_value=500,
            max_value=4000,
            value=1500,
            step=50
        )

        garage_cars = st.number_input(
            "Garage Capacity (Cars)",
            min_value=0,
            max_value=4,
            value=2,
            step=1
        )

        total_bsmt_sf = st.number_input(
            "Basement Area (sq ft)",
            min_value=300,
            max_value=2500,
            value=1000,
            step=50
        )

    with col2:
        year_built = st.number_input(
            "Year Built",
            min_value=1950,
            max_value=2023,
            value=2000,
            step=1
        )

        full_bath = st.number_input(
            "Full Bathrooms",
            min_value=0,
            max_value=4,
            value=2,
            step=1
        )

        bedroom_abv_gr = st.number_input(
            "Bedrooms",
            min_value=1,
            max_value=8,
            value=3,
            step=1
        )

        lot_area = st.number_input(
            "Lot Area (sq ft)",
            min_value=1000,
            max_value=20000,
            value=8000,
            step=100
        )

    st.write("")

    submitted = st.form_submit_button(
        "✨ Predict House Price"
    )


# ---------------- PREDICTION ----------------

if submitted:

    input_data = pd.DataFrame([{
        "OverallQual": overall_qual,
        "GrLivArea": gr_liv_area,
        "GarageCars": garage_cars,
        "TotalBsmtSF": total_bsmt_sf,
        "YearBuilt": year_built,
        "FullBath": full_bath,
        "BedroomAbvGr": bedroom_abv_gr,
        "LotArea": lot_area
    }])

    prediction = model.predict(input_data)[0]

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-label">
                Estimated House Price
            </div>
            <div class="result-price">
                {prediction:,.0f}
            </div>
            <div class="result-note">
                Predicted using the trained Linear Regression model
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.markdown("### 📋 Your Property Summary")

    summary1, summary2, summary3 = st.columns(3)

    summary1.metric("Living Area", f"{gr_liv_area:,} sq ft")
    summary2.metric("Bedrooms", bedroom_abv_gr)
    summary3.metric("Bathrooms", full_bath)

    st.caption(
        "Note: This is an estimated value based on a small practice "
        "dataset of 300 records. It is not a guaranteed market price."
    )


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    House Price Prediction · Machine Learning Project
    <br>
    Built with Python and Streamlit
</div>
""", unsafe_allow_html=True)
