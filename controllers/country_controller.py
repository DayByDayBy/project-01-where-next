from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def all_countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

@countries_blueprint.route("/countries/add", methods=['GET'])
def add_country():
    countries = country_repository.select_all()
    return render_template("countries/add.html", all_countries = countries)

@countries_blueprint.route("/countries",  methods=['POST'])
def create_country():
    name    = request.form['name']
    country_id  = country_repository.select(request.form['country_id'])
    visited   = request.form['visited']
    country = country(name, country_id, visited)
    country_repository.save(country)
    return redirect('/index')

@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country = country)


@countries_blueprint.route('/countries/have-been')
def visited_countries():
    countries = country_repository.see_visited()
    return render_template("countries/seen.html", all_countries = countries)
    
@countries_blueprint.route('/countries/')
def countries_to_visit():
    countries = country_repository.see_to_visit()
    return render_template("countries/have-not-been.html", all_countries = countries)


@countries_blueprint.route("/countries/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    countries = country_repository.select_all()
    return render_template('countries/edit.html', country=country, countries=countries)

#not sure about this next one....

@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    name    = request.form['name']
    country_id = country_repository.select(request.form['country_id'])
    visited   = request.form['visited']
    country = country(name, country_id, visited, id)
    print(country.name)
    country_repository.update(country)
    return redirect('/index')


@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/index')
