#!/usr/bin/env python
# printing_models.py: modifying a list in a function, Exercise 8-15
# 22 Aug 2018 | fjgl
import printing_functions as pf
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

