#!/usr/bin/env python
# sandwiches.py: Exercise 8-12
# 24 Aug 2018 | fjgl
def make_sandwich(*items):
    """Prints the items a person wants on a sandwich."""
    print("\nHere are the ingredients you want on your sandwich:")
    for item in items:
        print(item)

make_sandwich('lettuce')
make_sandwich('ham', 'cheese')
make_sandwich('lettuce', 'tomato', 'chicken')
