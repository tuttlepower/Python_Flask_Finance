import pandas as pd 
df = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=8AFMM6SKR6OD86F2&datatype=csv')
key = '8AFMM6SKR6OD86F2'
print(df.head())