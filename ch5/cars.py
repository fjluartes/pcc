#!/usr/bin/env python
# cars.py: if statements example
# 13 Aug 2018 | fjgl
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
