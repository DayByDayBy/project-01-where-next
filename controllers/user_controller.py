from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.user import User
import repositories.user_repository as user_repository
from models.country import Country
import repositories.city_repository as city_repository


users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def all_users():
    users = user_repository.select_all()
    return render_template("users/index.html", all_users = users)

@users_blueprint.route("/users/add", methods=['GET'])
def add_user():
    users = user_repository.select_all()
    return render_template("users/add.html", all_users = users)

@users_blueprint.route("/users",  methods=['POST'])
def create_user():
    name    = request.form['name']
    user_id  = user_repository.select(request.form['user_id'])
    visited   = request.form['visited']
    user = user(name, user_id, visited)
    user_repository.save(user)
    return redirect('/index')

@users_blueprint.route("/users/<id>", methods=['GET'])
def show_user(id):
    user = user_repository.select(id)
    return render_template('users/show.html', user = user)


@users_blueprint.route("/users/<id>/edit", methods=['GET'])
def edit_user(id):
    user = user_repository.select(id)
    users = user_repository.select_all()
    return render_template('users/edit.html', user=user, users=users)

#not sure about this next one....

@users_blueprint.route("/users/<id>", methods=['POST'])
def update_user(id):
    name    = request.form['name']
    user_id = user_repository.select(request.form['user_id'])
    visited   = request.form['visited']
    user = user(name, user_id, visited, id)
    print(user.name)
    user_repository.update(user)
    return redirect('/index')


@users_blueprint.route("/users/<id>/delete", methods=['POST'])
def delete_user(id):
    user_repository.delete(id)
    return redirect('/index')




