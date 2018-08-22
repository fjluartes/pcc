#!/usr/bin/env python
# cities.py: Exercise 8-5
# 22 Aug 2018 | fjgl
def describe_city(city, country='Japan'):
    """Display a sentence about a city and its country"""
    print(city.title() + " is in " + country.title() + ".")

describe_city('tokyo')
describe_city(city='osaka')
describe_city(city='paris', country='france')
