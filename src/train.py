import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load cleaned data
df = pd.read_csv("data/cleaned_data.csv")

# Features and target
X = df.drop("returned", axis=1)
y = df["returned"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/return_model.pkl")

print("Model trained successfully")