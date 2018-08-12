#!/usr/bin/env python
# pizzas.py: Exercises 4-1, 4-2, 4-11
# 12 Aug 2018 | fjgl
# 4-1. Pizzas
pizzas = ['pepperoni', 'garlic n shrimp', 'combo']
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
print("I really love pizza!")
print("")

# 4-11. My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]
pizzas.append('4 cheese')
friend_pizzas.append('meatlovers')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("")

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
print("")

# 4-2. Animals
animals = ['dog', 'cat', 'hamster']
for pet in animals:
    print("A " + pet + " would make a great pet.")
print("Any of these animals would make a great pet.")
