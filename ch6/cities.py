#!/usr/bin/env python
# cities.py: Exercise 6-11, 6-12
# 19 Aug 2018 | fjgl
# 6-11. Cities
cities = {
    'paris': {
        'country': 'france',
        'population': 12405426,
        'fact': 'Paris is known for its architectural landmarks, like the Louvre.'
        },
    'new york': {
        'country': 'usa',
        'population': 20320876,
        'fact': 'New York is situated in one of the largest natural harbors.'
        },
    'tokyo': {
        'country': 'japan',
        'population': 38305000,
        'fact': 'Tokyo is the most populous metropolitan area in the world.'
        }
    }

# 6-12. Extensions
cities['london'] = {
    'country': 'uk',
    'population': 14040163,
    'fact': 'London is the world\'s largest financial centre.'
    }

for city, city_info in cities.items():
    print("City: " + city.title())
    if city_info['country'] == 'usa' or city_info['country'] == 'uk':
        print("\tCountry: " + city_info['country'].upper())
    else:
        print("\tCountry: " + city_info['country'].title())
    print("\tPopulation: " + str(city_info['population']))
    print("\tFact: " + city_info['fact'])
