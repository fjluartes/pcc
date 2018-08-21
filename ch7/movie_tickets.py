#!/usr/bin/env python
# movie_tickets.py: Exercise 7-5
# 21 Aug 2018 | fjgl
prompt = "\nPlease enter your age:"
prompt += "\nEnter 'quit' to finish. "

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free.")
        elif age <= 12:
            print("Your ticket costs $10.")
        elif age > 12:
            print("Your ticket costs $15.")
