#!/usr/bin/env python
# toppings.py: if/else
# 13 Aug 2018 | fjgl
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("")

# if statements with lists
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we're out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
