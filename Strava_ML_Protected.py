import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor

assess = pd.read_csv("personal_data_Moesha.csv")

if "elapsed_time_ss" not in assess.columns:
    raise ValueError("Column 'elapsed_time_ss' not found in the dataset.")

assess["elapsed_time_ss"] = pd.to_numeric(assess["elapsed_time_ss"], errors="coerce")
assess = assess.dropna(subset=["elapsed_time_ss"])

window_size = 4
if len(assess) <= window_size:
    raise ValueError("Dataset is too small for the given window size.")

X = []
y = []

for i in range(len(assess) - window_size):
    X.append(assess["elapsed_time_ss"].iloc[i:i+window_size].values)
    y.append(assess["elapsed_time_ss"].iloc[i + window_size])

X = np.array(X)
y = np.array(y)

split_point = int(0.5 * len(X))
X_train, X_test = X[:split_point], X[split_point:]
y_train, y_test = y[:split_point], y[split_point:]

model = DecisionTreeRegressor(max_depth=4, min_samples_split=4)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")
print("Predictions:", y_pred)

