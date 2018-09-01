#!/usr/bin/env python
# favorite_numbers.py: Exercises 10-11, 10-12
# 1 Sep 2018 | fjgl
import json

def get_stored_number():
    """Display favorite number of user if available."""
    filename = 'favorite_numbers.json'
    try:
        with open(filename) as f_obj:
            fave_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fave_number

def get_new_number():
    """Get favorite number of user."""
    filename = 'favorite_numbers.json'
    fave_number = input("What is your favorite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(fave_number, f_obj)
    return fave_number

def show_number():
    """Show favorite number of user."""
    fave_number = get_stored_number()
    if fave_number:
        print("I know your favorite number! It's " + fave_number + "!")
    else:
        fave_number = get_new_number()
        print("I'll remember your favorite number!")

show_number()
