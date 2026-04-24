import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/ecommerce_returns.csv")

# Fill missing values
df.fillna(method='ffill', inplace=True)

# Encode category and size
encoder = LabelEncoder()

for col in ['category', 'size']:
    df[col] = encoder.fit_transform(df[col])

# Save cleaned file
df.to_csv("data/cleaned_data.csv", index=False)

print(df)
print("Preprocessing completed successfully")