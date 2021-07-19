# Greets user

from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def index():
    return render_template("index.html")

@app.route("/greet")
@cross_origin()
def greet():
    return render_template('greet.html',  name=request.args.get("name"))

@app.route("/page")
@cross_origin()
def page():
    return render_template('page.html',  name=request.args.get("title"))

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)