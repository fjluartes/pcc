#!/usr/bin/env python
# restaurant.py: Exercise 9-1, 9-2
# 25 Aug 2018 | fjgl
class Restaurant():
    """A restaurant class with a description method and open method."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the name and type of restaurant."""
        print("\nName: " + self.restaurant_name.title())
        print("Cuisine Type: " + self.cuisine_type.title())

    def open_restaurant(self):
        """Simulates opening of a restaurant."""
        print(self.restaurant_name.title() + " is now open.")

# 9-1. Restaurant
restaurant = Restaurant('ooma', 'japanese')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants
res1 = Restaurant('mendokoro ramenba', 'japanese')
res2 = Restaurant('buffalo wings n things', 'tex mex')
res3 = Restaurant('mesa', 'filipino')

res1.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()