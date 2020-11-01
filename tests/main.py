from flask import Flask, render_template,session, redirect, url_for, request
import pandas as pd
import yfinance as yf
app = Flask(__name__)

 
df = yf.Ticker('tsla')
df = df.history('1mo')
df['date'] =  df.index.values


labels = df['date'].to_numpy()


values = df['Open'].to_numpy()
values_2 = df['Close'].to_numpy()

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


@app.route("/")
def home():
    return render_template("test.html")

@app.route("/lines")
def lines():
    return render_template("LineChart.html", dates = df['dates'].to_numpy(),open = df['Open'])

@app.route('/line', methods=['GET', 'POST'])
def line():
    line_labels=labels
    line_values= values

    if request.method =='POST':
        ticker = request.form['ticker']
        timePeriod = request.form['time']
        
        df = DAO.get_yf_stock_price(ticker, timePeriod)
        stock = DAO.createStock(df)
        
        return render_template("test.html",title='Line', max=df['High'].max(),values=line_values,open = stock['open'], labels = labels,date = stock['date'])

    return render_template('line.html')


if __name__ == "__main__":
    app.run(debug=True)