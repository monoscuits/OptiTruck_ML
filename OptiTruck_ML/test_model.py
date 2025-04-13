""" TESTING THE MODELS TRAINED BY THE FILE 'train_model.py' """

import joblib
from utils.preprocessing import preprocess_input

# Load models and scaler
price_model = joblib.load("models/price_model.pkl")
demand_model = joblib.load("models/demand_model_class.pkl")  # <- classifier
scaler = joblib.load("models/scaler.pkl")

'''

tamper with it for easy fix!!!  

'''


# Insert TEST CASE under this comment!!!

truck_type = "Container trucks"
departure_date = "2024-04-01"
from_city = "Kolkata"
to_city = "Jaipur"


# Preprocess input
features = preprocess_input(truck_type, departure_date, from_city, to_city)
features_scaled = scaler.transform([features])

# Predict price
predicted_price = price_model.predict(features_scaled)[0]

# Predict demand (classification)
demand_label = demand_model.predict(features_scaled)[0]

# Output
print(f"🚚 Predicted Price: ₹{predicted_price:,.2f}")
print(f"📈 Predicted Demand: {demand_label}")




