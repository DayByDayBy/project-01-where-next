from db.run_sql import run_sql

from models.country import Country
from models.city import City
from models.user import User
from repositories import user_repository 

def save(city):
    sql = "INSERT INTO cities(name, country, visited ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [city.name, city.country.id, city.visited]
    results = run_sql( sql, values)
    city.id = results[0]['id']
    return city


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for row in results:
        city = City(row['name'], row['country'], row['visited'], row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if len(results) > 0:
        result = results[0]
        city = City(result['name'], result['country'], result['visited'], result['id'])
    return city

def users(city):
    users = []

    sql = "SELECT users.* FROM users INNER JOIN visits ON visits.user_id = users.id WHERE city_id = %s"
    values = [city.id]
    results = run_sql(sql, values)
    for row in results:
        user = User(row['name'], row['id'])
        users.append(user)
    return users

def delete(id):
    sql = "DELETE FROM cities where id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)
