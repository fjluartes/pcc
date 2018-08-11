#!/usr/bin/env python
# names_list.py: Exercises 3-1 to 3-3.
# 11 Aug 2018 | fjgl
# 3-1. Names, 3-2. Greetings
friends = ['Jamie Zawinski', 'Brad Fitzpatrick', 'Brendan Eich', 'Peter Norvig']
for name in friends:
    message = "Hello, " + name + "!"
    print(message)

# 3-3. Your own list
cars = ['Nissan', 'BMW', 'Subaru', 'Mazda', 'Tesla']
for car in cars:
    message = "I would like to own a " + car + "."
    print(message)
