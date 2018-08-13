#!/usr/bin/env python
# toppings.py: equality/inequality
# 13 Aug 2018 | fjgl
# checking for inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# checking if a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
