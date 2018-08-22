#!/usr/bin/env python
# pets.py: positional arguments
# 22 Aug 2018 | fjgl
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# positional arguments (order of arguments matter)
#describe_pet('hamster', 'harry')
#describe_pet('dog', 'willie')

# keyword arguments (order doesn't matter because of keywords)
#describe_pet(animal_type='hamster', pet_name='harry')
#describe_pet(pet_name='harry', animal_type='hamster')

# default values: animal_type='dog'
# parameters without default values should be defined first
#describe_pet(pet_name='willie')
#describe_pet('willie')
# default value is ignored
#describe_pet(pet_name='harry', animal_type='hamster')

# equivalent function calls
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
