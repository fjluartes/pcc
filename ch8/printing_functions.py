#!/usr/bin/env python
# printing_functions.py: modifying a list in a function, Exercise 8-15
# 24 Aug 2018 | fjgl
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

# pass a copy of the list in the function (keep original list)
# function_name(list_name[:])
# def print_models(unprinted_designs[:], completed_models):

def show_completed_models(completed_models):
    """Display all completed models."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

