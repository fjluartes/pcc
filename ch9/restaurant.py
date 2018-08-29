#!/usr/bin/env python
# restaurant.py: Exercise 9-1, 9-2, 9-4, 9-6
# 25 Aug 2018 | fjgl
"""A set of classes to represent kinds of restaurants."""
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
