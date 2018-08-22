#!/usr/bin/env python
# greeter.py: defining a function, function with while loop
# 22 Aug 2018 | fjgl
#def greet_user(username):
#    """Display a simple greeting."""
#    print("Hello, " + username.title() + "!")
#greet_user('jesse')
# parameter: username
# argument: 'jesse'

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
