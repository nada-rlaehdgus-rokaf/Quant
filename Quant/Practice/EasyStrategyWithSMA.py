import pandas as pd
import yfinance as yf
import numpy as np

# 주식 데이터 가져오기
data = yf.download("AAPL", start="2023-01-01", end="2023-12-31")

# 단기 및 장기 이동 평균 계산
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()

# 매수 및 매도 신호
data['Signal'] = 0
#data['Signal'][50:] = np.where(data['SMA_50'][50:] > data['SMA_200'][50:], 1, 0)
#data.loc[50:, 'Signal'] = np.where(data['SMA_50'][50:] > data['SMA_200'][50:], 1, 0)
# data slicing 시 chianed assignment 문제가 발 생해서 loc으로 바꿧는데 또 문제가 생겨서
# .loc[] 레이블 기반 인덱싱 (인덱스나 열 이름 사용) 
# .iloc[] 정수기반 인덱싱  (행과 열의 번호 사용 )
data.iloc[50:, data.columns.get_loc('Signal')] = np.where(data['SMA_50'][50:] > data['SMA_200'][50:], 1, 0)
data['Position'] = data['Signal'].diff()

# 결과 출력
print(data[['Close', 'SMA_50', 'SMA_200', 'Signal', 'Position']].tail())