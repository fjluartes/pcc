#!/usr/bin/env python
# dream_vacation.py: Exercise 7-10
# 21 Aug 2018 | fjgl
places = {}
active = True

while active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    places[name] = place

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        active = False

print("\n--- Poll Results ---")
for name, place in places.items():
    print(name.title() + " would like to go to " + place.title() + ".")
