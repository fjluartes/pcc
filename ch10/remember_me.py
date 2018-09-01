#!/usr/bin/env python
# remember_me.py: saving and reading user-generated data
# 1 Sep 2018 | fjgl
import json

# Refactoring
def greet_user():
    """Greet the user by name."""
    # Load the username, if it has been stored previously.
    #   Otherwise, prompt for the username and store it.
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()
