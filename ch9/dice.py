#!/usr/bin/env python
# dice.py: Exercise 9-14
# 29 Aug 2018 | fjgl
from random import randint

class Die():
    """A class to simulate a n-sided dice."""
    def __init__(self, sides=6):
        """Initialize parameters."""
        self.sides = sides

    def roll_die(self):
        """Roll dice."""
        roll = randint(1, self.sides)
        print(str(roll))

num_sides = 10
die = Die()
die_10 = Die(10)
die_20 = Die(20)

print("\nRoll 6-sided die:")
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()

print("\nRoll " + str(num_sides) + "-sided die:")
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()

num_sides = 20
print("\nRoll " + str(num_sides) + "-sided die:")
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
