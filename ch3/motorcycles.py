#!/usr/bin/env python
# motorcycles.py: Modifying elements in a list.
# 11 Aug 2018 | fjgl
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# append(): adding an item at the end of a list
motorcycles.append('ducati')
print(motorcycles)

# adding items in an empty list
motorcycles = []
print(motorcycles)
motorcycles.append('ducati')
motorcycles.append('suzuki')
motorcycles.append('honda')
motorcycles.append('yamaha')
print(motorcycles)

# deleting a specific item in a list
del motorcycles[0]
print(motorcycles)

# inserting an item in a specific position in a list
motorcycles.insert(1, 'ducati')
print(motorcycles)

# pop(): removes the last item in a list
# popped item can be used for other purposes
last_owned = motorcycles.pop()
print(motorcycles)
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# pop(i): pop an item from any position i
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
motorcycles.insert(0, first_owned)
motorcycles.append(last_owned)

# remove(): removing an item by value
# remove() only removes the first instance of an item in the list
# a loop is required to remove all instances of the item
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
