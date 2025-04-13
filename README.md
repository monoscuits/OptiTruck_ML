# 🧠 OptiTruck_ML

This is a lightweight **ML microservice** built using **FastAPI** that predicts product **demand level** (`Low`, `Moderate`, `High`) and **price** and helps optimize pricing for a truck booking system. It's designed to work as part of a larger microservice-based backend architecture.

---

## 🚀 What It Does

- 🏷️ Predicts **demand category** based on:
  - Truck type
  - Departure date
  - Source & destination cities
- 🔢 Uses a **classification model** (`RandomForestClassifier`) trained on realistic data
- 📦 Built with **FastAPI** to expose a simple REST API
- 🔁 Ready to integrate with any backend (e.g., Node.js)

---

## ⚙️ Tech Stack

- Python
- FastAPI
- scikit-learn
- pandas
- Uvicorn

---

## 🧪 Example Input

```json
{
  "truck_type": "Mini Truck",
  "departure_date": "2025-05-01",
  "from_city": "Delhi",
  "to_city": "Mumbai"
}
```

## 📈 Example Output

```
{
  "predicted_price: 22691.98,
  "predicted_demand": "High"
}

```

## 🛠️ How to Run

1. Clone the Repo
2. 
```
git clone https://github.com/your-username/ml-demand-predictor.git
cd ml-demand-predictor
```
2. Install Requirements

```
pip install -r requirements.txt
```
3. Start the Server
```
uvicorn main:app --reload

# Your API is now live at http://127.0.0.1:8000
```
