from flask import Flask, render_template,session, redirect, url_for, request
import pandas as pd
import finance_control as fc

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
        print(ticker)
        return render_template("test.html", ticker=ticker,date = fc.returnsDates(ticker,timePeriod),price = fc.returnsPrices(ticker,timePeriod))
    return render_template("test.html")

@app.route("/chartJSTest", methods=['GET', 'POST'])
def chartJSTest():
    if request.method =='POST':
        ticker = request.form['ticker']
        timePeriod = request.form['time']
        print(ticker)
    return render_template("chartJSTest.html",)
    
if __name__ == "__main__":
    app.run(debug=True)