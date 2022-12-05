from db.run_sql import run_sql

from models.city import City
from models.country import Country
from models.user import User
from repositories import city_repository


def save(user):
    sql = "INSERT INTO users( name ) VALUES ( %s ) RETURNING id"
    values = [user.name]
    results = run_sql( sql, values )
    user.id = results[0]['id']
    return user

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['id'])
        users.append(user)
    return users


def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        user = User(result['name'], result['language'], result['id'] )
    return user


def cities_visited(user):
    ticklist = []

    sql = "SELECT * FROM cities WHERE visited = %s"
    values = [True]
    results = run_sql(sql, values)
    for row in results:
        cities_visited = City(row['name'], row['language'], row['country_id'], row['id'])
        ticklist.append(cities_visited)

    return ticklist


def cities_to_visit(user):
    wishlist = []

    sql = "SELECT * FROM cities WHERE visited = %s"
    values = [False]
    results = run_sql(sql, values)
    for row in results:
        cities_visited = City(row['name'], row['language'], row['country_id'], row['id'])
        wishlist.append(cities_visited)

    return wishlist


def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)
