#!/usr/bin/env python
# users.py: Exercise 9-3
# 25 Aug 2018 | fjgl
class User():
    """Simulate a User with different information in its profile."""
    def __init__(self, first_name, last_name, **user_info):
        """Initializes first and last name of user."""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + ' ' + last_name
        self.user_info = user_info

    def describe_user(self):
        """Display a summary of user's information."""
        print("\nFirst Name: " + self.first_name.title())
        print("Last Name: " + self.last_name.title())
        for key, value in self.user_info.items():
            print(key.title() + ": " + value.title())

    def greet_user(self):
        """Display a greeting to the user."""
        print("\nHello, " + self.full_name.title() + "!")

user1 = User('albert', 'einstein',
             location='princeton',
             field='physics')
user1.describe_user()
user1.greet_user()

user2 = User('alan', 'turing',
             location='london',
             field='computer science')
user2.describe_user()
user2.greet_user()
