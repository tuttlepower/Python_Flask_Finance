from flask import Flask, render_template, session, redirect, url_for, request, jsonify
import pandas as pd
import StockDAO as DAO
import Stock as Stock


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/get_piechart_data/<ticker>/<timePeriod>')
def get_piechart_data(ticker = 'tsla', timePeriod ='1m'):
    # df = DAO.get_yf_stock_price(ticker, timePeriod)
    # stock = pd.DataFrame(DAO.createStock(df)) 
    df = DAO.get_yf_stock_price(ticker, timePeriod)
    print(df.head())

    return jsonify(str(df.to_dict()))


@app.route("/about")
def about():
    return '<h1>This is the way</h1>'


@app.route("/test", methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        ticker = request.form['ticker']
        timePeriod = request.form['time']
        df = DAO.get_yf_stock_price(ticker, timePeriod)
        stock = pd.DataFrame(DAO.createStock(df))
        return render_template("test.html", df=df)

    return render_template("test.html")


@app.route("/chartJSTest", methods=['GET', 'POST'])
def chartJSTest():
    if request.method == 'POST':
        ticker = request.form['ticker']
        timePeriod = request.form['time']
        # proof of concept. The Post is working
        print(ticker)
        print(timePeriod)
        df = DAO.get_yf_stock_price(ticker, timePeriod)
        stock = pd.DataFrame(DAO.createStock(df))
        return render_template("chartJSTest.html", ticker=ticker, timePeriod=timePeriod, opens= df['Open'])
    return render_template("chartJSTest.html")


if __name__ == "__main__":
    app.run(debug=True)
