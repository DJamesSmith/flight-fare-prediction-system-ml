# @dataclass module is introduced in Python 3.7 as a utility tool to make structured classes specially for storing data.
# These classes hold certain properties and functions to deal specifically with the data and its representation.

# Advantages of using @dataclass:
# 1. Less boilerplate.
# 2. Automatically generates __init__(), __repr__(), and __eq__().
# 4. Without a __init__() constructor, the class accepted values and assigned it to appropriate variables.
# 5. The output of printing object is a neat representation of the data present in it, without any explicit function coded to do this.
#    That means it has a modified __repr__() function.

from dataclasses import dataclass
from models.user import User

@dataclass
class Admin(User):
    def display_admin_details(self):
        self.display_details()
        print("Privileges : Administrator")

# Inheritance used:
# User
#    ▲
# Admin