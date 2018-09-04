#!/usr/bin/env python
# cities.py: exercise 11-1 (call get_formatted_city)
# 4 Sep 2018 | fjgl
from city_functions import get_formatted_city

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease enter a city: ")
    if city == 'q':
        break
    country = input("Please enter a country: ")
    if country == 'q':
        break

    formatted_city = get_formatted_city(city, country)
    print("Formatted city: " + formatted_city + '.')
