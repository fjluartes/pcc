#!/usr/bin/env python
# city_functions.py: Exercise 11-1
# 4 Sep 2018 | fjgl
def get_formatted_city(city, country):
    """Neatly formatted city and country."""
    formatted_city = city + ", " + country
    return formatted_city.title()
