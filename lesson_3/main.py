# class BankAccount:
#     def __init__(self, owner, balance, pin):
#         self.owner = owner
#         self._balance = balance
#         self.__pin = pin
#
#     def show_balance(self):
#         return f"Balance: {self._balance}"
#
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#
#     def get_pin(self):
#         return self.__pin
#
#     def check_pin(self, pin):
#         return self.__pin == pin
#
# account = BankAccount("John", 20000, 117)
# print(account.show_balance())
# account.deposit(500)
# print(account.show_balance())
#
# print(account.get_pin())
# print(account.check_pin(1177))
# print(account.check_pin(117))


# class AirCon:
#     def __init__(self):
#         self.__temperature = 25
#
#     @property
#     def temperature(self):
#         return self.__temperature
#
#     @temperature.setter
#     def temperature(self, value):
#         if 16 <= value <= 30:
#             self.__temperature = value
#         else:
#             raise ValueError("Temperature must be between 16 and 30")
#
# ac = AirCon()
# print(ac.temperature)
#
# ac.temperature = 29
# print(ac.temperature)


# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#
# class Dog(Animal):
#     def sound(self):
#         return "Woof"
#
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
#
# c = Cat()
# print(c.sound())
#
# d = Dog()
# print(d.sound())

"""  Task  """

from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, hp):
        self.name = name
        self.__hp = hp

    @abstractmethod
    def attack(self):
        pass

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value > 0:
            self.__hp = value
        else:
            print("Здоровье не может быть меньше 0")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} получил урон {damage}!")

class Warrior(Character):
    def attack(self):
        print(f"{self.name} ударил мечом!")

class Mage(Character):
    def attack(self):
        print(f"{self.name} использовал заклинание!")

w = Warrior("Artur", 100)
print(w.hp)
w.take_damage(20)
print(w.hp)
w.take_damage(20)
print(w.hp)

m = Mage("Jony", 100)
print(m.hp)
m.take_damage(20)
print(m.hp)
m.take_damage(40)
print(m.hp)



