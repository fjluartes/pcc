#!/usr/bin/env python
# pizza.py: nesting (list in a dictionary)
# 19 Aug 2018 | fjgl
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
    }
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
