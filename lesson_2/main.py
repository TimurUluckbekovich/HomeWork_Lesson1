""" Принципы ООП: """

"""  Наследование  """
# class Animal:
#     def eat(self):
#         print("Животное ест")
#     def breath(self):
#         print("Животное дышит")
#
# class Cat(Animal):
#     def meow(self):
#         print("Кот мяукает")
#
# c = Cat()
# c.eat()
# c.breath()
# c.meow()
#
# class Dog(Animal):
#     def gav(self):
#         print("Собака гавкает")
#
# d = Dog()
# d.eat()
# d.breath()
# d.gav()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        return f"Name {self.name}, Email: {self.email}"

class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def teach(self):
        return f"{self.name} teaches {self.subject}"

class Admin(User):
    def ban_user(self, user_name):
        return f"{self.name} banned {user_name.name}"

t = Teacher("Alice", "alice@gmail.com", "history")
b = Admin("Bob", "bob@gmail.com")

print(t.get_info())
print(t.teach())
print(b.get_info())
print(b.ban_user(t))


