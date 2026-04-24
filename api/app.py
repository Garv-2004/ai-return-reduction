from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load trained model
model = joblib.load("models/return_model.pkl")

@app.get("/")
def home():
    return {"message": "AI Return Prediction API Running"}

@app.post("/predict")
def predict():
    sample = pd.DataFrame([{
        'user_id': 9,
        'product_id': 109,
        'category': 1,
        'price': 1800,
        'size': 2,
        'rating': 4,
        'previous_returns': 3,
        'purchase_frequency': 8
    }])

    prediction = model.predict(sample)

    if prediction[0] == 1:
        result = "High chance of return"
    else:
        result = "Low chance of return"

    return {"prediction": result}