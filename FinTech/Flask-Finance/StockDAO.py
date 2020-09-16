import yfinance as yf
import pandas as pd 
import Stock as Stock
import matplotlib.pyplot as plt

def get_yf_stock_object(ticker):
    return yf.Ticker(ticker)

def get_yf_stock_price(ticker, timePeriod):
    return get_yf_stock_object(ticker).history(timePeriod)

def createStock(df):
    df = pd.DataFrame(df)
    df['date'] =  df.index.values
    return df

# df = get_yf_stock_price('tsla', 'ytd')
# test = createStock(df)
# print(test)