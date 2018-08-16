#!/usr/bin/env python
# hello_admin.py: Exercises 5-8, 5-9
# 16 Aug 2018 | fjgl
#users = ['admin', 'gon', 'killua', 'kurapika', 'leorio']
users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user + ", would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again.")
else:
    print("We need to find some users!")
