#!/usr/bin/env python
# city_functions.py: Exercise 11-1, 11-2
# 4 Sep 2018 | fjgl
def get_formatted_city(city, country, population=''):
    """Neatly formatted city and country."""
    if population:
        formatted_city = city + ", " + country + " - population " + str(population)
    else:
        formatted_city = city + ", " + country
    return formatted_city.title()
