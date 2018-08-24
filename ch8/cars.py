#!/usr/bin/env python
# cars.py: Exercise 8-14
# 24 Aug 2018 | fjgl
def make_car(manuf, model, **car_info):
    """Build a dictionary containing all information about a car."""
    car = {}
    car['manufacturer'] = manuf
    car['model_name'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car1 = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car1)
car2 = make_car('toyota', 'prius', color='white', tow_package=True)
print(car2)
