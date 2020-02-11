import yfinance as yf

msft = yf.Ticker("AMZN")
print(msft)
# get stock info
msft.info

# get historical market data
print(msft.history(period="2d", interval = "1d").to_json())
#print(type(msft.history(period="7d", interval = "1m")))