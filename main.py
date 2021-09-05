from flask import Flask, render_template, session, redirect, url_for, request, jsonify
import pandas as pd


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test", methods=['GET', 'POST'])
def test():
    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)
