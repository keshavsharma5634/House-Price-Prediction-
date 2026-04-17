import streamlit as st
import requests

st.title("🏠 House Price Prediction App")

st.write("Enter house details:")

# Inputs
LotArea = st.number_input("Lot Area", value=4000)
OverallQual = st.slider("Overall Quality", 1, 10, 5)
OverallCond = st.slider("Overall Condition", 1, 10, 5)
YearBuilt = st.number_input("Year Built", value=2000)
TotalBsmtSF = st.number_input("Basement Area", value=800)
GrLivArea = st.number_input("Living Area", value=1500)
FullBath = st.number_input("Full Bathrooms", value=2)
HalfBath = st.number_input("Half Bathrooms", value=1)
GarageCars = st.number_input("Garage Cars", value=2)
GarageArea = st.number_input("Garage Area", value=400)
TotRmsAbvGrd = st.number_input("Total Rooms", value=6)

# Button
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

    response = requests.post("http://127.0.0.1:8000/predict", json=data)

    if response.status_code == 200:
        price = response.json()["predicted_price"]
        st.success(f"💰 Predicted Price: ₹ {price:,.2f}")
    else:
        st.error("Error in prediction ❌")

