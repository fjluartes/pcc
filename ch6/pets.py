#!/usr/bin/env python
# pets.py: Exercise 6-8
# 19 Aug 2018 | fjgl
# 6-8. Pets
pet_0 = {'name': 'bella', 'animal': 'cat', 'owner': 'maggie'}
pet_1 = {'name': 'chloe', 'animal': 'dog', 'owner': 'sophie'}
pet_2 = {'name': 'shadow', 'animal': 'cat', 'owner': 'yuki'}
pet_3 = {'name': 'coco', 'animal': 'bird',  'owner': 'missy'}
pet_4 = {'name': 'buddy', 'animal': 'dog', 'owner': 'oliver'}

pets = [pet_0, pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(pet['name'].title() + " is the name of " +
          pet['owner'].title() + "'s pet " +
          pet['animal'] + ".")
