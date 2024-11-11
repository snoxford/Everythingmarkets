import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Fetch historical data
msft = yf.Ticker("MSFT")
spy = yf.Ticker("SPY")
qqq = yf.Ticker("QQQ")

msft_hist = msft.history(period="5y")
spy_hist = spy.history(period="5y")
qqq_hist = qqq.history(period="5y")

# Align dates
data = pd.DataFrame({
    'MSFT': msft_hist['Close'],
    'SPY': spy_hist['Close'],
    'QQQ': qqq_hist['Close']
}).dropna()

data2 = data

print(data.tail(5))
print(data2.tail(5))

# Create target variable (next day's closing price)
data2['MSFT_next'] = data2['MSFT'].shift(-1)
data2 = data2.dropna()
print(data2.tail(5))

# Split the data into features (X) and target (y)
X = data2[['SPY', 'MSFT', 'QQQ']]
y = data2['MSFT_next']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Get the most recent data point
last_row = data.iloc[-1]

# Predict the next day's MSFT price
next_day_features = np.array([[last_row['SPY'], last_row['MSFT'], last_row['QQQ']]])
next_day_prediction = model.predict(next_day_features)
print(next_day_features)
print(next_day_prediction)

# Create a DataFrame for the future prediction
from pandas.tseries.offsets import BDay
future_date = last_row.name + BDay(1)
future_data = pd.DataFrame({
    'Date': [future_date],
    'SPY Prev Close': [last_row['SPY']],
    'MSFT Prev Close': [last_row['MSFT']],
    'QQQ Prev Close': [last_row['QQQ']],
    'Predicted_MSFT': [next_day_prediction[0]]
})

# Display the future prediction DataFrame
print(future_data)
