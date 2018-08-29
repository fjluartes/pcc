#!/usr/bin/env python
# electric_car.py: Inheritance, Exercise 9-9
# 27 Aug 2018 | fjgl
# importing a module into a module
from car import Car

# Instances as attributes
class Battery():
    """A simple attempt to model a battery of an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")    

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    # 9-9. Battery Upgrade
    def upgrade_battery(self):
        """Upgrade battery to 85 kWh."""
        if self.battery_size != 85:
            self.battery_size = 85
        
# Inheritance
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    # overriding a method
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
        
#my_tesla = ElectricCar('tesla', 'model s', 2016)
#print(my_tesla.get_descriptive_name())
#my_tesla.battery.describe_battery()
#my_tesla.fill_gas_tank()
#my_tesla.battery.get_range()
#my_tesla.battery.upgrade_battery()
#my_tesla.battery.describe_battery()
#my_tesla.battery.get_range()

#my_car = Car('subaru', 'outback', 2015)
#print(my_car.get_descriptive_name())
#my_car.fill_gas_tank()
