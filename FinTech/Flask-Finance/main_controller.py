from flask import Flask, render_template,session, redirect, url_for, request
import pandas as pd
import StockDAO as DAO
import Stock as Stock

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/test", methods=['GET', 'POST'])
def test():
    if request.method =='POST':
        ticker = request.form['ticker']
        timePeriod = request.form['time']
        df = DAO.get_yf_stock_price(ticker, timePeriod)
        stock = pd.DataFrame(DAO.createStock(df))
        print(df.head())
        return render_template("test.html", df = df)

    return render_template("test.html")

@app.route("/chartJSTest", methods=['GET', 'POST'])
def chartJSTest():
    if request.method =='POST':
        ticker = request.form['ticker']
        timePeriod = request.form['time']
        #proof of concept. The Post is working
        print(ticker)
        print(timePeriod)
        df = DAO.get_yf_stock_price(ticker, timePeriod)
        stock = pd.DataFrame(DAO.createStock(df))
        return render_template("chartJSTest.html",ticker=ticker,timePeriod = timePeriod, opens = df['Open'])
    return render_template("chartJSTest.html")
    
if __name__ == "__main__":
    app.run(debug=True)