import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns

df = pd.read_csv("nasdaqlisted.txt", sep='|', index_col=False,)

def getValidTicker(ticker):
    if df['Symbol'].str.contains(ticker.upper()).any():
        return ticker
    else: 
        ticker = input("Invalid Ticker:")
        getValidTicker(ticker)

def graphStock(stock, timePeriod):

    #gets the yfinance data for the specified stock
    yf_Stock= yf.Ticker(stock)
    
    #gets the price history of the given stock 
    stock_history = yf_Stock.history(period = timePeriod)

    #Style choices
    sns.set(style="darkgrid")
    
    #creates Pandas df with the stock_history
    df = pd.DataFrame(stock_history,index=None)
    print(df.columns)
    #creates plot of the Closing price of the stock
    plt.plot(df['Close'], linewidth=2.0,alpha=0.1,label='Close')
    plt.plot(df['Open'], linewidth=2.0,alpha=0.1,label = 'Open')
    plt.plot(df['High'], linewidth=2.0,alpha=0.1, label = 'High')
    plt.plot(df['Low'], linewidth=2.0,alpha=0.1, label = 'Low')
    #plt.fill_between(df['"Date'],df['Low'],df['High'])
    plt.fill_betweenx(df.datetime,df['Close'],df['Open'])
    plt.legend()
    plt.title(stock)
    #show the plot
    plt.show()
def returnsPrices(ticker,timePeriod):
    #gets the yfinance data for the specified stock
    yf_Stock= yf.Ticker(ticker)
    
    #gets the price history of the given stock 
    stock_history = yf_Stock.history(period = timePeriod)

    #creates Pandas df with the stock_history
    df = pd.DataFrame(stock_history,index=None)
    return df['high']
def returnsDates(ticker,timePeriod):
    #gets the yfinance data for the specified stock
    yf_Stock= yf.Ticker(ticker)
    
    #gets the price history of the given stock 
    stock_history = yf_Stock.history(period = timePeriod)

    #creates Pandas df with the stock_history
    df = pd.DataFrame(stock_history,index=None)
    return df['date']

def confirmTimePeriodValidity(timePeriod):
    validDates = ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max']
    if timePeriod in validDates:
        return timePeriod
    else: 
        retry = input("Please enter a valid date:")
        confirmTimePeriodValidity(retry)
