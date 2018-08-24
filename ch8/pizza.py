#!/usr/bin/env python
# pizza.py: passing an arbitrary number of arguments
# 23 Aug 2018 | fjgl
#def make_pizza(*toppings):
#    """Summarize the pizza we are about to make."""
#    print("\nMaking a pizza with the following toppings:")
#    for topping in toppings:
#        print("- " + topping)

# Mixing positional and arbitrary arguments
# importing an entire module
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Parameter *toppings creates a tuple called toppings and inserts the
#   arguments passed into make_pizza.

