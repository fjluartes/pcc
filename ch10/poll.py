#!/usr/bin/env python
# poll.py: Exercise 10-5
# 29 Aug 2018 | fjgl
filename = 'poll.txt'
poll_active = True
responses = {}
with open(filename, 'a') as file_object:
    while poll_active:
        print("\nEnter 'q' to quit poll")
        name = input("What is your name? ")
        if name == 'q':
            poll_active = False
        else:
            reason = input("Why do you like programming? ")
            responses[name] = reason

    print("--- Poll Results ---")
    for name, response in responses.items():
        file_object.write(name.title() + ": " + reason + ".\n")
        print(name.title() + ": " + reason + "."
