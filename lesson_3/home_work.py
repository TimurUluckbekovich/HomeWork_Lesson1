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
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} получил урон {damage}!")

class Warrior(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        print(f"{self.name} ударил мечом!")

class Mage(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        print(f"{self.name} использовал заклинание!")

w = Warrior("Артур", 100)
m = Mage("Мерлин", 100)
print("---- Битва началась! ----")
print("Здоровье игроков")
print(f"{w.name}: {w.hp}     {m.name}: {m.hp}")
m.attack()
w.take_damage(40)
print(f"{w.name}: {w.hp}     {m.name}: {m.hp}")
w.attack()
m.take_damage(60)
print(f"{w.name}: {w.hp}     {m.name}: {m.hp}")



