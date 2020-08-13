import finance_control as fc

ticker = input("Please Enter a Ticker to analyze:") 
print(ticker)
stock = fc.getValidTicker(ticker)
timePeriod = input("Please Enter a time period:\nvalid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max: ")
timePeriod = fc.confirmTimePeriodValidity(timePeriod)
print(timePeriod)

fc.graphStock(stock,timePeriod)

