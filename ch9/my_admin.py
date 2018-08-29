#!/usr/bin/env python
# my_admin.py: Exercise 9-7, 9-8, 9-11, 9-12
# 29 Aug 2018 | fjgl
from admin import Admin, Privileges

# 9-7. Admin
admin = Admin('admin', 'user')
admin.describe_user()
admin.privileges.show_privileges()
