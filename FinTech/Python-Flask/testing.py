import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns

msft = yf.Ticker("MSFT")

sns.set(style="darkgrid")
hist =msft.history(period = "1mo")
df = pd.DataFrame(hist)
#hist['Close'].plot(figsize =(8,5))

# plt.plot(df['Close'], linewidth=1.0)
# plt.plot(df['Open'], linewidth=1.0)
# plt.plot(df['High'], linewidth=1.0)
# plt.plot(df['Low'], linewidth=1.0)
# plt.xticks(fontsize= 7,rotation=45)
# plt.yticks(fontsize=7)
# plt.show()
# print(df.head())
df = pd.DataFrame(msft.options)
# for option in df[0]:
#     print(df.head())

opt = msft.option_chain('2020-08-20')

print(opt)
#print(df.head())
#plt.plot(df['lastPrice'], linewidth=1.0)
#plt.show()