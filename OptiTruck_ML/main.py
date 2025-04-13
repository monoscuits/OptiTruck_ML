from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from utils.preprocessing import preprocess_input

"""Here goes the main file of the microservice api!
   It is to be connected with the main server made with express
   
   REQUEST FORMAT SHOULD BE => 
   {
  "truck_type": "string",
  "departure_date": "string",
  "from_city": "string",
  "to_city": "string"
    }
       
   RESPONSE FORMAT WOULD BE => 
   
    {
  "predicted_price": integer,
  "predicted_demand": "String"
    }
    
   """
app = FastAPI()

# Load models
price_model = joblib.load("models/price_model.pkl")
demand_model = joblib.load("models/demand_model_class.pkl")  # classification model

class PredictionRequest(BaseModel):
    truck_type: str
    departure_date: str
    from_city: str
    to_city: str

@app.post("/predict")
def predict(data: PredictionRequest):
    print("🚀 Received Input:", data.dict())

    features = preprocess_input(
        data.truck_type,
        data.departure_date,
        data.from_city,
        data.to_city
    )

    price_prediction = price_model.predict([features])[0]
    demand_prediction = demand_model.predict([features])[0]  # returns "Low", "Moderate", or "High"

    return {
        "predicted_price": round(price_prediction, 2),
        "predicted_demand": demand_prediction
    }

