#!/usr/bin/env python
# name_function.py: testing a function
# 4 Sep 2018 | fjgl
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
