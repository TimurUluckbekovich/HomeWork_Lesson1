""" Принципы ООП: """

"""  Наследование  """
class Animal:
    def eat(self):
        print("Животное ест")
    def breath(self):
        print("Животное дышит")

class Cat(Animal):
    def meow(self):
        print("Кот мяукает")

c = Cat()
c.eat()
c.breath()
c.meow()

class Dog(Animal):
    def gav(self):
        print("Собака гавкает")

d = Dog()
d.eat()
d.breath()
d.gav()