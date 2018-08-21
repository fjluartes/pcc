#!/usr/bin/env python
# pizza_toppings.py: Exercise 7-4
# 21 Aug 2018 | fjgl
prompt = "\nPlease enter the topping you want to add to your pizza:"
prompt += "\nEnter 'quit' to finish adding toppings. "

active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print("Adding " + topping + " to your pizza.")
print("\nFinished making your pizza!")
