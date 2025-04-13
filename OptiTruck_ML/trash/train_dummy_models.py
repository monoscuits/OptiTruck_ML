import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

# Generate dummy training data
X_train = np.array([[10, 200, 1], [20, 300, 2], [30, 150, 0], [40, 500, 3], [50, 600, 2]])
y_price = np.array([1000, 1500, 1200, 2000, 2500])  # Dummy prices
y_demand = np.array([50, 30, 70, 20, 10])  # Dummy demand values

# Train models
price_model = LinearRegression().fit(X_train, y_price)
demand_model = LinearRegression().fit(X_train, y_demand)

# Save models
joblib.dump(price_model, "price_model.pkl")
joblib.dump(demand_model, "demand_model.pkl")

print("Dummy models trained and saved.")
