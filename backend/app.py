from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#To allow the react appp to fetch data from here
@app.route("/")
def home():
    return "Hi, Welcome to the International Job Website!"

if __name__== "__main__":
    app.run(debug = True)
