from flask import Flask, render_template

from controllers.city_controller import *
from controllers.country_controller import *
from controllers.user_controller import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)