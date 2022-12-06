from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.user import User
import repositories.user_repository as user_repository
from models.country import Country
import repositories.city_repository as city_repository


users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def all_users():
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    users = user_repository.select_all()
    return render_template("users/index.html", all_users = users, ticklist=ticklist, wishlist=wishlist, user=user)

@users_blueprint.route("/users/add", methods=['GET'])
def add_user():
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    users = user_repository.select_all()
    return render_template("users/add.html", all_users = users, ticklist=ticklist, wishlist=wishlist, user=user)

@users_blueprint.route("/users",  methods=['POST'])
def create_user():
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    name    = request.form['name']
    language   = request.form['language']
    user = User(name, language)
    user_repository.save(user)
    return redirect('/index', ticklist=ticklist, wishlist=wishlist)

@users_blueprint.route("/users/<id>", methods=['GET'])
def show_user(id):
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    user_to_show = user_repository.select(id)
    return render_template('users/show.html', uuser_to_show = user_to_show, ticklist=ticklist, wishlist=wishlist, user=user)


@users_blueprint.route("/users/<id>/edit", methods=['GET'])
def edit_user(id):
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    ticklist=ticklist, wishlist=wishlist, user=user
    user_to_edit = user_repository.select(id)
    user = user_repository.select_all()[0]
    users = user_repository.select_all()
    return render_template('users/edit.html', user_to_edit=user_to_edit, users=users, ticklist=ticklist, wishlist=wishlist, user=user)

#not sure about this next one....

@users_blueprint.route("/users/<id>", methods=['POST'])
def update_user(id):
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    name    = request.form['name']
    user = User(id)
    print(user.name)
    user_repository.update(user)
    return redirect('/index', name, ticklist=ticklist, wishlist=wishlist, user=user)


@users_blueprint.route("/users/<id>/delete", methods=['POST'])
def delete_user(id):
    ticklist = user_repository.cities_visited()
    wishlist = user_repository.cities_to_visit()
    user = user_repository.select_all()[0]
    user_repository.delete(id)
    return redirect('/index', ticklist=ticklist, wishlist=wishlist, user=user)




