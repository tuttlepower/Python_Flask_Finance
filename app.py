from flask import Flask, render_template, session, redirect, url_for, request, jsonify,send_from_directory
import os
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test", methods=['GET', 'POST'])
def test():
    return render_template("test.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
                               'favicon.ico', mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
