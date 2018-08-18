#!/usr/bin/env python
# person.py: Exercise 6-1
# 18 Aug 2018 | fjgl
# 6-1. Person
person = {
    'first_name': 'maan',
    'last_name': 'bajan',
    'age': 23,
    'city': 'muntinlupa'
    }
print("Name: " + person['first_name'].title() + " " +
      person['last_name'].title() +
      "\nAge: " + str(person['age']) +
      "\nCity: " + person['city'].title())
