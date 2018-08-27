#!/usr/bin/env python
# users.py: Exercise 9-3, 9-5, 9-7, 9-8
# 25 Aug 2018 | fjgl
class User():
    """Simulate a User with different information in its profile."""
    def __init__(self, first_name, last_name, **user_info):
        """Initializes first and last name of user."""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + ' ' + last_name
        self.user_info = user_info
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of user's information."""
        print("\nFirst Name: " + self.first_name.title())
        print("Last Name: " + self.last_name.title())
        for key, value in self.user_info.items():
            print(key.title() + ": " + value.title())

    def greet_user(self):
        """Display a greeting to the user."""
        print("\nHello, " + self.full_name.title() + "!")

    def increment_login_attempts(self):
        """Increment the number of login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0

# 9-8. Privileges
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
        self.privileges = Privileges(self.full_name, 'add user',
                                     'update user', 'add post')
        
# 9-3. Users
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

# 9-5. Login Attempts
#user1.increment_login_attempts()
#print("Num of login attempts: " + str(user1.login_attempts))
#user1.increment_login_attempts()
#print("Num of login attempts: " + str(user1.login_attempts))
#user1.increment_login_attempts()
#print("Num of login attempts: " + str(user1.login_attempts))
#user1.reset_login_attempts()
#print("Num of login attempts: " + str(user1.login_attempts))

# 9-7. Admin
admin = Admin('admin', 'user')
admin.describe_user()
admin.privileges.show_privileges()
