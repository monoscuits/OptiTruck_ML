""" Random Forest Regressor and Classifier to predict price and demand state

    this script is responsible for the .pki files in the models folder """


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

# Step 1: Load dataset
df = pd.read_csv("data/training_data.csv")

# Step 2: Convert numerical demand into categories
low_threshold = df["demand"].quantile(0.33)   # ~1100
high_threshold = df["demand"].quantile(0.66)  # ~1400

def categorize_demand(d):
    if d < low_threshold:
        return "Low"
    elif d < high_threshold:
        return "Moderate"
    else:
        return "High"

df["demand_category"] = df["demand"].apply(categorize_demand)


# Step 3: Extract features and labels
X = df[["capacity", "distance_km", "season"]]
y_price = df["price"]
y_demand_class = df["demand_category"]

# Step 4: Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Train-test split
X_train, X_test, y_price_train, y_price_test, y_demand_train, y_demand_test = train_test_split(
    X_scaled, y_price, y_demand_class, test_size=0.2, random_state=42
)

# Step 6: Train models
price_model = RandomForestRegressor(random_state=42)
demand_model = RandomForestClassifier(random_state=42)

price_model.fit(X_train, y_price_train)
demand_model.fit(X_train, y_demand_train)

# Step 7: Save the models and scaler
joblib.dump(price_model, "models/price_model.pkl")
joblib.dump(demand_model, "models/demand_model_class.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("✅ Models trained and saved!")
