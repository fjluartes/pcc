#!/usr/bin/env python
# user_profile.py: using arbitrary keyword arguments
# 23 Aug 2018 | fjgl
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# **user_info creates an empty dictionary and store the
#   incoming key-value pairs
