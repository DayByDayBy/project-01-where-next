from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.city import City

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def all_cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

@cities_blueprint.route("/cities/add", methods=['GET'])
def add_city():
    cities = city_repository.select_all()
    return render_template("cities/add.html", all_cities = cities)

@cities_blueprint.route("/cities",  methods=['POST'])
def create_city():
    name    = request.form['name']
    country  = country_repository.select(request.form['country'])
    visited   = request.form['visited']
    city = City(name, country, visited)
    city_repository.save(city)
    return redirect('/index')

@cities_blueprint.route("/cities/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template('cities/show.html', city = city)


@cities_blueprint.route('/cities/have-been')
def visited_cities():
    cities = city_repository.see_visited()
    return render_template("cities/have-been.html", all_cities = cities)
    
@cities_blueprint.route('/cities/have-not-been')
def cities_to_visit():
    cities = city_repository.see_to_visit()
    return render_template("cities/have-not-been.html", all_cities = cities)


@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('cities/edit.html', city=city, countries=countries)

#not sure about this next one....

@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name    = request.form['name']
    country = country_repository.select(request.form['country'])
    visited   = request.form['visited']
    city = City(name, country, visited, id)
    print(city.name)
    city_repository.update(city)
    return redirect('/index')


@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/index')
