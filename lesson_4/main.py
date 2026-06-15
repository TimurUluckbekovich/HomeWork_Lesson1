"""  Magic method  """
# __init__
# __str__

class User:
    def __init__(self, name):
        self.name = name

user1 = User("Timur")
print(user1.name)