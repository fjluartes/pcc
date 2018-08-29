#!/usr/bin/env python
# admin.py: Exercise 9-7, 9-8, 9-11
# 29 Aug 2018 | fjgl
from users import User

# 9-8. Privileges
"""A set of classes to represent admin user and privileges."""
class Privileges():
    """Simple model of privileges of an admin."""
    def __init__(self, user, *list_privileges):
        """Initialize privileges attributes."""
        self.user = user
        self.privileges = list_privileges

    def show_privileges(self):
        """Display the list of admin privileges."""
        print("\nPrivileges available to " + self.user.title() + ":")
        for item in self.privileges:
            print(item.title())
        
        
class Admin(User):
    """Simulates an administrator user."""
    def __init__(self, first_name, last_name, **user_info):
        """Initializes attributes from parent class."""
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Privileges(self.full_name, 'add user', 'add post')
        
