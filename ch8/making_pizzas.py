#!/usr/bin/env python
# making_pizzas.py: Importing an entire module
# 24 Aug 2018 | fjgl
# import pizza.py to use make_pizza function
# import module_name | module_name.function_name()
#import pizza
#pizza.make_pizza(16, 'pepperoni')
#pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# importing specific functions
# from module_name import function_name | function_name()
#from pizza import make_pizza
#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# using 'as' to give a function an alias
# from module_name import function_name as alias | alias()
#from pizza import make_pizza as mp
#mp(16, 'pepperoni')
#mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# using 'as' to give a module an alias
# import module_name as alias | alias.function_name()
#import pizza as p
#p.make_pizza(16, 'pepperoni')
#p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# import all functions from a module
# from module_name import *
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
