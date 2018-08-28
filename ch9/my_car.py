#!/usr/bin/env python
# my_car.py: importing classes
# 28 Aug 2018 | fjgl
from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

