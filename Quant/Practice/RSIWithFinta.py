import pandas as pd
import yfinance as yf
import numpy as np
from finta import TA

# Fetch historical data
data = yf.download("AAPL", start="2023-01-01", end="2023-12-31")

# Ensure columns are uppercase
data.columns = [col.upper() for col in data.columns]

# Calculate RSI
data['RSI'] = TA.RSI(data)

# Set buy/sell signals based on RSI
data['Signal'] = np.where(data['RSI'] < 30, 1, np.where(data['RSI'] > 70, -1, 0))

# Display the last few rows of the DataFrame
print(data[['CLOSE', 'RSI', 'Signal']].tail())