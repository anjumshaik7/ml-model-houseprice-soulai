import joblib  # Import joblib to load .pkl files
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

# Load the saved model
model = joblib.load("rf_model.pkl")  # Ensure this path is correct

app = FastAPI()

# Define Pydantic schema for input validation
class HouseFeatures(BaseModel):
    Rooms: int
    Distance: float
    Postcode: float
    Bedroom2: float
    Bathroom: float
    Car: float
    Latitude: float
    Longitude: float
    Propertycount: float
    TotalArea: float
    PropertyAge: float
    Type_t: bool
    Type_u: bool
    Method_S: bool
    Method_SA: bool
    Method_SP: bool
    Method_VB: bool
    Regionname_Eastern_Victoria: bool
    Regionname_Northern_Metropolitan: bool
    Regionname_Northern_Victoria: bool
    Regionname_South_Eastern_Metropolitan: bool
    Regionname_Southern_Metropolitan: bool
    Regionname_Western_Metropolitan: bool
    Regionname_Western_Victoria: bool

@app.post("/predict")
def predict_price(features: HouseFeatures):
    # Convert input to NumPy array and reshape for prediction
    input_data = np.array([list(features.dict().values())]).reshape(1, -1)
    
    # Make prediction
    predicted_price = model.predict(input_data)[0]

    return {"predicted_price": predicted_price}
