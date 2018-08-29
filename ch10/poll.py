#!/usr/bin/env python
# poll.py: Exercise 10-5
# 29 Aug 2018 | fjgl
filename = 'poll.txt'
poll_active = True
responses = {}
with open(filename, 'a') as file_object:
    while poll_active:
        name = input("What is your name? ")
        reason = input("Why do you like programming? ")
        responses[name] = reason
        stop = input("\nWould you let another person respond? (yes/no) ")
        if stop.lower() == 'no':
            poll_active = False

    print("\n--- Poll Results ---")
    for name, reason in responses.items():
        file_object.write(name.title() + ": " + reason + ".\n")
        print(name.title() + ": " + reason + ".")
