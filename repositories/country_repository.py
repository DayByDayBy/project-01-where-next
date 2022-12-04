from db.run_sql import run_sql

from models.country import Country
from models.city import City
from models.user import User
from repositories import user_repository

def save(country):
    sql = "INSERT INTO countries (name, currency, continent) VALUES ( %s, %s, %s) RETURNING id"
    values = [country.name, country.currency, country.continent]
    results = run_sql( sql, values)
    country.id = results[0]['id']
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        country = country(row['name'], row['currency'], row['continent'], row['id'] )
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = country(result['name'], result['currency'], result['continent'], result['id'] )
    return country

# def users(country):
#     users = []

#     sql = "SELECT users.* FROM users INNER JOIN '____' ON user_id = users.id WHERE country_id = %s"
#     values = [country.id]
#     results = run_sql(sql, values)
#     for row in results:
#         user = User(row['name'], row['langueages'], row['id'])
#         users.append(user)
#     return users


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)
