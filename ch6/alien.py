#!/usr/bin/env python
# alien.py: simple dictionary
# 17 Aug 2018 | fjgl
#alien = {} # empty dictionary
alien_0 = {'color': 'green', 'points': 5}
#alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#print("Original x-position: " + str(alien_0['x_position']))

# adding new key-value pairs
#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)

# modifying values in a dictionary
#alien_0 = {'color': 'green'}
#print("The alien is " + alien_0['color'] + ".")
#alien_0 = {'color': 'yellow'}
#print("The alien is now " + alien_0['color'] + ".")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
#if alien_0['speed'] == 'slow':
#    x_increment = 1
#elif alien_0['speed'] == 'medium':
#    x_increment = 2
#else:
#    # This must be a fast alien.
#    x_increment = 3

# The new position is the old position plus the increment.
#alien_0['x_position'] = alien_0['x_position'] + x_increment
#print("New x-position: " + str(alien_0['x_position']))

# Removing key-value pairs
print(alien_0)
del alien_0['points']
print(alien_0)
