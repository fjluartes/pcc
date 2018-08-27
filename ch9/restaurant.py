#!/usr/bin/env python
# restaurant.py: Exercise 9-1, 9-2, 9-4, 9-6
# 25 Aug 2018 | fjgl
class Restaurant():
    """A restaurant class with a description method and open method."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the name and type of restaurant."""
        print("\nName: " + self.restaurant_name.title())
        print("Cuisine Type: " + self.cuisine_type.title())

    def open_restaurant(self):
        """Simulates opening of a restaurant."""
        print(self.restaurant_name.title() + " is now open.")

    def set_number_served(self, num_of_customers):
        """Set number of customers served."""
        self.number_served = num_of_customers

    def increment_number_served(self, customers):
        """Increment number of customers served"""
        self.number_served += customers

class IceCreamStand(Restaurant):
    """A simple model of an ice cream stand based on restaurant class."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing the parent class attributes."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_available_flavors(self, *flavors):
        """Add flavors available for sale in the ice cream stand."""
        self.flavors = flavors

    def display_flavors(self):
        """Display the flavors available at the ice cream stand."""
        print("Flavors available for today:")
        for flavor in self.flavors:
            print(flavor.title())
        
# 9-1. Restaurant
#restaurant = Restaurant('ooma', 'japanese')
#restaurant.describe_restaurant()
#restaurant.open_restaurant()

# 9-2. Three Restaurants
#res1 = Restaurant('mendokoro ramenba', 'japanese')
#res2 = Restaurant('buffalo wings n things', 'tex mex')
#res3 = Restaurant('mesa', 'filipino')
#res1.describe_restaurant()
#res2.describe_restaurant()
#res3.describe_restaurant()

# 9-4. Number Served
#print("Number of customers served: " +
#      str(restaurant.number_served))
#restaurant.set_number_served(20)
#print("Number of customers served: " +
#      str(restaurant.number_served))
#restaurant.increment_number_served(3)
#print("Number of customers served: " +
#      str(restaurant.number_served))

# 9-6. Ice Cream Stand
my_ice_cream_stand = IceCreamStand('dairy queen', 'soft serve')
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.add_available_flavors('chocolate', 'vanilla')
my_ice_cream_stand.display_flavors()
