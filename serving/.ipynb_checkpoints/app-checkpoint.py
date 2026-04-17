from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# ✅ FIRST define app
app = FastAPI()

# ✅ THEN load model
model = joblib.load("models/house_price_model.joblib")

# schema
class House(BaseModel):
    LotArea: float
    OverallQual: int
    OverallCond: int
    YearBuilt: int
    TotalBsmtSF: float
    GrLivArea: float
    FullBath: int
    HalfBath: int
    GarageCars: float
    GarageArea: float
    TotRmsAbvGrd: int

# routes
@app.get("/")
def home():
    return {"message": "House Price API running 🚀"}

@app.post("/predict")
def predict(h: House):

    d = h.model_dump()

    d["Age"] = 2025 - d["YearBuilt"]
    d["TotalBaths"] = d["FullBath"] + 0.5 * d["HalfBath"]
    d["AreaPerRoom"] = d["GrLivArea"] / d["TotRmsAbvGrd"]

    cols = [
        "LotArea","OverallQual","OverallCond","YearBuilt",
        "TotalBsmtSF","GrLivArea","FullBath","HalfBath",
        "GarageCars","GarageArea","TotRmsAbvGrd",
        "Age","TotalBaths","AreaPerRoom"
    ]

    df = pd.DataFrame([d])[cols]

    # 🔥 FINAL FIX
    pred = model.predict(df.values)

    return {"predicted_price": float(pred[0])}