from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.user_repository as user_repository
import pdb

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def all_countries():
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries=countries, ticklist=ticklist, wishlist=wishlist, user=user)

# @countries_blueprint.route("/countries/add", methods=['GET'])
# def add_country():
#     countries = country_repository.select_all()
#     return render_template("countries/add.html", all_countries = countries)


@countries_blueprint.route("/countries/delete/<product_id>", methods=['POST'])
def delete_country(product_id):
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    country_repository.delete(int(product_id))
    return redirect('/countries')

@countries_blueprint.route("/countries/add",  methods=['POST'])
def add_country():
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    name    = request.form['name']
    country_id  = country_repository.select(request.form['country_id'])
    visited   = request.form['visited']
    country = country(name, country_id, visited)
    country_repository.save(country)
    return redirect('/index', ticklist=ticklist, wishlist=wishlist, user=user)

@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    return render_template('countries/<id>', country=country, ticklist=ticklist, wishlist=wishlist, user=user)
 
@countries_blueprint.route('/countries/have-been')
def visited_countries():
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    countries = country_repository.see_visited()
    return render_template("countries/have-been.html", all_countries = countries, ticklist=ticklist, wishlist=wishlist, user=user)
    
@countries_blueprint.route('/countries/have-not-been')
def countries_to_visit():
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    countries = country_repository.to_visit()
    return render_template("countries/have-not-been.html", all_countries = countries, ticklist=ticklist, wishlist=wishlist, user=user)


@countries_blueprint.route("/countries/<id>/edit", methods=['GET'])
def edit_country(id):
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    country = country_repository.select(id)
    countries = country_repository.select_all()
    return render_template('countries/edit.html', country=country, countries=countries, ticklist=ticklist, wishlist=wishlist, user=user)


@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    name    = request.form['name']
    country_id = country_repository.select(request.form['country_id'])
    visited   = request.form['visited']
    country = country(name, country_id, visited, id)
    print(country.name)
    country_repository.update(country)
    return redirect('/index', ticklist=ticklist, wishlist=wishlist, user=user)



