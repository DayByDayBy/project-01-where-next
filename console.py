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

country1 = Country("GERMANY", 'eur', 'EU')
country_repository.save(country1)
country2 = Country("TANZANIA", 'tsh', 'AF')
country_repository.save(country1)
country3 = Country("RUSSIA", 'rub', 'AS')
country_repository.save(country1)
country4 = Country("AUSTRALIA", 'aud', 'OC')
country_repository.save(country1)
country5 = Country("USA", 'usd', 'NA')
country_repository.save(country1)
country6 = Country("ZIMBABWE", 'zwl', 'AF')
country_repository.save(country1)
country7 = Country("FRANCE", 'eur', 'EU')
country_repository.save(country1)

country_repository.select_all()

city_repository.delete_all()

city01 = City("BERLIN", country1, True)
city_repository.save(city01)
city02 = City("DAR ES SALAAM", country1, True)
city_repository.save(city02)
city03 = City("MOSCOw", country2, True)
city_repository.save(city03)
city04 = City("MELBOURNE", country2, True)
city_repository.save(city04)
city05 = City("LONDON", country3, True)
city_repository.save(city05)
city06 = City("LOS ANGELES", country3, True)
city_repository.save(city06)
city07 = City("HARARE", country4, True)
city_repository.save(city07)
city08 = City("PARIS", country4, True)
city_repository.save(city08)
city09 = City("BEIJING", country4, False)
city_repository.save(city09)
city10 = City("ADDIS ABABA", country4, False)
city_repository.save(city10)
city11 = City("TRIPOLI", country4, False)
city_repository.save(city11)
city12 = City("BEIRUT", country4, False)
city_repository.save(city12)
city13 = City("NEW YORK", country4, False)
city_repository.save(city13)
city14 = City("HANOI", country4, False)
city_repository.save(city14)

city_repository.select_all()

pdb.set_trace()