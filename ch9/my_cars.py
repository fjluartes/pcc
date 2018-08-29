#!/usr/bin/env python
# my_cars.py: importing multiple classes
# 28 Aug 2018 | fjgl
#from car import Car, ElectricCar
#import car
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

