import yfinance as yf


def get_yf_stock_object(ticker):
    return yf.Ticker(ticker)

def get_yf_stock_price(ticker, timePeriod):
    return get_yf_stock_object(ticker).history(timePeriod)

print(get_yf_stock_price('tsla','ytd').head())