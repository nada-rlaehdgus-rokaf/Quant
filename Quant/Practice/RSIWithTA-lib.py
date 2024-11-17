import pandas as pd
import yfinance as yf
import numpy as np
from finta import TA


data = yf.download("AAPL", start="2023-01-01", end="2023-12-31")
# RSI 계산
data['RSI'] = TA.RSI(data['Close'], timeperiod=14)

# 매수/매도 신호 설정 (예: RSI가 30 이하일 때 매수, 70 이상일 때 매도)
data['Signal'] = 0
data['Signal'] = np.where(data['RSI'] < 30, 1, np.where(data['RSI'] > 70, -1, 0))

print(data[['Close', 'RSI', 'Signal']].tail())