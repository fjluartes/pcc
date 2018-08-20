#!/usr/bin/env python
# cities.py: using break to exit a loop
# 20 Aug 2018 | fjgl
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
