#!/usr/bin/env python
# conditional_tests.py: Exercises 5-1, 5-2
# 15 Aug 2018 | fjgl
# 5-1. Conditional Tests
my_car = 'nissan'
print("Is my_car == 'nissan'? I predict True.")
if (my_car == 'nissan'):
    print(my_car == 'nissan')
    print("my_car == 'nissan'")
print("Is my_car == 'tesla'? I predict False.")
if (not my_car == 'tesla'):
    print(my_car == 'tesla')
    print("my_car != 'tesla'")
print("")

my_car = 'audi'
print("Is my_car == 'audi'? I predict True.")
if (my_car == 'audi'):
    print(my_car == 'audi')
    print("my_car == 'audi'")
print("Is my_car == 'nissan'? I predict False.")
if (not my_car == 'nissan'):
    print(my_car == 'nissan')
    print("my_car != 'nissan'")
print("")

my_car = 'bmw'
print("Is my_car == 'bmw'? I predict True.")
if (my_car == 'bmw'):
    print(my_car == 'bmw')
    print("my_car == 'bmw'")
print("Is my_car == 'audi'? I predict False.")
if (not my_car == 'audi'):
    print(my_car == 'audi')
    print("my_car != 'audi'")
print("")

my_car = 'subaru'
print("Is my_car == 'subaru'? I predict True.")
if (my_car == 'subaru'):
    print(my_car == 'subaru')
    print("my_car == 'subaru'")
print("Is my_car == 'bmw'? I predict False.")
if (not my_car == 'bmw'):
    print(my_car == 'bmw')
    print("my_car != 'bmw'")
print("")

my_car = 'toyota'
print("Is my_car == 'toyota'? I predict True.")
if (my_car == 'toyota'):
    print(my_car == 'toyota')
    print("my_car == 'toyota'")
print("Is my_car == 'subaru'? I predict False.")
if (not my_car == 'subaru'):
    print(my_car == 'subaru')
    print("my_car != 'subaru'")
print("\n")

# 5-2. More Conditional Tests
# Tests using equality/inequality
cars = ['audi', 'bmw', 'nissan', 'subaru', 'toyota']
print("my_car != cars[0]")
if (my_car != cars[0]):
    print(my_car != cars[0])
print("my_car == cars[0]")
if (not my_car == cars[0]):
    print(my_car == cars[0])
print("")
print("my_car == cars[4]")
if (my_car == cars[4]):
    print(my_car == cars[4])
print("my_car != cars[4]")
if (not my_car != cars[4]):
    print(my_car != cars[4])
print("")

# Tests using lower()
print("cars[0].lower() == 'audi'")
if (cars[0].lower() == 'audi'):
    print(cars[0].lower() == 'audi')
print("cars[1].lower() == 'audi'")
if (not cars[1].lower() == 'audi'):
    print(cars[1].lower() == 'audi')
print("\n")

# Numerical tests (==, !=, <, >, <=, >=)
numbers = [num for num in range(1, 6)]
if (numbers[0] == 1):
    print(str(numbers[0]) + " == 1")
    print(numbers[0] == 1)
if (not numbers[1] == 1):
    print(str(numbers[1]) + " == 1")
    print(numbers[1] == 1)
print("")

if (numbers[1] != 1):
    print(str(numbers[1]) + " != 1")
    print(numbers[1] != 1)
if (not numbers[0] != 1):
    print(str(numbers[0]) + " != 1")
    print(numbers[0] != 1)
print("")

if (numbers[1] < numbers[2]):
    print(str(numbers[1]) + " < " + str(numbers[2]))
    print(numbers[1] < numbers[2])
if (not numbers[2] < numbers[1]):
    print(str(numbers[2]) + " < " + str(numbers[1]))
    print(numbers[2] < numbers[1])
print("")

if (numbers[4] > numbers[3]):
    print(str(numbers[4]) + " > " + str(numbers[3]))
    print(numbers[4] > numbers[3])
if (not numbers[3] > numbers[4]):
    print(str(numbers[3]) + " > " + str(numbers[4]))
    print(numbers[3] > numbers[4])
print("")

if (numbers[1] <= numbers[2]):
    print(str(numbers[1]) + " <= " + str(numbers[2]))
    print(numbers[1] <= numbers[2])
if (not numbers[3] <= numbers[2]):
    print(str(numbers[3]) + " <= " + str(numbers[2]))
    print(numbers[3] <= numbers[2])
print("")

if (numbers[4] >= numbers[4]):
    print(str(numbers[4]) + " >= " + str(numbers[4]))
    print(numbers[4] >= numbers[4])
if (not numbers[2] >= numbers[4]):
    print(str(numbers[2]) + " >= " + str(numbers[4]))
    print(numbers[2] >= numbers[4])
print("\n")

# Tests using and and or keywords
if((numbers[2] > 1) and (numbers[2] < 4)):
    print(str(numbers[2]) + " > 1 and " + str(numbers[2]) + " < 4")
    print((numbers[2] > 1) and (numbers[2] < 4))
if((not numbers[2] < 1) and (not numbers[2] > 4)):
    print(str(numbers[2]) + " < 1 and " + str(numbers[2]) + " > 4")
    print((numbers[2] < 1) and (numbers[2] > 4))
print("")

if((numbers[3] > 1) or (numbers[3] < 4)):
    print(str(numbers[3]) + " > 1 or " + str(numbers[3]) + " < 4")
    print((numbers[3] > 1) or (numbers[3] < 4))
if((not numbers[3] < 1) or (not numbers[3] > 4)):
    print(str(numbers[3]) + " < 1 or " + str(numbers[3]) + " > 4")
    print((numbers[3] < 1) or (numbers[3] > 4))
print("\n")

# Tests whether an item is in or not in a list
my_car = 'subaru'
if (my_car in cars):
    print(my_car + " in cars")
    print(my_car in cars)
my_car = 'tesla'
if (not my_car in cars):
    print(my_car + " in cars")
    print(my_car in cars)
print("")

my_car = 'porsche'
if (my_car not in cars):
    print(my_car + " not in cars")
    print(my_car not in cars)
my_car = 'bmw'
if (not my_car not in cars):
    print(my_car + " not in cars")
    print(my_car not in cars)
