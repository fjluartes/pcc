#!/usr/bin/env python
# restaurant.py: Exercise 9-10
# 29 Aug 2018 | fjgl
from restaurant import Restaurant, IceCreamStand

# 9-1. Restaurant
restaurant = Restaurant('ooma', 'japanese')
restaurant.describe_restaurant()
restaurant.open_restaurant()

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
