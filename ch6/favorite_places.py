#!/usr/bin/env python
# favorite_places.py: Exercise 6-9
# 19 Aug 2018 | fjgl
# 6-9. Favorite Places
favorite_places = {
    'fred': ['korea', 'philippines'],
    'maan': ['korea', 'italy', 'france'],
    'ate': ['japan', 'china']
    }

for person, places in favorite_places.items():
    print(person.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())
