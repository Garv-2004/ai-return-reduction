import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/return_model.pkl")

# Sample customer input
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

# Predict
prediction = model.predict(sample)

# Output
if prediction[0] == 1:
    print("High chance of return")
else:
    print("Low chance of return")