from distutils.log import debug
from unicodedata import name
from flask import Flask


app = Flask(__name__)

@app.route("/" , methods=['GET' , 'POST'])

def index():
    return "Welcome to Innovia technologies! Now we'll Start Housing Price Predictor App"


if __name__=="__main__":
    app.run(debug=True)