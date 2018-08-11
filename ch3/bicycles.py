#!/usr/bin/env python
# bicycles.py: Accessing elements in a list.
# 11 Aug 2018 | fjgl
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(bicycles)
print(bicycles[1].title())
print(bicycles[2])

# access 1st element from the right
print(bicycles[-1])
print(message)
