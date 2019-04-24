import matplotlib.pyplot as plot
import fix_yahoo_finance as yf 
import pandas as pd
ticker = 'AAPL'
data = yf.download(ticker,'2018-01-01','2019-04-01')
data.Close.plot()
short = data.Close.rolling(window=10).mean()
short.plot()

long = data.Close.rolling(window=30).mean()
#long.plot()

plot.show()
