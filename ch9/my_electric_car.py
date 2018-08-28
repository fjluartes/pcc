#!/usr/bin/env python
# my_electric_car.py: importing classes
# 28 Aug 2018 | fjgl
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
