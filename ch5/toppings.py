#!/usr/bin/env python
# toppings.py: if/else
# 13 Aug 2018 | fjgl
# requested_toppings = []
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# multiple if statements
#if 'mushrooms' in requested_toppings:
#    print("Adding mushrooms.")
#if 'pepperoni' in requested_toppings:
#    print("Adding pepperoni.")
#if 'extra cheese' in requested_toppings:
#    print("Adding extra cheese.")
#print("")

# if statements with lists
#for requested_topping in requested_toppings:
#    if requested_topping == 'green peppers':
#        print("Sorry, we're out of green peppers right now.")
#    else:
#        print("Adding " + requested_topping + ".")

# checking if a list is empty
#if requested_toppings:
#    for requested_topping in requested_toppings:
#        print("Adding " + requested_topping + ".")
#    print("\nFinished making your pizza!")
#else:
#    print("Are you sure you want a plain pizza?")        

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
