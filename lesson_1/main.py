# st = "33"
# print(st)
# print(id(st))
# print(hash(st))
# st = st + "44"
# print(st)
# print(id(st))
# print(hash(st))


# class MyClass:
#     pass
#
# obj = MyClass()
# print(obj)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'{self.name} is {self.age} years old.')
#
# student1 = Student("John", 25)
# student1.info()

# class MyGroup:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         return f'  Name: {self.name},     Age: {self.age}'
#
# group44 = [
#     MyGroup("John", 25),
#     MyGroup("Bob", 17),
#     MyGroup("Alex", 22),
#     MyGroup("Monika", 20),
# ]
#
# group33 = [
#     MyGroup("Sam", 24),
#     MyGroup("Karl", 15),
#     MyGroup("James", 18),
#     MyGroup("Anna", 23),
# ]
#
# print("Group 44:")
# for student in group44:
#     print(student.info())
#
# print("Group 33:")
# for student in group33:
#     print(student.info())

class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def info(self):
        return f"""
            Name: {self.name}
            Age: {self.age}
            Breed: {self.breed}
        """
    # def set_age(self, age):
    #     self.age = age

dog = Animal("Dog", 3, "Golden Retriever")
print(dog.info())