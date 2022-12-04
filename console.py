import pdb
from models.city import City
from models.country import Country
from models.user import User

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository 
import repositories.user_repository as user_repository

user_repository.delete_all()

user1 = User("Richard Burton",['fra', 'eng', 'spa', 'ara', 'lat'])
user_repository.save(user1)
user2 = User("James Boag", ['eng', 'deu', 'fra'])
user_repository.save(user2)

user_repository.select_all()

country_repository.delete_all()

country01 = Country("GERMANY", 'eur', 'EU')
country_repository.save(country01)
country02 = Country("TANZANIA", 'tsh', 'AF')
country_repository.save(country02)
country03 = Country("RUSSIA", 'rub', 'AS')
country_repository.save(country03)
country04 = Country("AUSTRALIA", 'aud', 'OC')
country_repository.save(country04)
country05 = Country("ENGLAND", 'gbp', 'eu')
country_repository.save(country05)
country06 = Country("USA", 'usd', 'NA')
country_repository.save(country06)
country07 = Country("ZIMBABWE", 'zwl', 'AF')
country_repository.save(country07)
country08 = Country("FRANCE", 'eur', 'EU')
country_repository.save(country08)
country09 = Country("CHINA", 'cny', 'AS')
country_repository.save(country09)
country10 = Country("ETHIOPIA", 'etb', 'AF')
country_repository.save(country10)
country11 = Country("LEBANON", 'lbp', 'AS')
country_repository.save(country11)
country12 = Country("VIETNAM", 'vnd', 'AS')
country_repository.save(country12)



country_repository.select_all()

city_repository.delete_all()

city01 = City("BERLIN", country01, True)
city_repository.save(city01)
city02 = City("DAR ES SALAAM", country02, True)
city_repository.save(city02)
city03 = City("MOSCOw", country03, True)
city_repository.save(city03)
city04 = City("MELBOURNE", country04, True)
city_repository.save(city04)
city05 = City("LONDON", country05, True)
city_repository.save(city05)
city06 = City("LOS ANGELES", country06, True)
city_repository.save(city06)
city07 = City("HARARE", country07, True)
city_repository.save(city07)
city08 = City("PARIS", country08, True)
city_repository.save(city08)
city09 = City("BEIJING", country09, False)
city_repository.save(city09)
city10 = City("ADDIS ABABA", country10, False)
city_repository.save(city10)
city11 = City("BEIRUT", country11, False)
city_repository.save(city11)
city12 = City("NEW YORK", country06, False)
city_repository.save(city12)
city13 = City("HANOI", country12, False)
city_repository.save(city13)

city_repository.select_all()

pdb.set_trace()