from flask import Flask, render_template, redirect
from flask import Blueprint
from controllers.city_controller import *
from controllers.country_controller import *
from controllers.user_controller import *
from repositories import user_repository

app = Flask(__name__)

app.register_blueprint(cities_blueprint)
app.register_blueprint(countries_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def home():
    user = user_repository.select_all()[0]
    return render_template('index.html', user = user)

if __name__ == '__main__':
    app.run(debug=True)