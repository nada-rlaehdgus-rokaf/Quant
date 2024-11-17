import yfinance as yf

# 예: 애플(Apple) 주식 데이터 가져오기
data = yf.download("AAPL", start="2023-01-01", end="2023-12-31")
print(data.head())



