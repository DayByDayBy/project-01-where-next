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

@app.route('/base')
def base_bits():
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    return render_template('base.html', ticklist=ticklist, wishlist=wishlist, user=user)

@app.route('/')
def home():
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    return render_template('index.html', ticklist=ticklist, wishlist=wishlist, user = user)

@app.route('/users')
def users():
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    return render_template('users/index.html', ticklist=ticklist, wishlist=wishlist, user = user)

@app.route('/cities')
def cities():
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    return render_template('cities/index.html', ticklist=ticklist, wishlist=wishlist, user = user)

@app.route('/countries')
def countries():
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    return render_template('countries/index.html', ticklist=ticklist, wishlist=wishlist, user=user)

if __name__ == '__main__':
    app.run(debug=True)