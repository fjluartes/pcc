#!/usr/bin/env python
# city_names.py: Exercise 8-6
# 22 Aug 2018 | fjgl
def city_country(city, country):
    """Return a <city>, <country> formatted string."""
    city_country = city.title() + ', ' + country.title()
    return city_country

address = city_country('santiago', 'chile')
print(address)
address = city_country(country='germany', city='berlin')
print(address)
address = city_country(city='tel aviv', country='israel')
print(address)
