#!/usr/bin/env python
# three_exits.py: Exercise 7-6
# 21 Aug 2018 | fjgl
prompt = "\nPlease enter the topping you want to add to your pizza:"
prompt += "\nEnter 'quit' to finish adding toppings. "

# Using an active variable
#active = True
#while active:
#    topping = input(prompt)
#    if topping == 'quit':
#        active = False
#    else:
#        print("Adding " + topping + " to your pizza.")
#print("\nFinished making your pizza!")

# conditional test
#topping = ""
#while topping != 'quit':
#    topping = input(prompt)
#    if topping != 'quit':
#        print("Adding " + topping + " to your pizza.")
#print("\nFinished making your pizza!")

# break statement
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print("Adding " + topping + " to your pizza.")
print("\nFinished making your pizza!")

