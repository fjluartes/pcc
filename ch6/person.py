#!/usr/bin/env python
# person.py: Exercise 6-1, 6-7
# 18 Aug 2018 | fjgl
# 6-1. Person
#person = {
#    'first': 'alan',
#    'last': 'turing',
#    'age': 41,
#    'city': 'london'
#    }
#print("Name: " + person['first'].title() + " " +
#      person['last'].title() +
#      "\nAge: " + str(person['age']) +
#      "\nCity: " + person['city'].title())

# 6-7. People
people = {
    'aturing': {
        'first': 'alan',
        'last': 'turing',
        'age': 41,
        'city': 'manchester'
        },
    'dknuth': {
        'first': 'donald',
        'last': 'knuth',
        'age': 80,
        'city': 'stanford'
        },
    'sjones': {
        'first': 'simon',
        'last': 'jones',
        'age': 60,
        'city': 'cambridge'
        },
    'jarmstrong': {
        'first': 'joe',
        'last': 'armstrong',
        'age': 67,
        'city': 'stockholm'
        }
    }

for person in people.values():
    full_name = person['first'] + " " + person['last']
    print("\nName: " + full_name.title())
    print("\tAge: " + str(person['age']))
    print("\tCity: " + person['city'].title())
