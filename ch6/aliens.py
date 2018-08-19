#!/usr/bin/env python
# aliens.py: nesting (list of dictionaries)
# 19 Aug 2018 | fjgl
#alien_0 = {'color': 'green', 'points': 5}
#alien_1 = {'color': 'yellow', 'points': 10}
#alien_2 = {'color': 'red', 'points': 15}
#aliens = [alien_0, alien_1, alien_2]
#for alien in aliens:
#    print(alien)

# Make an empty list then store 30 aliens
aliens = []
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# change values of the first 3 aliens
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens are created
print("Total number of aliens: " + str(len(aliens)))
