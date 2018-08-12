#!/usr/bin/env python
# foods.py: copying a list, Exercise 4-10, 4-12
# 12 Aug 2018 | fjgl
my_foods = ['pizza', 'falafel', 'carrot cake']
# list_name[:]: include entire list
# copy my_foods into friend_foods
friend_foods = my_foods[:]

# both my_foods and friend_foods point to the same list
# friend_foods = my_foods

my_foods.append('cannoli')
my_foods.append('chocolate cake')
my_foods.append('dumpling')
my_foods.append('crepe')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print("")

# 4-10. Slices
print("The first three items in my favorite foods are:")
print(my_foods[0:3])

print("Three items from the middle of the list are:")
print(my_foods[2:5])

print("The last three items on my favorite foods are:")
print(my_foods[-3:])

# 4-12. More Loops
for food in my_foods:
    print(food)
print("")
for food in friend_foods:
    print(food)
