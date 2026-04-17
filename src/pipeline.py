from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

NUM = [
    "LotArea","OverallQual","OverallCond","YearBuilt",
    "TotalBsmtSF","GrLivArea","FullBath","HalfBath",
    "GarageCars","GarageArea"
]

CAT = [
    "MSZoning","Neighborhood","BldgType","HouseStyle"
]

num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

cat_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", num_pipeline, NUM),
    ("cat", cat_pipeline, CAT)
])