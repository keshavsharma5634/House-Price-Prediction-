import streamlit as st
import joblib
import pandas as pd

# load model
model = joblib.load("models/house_price_model.joblib")

st.title("🏠 House Price Prediction")

# inputs
LotArea = st.number_input("Lot Area", value=4000)
OverallQual = st.number_input("Overall Quality", value=5)
OverallCond = st.number_input("Overall Condition", value=5)
YearBuilt = st.number_input("Year Built", value=2000)
TotalBsmtSF = st.number_input("Basement Area", value=800)
GrLivArea = st.number_input("Living Area", value=1500)
FullBath = st.number_input("Full Bathrooms", value=2)
HalfBath = st.number_input("Half Bathrooms", value=1)
GarageCars = st.number_input("Garage Cars", value=2)
GarageArea = st.number_input("Garage Area", value=400)
TotRmsAbvGrd = st.number_input("Total Rooms", value=5)

if st.button("Predict Price"):

    data = {
        "LotArea": LotArea,
        "OverallQual": OverallQual,
        "OverallCond": OverallCond,
        "YearBuilt": YearBuilt,
        "TotalBsmtSF": TotalBsmtSF,
        "GrLivArea": GrLivArea,
        "FullBath": FullBath,
        "HalfBath": HalfBath,
        "GarageCars": GarageCars,
        "GarageArea": GarageArea,
        "TotRmsAbvGrd": TotRmsAbvGrd
    }

    # feature engineering
    data["Age"] = 2025 - data["YearBuilt"]
    data["TotalBaths"] = data["FullBath"] + 0.5 * data["HalfBath"]
    data["AreaPerRoom"] = data["GrLivArea"] / data["TotRmsAbvGrd"]

    df = pd.DataFrame([data])

    pred = model.predict(df)

    st.success(f"💰 Predicted Price: ₹ {pred[0]:,.2f}")
